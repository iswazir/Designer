# IM8 Deck Design System (Claude Design canvas)

Source of the IM8 Head of Content deck canvas published at
https://claude.ai/code/artifact/23f65d2f-786b-4173-b544-2311556babab

## What is here

- `im8-elevated-deck.html` — the seeded Claude Design canvas (the file that is published as the Artifact). Re-publish this to update the design system in Claude Design, or open it locally to view.
- `artboards/*.dc.html` — one artboard per slide plus the reference boards (System, Layouts, Components A, Components B). These are what Claude Design edits.
- `src/tokens.css` — the design tokens: red spectrum, light neutrals, highlights, gold, gradients, type roles, cards (Editorial / Light Glass / Dark Glass / Burgundy Proof / Highlight), tags, buttons, wordmark, timeline, table rows.
- `src/*.frag.html` — body-only fragments for each artboard; `src/build.py` wraps each fragment with the shared head + tokens to produce `artboards/*.dc.html`.
- `src/canvas.json` — artboard positions, titles and annotations on the canvas.
- `docs/IM8_Visual_System_Prompt.md` — the spec of record (palette, gradients, type, cards, glass, Swiss grid, layout families, deck decisions).
- `docs/IM8_Master_Deck_Copy_Build.md` and `docs/IM8_Deck_Claude_Design_Import.md` — the deck copy, full build and slide-by-slide import.
- `docs/IM8_Deck_Design_System_Spec.md` — earlier spec (superseded by the Visual System Prompt; kept for history).

## Fonts

Canvas fonts stand in for the licensed set: Inter for Aeonik, Fraunces for Arizona Flare, DM Mono for NB Architekt Mono. Swap in the licensed faces in Keynote/Figma, or embed the licensed files and update the `<link>` in `src/build.py`.

## Rebuild and re-seed

```
cd src
python3 build.py                      # fragments + tokens -> ../artboards/*.dc.html (writes next to the fragments; move as needed)
node <design-skill>/seed-canvas.mjs \
  --template <design-skill>/payload.template.html \
  --out ../im8-elevated-deck.html --title "IM8 Elevated Deck" \
  --artboard Main.dc.html --artboard Slide02.dc.html ... --artboard ComponentsB.dc.html \
  --canvas canvas.json
```

`build.py` writes the `.dc.html` files into the same directory it runs from; copy them into `artboards/` after building. The seed command lists artboards in canvas order (Main, Slide02–Slide12, System, Layouts, ComponentsA, ComponentsB).

## Voice

All deck copy should follow `../voice/IM8_VOICE.md` — the IM8 voice guide (governing line: "Know more. Say less. Prove what you say."). Check new or edited copy against its banned-words list (Section 26) and the eight editor tests (Section 30) before calling it final.

## Slide map

01 Thesis (Editorial Split, full-height image) · 02 Intake (Swiss Index on Signal Crimson) · 03 Team (four-up + band) · 04 Gates (sidebar + grid) · 05 Tiers + SLA (rows on a red field) · 06 AI receipts (Evidence Field) · 07 Ontology (metrics + chain) · 08 Learning (two-thirds / one-third) · 09 Global rhythm (panels + table) · 10 Creative I · 11 Creative II (image replaces a card) · 12 Close (the single Deep Crimson field).
