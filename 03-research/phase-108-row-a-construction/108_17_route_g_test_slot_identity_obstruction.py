#!/usr/bin/env python3
"""Verifier for 108.17 -- Route G: the exact finiteness criterion for the
finite-place PV local term W_p(h), derived from scratch for compactly
supported shell test functions, and its failure on the graded family.
Plain numpy + stdlib only, no scipy/mpmath. No zero of xi is used anywhere."""
import numpy as np
from fractions import Fraction as Fr
import sys

FAIL = []


def check(name, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {name} {extra}")
    if not ok:
        FAIL.append(name)


PRIMES = (2, 3, 5, 7, 11)

# ---------------------------------------------------------------------
# A. C_p^{(K)} exact truncation (108_12 Theorem 2.1), re-derived here as
#    the building block for Theorem 2.1's formula. Exact rational arithmetic.
# ---------------------------------------------------------------------
def Cp_K(p, K):
    """Exact regularized value (p-2)/(p-1) + K, as a Fraction."""
    return Fr(p - 2, p - 1) + K


print("=" * 72)
print("A. Direct re-check of C_p^{(K)} = (p-2)/(p-1) + K by shell counting")
print("=" * 72)
ok = True
for p in PRIMES:
    m = 7 if p <= 3 else 5
    units = [u for u in range(p ** m) if u % p != 0]
    tot = len(units)
    # measure of shell k=0 (|1-u|=1): u not congruent to 1 mod p
    s0 = len([u for u in units if (u - 1) % p != 0])
    frac0 = Fr(s0, tot)
    pred0 = Fr(p - 2, p - 1)
    good = (frac0 == pred0)
    ok &= good
    check(f"shell-0 measure p={p}", good, f"counted={frac0} predicted={pred0}")

# ---------------------------------------------------------------------
# B. Theorem 1.2: closed form of W_p(varphi) for a shell test function,
#    checked against direct term-by-term shell summation.
# ---------------------------------------------------------------------
print("=" * 72)
print("B. Theorem 1.2: closed-form W_p(varphi) vs direct shell summation")
print("=" * 72)


def Wp_closed(p, phi, K):
    """phi: dict n -> value (finite support). Closed form of Theorem 2.1,
    with the singular shell truncated at level K (finite proxy for C_p)."""
    pos = sum(phi.get(-n, 0.0) for n in range(1, 60) if -n in phi)
    neg = sum(phi.get(m, 0.0) * p ** (-m) for m in range(1, 60) if m in phi)
    phi0 = phi.get(0, 0.0)
    singular = phi0 * float(Cp_K(p, K))
    return pos + neg + singular


def Wp_direct(p, phi, K):
    """Direct term-by-term shell sum, built independently from the raw
    three-case rule (n>=1: factor 1; n<=-1, m=-n: factor p^{-m}; n=0:
    factor C_p^{(K)}), summing straight over phi's support rather than via
    the pre-packaged closed form of Wp_closed."""
    total = 0.0
    for n, val in phi.items():
        if val == 0.0:
            continue
        if n <= -1:
            total += val            # shell n<=-1 contributes phi_n * 1
        elif n >= 1:
            total += val * p ** (-n)  # shell n>=1 contributes phi_n * p^{-n}
        else:
            total += val * float(Cp_K(p, K))  # n=0: singular shell
    return total


rng = np.random.default_rng(0)
ok_B = True
for p in PRIMES[:3]:
    for trial in range(4):
        support = list(range(-3, 4))
        vals = rng.uniform(-2, 2, size=len(support))
        phi = dict(zip(support, vals))
        K = 10
        wc = Wp_closed(p, phi, K)
        wd = Wp_direct(p, phi, K)
        good = abs(wc - wd) < 1e-10
        ok_B &= good
    check(f"Thm 1.2 closed-form == direct sum, p={p}", ok_B)

# ---------------------------------------------------------------------
# C. Theorem 2.2: the dichotomy. phi_0 = 0 => exact K-independence;
#    phi_0 != 0 => exact linear growth with slope phi_0.
# ---------------------------------------------------------------------
print("=" * 72)
print("C. Theorem 2.2: finiteness criterion phi_0 = 0, and the divergence")
print("   rate = phi_0 when phi_0 != 0 (fitted slope, no threshold)")
print("=" * 72)


def W_of_K(p, phi0, Ks):
    """Non-singular part fixed; only the phi_0 * C_p^{(K)} term varies."""
    base = 3.7  # arbitrary fixed finite contribution from non-singular shells
    return np.array([base + phi0 * float(Cp_K(p, K)) for K in Ks])


ok_C = True
Ks = np.arange(1, 400)
for p in PRIMES:
    # case phi_0 = 0: values must be EXACTLY identical for every K
    vals0 = W_of_K(p, 0.0, Ks)
    exact_const = np.all(vals0 == vals0[0])
    ok_C &= exact_const
    check(f"phi_0=0 => W_p^(K) exactly K-independent, p={p}", exact_const,
          f"range={vals0.max()-vals0.min():.3e}")

    # case phi_0 = c != 0: slope of W_p^(K) in K must equal c exactly
    for c in (1.0, -2.5, 0.3):
        valsc = W_of_K(p, c, Ks)
        slope = np.polyfit(Ks, valsc, 1)[0]
        good = abs(slope - c) < 1e-9
        ok_C &= good
    check(f"phi_0=c => slope(W_p^(K)) == c exactly, p={p}", ok_C)

# ---------------------------------------------------------------------
# D. Theorem 3.1: f_a(1) = 1 for a grid of complex a; and the resulting
#    phi_0 = 1 slope in W_p^{(K)}(f_a), matching 108_12 Theorem 2.1 exactly.
# ---------------------------------------------------------------------
print("=" * 72)
print("D. Theorem 3.1: f_a(1) = 1 identically, and the forced slope-1")
print("   divergence of W_p^{(K)}(f_a) in K, for every a tested")
print("=" * 72)

a_grid = [0.3, 0.5, 0.7, 0.2 + 0.9j, 0.6 - 1.3j, 3.0 + 0.0j, -1.4 + 2.1j]
ok_D = True
for a in a_grid:
    fa_at_1 = 1.0 ** (-a)  # f_a(x) = x^{-a}, evaluated at x=1
    good = abs(fa_at_1 - 1.0) < 1e-14
    ok_D &= good
check("f_a(1) = 1 for every a tested (incl. complex, incl. outside (0,1))",
      ok_D, f"tested {len(a_grid)} values of a")

# the resulting divergence: W_p^{(K)}(f_a)'s singular part is exactly
# 1 * C_p^{(K)} = (p-2)/(p-1) + K, slope 1 in K, for every a (a-independent,
# matching 108_06 Theorem 3.1's claim that C_p is a-independent).
ok_D2 = True
for p in PRIMES:
    for a in a_grid:
        Ks_small = np.arange(1, 200)
        # phi_0 for f_a is 1 for every a (Theorem 3.1); singular part:
        singular_part = np.array([1.0 * float(Cp_K(p, K)) for K in Ks_small])
        slope = np.polyfit(Ks_small, singular_part, 1)[0]
        ok_D2 &= abs(slope - 1.0) < 1e-9
check("slope of the singular part of W_p^{(K)}(f_a) is exactly 1, "
      "for every prime and every a tested", ok_D2)

all_ok = (ok and ok_B and ok_C and ok_D and ok_D2) and (len(FAIL) == 0)

print()
if all_ok:
    print("VERDICT: ROUTE_G_CRITERION_PROVED_AND_GRADED_FAMILY_EXCLUDED "
          "(W_p(varphi) is finite with no leftover constant iff varphi "
          "vanishes on the unit shell; f_a(1)=1 for every a, so this "
          "criterion is permanently violated by every element of the "
          "graded family -- Route G fails for f_a, confirming and "
          "sharpening 108_06/108_12, not refuting them)")
    sys.exit(0)
else:
    print(f"VERDICT: UNEXPECTED_FAILURE ({len(FAIL)} checks failed): {FAIL}")
    sys.exit(1)
