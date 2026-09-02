#!/usr/bin/env bash
# Copy every skill in this repo into your personal Claude skills directory
# (~/.claude/skills), so they are available in any project without installing
# the plugins. Run from anywhere:
#
#   ./scripts/install-skills.sh            # install into ~/.claude/skills
#   DEST=.claude/skills ./scripts/install-skills.sh   # project-local instead
#
# Prefer `/plugin marketplace add <owner>/<repo>` if you want the commands
# (/design-screen, /color-palette, ...) as well as the skills.

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dest="${DEST:-$HOME/.claude/skills}"

mkdir -p "$dest"

count=0
while IFS= read -r skill_md; do
  skill_dir="$(dirname "$skill_md")"
  name="$(basename "$skill_dir")"
  if [ -e "$dest/$name" ]; then
    echo "skip (already exists): $name"
    continue
  fi
  cp -r "$skill_dir" "$dest/$name"
  count=$((count + 1))
done < <(find "$repo_root" -mindepth 4 -maxdepth 4 -path '*/skills/*/SKILL.md' | sort)

echo "Installed $count skill(s) into $dest"
