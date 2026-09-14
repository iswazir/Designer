# IM8 Visual System Prompt (spec of record, pasted by Inaayat 2026-09-11)

Governing principles: Light carries proof. Warmth carries people. Crimson carries conviction. Ember signals Longevity. Solid surfaces carry reading. Glass carries context. Cards carry complete ideas.

## Core red spectrum
Fire Engine #D50024 · Signal Crimson #BF0016 · IM8 Red #A40011 · Deep Burgundy #50000B · Deep Aubergine #2F0F12
IM8 Red, Deep Burgundy, Deep Aubergine carry identity. Fire Engine / Signal Crimson are concentrated moments.

## Text
Body #1A0205 · Headline #50000B · Emphasis #A40011 · Muted #6B4A4F · Inverse #FFFFFF
On dark: #FF8A78 or #FF9693 for highlighted text. Inside Ember tag: #1A0205.

## Highlights
Ember Coral #E85B4A — universal graphic highlight (markers, nodes, rules, large words, filled tags with #1A0205 text). Never small text on white.
Soft Salmon #FF9693 — large display on burgundy, human stories, gradient edges, tags on dark. Never ordinary text on white.

## Light neutrals
Pure White #FFFFFF · Clean Neutral #F7F7F5 (primary canvas) · Cool Mist #F2F4F5 (science, systems, AI) · Soft Porcelain #F6F3F1 (people) · Light Blush #F5EAEA (selective)

## Gold
Precision Gold #D4A84B · Light Gold #DBB15C — fine dividers, Longevity, milestones. Never general text.

## Gradients
Deep Crimson: linear-gradient(135deg,#2F0F12 0%,#50000B 48%,#A40011 100%) — flagship, chapter openings, rare full background. White text, one salmon phrase.
Signal Crimson: linear-gradient(135deg,#8A000E 0%,#A40011 55%,#D50024 100%) — CTAs, metrics, active, highlight cards, bands. White text.
Red to Salmon: linear-gradient(120deg,#A40011 0%,#D50024 48%,#FF9693 100%) — human energy, customer life. White over red, #1A0205 over salmon.
Neutral Salmon Wash: linear-gradient(135deg,#F2F4F5 0%,#F5EAEA 55%,#FFF1EE 100%) — people, quotes, intros.
Cool Neutral Light: linear-gradient(135deg,#F2F4F5 0%,#F7F7F5 55%,#FFFFFF 100%) — evidence, frameworks, tables, AI. Most frequent.
Soft Warm Light: linear-gradient(135deg,#F6F3F1 0%,#F7F7F5 60%,#FFFFFF 100%) — leadership, team, photography.
Cellular Ember: linear-gradient(110deg,#A40011 0%,#E85B3F 32%,#EF7745 58%,#F2A05A 78%,#F2C45B 100%) — Longevity only.

## Typography
Aeonik (Light/Regular/Medium) leads: titles, body, UI. Title Case headers, sentence-case body, tracking -0.01em–0, body lh 1.35–1.55, min 16px.
Arizona Flare Medium: selected editorial/human headlines, pull quotes, campaign hooks. Never all caps. lh 0.95–1.08, tracking -0.02em.
NB Architekt Mono (Regular/Medium/Semibold): eyebrows, numbers, evidence labels, tags, chart labels, stages, owners, dates. Only layer allowed all caps. Tracking 0.04–0.08em.
Balance: Aeonik-led 60–70%, Arizona-led 20–30%, mono ~10%.
Note (source): science mostly sans or mono; serif sometimes, for variation like the color concept.

### Deck decisions (2026-09-13)
- Every slide headline is Arizona Flare at a light weight (Regular on canvas: Fraunces 400; Medium reserved for very short display lines). A two-sentence, two-colour headline sets the second sentence in italic (IM8 Red). Smaller headlines and card titles are Aeonik Medium.
- Standfirst sits directly under the headline on the same left axis (Aeonik Light 24px, max 900px), never floated right.
- IM8 wordmark in the identity zone, top-right (white over dark or image). Page number bottom-right.
- Default light ground is Soft Warm Light. Cool Neutral Light only where science demands a cooler read.
- Content is distributed evenly between header and footer; no empty band in the middle.
- Images may replace a card in a Modular Cards row, and may bleed full height to the canvas edge in an Editorial Split.

- Red fields: Signal Crimson (IM8 Red → Fire) may carry a whole content-heavy slide when the chapter needs energy — white Editorial cards and one dark-glass panel on the field, salmon for the italic clause, at most two such slides in twelve (02 Intake, 05 Tiers).
- Content-heavy layout families (all on the 12-col grid, mapped on the Layouts board): Sidebar + Grid 3/9 · Two-thirds/One-third 8/4 · Four-up + band · Full-grid table · Index on a red field · Rows on a red field · Panels + table · Evidence Field.

### Canvas substitutions (fonts not on Google Fonts)
Aeonik → Inter (300/400/500) · Arizona Flare → Fraunces 500 · NB Architekt Mono → DM Mono (400/500). Swap in the licensed faces in Keynote/Figma.

## Presentation
1920×1080, 12 cols, 80px margins, 24px gutters, 8px baseline, ≥30% open (min 25%). Never shrink type to fit.
Hero 58–76 · Title 44–56 · Editorial line 34–48 · Subtitle 22–28 · Card title 20–26 · Body 17–21 · Mono 13–16 · Metric 36–64 · Footer 11–13.
Rhythm: alternate white, subtle neutral gradients, photography, selective crimson fields. Dark never the default. One Deep Crimson climax. One full-height image every 2–3 slides. One idea + one device per slide. Not every slide a card grid.

## Cards
Sequence: MONO LABEL → Title → 2–4 line explanation → compact proof/metric/owner → optional consequence. One idea per card; 2–4 per group; highlight only one.
Editorial: #FFF, 1px rgba(80,0,11,.10), r20, shadow 0 8px 28px rgba(47,15,18,.05).
Light Glass: rgba(255,255,255,.68), 1px rgba(255,255,255,.72), blur 18 sat 115%, r24 — over photography, washes.
Dark Glass: rgba(26,2,5,.28), 1px rgba(255,255,255,.18), blur 18 sat 120%, r24 — over Deep/Signal Crimson, Ember, dark photos.
Burgundy Proof: #50000B, 1px rgba(255,255,255,.12), r20 — evidence, decisions, gates, rules.
Highlight: Signal Crimson gradient, 1px rgba(255,255,255,.18), r20 — once per group.
Glass: only over gradients/images; never over white; one per section; never stacked; no blur behind tables.

## Geometry / borders
Pills 999 · buttons pill or 12–16 · compact card 16–20 · card 20–24 · hero glass 28–32 · image 20–32.
--border-default 1px rgba(80,0,11,.10) · --border-dark 1px rgba(255,255,255,.16) · --border-active 1px #A40011 · --divider-gold 1px rgba(212,168,75,.55)

## Buttons / tags
Primary: #A40011 / #FFF, Medium, sentence case, pill. Secondary: transparent, border #50000B.
Evidence tag: #50000B / #FFF mono caps. Human tag: #E85B4A / #1A0205 mono semibold. Longevity tag: #F2C45B / #1A0205, product-only.

## Guardrails
Not every headline serif · no extra display font · no burgundy default background · not every card translucent · no gradients in every component · no salmon small text on white · orange/gold never general · no paragraphs across gradient transitions · no decorative icons/shadows/pills · never shrink type · don't reproduce Seed literally.
Four questions per page: main idea? read next? evidence? remember/do?

---

# Swiss Grid System (added 2026-09-11)

Swiss-influenced modular grid across every IM8 format: precise, contemporary, scientific, editorial; expressive gradients, photography, glass and oversized type allowed inside it. Evokes Seed's modularity and Timeline's whitespace-led, science-forward hierarchy without copying either. The grid creates authority. Asymmetry creates energy. Whitespace creates confidence.

## Core principles
Visible-but-unpublished column structure · asymmetry inside order · left-align most copy · type, images, cards, dividers and metadata on shared grid lines · one dominant element + one supporting system · negative space is active · separate with spacing before boxes · thin rules, mono labels, numbers, coordinates selectively · photography/gradients break the grid only on purpose · don't centre everything · no symmetrical three-card layouts by default · never fill every cell · 25–40% open.

## Universal structure (five invisible zones)
1 Identity (logo, campaign, product, section label) · 2 Message (one dominant headline) · 3 Evidence (proof, metric, claim, detail) · 4 Image (product, person, science, field) · 5 Metadata (CTA, URL, page number, disclaimer, reference, status). One zone dominates, two support, the rest stay minimal.

## Alignment
One primary vertical axis per asset; ≥3 elements on it; a secondary axis for contrast; headlines and explanations on consistent columns; metadata anchored to a stable outer edge; card bottoms aligned when comparing; never centre body copy; centring only for very short declarations or singular product moments; let elements span columns.

## Slide grid
1920×1080 · 12 cols · 80 margins · 24 gutters · 8 baseline · header zone 64–88 · footer zone 40–56 · min open 25%, preferred 30–40%. Same header/footer anchors across the deck; vary the centre.

### Layout families
- Editorial Split — text cols 1–5, col 6 open, image/composition cols 7–12 (or 4/8). Strategic arguments, human stories, product intros, photo-led, before/after.
- Evidence Field — title cols 1–7, evidence/diagram cols 1–9, proof card cols 9–12, metadata outer-right or bottom. Science, research, operating models, performance data, claims. Canvas light; proof card is the one concentrated burgundy or glass element.
- Modular Cards — title cols 1–8; cards 3+3+3 with one column open, or 4+4 with four columns open or image-led. Workstreams, responsibilities, stages, principles, options. Unequal information gets an unequal grid: priority card larger, darker or offset.
- Swiss Index — large number cols 1–3, headline cols 4–10, explanation cols 7–11, metadata cols 11–12. Chapter openings, major statistics, milestones. Number in Aeonik Medium or mono, only when it carries meaning.
- Full-Bleed Interruption — image or gradient full canvas; stable text zone 4–6 cols; glass panel optional, maximum one; metadata on the outer margin. Campaign statements, turning points, Longevity moments, climaxes, closing. Never several cards over a full-bleed.

## Poster grid
Portrait 24×36 or proportional · 6 cols · margins 5–7% · gutters 2–3% · 8 or 12 row units · safe 5%. Hierarchy: one headline, one image/product/object, one proof point, one metadata cluster, one signature. Oversized type across 2–4 cols; product crops decisively, never a floating centred cutout.
Layouts: Typographic Monument (headline 40–60% of canvas, image cropped into the rest, mono proof on a distant edge, small logo) · Product and Proof (product 3–4 cols, claim beside not beneath, gold/burgundy divider, study metadata in mono) · Human and System (full-height photo, one text column, optional Light Glass proof, crimson as accent/crop/garment/line).

## Billboard grid
6 cols · safe 5–8% · message 1–7 words · support ≤8–12 words · 1–2 visual objects · one brand mark · URL/short action only. No paragraphs, no multiple glass, no fine detail.
Layouts: Headline Dominant (headline 1–4, product/person 4–6, logo/URL outer edge) · Image Dominant (image 1–4, headline 4–6, proof/URL beneath) · Extreme Reduction (one statement, one product, one crimson or Longevity field, one logo).

## Social grid
Square 1080×1080 · 6 cols · 72 margins · 20–24 gutters · safe 936². Recipes: 4-col headline + 2-col crop · 3-col product + 3-col proof · full image + one Light Glass · oversized metric across 4 cols with mono evidence · one Burgundy Proof card offset on light neutral.
Portrait 1080×1350 · 6 cols · 10 rows · central 1080² primary. Vertical progression: label → headline → image/metric → explanation → proof/CTA. Never just stretch the square.
Stories/Reels 1080×1920 · 6 cols · 72 margins · top safety 250 · bottom safety 300 · content zone central 1370. One vertical image, 1–3 line headline, one metric/detail, one CTA, at most one glass.
Carousels: fixed anchors (label position, headline axis, page-number zone, card padding); image placement and colour may progress cool neutral → salmon → crimson → Longevity. Sequence: Recognition → Orientation → Evidence → Meaning → Action → Source. Vary scale, crop, density; keep the grid.

## Web grid
Desktop ≤1440 · 12 cols · padding 48–80 · gutters 24–32 · section spacing 120–180 · card spacing 24–32. Tablet 8 cols · 32–48 · 20–24 · 88–120. Mobile 4 cols · 20–24 · 16 · 64–88; stack in reading order, don't force desktop asymmetry.
Behaviour: alternate expansive editorial with modular cards; horizontal scroll only for sequences; images may bleed while copy stays aligned; sticky labels sparingly; not every section in a container; components may overlap by one grid unit; full-width gradient fields as mode transitions; solid reading surfaces; minimal navigation.

## Image placement
Product: crop to show materiality; a product edge on a column line; no small centred pack shots; one hero product; pair with one proof; glass only when copy must overlap.
Human: decisive crops; faces/hands may cross columns; text away from faces; use photo negative space as the text zone; crimson through clothing, environment, light or a line; believable, specific.
Scientific: renders, ingredients, microscopic forms and diagrams are primary objects; one large render + small metadata; labels outside the object, connected by fine rules; cool neutral fields; Cellular Ember only for Longevity.

## Composition rules
Do: asymmetry inside a grid · oversized type against small metadata · scale contrast · shared axes · one dominant image or statement · mono labels as coordinates · hairlines · crop with conviction · deliberate empty cells · proof accessible · repeating anchors.
Don't: centre everything · identical equal-width cards · fill every column · scattered text boxes · several equal ideas on one asset · small centred pack shots · decorative "Swiss" shapes · metadata noise · tiny type · Seed's green or Timeline's black-and-white · cleverness over readability.

## Cross-format consistency
Preserve: headline language, colour family, type register, crop logic, mono metadata, one alignment axis, one proof point, one CTA. Adapt: columns, copy amount, crop, card count, type scale, glass opacity, metadata density, CTA prominence. Do not resize. Recompose.

## Final layout test
One entry point? Deliberate eye order? ≥3 elements on shared lines? Enough open space? One dominant element? Anything removable? Still IM8 without the logo? Seed/Timeline clarity without imitation?
