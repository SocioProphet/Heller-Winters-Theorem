import math


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]
EXPECTED_PHI = [1, 2, 8, 48, 480, 5760, 92160, 1658880, 36495360]
EXPECTED_MAX_GAP = [2, 4, 6, 10, 14, 22, 26, 34, 40]
EXPECTED_DGC = [1, 2, 3, 5, 7, 10, 13, 16, 20]
DIRECT_K_LIMIT = 7


def wheel_residues(n: int) -> list[int]:
    return [a for a in range(n) if math.gcd(a, n) == 1]


def wheel_gaps(residues: list[int], modulus: int) -> list[int]:
    gaps = []
    for i, value in enumerate(residues):
        next_value = residues[(i + 1) % len(residues)]
        gaps.append((next_value - value) % modulus or modulus)
    return gaps


def primorial(k: int) -> int:
    out = 1
    for p in PRIMES[:k]:
        out *= p
    return out


def wheel_stats(k: int) -> tuple[int, int, int, int]:
    n = primorial(k)
    residues = wheel_residues(n)
    gaps = wheel_gaps(residues, n)
    return n, len(residues), max(gaps), len(set(gaps))


def test_totient_formula_for_first_nine_primorials():
    actual = []
    for k in range(1, 10):
        phi = 1
        for p in PRIMES[:k]:
            phi *= p - 1
        actual.append(phi)
    assert actual == EXPECTED_PHI


def test_direct_wheel_gap_verification_bounded_runtime():
    """Direct residue enumeration is intentionally bounded.

    The ninth primorial has 36,495,360 totatives, so brute-force CI
    enumeration is not an honest or stable check. The document records
    the nine-term values; this test directly recomputes the bounded
    prefix where naive enumeration is appropriate.
    """
    actual_max_gap = []
    actual_dgc = []
    for k in range(1, DIRECT_K_LIMIT + 1):
        _, _, max_gap, dgc = wheel_stats(k)
        actual_max_gap.append(max_gap)
        actual_dgc.append(dgc)
    assert actual_max_gap == EXPECTED_MAX_GAP[:DIRECT_K_LIMIT]
    assert actual_dgc == EXPECTED_DGC[:DIRECT_K_LIMIT]


def test_mod_30_reduced_residue_classes():
    assert wheel_residues(30) == [1, 7, 11, 13, 17, 19, 23, 29]


def test_expected_nine_term_values_are_recorded_in_document():
    doc = open(
        "docs/prime-operator-lane/HW-PRIME-CIRCLE-001-primorial-wheel-correspondence.md",
        encoding="utf-8",
    ).read()
    assert "2, 4, 6, 10, 14, 22, 26, 34, 40" in doc
    assert "1, 2, 3, 5, 7, 10, 13, 16, 20" in doc
    assert "36495360" in doc or "36,495,360" in doc


def test_hw_prime_circle_document_has_boundary_language():
    doc = open(
        "docs/prime-operator-lane/HW-PRIME-CIRCLE-001-primorial-wheel-correspondence.md",
        encoding="utf-8",
    ).read()
    assert "A-HW-PRIME-001" in doc
    assert "does not" in doc
    assert "physical constant" in doc
    assert "HW-PRIME-CIRCLE-INV-001" in doc


def test_prime_program_anti_seed_exists():
    anti_seed = open("docs/prime-operator-lane/anti-seed-prime-program.md", encoding="utf-8").read()
    assert "A-HW-PRIME-001" in anti_seed
    assert "physical constants" in anti_seed
    assert "A-HW-PRIME-002" in anti_seed
