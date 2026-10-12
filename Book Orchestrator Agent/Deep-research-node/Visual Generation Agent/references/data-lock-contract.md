# DATA_LOCK Contract

Required only for `DATA_EXPLAINER`.

Before rendering, Adapt must emit a locked table of every numeric or categorical value allowed to appear in the image.

For each item record:
- `LABEL`
- `EXACT_VALUE`
- `SOURCE_OR_EVIDENCE_LOCATOR`
- `ALLOWED_ON_IMAGE_WORDING`
- `CAVEAT` when material

Rules:
- Render may not introduce another number, category, date, percentage, ratio, ranking, or benchmark.
- Render may not round or restate a value unless the lock explicitly permits it.
- Generated Visual Evaluate compares the actual rendered raster against the lock.
- Any changed/invented value is a hard failure and requires a new render attempt.
- DATA_LOCK is evidence control, not reader-facing chapter content.
