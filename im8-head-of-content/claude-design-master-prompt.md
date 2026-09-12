# IM8 Visual System Prompt

Master prompt for Claude Design. Version: 12 September 2026.

Design a premium IM8 presentation and digital interface inspired by the modular clarity, scientific confidence, generous whitespace, layered cards, and restrained glass effects of Seed's website.

Do not copy Seed literally. Translate those principles into an unmistakably IM8 system built around crimson, burgundy, clean neutrals, selective salmon, and a distinct orange-gold Longevity expression.

The result should feel:

- Scientific but not sterile
- Premium but not ornamental
- Editorial but highly functional
- Modular but not like generic SaaS
- Energetic but never visually frantic
- Human enough to offset the precision
- Considered before it feels designed

## Governing principles

> Light carries proof.
> Warmth carries people.
> Crimson carries conviction.
> Ember signals Longevity.
> Solid surfaces carry reading.
> Glass carries context.
> Cards carry complete ideas.
> The grid creates authority. Asymmetry creates energy. Whitespace creates confidence.

***

# Color System

## Core red spectrum

Use this five-color progression from fire-engine red to deep, almost-purple burgundy:

| Token | Hex | Role |
|---|---:|---|
| Fire Engine | `#D50024` | Highest-energy accent and urgent emphasis |
| Signal Crimson | `#BF0016` | Campaign moments and active states |
| IM8 Red | `#A40011` | Primary branded red, links and CTAs |
| Deep Burgundy | `#50000B` | Signature brand field and dark-red text |
| Deep Aubergine | `#2F0F12` | Premium near-purple depth and dark surfaces |

Color progression:

```text
#D50024 → #BF0016 → #A40011 → #50000B → #2F0F12
```

Allow IM8 Red, Deep Burgundy, and Deep Aubergine to carry most of the identity. Fire Engine and Signal Crimson should appear as concentrated moments of energy, not default backgrounds.

## Text colors

| Role | Hex |
|---|---:|
| Almost-black body text | `#1A0205` |
| Dark-red headline text | `#50000B` |
| Bright-red emphasis | `#A40011` |
| Muted secondary text | `#6B4A4F` |
| Inverse text | `#FFFFFF` |

Use `#1A0205` for dense reading, tables, and body copy.

Use `#50000B` for branded headlines, card titles, navigation, and selected short passages.

Use `#A40011` for links, metrics, section markers, and brief emphasis. Do not set entire paragraphs in bright red.

## Signature highlights

### Ember Coral

```text
#E85B4A
```

Use Ember Coral as the universal graphic highlight:

- Marker strokes
- Active diagram nodes
- Rules and small shapes
- Large emphasized words
- Graphic signals
- Filled tags with `#1A0205` text
- The bridge between IM8 red and the Longevity spectrum

Do not use Ember Coral for small text on white.

### Soft Salmon

```text
#FF9693
```

Use salmon as a softer secondary expression:

- Large display typography on burgundy
- Human and customer stories
- Atmospheric gradient edges
- Selected tags on dark surfaces
- Occasional editorial moments

Do not use salmon as ordinary text on white.

### Accessible text modes

- On light surfaces: use `#A40011` for highlighted text.
- On dark surfaces: use `#FF8A78` or `#FF9693`.
- For a universal graphic accent: use `#E85B4A`.
- For text inside an Ember Coral tag: use `#1A0205`.

## Light neutrals

Replace yellowish and oatmeal-like cream backgrounds with cleaner lights:

| Token | Hex | Character |
|---|---:|---|
| Pure White | `#FFFFFF` | Maximum clarity |
| Clean Neutral | `#F7F7F5` | Softened, nearly neutral white |
| Cool Mist | `#F2F4F5` | Cool gray with a restrained blue cast |
| Soft Porcelain | `#F6F3F1` | Slightly warm without becoming cream |
| Light Blush | `#F5EAEA` | Subtle pink-neutral atmosphere |

Use Clean Neutral as the primary editorial canvas.

Use Cool Mist for science, evidence, systems, AI, and information-dense material.

Use Soft Porcelain for people, leadership, customer life, and warmer photography.

Use Light Blush selectively. It should register as a neutral carrying a trace of pink, not as a pink page.

## Gold accents

| Token | Hex | Role |
|---|---:|---|
| Precision Gold | `#D4A84B` | Dividers, milestones, small premium details |
| Light Gold | `#DBB15C` | Longevity details and controlled illumination |

Use gold sparingly. Restrict it primarily to:

- Fine divider rules
- Longevity content
- Milestones
- Premium proof markers
- Small product-specific details

Do not use gold as a general text color or decorate every card with it.

***

# Gradient System

## Deep Crimson

```css
background: linear-gradient(
  135deg,
  #2F0F12 0%,
  #50000B 48%,
  #A40011 100%
);
```

Use for:

- Flagship brand statements
- Strategic chapter openings
- Conviction and decisive recommendations
- Premium campaign fields
- Rare full-background moments

Keep most of the field dark. Crimson should emerge at an edge rather than consume the entire composition.

Use white text. Salmon may be used for one large accent phrase.

## Signal Crimson

```css
background: linear-gradient(
  135deg,
  #8A000E 0%,
  #A40011 55%,
  #D50024 100%
);
```

Use for:

- Calls to action
- Launches
- Important metrics
- Active states
- Performance-oriented creative
- Highlight cards and horizontal bands

This is the energetic gradient. Prefer smaller surfaces and cropped fields over repeated full-page use.

Use white text.

## Red to Salmon

```css
background: linear-gradient(
  120deg,
  #A40011 0%,
  #D50024 48%,
  #FF9693 100%
);
```

Use for:

- Human-energy stories
- Community and culture
- Optimistic campaign moments
- Movement
- Customer-life imagery
- Large emotional statements

Treat salmon as light entering the red. Do not give each color equal visual weight.

Use white over the red region and `#1A0205` over the salmon region. Never place a paragraph across the entire transition.

## Neutral Salmon Wash

```css
background: linear-gradient(
  135deg,
  #F2F4F5 0%,
  #F5EAEA 55%,
  #FFF1EE 100%
);
```

Use for:

- People and culture
- Customer stories
- Pull quotes
- Introductions
- Approachable editorial moments
- Soft transitions between white and crimson sections

This should appear predominantly neutral. Confine the pink warmth to one edge or corner.

Use `#1A0205` for body copy and `#50000B` for headlines.

## Cool Neutral Light

```css
background: linear-gradient(
  135deg,
  #F2F4F5 0%,
  #F7F7F5 55%,
  #FFFFFF 100%
);
```

Use for:

- Scientific evidence
- Strategy frameworks
- Tables
- AI and operating systems
- Diagrams
- Information-dense pages
- Primary website reading sections

Keep the transition nearly imperceptible. Its purpose is depth, not decoration.

## Soft Warm Light

```css
background: linear-gradient(
  135deg,
  #F6F3F1 0%,
  #F7F7F5 60%,
  #FFFFFF 100%
);
```

Use for:

- Leadership
- Team
- Customer life
- Photography
- Human stories that should not become pink
- Editorial transitions

This replaces the website's more yellow cream behavior.

## Cellular Ember

```css
background: linear-gradient(
  110deg,
  #A40011 0%,
  #E85B3F 32%,
  #EF7745 58%,
  #F2A05A 78%,
  #F2C45B 100%
);
```

Use exclusively or primarily for:

- Daily Ultimate Longevity
- Cellular energy
- Healthy aging
- Ingredient systems
- Transformation
- Product-specific scientific visualization

Always anchor the gradient in IM8 Red. Orange and gold should feel like energy emitted from the brand red.

Use white over the red-orange region and `#1A0205` over the apricot-gold region.

## Gradient frequency

| Gradient | Frequency |
|---|---:|
| Cool Neutral Light | Most frequent |
| Neutral Salmon Wash | Frequent |
| Soft Warm Light | Frequent |
| Deep Crimson | Selective |
| Signal Crimson | Selective |
| Red to Salmon | Occasional |
| Cellular Ember | Longevity-specific |

Do not place gradients inside every card. Use them as section fields, emotional transitions, campaign punctuation, or product-world signals.

***

# Typography System

Typography must change according to the job. Do not force one premium-looking typeface onto every message.

> Aeonik leads.
> NB Architekt organizes and proves.
> Arizona Flare adds selective editorial warmth.

## Typeface roles

| Typeface | Weights | Role |
|---|---|---|
| Aeonik | Light, Regular, Medium | Default headlines, subtitles, body, navigation and UI |
| Arizona Flare | Medium | Selected editorial or human headlines |
| NB Architekt Mono | Regular, Medium, Semibold | Labels, evidence, metadata, numbers and system language |

Do not add Arizona Mix Condensed, Arizona Flare Condensed, or another display face at this stage. Color, scale, photography, gradients, glass, and layout already provide sufficient range.

## Aeonik

Aeonik is the default typeface.

Use Aeonik for:

- Most slide and page titles
- Clear strategic headlines
- Subtitles and standfirsts
- Body copy
- Card titles and explanations
- Navigation
- Buttons and links
- Tables
- Instructions
- Regulatory copy

### Weight rules

- Light: large subtitles and spacious introductory statements
- Regular: body copy, card explanations and captions
- Medium: headlines, buttons, navigation and emphasized phrases
- Do not use a heavier weight than Medium
- Create hierarchy through scale, spacing, color, and placement before increasing weight

### Styling

- Use Title Case for headers
- Use sentence case for body copy
- Tracking: `-0.01em` to `0`
- Body line height: `1.35` to `1.55`
- Keep reading lines between approximately 45 and 70 characters
- Never reduce meaningful presentation copy below 16 px

## Arizona Flare

Arizona Flare is an accent, not a default.

Use it for:

- Human or emotionally resonant titles
- Editorial statements
- Pull quotes
- Customer-life moments
- Campaign hooks
- Occasional defining lines

Do not use it for:

- Every slide title
- Paragraphs
- Tables
- Diagrams
- Instructions
- Navigation
- Metadata
- Evidence labels

### Styling

- Medium weight
- Title Case for headlines
- Never all caps
- Prefer one to three lines
- Tracking: approximately `-0.02em`
- Line height: `0.95` to `1.08`

## NB Architekt Mono

Use mono for:

- Eyebrows
- Section numbers
- Evidence labels
- Study metadata
- Tags and pills
- Chart labels
- Workflow stages
- Owners and statuses
- Dates and page numbers
- Scientific or operational details

### Weight rules

- Regular: metadata and footers
- Medium: tags and diagram labels
- Semibold: status, active states and significant numbers

### Styling

- All caps are allowed only in the mono layer
- Use tracking between `0.04em` and `0.08em`
- Keep labels concise
- Never set paragraphs in mono
- Mono must indicate genuine evidence or structure, not decorative "tech" styling

## Typeface balance

Use as a directional ratio, not a rigid quota:

- Aeonik-led pages: 60–70%
- Arizona Flare-led pages: 20–30%
- Mono-led or proof-heavy moments: approximately 10%

Science reads mostly in sans serif or mono. The serif is fine sometimes, but it exists to create variation in the same way the color system does, not to become the default register.

***

# Presentation System

## Canvas and grid

```text
Canvas: 1920 × 1080, 16:9
Columns: 12
Outer margins: 80 px
Gutters: 24 px
Baseline grid: 8 px
Target open space: 30%
Absolute minimum open space: 25%
```

The full column structure, layout families, and cross-format grids are defined in the Swiss Grid System below. If a slide feels crowded, remove or reorganize content. Do not solve density by making the typography smaller.

## Presentation type scale

| Element | Typeface | Size |
|---|---|---:|
| Hero title | Aeonik Medium or Arizona Flare Medium | 58–76 px |
| Standard title | Aeonik Medium | 44–56 px |
| Editorial defining line | Arizona Flare Medium | 34–48 px |
| Subtitle | Aeonik Light/Regular | 22–28 px |
| Card title | Aeonik Medium | 20–26 px |
| Body copy | Aeonik Regular | 17–21 px |
| Mono label | NB Architekt Mono Medium | 13–16 px |
| Major metric | Aeonik Medium or Arizona Flare | 36–64 px |
| Footer | NB Architekt Mono Regular | 11–13 px |

Essential information must be at least 16 px. Only page numbers, footers, and genuinely secondary metadata may be smaller.

## Slide rhythm

- Alternate white, subtle neutral gradients, photography, and selective crimson fields
- Do not use dark backgrounds as the deck-wide default
- Use one Deep Crimson climax, or very few
- Allow room for one full-height image every two or three slides
- Keep at least 30% of each slide open when possible
- Use one dominant idea and one primary visual device per slide
- Avoid turning every slide into a card grid
- Use gold only as a fine detail
- Use salmon typography only when large or contained inside a tag

***

# Swiss Grid System

Use a Swiss-influenced modular grid across every IM8 format: presentations, web, posters, billboards, and social. The grid should make the work feel precise, contemporary, scientific, and editorial while allowing expressive gradients, photography, glass cards, and oversized typography.

The system should evoke the clarity and modularity associated with Seed and Timeline Nutrition, but it must remain unmistakably IM8 through crimson, burgundy, clean neutral fields, Longevity gradients, and the established typography system. Timeline's visual language is particularly useful for its whitespace, scientific data, premium product photography, and crisp editorial hierarchy.[1] Seed's system is useful for its scalable modules and components across scientific, anatomical, product, and human-centered content.[2]

## Core principles

- Build every asset on a visible but unpublished column structure
- Use asymmetry within an ordered grid
- Left-align most copy
- Align type, images, cards, dividers, and metadata to shared grid lines
- Establish one dominant element and one supporting system
- Use negative space as an active compositional element
- Separate information through spacing before adding boxes or decoration
- Use thin rules, mono labels, numbers, coordinates, and metadata selectively
- Allow photography or gradients to break the grid only when the contrast is intentional
- Avoid centering every element
- Avoid symmetrical three-card layouts by default
- Never fill every grid cell
- Keep approximately 25–40% of most compositions open

> The grid creates authority. Asymmetry creates energy. Whitespace creates confidence.

## Universal Structure

Every format should share five invisible zones:

1. **Identity zone:** Logo, campaign name, product name, or section label
2. **Message zone:** One dominant headline or idea
3. **Evidence zone:** Proof, metric, claim, explanation, or product detail
4. **Image zone:** Product, person, scientific visualization, or atmospheric field
5. **Metadata zone:** CTA, URL, page number, disclaimer, study reference, or status

Do not give every zone equal visual weight. One zone should dominate, two should support, and the remaining zones should remain minimal.

### Alignment rules

- Choose one primary vertical axis for every asset
- Align at least three elements to that axis
- Use a secondary axis for contrast rather than scattering content
- Keep headlines and explanations on consistent columns
- Anchor metadata to a stable outer edge
- Align card bottoms when comparing information
- Do not center-align body copy
- Center alignment is reserved for very short campaign declarations or singular product moments
- Let some elements span multiple columns rather than placing one object in every column

## Slide Grid

### Base specification

```text
Canvas: 1920 × 1080
Columns: 12
Outer margins: 80 px
Gutters: 24 px
Baseline: 8 px
Header zone: 64–88 px
Footer zone: 40–56 px
Minimum open space: 25%
Preferred open space: 30–40%
```

Use the same header and footer anchors across the presentation, but vary the central composition.

### Slide layout families

#### Editorial Split

```text
Text: columns 1–5
Open transition: column 6
Image or composition: columns 7–12
```

Use for:

- Strategic arguments
- Human stories
- Product introductions
- Photography-led pages
- Before-and-after narratives

The text and image should not always divide the canvas exactly in half. Use a 5/7 or 4/8 relationship for greater tension.

#### Evidence Field

```text
Title: columns 1–7
Evidence or diagram: columns 1–9
Proof card: columns 9–12
Metadata: outer-right or bottom baseline
```

Use for:

- Scientific evidence
- Research findings
- Operating models
- Performance data
- Claims and substantiation

Keep the canvas predominantly light and use the proof card as a concentrated burgundy or glass element.

#### Modular Cards

```text
Title: columns 1–8
Cards: 3+3+3 columns, with one column of deliberate open space
Or: 4+4 columns, leaving four columns open or image-led
```

Use for:

- Comparable workstreams
- Responsibilities
- Stages
- Principles
- Strategic options

Avoid equal card grids when the information is not equal. Make the priority card larger, darker, or offset rather than merely adding a brighter border.

#### Swiss Index

```text
Large number: columns 1–3
Headline: columns 4–10
Explanation: columns 7–11
Metadata: columns 11–12
```

Use for:

- Chapter openings
- Major statistics
- Strategic milestones
- Sequence markers
- Defining operational principles

The oversized number can use Aeonik Medium or NB Architekt Mono. Do not use a decorative number unless it carries real meaning.

#### Full-Bleed Interruption

```text
Image or gradient: full canvas
Stable text zone: 4–6 columns
Glass panel: optional, maximum one
Metadata: anchored to outer margin
```

Use sparingly for:

- Campaign statements
- Emotional turning points
- Longevity product moments
- Section climaxes
- Closing slides

Do not place multiple cards over a full-bleed image. Choose either one glass panel or one direct typographic treatment.

## Poster Grid

### Standard portrait

```text
Format: 24 × 36 in or proportional portrait
Columns: 6
Outer margins: 5–7% of width
Gutters: 2–3% of width
Rows: 8 or 12 modular units
Safe area: 5%
```

### Poster hierarchy

1. One dominant headline
2. One image, product, or scientific object
3. One proof point or short explanatory statement
4. One small metadata cluster
5. One logo or brand signature

Use oversized type that occupies two to four columns. Let product or photography crop decisively rather than floating as a centered ecommerce cutout.

### Poster layouts

#### Typographic Monument

- Oversized Aeonik headline occupying 40–60% of the canvas
- Product or scientific image cropped into the remaining field
- Mono proof label aligned to a distant grid edge
- Logo small and restrained

Use for brand campaigns and concise declarations.

#### Product and Proof

- Product spanning three or four columns
- Claim or metric aligned beside it rather than underneath it
- Fine gold or burgundy divider
- Study or evidence metadata in mono at the bottom

Use for science-backed product communication.

#### Human and System

- Full-height person or lifestyle photograph
- One clean text column
- Optional Light Glass Card containing proof or context
- Crimson used as an image accent, crop, garment detail, or graphic line

Use for recognition, customer life, and human benefit.

## Billboard Grid

Billboards must work at speed and distance. Reduce the Swiss system to its strongest structural elements rather than reproducing a full editorial layout.

### Base specification

```text
Columns: 6
Outer safe margins: 5–8%
Primary message: 1–7 words
Supporting line: optional, maximum 8–12 words
Visual objects: maximum 1–2
Brand mark: one clear location
CTA: URL or short action only
```

### Billboard hierarchy

- One headline
- One product, person, or graphic object
- One brand mark
- Optional proof point
- No paragraph copy
- No multiple glass cards
- No fine detail that must be read from close range

### Billboard layouts

#### Headline Dominant

```text
Headline: columns 1–4
Product or person: columns 4–6
Logo/URL: bottom or top outer edge
```

#### Image Dominant

```text
Image: columns 1–4
Headline: columns 4–6
Proof/URL: aligned beneath headline
```

#### Extreme Reduction

```text
One short statement
One product
One crimson or Longevity field
One logo
```

Use Extreme Reduction when the message is recognition-led or campaign-defining. Avoid creating a miniature website on a billboard.

## Social Grid

Create a reusable grid family rather than resizing one master composition into every social ratio.

### Square feed

```text
Format: 1080 × 1080
Columns: 6
Outer margins: 72 px
Gutters: 20–24 px
Baseline: 8 px
Safe text area: 936 × 936 px
```

Use for:

- Single-message statements
- Product and proof
- Quotes
- Educational cards
- Campaign modules

#### Square recipes

- 4-column headline with a 2-column image crop
- 3-column product with a 3-column proof block
- Full-field image with one Light Glass Card
- Oversized metric spanning four columns with mono evidence beneath
- One Burgundy Proof Card offset against a light-neutral canvas

### Portrait feed

```text
Format: 1080 × 1350
Columns: 6
Outer margins: 72 px
Gutters: 20–24 px
Rows: 10
Primary safe area: central 1080 × 1080 region
```

Use the additional vertical space for narrative progression:

1. Label
2. Headline
3. Image or metric
4. Explanation
5. Proof or CTA

Do not simply enlarge the square composition vertically.

### Stories and Reels

```text
Format: 1080 × 1920
Columns: 6
Outer margins: 72 px
Top interface safety: 250 px
Bottom interface safety: 300 px
Primary content zone: central 1370 px
```

Place essential text and product information inside the central safe zone. Avoid putting labels, footnotes, or CTAs directly against interface controls.

Use:

- One strong vertical image
- One headline of one to three lines
- One metric or product detail
- One short CTA
- One restrained glass panel if the background requires it

### Carousels

Maintain fixed grid anchors across every frame:

- Label remains in one position
- Headline begins on the same axis
- Page number stays in the same metadata zone
- Cards maintain consistent internal padding
- Image placement may shift to create rhythm
- Color may progress from cool neutral to salmon, crimson, or Longevity as the story develops

#### Carousel sequence

1. **Recognition:** State the tension or question
2. **Orientation:** Explain why it matters
3. **Evidence:** Introduce research, mechanism, or product fact
4. **Meaning:** Translate the evidence into human relevance
5. **Action:** Offer the next step or product role
6. **Source:** Provide claims, study, or disclaimer information when needed

Do not repeat the exact same card composition on every frame. Keep the grid constant while varying scale, crop, and density.

## Web Grid

### Desktop

```text
Maximum content width: 1440 px
Columns: 12
Outer page padding: 48–80 px
Gutters: 24–32 px
Section spacing: 120–180 px
Card spacing: 24–32 px
Baseline: 8 px
```

### Tablet

```text
Columns: 8
Outer padding: 32–48 px
Gutters: 20–24 px
Section spacing: 88–120 px
```

### Mobile

```text
Columns: 4
Outer padding: 20–24 px
Gutters: 16 px
Section spacing: 64–88 px
```

Do not force desktop asymmetry onto mobile. Preserve information hierarchy while allowing content to stack in its natural reading order.

### Web behavior

- Alternate expansive editorial sections with modular card systems
- Use occasional horizontal scrolling only for genuinely sequential content
- Let images bleed to a viewport edge while copy remains grid-aligned
- Use sticky metadata or section labels sparingly
- Do not place every section inside a container
- Allow some components to overlap backgrounds by one grid unit
- Use full-width gradient fields as transitions between information modes
- Maintain solid reading surfaces for long-form copy
- Keep navigation minimal and highly legible

Seed's current brand system emphasizes scalable modules and components across scientific, anatomical, product, and human-centered content; use that principle rather than duplicating individual page compositions.[2]

## Image Placement

Photography and product imagery should obey the grid before selectively breaking it.

### Product imagery

- Crop large enough to reveal materiality and detail
- Align a significant product edge to a column line
- Avoid small centered pack shots surrounded by arbitrary empty space
- Use one hero product rather than several equal products
- Pair the product with one proof point or short claim
- Use glass only if copy must overlap the image

### Human photography

- Prefer decisive crops over perfectly centered portraits
- Allow faces, hands, or bodies to cross column boundaries
- Keep text away from visually active facial areas
- Use negative space within the photograph as a text zone
- Let crimson appear subtly through clothing, environment, light, or graphic intervention
- Smiling and aspirational imagery is acceptable when it remains believable and specific

### Scientific imagery

- Treat anatomical renders, ingredient imagery, microscopic forms, and diagrams as primary visual objects
- Use scale contrast: one large render with small, disciplined metadata
- Keep explanatory labels outside the object when possible
- Connect labels with fine rules rather than decorative arrows
- Use cool neutral fields for clarity and Cellular Ember only for Longevity-specific science

Seed's system connects human and scientific worlds through modular imagery and the juxtaposition of micro and macro scales; adapt that principle to IM8's product and content strategy.[2][3]

## Swiss Composition Rules

### Do

- Create asymmetry inside a clear grid
- Use oversized typography against small metadata
- Use strong scale contrast
- Align unrelated elements to shared axes
- Let one image or statement dominate
- Use mono labels as navigational coordinates
- Use hairline dividers and rules
- Crop with conviction
- Leave deliberate empty cells
- Keep proof visually accessible
- Use repeating grid anchors across campaigns

### Do not

- Center every headline and product
- Build every layout from identical equal-width cards
- Fill every column
- Scatter text boxes without shared alignment
- Place several equally important ideas on one asset
- Use small centered product pack shots as the default
- Add decorative geometric shapes merely to appear Swiss
- Turn metadata into visual noise
- Overuse tiny type
- Copy Seed's green palette or Timeline's black-and-white treatment
- Sacrifice readability for compositional cleverness

## Cross-Format Consistency

A campaign should maintain the same visual logic without using the exact same composition at every size.

Preserve across formats:

- Headline language
- Primary color family
- Typeface register
- Image or product crop logic
- Mono metadata treatment
- One recurring alignment axis
- One recognizable proof point
- One consistent CTA

Adapt across formats:

- Number of grid columns
- Amount of copy
- Image crop
- Card count
- Type scale
- Glass opacity
- Metadata density
- CTA prominence

> Do not resize. Recompose.

## Final Layout Test

Before approving any slide or asset, verify:

1. Is there one obvious entry point?
2. Does the eye move in a deliberate order?
3. Are at least three elements aligned to shared grid lines?
4. Is there enough open space to create authority?
5. Is one element clearly dominant?
6. Can any card, label, line, or decoration be removed?
7. Does the asset still feel like IM8 without the logo?
8. Does the composition translate the Seed/Timeline level of clarity without imitating either brand?

The final visual language should feel **Swiss in structure, Seed-like in modular intelligence, Timeline-like in scientific restraint, and distinctly IM8 in color, energy, humanity, and product expression**.

***

# Website Type Scale

```css
:root {
  --display-xl: clamp(3.5rem, 7vw, 7.5rem);
  --display-lg: clamp(2.75rem, 5vw, 5.5rem);
  --heading-1: clamp(2.25rem, 4vw, 4rem);
  --heading-2: clamp(1.75rem, 3vw, 3rem);
  --heading-3: clamp(1.25rem, 2vw, 1.75rem);
  --body-lg: clamp(1.125rem, 1.4vw, 1.375rem);
  --body: 1rem;
  --label: 0.75rem;
}
```

Use fluid typography while preserving the same information hierarchy at every breakpoint.

***

# Card Architecture

Cards should feel like calm editorial information modules, not SaaS pricing cards.

Every card follows this reading sequence:

```text
MONO LABEL / NUMBER / STATUS

Clear Card Title

One short explanation.
Prefer two to four lines.

Compact proof, metric, owner or detail

OPTIONAL OUTCOME OR CONSEQUENCE
```

## Card rules

- One complete idea per card
- Use two to four cards for comparable information
- Highlight only one card in a group
- Use generous internal padding
- Align labels, titles, and bottom details consistently
- Avoid decorative icons unless they carry meaning
- Do not add a gradient to every card
- Do not place buttons on presentation cards unless the presentation is interactive
- Do not make cards resemble pricing tiers
- Give each card a beginning, point, evidence, and consequence

***

# Card Components

## Editorial Card

```css
background: #FFFFFF;
border: 1px solid rgba(80, 0, 11, 0.10);
border-radius: 20px;
box-shadow: 0 8px 28px rgba(47, 15, 18, 0.05);
```

Use for:

- Frameworks
- Responsibilities
- Briefs
- Content lanes
- Explanatory modules
- Tables and reading-heavy information

Use `#1A0205` for body copy and `#50000B` for titles.

## Light Glass Card

```css
background: rgba(255, 255, 255, 0.68);
border: 1px solid rgba(255, 255, 255, 0.72);
backdrop-filter: blur(18px) saturate(115%);
-webkit-backdrop-filter: blur(18px) saturate(115%);
border-radius: 24px;
box-shadow: 0 12px 36px rgba(47, 15, 18, 0.08);
```

Use over:

- Photography
- Neutral Salmon Wash
- Soft Warm Light
- Subtle tonal or atmospheric backgrounds

Best for hero overlays, photography captions, customer stories, pull quotes, and contextual information.

## Dark Glass Card

```css
background: rgba(26, 2, 5, 0.28);
border: 1px solid rgba(255, 255, 255, 0.18);
backdrop-filter: blur(18px) saturate(120%);
-webkit-backdrop-filter: blur(18px) saturate(120%);
border-radius: 24px;
box-shadow: 0 16px 42px rgba(26, 2, 5, 0.20);
```

Use over:

- Deep Crimson
- Signal Crimson
- Cellular Ember
- Dark photography

Use for flagship proof, high-level decisions, strategic principles, and premium modules.

Use white text and no more than one coral or salmon accent.

## Burgundy Proof Card

```css
background: #50000B;
border: 1px solid rgba(255, 255, 255, 0.12);
border-radius: 20px;
box-shadow: none;
```

Use for:

- Evidence
- Decisions
- Standards
- Risk gates
- Operating rules
- Claims or proof modules

Use white text with an optional salmon mono label.

## Highlight Card

```css
background: linear-gradient(
  135deg,
  #8A000E 0%,
  #A40011 58%,
  #D50024 100%
);
border: 1px solid rgba(255, 255, 255, 0.18);
border-radius: 20px;
box-shadow: 0 16px 38px rgba(164, 0, 17, 0.18);
```

Use only once in a group to identify:

- The recommended route
- Primary decision
- Active stage
- Central takeaway
- Selected option

Use white text.

***

# Glass Rules

Glass is a selective contextual device, not the default reading surface.

- Use glass only over gradients, images, or tonal variation
- Do not use glass over plain white
- Keep long-form reading on solid or highly opaque surfaces
- Use no more than one glass treatment in a section
- Never stack glass on glass
- Avoid blur behind charts, tables, or detailed diagrams
- Confirm contrast against the most visually active background point
- Supply an opaque fallback when `backdrop-filter` is unsupported
- Reduce or remove blur on lower-powered mobile devices
- Use background opacity before adding stronger shadows

***

# Geometry

| Component | Radius |
|---|---:|
| Tags and pills | 999 px |
| Buttons | Pill or 12–16 px |
| Compact card | 16–20 px |
| Standard card | 20–24 px |
| Hero glass panel | 28–32 px |
| Image container | 20–32 px |

Use a consistent radius system. Do not mix severe rectangles and very soft rounded cards arbitrarily.

***

# Borders and Elevation

```css
--border-default: 1px solid rgba(80, 0, 11, 0.10);
--border-dark: 1px solid rgba(255, 255, 255, 0.16);
--border-active: 1px solid #A40011;
--divider-gold: 1px solid rgba(212, 168, 75, 0.55);

--shadow-default: 0 8px 28px rgba(47, 15, 18, 0.05);
--shadow-raised: 0 16px 42px rgba(47, 15, 18, 0.10);
```

Prefer hairline borders, tonal contrast, overlap, and whitespace to heavy shadows.

***

# Buttons and Tags

## Primary button

```text
Background: #A40011
Text: #FFFFFF
Typeface: Aeonik Medium
Case: Sentence case
Shape: Pill or 14 px radius
Hover: Signal Crimson gradient
```

## Secondary button

```text
Background: Transparent or #FFFFFF
Border: #50000B
Text: #50000B
Hover background: #F5EAEA
Typeface: Aeonik Medium
```

## Evidence tag

```text
Background: #50000B
Text: #FFFFFF
Typeface: NB Architekt Mono Medium
Case: All caps
```

## Human highlight tag

```text
Background: #E85B4A
Text: #1A0205
Typeface: NB Architekt Mono Semibold
```

## Longevity tag

```text
Background: #F2C45B
Text: #1A0205
Typeface: NB Architekt Mono Semibold
```

Only use the Longevity tag for product-specific information.

***

# Motion and Interaction

- Use transitions between 180 and 300 ms
- Cards may rise 2–4 px on hover
- Increase border opacity before increasing shadow
- Allow gradients to move extremely slowly, if at all
- Reveal card content in its natural reading order
- Do not animate every card independently
- Avoid pulsing, floating, or decorative motion
- Respect reduced-motion settings
- Motion should explain hierarchy, reveal information, or support transformation

***

# Final Guardrails

Do:

- Use Aeonik as the default headline and reading face
- Use Arizona Flare only when warmth or editorial humanity adds meaning
- Use mono only for genuine evidence, metadata, and structure
- Keep most surfaces light and clean
- Use crimson as punctuation and conviction
- Connect Longevity to the brand through IM8 Red
- Use salmon for softness and Ember Coral for graphic energy
- Use full-height photography regularly
- Protect whitespace
- Let each card communicate one complete idea
- Build every asset on the Swiss grid and recompose, never resize, across formats

Do not:

- Make every headline serif
- Introduce another display font
- Use dark burgundy as the default page background
- Make every card translucent
- Put gradients inside every component
- Use salmon for small text on white
- Let orange or gold become general brand colors
- Place paragraphs across high-contrast gradient transitions
- Add icons, shadows, or pills simply to make the interface feel designed
- Shrink type to solve overcrowding
- Reproduce Seed's identity literally
- Center every element or fill every grid cell

## Final design test

Every page should answer four questions immediately:

1. What is the main idea?
2. What should I read next?
3. What evidence or detail supports it?
4. What should I remember or do?

Then run the Final Layout Test from the Swiss Grid System.

The final system should feel recognizably IM8 across very different content types without requiring every page to look the same.

***

# Sources

Reference material for the Swiss Grid System. Use these for principle, not for imitation.

1. Timeline, stores.gallery: https://stores.gallery/stores/timeline
2. Seed Brand Evolution: Microbiome Science Redefined: https://www.linkedin.com/posts/seedhealth_today-were-sharing-the-evolution-of-seed-activity-7406735547211309057-KlRy
3. Seed Three, Landscape: https://thisislandscape.com/projects/seed-three/
4. Timeline Nutrition, Lorenz Wöhr: https://dribbble.com/lw/projects/6886424-Timeline-Nutrition
5. Charles Fulford on the Seed evolution: https://www.linkedin.com/posts/charlesfulford_this-evolution-represents-whats-possible-activity-7406741851287998464-5pUe
6. Timeline Nutrition brand film, Sebastian Helene: https://www.sebastianhelene.com/work/timeline-nutrition
7. Timeline Nutrition, pelican sound: https://www.pelicansound.studio/projects/timeline-nutrition
8. Timeline Nutrition, Craftwork: https://craftwork.design/curated/website/timeline-nutrition
9. Timeline launches first national campaign, "It's About Time": https://www.timeline.com/blog/timeline-launches-first-national-campaign-it-s-about-time
10. Seed Health brand assets, Brandfetch: https://brandfetch.com/seed.com
