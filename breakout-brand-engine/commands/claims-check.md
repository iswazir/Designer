---
description: Review copy, a script or a finished asset for health-claim risk before production
argument-hint: [the copy, script or asset description to review]
---

Review for claims risk: $ARGUMENTS

Apply the `health-claim-gate` skill. Specifically:

1. Assign a claim tier and say what routing that implies.
2. Assess the net impression of the whole asset, including visuals, music,
   testimonials and sequence — not the literal wording alone.
3. Flag the recurring failure patterns: stacking, testimonial claims, visual
   implication, paraphrase drift, missing endorsement disclosure.
4. For each flagged span, offer a rewrite using the `claim-to-copy` skill
   that keeps the emotional force without widening the claim's scope.
5. Note any market where this could not run, per the
   `localization-claims-matrix` skill.

Flag and explain; do not approve. Sign-off is a human decision, and this
review is not legal advice.
