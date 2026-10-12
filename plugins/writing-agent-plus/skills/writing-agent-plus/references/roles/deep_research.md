# Deep Research adapter

Read these repository files for the active role:

- Main Deep Research worker: `Book Orchestrator Agent/Deep-research-node/deep-research-skill-3/SKILL.md`
- Deep Research evaluator: `Book Orchestrator Agent/Deep-research-node/Evaluate/SKILL.md`
- Deep Research rubric: `Book Orchestrator Agent/Deep-research-node/Evaluate/references/rubrics/deep_research.yaml`
- Diagnose: `Book Orchestrator Agent/Deep-research-node/Diagnose/SKILL.md`
- Visual Extraction adapter: `references/roles/visual_research.md`
- Visual Generation adapter: `references/roles/visual_generation.md`
- Node contract: `Book Orchestrator Agent/Deep-research-node/instruction.md`

Require the exact approved Broad Research and Research Mapping Docs.

## Three durable sub-agents

Deep Research contains exactly three durable sub-agents:

1. `Main Deep Research`
2. `Visual Extraction`
3. `Visual Generation`

Selector/Adapt/Render/installed Render Review/generated evaluation/Unified Review are internal executions owned by Visual Generation, not additional durable workflow agents.

## 1. Main Deep Research

Research only mapped assignments and identified GAPs. Deepen citation trails, facts, mechanisms, statistics, quotes, surprising details, and caveats. A new primary source may be introduced only when needed to resolve a mapped GAP. Do not make visual decisions inside the canonical Deep Research Package.

Publish a native immutable Deep Research Package. Evaluate it under the subscription safe-evaluation protocol. Failed evaluation or human comments route to Diagnose and mandatory re-evaluation, capped at three Diagnose attempts per review cycle.

## 2. Visual Extraction

After the current Deep Research Package passes:

1. Create/reuse the `Visual Assets` folder under Deep Research.
2. Run `references/roles/visual_research.md` against approved mapping + current passing Deep Research Package.
3. Publish `Source Visual Review` and faithful exact-source candidate assets where possible.
4. Evaluate Source Visual Review using the existing source-visual rubric.
5. A failed Source Visual Review blocks Visual Generation.

Visual Extraction is primary-source only and never generates a substitute.

## 3. Visual Generation

After Source Visual Review passes:

1. Run `references/roles/visual_generation.md` with current Deep Research Package + Source Visual Review.
2. Generate fallbacks only where no usable EXTRACTED source visual exists.
3. For every GEN attempt, require the pinned installed Render article-review/validator to pass first, then require the separate Writing Agent generated-image evidence rubric to pass.
4. Preserve exact VIS candidates and add only GEN candidates that passed both gates.
5. Publish and verify one Unified Visual Review.
6. Surface only the passing Unified Visual Review + Visual Assets to the human.

Do not permit Chapter Writing while any current VIS/GEN candidate remains `HUMAN DECISION: PENDING`.

The human may edit Unified Visual Review directly or provide exact VIS/GEN KEEP/EXCLUDE decisions. New V3 chat decisions are applied through Visual Generation decision mode, not Visual Extraction.

If Deep Research is revised after comments, all prior visual outputs become stale for routing. Run fresh Visual Extraction, fresh Visual Generation, and require fresh human decisions.

## Isolation

Each durable sub-agent uses a fresh role context. Inside Visual Generation, Selector, each candidate Adapt, Render, installed Render Review, Writing Agent generated evaluator, and Unified Review verification each use fresh contexts as defined by its skill. Controller carries only identifiers/status.

Never allow Chapter Writing to consume a failed/unapproved Deep Research Package or unresolved Unified Visual Review.

Replace Gumloop/Slack with connected web and Google Drive tools. Return metadata only. Controller owns Sheets/checkpoints/main approvals.
