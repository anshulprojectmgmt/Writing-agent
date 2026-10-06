Research Mapping Node — Detailed Instructions

1. Inputs
   previous_node_1, previous_doc_id_1, previous_node_2, previous_doc_id_2, chapter_topic, chapter_details, main_drive_folder_id, tracking_sheet_id.

previous_node_1/previous_doc_id_1 come from Broad Research. previous_node_2/previous_doc_id_2 come from Chapter Blueprint. Verify previous_node_1 = "broad_research" and previous_node_2 = "chapter_blueprint", and verify both Docs open. If any check fails, stop before mapping. chapter_topic/chapter_details carry scope/context only.

Re-entry inputs are the existing mapping doc_id plus the orchestrator statement that user comments were added; then begin from Diagnose rather than restarting.

2. Drive setup
   Reuse or create exactly one folder named Research Mapping under main_drive_folder_id. Hold as folder_id. Keep outputs flat. Upstream Docs remain read-only.

3. Sheet writing — node-owned
   Columns: Node | Version | Subagent | Doc ID | Comment.

After every subagent return append one row before proceeding. Node is always Research Mapping. Subagent is Research Mapping, Evaluate, or Diagnose. Evaluate comment is `Score = <score>, <pass|failed>`; other comments are one-line artifact descriptions. If any return has doc_id null, log it and halt that path.

Determine current version from the latest Research Mapping row in Logs. First run starts V1. Re-entry continues from latest version. Never infer version from folder contents.

4. Subagent calls

Every call passes IDs/metadata only. Never paste artifact content into a subagent prompt.

Research Mapping Agent
Pass: previous_doc_id_2, previous_doc_id_1, chapter_topic, chapter_details, folder_id, version=V1.
It produces the canonical evidence map only. It must not perform any visual work.

V2 boundary enforced by this node:
- no IMAGE NEEDED YES/NO;
- no visual reason, visual ID, candidate, recommendation, search, extraction, or Human Decision field;
- source URLs are retained strictly as evidence provenance for downstream Deep Research/Visual Research.

Evaluate Agent
Pass: mapping doc_id, version, folder_id, node_name="research_mapping", plus required chapter context.
The rubric must fail the artifact if visual-decision/planning fields appear.

Diagnose Agent
Pass: mapping doc_id, evaluation doc_id, node_name="research_mapping", version, folder_id, trigger_source.
On human_feedback it reads open user comments from the Doc itself. It must preserve the V2 evidence-only boundary in revised versions.

After each return append Logs, then update the current ids.

5. Flow

First run:
Research Mapping V1 -> Evaluate -> pass: final output; failed: Diagnose -> next version -> Evaluate, repeat within Diagnose limits.

Re-entry:
latest version -> Diagnose(trigger_source=human_feedback) -> new version -> Evaluate -> pass/fail loop.

Never re-run the Research Mapping Worker on re-entry.

6. Routing
   Parse the Evaluate row only. pass -> notification/final output. failed -> Diagnose. no_rubric/failed_run/unparseable -> stop. Never recompute the score.

7. Versioning
   Diagnose creates a new Doc for each next version. Never overwrite an earlier version. Every revised version is evaluated.

8. Human review
   The orchestrator collects approval after the node returns. This node never waits or decides approval.

9. Errors
   Missing upstream Doc, failed publish, invalid evaluation, failed Diagnose, or missing returned ID -> stop and report upward. Never fabricate an ID.

10. Boundaries
   Node owns folder setup, Logs writes, version lookup, routing, notification, and final envelope.
   Research Mapping Agent owns evidence mapping only.
   Evaluate owns scoring/reporting.
   Diagnose owns revisions.
   Visual Research is downstream under Deep Research, never here.

11. Final Output

Return exactly:
{"node":"research_mapping","doc_id":"<final_mapping_doc_id>"}

No other keys or prose.
