# Unified Visual Review Format

Create one section for every approved chapter subsection in Blueprint/Research Mapping order.

## Source candidates

For every carried-forward primary-source candidate:

`VIS ID: VIS-###`
`ORIGIN: PRIMARY_SOURCE`
`SUBSECTION: <id/title>`
`IMAGE STATUS: FOUND`
`EXTRACTION STATUS: EXTRACTED | SOURCE-LINKED`
`PRIMARY SOURCE: <exact URL/title/owner>`
`FIGURE LOCATOR: <exact locator>`
`AI RECOMMENDATION: RECOMMEND | SKIP`
`ASSET: <Drive asset ID/path when extracted>`
`HUMAN DECISION: PENDING`

Preserve the actual visual preview when available.

## Generated candidates

For every passing generated candidate:

`GEN ID: GEN-###`
`ORIGIN: GENERATED_EXPLAINER`
`SUBSECTION: <id/title>`
`MODE: DATA_EXPLAINER | TOPIC_EXPLAINER | HUMOUR_METAPHOR`
`EVIDENCE BASIS: <Deep Research locator(s)>`
`ADAPT BRIEF: <locator>`
`RENDER ASSET: <exact Drive asset ID/path>`
`GENERATED EVALUATION: PASS`
`DATA_LOCK: <summary or N/A>`
`HUMAN DECISION: PENDING`

Embed/show the exact generated visual that the human is deciding on.

## Subsection with no candidate

If there is no VIS candidate and generation failed, state:

`SOURCE VISUAL: NOT FOUND`
`GENERATED VISUAL: GENERATION FAILED`
`REASON: <concise verified reason>`

No Human Decision field is required when no candidate exists.

## Rules

- VIS and GEN IDs must be globally unique within the review.
- Do not turn GEN images into evidence/source citations.
- Do not hide SOURCE-LINKED or failed-generation states.
- Every actual candidate starts PENDING in a newly created review.
- Human may KEEP both a VIS and GEN candidate for the same subsection, keep one, or exclude both.
- Do not include evaluator chain-of-thought or workflow prose in the reader-facing chapter; this review is an audit artifact only.
