# Durable workflow protocol

## Start a run

1. Resolve one active Project Configuration row. If several projects are possible, ask the user.
2. Require `chapter_topic`; accept optional details but ask once when the topic is too ambiguous to research responsibly.
3. Reject a second active run by the same user unless explicitly queued. Keep at most three queued rows per user.
4. Create a run ID and stable operation ID before any Drive write.
5. Search the project root for a matching chapter folder. Reuse one unambiguous match, create one if absent, and stop if several match.
6. Under the chapter folder, create/reuse exactly one direct child for each of the six main stages plus native `Logs` and `Automation Resume Record`. Deep Research later creates/reuses its `Visual Assets` child folder.
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

## Deep Research + Visual Research protocol

After a passing Deep Research Package:

1. Create/reuse `Deep Research/Visual Assets`.
2. Run Visual Research from `references/roles/visual_research.md`.
3. Visual Research inspects every approved subsection using only primary sources already mapped to that subsection plus a primary source added by Deep Research specifically to resolve that subsection's mapped GAP.
4. Candidate selection uses only three substantive criteria:
   - directly explains the subsection;
   - contains meaningful data, mechanism, or comparison;
   - strong enough to improve the chapter.
5. Selection happens before extraction. Extraction inconvenience cannot turn a valid candidate into NOT FOUND.
6. Publish a Visual Review covering every subsection and persist exact-source candidate assets to Visual Assets where possible.
7. Evaluate Visual Review with the `visual_research` rubric. A failed visual evaluation blocks the run.
8. After both the Deep Research Package and Visual Review are valid, require explicit human decisions for every FOUND candidate. State becomes `AWAITING_VISUAL_REVIEW` while any candidate is PENDING.
9. Human can edit the Visual Review directly or supply exact VIS-ID KEEP/EXCLUDE decisions. Never infer a choice.
10. Chapter Writing cannot begin until the Deep Research Package is approved AND all candidates are KEEP/EXCLUDE.

If Deep Research is revised after comments, the old Visual Review becomes stale. Run fresh Visual Research, fresh visual evaluation, and fresh human visual decisions.

## Chapter Writing dual-artifact protocol

Chapter Writing has two deliberate outputs.

### Artifact A — canonical Anshul style

Run the existing canonical Chapter Writing worker only. It uses `anshul-chapter-writing-4` plus its bundled Anshul voice, writing-style, and output-formatting references. Do not inject the LinkedIn-derived final style.

Evaluate Artifact A with the Chapter Clean Evaluate Agent using the canonical `chapter_writing` rubric. The evaluator writes a separate report only and never annotates Artifact A.

If it fails, revise canonical Artifact A through Diagnose and clean-evaluate the new version. Visual Placement cannot run until the current canonical artifact passes.

### Artifact B — LinkedIn style + visuals

After Artifact A passes, run Visual Placement from `references/roles/visual_placement.md`.

It creates a NEW document from Artifact A, applies only the approved LinkedIn-derived reader-facing presentation style, and inserts only human-KEEP primary-source visuals. It never overwrites Artifact A and never conducts new research.

It creates a separate Visual Placement Report accounting for every candidate as INSERTED, EXCLUDED, or FAILED. A failed KEEP gets a specific exact-source/technical reason; it is never silently replaced.

Evaluate Artifact B through Chapter Clean Evaluate using `chapter_writing_final` and cross-check against Artifact A, Visual Review, and Placement Report. The final evaluator never writes to Artifact B.

The Chapter Writing main-stage pending/approved Doc is Artifact B. Preserve Artifact A separately in Logs and Run State for comparison.

## Human decisions

An approval command must identify one run unambiguously. Compare the supplied/inferred Doc ID to the exact current Pending Doc ID. Record a unique Decision row first, then update the matching approval field/state. Duplicate decisions with the same ID are harmless.

For `COMMENTS_READY`, confirm open comments exist on the exact pending Doc and start the appropriate revision route.

For Blueprint selection, record exact options Doc ID and verbatim choice, then resume the existing worker operation.

For visual decisions, record exact Visual Review Doc ID and exact KEEP/EXCLUDE choices. Never accept a visual decision against a stale review.

Final Artifact B comments are classified conservatively by Visual Placement:
- presentation/voice/formatting/placement only -> regenerate Artifact B from unchanged Artifact A;
- substantive facts/evidence/citations/statistics/claims/caveats/fixed punch lines/approved structure/reader transformation -> `Requires canonical revision`; do not create a contradictory final-only patch.

## Scheduled recovery

Each scheduled wake-up processes no more than one eligible transition:
- `READY`: claim and run the recorded transition;
- stale `RUNNING`: reconcile before retrying;
- due `PAUSED_LIMIT`: resume from exact checkpoint;
- `AWAITING_APPROVAL`, `AWAITING_BLUEPRINT_SELECTION`, `AWAITING_VISUAL_REVIEW`: do nothing and remain quiet;
- blocked/completed/cancelled: do nothing.

If allowance is exhausted, preserve last confirmed checkpoint, set `PAUSED_LIMIT`, and record visible reset time when available. Never invent a reset time.

## Resume Record body

Keep at the top:
- Run ID and project ID
- Topic and requester
- Chapter folder and Logs links
- Current state, stage, version, attempt
- Last completed checkpoint
- Approved upstream Doc IDs
- Deep Research Visual Review Doc ID and Visual Assets folder ID when created
- Canonical Chapter Artifact A Doc ID when created
- Pending Doc ID and operation ID
- exact next transition
- pause/error reason
- earliest retry time when known
- last update timestamp

Append a brief chronological checkpoint table below. Do not paste artifact prose or visual-candidate content into this Doc.
# Execution prerequisites

Before dispatch or recovery, read `execution-policy.md`. Every role uses a fresh `fork_turns="none"` context and actual approved model/reasoning settings. Validate exported current state, the intended dispatch, and exact pending approval with `scripts/state_machine.py`; never treat prompt wording as enforcement. Persist the verified guard metadata in Runs and Resume Record. A failed guard blocks the transition.
