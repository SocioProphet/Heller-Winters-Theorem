import math


def test_A_k_lower_bound():
    # |A_k| = |10^(k*rho) - 10^((k-1)*rho)| / |rho|
    # >= (1 - 10^(-1/2)) * 10^(k*(1/2+delta)) / |rho|.
    delta = 0.1
    gamma = 14.1347
    rho = complex(0.5 + delta, gamma)
    for k in range(2, 8):
        A_k = abs(10 ** (k * rho) - 10 ** ((k - 1) * rho)) / abs(rho)
        lower = (1 - 10 ** (-0.5)) * 10 ** (k * (0.5 + delta)) / abs(rho)
        assert A_k >= lower * 0.99


def test_B_k_on_line_dominated_for_large_k():
    # |B_k^on| = O(10^(k/2) * log^2(k)).
    # |A_k| / |B_k^on| has envelope 10^(k*delta)/log^2(10^k),
    # which tends to infinity for delta > 0.
    delta = 0.1
    for k in [10, 20, 50]:
        ratio = 10 ** (k * delta) / (math.log(10**k) ** 2)
        assert ratio > 1


def test_variance_normalized_decreasing():
    # Var_P(W_k)/10^k decreased in the measured P=210 computation.
    # This is finite diagnostic evidence only, not an asymptotic theorem.
    vars_norm = [1.730, 1.446]
    assert vars_norm[1] < vars_norm[0]


def test_proof_obligation_B_k_off_not_discharged():
    # The equidistribution / almost-periodicity argument for other off-line
    # zeros is not formalized in this framework. Guard against premature closure.
    b_k_off_discharged = False
    assert not b_k_off_discharged
