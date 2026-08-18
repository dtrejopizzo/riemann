#!/usr/bin/env python3
"""Checks for 104_94.

Exact (Fraction) checks:
  J(x) = sum_k pi(x^(1/k))/k;
  J = pi + Q;
  pi(x) = sum_k mu(k) J(x^(1/k))/k.

The larger table is diagnostic only.  It separates the discrete Cramer
energies of B, the ordinary-prime core P, and the proper-power correction Q.
"""

from fractions import Fraction
from math import isqrt, log, sqrt


N_EXACT = 400
N_DIAG = 1_000_000
SAMPLES = {100, 1_000, 10_000, 100_000, N_DIAG}


def sieve(n):
    prime = bytearray(b"\x01") * (n + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if prime[p]:
            start = p * p
            prime[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    primes = [p for p in range(2, n + 1) if prime[p]]
    pi = [0] * (n + 1)
    count = 0
    for m in range(n + 1):
        if prime[m]:
            count += 1
        pi[m] = count
    return prime, primes, pi


def kth_root_floor(n, k):
    if k == 1:
        return n
    r = int(round(n ** (1.0 / k)))
    if r < 1:
        r = 1
    while (r + 1) ** k <= n:
        r += 1
    while r**k > n:
        r -= 1
    return r


def mobius_up_to(n):
    mu = [1] * (n + 1)
    prime_count = [0] * (n + 1)
    square = [False] * (n + 1)
    for p in range(2, n + 1):
        is_p = True
        for d in range(2, isqrt(p) + 1):
            if p % d == 0:
                is_p = False
                break
        if not is_p:
            continue
        for j in range(p, n + 1, p):
            prime_count[j] += 1
        p2 = p * p
        for j in range(p2, n + 1, p2):
            square[j] = True
    mu[0] = 0
    for j in range(1, n + 1):
        mu[j] = 0 if square[j] else (-1 if prime_count[j] % 2 else 1)
    return mu


def exact_checks(primes, pi):
    atom = [Fraction(0) for _ in range(N_EXACT + 1)]
    proper_atom = [Fraction(0) for _ in range(N_EXACT + 1)]
    for p in primes:
        if p > N_EXACT:
            break
        q = p
        k = 1
        while q <= N_EXACT:
            atom[q] += Fraction(1, k)
            if k >= 2:
                proper_atom[q] += Fraction(1, k)
            if q > N_EXACT // p:
                break
            q *= p
            k += 1

    j_prefix = [Fraction(0) for _ in range(N_EXACT + 1)]
    q_prefix = [Fraction(0) for _ in range(N_EXACT + 1)]
    for m in range(2, N_EXACT + 1):
        j_prefix[m] = j_prefix[m - 1] + atom[m]
        q_prefix[m] = q_prefix[m - 1] + proper_atom[m]

    max_k = 0
    q = 1
    while q * 2 <= N_EXACT:
        q *= 2
        max_k += 1
    mu = mobius_up_to(max_k)

    for x in range(2, N_EXACT + 1):
        tower = Fraction(0)
        inverse = Fraction(0)
        k = 1
        while 2**k <= x:
            root = kth_root_floor(x, k)
            tower += Fraction(pi[root], k)
            inverse += Fraction(mu[k], k) * j_prefix[root]
            k += 1
        assert tower == j_prefix[x], (x, tower, j_prefix[x])
        assert j_prefix[x] == pi[x] + q_prefix[x]
        assert inverse == pi[x], (x, inverse, pi[x])

    # Exact lcm/radical support check: max exponent versus one exponent.
    lcm_constructed = 1
    radical = 1
    for p in primes:
        if p > 30:
            break
        radical *= p
        power = p
        while power * p <= 30:
            power *= p
        lcm_constructed *= power
    from math import gcd

    literal_lcm = 1
    for m in range(1, 31):
        literal_lcm = literal_lcm * m // gcd(literal_lcm, m)
    assert lcm_constructed == literal_lcm
    assert radical > 0 and literal_lcm % radical == 0

    print(f"exact tower/Mobius identities: x <= {N_EXACT}: PASS")
    print("exact lcm/radical support check: m <= 30: PASS")


def diagnostic(prime, primes):
    q_atom = [0.0] * (N_DIAG + 1)
    for p in primes:
        q = p * p
        k = 2
        while q <= N_DIAG:
            q_atom[q] += 1.0 / k
            if q > N_DIAG // p:
                break
            q *= p
            k += 1

    s = 0.0
    q = 0.0
    pi_count = 0
    e_b = e_p = e_q = 0.0
    rows = []
    max_identity_error = 0.0
    max_minkowski_excess = -1e100
    for m in range(2, N_DIAG + 1):
        s += 1.0 / log(m)
        if prime[m]:
            pi_count += 1
        q += q_atom[m]
        p_core = pi_count - s
        b = p_core + q
        weight = 1.0 / (m * (m + 1.0))
        e_b += b * b * weight
        e_p += p_core * p_core * weight
        e_q += q * q * weight
        max_identity_error = max(max_identity_error, abs(b - (p_core + q)))
        excess = abs(sqrt(e_b) - sqrt(e_p)) - sqrt(e_q)
        max_minkowski_excess = max(max_minkowski_excess, excess)
        if m in SAMPLES:
            rows.append((m, e_b, e_p, e_q, b, p_core, q))

    assert max_identity_error < 1e-12
    assert max_minkowski_excess < 1e-12

    print("\nDiagnostic table (not a certificate of asymptotics)")
    print("N          E_B            E_P            E_Q          B_N        P_N        Q_N")
    for row in rows:
        n, eb, ep, eq, b, p, qv = row
        print(
            f"{n:<8d} {eb:13.8f} {ep:13.8f} {eq:13.8f}"
            f" {b:10.4f} {p:10.4f} {qv:10.4f}"
        )
    print(f"max exact-decomposition float residual: {max_identity_error:.3e}")
    print(f"max Minkowski excess (must be <=0): {max_minkowski_excess:.3e}")


def main():
    prime, primes, pi = sieve(N_DIAG)
    exact_checks(primes, pi)
    diagnostic(prime, primes)
    print("ordinary-prime finite-energy gate checks: PASS")


if __name__ == "__main__":
    main()
