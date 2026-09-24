---
name: diagnose-skill-v2
description: Revises a pipeline node's Google Doc after a failed evaluation or a human review. Exports the previous version back to HTML section by section — carrying every untouched block through byte for byte and dropping evaluate's comment blocks — rewrites only the parts the comments name, merges everything into one HTML file, and creates the next version's Doc from that file. The new version is the previous doc exactly, plus the updated and new content. Use after evaluate fails or a human requests changes.
---

# Diagnose

A bounded subagent — runs once and returns. Never pauses for a human,
posts to Slack, touches a tracking sheet, or scores content. Whether the
revision now passes is a fresh `evaluate` call, made by the parent.

**The flow, in this order:**

1. Read the previous version and its comments.
2. Export it to one HTML file per section — evaluate's comment blocks
   dropped, everything else exactly as it is.
3. Diagnose what each comment needs, researching where a fix needs
   material the doc doesn't have.
4. Rewrite only the parts that change, inside their own section file.
5. Merge the section files into one HTML document and verify nothing else
   moved.
6. Create the next version's Doc from that file.

**Old content is carried, never retyped.** The export in Step 2 is code,
so every claim, label, URL, list item and spacer that no comment mentions
arrives in the new version character for character. You write HTML only
for the parts a comment actually names. Re-emitting a whole section by
hand is how content gets dropped and reworded in places nobody asked you
to touch — these documents run to tens of thousands of characters, and
retyping them truncates.

**The previous version is read-only.** You read its text and its
comments. You never write to it, never resolve or delete its comments,
and never delete it.

---

## References

- `references/rubrics/{node_name}.yaml` — this node's output format: the
  exact HTML of every section and block, the spacing each one carries,
  where a new block goes, and the `verify` list for Step 5. Schema in
  `references/rubrics/README.md`.

**All node-specific structure lives in that rubric.** This skill is the
same for every node: it never assumes what sections a document has, what
a block is called, or what counts it tracks. Whenever you need to know
how something is marked up, read the rubric and the exported file — never
work from memory of another node.

**Voice for rewritten prose.** No style file is needed: the previous
version already shows how this node writes each section. Before
rewriting prose, read the neighbouring blocks in that same exported
section and match them — sentence length, how concrete they are, how
they name things. Sections that are data or audit trail stay plain,
exactly as they already read.

---

## Tools

| Tool | Use for |
|------|---------|
| **gdocs** `read_doc` | Reading the previous version (Step 1). |
| **gdocs** comment tool | Reading the previous version's comment threads, with replies (Step 1). |
| **gdocs** `create_doc` | Creating the next version from the merged file (Step 6). |
| **gdocs** `update_doc` | Only to repair a created Doc that came out holding placeholder text (Step 6). |
| **web_search** -firecrawl | Finding a real source when a comment's fix needs evidence the doc doesn't have (Step 3). |
| **web_extract** | Pulling a promising URL in full when the search snippet isn't enough (Step 3). |

Every call runs from the sandbox through the Gumloop client:

```python
from gumloop import Gumloop
client = Gumloop()

result = client.mcp.execute("gdocs", "<tool>", { ... }).results[0]

print("status:", result.status)
if result.status != "success":
    print("error:", result.error)
print(result.decoded_content)
```

`read_doc` returns the document as `result.decoded_content[0]`, with its
paragraphs under `["body"]["content"]`. Work in the sandbox: write files
under `/home/user/`, and keep documents in files rather than in your own
output.

---

## Input you'll receive

- `doc_id` — the previous version's Doc: its comments are read in Step 1,
  its content exported in Step 2. Read-only throughout.
- `evaluation_doc_id` — the evaluation report for that version. Read-only
  context; nothing is ever written back to it.
- `node_name` — selects the rubric.
- `version` — the version being diagnosed. The revision is the next one
  up: `V1` → `V2`.
- `folder_id` — the exact Drive folder the new Doc is created in. This
  skill writes nowhere else; do not resolve, create or guess at another
  location.
- `trigger_source` — `evaluation_failure` or `human_feedback`. Required,
  and given explicitly — never inferred from which other fields arrived.
- `attempts_used` / `max_attempts` — optional, Evaluation Path only.
  **Default `attempts_used` to 0 and `max_attempts` to 3 when either is
  missing; `max_attempts` is never taken above 3.**

If a required input is missing, or a referenced Doc can't be opened, stop
and escalate.

---

## Step 0 — Load the output format

Load `references/rubrics/{node_name}.yaml`. If no file matches
`node_name`, stop and return `status: escalated` with the reasoning line
`no output format for {node_name}` — never guess at markup.

If `attempts_used >= max_attempts`, escalate immediately: no export, no
changes, no new Doc.

---

## Step 1 — Read the previous version and its comments

Read the Doc, and note its title — Step 6 reuses it with the version
incremented.

Then read its comment threads, with their replies. Act on **open**
threads only; a resolved thread is already settled.

- **An `evaluate` comment** carries three lines: `Topic`, `Comment`,
  `Dimension`. `Topic` is the exact section name and matches
  `evaluate_topic` in the rubric; `Comment` is the issue, in one
  sentence. Skip `evaluate`'s general comment that only names what worked
  in a section — it asks for no change.
- **A human comment** — take its text, its replies, and its quoted text
  (the span the human selected), which tells you where it points. A human
  reply inside an `evaluate` thread is a human instruction too.

On the Evaluation Path, the report at `evaluation_doc_id` is useful
context for which sections scored worst. The comments are what you act
on.

If the doc or its comments can't be read, stop and escalate, naming
exactly what couldn't be located — the comments are this skill's entire
input.

---

## Step 2 — Export the previous version, section by section

Write code that reads the Doc and converts it back to HTML: one file per
section under `/home/user/sections`, plus an untouched copy of each under
`/home/user/sections_original` for Step 5 to compare against. No
judgment, no rewriting, and nothing written back to the Doc.

**How each paragraph converts.** This is where the fidelity lives:

- A `HEADING_n` paragraph becomes `<hn>`; a bulleted paragraph becomes
  `<li>`, with one `<ul>` or `<ol>` wrapping each consecutive run of them
  (`<ol>` when the list's glyph is numbered); anything else becomes `<p>`.
- A paragraph whose only text is a non-breaking space becomes
  `<p>&nbsp;</p>` — that is what a blank line is in these documents.
- A paragraph holding a horizontal rule becomes `<hr>`.
- **A table becomes a `<table>`**, one `<tr>` per row and one `<td>` per
  cell — `<th>` where the row is a header — with each cell's paragraphs
  converted by these same rules. Nothing in the document is skipped for
  not being a paragraph: dropping a table loses a whole block of content.
- Runs keep their styling: bold becomes `<strong>`, italic `<em>`, and a
  linked run becomes `<a href="{its own href}">{its own text}</a>`.
  Reproduce what the document has; the rubric's rule about what link text
  should be governs new content, not carried content.
- Escape `&`, `<` and `>`, and write the entities the rubric names
  (`&mdash;`, `&ndash;`, `&hellip;`, `&rarr;`). Never emit CSS.
- Each `HEADING_1` or `HEADING_2` starts a new file, numbered in document
  order so the names sort back into it.

**How `evaluate`'s annotations are dropped** — they are never exported,
not deleted from anything. **Nothing inside a block is read.** The
comments you act on come from the doc's comment threads in Step 1; the
copies `evaluate` inserted into the body are noise to be discarded, never
a source, so no line inside a block is parsed, quoted or carried forward.

- A findings block is bounded by two lines of exactly **26 × `─`**
  (U+2500, the box-drawing character `evaluate` writes — not the hyphen
  `-`). Skip every paragraph from the opening divider through the closing
  one, whatever they say.
- Also skip a truly empty paragraph sitting directly above an opening
  divider — that is `evaluate`'s padding. **A horizontal-rule paragraph
  reads as empty too, so check for the rule first and never drop one.**
- A closing divider can share its line with the original line that
  followed it, because `evaluate` inserts without a trailing newline.
  Export whatever follows the 26 dashes on that line — usually the blank
  line — on its own, so the spacing comes back as it was.
- An odd number of divider lines means a block is broken: stop and
  escalate, naming where. The only thing to check inside a pair is that
  every line looks like an annotation line — bullet-prefixed or blank.
  Anything else means the dividers don't bound what you think they do, so
  stop rather than drop real content. Never guess where a broken block
  ends.

Read the exported files before Step 3. They are what you edit, and they
show the exact shape every block in this document already follows.

---

## Step 3 — Diagnose: what does each comment need?

**One comment can need several changes**, in more than one section. Work
out all of them. For every comment:

1. **Look at the section's exported HTML** — which blocks it holds, how
   many, their identifiers, the order they run in.
2. **Decide what it needs**, and nothing more: **rewrite** (content is
   there but wrong or weak), **add** (something is missing), or
   **remove** (something shouldn't be there).
3. **Research what the fix needs.** If a change needs a fact, source or
   figure the doc doesn't have, search for it and use only what you
   actually find. If nothing real exists, use the alternative the rubric
   allows for that case where there is one, or — on the Evaluation Path
   — escalate. Never invent a source, finding, figure or date to make a
   comment answerable.
4. **Write the new HTML from the rubric's template** for that block: the
   same tags, the same spacer paragraphs, the same separators, and the
   rubric's own rules. Only the words are new. No CSS, ever.
5. **Match the section's own voice** for prose you rewrite.
6. **Knock-ons.** A change to a count or an identifier changes whatever
   refers to it elsewhere in the document. The rubric says which fields
   those are. Each is its own change — skipping them fails `evaluate`'s
   consistency checks on the next run.
7. **The version mention.** Where the document states its own version, it
   changes to the new version number, and nothing else on that line
   changes. A version belonging to something the content is about — a
   model, a product, a paper — is never touched.

The result is a change list, **one row per change, not per comment**:
the file, the action, the exact `old` HTML from that file, and the `new`
HTML. `old` must appear in its file exactly once — if it doesn't, include
the line before or after it until it does. Lists are always changed
whole: one list out, one list in, since a lone `<li>` starts a second
list.

---

## Step 4 — Rewrite only what changes

Apply each row as a single string swap inside one section file: find
`old`, confirm it appears exactly once, replace it with `new`, and leave
the rest of the file untouched. Adding is the same swap with the anchor
block plus the new block; removing is the swap with an empty string.

If `old` isn't found exactly once, nothing is written — re-read the
section file, fix the row, and run it again.

Keep the list of file names you changed; Step 5 needs it.

---

## Step 5 — Merge and verify

Concatenate the section files in name order into one HTML document at
`/home/user/revision.html`. Then prove the merge is the previous version
plus exactly the planned changes:

1. Every file Step 4 did **not** change is byte-identical to its copy in
   `/home/user/sections_original`, and every file it **did** change
   really differs.
2. No divider line and no `• Topic:` / `• Comment:` / `• Dimension:` text
   survives anywhere.
3. No `style` attribute, `class` or `<style>` block appears.
4. In the blocks you changed, links follow the rubric's link rule.
5. No empty list item or empty heading, and no spacer paragraph inside a
   list.
6. The rubric's `verify` list holds for every section you changed.

Each failure is a real defect: fix the section file, merge again, verify
again. Only a clean run goes to Step 6.

---

## Step 6 — Create the next version's Doc

Name it exactly like the previous version with only the version number
incremented — `…_v1_…` becomes `…_v2_…`. If the title carries no version
token, append one for `version + 1`. If a Doc with that name already
exists in the folder, don't overwrite or delete it — escalate, naming it.

> **Never pass the HTML as a literal tool-call parameter.** A revision
> runs to tens of thousands of characters. Typing it into a tool call
> means re-emitting the whole document as tokens, which truncates, fails,
> and leads to placeholder text being sent instead. The document body
> must reach the tool as a **variable read from the file**, never as text
> you retype. Do not print the HTML to inspect it, and do not try to copy
> it out of a previous output — open the file and pass the handle's
> contents.

```python
with open('/home/user/revision.html', encoding='utf-8') as f:
    content = f.read()

from gumloop import Gumloop
client = Gumloop()

result = client.mcp.execute("gdocs", "create_doc", {
    "title": "{the previous title, version incremented}",
    "content_format": "html",
    "content": content,
    "folder_id": "{folder_id}"
}).results[0]

print("status:", result.status)
if result.status != "success":
    print("error:", result.error)
print(result.decoded_content)
```

Nothing is written anywhere outside that folder, and the previous version
is left exactly as it was.

If the created document ever ends up holding placeholder text, do not
create another one. Fix the same document in place with `update_doc`,
passing `operation: "replace"` and the content read from the file exactly
as above.

---

## Final Output

Success:

```json
{
  "version": "<incremented_version>",
  "doc_id": "<revised_doc_id>",
  "comment": "New version with updates"
}
```

Escalation:

```json
{
  "version": "<version>",
  "doc_id": null,
  "comment": "Escalated: <short reason>"
}
```

Metadata only — no diffs, no patched text, no diagnostic report. Never
fabricate a doc id.

---

## What this skill does NOT do

- Does not score content, on either path — that's a fresh `evaluate` call.
- Does not infer `trigger_source` — it must be given explicitly.
- Does not decide, on its own initiative, to re-run evaluation after revising — that's the parent's job.
- Does not call another subagent for any part of this.
- Does not publish to a tracking sheet, notify Slack, or ask a human anything.
- Does not write to the previous version, resolve or delete its comments, or delete the doc itself.
- Does not retype content a comment didn't name — carried blocks come through the export, byte for byte.
- Does not re-author a whole section by hand when one block inside it changed.
- Does not pass the document body as a literal tool-call parameter — it is read from the file.
- Does not assume a document's structure from another node — the rubric and the exported files are the only sources.
- Does not add markup the rubric's template doesn't have, and never drops a spacer or separator it has.
- Does not write CSS: no `style` attribute, no `<style>` block, no `class`, anywhere.
- Does not carry an `evaluate` findings block, or any part of one, into the revision.
- Does not fabricate a source, finding, figure or date to satisfy a comment.
- Does not guess at a doc, report or block it can't parse — it escalates with a specific reason instead.
- Does not create a second Doc when the first needs fixing — it repairs that one in place.
- Does not produce a diagnostic report as a saved artifact — the diagnosis is working reasoning, and only its outcome shows up in the revision and the returned `comment`.
