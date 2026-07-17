#!/usr/bin/env python3
import math
import cmath
import numpy as np


def cauchy_block(nodes):
    n = len(nodes)
    out = np.zeros((n, n), dtype=complex)
    for j, a in enumerate(nodes):
        for k, b in enumerate(nodes):
            out[j, k] = 1.0 / (a + b)
    return out


def tail_kernel(L, M, z, w, mmax=200000):
    ez = 1.0 - cmath.exp(z * L)
    total = 0j
    for m in range(M + 1, mmax + 1):
        for sgn in (-1, 1):
            mm = sgn * m
            dm = 2.0 * math.pi * mm / L
            total += ez / ((1j * z - dm) * (w * w + dm * dm))
    return 2j * w * total / L


def run():
    print("E72.395 natural nodal block probe")
    print("   L    M      p   cluster  cond(CA)  relTailOp")
    clusters = {
        "pair": [0.20 + 14.0j, 0.20 - 14.0j],
        "triple": [0.20 + 14.0j, 0.20 - 14.0j, 0.20 + 21.0j],
    }
    for L in (8.0, 12.0, 16.0):
        for p in (1.5, 2.0):
            M = int(math.ceil(L ** p))
            for name, nodes in clusters.items():
                ca = cauchy_block(nodes)
                cond = np.linalg.cond(ca)
                tail = np.zeros_like(ca)
                lead = np.zeros_like(ca)
                for j, a in enumerate(nodes):
                    for k, b in enumerate(nodes):
                        lead[j, k] = cmath.exp(a * L) * ca[j, k]
                        tail[j, k] = tail_kernel(L, M, a, b)
                rel = np.linalg.norm(np.linalg.solve(lead, tail), 2)
                print(f"{L:5.1f} {M:4d} {p:5.1f} {name:>7s} {cond:9.3e} {rel:10.3e}")


if __name__ == "__main__":
    run()
