# Deep Research adapter

Read these repository files for the active role:

- Deep Research worker: `Book Orchestrator Agent/Deep-research-node/deep-research-skill-3/SKILL.md`
- Deep Research evaluator: `Book Orchestrator Agent/Deep-research-node/Evaluate/SKILL.md`
- Deep Research rubric: `Book Orchestrator Agent/Deep-research-node/Evaluate/references/rubrics/deep_research.yaml`
- Diagnose: `Book Orchestrator Agent/Deep-research-node/Diagnose/SKILL.md`
- Visual Research adapter: `references/roles/visual_research.md`
- Node contract: `Book Orchestrator Agent/Deep-research-node/instruction.md`

Require the exact approved Broad Research and Research Mapping Docs.

## Canonical Deep Research

Research only mapped assignments and identified GAPs. Deepen citation trails, facts, mechanisms, statistics, quotes, surprising details, and caveats. A new primary source may be introduced only when needed to resolve a mapped GAP. Do not redesign the chapter and do not make visual decisions inside the canonical Deep Research Package.

Publish a native immutable Deep Research Package. Evaluate it with `deep_research`. Failed evaluation or human comments route to Diagnose and mandatory re-evaluation, capped at three Diagnose attempts per review cycle.

## Visual Research V2 after Deep Research passes

After the current Deep Research Package passes:

1. Create/reuse the `Visual Assets` folder under Deep Research.
2. Run `references/roles/visual_research.md` against the approved mapping + current passing Deep Research Package.
3. Publish Visual Review and exact-source candidate assets where possible.
4. Evaluate Visual Review with `visual_research` rubric.
5. If visual evaluation passes, surface Visual Review + Visual Assets to the human.
6. Do not permit Chapter Writing while any FOUND candidate remains `HUMAN DECISION: PENDING`.

The human may edit Visual Review directly or provide exact VIS-ID KEEP/EXCLUDE decisions. Apply chat decisions through the Visual Research decision mode; it may modify only Human Decision fields.

If Deep Research is revised after human comments, the old Visual Review becomes stale. Run Visual Research again from the revised package and require fresh decisions.

Never allow Chapter Writing to consume a failed/unapproved Deep Research Package or unresolved Visual Review.

Replace Gumloop/Slack with connected web and Google Drive tools. Return metadata only. Controller owns Sheets/checkpoints/main approvals.
