---
name: performance-creative-ladder
description: Run the concept to test to scale pipeline on a large live ad account, and manage fatigue without flooding it with near-duplicates. Use when designing creative testing, deciding what graduates to scale, or diagnosing declining account performance. For generating the concepts entering it, use `category-entry-points`.
---

# Performance Creative Ladder

A large ad account fails in one of two directions: starved, because testing
is too slow, or drowned, because every idea gets scaled and nothing is
learned. The ladder exists to make graduation a decision with criteria rather
than a reaction to yesterday's numbers.

## The four rungs

**1. Concept.** A structurally distinct idea — new entry point, new hook
family, or a new objection answered. Cosmetic variants do not enter here.

**2. Test.** Clean read against a control. Fixed budget, fixed duration,
decided before launch. The discipline that matters most: define the kill
criterion in writing before the test runs, because after it runs everyone can
see a reason to keep going.

**3. Scale.** Graduated concepts get spend and derivative production —
cosmetic variants, format adaptations, localisation.

**4. Evergreen.** The rare concept that holds for quarters. Protect it,
refresh it cosmetically, and never let it become the only thing working.

Movement is not one-way. A scaled concept whose efficiency decays returns to
test with a variation hypothesis rather than being killed outright — you
usually learn more from why it decayed than from a new concept.

## Test cleanly

Three failures make most creative tests unreadable:

- **Confounded variables.** Changing hook and offer together teaches nothing.
- **Underpowered reads.** Calling a winner on a difference the sample cannot
  support, then scaling into noise.
- **Optimising the same metric you judge on.** If the platform optimises
  delivery toward a metric, that metric is partly an artefact of delivery,
  not a property of the creative.

Where you can, validate the biggest graduations against an incrementality
read rather than platform-reported performance alone. Platform attribution
systematically flatters creative that reaches people who would have converted
anyway — see `creative-unit-economics`.

## Fatigue

Fatigue is a portfolio property, not an asset property. Track it at concept
level: when a concept's whole family decays together, that is genuine
fatigue; when one asset decays while siblings hold, that is asset-level wear
and a cosmetic refresh will do.

Two practical controls:

- **Structural diversity floor.** Maintain live coverage across a minimum
  number of hook families and entry points, so the account can never be
  simultaneously fatigued.
- **Refresh before collapse.** Schedule refreshes on a decay curve, not on a
  performance alarm. Reacting to collapse means running degraded creative for
  the whole detection window.

## Turn data into insight, not variations

The low-value read is "the version with the number in the hook won, make
more with numbers." The high-value read asks *what the win revealed about the
customer* — and that read belongs upstream.

If demonstration hooks consistently beat testimonial hooks, the finding is
not a hook preference. It is that the audience's binding objection is
credibility, not relevance — which should change the brand film, the OOH
line, and what you ask an ambassador to do on camera. Route these findings
into `mental-model-audit` and `objection-ladder` on a fixed cadence, or they
stay trapped in the ad account.

## Cadence

Weekly: test reads and graduations. Monthly: concept-level fatigue and
diversity audit. Quarterly: upstream insight review with brand, so
performance learning actually reaches the work it should change.
