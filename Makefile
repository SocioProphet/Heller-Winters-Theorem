.PHONY: glossary-strict glossary-check figure-2-1

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
