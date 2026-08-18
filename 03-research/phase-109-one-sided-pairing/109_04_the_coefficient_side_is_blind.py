#!/usr/bin/env python3
"""Verifier for 109.04 -- the coefficient side is blind, for every kernel.

Checks Theorem 1.1 (blindness for ANY kernel supported on prime powers),
Theorem 1.2 (the witness sin(pi x) and its Mellin transform), Corollary 1.3.

Discipline: every check that has a "correct value" tests the VALUE and
carries a control clause that would reject a plausible wrong answer.
Theorem 1.1 is tested on RANDOM NON-DIAGONAL kernels, precisely because the
claim is that the diagonal choice of 109_01 is irrelevant.
"""
import random
import sys

import mpmath as mp

mp.mp.dps = 30

PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print("[%s] %s  %s" % ("PASS" if ok else "FAIL", name, detail))


def prime_powers(limit):
    out, sieve = [], [True] * (limit + 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            for m in range(p * p, limit + 1, p):
                sieve[m] = False
            q = p
            while q <= limit:
                out.append(q)
                q *= p
    return sorted(out)


F = lambda x: mp.sin(mp.pi * x)
Fhat = lambda s: mp.pi ** (-s) * mp.gamma(s) * mp.sin(mp.pi * s / 2)

print("=" * 70)
print("Theorem 1.2 -- the witness lies in Z (vanishes at every prime power)")
print("=" * 70)
pps = prime_powers(200)[:10]
vals = [abs(F(mp.mpf(n))) for n in pps]
check("sin(pi n) = 0 at ten prime powers %s" % pps,
      max(vals) < mp.mpf('5e-30'), "max |sin(pi n)| = %s" % mp.nstr(max(vals), 4))
# control: the same test must NOT pass at a non-integer
ctrl = abs(F(mp.mpf('2.5')))
check("control: the test is discriminating (sin(pi*2.5) is not 0)",
      ctrl > mp.mpf('0.9'), "|sin(2.5 pi)| = %s" % mp.nstr(ctrl, 6))
check("the witness is nonzero as a function", abs(F(mp.mpf('0.5'))) > mp.mpf('0.9'))

print()
print("=" * 70)
print("Theorem 1.2 -- Fhat does not vanish at any zero of xi")
print("=" * 70)
mags = []
for k in range(1, 7):
    rho = mp.zetazero(k)
    v = abs(Fhat(rho))
    mags.append(v)
    print("    rho_%d = %s   |Fhat(rho)| = %s"
          % (k, mp.nstr(rho, 14), mp.nstr(v, 10)))
check("Fhat(rho) != 0 at the first six zeros of xi",
      min(mags) > mp.mpf('0.5'), "min |Fhat| = %s" % mp.nstr(min(mags), 8))
# control: a transform that DOES vanish somewhere must be detected as such.
# sin(pi s / 2) vanishes at s = 2; confirm the same machinery sees a zero.
check("control: the same machinery detects a genuine zero (Fhat at s=2)",
      abs(Fhat(mp.mpf(2))) < mp.mpf('1e-20'),
      "|Fhat(2)| = %s" % mp.nstr(abs(Fhat(mp.mpf(2))), 4))

# The constant 1/sqrt(2) is EXACT on the critical line, not asymptotic:
#   |Fhat|^2 = pi^-1 * |Gamma(1/2+it)|^2 * |sin(pi/4 + i pi t/2)|^2
#            = pi^-1 * (pi/cosh(pi t)) * (1/2 + sinh^2(pi t/2)) = 1/2,
# using cosh(pi t) = 1 + 2 sinh^2(pi t / 2).  Test the identity at fixed
# precision across a wide range of t; residuals must stay at round-off.
target = 1 / mp.sqrt(2)
ts = [mp.mpf(t) for t in ('0.5', 3, 10, 40, 160, 640)]
errs = [abs(abs(Fhat(mp.mpc('0.5', t))) - target) for t in ts]
check("|Fhat(1/2+it)| = 1/sqrt(2) EXACTLY on the critical line",
      max(errs) < mp.mpf('1e-25'),
      "max residual over t in [0.5,640] = %s" % mp.nstr(max(errs), 4))
# Verify the trig identity the proof rests on, independently.  Use RELATIVE
# error: cosh(pi t) reaches e^2010 at t=640, so an absolute difference of two
# such numbers is pure round-off (catastrophic cancellation), not a defect.
tid = max(abs(mp.cosh(mp.pi * t) - (1 + 2 * mp.sinh(mp.pi * t / 2) ** 2))
          / mp.cosh(mp.pi * t) for t in ts)
check("control: cosh(pi t) = 1 + 2 sinh^2(pi t/2) (relative error)",
      tid < mp.mpf('1e-25'), "max relative defect = %s" % mp.nstr(tid, 4))
# control: the value is 1/sqrt(2), NOT 1 or 1/2 -- a discriminating clause
v = abs(Fhat(mp.mpc('0.5', 7)))
check("control: the value is 1/sqrt(2), not 1 and not 1/2",
      abs(v - target) < mp.mpf('1e-25') and abs(v - 1) > mp.mpf('0.2')
      and abs(v - mp.mpf('0.5')) > mp.mpf('0.2'), "value = %s" % mp.nstr(v, 14))

print()
print("=" * 70)
print("Theorem 1.1 -- blindness for RANDOM NON-DIAGONAL kernels")
print("=" * 70)
random.seed(20260803)
支 = prime_powers(120)
n_kernels, worst = 40, mp.mpf(0)
for trial in range(n_kernels):
    # random kernel supported on prime powers, deliberately NOT diagonal
    K = {(a, b): mp.mpf(random.uniform(-5, 5))
         for a in 支 for b in 支}
    offdiag = sum(1 for (a, b), v in K.items() if a != b and v != 0)
    # random g, arbitrary values
    g = {n: mp.mpf(random.uniform(-9, 9)) for n in 支}
    # f = the witness, restricted to the support: identically 0 there
    f = {n: F(mp.mpf(n)) for n in 支}
    B = sum(K[(a, b)] * f[a] * g[b] for a in 支 for b in 支)
    worst = max(worst, abs(B))
    if trial == 0:
        print("    kernel 0: %d off-diagonal nonzero entries, support size %d"
              % (offdiag, len(支)))
check("B_K(F, g) = 0 for %d random non-diagonal kernels" % n_kernels,
      worst < mp.mpf('1e-25'), "max |B_K(F,g)| = %s" % mp.nstr(worst, 4))

# control: the SAME kernels must give nonzero on a function NOT in Z,
# otherwise the check above would be vacuous (e.g. if K or g were zero).
random.seed(20260803)
nonzero_seen = 0
for trial in range(n_kernels):
    K = {(a, b): mp.mpf(random.uniform(-5, 5)) for a in 支 for b in 支}
    g = {n: mp.mpf(random.uniform(-9, 9)) for n in 支}
    h = {n: mp.mpf(1) for n in 支}          # h = 1, manifestly NOT in Z
    B = sum(K[(a, b)] * h[a] * g[b] for a in 支 for b in 支)
    if abs(B) > mp.mpf('1e-6'):
        nonzero_seen += 1
check("control: the same kernels give B_K != 0 on h=1 (test is not vacuous)",
      nonzero_seen == n_kernels,
      "%d/%d kernels gave a nonzero value" % (nonzero_seen, n_kernels))

print()
print("=" * 70)
print("Corollary 1.3 -- rad B_K is not inside the zero-determined space")
print("=" * 70)
check("F is in rad B_K (all kernels) but Fhat(rho) != 0 -> not contained",
      max(vals) < mp.mpf('5e-30') and min(mags) > mp.mpf('0.5')
      and worst < mp.mpf('1e-25'))

print()
print("Summary: %d passed, %d failed" % (len(PASS), len(FAIL)))
if FAIL:
    print("FAILED:", FAIL)
    print("VERDICT: FAILURES PRESENT")
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")
sys.exit(0)
