#!/usr/bin/env python3
import cmath
import numpy as np


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


def row_lebesgue(L, off_nodes, crit_nodes):
    vals = []
    for b in off_nodes:
        vals.append(abs(cmath.exp(b.real * L)) * sum(abs(pi_kernel(b, k, off_nodes)) for k in crit_nodes))
    return max(vals)


def run():
    print("E73.025 Pi Lebesgue cluster falsifier")
    print("Shows PI-LEB needs node geometry; arbitrary positive-half-plane clusters can blow up.")
    print("   L   nO   sepScale       maxWeightedLebesgue")
    crit_nodes = [1j * y for y in [14.1, 21.0, 25.0, 30.4, 32.9]]
    for L in [5, 10, 15, 20]:
        for sep_scale in [0.0, 0.5, 1.0, 1.5]:
            eps = np.exp(-sep_scale * L)
            # Cluster three off-line nodes with the same positive real part and nearly equal height.
            off_nodes = [
                0.20 + 1j * 14.1,
                0.20 + 1j * (14.1 + eps),
                0.20 + 1j * (14.1 + 2 * eps),
            ]
            leb = row_lebesgue(L, off_nodes, crit_nodes)
            print(f"{L:4.0f} {len(off_nodes):4d} {sep_scale:10.2f} {leb:24.3e}")


if __name__ == "__main__":
    run()
