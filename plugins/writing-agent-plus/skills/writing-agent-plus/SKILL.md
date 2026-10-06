---
name: writing-agent-plus
description: Run or resume the Products of Tomorrow six-stage chapter workflow in ChatGPT Work or Codex using the signed-in ChatGPT plan and connected Google Drive. Use when the user starts a chapter, checks a run, approves a stage, resolves the visual review, requests a comment-driven revision, selects a blueprint, or resumes after a usage limit. Do not use an OpenAI API key or external cloud service.
---

# Writing Agent Plus

This is the subscription edition. It runs inside ChatGPT Work or Codex with the user's included allowance. Never request an OpenAI API key, start the hosted FastAPI edition, or claim guaranteed 24x7 execution. Google Drive is the durable system of record; local files are recoverable scratch.

Before the first run, read `references/setup.md`. For a start, resume, approval, visual decision, revision, status, or scheduled check, read `references/workflow.md` and `references/sheet-schema.md`. Read the role adapter for only the role being executed. Original role packages under `Book Orchestrator Agent/` remain authoritative for research, rubrics, voice, formatting, and diagnosis details unless this subscription adapter replaces Gumloop, Slack, API, storage, or evaluation-mutation behavior.

For legacy Evaluate/Diagnose roles, also read `references/safe-evaluation.md`; the subscription edition keeps source artifacts immutable. Chapter Writing uses the dedicated `Chapter Clean Evaluate Agent` and must not use the legacy inline evaluator on either chapter artifact.

## Fixed six-stage pipeline

Run sequentially, never in parallel:

1. `broad_research`
2. `research_analysis`
3. `chapter_blueprint`
4. `research_mapping`
5. `deep_research`
6. `chapter_writing`

The six main approval stages do not change. Two internal V2 subflows are mandatory:

### Deep Research subflow

`Deep Research Worker -> Evaluate -> Visual Research -> Evaluate Visual -> Human Visual Review`

Research Mapping is evidence-only. It must never output IMAGE NEEDED, visual candidates, image reasons, or visual recommendations.

Visual Research may inspect only:
- primary sources mapped to that exact subsection in Research Mapping; and
- a primary source added by Deep Research specifically to resolve that subsection's mapped GAP.

A visual candidate is selected using only three substantive criteria:
1. directly explains the subsection;
2. contains meaningful data, mechanism, or comparison;
3. is strong enough that it should improve the chapter.

Selection happens before extraction. Extraction difficulty cannot turn a qualifying candidate into NOT FOUND. The human owns final KEEP/EXCLUDE decisions. Chapter Writing cannot start while any candidate remains PENDING.

### Chapter Writing subflow

`Canonical Chapter Worker -> Clean Evaluate Canonical -> Visual Placement + LinkedIn Style -> Clean Evaluate Final`

Artifact A is the output of the existing canonical `anshul-chapter-writing-4` skill using its original bundled voice, writing-style, and output-formatting references. Do not inject the LinkedIn-derived style into Artifact A.

Artifact B is a NEW separate reader-facing Doc generated only after Artifact A passes. Visual Placement transforms presentation into the approved LinkedIn-derived style, inserts only human-KEEP primary-source visuals, and keeps placement audit in a separate report. Artifact B must not contain Chapter Writing Notes, Handoff Package, Completeness Summary, evaluator blocks, or visual workflow metadata.

The final Chapter Writing stage Doc ID is Artifact B. Artifact A remains preserved in Drive and Logs for comparison.

## Invocation modes

- **Start:** require topic and useful chapter details. Resolve/create one chapter folder, six stage folders, Logs, and Automation Resume Record.
- **Continue:** read Run State + Resume Record, reconcile the last operation, then perform only the recorded next transition.
- **Approve:** accept only explicit approval for the exact pending artifact.
- **Visual decision:** accept exact KEEP/EXCLUDE decisions for the current Visual Review, or verify the user edited all PENDING fields directly. Never infer a visual decision.
- **Revise:** require comments on the exact pending Doc. Diagnose/revise according to the active artifact contract.
- **Status:** report metadata/links from durable state; do not summarize artifact prose unless explicitly asked.
- **Scheduled check:** process at most one eligible transition and never bypass a human gate.

## Isolation and delegation

The controller carries identifiers and status only. Never place research, analysis, evidence, draft prose, evaluation findings, visual candidate content, or comment text into controller state. When isolated subagents are available, start a fresh context for each worker/evaluator/diagnose/visual role and tell it to read its adapter. Do not fork conversational history. When isolated execution is unavailable, run one role at a time and clear role-specific scratch before switching; retain only IDs/receipts.

## Google rules

Use connected Google Drive/Docs/Sheets/comments. Verify account, native MIME type, parent, ID, and readability after every creation. Never overwrite an earlier artifact version.

Visual Research creates/reuses `Deep Research/Visual Assets`. Its Visual Review is a separate native Doc. Exact-source image files are persisted in Visual Assets where possible; SOURCE-LINKED candidates retain exact primary source + locator rather than being dropped or substituted.

The workbook schema lives in `references/sheet-schema.md`. Queue/Run State + Resume Record remain recovery authorities. Before/after every external side effect, write a stable-operation checkpoint and reconcile uncertainty before retrying.

## Human gates

After every passing main-stage evaluation, set `AWAITING_APPROVAL` and wait for explicit approval of that exact Doc ID.

Blueprint retains its additional `AWAITING_BLUEPRINT_SELECTION` gate.

Deep Research additionally uses `AWAITING_VISUAL_REVIEW` after its Deep Research Package and Visual Review are ready. Chapter Writing starts only after:
- the Deep Research Package is explicitly approved; and
- every Visual Review candidate is KEEP or EXCLUDE.

A scheduled wake-up or silence never satisfies either gate.

## Chapter revision safety

Final Artifact B feedback is classified conservatively.
- presentation/voice/formatting/visual-placement only: regenerate Artifact B from the unchanged passing Artifact A and re-evaluate Final.
- facts/evidence/citations/statistics/claims/caveats/fixed punch lines/approved structure/reader transformation: stop with `Requires canonical revision`; do not create a final-only contradiction.

Canonical Artifact A revision follows its Diagnose -> Clean Evaluate loop before Artifact B is regenerated.

## Limits and recovery

The ChatGPT plan controls usage. Precise token/credit usage is not programmatically available. Leave unknown usage cells blank, never zero by guess. On limits, checkpoint and set `PAUSED_LIMIT`; never bypass or purchase API credits.

## Safety invariants

- Never advance after failed/missing/malformed evaluation.
- Never approve a stale/superseded artifact.
- Never exceed three Diagnose attempts in one review cycle.
- Never duplicate an external artifact for the same operation ID.
- Never move artifacts outside the authorized project root.
- Never use Gumloop, Slack, OpenAI API keys, Agents API, Cloud Run, or Terraform in this edition.
- Never allow visual work in Research Mapping.
- Never allow Chapter Writing while Visual Review has PENDING candidates.
- Never rewrite Artifact A into LinkedIn style.
- Never overwrite Artifact A when creating Artifact B.
- Never use an EXCLUDE visual or replace a failed KEEP with another/generated/redrawn image.
- Never claim completion until Artifact B passes final clean evaluation and all six main-stage approvals are recorded.

On completion, report topic, chapter folder, Logs, Resume Record, six approved main-stage Doc IDs/links, Deep Research Visual Review + Visual Assets IDs, and both Chapter Writing artifacts (Artifact A from Logs and approved Artifact B).
