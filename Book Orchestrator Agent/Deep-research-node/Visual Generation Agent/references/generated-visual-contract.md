# Generated Visual Production Contract

A generated visual is an explanatory artifact derived from already-approved subsection evidence. It is never a new evidence source.

## Candidate identity

Use stable IDs: `GEN-001`, `GEN-002`, ...

Each GEN record must bind to exactly one approved subsection and one current Deep Research version.

## Required provenance

Every GEN candidate records:
- subsection;
- selected mode;
- Deep Research evidence locator(s);
- Adapt Visual Story Brief locator;
- Render skill/package version;
- rendered asset ID/path;
- render attempt;
- evaluator report/status;
- DATA_LOCK when applicable.

## Rendering invariants

- One subsection -> one candidate render context.
- One candidate -> one standalone article-section image.
- No batch/collage/multi-section composition.
- Use the full pinned installed Adapt and Render packages, not a paraphrased prompt.
- ChatGPT native image generation only.
- Article-section visual mode and installed reference/design/quality assets load automatically.
- Keep copy minimal enough that the article/chapter carries nuance.
- No signature or author identity block in book mode.

## Evidence invariants

- No new research.
- No invented statistic or label.
- No stronger factual claim than the Deep Research evidence supports.
- Humour may clarify but never change the claim.
- A GEN image may explain evidence but cannot be cited as evidence.

## Retry/immutability

Maximum two render attempts per GEN candidate.

After a generated asset passes evaluation and enters Unified Visual Review, preserve that exact asset.

After human `KEEP`, Visual Placement must insert the exact reviewed asset and must never regenerate/reinterpret it.
