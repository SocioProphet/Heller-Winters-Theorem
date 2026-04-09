# Contributing Guide

## Draft Versioning Protocol (Issue #18)

Every chapter draft rendition must be stored as a versioned artifact in
`manuscript/_drafts/chXX/`.

### File naming

```
vNN-chXX--YYYYMMDD.md
```

Examples:
- `v01-ch02--20260101.md`
- `v04-ch02--20260109.md`

### VERSIONS.md index

Each `_drafts/chXX/` directory must contain a `VERSIONS.md` file with:

| Version | Date | Delta summary | Promoted? | Notes |
|---------|------|---------------|-----------|-------|

### Stamping a new version

```bash
# Write content safely — never paste prose into bash
cat <<'EOF' > manuscript/_drafts/ch02/v04-ch02--YYYYMMDD.md
...content...
EOF

# Then update VERSIONS.md
python3 bin/write_draft.py manuscript/_drafts/ch02/VERSIONS.md --append <<'EOF'
| v04 | 2026-01-09 | Euclid proof fix + policy machine defn + sqrt stopping rule | no | |
EOF
```

### Shell ergonomics: never paste prose into bash

Always write content via a file, heredoc, or `bin/write_draft.py`:

```bash
# CORRECT — heredoc as a single compound statement
cat <<'EOF' > path/to/file.md
In Part II we use the Log-circle phase map to embed primes on the unit circle.
EOF

# CORRECT — pipe to write_draft.py
echo "content" | python3 bin/write_draft.py path/to/file.md

# WRONG — pasting prose at the shell prompt
In Part II we use...   # bash: In: command not found
```

`&&` must appear at the **end** of a line, never at the start of a new one:

```bash
# CORRECT
python3 bin/check_glossary_usage.py --strict \
  && echo "OK"

# WRONG
&& python3 bin/check_glossary_usage.py --strict
```

---

## Term Adoption Workflow (Issues #1, #17, #21)

1. Add or update terms in the canonical glossary:
   `manuscript/part-ii-technical-core/chapters/chapter-00-claims-ledger-notation-and-the-reproducibility-standard/sections/0.10-glossary-core-terms.md`

2. Run the adoption tool to update `TERMINOLOGY.md` and check enforcement:
   ```bash
   python3 bin/glossary_construction.py --apply
   ```

3. Or run strict enforcement directly:
   ```bash
   python3 bin/check_glossary_usage.py --strict
   # Equivalent to:
   make glossary-strict
   ```

4. If a term has zero outside uses, either:
   - Use it in at least one non-glossary chapter/note, **or**
   - Remove it from the glossary.

### Stable path lookup

```bash
python3 bin/check_glossary_usage.py --show-path
```

Never regex-scrape the script source to find the glossary path. Use the flag.

---

## Figure Regeneration (Issues #15, #19)

To regenerate Figure 2.1 (sieve grid + wheel overlay):

```bash
python3 bin/gen_fig2_1.py
# Output: manuscript/assets/figures/fig2-1.svg
```

Custom output path:
```bash
python3 bin/gen_fig2_1.py --output path/to/fig.svg
```
