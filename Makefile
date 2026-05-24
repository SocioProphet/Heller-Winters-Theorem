.PHONY: glossary-strict glossary-check figure-2-1 glossary-apply validate-claim-ledger generate-json-schema check-claim-ledger check-proof-hazards check-p210-character-table check-registry check-finite-character-operator check-antisymmetric-character-operator check-gaussian-integer-operator

## Run glossary enforcement in strict mode (min 1 outside use per term)
glossary-strict:
	GLOSSARY_MIN_OUTSIDE_USES=1 python3 bin/check_glossary_usage.py

## Run glossary check with default threshold (0 = local/dev mode)
glossary-check:
	python3 bin/check_glossary_usage.py

## Regenerate Figure 2.1 (1–120 sieve grid + 30-wheel overlay)
figure-2-1:
	python3 bin/gen_fig2_1.py

## Apply glossary adoption file and run strict-mode check
glossary-apply:
	python3 bin/glossary_construction.py --apply

## Validate prime/operator-lane claim ledger schema fixtures
validate-claim-ledger:
	python3 -m pytest -q tests/test_claim_ledger_schema.py

## Validate proof-hazard negative-control fixtures
check-proof-hazards:
	python3 bin/check_proof_hazard_fixtures.py
	python3 -m pytest -q tests/test_proof_hazard_fixtures.py

## Validate P(7)=210 finite character-table scaffold
check-p210-character-table:
	python3 tools/check_p210_character_table.py

## Validate analytic registry schema fixtures
check-registry:
	python3 -m pytest -q tests/test_zero_registry_schema.py

## Validate finite character-operator diagnostic
check-finite-character-operator:
	python3 tools/check_finite_character_operator.py
	python3 -m pytest -q tests/test_finite_character_operator.py

## Validate antisymmetric finite character-operator diagnostic
check-antisymmetric-character-operator:
	python3 tools/check_antisymmetric_character_operator.py
	python3 -m pytest -q tests/test_antisymmetric_character_operator.py

## Validate Gaussian-integer finite character-operator diagnostic
check-gaussian-integer-operator:
	python3 tools/check_gaussian_integer_operator.py
	python3 -m pytest -q tests/test_gaussian_integer_operator.py

## Generate portable JSON Schema artifacts from Pydantic models
generate-json-schema:
	python3 scripts/generate_json_schema.py

## Run full local/CI claim-ledger gate: regenerate, validate, and verify committed JSON Schema
check-claim-ledger:
	$(MAKE) generate-json-schema
	$(MAKE) validate-claim-ledger
	@if ! git diff --exit-code -- schemas/json; then \
		echo "schemas out of date — run 'make generate-json-schema' and commit schemas/json"; \
		exit 1; \
	fi