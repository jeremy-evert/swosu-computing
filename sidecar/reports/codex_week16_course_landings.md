# Week 1–16 course landing pages

## Built

- Vendored `week-slider.js` and `week-slider.css` byte-for-byte from `computing_commons`, branch `ivy/week16-slider-component`, commit `f8959dd`; provenance is recorded in `assets/week-slider/PROVENANCE.md`.
- Added `week-data.json` with 16 ordered entries and `week1_start_date: 2026-08-17` for CS1, CS2, DSCT, and Computer Architecture.
- Added the slider includes, inline JSON, mount call, and Computing Commons link to all four course pages, preserving each existing quick-links row below the slider.

## Title source citations

Each cited heading is the first `# ` heading on source line 1; the displayed title strips the indicated Week prefix.

### CS1

- `computer_science_1/planning/week-01.md:1` — `# Week 1 — Success Foundations (Aug 17–21)`
- `computer_science_1/planning/week-02.md:1` — `# Week 2 — Learning Science (Aug 24–28)`
- `computer_science_1/planning/week-03.md:1` — `# Week 3 — Growth (Aug 31–Sep 4)`
- `computer_science_1/planning/week-04.md:1` — `# Week 4 — Thinking (Sep 7–11)`
- `computer_science_1/planning/week-05.md:1` — `# Week 5 — Reasoning (Sep 14–18)`
- `computer_science_1/planning/week-06.md:1` — `# Week 6 — Evidence (Sep 21–25)`
- `computer_science_1/planning/week-07.md:1` — `# Week 7 — Design (Sep 28–Oct 2)`
- `computer_science_1/planning/week-08.md:1` — `# Week 8 — Craftsmanship (Oct 5–9)`
- `computer_science_1/planning/week-09.md:1` — `# Week 9 — Evolution (Oct 12–16)`
- `computer_science_1/planning/week-10.md:1` — `# Week 10 — Engineering (Oct 19–23)`
- `computer_science_1/planning/week-11.md:1` — `# Week 11 — Delivery (Oct 26–30)`
- `computer_science_1/planning/week-12.md:1` — `# Week 12 — Productivity (Nov 2–6)`
- `computer_science_1/planning/week-13.md:1` — `# Week 13 — People (Nov 9–13)`
- `computer_science_1/planning/week-14.md:1` — `# Week 14 — Communication (Nov 16–20)`
- `computer_science_1/planning/week-15.md:1` — `# Week 15 — Modern AI (Nov 23–27)`
- `computer_science_1/planning/week-16.md:1` — `# Week 16 — Farkle / Machine Learning fun week (Nov 30–Dec 4)`

### CS2

**Correction made during Ivy's integration review (not by the original
Codex worker):** `computer_science_2/planning/week-NN.md` is stale for
weeks 3–15. A real content re-slide (`b6fc6b1`, "World Bible week-slide:
intro/test/collaborate Week 2-4 -> Week 3-5") shifted the Reasoning Odyssey
gate/rubric chain for weeks 3–15 by one week but did **not** update the
`planning/` files to match (confirmed independently: `planning/week-04.md`
still describes "Collaborating Objects, Composition, and Invariants," which
is now Week 5's topic per `assignments/odyssey_gates/week-05.md` and
`rubrics/odyssey_gates/week-05_rubric.md`'s own headers — the same drift
Anna caught in the separate B1.3b bite). The original worker correctly
followed its own instructions (use `planning/week-NN.md`), which were wrong
for CS2 specifically; CS1 and Computer Architecture were not affected — the
re-slide commit is explicit that it dogfooded in CS2 only. Titles for CS2
weeks 3–15 below were re-derived from
`assignments/odyssey_gates/week-NN.md`'s own current header instead, and
`cs2/week-data.json` plus the inline JSON in `cs2/index.html` were both
corrected to match. Weeks 1, 2, and 16 (no re-slide, no gate file for 1–2,
week 16 the same before and after) are unaffected and use the original
`planning/` source as the worker found it.

- `computer_science_2/planning/week-01.md:1` — `# Week 1 — Success Foundations`
- `computer_science_2/planning/week-02.md:1` — `# Week 2 — Build and Verify Your Local AI Lab`
- `computer_science_2/assignments/odyssey_gates/week-03.md:1` — `# Reasoning Odyssey Gate — Week 3 — Found Your World (ungraded)` → title "Found Your World" ("(ungraded)" is a grading-status note, not part of the topic name, dropped for consistency with the other titles' style)
- `computer_science_2/assignments/odyssey_gates/week-04.md:1` — `# Reasoning Odyssey Gate — Week 4 — Cohesive Object Boundary (S01)`
- `computer_science_2/assignments/odyssey_gates/week-05.md:1` — `# Reasoning Odyssey Gate — Week 5 — Collaborating Objects and Invariant (S01/S08)`
- `computer_science_2/assignments/odyssey_gates/week-06.md:1` — `# Reasoning Odyssey Gate — Week 6 — Earned Substitution (S02)`
- `computer_science_2/assignments/odyssey_gates/week-07.md:1` — `# Reasoning Odyssey Gate — Week 7 — Contract and Swap (S03/S08)`
- `computer_science_2/assignments/odyssey_gates/week-08.md:1` — `# Reasoning Odyssey Gate — Week 8 — World-Fit Data Abstraction (S05)`
- `computer_science_2/assignments/odyssey_gates/week-09.md:1` — `# Reasoning Odyssey Gate — Week 9 — Search/Order Tradeoff (S05/S06)`
- `computer_science_2/assignments/odyssey_gates/week-10.md:1` — `# Reasoning Odyssey Gate — Week 10 — Compact GUI over Tested Model (S04)`
- `computer_science_2/assignments/odyssey_gates/week-11.md:1` — `# Reasoning Odyssey Gate — Week 11 — Honest Visualization from Project Data (S09/S06/S08)`
- `computer_science_2/assignments/odyssey_gates/week-12.md:1` — `# Reasoning Odyssey Gate — Week 12 — Data Storytelling / Flex Clinic (S09 + S07)`
- `computer_science_2/assignments/odyssey_gates/week-13.md:1` — `# Reasoning Odyssey Synthesis Checkpoint — Week 13 — Stabilization and Peer-Review Preparation (S08)`
- `computer_science_2/assignments/odyssey_gates/week-14.md:1` — `# Reasoning Odyssey Synthesis Checkpoint — Week 14 — Culmination Design Review (S01–S08)`
- `computer_science_2/assignments/odyssey_gates/week-15.md:1` — `# Reasoning Odyssey Gate — Week 15 — Professional Workflow Receipt (S08)`
- `computer_science_2/planning/week-16.md:1` — `# Week 16 — Shared Farkle + Machine Learning Applied Fun` (week 16's gate header reads "retired" — that marks no Reasoning Odyssey gate this finale week, not a retired topic, so the `planning/` title was kept)

### Computer Architecture

- `computer_architecture/planning/week-01.md:1` — `# Week 1 - Success Foundations (Aug 17-21)`
- `computer_architecture/planning/week-02.md:1` — `# Week 2 - AI Laboratory Training (Aug 24-28)`
- `computer_architecture/planning/week-03.md:1` — `# Week 3 - Containers & Repeatability (Aug 31-Sep 4)`
- `computer_architecture/planning/week-04.md:1` — `# Week 4 - Linux as a Machine Telescope (Sep 8-11)`
- `computer_architecture/planning/week-05.md:1` — `# Week 5 - Build the Machine (Sep 14-18)`
- `computer_architecture/planning/week-06.md:1` — `# Week 6 - Bits Become Instructions (Sep 21-25)`
- `computer_architecture/planning/week-07.md:1` — `# Week 7 - Crack Open the CPU (Sep 28-Oct 2)`
- `computer_architecture/planning/week-08.md:1` — `# Week 8 - Make It Fast Without Breaking It (Oct 5-9)`
- `computer_architecture/planning/week-09.md:1` — `# Week 9 - Follow the Program Down (Oct 12-14)`
- `computer_architecture/planning/week-10.md:1` — `# Week 10 - Make the Memory Hierarchy Hurt (Oct 19-23)`
- `computer_architecture/planning/week-11.md:1` — `# Week 11 - The Useful Lie of Memory (Oct 26-30)`
- `computer_architecture/planning/week-12.md:1` — `# Week 12 - More Cores, More Problems (Nov 2-6)`
- `computer_architecture/planning/week-13.md:1` — `# Week 13 - Different Machines for Different Work (Nov 9-13)`
- `computer_architecture/planning/week-14.md:1` — `# Week 14 - Sit in the Architect's Chair (Nov 16-20)`
- `computer_architecture/planning/week-15.md:1` — `# Week 15 - Thanksgiving Wind-Down (Nov 23-27)`
- `computer_architecture/planning/week-16.md:1` — `# Week 16 - Farkle + Machine Learning (Nov 30-Dec 4)`

### DSCT

- `discrete_structures_and_critical_thinking/week-01/README.md:1` — `# Week 1 — Reasoning Odyssey launch`
- `discrete_structures_and_critical_thinking/week-02/README.md:1` — `# Week 2 — Building Your AI Lab / Containers and Repeatability`
- `discrete_structures_and_critical_thinking/week-03/student/container-latex-skill-ladder.md:1` — `# Week 3 — running your reasoning in a container`
- `discrete_structures_and_critical_thinking/week-04/README.md:1` — `# Week 4 — Logic, Claims & Proof`
- `discrete_structures_and_critical_thinking/week-05/README.md:1` — `# Week 5 — Sets, Functions & Sequences as Representations`
- `discrete_structures_and_critical_thinking/week-06/README.md:1` — `# Week 6 — Algorithms, Correctness & Growth`
- `discrete_structures_and_critical_thinking/week-07/README.md:1` — `# Week 7 — Integer Properties & Cryptography`
- `discrete_structures_and_critical_thinking/week-08/README.md:1` — `# Week 8 — Induction, Recursion & Recurrences`
- `discrete_structures_and_critical_thinking/week-09/README.md:1` — `# Week 9 — Counting & Combinatorial Reasoning`
- `discrete_structures_and_critical_thinking/week-10/README.md:1` — `# Week 10 — Probability, Uncertainty & Evidence`
- `discrete_structures_and_critical_thinking/week-11/README.md:1` — `# Week 11 — Relations, Equivalence, Partial Orders, Matrices & Digraphs`
- `discrete_structures_and_critical_thinking/week-12/README.md:1` — `# Week 12 — Graphs & Network Reasoning`
- `discrete_structures_and_critical_thinking/week-13/README.md:1` — `# Week 13 — Trees, Search & Decision Structures`
- `discrete_structures_and_critical_thinking/week-14/README.md:1` — `# Week 14 — Boolean Algebra, Circuits, SAT & Finite-State Machines`
- `discrete_structures_and_critical_thinking/week-15/README.md:1` — `# Week 15 — Thanksgiving / Mexico Travel Buffer`
- `discrete_structures_and_critical_thinking/week-16/README.md:1` — `# Week 16 — Farkle, Machine Learning, and What the Evidence Lets You Say`

DSCT Week 3 is the authorized one-off source substitution: `week-03/README.md` does not exist on `origin/main`; the title comes from `week-03/student/container-latex-skill-ladder.md:1`, whose heading is `# Week 3 — running your reasoning in a container`.

## Known placeholders and unresolved link

Every week's URL intentionally repeats its course's existing Canvas front-page URL:

- CS1: `https://swosu.instructure.com/courses/74029`
- CS2: `https://swosu.instructure.com/courses/74031`
- DSCT: `https://swosu.instructure.com/courses/74035`
- Architecture: `https://swosu.instructure.com/courses/75249`

These are known placeholders; Flo should swap them for real per-week Canvas module links once those modules exist and are loaded. No Canvas authentication or live Canvas access was used.

No existing Computing Commons URL was present in the four pages, so each page uses the relative placeholder `../commons.swosu-computing/`; this remains unresolved and must be replaced when the hub URL is known.

## Checks

Ran from the isolated worktree:

- `node` JSON validation: all four `week-data.json` files have 16 ordered entries and the shared start date.
- Static page check with `node`: all four pages contain the CSS/JS includes, slider container, application/json block, mount call, and 16-entry inline data; output was `cs1 OK`, `cs2 OK`, `architecture OK`, `dsct OK`.
- SHA-256 comparison: vendored JS and CSS matched the accepted source files exactly.
- `git diff --check`: passed.
- No browser-level render or console check was available in this environment; no browser success is claimed.
