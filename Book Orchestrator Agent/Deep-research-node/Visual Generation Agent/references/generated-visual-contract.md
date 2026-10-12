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
- installed `review-linkedin-visual-post` verdict/locator;
- Writing Agent generated evaluator report/status;
- DATA_LOCK when applicable.

## Rendering invariants

- One subsection -> one candidate Adapt context.
- One candidate -> one standalone article-section Render context.
- The installed Render reviewer runs in a separate fresh context before the Writing Agent generated-image evidence gate.
- No batch/collage/multi-section composition.
- Use the full pinned installed Adapt, Render and Render-review packages, not paraphrased prompts.
- ChatGPT native image generation only.
- Article-section visual mode and installed reference/design/quality assets load automatically.
- Keep copy minimal enough that the article/chapter carries nuance.
- No signature or author identity block in book mode.

## Two acceptance gates

A GEN candidate enters Unified Visual Review only after both are true:

1. **Installed Render Review PASS** — the pinned `review-linkedin-visual-post` article validator/reviewer accepts visual composition, hierarchy, readability and article-mode quality.
2. **Writing Agent Generated Visual PASS** — `generated_visual.yaml` accepts factual fidelity, selected-mode fit, explanatory value, render accuracy and DATA_LOCK compliance.

A failure at either gate consumes that complete render attempt. Do not patch or inpaint a rejected candidate; regenerate a complete candidate according to the pinned Render skill.

## Evidence invariants

- No new research.
- No invented statistic or label.
- No stronger factual claim than the Deep Research evidence supports.
- Humour may clarify but never change the claim.
- A GEN image may explain evidence but cannot be cited as evidence.

## Retry/immutability

Maximum two complete render attempts per GEN candidate across both acceptance gates.

After a generated asset passes both gates and enters Unified Visual Review, preserve that exact asset.

After human `KEEP`, Visual Placement must insert the exact reviewed asset and must never regenerate/reinterpret it.
