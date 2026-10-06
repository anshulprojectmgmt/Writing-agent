# Chapter Writing adapter

Read these repository files for the active role:

- Canonical worker skill: `Book Orchestrator Agent/Chapter-writing-node/Chapter Writing Agent/SKILL.md`
- Canonical worker instruction: `Book Orchestrator Agent/Chapter-writing-node/Chapter Writing Agent/instruction.md`
- Canonical voice: `Book Orchestrator Agent/Chapter-writing-node/Chapter Writing Agent/references/anshul-voice.md`
- Canonical writing style/output formatting: sibling references under the canonical worker
- Clean evaluator adapter: `references/roles/chapter_clean_evaluate.md`
- Visual Placement adapter: `references/roles/visual_placement.md`
- Diagnose: `Book Orchestrator Agent/Chapter-writing-node/Diagnose/SKILL.md`
- Node contract: `Book Orchestrator Agent/Chapter-writing-node/instruction.md`

Require:
- exact approved Research Mapping Doc;
- exact approved Deep Research Doc;
- current Visual Review Doc;
- Visual Assets folder;
- every FOUND visual decision resolved to KEEP or EXCLUDE.

Any PENDING visual blocks this stage.

## Artifact A — canonical result

Run the existing `anshul-chapter-writing-4` worker exactly as authored. Preserve its bundled Anshul voice, writing style, output formatting, blueprint structure, evidence assignments, citations, canonical Notes/Handoff/Summary outputs, and factual constraints.

Do NOT apply the LinkedIn-derived style to this worker. Artifact A exists specifically so the user can inspect the original Anshul-skill result separately.

Evaluate Artifact A using `references/roles/chapter_clean_evaluate.md` with rubric `chapter_writing`. Source Doc must remain untouched. Canonical failure routes to Diagnose and then clean re-evaluation.

## Artifact B — final presentation result

Only after Artifact A passes, run `references/roles/visual_placement.md`.

Visual Placement creates a NEW Google Doc from Artifact A, applies the approved LinkedIn-derived reader-facing style, and inserts only human-KEEP primary-source visuals. It does not overwrite Artifact A and does not conduct new research.

It also creates a separate Visual Placement Report accounting for all visual decisions.

Evaluate Artifact B through `references/roles/chapter_clean_evaluate.md` with rubric `chapter_writing_final`, cross-checking Artifact A, Visual Review, and Placement Report. Artifact B must remain clean: no evaluator blocks, workflow notes, canonical Notes/Handoff/Completeness, or visual decision metadata in reader-facing prose.

The main Chapter Writing stage Pending/Approved Doc is Artifact B. Preserve Artifact A separately in Logs and Run State as `Canonical Chapter Writing Doc ID`.

## Human feedback on Artifact B

Presentation/voice/formatting/visual-placement feedback may regenerate Artifact B from the unchanged passing Artifact A.

If feedback changes facts, evidence, citations, statistics, claims, caveats, fixed punch lines, approved structure, or designated reader transformation, stop with `Requires canonical revision`; do not patch only Artifact B.

Replace Gumloop/Slack with connected Drive tools. Return metadata only. Controller owns Sheets/checkpoints/approval/completion.
