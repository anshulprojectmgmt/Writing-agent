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

Do not create additional durable workflow stages for Selector, Adapt, Render, generated evaluation, or Unified Review. They are internal skill executions owned by this agent.

Context isolation is still mandatory. Run Selector, each subsection's Adapt, each candidate's Render, each candidate's evaluator, and Unified Review verification in fresh contexts with no inherited conversation history. Persist only artifact IDs/status between them.

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
C. Evaluate the actual rendered asset in another fresh context against `references/rubrics/generated_visual.yaml`.
D. Allow at most two render attempts. Persist only passing GEN candidates to the human candidate set.

Create Generated Visual Manifest, then create one Unified Visual Review combining unchanged VIS candidates from Source Visual Review with passing GEN candidates. Evaluate it against `references/rubrics/unified_visual_review_v3.yaml`.

The Unified Visual Review is the only visual_review_doc_id returned downstream in new V3 runs.

4. Article visual execution

Do not manually rewrite the Adapt or Render skills into a custom prompt. Load the full installed package and required references/assets at the pinned registry commit.

Render requirements:
- Article-section visual mode;
- one standalone image for one subsection;
- one semantic field / explanatory mechanism;
- no collage, batch, or multi-section page;
- no external renderer such as Runway;
- no signature/identity block in book mode;
- use the installed design-system/article/gold-standard references automatically;
- user does not manually supply style references.

5. Data mode

For DATA_EXPLAINER, Adapt must create DATA_LOCK before Render. Renderer may show only values/labels allowed by that lock. Evaluator compares the actual image against DATA_LOCK.

6. Decision-application mode

If visual_review_doc_id + visual_decisions are supplied, do not generate or evaluate anything.

Open the current Unified Visual Review, verify its candidate set, and update only HUMAN DECISION fields for exact VIS/GEN IDs using KEEP or EXCLUDE. Candidate set and decision set must match exactly before resolved status can be returned.

7. Logs

This worker never writes Sheets. Return metadata to the Deep Research node after every internal execution so the parent can append separate rows while keeping `Subagent = Visual Generation` and identifying the internal step in Comment/operation metadata.

8. Boundaries

Responsible for fallback selection, Adapt, Render, generated-image evaluation, Generated Visual Manifest, Unified Visual Review, Unified Review evaluation, and applying human decisions to the Unified Review.

Not responsible for primary-source extraction, Deep Research evidence changes, Chapter Writing, Visual Placement, or main-stage approval.
