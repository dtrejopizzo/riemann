#!/usr/bin/env python3
"""P75.002: compare Cauchy, barycentric, and bordered numerator forms."""

import numpy as np
from numpy.linalg import det, norm


def mesh(n=8, L=5.7):
    idx = np.r_[np.arange(-n, 0), np.arange(1, n + 1)]
    return 2.0 * np.pi * idx / L


def numerator_barycentric(z, d, xi):
    total = 0.0 + 0.0j
    for n in range(len(d)):
        prod = 1.0 + 0.0j
        for m in range(len(d)):
            if m != n:
                prod *= z - d[m]
        total += xi[n] * prod
    return total


def denominator(z, d):
    out = 1.0 + 0.0j
    for pole in d:
        out *= z - pole
    return out


def cauchy(z, d, xi):
    return np.sum(xi / (z - d))


def numerator_bordered(z, d, xi):
    a = np.diag(z - d).astype(complex)
    block = np.zeros((len(d) + 1, len(d) + 1), dtype=complex)
    block[:-1, :-1] = a
    block[:-1, -1] = xi
    block[-1, :-1] = 1.0
    return -det(block)


def run():
    rng = np.random.default_rng(75)
    d = mesh()
    xi = rng.normal(size=len(d))
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    points = [0.7, 3.1, 7.0, 2.3 + 0.4j, -4.2 + 0.2j]

    print("P75.002 finite numerator package")
    print("z                  |P-D*C|        |P-P_border|    normalized Q diff")
    worst = 0.0
    for z in points:
        p = numerator_barycentric(z, d, xi)
        c = cauchy(z, d, xi)
        den = denominator(z, d)
        pb = numerator_bordered(z, d, xi)
        err1 = abs(p - den * c)
        err2 = abs(p - pb)
        row = 1.0 / (z - d)
        q_norm = np.dot(row / norm(row), xi)
        norm_diff = abs(q_norm - c / norm(row))
        worst = max(worst, err1, err2, norm_diff)
        print(f"{z!s:18s} {err1:12.3e} {err2:14.3e} {norm_diff:18.3e}")
    print(f"worst_error {worst:.3e}")


if __name__ == "__main__":
    run()

