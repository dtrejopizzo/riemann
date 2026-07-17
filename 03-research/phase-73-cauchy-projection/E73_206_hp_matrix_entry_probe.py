#!/usr/bin/env python3
import math
import sys
from collections import defaultdict

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E73_201_mp_finite_assembly_probe import mp_arch_closed_digamma, mp_prime_modes  # noqa: E402


mp.mp.dps = 100


def entry_modes(m, n, L):
    d_m = 2.0 * math.pi * m / L
    d_n = 2.0 * math.pi * n / L
    const = defaultdict(complex)
    linear = defaultdict(complex)
    if m == n:
        const[d_n] += 1.0
        const[-d_n] += 1.0
        linear[d_n] += -1.0 / L
        linear[-d_n] += -1.0 / L
    else:
        den = math.pi * (n - m)
        const[d_m] += 1.0 / (2j * den)
        const[-d_m] += -1.0 / (2j * den)
        const[d_n] += -1.0 / (2j * den)
        const[-d_n] += 1.0 / (2j * den)
    return dict(const), dict(linear)


def hp_entry(m, n, L, lam, include_arith=True):
    const, linear = entry_modes(m, n, L)
    arch = mp_arch_closed_digamma(const, linear, L, 80)
    if include_arith:
        return arch - mp_prime_modes(const, linear, L, lam)
    return arch


def hp_matrix(lam, n_modes, include_arith=True):
    L = 2.0 * math.log(lam)
    idx = np.arange(-n_modes, n_modes + 1)
    mat = [[mp.mpf("0") for _ in idx] for __ in idx]
    for a, m in enumerate(idx):
        for b in range(a, len(idx)):
            n = idx[b]
            v = hp_entry(int(m), int(n), L, lam, include_arith=include_arith)
            mat[a][b] = v
            mat[b][a] = v
    return idx, L, mat


def to_numpy(mat):
    return np.array([[float(mp.re(v)) for v in row] for row in mat], dtype=float)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.206 high-precision closed matrix entries")
    print("Compares closed mp entries to the legacy quadrature matrix.")
    print(" lam     L    N  dim include   maxEntryB   diffB   relDiff")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        for include in [False, True]:
            idx, L, hp = hp_matrix(lam, n_modes, include_arith=include)
            hp_np = to_numpy(hp)
            legacy, _, _ = build(lam, n_modes, include_arith=include)
            diff = np.max(np.abs(hp_np - legacy))
            scale = np.max(np.abs(hp_np))
            rel = diff / max(scale, 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {n_modes:4d} {len(idx):4d}"
                f" {str(include):>7s} {bexp(scale, L):10.2f}"
                f" {bexp(diff, L):7.2f} {rel:9.2e}"
            )


if __name__ == "__main__":
    run()
