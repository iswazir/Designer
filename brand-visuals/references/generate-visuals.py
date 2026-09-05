#!/usr/bin/env python3
"""
generate-visuals.py

Prompt-to-image runner for rough storyboard frames and mock plates.
Standard library only. Calls the Gemini image API over REST.

Reads:   references/prompts.json          (manifest: style_prefix, negative, concepts[].frames[])
         inputs/references/*.png|jpg      (up to 3 attached to every Gemini call as visual direction)
Writes:  outputs/YYYY-MM-DD/<concept>/frame-<id>-v<version>.png
         outputs/YYYY-MM-DD/<concept>/index.md   (receipt: one row per frame, human columns blank)

Env:     GEMINI_API_KEY   (required unless --dry-run or --list-models)
         IMAGE_MODEL      (optional; default gemini-2.5-flash-image)

Usage:
  python3 references/generate-visuals.py --list-models
  python3 references/generate-visuals.py --dry-run
  python3 references/generate-visuals.py --concept say-the-thing [--frames 01,04]
  python3 references/generate-visuals.py --all
  python3 references/generate-visuals.py --all --model imagen-4.0-generate-001
"""

import argparse
import base64
import datetime as dt
import hashlib
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "references", "prompts.json")
REF_DIR = os.path.join(ROOT, "inputs", "references")
OUT_DIR = os.path.join(ROOT, "outputs")
API = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_MODEL = "gemini-2.5-flash-image"
MAX_REFS = 3


def load_env():
    """Minimal .env loader so the script has no dependencies."""
    path = os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def api_key():
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key:
        sys.exit("GEMINI_API_KEY is not set. Copy .env.example to .env and add your key.")
    return key


def http_json(url, body=None, key=None, method=None, timeout=180):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method or ("POST" if data else "GET"))
    req.add_header("Content-Type", "application/json")
    if key:
        req.add_header("x-goog-api-key", key)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def list_models(key):
    out = http_json(f"{API}/models?pageSize=200", key=key)
    names = [m["name"].split("/", 1)[1] for m in out.get("models", [])]
    image_like = [n for n in names if "image" in n or "imagen" in n]
    print("Image-capable models visible to this key:")
    for n in image_like:
        print("  ", n)
    if not image_like:
        print("  (none matched 'image'; full list follows)")
        for n in names:
            print("  ", n)


def load_refs():
    if not os.path.isdir(REF_DIR):
        return []
    files = sorted(
        f for f in os.listdir(REF_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    )[:MAX_REFS]
    parts = []
    for f in files:
        p = os.path.join(REF_DIR, f)
        mime = mimetypes.guess_type(p)[0] or "image/png"
        with open(p, "rb") as fh:
            parts.append({"inline_data": {"mime_type": mime, "data": base64.b64encode(fh.read()).decode()}})
    return parts


def build_prompt(manifest, frame):
    return (
        f"{manifest['style_prefix']}\n\n"
        f"Frame: {frame['prompt']}\n\n"
        f"Avoid: {manifest['negative']}"
    )


def call_gemini(key, model, prompt, aspect, ref_parts):
    body = {
        "contents": [{"parts": ref_parts + [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect},
        },
    }
    out = http_json(f"{API}/models/{model}:generateContent", body, key)
    for cand in out.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            if "inlineData" in part:
                return base64.b64decode(part["inlineData"]["data"]), part["inlineData"].get("mimeType", "image/png")
            if "inline_data" in part:
                return base64.b64decode(part["inline_data"]["data"]), part["inline_data"].get("mime_type", "image/png")
    raise RuntimeError(f"No image in response: {json.dumps(out)[:600]}")


def call_imagen(key, model, prompt, aspect):
    body = {
        "instances": [{"prompt": prompt}],
        "parameters": {"sampleCount": 1, "aspectRatio": aspect, "personGeneration": "allow_adult"},
    }
    out = http_json(f"{API}/models/{model}:predict", body, key)
    preds = out.get("predictions", [])
    if not preds or "bytesBase64Encoded" not in preds[0]:
        raise RuntimeError(f"No image in response: {json.dumps(out)[:600]}")
    return base64.b64decode(preds[0]["bytesBase64Encoded"]), preds[0].get("mimeType", "image/png")


def generate(key, model, prompt, aspect, ref_parts, retries=3):
    last = None
    for attempt in range(1, retries + 1):
        try:
            if model.startswith("imagen"):
                return call_imagen(key, model, prompt, aspect)
            return call_gemini(key, model, prompt, aspect, ref_parts)
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:400]
            last = f"HTTP {e.code}: {msg}"
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(4 * attempt)
                continue
            raise RuntimeError(last)
    raise RuntimeError(last or "unknown error")


def ensure_index(path, concept, model):
    if os.path.exists(path):
        return
    with open(path, "w") as f:
        f.write(f"# Receipt: {concept['title']}\n\n")
        f.write(f"Model: `{model}`  \nRun date: {dt.date.today().isoformat()}\n\n")
        f.write("Fill in **disposition** (accept / revise / reject) and **reason** by hand. ")
        f.write("A rejected frame with a specific reason is the strongest Slide 6 evidence.\n\n")
        f.write("| frame | version | prompt hash | output | disposition | reason |\n")
        f.write("|---|---|---|---|---|---|\n")


def append_index(path, frame, phash, outname):
    with open(path, "a") as f:
        f.write(f"| {frame['id']} | v{frame.get('version', 1)} | `{phash}` | `{outname}` |  |  |\n")


def run_concept(manifest, concept, frames_filter, model, key, dry, ref_parts):
    today = dt.date.today().isoformat()
    outdir = os.path.join(OUT_DIR, today, concept["slug"])
    os.makedirs(outdir, exist_ok=True)
    index = os.path.join(outdir, "index.md")
    if not dry:
        ensure_index(index, concept, model)

    for frame in concept["frames"]:
        if frames_filter and frame["id"] not in frames_filter:
            continue
        aspect = frame.get("aspect", concept.get("aspect", "3:2"))
        prompt = build_prompt(manifest, frame)
        phash = hashlib.sha1(prompt.encode()).hexdigest()[:10]
        outname = f"frame-{frame['id']}-v{frame.get('version', 1)}.png"
        outpath = os.path.join(outdir, outname)

        print(f"[{concept['slug']}] frame {frame['id']} v{frame.get('version', 1)} aspect {aspect} hash {phash}")
        if dry:
            print("   prompt:", frame["prompt"][:110].replace("\n", " "), "...")
            continue
        if os.path.exists(outpath):
            print("   exists, skipping (bump version to regenerate)")
            continue
        try:
            img, mime = generate(key, model, prompt, aspect, ref_parts)
        except Exception as e:
            print("   FAILED:", e)
            with open(index, "a") as f:
                f.write(f"| {frame['id']} | v{frame.get('version', 1)} | `{phash}` | FAILED: {str(e)[:80]} | reject | generation error |\n")
            continue
        with open(outpath, "wb") as f:
            f.write(img)
        append_index(index, frame, phash, outname)
        print("   saved", os.path.relpath(outpath, ROOT))
        time.sleep(1.5)


def main():
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--concept", help="concept slug from prompts.json")
    ap.add_argument("--frames", help="comma-separated frame ids, e.g. 01,04")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="print prompts, call nothing")
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--model", default=os.environ.get("IMAGE_MODEL", DEFAULT_MODEL))
    args = ap.parse_args()

    with open(MANIFEST) as f:
        manifest = json.load(f)

    if args.list_models:
        list_models(api_key())
        return

    if not (args.concept or args.all):
        ap.error("pass --concept <slug> or --all (or --dry-run with either)")

    key = None if args.dry_run else api_key()
    ref_parts = [] if args.dry_run else load_refs()
    if not args.dry_run:
        print(f"model: {args.model}   reference images attached: {len(ref_parts)}")

    frames_filter = set(args.frames.split(",")) if args.frames else None
    for concept in manifest["concepts"]:
        if args.all or concept["slug"] == args.concept:
            run_concept(manifest, concept, frames_filter, args.model, key, args.dry_run, ref_parts)

    if not args.all and args.concept and not any(c["slug"] == args.concept for c in manifest["concepts"]):
        sys.exit(f"unknown concept '{args.concept}'. slugs: {[c['slug'] for c in manifest['concepts']]}")


if __name__ == "__main__":
    main()
