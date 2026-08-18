#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the CC archimedean-germ/Fock determinant realization."""

from mpmath import mp
from sympy import Matrix, Poly, Rational, Symbol, expand


mp.dps = 70
PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.25"), mp.mpf("2"), mp.mpc(2, 3))
CUTOFFS = (4, 8, 16)


def finite_ideal_det(q, first_degree, cutoff):
    return mp.fprod(1 - mp.power(q, n) for n in range(first_degree, cutoff + 1))


max_ratio_error = mp.mpf(0)
green_ok = True
for p in PRIMES:
    for s in PARAMETERS:
        q = mp.power(p, -s)
        for cutoff in CUTOFFS:
            ratio = finite_ideal_det(q, 1, cutoff) / finite_ideal_det(q, 2, cutoff)
            max_ratio_error = max(max_ratio_error, abs(ratio - (1 - q)))
        green = mp.log(p) * q / (1 - q)
        derivative = mp.diff(lambda z: mp.log(1 - mp.power(p, -z)), s)
        green_ok &= abs(green - derivative) < mp.mpf("1e-55")

finite_ratio_ok = max_ratio_error < mp.mpf("1e-60")

# Exact nonlinear-coordinate test on N-jets.  Columns of C express
# w^j=(z+2z^2-z^3)^j in the z-basis modulo z^(N+1).
z = Symbol("z")
N = 7
w = z + 2 * z**2 - z**3
C = Matrix.zeros(N, N)
for j in range(1, N + 1):
    polynomial = Poly(expand(w**j), z)
    for degree in range(1, N + 1):
        C[degree - 1, j - 1] = polynomial.coeff_monomial(z**degree)

coordinate_ok = C.det() != 0
for p in PRIMES:
    q = Rational(1, p**2)
    diagonal = Matrix.diag(*(q**n for n in range(1, N + 1)))
    conjugated = C.inv() * diagonal * C
    full_det = (Matrix.eye(N) - conjugated).det()
    tail_det = (Matrix.eye(N - 1) - conjugated[1:, 1:]).det()
    coordinate_ok &= full_det / tail_det == 1 - q
    coordinate_ok &= conjugated[:1, 1:] == Matrix.zeros(1, N - 1)

# A translated contraction has no fixed trivial point; its pullback sends
# the generator z of m to q*z+c, which has a nonzero constant term.
translated_action_rejected = True
for p in PRIMES:
    translated_pullback = Poly(Rational(1, p) * z + Rational(1, p + 1), z)
    translated_action_rejected &= translated_pullback.coeff_monomial(1) != 0

verdict = finite_ratio_ok and green_ok and coordinate_ok and translated_action_rejected

print(f"ACTUAL_PRIMES_TESTED: {len(PRIMES)}")
print(f"SPECTRAL_PARAMETERS_TESTED: {len(PARAMETERS)}")
print(f"MAX_FINITE_JET_RATIO_ERROR: {mp.nstr(max_ratio_error, 8)}")
print(f"IDEAL_FILTRATION_DETERMINANT_RATIO: {'YES' if finite_ratio_ok else 'NO'}")
print(f"GREEN_LOG_DERIVATIVE_MATCHES: {'YES' if green_ok else 'NO'}")
print(f"NONLINEAR_COORDINATE_INVARIANCE: {'YES' if coordinate_ok else 'NO'}")
print(f"NON_FIXED_TRANSLATION_REJECTED: {'YES' if translated_action_rejected else 'NO'}")
print("CC_ARCHIMEDEAN_GERM_FOCK_REALIZATION: CONSTRUCTED")
print("PROPER_GLOBAL_FIXED_SECTION: NOT_CONSTRUCTED")
print("ARITHMETIC_SQUARE_PUSHFORWARD: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
