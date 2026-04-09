# Chapter numbering disambiguation decision record
# Issues #9, #14, #16

## Decision (recorded 2026-01-09)

We have two legitimate "Chapter 2" artifacts that must not collide:

| Label | Content | Location |
|-------|---------|----------|
| **Part I — Chapter 2** | Euclid/Eratosthenes/wheel history ("First Prime Machines") | `manuscript/part-i-history/` or `manuscript/_drafts/ch02/` |
| **Part II — Chapter 2 / First Experiment** | Log-phase circle experiment (log-circle null comparison) | `manuscript/_drafts/part-ii-logphase-experiment/` or the TOC-canonical Part II chapter slot |

## Rules going forward

1. **Part I Chapter 2** is the canonical "Chapter 2" in the running manuscript
   (history: Euclid, Eratosthenes, wheel). Filenames use `ch02-` prefix under Part I.

2. **Part II first experiment** (log-phase circle + nulls) is assigned to its
   TOC-canonical slot in Part II — not called "Chapter 2" unless the TOC explicitly
   numbers it as such there. Filenames use the Part II chapter number from the TOC.

3. No two files in the combined manuscript tree may share the same chapter/section
   number unless they live in different parts AND are cross-linked.

## Cross-link note

Any file referring to "Chapter 2" must qualify the reference:
- "Chapter 2 (Part I — Prime Machines)" for the history chapter.
- "Chapter 2 (Part II — Log-phase experiment)" for the experiment chapter, only if
  the TOC assigns it that number.

## TOC canonical placement (see `manuscript/toc/TOC.md`)

- Part I Chapter 2: confirmed as Euclid/Eratosthenes/wheel history.
- Part II experiment chapter: to be assigned per TOC; update this file when locked.

## Acceptance

- [x] Decision recorded here (Issue #9, #14, #16).
- [ ] TOC/filenames updated to reflect decision when Part II chapter numbering is locked
      (deferred per Issue #20 backlog).
