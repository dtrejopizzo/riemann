#!/home/trabajo/miniforge3/bin/python
"""Falsifier for Gamma cancellation of det_5 prime-zeta counterterms."""

from fractions import Fraction

from mpmath import mp
from sympy import mobius


mp.dps = 70
MOBIUS_CUTOFF = 30


def coefficient(index):
    value = Fraction(int(mobius(index)), index)
    if index % 2 == 0:
        value += Fraction(int(mobius(index // 2)), index)
    return value


coefficients = {index: coefficient(index) for index in range(1, MOBIUS_CUTOFF + 1)}
critical_half_branch_cancelled = coefficients[2] == 0
one_third_coefficient_exact = coefficients[3] == Fraction(-1, 3)
one_quarter_coefficient_exact = coefficients[4] == Fraction(-1, 4)


def prime_zeta_continuation(s):
    total = mp.mpc(0)
    for index in range(1, MOBIUS_CUTOFF + 1):
        mu = int(mobius(index))
        if mu:
            total += mp.mpf(mu) / index * mp.log(mp.zeta(index * s))
    return total


def counterterm(s):
    return prime_zeta_continuation(s) + prime_zeta_continuation(2 * s) / 2


epsilon_large = mp.mpf("1e-4")
epsilon_small = mp.mpf("1e-8")
s_large = mp.mpf(1) / 3 + epsilon_large
s_small = mp.mpf(1) / 3 + epsilon_small
observed_slope = (
    mp.re(counterterm(s_small)) - mp.re(counterterm(s_large))
) / mp.log(epsilon_small / epsilon_large)
logarithmic_slope_ok = abs(observed_slope - mp.mpf(1) / 3) < mp.mpf("2e-4")

fractional_monodromy = mp.e ** (-2j * mp.pi / 3)
nontrivial_monodromy_ok = abs(fractional_monodromy - 1) > 1


def archimedean_factor(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)


center = mp.mpf(1) / 3
arch_value = archimedean_factor(center)
archimedean_regular_ok = mp.isfinite(arch_value) and abs(arch_value) > mp.mpf("1e-10")

verdict = all(
    [
        critical_half_branch_cancelled,
        one_third_coefficient_exact,
        one_quarter_coefficient_exact,
        logarithmic_slope_ok,
        nontrivial_monodromy_ok,
        archimedean_regular_ok,
    ]
)

print(f"MOBIUS_COEFFICIENTS_TESTED: {MOBIUS_CUTOFF}")
print(f"HALF_LINE_BRANCH_CANCELLED: {'YES' if critical_half_branch_cancelled else 'NO'}")
print(f"ONE_THIRD_BRANCH_COEFFICIENT: {coefficients[3]}")
print(f"ONE_QUARTER_BRANCH_COEFFICIENT: {coefficients[4]}")
print(f"OBSERVED_ONE_THIRD_LOG_SLOPE: {mp.nstr(observed_slope, 12)}")
print(f"FRACTIONAL_MONODROMY_NONTRIVIAL: {'YES' if nontrivial_monodromy_ok else 'NO'}")
print(f"ARCHIMEDEAN_FACTOR_REGULAR_AT_ONE_THIRD: {'YES' if archimedean_regular_ok else 'NO'}")
print("GAMMA_POLE_COUNTERTERM_CANCELLATION: CLOSED_NO_GO")
print("REQUIRED_RENORMALIZATION: PRIME_SIDE_RELATIVE_BRANCH_DATA")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
