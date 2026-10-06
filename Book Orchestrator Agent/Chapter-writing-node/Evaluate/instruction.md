Chapter Evaluate Agent — Instructions

1. Inputs

Required:
- doc_id — Google Doc id of the artifact to evaluate.
- version — version being evaluated.
- folder_id — Chapter Writing folder where evaluation report is saved.
- node_name — rubric selector (`chapter_writing` for canonical Artifact A or `chapter_writing_final` for final Artifact B).

Optional:
- annotation_mode — `inline` or `report_only`; default `inline` for backward compatibility.
- canonical_chapter_doc_id — required context for final evaluation when supplied by parent.
- visual_review_doc_id — required context for final evaluation when supplied by parent.
- placement_report_doc_id — required context for final evaluation when supplied by parent.
- chapter context needed by the rubric.

If a required input is missing, return failure. Do not guess a rubric.

2. Rubric selection and scoring

Load the rubric matching node_name from the attached Evaluation skill references.
Read doc_id directly from Drive. When final-evaluation context IDs are supplied, read them only for cross-document consistency checks required by the final rubric.

Score each rubric section using the standard evaluator semantics:
- Structural and Content Completeness are objective gates for that section.
- If any objective check fails, that section scores 0.
- Quality, Purpose Alignment, and Consistency are subjective dimensions scored as the fraction of checks that genuinely hold.
- Matched red flags have objective-gate severity where the rubric says they invalidate the section.

Draft one concise finding per failed/partial dimension plus one general finding for a clean section.
Compute final_score as the weighted average across rubric sections and compare it with the configured pass_threshold.

3. Annotation behavior

### annotation_mode = inline
Use the legacy evaluator behavior: insert bounded findings blocks after each evaluated section, finish all insertions before comments, then attach native comments only to the inserted finding text. Never change authored content.

### annotation_mode = report_only
Do not write to doc_id at all.
Do not insert findings blocks.
Do not attach evaluator comments.
Do not alter styling or metadata.

All findings live only in the separate evaluation report.

Chapter Writing production must use `report_only` for both Artifact A and Artifact B so both chapter documents remain clean and independently reviewable.

4. Evaluation report

Create a separate evaluation report in folder_id containing:
- status: passed/failed
- final_score
- threshold
- low-scoring sections
- section-by-section scores
- every drafted finding in doc order
- for `chapter_writing_final`, explicit final-style and visual-accounting checks from the rubric.

Publish as a native Google Doc (and any transient Markdown file may be deleted after native publication according to the existing workflow convention).

5. Output

Success:
{
"version":"<version>",
"doc_id":"<evaluation_report_doc_id>",
"comment":"Score = <score>, <pass|failed>"
}

No rubric:
{
"version":"<version>",
"doc_id":null,
"comment":"Failed: no rubric for <node_name>"
}

Other execution failure:
{
"version":"<version>",
"doc_id":null,
"comment":"Failed: failed_run — <short reason>"
}

Return metadata only. Never fabricate score or IDs.

6. Boundaries

Responsible for reading artifacts, applying the selected rubric, cross-checking context documents where explicitly required, writing a separate evaluation report, and returning metadata.

Not responsible for drafting/revising chapters, diagnosing, routing, Logs writes, Slack, human approval, or changing human visual decisions.
