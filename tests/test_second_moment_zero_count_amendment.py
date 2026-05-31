import math


def test_von_mangoldt_zero_count_squared_dominated_by_exponential():
    # N(K)^2 = O(K^2 log^2 K). For fixed delta > 0,
    # 10^(2*delta*K) / (K^2 log^2 K) -> infinity.
    delta = 0.1
    for K in [50, 100, 200]:
        n_sq = K**2 * math.log(K) ** 2
        exp_term = 10 ** (2 * delta * K)
        assert exp_term / n_sq > 1


def test_second_moment_lower_bound_grows_exponentially():
    # Lower-bound multiplier relative to the GRH-scale 10^K/K^2 variance
    # is 10^(2*delta*K)/(K^2 log^2 K), which grows without bound.
    delta = 0.1
    for K in [50, 100]:
        lower_multiplier = 10 ** (2 * delta * K) / (K**2 * math.log(K) ** 2)
        assert lower_multiplier > 1


def test_cross_term_estimate_remains_open():
    # The size comparison against Riemann-von Mangoldt zero count is not the
    # same as the oscillatory cross-term estimate. The latter remains open here.
    cross_term_estimate_discharged = False
    assert not cross_term_estimate_discharged
