---
name: ai-production-pipeline
description: Embed AI into content production with real prompts, evaluation and defined limits rather than a tool list. Use when scaling output with AI, designing prompts for variant generation or QA, or deciding where models must not be trusted. For the claims sign-off AI cannot perform, use `health-claim-gate`.
---

# AI Production Pipeline

AI earns its place in a content operation at specific stages, with specific
inputs, measured against a bar. The failure pattern is treating it as a
general accelerant: output volume rises, win rate falls, and the team spends
its savings on triage.

Design it as pipeline stages with entry conditions and quality gates, exactly
as you would a human stage in `content-engine-architecture`.

## Where AI genuinely pays

Ordered by reliability:

1. **Tagging and metadata** — classifying existing assets by concept, hook
   family, entry point, claim set. Highest reliability, immediate compounding
   value, and it fixes the measurement problem most operations have.
2. **Library QA sweeps** — finding assets carrying retired claims, missing
   disclosures, or expired talent rights. Recall matters more than precision
   here; a human confirms.
3. **Variant generation** — cosmetic variation on proven winners. Reliable
   because the concept is already validated.
4. **First-pass localisation** — draft transcreation for a local writer to
   correct. Never a final pass in a claims-bearing market.
5. **Ideation breadth** — generating candidate angles for humans to select
   from. Valuable for coverage, weak at judgement.

## Where it must not go

- **Claims sign-off.** Never. A confident wrong approval is worse than no
  check, because it manufactures assurance precisely where error is most
  expensive.
- **Final ambassador or talent work.** Likeness, rights and relationship risk
  are not model-legible.
- **Irreversible assets.** TV and out-of-home get human craft end to end.
- **Deciding what a performance result means.** Models extrapolate from
  patterns; the valuable read is usually a causal hypothesis about a customer,
  which is a human judgement — see `performance-creative-ladder`.

## Prompts that work in production

Production prompts differ from ad-hoc ones in three ways: they carry the
voice artefact, they constrain scope explicitly, and they ask for a structured
output that a pipeline can consume.

**Variant generation.** Supply the winning asset's transcript, the concept's
one thing, the approved claim strings verbatim, and the lexicon from
`voice-codification`. Constrain hard: vary only the specified dimension, reuse
claim strings exactly, never introduce a benefit statement. Ask for a table
with a column stating which dimension was varied — that column is what makes
the output auditable and stops cosmetic variants being logged as concepts.

**Claims risk screening.** Supply the full asset — script, on-screen text, and
a description of visuals and audio, since net impression is not a text
property. Ask for flagged spans, the reason, and a severity, with an explicit
instruction to flag rather than resolve. Screening prompts should be tuned for
recall: a missed risk costs more than a false flag a human clears in seconds.

**Metadata extraction.** Supply the asset and the controlled vocabulary.
Require output restricted to that vocabulary, with an explicit "uncertain"
value — models asked to classify without an escape hatch will invent
confidence, and a wrong tag silently corrupts every downstream measurement.

**Transcreation drafting.** Supply the concept intent rather than the source
sentence, plus the market's permitted claim wording from
`localization-claims-matrix`. Ask for three options at different distances
from the original, with a note on what each sacrifices.

## Evaluate, don't trust

Every AI stage needs a bar and a periodic check against it. Hold out a sample,
have a human grade it, and track the pass rate over time — models change
underneath you, and prompt performance drifts even when the prompt doesn't.

Version prompts like code, with a changelog. An undocumented prompt change
that degrades output is nearly impossible to diagnose from the symptoms, which
show up as a vague sense that quality slipped.

## Be honest about the economics

Measure AI stages on cost per *winning* asset, not on volume produced. A stage
that triples output and halves win rate has made the operation worse and
busier. `creative-unit-economics` is the check that keeps enthusiasm accountable.
