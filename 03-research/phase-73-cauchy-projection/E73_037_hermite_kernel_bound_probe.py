#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def confluent_matrix(a, m):
    mat = np.zeros((m, m), dtype=complex)
    for q in range(m):
        for p in range(m):
            mat[q, p] = ((-1) ** q) * math.comb(p + q, p) / ((2 * a) ** (p + q + 1))
    return mat


def qjet_coeff(a, k, m):
    return np.array([((-1) ** q) / ((a + k) ** (q + 1)) for q in range(m)], dtype=complex)


def hcoeff_for_k(a, k, m):
    return np.linalg.solve(confluent_matrix(a, m), qjet_coeff(a, k, m))


def hermite_norm(vec):
    return sum(abs(c) / math.factorial(i) for i, c in enumerate(vec))


def h_bound(a, k, m, theta):
    beta = k - a
    w0 = 1.0 / (2.0 * a)
    wstar = -1.0 / beta
    d = abs(wstar - w0)
    r = theta * d
    mr = 1.0 / (abs(beta) * (1.0 - theta) * d)
    total = 0.0
    for p in range(m):
        inner = 0.0
        for rr in range(p, m):
            inner += math.comb(rr, p) * (abs(w0) ** (rr - p)) * (r ** (-rr))
        total += inner / math.factorial(p)
    return mr * total


def run():
    print("E73.037 Hermite kernel bound probe")
    print("Compares exact confluent Hermite norm with explicit Taylor-Cauchy bound.")
    print(" sigma      tau   gamma   m theta       actual        bound      ratio")
    for sigma, tau in [(0.05, GAMMAS[0]), (0.10, GAMMAS[0]), (0.20, GAMMAS[0]), (0.20, GAMMAS[1])]:
        a = sigma + 1j * tau
        for gamma in GAMMAS[:6]:
            k = 1j * gamma
            for m in [1, 2, 3, 5]:
                actual = hermite_norm(hcoeff_for_k(a, k, m))
                bound = h_bound(a, k, m, theta=0.5)
                print(
                    f"{sigma:6.2f} {tau:8.3f} {gamma:7.3f} {m:3d} {0.5:5.2f}"
                    f" {actual:12.3e} {bound:12.3e} {bound/max(actual, 1e-300):10.3e}"
                )


if __name__ == "__main__":
    run()
