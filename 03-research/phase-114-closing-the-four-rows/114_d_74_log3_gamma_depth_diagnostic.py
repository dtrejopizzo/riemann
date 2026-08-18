#!/usr/bin/env python3
"""Midpoint diagnostic at T=log(3)/2 for Gamma depths 80, 160, 320.

This is deliberately not an interval certificate.  It fixes the exact
step discretization used to select the later Arb/Feshbach computation.
"""

import math
import numpy as np

T = math.log(3.0) / 2.0
A = math.log(2.0)
C_PRIME = A / math.sqrt(2.0)
M0 = math.log(math.pi) + 0.5772156649015329 + math.pi / 2 + 3 * A
H_TARGET = 0.002
RHO = 1000.0

delta = 2 * T - A
mb = math.ceil(delta / H_TARGET)
mm = math.ceil((A - delta) / H_TARGET)

edges = []
for lo, hi, count in (
    (-T, T - A, mb),
    (T - A, A - T, mm),
    (A - T, T, mb),
):
    part = np.linspace(lo, hi, count + 1)
    if edges:
        part = part[1:]
    edges.extend(part.tolist())

edges = np.asarray(edges)
left, right = edges[:-1], edges[1:]
length = right - left
n = len(length)
assert (mb, mm, n) == (203, 144, 550)

roots = np.sqrt(np.outer(length, length))
upper = np.triu_indices(n, 1)
boundary = np.arange(mb)
kernel = np.zeros((n, n))
gamma_constant = 0.0

moment_plus = (
    2 * np.exp(left / 2) * np.expm1(length / 2) / np.sqrt(length)
)
moment_minus = (
    2 * np.exp(-right / 2) * np.expm1(length / 2) / np.sqrt(length)
)


def parity_minima(matrix):
    half = n // 2
    even = matrix[:half, :half] + matrix[:half, ::-1][:, :half]
    odd = matrix[:half, :half] - matrix[:half, ::-1][:, :half]
    return np.linalg.eigvalsh(even)[0], np.linalg.eigvalsh(odd)[0]


print(f"T={T:.17g} mb={mb} mm={mm} n={n} hmax={length.max():.17g}")
for j in range(320):
    b = 2.0 * j + 0.5
    gamma_constant += 2.0 / b
    kernel[np.diag_indices(n)] += (
        2 * (length / b + np.expm1(-b * length) / b**2) / length
    )
    first = np.exp(b * left) * np.expm1(b * length) / b
    second = np.exp(-b * right) * np.expm1(b * length) / b
    block = np.outer(first, second) / roots
    kernel[upper] += block[upper]
    kernel[(upper[1], upper[0])] += block[upper]

    depth = j + 1
    if depth not in (80, 160, 320):
        continue

    form = (gamma_constant - M0) * np.eye(n) - kernel.copy()
    form[boundary, n - mb + boundary] -= C_PRIME
    form[n - mb + boundary, boundary] -= C_PRIME
    form += RHO * (
        np.outer(moment_plus, moment_plus)
        + np.outer(moment_minus, moment_minus)
    )
    even, odd = parity_minima(form)
    print(f"depth={depth:3d} even={even:.16e} odd={odd:.16e}")

print("DIAGNOSTIC_ONLY: no continuum residual or interval radius is certified")
