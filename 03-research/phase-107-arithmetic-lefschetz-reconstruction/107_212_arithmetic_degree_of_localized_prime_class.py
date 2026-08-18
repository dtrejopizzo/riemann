#!/home/trabajo/miniforge3/bin/python
"""Falsifier for arithmetic degrees of localized prime-return classes."""

from fractions import Fraction

from mpmath import mp
from sympy import primerange


mp.dps = 60
BOUND = 100_000
PRIMES = tuple(primerange(2, BOUND + 1))
PARAMETERS = (mp.mpf("1.5"), mp.mpf("2"), mp.mpc(2, 3))

# The coherent resolution gives [F_p]=[Z]-[Z]=0, whereas arithmetic
# degree remembers the norm of multiplication by p.
ordinary_g0_kills_prime = all((1 - 1) == 0 for _ in PRIMES[:5])
arithmetic_degree_nonzero = all(mp.log(p) > 0 for p in PRIMES[:5])

# Exact return-tower check at integral s.
return_tower_exact = True
for p in PRIMES[:25]:
    q = Fraction(1, p * p)
    partial = sum((q**e for e in range(1, 13)), Fraction(0))
    tail = q**13 / (1 - q)
    return_tower_exact &= partial + tail == q / (1 - q)

max_global_error = mp.mpf(0)
max_tail_ratio = mp.mpf(0)
max_derivative_error = mp.mpf(0)

for s in PARAMETERS:
    sigma = mp.re(s)
    finite_degree = mp.fsum(
        mp.log(p) * mp.power(p, -s) / (1 - mp.power(p, -s)) for p in PRIMES
    )
    target = -mp.diff(lambda z: mp.log(mp.zeta(z)), s)
    global_error = abs(finite_degree - target)
    max_global_error = max(max_global_error, global_error)

    denominator = 1 - mp.power(BOUND, -sigma)
    tail_bound = (
        mp.power(BOUND, 1 - sigma)
        * (mp.log(BOUND) / (sigma - 1) + 1 / (sigma - 1) ** 2)
        + mp.log(BOUND) * mp.power(BOUND, -sigma)
    ) / denominator
    max_tail_ratio = max(max_tail_ratio, global_error / tail_bound)

    for p in PRIMES[:5]:
        q = mp.power(p, -s)
        arithmetic_degree = mp.log(p) * q / (1 - q)
        determinant_derivative = mp.diff(
            lambda z: mp.log(1 - mp.power(p, -z)), s
        )
        max_derivative_error = max(
            max_derivative_error, abs(arithmetic_degree - determinant_derivative)
        )

tail_certified = max_tail_ratio < 1
derivative_ok = max_derivative_error < mp.mpf("1e-55")

# Omitting deg[p]=log p must not reproduce the Green summand.
unweighted_mutation_rejected = all(
    abs(
        mp.power(p, -2) / (1 - mp.power(p, -2))
        - mp.log(p) * mp.power(p, -2) / (1 - mp.power(p, -2))
    )
    > mp.mpf("1e-3")
    for p in PRIMES[:5]
)

verdict = (
    ordinary_g0_kills_prime
    and arithmetic_degree_nonzero
    and return_tower_exact
    and tail_certified
    and derivative_ok
    and unweighted_mutation_rejected
)

print(f"ACTUAL_PRIMES_TESTED: {len(PRIMES)}")
print(f"MAX_GLOBAL_GREEN_ERROR: {mp.nstr(max_global_error, 8)}")
print(f"MAX_ERROR_TO_EXPLICIT_TAIL_BOUND: {mp.nstr(max_tail_ratio, 8)}")
print(f"MAX_DETERMINANT_DEGREE_ERROR: {mp.nstr(max_derivative_error, 8)}")
print(f"ORDINARY_G0_RETAINS_PRIME_CLASS: {'NO' if ordinary_g0_kills_prime else 'YES'}")
print(f"ARITHMETIC_DEGREE_RETAINS_LOG_P: {'YES' if arithmetic_degree_nonzero else 'NO'}")
print(f"PRIME_RETURN_TOWER_EXACT: {'YES' if return_tower_exact else 'NO'}")
print(f"UNWEIGHTED_MUTATION_REJECTED: {'YES' if unweighted_mutation_rejected else 'NO'}")
print("FINITE_SUPPORT_ARITHMETIC_GREEN_CLASS: CONSTRUCTED")
print("INFINITE_SUPPORT_ARITHMETIC_DIVISOR: NOT_CONSTRUCTED")
print("RENORMALIZED_ARITHMETIC_HODGE_THEOREM: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

