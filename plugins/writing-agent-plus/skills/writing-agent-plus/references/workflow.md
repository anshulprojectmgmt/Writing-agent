# Durable workflow protocol

## Start a run

1. Resolve one active Project Configuration row. If several projects are possible, ask the user.
2. Require `chapter_topic`; accept optional details but ask once when the topic is too ambiguous to research responsibly.
3. Reject a second active run by the same user unless explicitly queued. Keep at most three queued rows per user.
4. Create a run ID and stable operation ID before any Drive write.
5. Search the project root for a matching chapter folder. Reuse one unambiguous match, create one if absent, and stop if several match.
6. Under the chapter folder, create/reuse exactly one direct child for each of the six main stages plus native `Logs` and `Automation Resume Record`. Deep Research later creates/reuses its `Visual Assets` child folder and Visual Generation may create `Visual Assets/Generated`.
7. Verify every object after creation and write Queue, Runs, chapter Run State, Resume Record, and Events checkpoints before Broad Research.

## Perform a standard stage

Read the adapter in `references/roles/<stage>.md`. Adapter rules replace Gumloop/Slack and any instruction to advance without human approval.

For legacy Evaluate/Diagnose roles, follow `references/safe-evaluation.md`: source artifacts stay immutable and findings live in a separate native evaluation report. Chapter Writing instead uses the dedicated Clean Evaluate adapter.

For each role attempt:
1. Set stable operation ID `<run-id>:<stage>:<role>:v<version>:a<attempt>`.
2. Reconcile Events/stage folder for an existing receipt before writing.
3. Write `BEFORE_<ROLE>` checkpoints.
4. Start a fresh isolated agent when available and pass only required IDs/context/version/attempt/operation ID.
5. Role reads source Docs/comments itself and returns metadata only.
6. Verify native MIME type, authorized parent, ID, and required metadata.
7. Append one Artifact Log row and read it back.
8. Write `AFTER_<ROLE>` checkpoints before routing.

Normal worker success routes to evaluation. Evaluation pass routes to a human gate, not automatically to the next main stage. Evaluation failure routes to Diagnose if the review cycle has fewer than three diagnose attempts. Diagnose creates the next immutable version and routes back to evaluation. Malformed/missing artifacts or exhausted attempts set `BLOCKED`.

## Research Mapping V2 boundary

Research Mapping is evidence mapping only.

It maps approved Broad Research sources to Blueprint subsections, preserves exact source URLs, assigns HIGH/MED fit, records honest GAPs, and produces Coverage Summary.

It must not produce IMAGE NEEDED, YES/NO image decisions, visual IDs, visual reasons, candidate suggestions, figure recommendations, image searches, extraction steps, or Human Decision fields. Its evaluator must fail such output.

## Deep Research V3 — three durable sub-agents

Deep Research has exactly three durable sub-agents:

`Main Deep Research -> Visual Extraction -> Visual Generation -> Human Visual Review`

Selector/Adapt/Render/installed Render Review/generated evaluation/Unified Review are internal skill executions of Visual Generation, not additional durable workflow stages.

### 1. Main Deep Research

Run existing canonical Deep Research worker and safe evaluation/Diagnose loop. It deepens mapped evidence and resolves mapped GAPs only.

No visual work starts until current Deep Research Package passes.

### 2. Visual Extraction

After a passing Deep Research Package:

1. Create/reuse `Deep Research/Visual Assets`.
2. Run Visual Extraction from `references/roles/visual_research.md`.
3. Inspect every approved subsection using only primary sources already mapped to that subsection plus a primary source added by Deep Research specifically to resolve that subsection's mapped GAP.
4. Candidate selection uses only three substantive criteria:
   - directly explains the subsection;
   - contains meaningful data, mechanism, or comparison;
   - strong enough to improve the chapter.
5. Selection happens before extraction. Extraction inconvenience cannot turn a valid candidate into NOT FOUND.
6. Publish `Source Visual Review` covering every subsection and persist exact-source candidate assets to Visual Assets where possible.
7. Evaluate Source Visual Review with existing source-visual rubric. Failure blocks Visual Generation.

Visual Extraction never generates/redraws/substitutes a visual.

### 3. Visual Generation

After Source Visual Review passes:

1. Run `references/roles/visual_generation.md` with current Deep Research Package + Source Visual Review.
2. Generation is fallback-only:
   - usable EXTRACTED source visual -> no generation by default;
   - SOURCE-LINKED only -> generate fallback;
   - NOT FOUND -> generate fallback.
3. Select DATA_EXPLAINER / TOPIC_EXPLAINER / HUMOUR_METAPHOR using approved short rubric.
4. For each target independently:
   - fresh Adapt context using only that subsection's evidence and full pinned installed Adapt package;
   - fresh Render context using full pinned installed Render package, Article-section mode and ChatGPT native image generation;
   - fresh installed `review-linkedin-visual-post` context using Render's article reviewer/validator; failed review discards the complete render attempt;
   - fresh Writing Agent generated-image evaluator context only after installed review passes;
   - maximum two complete render attempts across both acceptance gates.
5. Publish Visual Generation Plan and Generated Visual Manifest, including installed review verdict and Writing Agent evaluation status per GEN candidate.
6. Build one Unified Visual Review containing unchanged VIS candidates plus only GEN candidates passing both gates.
7. Evaluate Unified Visual Review in a fresh context. A failed review blocks the run.

The installed Adapt/Render/Render-review packages and required references/assets/scripts are loaded from exact pinned registry commit. Do not rewrite skills into simplified prompts and do not ask human to provide style references.

Generated visuals explain approved evidence; they are not evidence sources.

### Human visual review

After both Deep Research Package and Unified Visual Review are valid, require explicit human decisions for every current VIS/GEN candidate. State becomes `AWAITING_VISUAL_REVIEW` while any candidate is PENDING.

Human can edit Unified Visual Review directly or supply exact candidate-ID KEEP/EXCLUDE decisions. New V3 chat decisions are applied through Visual Generation decision mode. Never infer a choice.

Chapter Writing cannot begin until Deep Research Package is approved AND all current VIS/GEN candidates are KEEP/EXCLUDE.

If Deep Research is revised after comments, all previous source/generated visual artifacts become stale for routing. Run fresh Visual Extraction, fresh Visual Generation, and require fresh human decisions.

## Chapter Writing dual-artifact protocol

Chapter Writing has two deliberate outputs.

### Artifact A — integrated Anshul writing

Run existing integrated Chapter Writing worker: storytelling-article argument/story development -> anshul-writing-style writing + formatting + internal ai-humanizer-core -> story-integrity review -> verified native formatting. Read all dependencies and bundled inner references. Record execution checks in Notes; clean evaluator must verify them before controller state records a passing version-1 execution gate.

Evaluate Artifact A with Chapter Clean Evaluate Agent using canonical `chapter_writing` rubric. Evaluator writes separate report only and never annotates Artifact A.

If it fails, revise canonical Artifact A through Diagnose and clean-evaluate new version. Visual Placement cannot run until current canonical artifact passes.

### Artifact B — preserved writing + approved visuals

After Artifact A passes, run Visual Placement from `references/roles/visual_placement.md`.

It creates a NEW document from Artifact A, preserves completed prose/voice/native formatting, and inserts only exact human-KEEP assets from current Unified Visual Review:
- VIS -> exact approved source asset;
- GEN -> exact approved generated asset.

No second style rewrite is allowed. Visual Placement never regenerates a GEN candidate and never replaces a failed KEEP with another asset. It never overwrites Artifact A and never conducts new research.

It creates a separate Visual Placement Report accounting for every candidate as INSERTED, EXCLUDED, or FAILED.

Evaluate Artifact B through Chapter Clean Evaluate using `chapter_writing_final` and cross-check against Artifact A, Unified Visual Review, and Placement Report. Final evaluator never writes to Artifact B.

Chapter Writing main-stage pending/approved Doc is Artifact B. Preserve Artifact A separately in Logs and Run State for comparison.

## Human decisions

An approval command must identify one run unambiguously. Compare supplied/inferred Doc ID to exact current Pending Doc ID. Record a unique Decision row first, then update matching approval field/state. Duplicate decisions with same ID are harmless.

For `COMMENTS_READY`, confirm open comments exist on exact pending Doc and start appropriate revision route.

For Blueprint selection, record exact options Doc ID and verbatim choice, then resume existing worker operation.

For visual decisions, record exact current Unified Visual Review Doc ID and exact VIS/GEN KEEP/EXCLUDE choices. Never accept a visual decision against a stale review.

Final Artifact B comments are classified conservatively by Visual Placement:
- placement/layout/caption only -> regenerate Artifact B from unchanged Artifact A;
- voice/prose/emphasis/formatting -> targeted integrated Chapter Writing revision, evaluate A, then regenerate B;
- substantive facts/evidence/citations/statistics/claims/caveats/fixed punch lines/approved structure/reader transformation -> `Requires canonical revision`; do not create contradictory final-only patch.

## Scheduled recovery

Each scheduled wake-up processes no more than one eligible transition:
- `READY`: claim and run recorded transition;
- stale `RUNNING`: reconcile before retrying;
- due `PAUSED_LIMIT`: resume from exact checkpoint;
- `AWAITING_APPROVAL`, `AWAITING_BLUEPRINT_SELECTION`, `AWAITING_VISUAL_REVIEW`: do nothing and remain quiet;
- blocked/completed/cancelled: do nothing.

If allowance is exhausted, preserve last confirmed checkpoint, set `PAUSED_LIMIT`, and record visible reset time when available. Never invent a reset time.

## Resume Record body

Keep at top:
- Run ID and project ID
- Topic and requester
- Chapter folder and Logs links
- Current state, stage, version, attempt
- Last completed checkpoint
- Approved upstream Doc IDs
- Deep Research Unified Visual Review Doc ID and Visual Assets folder ID when created
- Canonical Chapter Artifact A Doc ID when created
- Pending Doc ID and operation ID
- exact next transition
- pause/error reason
- earliest retry time when known
- last update timestamp

Append brief chronological checkpoint table below. Do not paste artifact prose or visual-candidate content into this Doc.

# Execution prerequisites

Before dispatch or recovery, read `execution-policy.md`. Every durable role uses fresh `fork_turns="none"` context and actual approved model/reasoning settings. Visual Generation also requires fresh internal contexts for Selector, each candidate Adapt, each candidate Render, each candidate installed Render Review, each candidate Writing Agent generated evaluator, and Unified Review verification. Validate exported current state, intended dispatch, and exact pending approval with `scripts/state_machine.py`; never treat prompt wording as enforcement. Persist verified guard metadata in Runs and Resume Record. A failed guard blocks transition.

## Mandatory approved presentation gate
Read Chapter Writing references/presentation-contract.md and presentation-profile.json. Use personal-agents-approved-v1 and run scripts/validate_chapter_presentation.py on actual native Doc JSON plus revision-bound presentation plan. Counts/self-declarations cannot substitute. Worker-only tests also require this before returning success. Independently inspect semantic placement in clean evaluation. Execution receipt must include matching presentation profile/baseline provenance, current Artifact A revision, passing native_validator_passed and locatable evidence. Missing/stale/failed presentation blocks handoff regardless of score. Use numbered main HEADING_1, unnumbered HEADING_2, functional icons, meaningful existing opening emphasis, explanatory lists, plain reader citations and exact linked source URLs in Handoff. No new formatting node or Visual Placement rewrite.
