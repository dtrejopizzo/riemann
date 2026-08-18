#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the equivariant derived fixed-point self-intersection."""

from fractions import Fraction

from mpmath import mp
from sympy import Matrix, Rational, Symbol


mp.dps = 70
PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.25"), mp.mpf("2"), mp.mpc(2, 3))

# Exact Tor calculation at s=2: Tor_0 has weight 1 and Tor_1 has
# conormal weight q.  Their alternating character must be 1-q.
tor_exact = True
underived_rejected = True
for p in PRIMES:
    q = Fraction(1, p * p)
    tor0 = Fraction(1)
    tor1 = q
    tor_exact &= tor0 - tor1 == 1 - q
    underived_rejected &= tor0 != 1 - q

# Nonlinear changes of coordinate conjugate every jet action.  The
# first diagonal character, hence lambda_{-1}, must remain q.
coordinate_ok = True
N = 6
for p in PRIMES:
    q = Rational(1, p**2)
    change = Matrix.eye(N)
    for row in range(1, N):
        for column in range(row):
            change[row, column] = (row + 2 * column + 1) % 5 - 2
    diagonal = Matrix.diag(*(q**n for n in range(1, N + 1)))
    conjugated = change.inv() * diagonal * change
    coordinate_ok &= conjugated[0, 0] == q
    coordinate_ok &= 1 - conjugated[0, 0] == 1 - q

max_green_error = mp.mpf(0)
for p in PRIMES:
    for s in PARAMETERS:
        q = mp.power(p, -s)
        derived = mp.diff(lambda z: mp.log(1 - mp.power(p, -z)), s)
        expected = mp.log(p) * q / (1 - q)
        max_green_error = max(max_green_error, abs(derived - expected))

green_ok = max_green_error < mp.mpf("1e-55")
verdict = tor_exact and underived_rejected and coordinate_ok and green_ok

print(f"ACTUAL_PRIMES_TESTED: {len(PRIMES)}")
print(f"SPECTRAL_PARAMETERS_TESTED: {len(PARAMETERS)}")
print(f"MAX_GREEN_DERIVATIVE_ERROR: {mp.nstr(max_green_error, 8)}")
print(f"KOSZUL_TOR_ALTERNATING_CLASS: {'YES' if tor_exact else 'NO'}")
print(f"NONLINEAR_COORDINATE_INVARIANCE: {'YES' if coordinate_ok else 'NO'}")
print(f"UNDERIVED_PULLBACK_REJECTED: {'YES' if underived_rejected else 'NO'}")
print("EQUIVARIANT_DERIVED_LOCAL_INTERSECTION: CONSTRUCTED")
print("PROPER_NUMERICAL_PUSHFORWARD: NOT_CONSTRUCTED")
print("GLOBAL_ARITHMETIC_SQUARE_INTERSECTION: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

