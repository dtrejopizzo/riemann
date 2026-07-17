#!/usr/bin/env python3
import sys
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
from E72_380_actual_packet_wwr_probe import setup  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS, g_cancelled  # noqa: E402
from E73_002_rational_projection_probe import rational_projection  # noqa: E402


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


def dd_kernel(u, d, L):
    if abs(u - d) < 1e-10:
        return 1j * L
    return (cmath.exp(-1j * d * L) - cmath.exp(-1j * u * L)) / (u - d)


def source_projection(off_nodes, crit_nodes, idx, d, xi, L):
    out = []
    for b in off_nodes:
        total = 0j
        for dm, xm in zip(d, xi):
            sb = 0j
            for k in crit_nodes:
                gamma = (-1j * k).real
                sb += pi_kernel(b, k, off_nodes) * dd_kernel(-gamma, dm, L)
            total += xm * sb
        out.append(total)
    return np.array(out, dtype=complex)


def run():
    print("E73.003 critical source probe")
    print(" lam     L    nO nK    |rat|       |src|       absErr     expWeighted")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        crit_vals = [g_cancelled(k, d, xi, L) for k in crit_nodes]
        rat = rational_projection(off_nodes, crit_nodes, crit_vals)
        src = source_projection(off_nodes, crit_nodes, idx, d, xi, L)
        err = np.linalg.norm(rat - src)
        weighted = max(abs(cmath.exp(b.real * L) * v) for b, v in zip(off_nodes, src))
        print(
            f"{lam:4.0f} {L:7.3f} {len(off_nodes):4d} {len(crit_nodes):2d} "
            f"{np.linalg.norm(rat):10.3e} {np.linalg.norm(src):10.3e} "
            f"{err:10.3e} {weighted:12.3e}"
        )


if __name__ == "__main__":
    run()
