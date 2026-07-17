#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS, g_cancelled  # noqa: E402
from E73_003_critical_source_probe import pi_kernel  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return d, L, xi


def run():
    print("E73.024 Pi amplification probe")
    print("Separates absolute interpolation ceiling from signed cancelled-Cauchy sum.")
    print(" lam nK     L       bIm       geomAbs      dataMax      absCeil      signed    cancelRatio")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22)]:
        d, L, xi = setup_full(lam, n_modes)
        for nK in [3, 4, 5, 6]:
            crit_nodes = [1j * g for g in GAMMAS[:nK]]
            data = np.array([g_cancelled(k, d, xi, L) for k in crit_nodes], dtype=complex)
            for b in off_nodes:
                pis = np.array([pi_kernel(b, k, off_nodes) for k in crit_nodes], dtype=complex)
                signed = abs(np.sum(pis * data))
                geom_abs = abs(cmath.exp(b.real * L)) * np.sum(np.abs(pis))
                data_max = np.max(np.abs(data))
                abs_ceil = geom_abs * data_max
                weighted = abs(cmath.exp(b.real * L)) * signed
                ratio = weighted / max(abs_ceil, 1e-300)
                print(
                    f"{lam:4d} {nK:2d} {L:7.3f} {b.imag:9.3f} "
                    f"{geom_abs:12.3e} {data_max:11.3e} {abs_ceil:12.3e} "
                    f"{weighted:10.3e} {ratio:12.3e}"
                )


if __name__ == "__main__":
    run()
