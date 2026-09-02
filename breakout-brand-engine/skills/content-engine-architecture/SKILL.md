---
name: content-engine-architecture
description: Design the end-to-end system that ships content at volume across channels with different quality bars. Use when building a content operation, diagnosing why output stalls, or documenting a workflow from brief to measurement. For allocating finite capacity across it, use `tentpole-allocation`.
---

# Content Engine Architecture

An engine that ships thousands of assets a month is not one workflow run
faster. It is two or three workflows with different tolerances, sharing
inputs, and the single most common design failure is forcing high-volume and
high-stakes work through the same gates. Route a paid-social variant through
a brand-film approval chain and throughput collapses; route a billboard
through a paid-social chain and something reaches a motorway that shouldn't.

## Separate the lanes first

Define lanes by *cost of being wrong*, not by channel or team.

| Lane | Examples | Reversibility | Gate design |
|---|---|---|---|
| Fast | Paid social variants, organic reactive | Kill in minutes | Automated checks, spot audit |
| Considered | New concepts, CRM, retail | Days to unwind | Named reviewer, fixed SLA |
| Irreversible | TV, OOH, ambassador, PR | Cannot unwind | Full chain, legal, sign-off |

Assets move *up* lanes freely and *down* never. A social cutdown of a
high-stakes film inherits that film's clearances; it does not get re-judged
as fast-lane work.

## The nine stages

Every asset passes some subset. Name an owner for each stage in each lane —
ambiguity here is where days disappear.

1. **Intake** — demand arrives with a channel, a date, and a reason
2. **Brief** — one page per `concept-brief`
3. **Production** — shoot, design, or generate
4. **Assembly** — edit, version, adapt
5. **Claims and compliance** — see `health-claim-gate`
6. **Brand review** — codes and voice, per `distinctive-assets`
7. **Localisation** — see `localization-claims-matrix`
8. **Distribution** — trafficking, naming, metadata
9. **Measurement** — read back into concepts, per `performance-creative-ladder`

Stage 5 is the one to place carefully. Run it too early and you review copy
that changes; too late and you rework finished assets. The workable position
is *at approved script or locked copy* — before pixels, after wording is
final.

## Where each maker sits

- **In-house editors** — highest-context work: new concepts, brand-critical
  assembly, and anything defining the quality bar others copy.
- **Freelancers** — surge capacity on well-defined derivative work. They need
  the strongest briefs, because they have the least context.
- **Agencies** — capability you shouldn't build in-house: high-end
  production, specialist formats.
- **Creators** — origination in their own voice. Briefing them like editors
  destroys the thing you hired them for.
- **AI** — variant generation, first-pass localisation, tagging, QA sweeps.
  See `ai-production-pipeline` for where it must stop.

## Metadata is the engine's real infrastructure

Every asset needs concept, entry point, hook family, lane, claim set, talent,
market, and version encoded at creation — not at reporting time. Without
this, measurement degrades into ranking individual files, and you cannot
learn anything transferable. Naming conventions are unglamorous and they
determine whether the whole system compounds or just runs.

## Diagnose a stalled engine

Throughput problems are almost always one of four things, in this order of
likelihood: briefs that arrive incomplete, a single named approver in the
critical path, missing derivative plans forcing re-shoots, or a review stage
placed after the expensive work rather than before it. Measure stage
dwell-time before adding people — capacity is rarely the binding constraint.
