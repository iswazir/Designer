#!/usr/bin/env python3
"""Convert the Perceptual Protocols repo into one claude.ai-uploadable Skill.

github.com/Owl-Listener/perceptual-protocols ships no SKILL.md — it is a family
of markdown prompt templates and format specs meant to be pasted into a chat by
hand. This wraps the nine protocols in a router SKILL.md so Claude reaches for
the right one on its own, keeping each protocol's PROMPT.md (the instructions),
FORMAT.md/SPEC.md (the output contract), and worked examples as reference files.

The repo's PNG moodboards (13 MB of the 13.2 MB total) and its Python CLI
helpers are left out: the images are references for a human eye and the scripts
need API keys and a terminal, neither of which applies inside a Skill.

Usage: build-perceptual-protocols.py <path-to-cloned-repo>
"""

import pathlib
import re
import sys
import zipfile

SKILL = "perceptual-protocols"
OUT = pathlib.Path(__file__).resolve().parent.parent / "dist" / "claude-ai" / "all-in-one"

# Ordered as the repo's README orders them: declare intent, share vocabulary
# across modalities, weight by context, annotate the system, read existing work,
# close the loop.
PROTOCOLS = [
    ("mood", "mood.md", "Declare what the product should feel like, from visual references",
     "the user has a moodboard, screenshots, or visual references and needs to state the intended feel"),
    ("vocab", "vocab.md", "Share a vocabulary for the static qualities you mean",
     "words like warm, restrained, or dense are being used loosely and need anchoring to references"),
    ("motion", "motion.md", "Share a vocabulary for how the product should move",
     "animation, transitions, easing, or the feel of movement is being specified"),
    ("voice", "voice.md", "Specify how the brand writes — personality, register, mechanics",
     "tone of voice, copy personality, or writing style needs to be pinned down"),
    ("listen", "listen.md + sound.md", "Author a brief from audio references; share sound vocabulary",
     "music, soundtrack, sound design, or a recorded place is part of the brief"),
    ("situation", "situation.md", "Weight the qualities differently by context",
     "the same product must feel different in different contexts (calm vs. urgent, first use vs. daily)"),
    ("tokens", "tokens.md", "Annotate the design system you already have with intent",
     "a token set or design system exists and needs the reasoning behind its values recorded"),
    ("trace", "trace.md", "Read an existing UI and capture its implicit mood",
     "an existing product or screenshot needs its unstated aesthetic reverse-engineered"),
    ("critique", "critique.md", "Critique agent output against the brief",
     "generated design work needs judging against a mood, vocab, or voice brief"),
]

# PROMPT.md is the protocol itself; the rest is contract and worked examples.
KEEP = re.compile(r"\.md$")
SKIP_DIRS = {".git"}


def build(repo):
    body = [
        "---",
        f"name: {SKILL}",
        "description: >-",
        "  Capture and communicate how a design should FEEL — mood, aesthetic vocabulary,"
        " motion character, brand voice, and sound — as structured markdown briefs an agent"
        " can read. Use when a design brief is vague about feel, when words like warm,"
        " restrained, playful, or premium need anchoring to something specific, when"
        " translating a moodboard or audio reference into a written brief, when recording"
        " the intent behind design tokens, when reverse-engineering the mood of an existing"
        " UI, or when critiquing generated design work against an agreed brief.",
        "---",
        "# Perceptual Protocols",
        "",
        "Nine protocols for stating how something should feel, precisely enough that an agent "
        "can act on it. Each produces one plain markdown file that lives in the project and "
        "gets read alongside the code.",
        "",
        "## How to use this skill",
        "",
        "Pick the protocol matching the request from the table below and read its "
        "`PROMPT.md` — that file contains the actual protocol, including what to ask the "
        "user for. Read its `FORMAT.md` (or `SPEC.md`) before writing output, since the "
        "value of these files is that they follow a fixed shape other agents can parse. "
        "Read an `example-*.md` when the shape of a good result is unclear.",
        "",
        "Produce the named output file as the deliverable. Do not invent a format — follow "
        "the spec.",
        "",
        "| Protocol | Output | Reach for it when |",
        "| --- | --- | --- |",
    ]
    for slug, out, _, when in PROTOCOLS:
        body.append(f"| [`{slug}`](protocols/{slug}/PROMPT.md) | `{out}` | {when} |")

    body += [
        "",
        "## How they compose",
        "",
        "They work alone but are designed to stack, in this order:",
        "",
        "1. **Declare intent** — `mood` from visual references, `listen` from audio.",
        "2. **Share vocabulary** — `vocab` for static qualities, `motion` for movement, "
        "`voice` for writing.",
        "3. **Weight by context** — `situation`, when the feel must shift by circumstance.",
        "4. **Annotate the system** — `tokens`, once a design system exists.",
        "5. **Read existing work** — `trace`, to recover the mood a live UI already has.",
        "6. **Close the loop** — `critique`, to judge output against the brief.",
        "",
        "When several of these files already exist in a project, read all of them before "
        "generating design work — they are written to be read together.",
        "",
        "## Attribution",
        "",
        "From Perceptual Protocols by Owl-Listener "
        "(https://github.com/Owl-Listener/perceptual-protocols), MIT licensed. "
        "The PNG moodboards and Python helpers in the source repo are omitted here; "
        "clone the repo for those.",
        "",
    ]

    files = []
    for slug, *_ in PROTOCOLS:
        src = repo / f"{slug}-protocol"
        for f in sorted(src.rglob("*")):
            if f.is_dir() or not KEEP.search(f.name):
                continue
            files.append((f, f"protocols/{slug}/{f.relative_to(src)}"))
    for top in ("README.md", "TUTORIAL.md", "READING.md", "LICENSE"):
        if (repo / top).is_file():
            files.append((repo / top, f"source/{top}"))

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{SKILL}.zip"
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{SKILL}/SKILL.md", "\n".join(body))
        for src, rel in files:
            z.write(src, f"{SKILL}/{rel}")
        names = z.namelist()

    # The two limits that actually reject an upload, plus the one-Skill invariant.
    assert [n for n in names if n.endswith("SKILL.md")] == [f"{SKILL}/SKILL.md"], \
        "zip must hold exactly one SKILL.md or claude.ai splits it into separate uploads"
    assert len(names) < 200, f"{len(names)} files exceeds the 200-file cap"
    print(f"{SKILL}: {len(PROTOCOLS)} protocols, {len(names)} files, "
          f"{path.stat().st_size / 1024:.1f} KB -> {path}")


build(pathlib.Path(sys.argv[1]).resolve())
