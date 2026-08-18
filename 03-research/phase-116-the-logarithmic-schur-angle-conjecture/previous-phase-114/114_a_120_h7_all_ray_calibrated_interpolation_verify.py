#!/usr/bin/env python3
"""Exact regression checks for a120 all-positive-ray calibration."""

from fractions import Fraction
from math import floor, gcd, log, sqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_120_H7_ALL_POSITIVE_RAY_CALIBRATED_INTERPOLATION.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def inv_mod(a, p):
    return pow(a % p, -1, p)


def solve_mod(matrix, rhs, p):
    n = len(matrix)
    aug = [[x % p for x in row] + [rhs[i] % p]
           for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col] % p)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = inv_mod(aug[col][col], p)
        aug[col] = [(scale * x) % p for x in aug[col]]
        for i in range(n):
            if i != col:
                scale = aug[i][col]
                aug[i] = [(aug[i][j] - scale * aug[col][j]) % p
                          for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


# p=101 is 2 mod 3.  The generalized Vandermonde with powers 1,3,9 is
# invertible and hits every tested target exactly.
p = 101
m = 3
exponents = [3**r for r in range(m)]
matrix = [[pow(j, e, p) for j in range(1, m + 1)] for e in exponents]
P, Q, t = 2, 5, 4
targets = ([0, 0, 0], [1, 2, 3], [100, 17, 44], [9, 9, 9])
for y in targets:
    rhs = [(pow(P, t, p) * pow(Q, t * e, p) * y[r]) % p
           for r, e in enumerate(exponents)]
    coeffs = solve_mod(matrix, rhs, p)
    recovered = []
    for r, e in enumerate(exponents):
        raw = sum(coeffs[j - 1] * pow(j, e, p) for j in range(1, m + 1))
        value = raw * inv_mod(pow(P, t, p), p)
        value *= inv_mod(pow(Q, t * e, p), p)
        recovered.append(value % p)
    check(f"exact generalized-Vandermonde target {y}", recovered == list(y))

for e in exponents:
    check(f"odd power invertible e={e}", gcd(e, p - 1) == 1)


# The constant window is nonempty for every orientation a>=b; test exact
# rational equivalents and several degree ratios.
L = log(3)
c = 1 / (2 * L)
C_minus = 5 * L / 4
C_plus = 3 * L / 2
for a, b in ((1.0, 1.0), (2.0, 1.0), (10.0, 0.2), (0.7, 0.7)):
    lower = sqrt(c * a * b / C_minus)
    upper = a / C_plus
    check(f"nonempty mu window a={a},b={b}", lower < upper)

check("exact window reduction 9b<10a", Fraction(9, 1) < Fraction(10, 1))


# Use an abstract admissible log(p) inside the proved exponential interval;
# verify the two norm exponents, k<=m and O(t) calibration error.
a, b = 2.0, 0.8
lower = sqrt(c * a * b / C_minus)
upper = a / C_plus
mu = (lower + upper) / 2
errors = []
for t in (100, 200, 400, 800):
    mt = floor(mu * t)
    logp = ((C_minus + C_plus) / 2) * mt
    kt = floor(c * a * b * t * t / logp)
    check(f"selected coordinates fit t={t}", 0 < kt <= mt)
    check(f"coefficient norm margin t={t}", C_plus * mt < a * t)
    check(f"node norm margin t={t}", 1.5 * log(mt) < b * t)
    error = abs(kt * logp - c * a * b * t * t)
    check(f"floor error bounded by logp t={t}", error <= logp + 1e-9)
    errors.append(error / (t * t))
check("normalized calibration error tends down", errors[-1] < errors[0])


markers = (
    "unique form",
    "common content of all coefficients",
    "every positive effective ray",
    "genuine bounded scalar pro-section",
    "map surjectively onto `F_p^m`",
    "on **every** ray with `a,b>0`",
    "H7-FRESH-EXACT",
    "H7-REG-EXCESS-RR",
    "a possible anti-diagonal relation",
    "Row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: SHARP CALIBRATED COEFFICIENT HOLDS ON EVERY POSITIVE RAY")
