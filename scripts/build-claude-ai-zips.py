#!/usr/bin/env python3
"""Bundle the skills into zips that claude.ai accepts as ONE Skill each.

claude.ai takes one zip per Skill, uploaded by hand, and treats every SKILL.md
it finds in the zip as a separate Skill. So a bundle has to contain exactly one
SKILL.md at the zip root; the skills it bundles ride along as plain .md files
under reference/, which the router SKILL.md points at and Claude reads on demand
(progressive disclosure). Naming them anything other than SKILL.md is what keeps
the importer from unpacking them into separate uploads.

Builds two shapes:
  dist/claude-ai/all-in-one/designer-skills.zip   1 upload,  all 107 skills
  dist/claude-ai/by-collection/<name>.zip         9 uploads, one per collection

Re-run after editing any SKILL.md.
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

# claude.ai upload limits that actually bite.
MAX_FILES = 200
MAX_DESC = 1024

FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
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


def use_for(desc, limit=110):
    """First sentence of a skill description, trimmed for an index table."""
    s = re.split(r"(?<=[.!?])\s", desc.strip())[0].rstrip(".")
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + "…"


def load(collection):
    src = ROOT / collection
    plugin = json.loads((src / ".claude-plugin" / "plugin.json").read_text())
    skills = [(p.parent.name, frontmatter(p), p)
              for p in sorted((src / "skills").glob("*/SKILL.md"))]
    cmds = [(p.stem, frontmatter(p), p)
            for p in sorted((src / "commands").glob("*.md"))] if (src / "commands").is_dir() else []
    return plugin, skills, cmds


def clamp(desc):
    if len(desc) <= MAX_DESC:
        return desc
    return desc[:MAX_DESC - 4].rsplit(", ", 1)[0] + "."


def write_zip(path, skill_name, router, files):
    """files: list of (source_path, path_inside_skill_folder)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{skill_name}/SKILL.md", router)
        for src, rel in files:
            z.write(src, f"{skill_name}/{rel}")
        names = z.namelist()

    skill_mds = [n for n in names if n.endswith("SKILL.md")]
    assert skill_mds == [f"{skill_name}/SKILL.md"], \
        f"{skill_name}: zip must hold exactly one SKILL.md, found {skill_mds}"
    assert len(names) < MAX_FILES, f"{skill_name}: {len(names)} files exceeds the {MAX_FILES} cap"
    return len(names), path.stat().st_size


def build_collection(collection):
    plugin, skills, cmds = load(collection)
    desc = clamp(f"{plugin['description']} Covers: "
                 f"{', '.join(s for s, _, _ in skills)}.")

    body = [
        "---", f"name: {collection}", f"description: {desc}", "---",
        f"# {display_name(collection)}", "", plugin["description"], "",
        "## How to use this skill", "",
        f"This bundles {len(skills)} focused skills as reference files. Match the "
        "request to a row below, then read that file before answering — the table is "
        "only an index, the guidance itself lives in the files.", "",
        "| Skill | File | Use it for |", "| --- | --- | --- |",
    ]
    files = []
    for slug, fm, path in skills:
        body.append(f"| `{slug}` | `reference/{slug}.md` | {use_for(fm.get('description', ''))} |")
        files.append((path, f"reference/{slug}.md"))

    if cmds:
        body += ["", "## Multi-step workflows", "",
                 "Each chains several skills above into one end-to-end process. Read the "
                 "file when the request matches the whole workflow, not a single skill.", ""]
        for slug, fm, path in cmds:
            body.append(f"- `workflows/{slug}.md` — {use_for(fm.get('description', slug))}")
            files.append((path, f"workflows/{slug}.md"))

    body += ["", "## Attribution", "",
             f"From the Designer Skills suite by {plugin['author']['name']} "
             f"({plugin['homepage']}), MIT licensed.", ""]

    n, size = write_zip(OUT / "by-collection" / f"{collection}.zip",
                        collection, "\n".join(body), files)
    print(f"  {collection:22} {len(skills):>3} skills  {n:>3} files  {size / 1024:>6.1f} KB")


def build_all_in_one():
    name = "designer-skills"
    groups = [(c, *load(c)) for c in COLLECTIONS]
    total = sum(len(s) for _, _, s, _ in groups)

    desc = clamp(
        "Complete design practice toolkit — user research, design systems, UX "
        "strategy, UI craft, interaction design, prototyping and testing, design "
        "ops, and visual critique. Use for any design task: personas, journey maps, "
        "usability tests, design tokens, component specs, information architecture, "
        "user flows, colour systems, typography scales, layout grids, responsive and "
        "dark mode, accessibility, micro-interactions, animation, error states, "
        "design critique, and design team process."
    )

    body = [
        "---", f"name: {name}", f"description: {desc}", "---",
        "# Designer Skills", "",
        f"{total} design skills across nine areas of practice, plus end-to-end workflows.", "",
        "## How to use this skill", "",
        "Match the request to a row in the tables below, then read that reference file "
        "before answering. The tables are only an index — the actual guidance lives in "
        "the files, so read the relevant one rather than working from the summary. Read "
        "more than one when a request spans areas (a screen design might pull "
        "`layout-grid`, `color-system`, and `visual-hierarchy` together).", "",
        "If nothing matches closely, answer normally rather than forcing a poor fit.", "",
    ]

    files = []
    for collection, plugin, skills, cmds in groups:
        body += [f"## {display_name(collection)}", "",
                 "| Skill | File | Use it for |", "| --- | --- | --- |"]
        for slug, fm, path in skills:
            rel = f"reference/{collection}/{slug}.md"
            body.append(f"| `{slug}` | `{rel}` | {use_for(fm.get('description', ''), 72)} |")
            files.append((path, rel))
        body.append("")
        for slug, fm, path in cmds:
            files.append((path, f"workflows/{collection}/{slug}.md"))

    body += ["## Multi-step workflows", "",
             "Each chains several skills into one end-to-end process. Read the file when "
             "the request matches a whole workflow rather than a single skill.", ""]
    for collection, _, _, cmds in groups:
        if cmds:
            body.append(f"- **{display_name(collection)}** — "
                        + ", ".join(f"`workflows/{collection}/{s}.md`" for s, _, _ in cmds))

    body += ["", "## Attribution", "",
             "From the Designer Skills suite by MC Dean "
             "(https://github.com/Owl-Listener/designer-skills), MIT licensed.", ""]

    router = "\n".join(body)
    n, size = write_zip(OUT / "all-in-one" / f"{name}.zip", name, router, files)
    print(f"  {name:22} {total:>3} skills  {n:>3} files  {size / 1024:>6.1f} KB"
          f"   router ~{len(router) // 4} tokens")


print("all-in-one (1 upload):")
build_all_in_one()
print("\nby-collection (9 uploads):")
for c in COLLECTIONS:
    build_collection(c)
