---
name: brand-visuals
description: Generate rough storyboard frames and mock plates from a prompt manifest using the Gemini image API, with a receipt log per run. Use when asked to render, storyboard, mock, or visualise a concept, or to add or revise frames in references/prompts.json.
---

# brand-visuals

## Before generating

1. Read `references/style-analysis.md`. It is the visual grammar. Every prompt inherits `style_prefix` and `negative` from `references/prompts.json`; do not restate them inside frame prompts.
2. Check `inputs/references/` for reference images. Up to three are attached to every Gemini call as visual direction. If the folder is empty, generation still runs on text alone.
3. Check `inputs/product/` for real pack shots. They are never sent to the model. They are composited afterwards.

## Writing a frame prompt

One frame, one picture, one sentence of intent, then specifics in this order: subject and casting, setting, light, lens and distance, what the hands are doing, what is deliberately absent. Under 90 words. Present tense. No adjectives that describe mood without describing a visible thing.

Good: "A woman in her late forties at an office desk at 2:40pm, third coffee beside the keyboard, looking past the screen at nothing. Flat fluorescent light, no window. Phone-camera feel, slightly too close, handheld. No text on screen."

Bad: "An empowering, relatable image of a tired professional woman feeling drained in the afternoon."

## Hard rules

- **No text, logos, wordmarks or typography** in any prompt. Models mangle type. Set copy in Figma.
- **No product packaging.** Never describe the sachet, bottle, label or logo. A "plain blank foil sachet, no printing" is an acceptable placeholder for compositing. Real packs come from `inputs/product/`.
- **No named or recognisable people.** Never prompt an ambassador, athlete, founder or customer by name or likeness. Generic casting with age, build and role only.
- **No competitor packaging or identifiable products.** For Out of the Green, green drinks are in plain glasses or unbranded matte tubs.
- **Crimson is the exception, never the field.** Under ten percent of frame unless the concept notes say otherwise. One crimson object per frame.
- **No medical or injury imagery adjacent to product.** For What Are You Training For?, the product plate and the treatment-room plate are separate frames and are never composited together.
- **Aspect ratio per concept**, set in the manifest, not in the prompt.

## After generating

Every run writes `outputs/YYYY-MM-DD/<concept>/index.md` with one row per frame: frame id, model, prompt hash, output path, and two blank columns, **disposition** (accept, revise, reject) and **reason**. Fill both in by hand. The receipt is only useful with the human columns complete, and a rejected frame with a specific reason is the strongest evidence for Slide 6.

Then composite: real pack shot, typography, crimson rule, in Figma. The generated frame is a plate, not a finished unit.

## Revising a frame

Change one variable per revision: casting, light, distance, or the absent thing. Bump the frame `version` in the manifest so the receipt shows lineage. Do not overwrite the previous output.

## Commands

```
python3 references/generate-visuals.py --list-models
python3 references/generate-visuals.py --dry-run
python3 references/generate-visuals.py --concept <slug> [--frames 01,03]
python3 references/generate-visuals.py --all
python3 references/generate-visuals.py --concept <slug> --model imagen-4.0-generate-001
```
