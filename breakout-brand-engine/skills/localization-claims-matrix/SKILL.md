---
name: localization-claims-matrix
description: Adapt content across many markets where permitted claims, not just language, differ by jurisdiction. Use when shipping to multiple countries, planning localisation capacity, or discovering that approved home-market copy cannot run abroad. For the home-market gate, use `health-claim-gate`.
---

# Localization Claims Matrix

Localisation is usually planned as a translation cost. In regulated
categories it is a *claims* problem wearing a translation costume: the same
sentence can be substantiated and lawful in one market and prohibited in
another regardless of how well it is translated.

Teams discover this late, typically when a well-performing asset is rolled
out internationally and stopped. Building the matrix early converts a
recurring crisis into a routine production input.

This skill describes the operating system, not the law of any jurisdiction.
Every market position must be confirmed with local regulatory counsel.

## Why translation is the smaller half

A rough map of how much the ground moves:

- **United States** — structure/function claims permitted without
  pre-approval, with substantiation obligations and the required disclaimer.
  See `health-claim-gate`.
- **European Union** — nutrition and health claims are governed by Regulation
  (EC) No 1924/2006, under which only claims authorised on the EU Register
  may be used, in the authorised wording or wording with the same meaning.
  This is a fundamentally different model: permission is granted per claim,
  not asserted with substantiation held in reserve. Much US-legal supplement
  copy simply has no EU equivalent.
- **United Kingdom** — a comparable authorised-list model operating
  separately post-Brexit.
- **Canada, Australia and others** — product-licensing regimes where the
  product itself is authorised and permitted claims flow from that licence.

The consequence for a content operation is structural: you cannot maintain
one global claims library. You maintain a claim set per market cluster, and a
single asset may need genuinely different copy — not translated copy — per
cluster.

## Build the matrix

Rows are claims. Columns are market clusters. Each cell holds one of:

- **Approved** — with the exact permitted local wording
- **Approved with variation** — the local wording differs materially; store it
- **Not permitted** — with the nearest permissible alternative, if any
- **Unreviewed** — treated as not permitted until cleared

Cluster markets by regulatory regime rather than by language. Spanish for
Spain and Spanish for Mexico share a language and not a claims regime;
treating them as one market is a common and costly error.

## Design assets for adaptability

Once the matrix exists, production changes upstream. Cheap adaptation comes
from decisions made at shoot and edit time:

- **Keep claim language out of burned-in visuals.** Text baked into a frame
  turns a copy swap into a re-edit.
- **Separate claim-bearing and claim-free segments** so a market that cannot
  run a claim can drop a segment rather than lose the asset.
- **Shoot claim-neutral coverage** — footage that carries the idea without
  asserting a benefit is the most portable inventory you own.
- **Record voiceover separately from music and effects** so audio localises
  without a remix.

These are `asset-multiplication` decisions, and they are the difference
between a global asset library and a US library with expensive foreign
cousins.

## Transcreation, not translation

For hooks, humour, idiom and cultural reference, literal translation reliably
underperforms. Brief a local writer with the *intent* — the tension, the one
thing, the objection being answered — and let the execution differ. Send the
concept, not the sentence.

Retain the distinctive assets across markets even as language changes: codes
travel where copy cannot. See `distinctive-assets`.

## Operating the matrix

Assign an owner per cluster, and attach market clearance to asset metadata so
distribution can be gated automatically rather than by memory. Re-review on a
fixed cadence and immediately on regulatory change; when a claim is
withdrawn in a market, metadata is what lets you find every live asset
carrying it.

Plan capacity honestly: localisation of a claim-bearing asset is a review
cycle plus an edit, not a subtitle pass. Budget it in `tentpole-allocation`
as real production work, because that is what it is.
