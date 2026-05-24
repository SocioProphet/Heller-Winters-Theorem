import math


def test_parseval_bias_is_a_proof_obligation_not_a_theorem():
    # This test asserts that the Parseval-bias lower bound for off-line zeros
    # has NOT been proved within this framework. It is a proof target.
    #
    # Target statement, not discharged here:
    #   Var_P(W_k) = Omega(10^((1+2*delta)*k) / k^2)
    #   if L(s,chi) has a zero at Re(rho)=1/2+delta, delta>0.
    proof_discharged = False
    assert not proof_discharged


def test_hyperbolic_lower_bound_grows_exponentially_in_theory():
    # The cosh lower bound on the off-line envelope is computable from the
    # hyperbolic mechanism. This does not discharge the Parseval-bias proof
    # obligation; it checks the envelope-growth side only.
    delta = 0.1
    for k in [5, 10, 20]:
        cosh_bound = math.cosh(delta * k * math.log(10)) ** 2
        poly_bound = k**2 * math.log(k) ** 4
        if k >= 10:
            assert cosh_bound > poly_bound
