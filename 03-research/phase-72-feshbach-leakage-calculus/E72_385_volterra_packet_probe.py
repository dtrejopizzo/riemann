#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup, a_vec  # noqa: E402


def packets(idx, d, L, xi, z, grid_n):
    r = np.linspace(0.0, L, grid_n)
    phase = np.exp(1j * np.outer(r, d))
    avec = a_vec(z, L, d)
    az = phase @ avec
    az_sharp = np.conjugate(phase) @ avec
    x = phase @ xi
    dm = phase @ np.ones(len(d), dtype=complex)
    return r, az, az_sharp, x, dm


def volterra_abs(r, x, c):
    # K_c |X|(r_j) = int_0^r_j exp(c(r_j-t))|X(t)|dt, cumulative trapezoid.
    h = r[1] - r[0]
    vals = np.exp(-c * r) * np.abs(x)
    cum = np.zeros_like(r, dtype=float)
    increments = 0.5 * h * (vals[1:] + vals[:-1])
    cum[1:] = np.cumsum(increments)
    return np.exp(c * r) * cum


def run():
    print("E72.385 Volterra packet bounds probe")
    print(" lam    L    M     AXscaled   DXscaled   Bscaled   boundScale")
    z = 0.25 + 1.0j
    sigma = z.real
    c = 0.65
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        r, az, azs, x, dm = packets(idx, d, L, xi, z, 3201)
        kc = volterra_abs(r, x, c)
        ax = np.trapezoid(np.abs(az) * kc, r)
        dx_raw = np.trapezoid(np.abs(dm) * kc, r)
        ez = abs(1 - cmath.exp(z * L))
        dx = ez * dx_raw
        boundary = (np.abs(az[-1]) + np.abs(azs[-1])) / L * np.abs(x[::-1])
        bdry = np.trapezoid(np.exp(c * r) * boundary, r)
        scale = math.exp((c + sigma) * L)
        print(
            f"{lam:4.0f} {L:6.3f} {max(abs(idx)):4d} "
            f"{ax/scale:10.3e} {dx/scale:10.3e} {bdry/scale:9.3e} "
            f"{math.sqrt(L)*L:10.3e}"
        )


if __name__ == "__main__":
    run()
