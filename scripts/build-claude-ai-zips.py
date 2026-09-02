#!/usr/bin/env python3
"""Bundle each plugin collection into one zip that claude.ai accepts as a Skill.

claude.ai takes one zip per Skill, with the skill folder as the zip root and a
SKILL.md at its top. Uploading all 107 skills individually would mean 107 trips
through the upload dialog and ~10k tokens of always-loaded metadata, so instead
each collection becomes a single Skill: a router SKILL.md that lists what the
collection covers, with the original skills kept alongside it as files Claude
reads on demand (progressive disclosure).

Writes dist/claude-ai/<collection>.zip. Re-run after editing any SKILL.md.
"""

import json
import pathlib
import re
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "claude-ai"

COLLECTIONS = [
    "design-research", "design-systems", "ux-strategy", "ui-design",
    "interaction-design", "prototyping-testing", "design-ops",
    "designer-toolkit", "visual-critique",
]

FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

# Words the generic title-caser would mangle ("Ui Design", "Ux Strategy").
ACRONYMS = {"ui": "UI", "ux": "UX", "ops": "Ops"}


def display_name(slug):
    return " ".join(ACRONYMS.get(w, w.title()) for w in slug.split("-"))


def frontmatter(path):
    m = FM.match(path.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"no frontmatter: {path}")
    out, key = {}, None
    for line in m.group(1).splitlines():
        if re.match(r"^\w[\w-]*:", line):
            key, _, val = line.partition(":")
            out[key.strip()] = val.strip()
        elif key:
            out[key] += " " + line.strip()
    return out


def first_sentence(text):
    return re.split(r"(?<=[.!?])\s", text.strip())[0]


def build(name):
    src = ROOT / name
    plugin = json.loads((src / ".claude-plugin" / "plugin.json").read_text())

    skills = []
    for skill_md in sorted((src / "skills").glob("*/SKILL.md")):
        fm = frontmatter(skill_md)
        skills.append((skill_md.parent.name, fm.get("description", "")))

    # claude.ai caps description at 1024 chars; keep the topic list inside it.
    topics = ", ".join(s for s, _ in skills)
    desc = f"{plugin['description']} Covers: {topics}."
    if len(desc) > 1024:
        desc = desc[:1020].rsplit(", ", 1)[0] + "."

    lines = [
        "---",
        f"name: {name}",
        f"description: {desc}",
        "---",
        f"# {display_name(name)}",
        "",
        plugin["description"],
        "",
        "## How to use this skill",
        "",
        f"This bundles {len(skills)} focused skills. Find the one that matches the "
        "request in the table below, then read its file before answering — the table "
        "is only an index, the actual guidance lives in the linked files.",
        "",
        "| Skill | File | Use it for |",
        "| --- | --- | --- |",
    ]
    for slug, sdesc in skills:
        lines.append(f"| `{slug}` | `skills/{slug}/SKILL.md` | {first_sentence(sdesc)} |")

    commands = sorted((src / "commands").glob("*.md")) if (src / "commands").is_dir() else []
    if commands:
        lines += [
            "",
            "## Multi-step workflows",
            "",
            "These chain several of the skills above into one end-to-end process. "
            "Read the file when a request matches the whole workflow rather than a single skill.",
            "",
        ]
        for cmd in commands:
            lines.append(f"- `commands/{cmd.name}` — {first_sentence(frontmatter(cmd).get('description', cmd.stem))}")

    lines += ["", "## Attribution", "",
              f"From the Designer Skills suite by {plugin['author']['name']} "
              f"({plugin['homepage']}), MIT licensed.", ""]
    router = "\n".join(lines)

    OUT.mkdir(parents=True, exist_ok=True)
    zip_path = OUT / f"{name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{name}/SKILL.md", router)
        for f in sorted(src.rglob("*")):
            if f.is_dir() or ".claude-plugin" in f.parts:
                continue
            z.write(f, f"{name}/{f.relative_to(src)}")
        count = len(z.namelist())

    assert count < 200, f"{name}: {count} files exceeds the 200-file upload cap"
    assert len(desc) <= 1024, f"{name}: description too long"
    print(f"{name:22} {len(skills):>3} skills  {count:>3} files  {zip_path.stat().st_size / 1024:>6.1f} KB")


for c in COLLECTIONS:
    build(c)
print(f"\nWrote {len(COLLECTIONS)} zips to {OUT.relative_to(ROOT)}/")
