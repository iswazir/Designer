---
name: health-claim-gate
description: Run the claims and compliance gate for health, supplement and wellness content so benefit language is substantiated before production. Use when writing or reviewing any copy that says what a product does to the body, briefing talent scripts, or designing an approval chain. For writing the language itself, use `claim-to-copy`.
---

# Health Claim Gate

In a regulated category the claims gate is not a legal checkbox at the end of
the process. It is an operating stage with a position, an owner, and a
turnaround time — and putting it in the right place is the difference between
reviewing sentences and reworking finished films.

Place it at **approved script or locked copy**: after wording is final,
before anything expensive is made.

This skill describes the operating gate. It is not legal advice, and nothing
here replaces qualified counsel or your regulatory team — its purpose is to
make sure the right things reach them, early, in a reviewable form.

## The two regimes to hold in your head

**Substantiation (FTC).** The FTC's Health Products Compliance Guidance,
issued December 2022, replaced the 1998 dietary supplements guide and covers
foods, supplements, over-the-counter drugs and health apps. Health-benefit
claims generally require randomised, controlled human clinical trials to meet
the "competent and reliable scientific evidence" standard. No fixed number of
trials is required — quality outweighs quantity, though independent
replication strengthens the weight of evidence. High-quality epidemiological
evidence is accepted only in limited cases where experts consider it an
acceptable substitute and trials are not feasible. Animal and in vitro
studies alone are not sufficient; they can support, but not substantiate.

**Claim type (FDA / DSHEA).** Structure/function claims — describing an
effect on the normal structure or function of the body — are permitted for
dietary supplements without pre-approval, and must carry the disclaimer:

> This statement has not been evaluated by the Food and Drug Administration.
> This product is not intended to diagnose, treat, cure, or prevent any
> disease.

Where multiple such statements appear, the plural form ("These statements
have not been evaluated…") may be used. The disclaimer must be prominent, in
boldface, and placed adjacent to the statement or linked by a symbol such as
an asterisk. Note that in December 2025 the FDA signalled enforcement
discretion regarding the requirement that the disclaimer appear on *each
panel* of a label while it considers amending the rule — confirm the current
position with your regulatory team rather than relying on this note.

Disease claims — stating or implying that a product diagnoses, treats, cures,
prevents or mitigates a disease — move a product into drug territory. This is
the line that ordinary marketing language crosses accidentally.

## Net impression is the standard that catches teams out

Compliance is assessed on the overall impression a reasonable consumer takes
from the whole asset — visuals, music, testimonials, on-screen text, and
sequence — not on the literal wording alone. An asset composed entirely of
individually permissible elements can still convey an impermissible claim.

The practical consequence: **review finished assets, not scripts only.** A
script that passes and an edit that doesn't is a common and expensive
discovery.

## Claim tiers

Route by risk. This is what lets the gate be fast for most work.

| Tier | Content | Route | Target SLA |
|---|---|---|---|
| 0 | No benefit language — brand, lifestyle, product visuals only | Editor self-check against list | Immediate |
| 1 | Approved claim used verbatim from the claims library | Automated string check | Immediate |
| 2 | New phrasing of an existing substantiated claim | Named reviewer | 24 hours |
| 3 | New claim, new evidence, or comparative claim | Regulatory and legal | Defined, longer |
| 4 | Anything touching disease, diagnosis, or medical context | Full review, senior sign-off | No shortcut |

Most volume is tiers 0 and 1, which is exactly why the claims library
matters more than the review queue.

## The claims library

The single highest-leverage artefact in a regulated content operation: every
approved claim, in approved wording, with its substantiation reference,
its permitted contexts, its required disclosures, and its expiry or review
date.

With it, most assets never need review — they use cleared language verbatim.
Without it, every asset is a bespoke legal question and the gate becomes the
bottleneck that the whole operation routes around.

Version it. When evidence changes or a claim is retired, you need to find
every live asset using it, which requires claim identifiers in asset
metadata — see `content-engine-architecture`.

## Recurring failure patterns

- **Stacking.** Individually permissible statements that, together, describe
  a diagnosable condition.
- **Testimonials.** Genuine customer stories describing recovery. Sincerity
  is not a defence; a testimonial conveying a claim is a claim, and typical
  results and disclosure obligations apply.
- **Visual implication.** Clinical settings, white coats, stethoscopes,
  charts — imagery that implies medical endorsement the brand doesn't have.
- **Paraphrase drift.** Approved language reworded between brief and export.
  This is why claims text belongs verbatim in the must-include field of
  `concept-brief`.
- **Endorsement disclosure.** Material connections must be disclosed clearly
  and conspicuously. A high-profile endorser increases scrutiny — see
  `founder-signal`.
- **Comment sections.** Responses from brand accounts can create claims, and
  amplifying a customer's disease claim can adopt it.

## Where AI must stop

Generation and first-pass screening are useful; sign-off is not delegable.
Use models to flag risky language, check approved-claim strings, and sweep
libraries for retired claims — then have a human decide. A model's confident
approval of a borderline claim is worse than no check, because it manufactures
false assurance at the exact point where the cost of being wrong is highest.
See `ai-production-pipeline`.

## Sources

- [FTC announces new business guidance for marketers and sellers of health products](https://www.ftc.gov/news-events/news/press-releases/2022/12/ftc-announces-new-business-guidance-marketers-sellers-health-products)
- [FTC issues new guidance on health-related claims — Covington](https://www.cov.com/en/news-and-insights/insights/2023/01/ftc-issues-new-guidance-on-health-related-claims-to-replace-the-dietary-supplements-advertising-guide)
- [FTC revises Health Products Compliance Guidance — Cooley](https://www.cooley.com/news/insight/2023/2023-03-02-ftc-revises-health-products-compliance-guidance)
- [Structure/function and related claims for dietary supplements — NPA](https://www.npanational.org/education/structure-function-and-related-claims-for-dietary-supplements/)
- [FDA notifies industry of enforcement discretion regarding the DSHEA disclaimer](https://www.hlc.com/en/publications/fda-notifies-industry-of-enforcement-discretion-regarding-dshea-disclaimer-on-dietary)
