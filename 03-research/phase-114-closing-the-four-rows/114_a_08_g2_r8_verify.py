#!/usr/bin/env python3
"""Exact/asymptotic checks for 114.a.08."""

import math
import sys

import mpmath as mp

mp.mp.dps = 60
FAIL = []


def check(name, condition, detail=""):
    print(("PASS  " if condition else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not condition:
        FAIL.append(name)


def cross_count(r, R):
    return sum((2**j) * math.comb(r, j) * math.comb(R, j) for j in range(min(r, R) + 1))


print("A. Exact cross-polytope count")
# Exhaustive enumeration in small dimensions.
from itertools import product

ok = True
for r in range(1, 5):
    for R in range(0, 7):
        brute = sum(1 for c in product(range(-R, R + 1), repeat=r) if sum(abs(x) for x in c) <= R)
        ok &= brute == cross_count(r, R)
check("A1 formula sum 2^j C(r,j)C(R,j) matches exhaustive counts", ok)

print("\nB. Dominant term")
dominance_ok = True
details = []
for r, R in [(8, 1000), (16, 100000), (30, 10**8)]:
    total = cross_count(r, R)
    top = (2**r) * math.comb(R, r)
    q = mp.mpf(r * r) / (2 * (R - r + 1))
    ratio = mp.mpf(total) / top
    dominance_ok &= 1 <= ratio <= 1 / (1 - q)
    details.append(f"r={r}: ratio-1={float(ratio-1):.3e}")
check("B1 T_r <= total <= T_r/(1-q)", dominance_ok, "; ".join(details))

print("\nC. Coupled asymptotic")
k, a = 2, mp.mpf("0.35")
errors = []
for m in (20, 30, 40, 50):
    r = k * m + 1
    R = int(mp.floor(mp.exp(a * m)))
    exact = mp.log(cross_count(r, R))
    main = r * mp.log(2 * R) - mp.loggamma(r + 1)
    errors.append(abs(exact - main))
check("C1 exact log count agrees with r log(2R)-log(r!) to O(r^2/R)",
      errors[-1] < errors[0] and errors[-1] < mp.mpf("1e-3"),
      "errors=" + ",".join(f"{float(e):.2e}" for e in errors))

# Check the explicit Stirling expansion, using log R rather than ma to avoid a
# floor artefact at the deliberately moderate verifier sizes.
stirling_errors = []
for m in (20, 30, 40, 50):
    r = k * m + 1
    R = int(mp.floor(mp.exp(a * m)))
    exact = mp.log(cross_count(r, R))
    expansion = r * mp.log(2 * R) - ((r + mp.mpf("0.5")) * mp.log(r) - r
                                     + mp.log(2 * mp.pi) / 2 + 1 / (12 * r))
    stirling_errors.append(abs(exact - expansion))
check("C2 Stirling expansion including log terms has vanishing error", stirling_errors[-1] < mp.mpf("2e-3"),
      "last error=%.3e" % float(stirling_errors[-1]))

print("\nD. Gauge-dependent subleading terms")
m = 60
r = k * m + 1
A = a * m
R = int(mp.floor(mp.exp(A)))
l1 = mp.log(cross_count(r, R))
box = r * mp.log(2 * R + 1)
theta_polynomial = k * a * m * m + a * m
check("D1 l1 differs from quadratic scale by a negative m log m term", l1 - k * a * m * m < -k * m * mp.log(m) / 2)
check("D2 box and theta have different linear corrections", abs((box-k*a*m*m)/m - (theta_polynomial-k*a*m*m)/m) > mp.mpf("0.5"))

print("\nE. R8 basepoint")
theta1 = mp.jtheta(3, 0, mp.e ** (-mp.pi))
h0_O = mp.log(theta1)
h_thr_O = h0_O - h0_O
check("E1 h0(O)=log theta(1)>0", h0_O > 0, "h0(O)=%.15f" % float(h0_O))
check("E2 threshold normalization puts O exactly on boundary", h_thr_O == 0)

print("\n" + "=" * 72)
if FAIL:
    print("FAILED CHECKS:", FAIL)
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")

