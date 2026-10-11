---
name: storytelling-article
description: Orchestrate Anshul's thinking, evidence, articulation, writing, narrative design, and visualization to create story-led articles from raw thoughts, notes, conversations, or developed ideas. Own story architecture and story-integrity review; delegate voice, prose, formatting, and humanization to anshul-writing-style. Visualization is default unless the user explicitly asks to skip it.
metadata:
  author: Anshul Jain
  version: "1.0"
  display_name: "Storytelling Article"
  status: "prod"
---

# Storytelling Article

## Purpose

Turn a raw thought, conversation, note dump, draft, observation, or developed idea into an article that feels like **one unfolding story**, not a collection of related points.

This skill has two jobs:

1. **Orchestrator** — invoke the right existing Anshul skills in the right order.
2. **Story specialist** — directly own story architecture and final story-integrity review.

Do not duplicate capabilities already owned by other skills.

## Core principle

**Think → articulate → architect the story → write → verify the story survived → visualize.**

Do not use storytelling to make a weak idea sound stronger than it is.
Do not force every stage when the input is already developed.
Do not confuse internal story structure with visible article formatting.

## Activation boundary

Use this skill when Anshul wants to create or substantially rewrite a story-led article, essay, long-form thought-leadership piece, or similar nonfiction where **narrative progression matters**.

Typical triggers include:
- turn this thought into an article
- help me write an article around this idea
- this article does not flow
- make this more story-led
- create the article and visuals
- structure this like a story

Do not use it for a simple caption, short message, factual report, or ordinary explainer unless the user specifically wants a story-led treatment.

---

# Pipeline

The normal pipeline is:

**1. THINK → 2. RESEARCH IF NEEDED → 3. ARTICULATE → 4. STORY ARCHITECTURE → 5. WRITE + FORMAT + HUMANIZE → 6. STORY INTEGRITY REVIEW → 7. VISUALIZE**

This is adaptive. Skip stages whose work is already done, but preserve the ordering of the stages that remain.

---

# 1. THINK

Invoke:

`anshul-brain-thinking-os`

Use Sensemaking, Critical Analysis, and Discovery modes as needed **within the same thinking pass**. Do not create separate mandatory calls for each mode.

Determine, where relevant:
- What triggered the thought?
- What is Anshul actually trying to say?
- What deeper idea explains the surface observation?
- What assumption or conventional belief is being questioned?
- What tension or contradiction makes the idea interesting?
- What changed in Anshul's thinking?
- What causal relationships matter?
- What counterarguments or weaknesses need consideration?
- What remains genuinely uncertain?
- Why does the idea matter?

Preserve uncertainty when it is real. Do not force convergence merely because the final output is an article.

### Handoff to downstream stages

Carry forward a compact internal brief containing only what is useful:

- Trigger
- Core idea
- Old assumption / existing belief
- What changed
- Central tension
- Causal model
- Important counterargument
- Key implications
- Unresolved edge

---

# 2. RESEARCH IF NEEDED

Conditionally invoke:

`anshul-brain-research-and-evidence`

Research only when external evidence materially improves the article, for example when:
- an important factual claim needs verification,
- a current number or trend matters,
- a real example would strengthen the argument,
- a counterargument needs investigation,
- the thesis depends on external facts rather than only reasoning.

**Research supports the story; it does not become the story.**

Prefer a few high-value pieces of evidence over an exhaustive evidence dump.

---

# 3. ARTICULATE

Invoke:

`anshul-brain-articulate-thought-leadership`

Turn the developed thought into the **intellectual spine** of the article.

Clarify:
- What assumption are we starting from?
- What changed?
- Why does that change matter?
- What follows from it?
- What bigger implication appears?
- What new problem, tension, or possibility emerges?
- What is Anshul's emerging point of view?
- What should the reader reconsider after reading?

A useful internal representation is:

**CURRENT ASSUMPTION → CHANGE → IMPLICATION → BIGGER IMPLICATION → NEW TENSION → EMERGING POINT OF VIEW**

This is the argument spine, not yet the story outline.

---

# 4. STORY ARCHITECTURE

This stage is owned directly by `storytelling-article`.

Its purpose is to convert the intellectual argument into a reader journey where each major move makes the next one feel earned.

All of the following are **substeps of Stage 4**, not separate pipeline stages.

## 4.1 Find the central tension

Identify the dominant question, contradiction, or unresolved idea that pulls the reader forward.

Examples:
- This sounds wrong today. Why might it become right?
- If engineering becomes abundant, what becomes scarce?
- If AI makes everyone more productive, why might we need more Product people?

Secondary ideas should support this tension rather than compete with it.

## 4.2 Build Level 1 story beats

Level 1 beats are mandatory.

Usually use **4–7 major beats**. Each beat should represent a meaningful change in the reader's understanding.

Possible beat functions include:
- trigger,
- provocative idea,
- existing assumption,
- disruption,
- realization,
- complication,
- counterargument,
- reversal,
- consequence,
- new bottleneck,
- synthesis,
- unresolved question,
- ending.

These are possible functions, not a template.

## 4.3 Add Level 2 beats only where needed

Level 2 beats are optional.

Use them when a Level 1 beat is complex enough that its internal movement needs planning. Usually **2–4 Level 2 beats** are enough.

Do not force Level 2 beneath every Level 1 beat.
Do not assume Level 2 beats will become visible subheadings.

**Use the minimum story structure required to make causality and progression clear.**

## 4.4 Design the opening

Start close to the real source of the thought whenever possible:
- something Anshul heard,
- something he saw,
- a conversation,
- an incident,
- a question that stayed with him,
- a contradiction,
- a belief that stopped making sense,
- a provocative claim that initially sounds wrong.

Avoid generic setup such as "AI is changing everything."
Do not manufacture an anecdote merely to create a story.

## 4.5 Test causality between beats

Between every two Level 1 beats ask:

> **Why does Beat B follow Beat A?**

Useful internal tests:
- Because this is true, what follows?
- If this changes, what else changes?
- That solves one problem; what new problem appears?
- This sounds convincing, but what breaks?
- If this becomes abundant, what becomes scarce?

If the only answer is "they are both related to the topic," the architecture is weak. Reorder, merge, deepen, or remove beats.

## 4.6 Create progression and escalation

The article should deepen rather than repeat.

A possible movement is:

**OBSERVATION → IMPLICATION → BIGGER IMPLICATION → NEW PROBLEM → REFRAME → EMERGING CONCLUSION**

Do not force this exact pattern. Preserve the actual thought path.

## 4.7 Design transitions and open loops

Where natural, let a beat create forward pull through:
- a question,
- contradiction,
- unresolved consequence,
- surprising implication,
- new problem,
- tension that the next beat answers or deepens.

Do not overuse rhetorical questions. Not every section needs an open loop.

## 4.8 Design the ending

The ending should resolve the journey without making the thought artificially neat.

Valid endings include:
- a changed belief,
- a working conclusion,
- a practical implication,
- a provocative prediction,
- a genuine remaining uncertainty,
- an open question that honestly remains open.

Avoid generic motivation, summary-for-summary's-sake, manufactured punchlines, or certainty stronger than the underlying thinking.

Ask:
- Did the article actually arrive somewhere?
- Is the ending more certain than Anshul really is?

## Story architecture representation

For each important Level 1 beat, keep a lightweight internal representation:

- **Beat** — what happens here?
- **Purpose** — why does it exist?
- **Reader starts believing** — what is the reader's current model?
- **Movement** — what changes here?
- **Reader ends believing** — what do they now understand?
- **Next tension** — what pulls them forward?

Add Level 2 beats only where useful.

---

# 5. WRITE + FORMAT + HUMANIZE

Invoke:

`anshul-writing-style`

Provide it with:
- original source material,
- developed thought,
- argument spine,
- Level 1 beats,
- relevant Level 2 beats,
- evidence where needed,
- central tension,
- intended emotional tone,
- important original phrases worth preserving.

`anshul-writing-style` owns:
- voice,
- vocabulary,
- sentence rhythm,
- paragraph construction,
- visible headings,
- bullets,
- paragraph breaks,
- emphasis and formatting choices,
- bold / underline conventions when appropriate,
- simplicity,
- humour,
- emotion,
- self-correction,
- natural uncertainty,
- humanization.

Its internal `ai-humanizer-core` remains part of the same writing pass. Do not invoke the humanizer separately.

### Important boundary

`storytelling-article` does **not** run a second detailed formatting stage.

Internal L1/L2 story beats do not automatically become visible headers/subheaders. The writing skill decides how the article should look on the page while preserving the intended story.

---

# 6. STORY INTEGRITY REVIEW

This stage is owned directly by `storytelling-article`.

Compare the **planned story architecture** with the **written and formatted article**.

The goal is not to re-edit every sentence. The goal is to verify that the narrative structure survived the writing process.

Check:

### Progression
- Can the Level 1 progression still be felt in the article?
- Did two beats accidentally collapse into one?
- Did any section become a side-track?

### Causality
- Does each major section still earn the next one?
- Were any essential causal transitions lost during writing?

### Central tension
- Is the main tension still visible?
- Does the article keep pulling on the same core question rather than drifting into several competing theses?

### Visible structure
- Does the formatting make the intended storyline easier to perceive?
- Did too many headings fragment the narrative?
- Did too little structure bury an important story turn?
- Did an internal L2 beat accidentally become an unnecessary visible section?

Do **not** impose a formatting template. Review only whether the formatting supports the architecture.

### Ending
- Does the final ending land where the designed story was supposed to land?
- Did writing polish make it more certain, generic, or neat than the actual thought?

### Fixing failures

If the structure did not survive, issue **targeted corrections** back to `anshul-writing-style`.

Do not regenerate unaffected sections.

Examples:
- missing causal bridge → repair that transition,
- two beats collapsed → restore the distinction,
- too many visible headers → reduce headers without changing the underlying beats,
- story tension diluted → sharpen the relevant passages,
- ending became generic → restore the actual unresolved edge.

After correction, re-run the story-integrity check once.

---

# 7. VISUALIZE — DEFAULT

Unless Anshul explicitly asks to skip visuals, invoke:

`anshul-brain-visualize-idea`

Visualization is the **default final stage**, not an optional extra that must be requested.

Pass the visual skill:
- central idea,
- central tension,
- Level 1 story beats,
- relevant Level 2 beats,
- emotional/intellectual progression,
- important transitions,
- open loops,
- final reader realization,
- final article where useful.

Do not merely pass the finished prose and ask for "some images."

The visual treatment should preserve the same narrative spine as the article.

For a multi-image story, use an internal mapping such as:

**IMAGE 1** — story beat / core message / ending tension
**IMAGE 2** — answer or continuation / core message / next tension
**IMAGE 3+** — continue the progression

Images should not become disconnected summary cards.

If only one visual is appropriate, identify the single image concept that best captures the article's central tension or realization.

Actual rendering should follow the normal visual/image-generation workflow available in the environment.

Skip Stage 7 only when Anshul explicitly says things such as:
- no visuals,
- article only,
- skip images,
- just give me the text.

---

# Adaptive routing

Do not run every upstream stage at full depth.

### Raw or unresolved thought
**THINK → RESEARCH IF NEEDED → ARTICULATE → STORY ARCHITECTURE → WRITE → STORY REVIEW → VISUALIZE**

### Already-developed idea
**ARTICULATE → STORY ARCHITECTURE → WRITE → STORY REVIEW → VISUALIZE**

### Evidence-heavy argument
**THINK → RESEARCH → ARTICULATE → STORY ARCHITECTURE → WRITE → STORY REVIEW → VISUALIZE**

### Existing article with a flow problem
Diagnose whether the issue is:
- thinking / thesis,
- articulation,
- story architecture,
- writing / voice,
- story integrity.

Repair the affected layer rather than restarting the full pipeline.

---

# Feedback routing

When Anshul gives feedback, diagnose the layer before changing the article.

- **"This isn't what I mean."** → THINK / ARTICULATE
- **"This doesn't flow."** → STORY ARCHITECTURE
- **"This section doesn't connect."** → STORY ARCHITECTURE, especially causal transition
- **"Too many line breaks / headers / bullets."** → `anshul-writing-style`; then verify story integrity
- **"Doesn't sound like me."** → `anshul-writing-style`
- **"The ending isn't right."** → STORY ARCHITECTURE + actual unresolved thought
- **"The images don't connect."** → VISUAL STORY MAPPING

**Preserve good work from unaffected layers. Do not regenerate the entire article for a local problem.**

---

# Long-form routing

For a normal article, keep story architecture inside this skill.

If the work becomes substantially larger and resembles a book chapter, deep essay, multi-part nonfiction argument, or research-heavy long-form project, consider handing the broader development to:

`anshul-brain-develop-and-write-nonfiction`

Then use this skill where story-led article architecture is still useful.

Do not automatically turn an article into a book chapter.

---

# Final QA

Before finalizing, ask:

### Idea
Can the central insight be expressed clearly in one or two sentences?

### Tension
Is there a reason to continue reading after the opening?

### Story
Does each Level 1 beat meaningfully change the reader's understanding?

### Causality
Can we explain why each major beat follows the previous one?

### Progression
Does the article deepen rather than repeat?

### Authenticity
Does it preserve Anshul's actual thought process and uncertainty?

### Voice and formatting
Did `anshul-writing-style` produce something that sounds and looks like Anshul while keeping the story visible?

### Ending
Did the article arrive somewhere meaningful without forcing certainty?

### Visuals
Unless explicitly skipped, did the visual concept/sequence carry the same central tension and story progression?

---

# Anti-patterns

Reject or rework the article if it feels like:
- a collection of good points,
- a research report disguised as an article,
- a framework with a story pasted around it,
- a sequence of headings and explanations,
- generic LinkedIn thought leadership,
- excessive internal structure exposed as visible headings,
- a conclusion more certain than Anshul's actual position,
- a story imposed on an idea that was better expressed directly,
- visuals that summarize isolated points instead of continuing the story.

Desired reader reaction:

> **"I can see how he arrived at this thought — and now I am thinking about it too."**

# Governing principle

**Do not optimize every paragraph independently. Optimize the reader's journey through the idea.**

The final result should preserve:

**Anshul's thinking + intellectual rigor + narrative progression + Anshul's voice + natural formatting + coherent visuals.**
