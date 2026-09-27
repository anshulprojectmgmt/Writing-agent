# Durable workflow protocol

## Start a run

1. Resolve one active Project Configuration row. If several projects are possible, ask the user.
2. Require `chapter_topic`; accept optional details but ask once when the topic is too ambiguous to
   research responsibly.
3. Reject a second active run by the same user unless the user explicitly queues it. Keep at most
   three queued rows per user.
4. Create a run ID and stable operation ID before any Drive write.
5. Search the project root for a matching chapter folder. Reuse one unambiguous match, create one
   if absent, and stop if several match.
6. Under the chapter folder, create/reuse exactly one direct child for each stage plus a native
   `Logs` workbook and `Automation Resume Record` Doc. Verify every object after creation.
7. Write Queue, Runs, chapter Run State, Resume Record, and Events checkpoints. Only then start Broad
   Research.

## Perform a stage

Read the adapter in `references/roles/<stage>.md`. It points to the original worker, evaluator,
diagnose, formatting, and rubric resources. Adapter rules replace Gumloop calls, Slack, and any
instruction to continue without human approval.

Evaluate and Diagnose must also follow `references/safe-evaluation.md`. Evaluation never mutates
the source artifact in the subscription edition; all findings live in a separate verified native
evaluation report. Diagnose uses that report for evaluation failures and uses open Doc comments
only for human-feedback revisions.

For each role attempt:

1. Set a stable operation ID: `<run-id>:<stage>:<role>:v<version>:a<attempt>`.
2. Check Events and the stage folder for an existing receipt carrying that ID.
3. Write `BEFORE_<ROLE>` to Run State, Resume Record, and Events.
4. Start a fresh isolated agent when available. Pass only topic/details when required, approved
   upstream Doc IDs, destination folder ID, version, attempt, and operation ID.
5. The role reads source Docs and comments itself. It returns metadata only.
6. Verify native MIME type, authorized parent, ID, and required metadata.
7. Append one Artifact Log row and read it back.
8. Write `AFTER_<ROLE>` checkpoints. Only then route the next transition.

Worker success always routes to Evaluate. Evaluation pass routes to `AWAITING_APPROVAL`, never the
next stage. Evaluation failure routes to Diagnose if the review cycle has fewer than three diagnose
attempts. Diagnose success creates the next version and routes back to Evaluate. A malformed result,
missing artifact, or attempt exhaustion sets `BLOCKED`.

## Human decisions

An approval command must identify one run unambiguously. Compare the supplied or inferred Doc ID to
the exact current Pending Doc ID. Record a unique Decision row first, then copy the Doc ID into the
corresponding Approved column and advance to the next stage. Duplicate decisions are harmless.

For `COMMENTS_READY`, confirm open comments exist on the exact pending Doc, record the decision, and
start a new review cycle at Diagnose. The controller never reads or paraphrases comment text.

For Blueprint selection, record the exact options Doc ID and verbatim choice. Resume the existing
worker operation to build the complete blueprint; do not create a second Block 1 worker.

## Scheduled recovery

Each scheduled wake-up processes no more than one transition:

- `READY`: claim the row by writing a new operation ID and `RUNNING`, then verify the readback.
- stale `RUNNING`: reconcile the recorded operation with Drive and Events. Complete its missing
  after-checkpoint or safely retry only when absence is proven.
- due `PAUSED_LIMIT`: reconcile and resume from `Next Action`.
- approval/selection states: do nothing and remain quiet.
- blocked/completed/cancelled states: do nothing.

If allowance is exhausted, preserve the last confirmed checkpoint when possible, set
`PAUSED_LIMIT`, and store the visible reset time in `Not Before`. If no reset time is visible, use
the next normal scheduled check without inventing a time.

## Resume Record body

Keep these fields at the top of the native Doc:

- Run ID and project ID
- Topic and requester
- Chapter folder and Logs workbook links
- Current state, stage, version, and attempt
- Last completed checkpoint
- Approved upstream Doc IDs
- Pending Doc ID and operation ID
- Exact next transition
- Pause or error reason
- Earliest retry time when known
- Last update timestamp

Append a brief chronological checkpoint table below. Do not paste artifact prose into this Doc.
