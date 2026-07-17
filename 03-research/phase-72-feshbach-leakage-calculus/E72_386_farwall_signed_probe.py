#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import (  # noqa: E402
    setup,
    sample_packet,
    packet_B,
    von_mangoldt_prime_powers,
)


def D_T(x, T):
    out = np.empty_like(x, dtype=float)
    mask = np.abs(x) < 1e-12
    out[mask] = T / math.pi
    out[~mask] = np.sin(T * x[~mask]) / (math.pi * x[~mask])
    return out


def interp_complex(x, xs, ys):
    return np.interp(x, xs, ys.real) + 1j * np.interp(x, xs, ys.imag)


def compute(lam, n_modes, z, c=0.65, grid_n=14001):
    idx, d, L, xi = setup(lam, n_modes)
    T = math.exp(L)
    delta = 1.0 / math.sqrt(T)
    ts, bs = sample_packet(z, idx, d, L, xi, grid_n)
    gs = np.exp(c * ts) * bs
    rows = von_mangoldt_prime_powers(int(math.exp(L)))
    near = 0j
    far = 0j
    far_abs = 0.0
    total = 0j
    for n, lamn, u in rows:
        if u > L:
            continue
        coeff = lamn * n ** (-0.5 - c)
        gu = math.exp(c * u) * packet_B(u, z, idx, d, L, xi)
        kernel = D_T(ts - u, T)
        diff = (gs - gu) * kernel
        near_mask = np.abs(ts - u) <= delta
        near += coeff * np.trapezoid(diff[near_mask], ts[near_mask])
        far_piece = coeff * np.trapezoid(diff[~near_mask], ts[~near_mask])
        far += far_piece
        far_abs += abs(coeff) * float(np.trapezoid(np.abs(diff[~near_mask]), ts[~near_mask]))
        total += coeff * np.trapezoid(diff, ts)
    return L, T, delta, total, near, far, far_abs


def run():
    print("E72.386 FarWall signed probe")
    print(" lam     L       T       |total|      |near|       |far|       farAbs   abs/far")
    z = 0.25 + 1.0j
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        L, T, delta, total, near, far, far_abs = compute(lam, n_modes, z)
        ratio = far_abs / max(abs(far), 1e-30)
        print(
            f"{lam:4.0f} {L:7.3f} {T:8.1f} {abs(total):11.3e} "
            f"{abs(near):11.3e} {abs(far):11.3e} {far_abs:11.3e} {ratio:9.3e}"
        )


if __name__ == "__main__":
    run()
