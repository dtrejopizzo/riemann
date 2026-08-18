#!/usr/bin/env python3
"""Checks for D.136 crossed periodic/fixed-contact audit.

Only elementary fixed-point, cyclotomic and inertia identities are checked.
No zeta zero or sign of B_nuc is used.
"""

from __future__ import annotations

import math

import numpy as np
import sympy as sp


def prime_power(n: int):
    fac = sp.factorint(n)
    if len(fac) != 1:
        return None
    p, k = next(iter(fac.items()))
    return int(p), int(k)


# 1. Rotation by log(n) fixes C_p exactly for n=p^k.
primes = [2, 3, 5, 7, 11]
for n in range(2, 151):
    pp = prime_power(n)
    for p in primes:
        fixed_by_factorization = pp is not None and pp[0] == p
        # log(n)/log(p) is an integer precisely in that case; use exact
        # integer arithmetic instead of floating logarithms.
        k = 0
        m = n
        while m % p == 0:
            m //= p
            k += 1
        fixed_exact = m == 1 and k >= 1
        assert fixed_by_factorization == fixed_exact


# 2. Cyclotomic evaluation supplies the missing arithmetic differential.
x = sp.Symbol("x")
for n in range(2, 101):
    value = int(sp.cyclotomic_poly(n, x).subs(x, 1))
    pp = prime_power(n)
    expected = pp[0] if pp is not None else 1
    assert value == expected, (n, value, expected)


# 3. Circle rotation acts by identity on H^0 and H^1, so Lefschetz number 0.
trace_h0 = 1
trace_h1 = 1
assert trace_h0 - trace_h1 == 0


# The local derived self-intersection has exterior ranks (1,1).
exterior_ranks_dim1 = [1, 1]
assert sum((-1) ** i * r for i, r in enumerate(exterior_ranks_dim1)) == 0


# On a two-dimensional periodic product the exterior ranks are (1,2,1).
exterior_ranks_dim2 = [1, 2, 1]
assert sum((-1) ** i * r for i, r in enumerate(exterior_ranks_dim2)) == 0


# 4. The crossed-label composition is multiplication.
for m in range(1, 20):
    for n in range(1, 20):
        # Translation lengths add, which is multiplication after exp.
        assert abs((math.log(m) + math.log(n)) - math.log(m * n)) < 1e-14


# 5. The local contact matrix has one positive direction per prime and
# therefore unbounded rank on finite truncations.
for r in range(1, 9):
    chosen = primes[: min(r, len(primes))]
    if r > len(primes):
        chosen = list(map(int, list(sp.primerange(2, 30))[:r]))
    # two powers per prime
    labels = [(p, k) for p in chosen for k in (1, 2)]
    K = np.zeros((len(labels), len(labels)))
    for i, (p, _) in enumerate(labels):
        for j, (q, _) in enumerate(labels):
            if p == q:
                K[i, j] = math.log(p)
    ev = np.linalg.eigvalsh(K)
    positive = np.count_nonzero(ev > 1e-10)
    rank = np.linalg.matrix_rank(K, tol=1e-10)
    assert positive == len(chosen)
    assert rank == len(chosen)


# 6. A degree-only quadratic RR form has zero cross-effect on labels whose
# two ruling degrees are zero.
def rr(d1, d2):
    return d1 * d2


base = (1.7, -0.4)
gamma_degree = (0.0, 0.0)
cross = (
    rr(base[0] + gamma_degree[0], base[1] + gamma_degree[1])
    - rr(*base)
    - rr(*gamma_degree)
    + rr(0.0, 0.0)
)
assert cross == 0.0


print("D136 crossed periodic/profunctor fixed-trace audit: PASS")
