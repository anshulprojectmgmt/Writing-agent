# Writing Agent Plus

Subscription-only edition for ChatGPT Work and Codex. It uses the signed-in ChatGPT plan, the
connected Google Drive account, native skills, and scheduled task wake-ups. It does not use the
OpenAI API, Cloud Run, Firestore, or a separately billed model key.

## Install

1. Connect this repository to Codex Cloud or open it as a Codex project.
2. Add the repository marketplace: `codex plugin marketplace add <repo>/.agents/plugins`.
3. Install: `codex plugin add writing-agent-plus@personal`.
4. Start a new chat so the skill is loaded.
5. Install/connect the official Google Drive plugin and authorize the account that owns the book
   folder.

## First command

`Use $writing-agent-plus to set up my Writing Agent project in Google Drive.`

After preflight succeeds:

`Start a chapter about <topic>. Details: <scope, audience, and important constraints>.`

The automation stops after every passing stage for explicit approval. Review the linked Google Doc
and reply `Approved`, or add comments and reply `Comments ready`.

See the skill references for the control-sheet schema, recovery behavior, and scheduled-task prompt.
