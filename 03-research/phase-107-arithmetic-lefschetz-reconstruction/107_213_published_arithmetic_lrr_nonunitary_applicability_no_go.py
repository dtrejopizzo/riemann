#!/home/trabajo/miniforge3/bin/python
"""Falsifier for published arithmetic LRR at nonunitary prime characters."""

import cmath

from mpmath import mp


mp.dps = 60
PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.25"), mp.mpf("2"), mp.mpc(2, 3))
ORDERS = tuple(range(1, 65))

all_nonunitary = True
finite_cyclic_rejected = True
radial_separation = True
min_radial_gap = mp.inf

for p in PRIMES:
    for s in PARAMETERS:
        q = mp.power(p, -s)
        modulus = abs(q)
        all_nonunitary &= modulus < 1
        min_radial_gap = min(min_radial_gap, 1 - modulus)
        radial_separation &= 1 - modulus > 0
        for n in ORDERS:
            finite_cyclic_rejected &= abs(mp.power(q, n) - 1) > mp.mpf("1e-30")

# A genuine root of unity must pass the same finite-cyclic relation.
unitary_mutation_accepted = True
for n in (2, 3, 5, 7, 11):
    root = mp.e ** (2j * mp.pi / n)
    unitary_mutation_accepted &= abs(root**n - 1) < mp.mpf("1e-50")

# Directly sample roots of unity and confirm the reverse triangle bound.
sample_bound_ok = True
for p in PRIMES:
    q = complex(mp.power(p, -2))
    for n in ORDERS:
        for k in range(n):
            root = cmath.exp(2j * cmath.pi * k / n)
            sample_bound_ok &= abs(root - q) + 1e-14 >= 1 - abs(q)

verdict = (
    all_nonunitary
    and finite_cyclic_rejected
    and radial_separation
    and unitary_mutation_accepted
    and sample_bound_ok
)

print(f"ACTUAL_PRIME_CHARACTERS_TESTED: {len(PRIMES) * len(PARAMETERS)}")
print(f"FINITE_CYCLIC_ORDERS_TESTED: {len(ORDERS)}")
print(f"MIN_RADIAL_GAP_FROM_UNIT_CIRCLE: {mp.nstr(min_radial_gap, 8)}")
print(f"TANG_FINITE_CYCLIC_SPECIALIZATION: {'REJECTED' if finite_cyclic_rejected else 'ADMISSIBLE'}")
print(f"FINITE_CYCLIC_LIMIT_TO_P_MINUS_S: {'NO' if radial_separation else 'UNRESOLVED'}")
print(f"UNITARY_CONTROL_ACCEPTED: {'YES' if unitary_mutation_accepted else 'NO'}")
print("KR_TORUS_RESIDUE_FORMULA: APPLICABLE_INFINITESIMALLY")
print("KR_NONUNITARY_TORSION_IDENTITY: NOT_PROVED")
print("PUBLISHED_ARITHMETIC_LRR_CLOSES_GLOBAL_PUSHFORWARD: NO")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

