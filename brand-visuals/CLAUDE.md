# brand-visuals

Prompt-to-image pipeline for rough storyboard frames and mocks. Built for the IM8 Head of Content Part 3 concepts; reusable for any brand by replacing `references/style-analysis.md` and `references/prompts.json`.

## What this is for

- Rough storyboard frames for concept slides. Legible enough to judge composition, light and casting direction.
- Mock backgrounds for OOH and static units. Typography and real product packs are added afterwards in Figma.
- An AI receipt: every run logs prompt version, model, output path and a blank human-disposition column. Fill the disposition in. A rejected frame with a reason is worth more to the deck than an accepted one.

## What this is not for

- Hero imagery. The deck rule is no generic AI imagery for hero concepts unless the idea needs a synthetic aesthetic.
- Product packaging. Never generate the sachet, bottle or logo. Composite real pack shots from `inputs/product/`.
- Real people. Never generate ambassadors, athletes or customers by name or likeness. Generic casting only.
- On-image text. Models mangle type. Generate clean plates; set copy in Figma.

## Commands

```
cp .env.example .env            # add GEMINI_API_KEY
python3 references/generate-visuals.py --list-models
python3 references/generate-visuals.py --dry-run
python3 references/generate-visuals.py --concept say-the-thing
python3 references/generate-visuals.py --all
```

Outputs land in `outputs/YYYY-MM-DD/<concept>/frame-NN.png` with an `index.md` receipt per run.

## Rules Claude follows when writing or editing prompts

Read `skills/brand-visuals/SKILL.md` before touching `references/prompts.json`.
