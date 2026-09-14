# IM8 Deck — Design System Spec (from reference analysis)

Paste alongside the deck copy file. Governs every slide.

## Two zones (the Seed logic, in red)
- Every slide is split into a light zone and a dark zone (60/40). Each zone has its own complete language; nothing crosses over except type, buttons and photography.
- Light zone: neutral ground #F8F6F3 → super-light tinted cards (neutral #FBF9F7, rose #FAF0EE, peach #FBF3EA), each outlined 1px #4A0E14 → one bright accent for badges. Dark appears only as type (#4A0E14 / #241512), a solid maroon button, or product imagery. Never a dark card.
- Dark zone: all the reds together. Ground gradient #8C1220 → #6B0F1A → #4A0E14; cards are tonal shifts of the ground — warm #7C1E22 (toward orange), cool #5A1230 (toward wine) — or glass rgba(255,255,255,0.08) with blur 20px. Light appears as type (cream #F8F6F3, pink #F4B8B0, coral #E39089 labels), a cream button, pale badges, and photography.
- Accent (the lime equivalent): strawberry #F52D3F, halfway between orange-red #FF4500 and crimson #DC143C. Badge = strawberry fill, dark text #3A0A10, sans 600 11px. Variants: hot pink #FF3D9A (secondary, sparingly), soft rgba(245,45,63,0.14) with #8C1220 text on light, dark-zone rgba(245,45,63,0.26) with #FFD6D0 text.
- Badges (sans 600, filled) are for highlights: Bestseller, New, Owned, First scale bet, Days 1–10. Pills (mono, outlined) are for metadata: formats, markets, Assisted.

## Color roles
- Ground: light neutral #F8F6F3 (default). Light cards: #FBF9F7 / #FAF0EE / #FBF3EA with 1px #4A0E14 border.
- Ink: #241512 for body/card titles. Headlines in deep maroon #4A0E14. Body grey rgba(36,21,18,0.62). Micro-label grey #7F665C (min ~4.8:1 on cream).
- Reds: darkest #3A0E12, deep maroon #4A0E14, maroon #6B0F1A, deep crimson #8C1220, crimson #A32430, bright red #C8102E, coral #E39089, light pink #F4B8B0.
- Longevity gradient (accent only): linear-gradient(160deg, #E8842B 0%, #C8102E 48%, #8C1220 100%). Use for photo cells, end frames, stat numerals (background-clip: text), small badges. Never as a full-slide ground.
- Ratio: 60/40 light to dark on every slide. Dark arrives as one region per slide — a column (35–40% width) or a band (40% height) — never as scattered dark cards. Region fill: linear-gradient(160deg, #8C1220 0%, #6B0F1A 55%, #4A0E14 100%). The darkest oxblood (#3A0E12) is retired.
- Card follows ground. On the neutral ground, cards are the three light tints with a 1px dark outline; a crimson or maroon card never floats on the light ground. Dark cards (warm, cool, glass) live only inside a region or over an image. Free copy inside a region is cream (#F8F6F3) for titles, pink rgba(244,184,176,0.85) for body, coral #E39089 for micro labels.
- Region placement rotates so the deck doesn't repeat: right column (1), bottom band (3, 7), left column (6, 12), image card (10).
- Deep maroon is for headlines, borders (1px rgba(74,14,20,0.14)), icon strokes, hairline rules — not major backgrounds.
- Pink text ONLY on maroon/crimson fills. Cream text on crimson cards. Crimson italic clause for the headline "turn."
- Emphasis on light cards: a 2px crimson top rule, a crimson pill, or pale pink instead of warm neutral. Not a dark fill.

## Icons
- Bare line icons, 22px, stroke 1.5, no container tile. Crimson #A32430 on light grounds; coral #E39089 or cream inside dark regions; grey #7F665C for de-emphasised items.

## Vertical grid (the spacing rule)
- Slide 1280×720 (or 1280×900 for dense pages). Outer margin 64px all sides.
- Zone A, header: mono tag → headline → optional body split. Occupies top 25–30%.
- Gap: fixed 64–96px between header and content. Never less.
- Zone B, content: vertically centered in the remaining height; equal padding above/below.
- Footer strip: page counter + optional callback tag, 11px mono, bottom-right.

## Typography
- Display (headlines): Newsreader 500, 32–52px, line-height 1.05. Secondary clause in crimson italic 400, or in body grey.
- Body/UI: IBM Plex Sans 400/500/600, 12.5–17px, line-height 1.45–1.5.
- Mono (tags, kickers, pills, footer metadata, card micro-labels): IBM Plex Mono 500, 10–12px, uppercase, letter-spacing 0.08–0.14em.

## Layout archetypes
1. Editorial split header — headline left 55%, grey body right 35%, hairline rule above, mono tag top-left.
2. Icon-topped card row — 3–4 equal cards: 24px line icon → title → description → mono micro-label at bottom.
3. Numbered bento — 3×2 grid: label cell, numbered cards 01–05, one or two photo cells. Light or ≤50% dark variant.
4. Stat row — big numeral (56–72px) → dotted or hairline rule → label → descriptor; vertical hairline dividers between.
5. Glass panel — frosted card over photo or soft gradient: rgba(255,255,255,0.35) fill, backdrop-blur 18–24px, 1px rgba(255,255,255,0.5) border, 20px radius. Holds tables and feature rows.
6. Timeline rail — vertical line, dot markers, pill labels; upcoming steps faded to 40%.

## Cards
- Radius 16–24px; fill 2–4% ink tint or pale pink; no border, or 1px hairline; shadow none or 0 1px 2px rgba(36,21,18,0.06).
- Padding 24–28px, identical across siblings; gap 14–20px.
- Optional tint progression across a row (light → medium → deeper) to imply sequence.
- Micro-label inside card: mono, uppercase, #8A6B60.

## Pills and badges
- A pill always hugs its word: `align-self: flex-start` (or wrap in a row) so it never stretches to the card width.
- Pills are for states and formats (Owned, Assisted, Days 1–10, Creator 9:16). Role titles and names are never pills — set them as a mono micro line.
- Tag pill: mono uppercase, 1px hairline or soft tint fill, full radius.
- Category pill (badge): solid maroon→orange gradient, white mono text, sparingly.
- Checklist bullet: 18px filled crimson circle/shield with white check.

## Photography and imagery
- Never full-slide. Three ways in, and only these: (1) photo-top card — image owns the top half, third or two-thirds, copy below on a warm neutral; (2) glass over image — the image fills the card and content sits in a frosted panel; (3) row rule — three info cards and one full-image card.
- No small frame strips or thumbnails inside cards; they read as clutter.
- Crop tight, subject off-center, muted grade; no stock-wellness smiling-at-camera.
- Placeholders: longevity-gradient block with a glass mono chip caption, never grey boxes.

## Free copy
- Not everything lives in a card. Roughly one block in five stands free on the ground with a hairline rule and generous space. Cards organise; free copy breathes.
- Always free: timelines and rails, stat rows, tables (hairline rows only), the thesis line, closing lines, the "assisted" half of an assisted/owned contrast.
- Cards are for the thing being emphasised or grouped: the owned stage, the hire, the concept, the compounding loop.
- Free blocks use the same type roles and the same 64px grid; the hairline (1px rgba(74,14,20,0.25)) is the only structure.

## Icons
- Thin single-weight line icons on a 20/24px grid, one consistent stroke.
- Circle-outlined icons for attribute grids; filled crimson badge for benefit bullets.
- No emoji.

## Slide-type mapping
- Thesis (1): editorial split + photo/gradient cell right, ≤50%.
- Machine slides (2, 4, 5): icon-topped card rows; SLA and decision tiers as cards.
- Team (3): numbered bento + timeline rail for the 30 days.
- AI receipts (6): glass panels on pink-orange gradient, crimson badge on owned stages.
- Multiplication (7): stat row above the ontology table.
- Learning (8): two-zone split, shared axis, cadence rail at bottom.
- Global rhythm (9): three-panel handoff + RACI in a glass panel.
- Creative (10–12): photo cell + text cell bento; one shared concept-card template.
