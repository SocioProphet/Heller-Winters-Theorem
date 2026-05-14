# Pydantic Version Pin

Status: active engineering note for the claim-ledger validation stack.

The claim-ledger validation tools pin Pydantic exactly in `requirements-dev.txt`.

Current pin:

```text
pydantic==2.13.3
```

## Why the pin exists

The repository commits generated JSON Schema artifacts under `schemas/json/`. Those files are produced by:

```bash
make generate-json-schema
```

which calls:

```bash
python3 scripts/generate_json_schema.py
```

The generated JSON Schema output depends on Pydantic's JSON Schema emitter. Pydantic minor releases can change schema rendering details such as default handling, title generation, enum representation, `$defs` layout, and field ordering. Those changes may be semantically harmless but still produce a `git diff` in `schemas/json/`.

The CI gate intentionally checks this:

```bash
make check-claim-ledger
```

That target regenerates JSON Schema, runs fixture validation, and fails if generated schema files differ from committed files.

## Failure mode being prevented

Without an exact Pydantic pin, a contributor could change an unrelated schema fixture or test and trigger a JSON Schema diff solely because their installed Pydantic version renders schemas differently. That would make the CI failure look like a claim-ledger problem when it is actually toolchain drift.

The exact pin makes generated schema output deterministic across local development and CI.

## Upgrade procedure

To upgrade Pydantic deliberately:

1. Update `requirements-dev.txt`.
2. Run:

```bash
pip install -r requirements-dev.txt
make check-claim-ledger
```

3. Review the generated schema diff under `schemas/json/`.
4. Commit the dependency pin change and generated schema changes together.
5. In the commit or PR body, state whether the diff is semantic or emitter-only.

If CI fails with a schema drift message, run:

```bash
make generate-json-schema
```

and commit the resulting `schemas/json/` changes if the model change was intentional.
