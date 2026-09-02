---
description: Design or diagnose a content operating system that ships at volume across channels
argument-hint: [the operation, its volume target, and what is breaking]
---

Design the content operating system for: $ARGUMENTS

Work through it in this order, using the `content-engine-architecture` skill
as the spine:

1. Separate the lanes by cost of being wrong, not by channel.
2. Name an owner and an SLA for each of the nine stages, per lane.
3. Place the claims gate at approved script or locked copy — apply the
   `health-claim-gate` skill for the tiering.
4. Show where editors, freelancers, agencies, creators and AI each sit.
5. Define the metadata schema, since measurement depends on it.
6. Allocate capacity with the `tentpole-allocation` skill, protecting the
   always-on floor before planning tentpoles.

Finish with the three most likely failure points in this specific operation
and the control that catches each one.
