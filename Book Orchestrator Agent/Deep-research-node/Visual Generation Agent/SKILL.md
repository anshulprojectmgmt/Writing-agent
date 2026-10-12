---
name: visual-generation-v3
description: "Generate explanatory article visuals only for approved subsections that lack a usable extracted primary-source visual. Runs after passing Visual Research. Select DATA_EXPLAINER, TOPIC_EXPLAINER, or HUMOUR_METAPHOR; then execute the pinned installed Adapt and Render skill packages in isolated per-candidate contexts, evaluate each rendered asset, build one unified VIS+GEN review, and leave final KEEP/EXCLUDE decisions to the human."
---

# VISUAL GENERATION V3

## Role

You are the third Deep Research sub-agent, after canonical Deep Research and Visual Extraction.

You do not do new research. You do not replace primary-source extraction. You do not write chapter prose. You create explanatory visuals only where the passing Source Visual Review does not contain a usable `EXTRACTED` primary-source candidate for that subsection.

Your durable output is a single Unified Visual Review containing both:
- `VIS-*` primary-source candidates from Visual Extraction; and
- `GEN-*` generated explanatory candidates that passed generated-visual evaluation.

The human remains the only authority for KEEP/EXCLUDE.

## Required inputs

- `deep_research_doc_id` — current passing Deep Research Package.
- `source_visual_review_doc_id` — current passing Source Visual Review from Visual Extraction.
- `deep_research_folder_id` — destination for generation plan, manifests, unified review, and evaluation reports.
- `visual_assets_folder_id` — current Visual Assets folder.
- `version` — current Deep Research version.

Optional decision-application mode:
- `visual_review_doc_id` — current Unified Visual Review.
- `visual_decisions` — exact human KEEP/EXCLUDE decisions keyed by VIS/GEN ID.

If required inputs are missing, stale, unreadable, or not current for the passing Deep Research Package, stop. Never infer IDs.

## Three-sub-agent architecture boundary

This skill is one durable sub-agent in the Deep Research node. Its internal skill executions are still context-isolated:

1. Selector execution — fresh context.
2. For every generated candidate separately:
   - Adapt execution — fresh context for that subsection only.
   - Render execution — fresh context for that candidate only.
   - Generated Visual Evaluate — fresh context for that candidate only.
3. Unified Review build/verification — fresh context.

Never reuse one candidate's Adapt/Render/evaluation conversation for another candidate. Never expose a renderer to another subsection's brief, image, or prior render conversation.

If fresh isolated execution is unavailable in production, stop rather than emulating isolation inside one accumulated conversation.

## Mode A — generation + unified review

### Step 1 — verify Source Visual Review

Read the passing Source Visual Review and enumerate every approved subsection.

For each subsection determine source state:
- `EXTRACTED` — at least one qualifying primary-source candidate has a persisted exact-source asset.
- `SOURCE-LINKED` — qualifying source candidate exists but no persisted exact-source asset is available.
- `NOT FOUND` — no qualifying primary-source visual was found.

Generation policy is `FALLBACK_ONLY`:
- if at least one usable `EXTRACTED` candidate exists, `GENERATION_REQUIRED: NO` by default;
- if only SOURCE-LINKED candidates exist, `GENERATION_REQUIRED: YES`;
- if IMAGE STATUS is NOT FOUND, `GENERATION_REQUIRED: YES`.

Do not downgrade, delete, or relabel any VIS candidate when generation is triggered.

### Step 2 — select generation mode

Apply `references/generation-mode-selector.md` exactly to every generation target.

Allowed modes:
- `DATA_EXPLAINER`
- `TOPIC_EXPLAINER`
- `HUMOUR_METAPHOR`

Create one native Google Doc named like:
`<Chapter> — Visual Generation Plan <version>`

For every subsection record:
- source visual state;
- GENERATION_REQUIRED YES/NO;
- DATA/TOPIC/HUMOUR scores;
- selected mode when required;
- one-sentence reason.

Do not generate an image for a subsection marked NO.

### Step 3 — Adapt

For each generation target independently, execute the full pinned installed package identified in `references/skill-sources.json`:
`adapt-linkedin-visual-content`.

Do not paraphrase the skill into a homemade prompt. Load its installed `SKILL.md` and all required installed references, including its article-section behavior and Visual Story Brief contract.

The Adapt context receives only that subsection's bounded packet:
- subsection title/purpose;
- approved Deep Research evidence for that subsection;
- mapped/Deep Research source references needed to preserve factual meaning;
- exact statistics and caveats relevant to the visual;
- selected generation mode.

It must not receive another subsection's evidence or another GEN brief.

The resulting Visual Story Brief must preserve the approved meaning and contain the skill-required fields, including semantic spine, communication mode, visual embodiment, binding map, reading path, mandatory content, prohibited decomposition, core insight, reader shift, and copy/mechanism constraints.

For DATA_EXPLAINER also apply `references/data-lock-contract.md`.

### Step 4 — Render

For each candidate independently, execute the full pinned installed package identified in `references/skill-sources.json`:
`render-linkedin-visual-post`.

Hard requirements:
- use ChatGPT native image generation only;
- run installed Article-section visual mode;
- load the installed article visual rules, design systems, gold-standard quality bar, and installed reference assets automatically;
- the human must never have to supply style references manually;
- generate exactly ONE standalone image for the current subsection;
- never batch candidates;
- never create a collage or multi-section page;
- use one semantic field / one main explanatory mechanism;
- keep article nuance in the article, not dense raster text;
- no signature/author identity block unless the installed article mode explicitly requires one (book mode defaults to none).

Persist each successful generated asset under `Visual Assets/Generated` with a stable GEN ID (`GEN-001`, `GEN-002`, ...). Never overwrite an earlier attempt; retries use attempt metadata/new asset receipt.

### Step 5 — Generated Visual Evaluate

Evaluate the actual rendered image, not only its prompt or brief, using `references/rubrics/generated_visual.yaml` in a fresh evaluator context.

Required gates:
1. factual fidelity;
2. selected-mode fit;
3. explanatory value;
4. render accuracy;
5. visual quality.

DATA_EXPLAINER must match DATA_LOCK exactly.

Hard failure includes invented/changed numbers, unsupported claims, wrong relationships, humour that changes meaning, unreadable core copy, decorative-only output, or collage/multi-section output.

Allow at most two render attempts per GEN candidate. If attempt 2 still fails, mark that candidate `GENERATION FAILED`; do not put it in the human candidate set and do not loop indefinitely.

### Step 6 — Generated Visual Manifest

Create one native Google Doc named like:
`<Chapter> — Generated Visual Manifest <version>`

For every target record:
- GEN ID;
- subsection;
- selected mode;
- evidence basis/Deep Research locator;
- Adapt brief locator;
- render asset ID/path;
- render attempt count;
- generated evaluator status/report locator;
- DATA_LOCK when applicable;
- final status PASS or GENERATION FAILED.

### Step 7 — Unified Visual Review

Build one new native Google Doc named like:
`<Chapter> — Unified Visual Review <version>`

Use `references/unified-visual-review-format.md`.

It must cover every approved subsection and preserve all source candidate records from Source Visual Review. Add only passing GEN candidates.

Candidate provenance is explicit:
- `ORIGIN: PRIMARY_SOURCE` for VIS candidates;
- `ORIGIN: GENERATED_EXPLAINER` for GEN candidates.

Every candidate begins `HUMAN DECISION: PENDING` in a newly generated Unified Review, regardless of prior decisions on a stale review.

Generated visuals are explanatory artifacts derived from approved evidence. They are never new evidence and never replace the provenance of the underlying research.

### Step 8 — Unified Review Evaluate

Evaluate the Unified Visual Review using `references/rubrics/unified_visual_review_v3.yaml` in a fresh evaluator context.

The review must fail closed if candidate provenance is missing, a generated candidate did not pass its evaluator, a stale source review is mixed in, IDs collide, an approved subsection is missing, or a candidate lacks a Human Decision field.

Only a passing Unified Visual Review may be returned to the parent node for human review.

## Mode B — apply visual decisions

When `visual_review_doc_id` and exact `visual_decisions` are supplied:
- verify `visual_review_doc_id` is the current Unified Visual Review;
- do not rerun Selector, Adapt, Render, extraction, or evaluation;
- accept only KEEP or EXCLUDE values;
- update only matching `HUMAN DECISION` fields for exact VIS/GEN IDs;
- never alter origin, source/evidence basis, asset ID, mode, or evaluator status;
- verify the current candidate set and decision set match exactly.

Return `visual_review_status: resolved` only when no candidate remains PENDING.

## Logging contract

The parent Deep Research node owns Sheets and durable routing. Return enough metadata for it to log each internal execution separately while keeping `Subagent = Visual Generation`:
- Selector
- Adapt <GEN-ID>
- Render <GEN-ID> attempt N
- Evaluate <GEN-ID> attempt N
- Unified Review
- Evaluate Unified Review
- Apply Visual Decisions

Each logged step must include operation ID, input artifact IDs, output artifact/asset ID, result, and retry count where applicable.

## Hard prohibitions

- No new research source.
- No generated visual when a usable EXTRACTED primary-source visual already exists, unless a future explicit policy override is introduced by production configuration.
- No manually reimplemented/summarized version of the pinned Adapt/Render skills.
- No external image generator such as Runway.
- No cross-candidate render context reuse.
- No generated visual presented as primary-source evidence.
- No human decision inference.
- No chapter placement; Visual Placement owns that later.
- No regeneration after a GEN asset has been human-KEEP for placement; placement must use the exact reviewed asset.

## Output

Generation success:
{
  "version":"<version>",
  "visual_review_doc_id":"<unified_visual_review_doc_id>",
  "visual_assets_folder_id":"<visual_assets_folder_id>",
  "visual_review_status":"pending",
  "generation_plan_doc_id":"<generation_plan_doc_id>",
  "generated_visual_manifest_doc_id":"<generated_visual_manifest_doc_id>",
  "comment":"Visual Generation complete: <G> passing GEN candidates; Unified Visual Review contains <V> VIS + <G> GEN candidates; human decisions pending"
}

Decision-application returns the same shape and sets status `resolved` only when every current VIS/GEN candidate is KEEP/EXCLUDE.

On failure, never fabricate IDs. Return the valid artifact IDs that exist plus a `Failed:` comment naming the exact blocked step.