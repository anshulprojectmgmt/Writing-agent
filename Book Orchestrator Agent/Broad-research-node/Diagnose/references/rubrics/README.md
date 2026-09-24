# Output-format rubrics

One file per node, named to match `node_name` exactly (plus `.yaml`) —
the same layout as `evaluate`'s rubrics. Where `evaluate`'s rubric says
what a section must *contain*, this one says how it must be *marked up*:
the exact HTML, spacing included, that the node's own skill generated.
`diagnose` builds every fix from these templates, so a revised block
looks exactly like the blocks around it.

| `node_name` | file | source |
|---|---|---|
| `broad_research` | `broad_research.yaml` | Broad Research skill v2 → `references/output-formatting.md` |
| `chapter_blueprint` | `chapter_blueprint.yaml` | Chapter Blueprint skill → `references/output-formatting.md` |
| `chapter_writing` | `chapter_writing.yaml` | Chapter Writing skill → its own Formatting + Delivery Format sections (this node has no output-formatting file) |
| `deep_research` | `deep_research.yaml` | Deep Research skill → `references/output-formatting.md` |
| `research_analysis` | `research_analysis.yaml` | Research Analysis skill → `references/output-formatting.md` |
| `research_mapping` | `research_mapping.yaml` | Research Mapping skill → `references/output-formatting.md` |

A node with no file here makes `diagnose` escalate with
`no output format for {node_name}` — it never guesses at markup.

## Schema

```yaml
node_name: broad_research
content_format: html

global:
  spacer: "<p>&nbsp;</p>"
  rules: [...]          # markup rules that apply to every section
  headings: {...}       # which tag is used for what
  in_the_doc: {...}     # how the HTML reads back from read_doc — used to find indexes

sections:
  - id: source_ladder_findings
    heading: "3. Source Ladder Findings"                        # exact heading text in the doc
    evaluate_topic: "3. Source Ladder Findings (Rungs 1-10)"    # the Topic evaluate writes for this section
    section: |                                                  # the section's outer shell
      <h2>3. Source Ladder Findings</h2>
      <p>&nbsp;</p>
      <hr>
      <p>&nbsp;</p>
      {rungs}
    blocks:                                     # repeatable units inside the section
      finding:
        html: |
          ...exact template, spacers included...
        add_after: "where a new one goes"
    rules: [...]                                # section-specific markup rules

verify: [...]           # checks run on the merged revision (diagnose Step 5)
```

- Some sections also carry `also_resolves` — other `Topic:` lines evaluate can write for content that lives in that same section.
- `heading` is what `diagnose` searches for in the doc; `evaluate_topic`
  is what an `evaluate` comment's `Topic:` line says. They differ where
  `evaluate`'s rubric names the section differently (e.g. Section 3).
- Templates are markup only. `{…}` placeholders take the fix's words;
  every tag, spacer and `<hr>` around them stays exactly as written.
- To add a node: convert that node's output-formatting file into this
  shape and list it in the table above.
