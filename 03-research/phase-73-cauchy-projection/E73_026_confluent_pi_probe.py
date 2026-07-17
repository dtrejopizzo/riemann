#!/usr/bin/env python3
import cmath
import math
import numpy as np


def confluent_matrix(a, m):
    mat = np.zeros((m, m), dtype=complex)
    for q in range(m):
        for p in range(m):
            # (1/q!) d^q/ds^q (s+a)^(-p-1) at s=a.
            mat[q, p] = ((-1) ** q) * math.comb(p + q, p) / ((2 * a) ** (p + q + 1))
    return mat


def qjet_coeff(a, k, m):
    # Coefficients of G_k in (1/q!) Q^(q)(a), Q(s)=sum_k G_k/(s+k).
    return np.array([((-1) ** q) / ((a + k) ** (q + 1)) for q in range(m)], dtype=complex)


def confluent_coeffs_for_k(a, k, m):
    mat = confluent_matrix(a, m)
    return np.linalg.solve(mat, qjet_coeff(a, k, m))


def confluent_lebesgue(L, a, crit_nodes, m, factorial_weight=True):
    total = 0.0
    for k in crit_nodes:
        coeffs = confluent_coeffs_for_k(a, k, m)
        if factorial_weight:
            # Hermite coordinates for p-th pole coefficient are normalized by p!.
            weights = np.array([1.0 / math.factorial(p) for p in range(m)])
            total += np.sum(np.abs(coeffs) * weights)
        else:
            total += np.sum(np.abs(coeffs))
    return abs(cmath.exp(a.real * L)) * total


def d_o(s, off_nodes):
    out = 1.0 + 0j
    for b in off_nodes:
        out *= s + b
    return out


def d_o_prime_at_minus(b, off_nodes):
    out = 1.0 + 0j
    for c in off_nodes:
        if c != b:
            out *= -b + c
    return out


def ell(a, s, off_nodes):
    out = 1.0 + 0j
    for c in off_nodes:
        if c != a:
            out *= (s - c) / (a - c)
    return out


def pi_kernel(b, k, off_nodes):
    total = 0j
    for a in off_nodes:
        total += d_o(a, off_nodes) * ell(a, -b, off_nodes) / (a + k)
    return total / d_o_prime_at_minus(b, off_nodes)


def separated_lebesgue(L, off_nodes, crit_nodes):
    vals = []
    for b in off_nodes:
        vals.append(abs(cmath.exp(b.real * L)) * sum(abs(pi_kernel(b, k, off_nodes)) for k in crit_nodes))
    return max(vals)


def run():
    print("E73.026 confluent Pi probe")
    print("Compares separated-node blow-up with Hermite/confluent coordinates.")
    print("   L   m   sepScale        separated          confluent      ratio")
    crit_nodes = [1j * y for y in [14.1, 21.0, 25.0, 30.4, 32.9]]
    a = 0.20 + 1j * 14.1
    for L in [5, 10, 15, 20]:
        for m in [2, 3, 4]:
            conf = confluent_lebesgue(L, a, crit_nodes, m)
            for sep_scale in [0.0, 0.5, 1.0, 1.5]:
                eps = np.exp(-sep_scale * L)
                off_nodes = [a + 1j * j * eps for j in range(m)]
                sep = separated_lebesgue(L, off_nodes, crit_nodes)
                print(f"{L:4.0f} {m:3d} {sep_scale:10.2f} {sep:16.3e} {conf:16.3e} {sep/conf:10.3e}")


if __name__ == "__main__":
    run()
