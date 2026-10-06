# Scheduled task prompt

Use this prompt when creating the recurring ChatGPT Work/Codex automation:

> Use the `$writing-agent-plus` skill in the connected Writing Agent repository. Open the configured
> Google Sheet named `Writing Agent Control` through the connected Google Drive account. Inspect the
> Queue tab and process at most one safe, eligible workflow transition according to the skill's
> scheduled-recovery protocol. Reconcile the operation ID before repeating any external write.
> Never advance an approval gate, blueprint-selection gate, or visual-review KEEP/EXCLUDE gate.
> Stay quiet when no transition is eligible. Notify me only when a document needs review, a blueprint
> choice is needed, a Visual Review needs KEEP/EXCLUDE decisions, the run completes, or the workflow
> becomes blocked. If the ChatGPT plan allowance is exhausted, preserve or reconcile the Drive
> checkpoint on the next available run and continue after the displayed reset; never use an API key
> or purchase credits.

Recommended cadence: every 30 minutes. A more frequent schedule consumes allowance faster and does not bypass plan limits.
