#!/usr/bin/env python3
import math
import numpy as np


def confluent_matrix(a, m):
    mat = np.zeros((m, m), dtype=complex)
    for q in range(m):
        for p in range(m):
            mat[q, p] = ((-1) ** q) * math.comb(p + q, p) / ((2 * a) ** (p + q + 1))
    return mat


def qjet_coeff(a, k, m):
    return np.array([((-1) ** q) / ((a + k) ** (q + 1)) for q in range(m)], dtype=complex)


def hermite_norm(coeffs):
    return sum(abs(c) / math.factorial(i) for i, c in enumerate(coeffs))


def coeff_norm(a, k, m):
    return hermite_norm(np.linalg.solve(confluent_matrix(a, m), qjet_coeff(a, k, m)))


def run():
    print("E73.028 confluent multiplicity growth probe")
    print("Hermite projection norm as multiplicity grows.")
    print(" sigma      t   delta    m        normH     normH/m^2    normH/exp(m)")
    for sigma, t, delta in [(0.2, 14.0, 3.0), (0.2, 50.0, 3.0), (0.2, 50.0, 0.5), (0.05, 50.0, 0.5)]:
        a = sigma + 1j * t
        k = 1j * (t + delta)
        for m in [2, 3, 4, 6, 8, 10, 12, 16, 20]:
            val = coeff_norm(a, k, m)
            print(f"{sigma:6.2f} {t:6.1f} {delta:7.2f} {m:4d} {val:12.3e} {val/(m*m):12.3e} {val/np.exp(m):12.3e}")


if __name__ == "__main__":
    run()
