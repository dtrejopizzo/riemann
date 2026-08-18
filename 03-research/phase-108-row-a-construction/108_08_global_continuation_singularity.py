#!/usr/bin/env python3
"""
108_08 verifier: analytic continuation of the two global halves A(a), B(a)
-- the singularities at a=1/N (N>=2) and a=1-1/M (M>=2) do NOT cancel at
their one common point a=1/2; they reinforce.

Plain python3 + numpy only (no scipy, no mpmath). zeta(s) for real s>0,
s != 1, is implemented via Euler-Maclaurin summation.
"""

import cmath
import math
import numpy as np


# ----------------------------------------------------------------------
# zeta(s) for real s > 0, s != 1, via Euler-Maclaurin summation
# ----------------------------------------------------------------------

def zeta(s, N=100):
    """Euler-Maclaurin approximation to the Riemann zeta function,
    valid (and increasingly accurate) for real or complex s with s != 1.
    """
    n = np.arange(1, N, dtype=np.complex128)
    total = np.sum(n ** (-s))
    total += (N ** (1.0 - s)) / (s - 1.0)
    total += 0.5 * N ** (-s)
    total += -(s / 12.0) * N ** (-s - 1.0)
    total += (s * (s + 1.0) * (s + 2.0) / 720.0) * N ** (-s - 3.0)
    return total


def check_zeta_implementation():
    print("=== zeta() implementation sanity check ===")
    ok = True
    tests = [(2.0, math.pi ** 2 / 6.0), (4.0, math.pi ** 4 / 90.0), (6.0, math.pi ** 6 / 945.0)]
    for s, exact in tests:
        val = zeta(s).real
        err = abs(val - exact) / abs(exact)
        good = err < 1e-6
        ok = ok and good
        print(f"  zeta({s}) = {val:.12f}, exact = {exact:.12f}, err={err:.2e}  {'OK' if good else 'FAIL'}")
    return ok


def check_no_real_zeros():
    print("=== Lemma 3.1: zeta(s) has no real zero for s>0; sign pattern ===")
    ok = True
    for s in [0.1, 0.3, 0.5, 0.7, 0.9]:
        v = zeta(s).real
        good = v < 0
        ok = ok and good
        print(f"  zeta({s}) = {v:.6f} < 0 : {'OK' if good else 'FAIL'}")
    for s in [1.5, 2.0, 3.0, 5.0]:
        v = zeta(s).real
        good = v > 0
        ok = ok and good
        print(f"  zeta({s}) = {v:.6f} > 0 : {'OK' if good else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------
# totient
# ----------------------------------------------------------------------

def phi(n):
    result = n
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def sieve_primes(bound):
    is_p = np.ones(bound + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(bound ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i:: i] = False
    return np.nonzero(is_p)[0]


def A_direct(a, prime_bound=2_000_000):
    """Original definition: sum_p p^{-a}/(1-p^{-a}), Re a > 1, truncated."""
    primes = sieve_primes(prime_bound)
    x = primes.astype(np.float64) ** (-a)
    return np.sum(x / (1.0 - x))


def A_series(a, Ncut=60):
    """Reformulated series: sum_N (phi(N)/N) log zeta(N a)."""
    total = 0.0 + 0.0j
    for N in range(1, Ncut + 1):
        z = zeta(N * a)
        total += (phi(N) / N) * cmath.log(z)
    return total


def check_reformulation():
    print("=== Proposition 2.1: A(a) = sum_N (phi(N)/N) log zeta(N a) ===")
    a = 1.5
    direct = A_direct(a)
    series = A_series(a, Ncut=60).real
    err = abs(direct - series) / abs(direct)
    good = err < 1e-4
    print(f"  a={a}: A_direct (prime sum, truncated) = {direct:.8f}, "
          f"A_series (totient reformulation) = {series:.8f}, err={err:.2e}  {'OK' if good else 'FAIL'}")
    return good


def check_pole_law():
    print("=== Lemma 4.1: |zeta(w)|*|w-1| -> 1 as w -> 1 (from both sides) ===")
    ok = True
    for d in [0.1, 0.01, 0.001, 0.0001]:
        for w in [1.0 + d, 1.0 - d]:
            prod = abs(zeta(w)) * abs(w - 1.0)
            err = abs(prod - 1.0)
            good = err < 5.0 * d  # residue-1 law: error is O(w-1) itself
            ok = ok and good
            print(f"  w={w:.4f}: |zeta(w)|*|w-1| = {prod.real:.6f}, err={err:.2e}  {'OK' if good else 'FAIL'}")
    # explicit trend check: error should shrink as d shrinks
    prods = []
    for d in [0.1, 0.01, 0.001, 0.0001]:
        prods.append(abs(abs(zeta(1.0 + d)) * d - 1.0))
    shrinking = all(prods[i + 1] < prods[i] for i in range(len(prods) - 1))
    print(f"  error |.|-1 shrinks monotonically as w->1+: {'OK' if shrinking else 'FAIL'}")
    return ok and shrinking


# ----------------------------------------------------------------------
# the decisive check: reinforcement, not cancellation, at a=1/2
# ----------------------------------------------------------------------

def Re_A_plus_B(a, Ncut=60):
    """Re[A(a)+B(a)] = Re[A(a)] + Re[A(1-a)] via the totient series."""
    return A_series(a, Ncut).real + A_series(1.0 - a, Ncut).real


def check_reinforcement():
    print("=== Theorem 7.1: reinforcement (not cancellation) at a=1/2 ===")
    print("    predicted: Re[A(a)+B(a)] = -log|2a-1| + O(1)  ->  +infinity")
    print("    (a spurious cancellation would instead predict a bounded limit)")

    epss = [0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
    xs = []
    ys = []
    for eps in epss:
        a = 0.5 + eps
        val = Re_A_plus_B(a, Ncut=80)
        x = -math.log(2.0 * eps)
        xs.append(x)
        ys.append(val)
        print(f"  eps={eps:.4f}: Re[A+B](0.5+eps) = {val:.6f}, -log(2 eps) = {x:.6f}")

    xs = np.array(xs)
    ys = np.array(ys)
    slope, intercept = np.polyfit(xs, ys, 1)

    # divergence check: value must grow without bound as eps -> 0, i.e.
    # NOT converge to a finite limit (which is what cancellation would give)
    diverges = (ys[-1] - ys[0]) > 0.5 * (xs[-1] - xs[0])  # grows at least at half the
                                                            # predicted rate over the run
    slope_matches = abs(slope - 1.0) < 0.25  # theory: coefficient exactly 1

    good = diverges and slope_matches
    print(f"  fitted slope = {slope:.4f} (theory: 1.0, i.e. coefficient of -log|2a-1| is -1);"
          f" value grows (no cancellation): {diverges}  {'OK' if good else 'FAIL'}")
    return good


def check_no_interference_at_third():
    print("=== Corollary 7.2: B(a) stays bounded as a -> 1/3 (in Sigma_A, not Sigma_B) ===")
    # A(a) should blow up (singular at a=1/3), B(a)=A(1-a) should stay bounded
    # (1/3 is not of the form 1-1/M for integer M, Lemma 6.1)
    epss = [0.02, 0.01, 0.005, 0.002]
    A_vals = []
    B_vals = []
    for eps in epss:
        a = 1.0 / 3.0 + eps
        A_vals.append(A_series(a, Ncut=80).real)
        B_vals.append(A_series(1.0 - a, Ncut=80).real)
    A_diverges = A_vals[-1] > A_vals[0] + 1.0  # A grows substantially
    B_bounded = max(abs(v) for v in B_vals) < 20.0 and (max(B_vals) - min(B_vals)) < 1.0
    good = A_diverges and B_bounded
    print(f"  A(1/3+eps) over eps in {epss}: {['%.4f' % v for v in A_vals]}  (should grow)")
    print(f"  B(1/3+eps) over eps in {epss}: {['%.4f' % v for v in B_vals]}  (should stay ~constant)")
    print(f"  {'OK' if good else 'FAIL'}")
    return good


def main():
    r1 = check_zeta_implementation()
    r2 = check_no_real_zeros()
    r3 = check_reformulation()
    r4 = check_pole_law()
    r5 = check_reinforcement()
    r6 = check_no_interference_at_third()

    all_ok = r1 and r2 and r3 and r4 and r5 and r6
    print()
    if all_ok:
        print("VERDICT: PASS - the singularities of the two analytically continued halves "
              "A(a), B(a) do NOT cancel at a=1/2; they reinforce (Re[A+B] ~ -log|2a-1|), "
              "and the full singular set {1/N}u{1-1/M} accumulates at both strip endpoints.")
    else:
        print("VERDICT: FAIL - see failed checks above.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
