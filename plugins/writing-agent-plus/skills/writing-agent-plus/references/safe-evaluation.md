# Safe evaluation protocol

This protocol applies to every stage in the subscription edition. It overrides conflicting
instructions in the original Evaluate and Diagnose packages.

## Evaluate

- Treat the artifact being evaluated as immutable and read-only. Never insert findings blocks,
  recolor text, attach generated evaluator comments, resolve comments, or otherwise mutate it.
- Score the artifact section by section with the original node rubric and threshold. Keep the
  original finding template and include every finding in the evaluation report.
- Save the complete report as a separate native Google Doc in the authorized stage folder. A
  direct native report Doc is allowed; the Markdown upload-and-convert sequence is not required.
- Verify the report's ID, native Google Docs MIME type, authorized parent, title, and readability.
- Return `comments_placed: 0` and `source_doc_mutated: false`. Zero comments is valid in this mode
  and does not make a complete, verified evaluation malformed.
- A pass still routes to explicit human approval. A failure routes to Diagnose with the report ID.

## Diagnose

- On `evaluation_failure`, use the verified evaluation report as the authoritative findings input.
  Source-document evaluator comments and inserted findings blocks are not required and must not be
  expected. Revise only the sections named by actionable report findings.
- On `human_feedback`, read open human comments from the exact pending Doc as before. Do not treat
  the absence of evaluator comments as an error.
- Keep every prior artifact read-only and create a new immutable version in the authorized folder.

## Recovery

- Reconcile by operation ID and search the authorized stage folder before creating a report. Reuse
  a verified report already created for that operation; never create a duplicate.
- A blocked legacy attempt that produced no source mutation, no comments, and no Drive report may
  be retried once under this protocol with a new attempt ID.
