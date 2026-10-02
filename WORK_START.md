# Codex entry point

Run the Products of Tomorrow workflow in an interactive Codex chat, not as a headless shell job. Read this file completely, then `Book Orchestrator Agent/SKILL.md` and `Book Orchestrator Agent/references/codex-runtime.md` completely before acting.

## Setup in the receiving account

1. Fetch the entire repository at one resolved commit. Record that commit in the run; never pull changing instructions during a chapter. The substantive stage packages are from source revision `1512c022298eb542de5e3683b06727dba43294bd`.
2. Use the available personal skill installation mechanism to install the eight complete packages listed in the orchestrator skill and the orchestrator itself. Preserve each stage package's adjacent instruction.md and references recursively. For the orchestrator, install only its SKILL.md, instruction.md and references/codex-runtime.md; do NOT recursively install its nested node folders as duplicate skills. Retain the complete pinned repository checkout separately for node-controller files and source paths. Do not generate substitutes. The orchestrator's relative source paths must be resolved against that checkout, not against an installed personal skill directory. Record that checkout path as `workflow_source_root`. If the host cannot install skills, disclose that; direct complete-file loading can prepare a run but is not a verified installation. Do not imply skills are attached automatically.
3. If an installed package with the same frontmatter name differs, do not overwrite it silently. Compare and ask whether to replace or use an isolated copy. Do not load multiple conflicting copies.
4. Run `python3 scripts/verify_workflow.py` in the checkout. This is performed by Codex; do not ask the reviewer to use a terminal. The validator checks source integrity, package paths and required files; it does NOT certify live tools or account/model access.
5. Discover live Google Drive/Docs/Sheets and web-search capabilities, and read their applicable skills. Select the receiving user's own Google account. If one account is connected, state its actual email and use it. If several exist, ask once. Never use someone else's connector identifiers or credentials. If disconnected, ask the user to connect the Google Drive plugin; never request passwords in chat.
6. Verify actual model selection, reasoning selection and fresh-context delegation. A model name in a prompt is not a model selection. Follow the exact runtime table; stop before production if required worker settings cannot be enforced. Disclose the specified controller fallback if needed.
7. Create a fresh standalone chapter folder and its Logs sheet and a receiving-account Writing Agent Control sheet. Verify actual Docs/Sheets write and read-back using these setup artifacts, and verify HTML import plus native comment creation/read-back on a clearly titled Setup Verification Doc inside the new folder. Keep it labelled as setup, not a chapter artifact. If importing or native comments are unavailable, stop before research and explain the missing capability. Do not silently degrade to plain text or report-only evaluation.
8. Set up recovery only through a real exposed automation capability, as defined by the runtime reference. If unavailable, offer manual resume and ask the reviewer whether to continue without automatic recovery. A control sheet alone is not a scheduler.
9. Show the account, pinned commit, actual models, folder/Logs/control links and scheduler status. If checks pass and the user requested a start, run Broad Research and stop at its human approval gate. Do not add an extra setup approval gate when no material choice or blocker exists.

Preserve all chapter drafts, reports, native comments, version histories and approval checkpoints. Do not load an old chapter as evidence, do not copy prior exceptions into this run, and do not import personal run IDs, document IDs or approvals.

## Receiving-user launch

The user provides the topic and details in the chat and requests this entry point. Resolve all other IDs in their own account. If topic or details are missing, ask for both together. On interruption, resume by reading the receiving account's control sheet and Logs; never start over merely because the chat lost context.

This entry point reproduces the completed Codex run's execution policy. It does not promise identical stochastic prose, plan credits, model availability or connector availability on another account.
