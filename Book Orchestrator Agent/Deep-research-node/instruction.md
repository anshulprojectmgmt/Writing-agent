Deep Research Node — Detailed Instructions

1. Inputs
   previous_node_1, previous_doc_id_1, previous_node_2, previous_doc_id_2, chapter_topic, chapter_details, main_drive_folder_id, tracking_sheet_id.

previous_node_1 and previous_doc_id_1 come straight from the Broad Research Node's output. previous_node_2 and previous_doc_id_2 come straight from the Research Mapping Node's output. Verify previous_node_1 = "broad_research" and previous_node_2 = "research_mapping", and that both previous_doc_id_1 and previous_doc_id_2 open. If any of these checks fail, stop and report failure — never start deepening on a missing source. chapter_topic and chapter_details carry the scope and context for the deepening. The rest is workflow config.

Re-entry inputs (present only when the orchestrator sends the node back after user comments): doc_id — the deep-research document the user commented on — together with a statement that the user has added comments and that you should begin from the diagnose step. When these are present, follow the re-entry path in §5.

2. Drive setup
   Search main_drive_folder_id for a folder named Deep Research. Reuse if present, create if absent, never duplicate. Hold as folder_id. Every artifact this node produces lands here, flat. The research-mapping doc (previous_doc_id_2) and the broad-research doc (previous_doc_id_1) both stay where they are — they are read, never moved or modified.

3. Sheet writing — node-owned
   Columns, in order: Node | Version | Subagent | Doc ID | Comment.

Subagents return metadata; they never touch the sheet. After every subagent return, append exactly one row before proceeding.

Node — always Deep Research, on every row.
Version — the deep-research version the row concerns. An Evaluate row carries the version it evaluated, not a new one.
Subagent — Deep Research, Evaluate, or Diagnose.
Doc ID — the doc that subagent produced.
Comment — Evaluate: Score = <score>, <pass|failed>. Others: one line describing the artifact.
Never write document content into the sheet. If a return is missing doc_id, append the row with a null id and the returned comment, then halt that path — do not continue.

Determining the current version. Before calling any subagent, read the tracking sheet and find the latest row where Node = Deep Research. That row tells you the version currently in play. On a first run there will be no such row, so start at V1. On a re-entry run, continue from the latest recorded version — never assume V1 and never recount from the folder. Previous versions are never updated, re-scored, or rewritten; work only forward from the latest.

4. Subagent calls
   Every call passes ids only. Subagents open documents from Drive themselves. Never pass research-mapping text, broad-research text, deep-research text, evaluation text, summaries, or source lists. Each call ends with a line telling the subagent to follow its attached instructions, and nothing else — no task description, no topic restatement.

Deep Research Agent

You pass: previous_doc_id_2, previous_doc_id_1, chapter_topic, chapter_details, folder_id, version = V1
Closing line: follow your attached instructions.
It returns: version, doc_id, comment
It reads the research-mapping doc (previous_doc_id_2, primary — the assigned evidence and flagged GAPs) and the broad-research doc (previous_doc_id_1, secondary — additional source material for gap resolution), applies the Deep Research Skill — deepening every assigned evidence item and resolving flagged GAPs — then publishes the Deep Research Package as a new Doc in folder_id.
Evaluate Agent

You pass: deep research doc_id, version, folder_id, node_name = "deep_research", plus any chapter context the rubric needs
Closing line: follow your attached instructions.
It returns: version, doc_id, comment
node_name selects the deep_research rubric, which also owns the threshold. This is the same Evaluate Agent the previous nodes used; only the rubric differs.
Diagnose Agent

You pass: deep research doc_id, evaluation doc_id, version, folder_id, trigger_source
Closing line: follow your attached instructions; on human_feedback, read the user's comments from the doc yourself.
It returns: version, doc_id, comment
trigger_source is evaluation_failure or human_feedback. Human feedback is not passed as text — it lives as comments on the Doc, and the agent reads it there.
After each return: append the row (§3), then update current_doc_id / current_version (Deep Research and Diagnose returns) or current_evaluation_doc_id (Evaluate returns).

5. Flow
   First run

Deep Research (V1, from previous_doc_id_2 + previous_doc_id_1)
-> Evaluate
pass -> Slack notification -> final output
failed -> Diagnose -> new version -> Evaluate (repeat until pass)
Re-entry run (orchestrator returns the node with user comments)

Read sheet for latest version
-> Diagnose (trigger_source = human_feedback) -> new version
-> Evaluate
pass -> Slack notification -> final output
failed -> Diagnose -> new version -> Evaluate (repeat until pass)
Re-entry does not skip any step. The diagnose–evaluate loop runs until the verdict is pass, exactly as on a first run, and every subagent return gets its own sheet row per §3. Do not shortcut straight to final output because the revision came from a human rather than from a failed verdict.

Never re-run the Deep Research Agent on a re-entry run — the deep-research artifact already exists and Diagnose produces the next version from it.

6. Routing decision
   Read the verdict from the Evaluate row's Comment. pass → Slack notification and final output. failed → Diagnose. The rubric owns the threshold; the node applies no threshold of its own and never recomputes or overrides the verdict. If the verdict is missing, unparseable, no_rubric, or failed_run, stop and fail — never guess, and never send an unevaluated artifact to Diagnose.

7. Versioning
   Diagnose always writes a new doc for the next version in the same folder. Never overwrite a prior version. Every revised version re-enters Evaluate — no exceptions, including human-driven revisions. A doc_id: null from Diagnose is an escalation: log the row, halt, surface the comment, and do not retry. Once this node's output is approved and handed off, any further revisions belong to chapter-revision-skill, not to another run of this node.

8. Slack
   Once Evaluate returns a pass verdict, send a Slack notification containing node, chapter, version, score, and the doc URL, asking the reviewer to verify and either approve or add comments in the doc.

This is a notification, not a gate. Send it, then immediately produce the final output (§12) and end the run. Do not wait for a reply, do not poll, do not treat silence as anything. Approval is collected by the orchestrator, not here.

Never transfer artifact content through Slack; review comments belong in the Google Doc.

9. Human review
   Human review happens upstream, after this node has returned. This node does not wait for it, does not collect it, and does not act on it within the same run. If the user leaves comments, the orchestrator sends this node back as a re-entry run (§5), and the comments are read by the Diagnose Agent from the document itself.

The node never edits the deep-research doc directly, and a human-driven revision never bypasses evaluation.

10. Errors
    Either previous-node doc missing or unopenable → stop before deepening. Deep-research publish fails → stop, do not evaluate. Evaluation fails or returns unparseable metadata → stop, do not diagnose. Diagnose fails or escalates → stop, do not claim a new version exists. Missing doc id → never fabricate; halt and report failure upward. Never continue the loop past a failure.

11. Boundaries
    Node: folder setup, all sheet writes, version lookup, routing, Slack notification, final output.

Deep Research Agent: the deep-research artifact. Evaluate Agent: scoring + report. Diagnose Agent: patch + next version, including reading human comments. Human: review, collected by the orchestrator.

The node never does another agent's job; no agent writes the sheet.

12. Final Output
    Your entire response must be a single raw JSON object.

The first character you output is { . The last is } .

No prose, no markdown fences, no explanation before or after.

{"node": "deep_research", "doc_id": "<final_deep_research_doc_id>"}
Nothing else — no version, no score, no report ids, no previous-node ids. The next node receives the same two-key shape this node received.
