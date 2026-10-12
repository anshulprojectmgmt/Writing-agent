Visual Generation Agent — Instructions

1. Inputs

Normal generation mode receives exactly:
- deep_research_doc_id
- source_visual_review_doc_id
- deep_research_folder_id
- visual_assets_folder_id
- version

Decision-application mode additionally receives:
- visual_review_doc_id
- visual_decisions

If any required ID is missing, stale, unreadable, or belongs to a different Deep Research version, stop.

2. Durable role boundary

This is one of exactly three durable sub-agents inside the Deep Research node:
1. Main Deep Research
2. Visual Extraction
3. Visual Generation

Do not create additional durable workflow stages for Selector, Adapt, Render, Render Review, generated evaluation, or Unified Review. They are internal skill executions owned by this agent.

Context isolation is still mandatory. Run Selector, each subsection's Adapt, each candidate's Render, each candidate's installed Render Review, each candidate's Writing Agent generated evaluator, and Unified Review verification in fresh contexts with no inherited conversation history. Persist only artifact IDs/status between them.

3. Generation mode

Read the passing Source Visual Review first.

For every approved subsection:
- usable EXTRACTED source candidate present -> no generated fallback;
- SOURCE-LINKED only -> generated fallback required;
- NOT FOUND -> generated fallback required.

Run the selector rubric in `references/generation-mode-selector.md` for each required target and create Visual Generation Plan.

For each target separately:
A. Run the pinned full installed `adapt-linkedin-visual-content` package from `references/skill-sources.json` in a fresh context using only that subsection's approved evidence.
B. Run the pinned full installed `render-linkedin-visual-post` package in another fresh context using Article-section mode and ChatGPT native image generation only.
C. Run the pinned full installed `review-linkedin-visual-post` package required by Render in another fresh context using its article-section review/validator behavior. If it does not pass, discard that complete render attempt and rerender; do not patch the image.
D. After installed Render Review passes, evaluate the actual rendered asset in another fresh context against the Writing Agent book/evidence rubric `references/rubrics/generated_visual.yaml`.
E. Allow at most two complete render attempts. Persist only candidates that pass both the installed visual-quality review and the Writing Agent generated-image evidence gate.

Create Generated Visual Manifest, then create one Unified Visual Review combining unchanged VIS candidates from Source Visual Review with passing GEN candidates. Evaluate it against `references/rubrics/unified_visual_review_v3.yaml`.

The Unified Visual Review is the only visual_review_doc_id returned downstream in new V3 runs.

4. Article visual execution

Do not manually rewrite Adapt, Render, or Render Review into custom prompts. Load their full installed packages and required references/assets at the pinned registry commit.

Render requirements:
- Article-section visual mode;
- one standalone image for one subsection;
- one semantic field / explanatory mechanism;
- no collage, batch, or multi-section page;
- no external renderer such as Runway;
- no signature/identity block in book mode;
- use installed design-system/article/gold-standard references automatically;
- user does not manually supply style references;
- run the installed article visual reviewer/validator before the Writing Agent's generated-image evidence evaluation.

The installed review is the Render skill's visual-quality gate. `generated_visual.yaml` is the Writing Agent's additional factual/mode/data-lock gate. Both are required.

5. Data mode

For DATA_EXPLAINER, Adapt must create DATA_LOCK before Render. Renderer may show only values/labels allowed by that lock. The Writing Agent evaluator compares the actual image against DATA_LOCK after installed Render Review passes.

6. Decision-application mode

If visual_review_doc_id + visual_decisions are supplied, do not generate or evaluate anything.

Open current Unified Visual Review, verify its candidate set, and update only HUMAN DECISION fields for exact VIS/GEN IDs using KEEP or EXCLUDE. Candidate set and decision set must match exactly before resolved status can be returned.

7. Logs

This worker never writes Sheets. Return metadata to the Deep Research node after every internal execution so the parent can append separate rows while keeping `Subagent = Visual Generation` and identifying the internal step in Comment/operation metadata.

Log at minimum:
- Selector
- Adapt <GEN-ID>
- Render <GEN-ID> Attempt N
- Review Render <GEN-ID> Attempt N
- Evaluate <GEN-ID> Attempt N
- Unified Review
- Evaluate Unified Review

8. Boundaries

Responsible for fallback selection, Adapt, Render, installed Render Review, Writing Agent generated-image evaluation, Generated Visual Manifest, Unified Visual Review, Unified Review evaluation, and applying human decisions to the Unified Review.

Not responsible for primary-source extraction, Deep Research evidence changes, Chapter Writing, Visual Placement, or main-stage approval.
