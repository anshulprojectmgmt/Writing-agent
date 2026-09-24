# Section Design Guide — The Technology Beneath

Full specification for the mandatory `[TECH]` section referenced in
Block 1 and Block 2.

## Purpose

The `[TECH]` section's only job is giving the reader usable vocabulary —
named technical concepts explained in plain English, connected to what
they actually enable in a real product. Not a lecture. A field manual.

## What a strong [TECH] section does

1. **Names 1–3 specific technical concepts** relevant to the chapter's
   topic — not "AI" generically, but the actual mechanism (e.g. "context
   window," "retrieval-augmented generation," "tool use," "chain-of-
   thought reasoning").
2. **Explains each with an analogy first, abstraction second.** Reach for
   a concrete comparison before the formal definition — the definition
   lands better once the analogy has done the work.
3. **Connects the concept to product behavior.** Every concept should
   answer "so what does this actually let a product do?" — not stay
   abstract.
4. **Includes exactly one WOW MOMENT** — a specific, sourced, surprising
   finding or benchmark that makes a knowledgeable reader sit up. This
   is not the place for a generic "AI is advancing fast" statement; it
   needs a real, specific number or example.
5. **Ends with something quotable** — a one-sentence takeaway the reader
   could repeat in a meeting and sound sharp doing it.

## What a weak [TECH] section looks like (avoid)

- Defines a term correctly but never connects it to product behavior
- Uses jargon to explain jargon (avoid unless the term is truly
  unavoidable — then define it in the same sentence)
- WOW MOMENT is actually just "AI is really impressive these days" with
  no specific number, source, or example behind it
- Reads like a textbook glossary entry rather than something a PM would
  actually say out loud

## Placement

The `[TECH]` section can sit early (establishing vocabulary before the
chapter's argument needs it) or late (once the reader has enough context
to appreciate the mechanism) — this is a legitimate structural choice
between Block 1 options, not a fixed rule. Different placement is one
of the valid ways two options can meaningfully differ from each other.
