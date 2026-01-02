# Part II — Technical Core (Heller–Winters Construction)

We keep edits small and isolatable by enforcing a three-level lattice:

- `chapter-XX-*` — chapter scope
- `sections/NN-*` — section/subtopic scope
- `subsections/` — sub-subtopic scope (three default lanes):
  01-context, 02-formalism, 03-tests

Each node has:
- `README.md` (human-facing overview)
- `toc/TOC.md` (local navigation)
- optional `versions/`, `synthesis/`, `notes/` if needed later
