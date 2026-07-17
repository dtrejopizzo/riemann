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


def interp_complex(x, xs, ys):
    return np.interp(x, xs, ys.real) + 1j * np.interp(x, xs, ys.imag)


def compute(lam, n_modes, z, T, grid_n=4001):
    idx, d, L, xi = setup(lam, n_modes)
    ts_full, bs_full = sample_packet(z, idx, d, L, xi, grid_n)
    pos = ts_full >= 0
    xs = ts_full[pos]
    bs = bs_full[pos]
    h = xs[1] - xs[0]
    deriv = np.gradient(bs, h)
    delta = 1.0 / math.sqrt(T)
    rows = von_mangoldt_prime_powers(int(math.exp(L)))

    omega = 0.0
    mass = 0.0
    w = np.zeros_like(xs, dtype=float)
    for n, lamn, u in rows:
        if u > L:
            continue
        b0 = packet_B(u, z, idx, d, L, xi)
        mask = np.abs(xs - u) <= delta
        if np.any(mask):
            omega += lamn * n ** -0.5 * float(np.max(np.abs(bs[mask] - b0)))
            w[mask] += lamn * n ** -0.5
        mass += lamn * n ** -0.5 * abs(b0)

    deriv_int = float(np.trapezoid(np.abs(deriv) * w, xs))
    return L, len(idx), len(rows), delta, omega, deriv_int, mass


def run():
    print("E72.381 local WWR derivative probe")
    print(" lam  dim    T     delta    Omega      derivInt    ratio    mass")
    for lam, n_modes, T in [(6, 10, 50.0), (8, 12, 70.0), (10, 14, 90.0), (12, 16, 110.0)]:
        L, dim, cells, delta, omega, deriv_int, mass = compute(lam, n_modes, 0.25 + 1.0j, T)
        ratio = omega / deriv_int if deriv_int else float("nan")
        print(
            f"{lam:4.0f} {dim:4d} {T:6.1f} {delta:8.3e} "
            f"{omega:10.3e} {deriv_int:11.3e} {ratio:8.3f} {mass:8.3e}"
        )


if __name__ == "__main__":
    run()
