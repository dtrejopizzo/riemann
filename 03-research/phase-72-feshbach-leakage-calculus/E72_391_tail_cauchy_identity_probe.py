#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup  # noqa: E402
from E72_390_parity_tail_probe import GAMMAS, phi  # noqa: E402


def cauchy_c(iw, d, xi):
    return sum(xn / (iw - dn) for dn, xn in zip(d, xi))


def g_cancelled(w, d, xi, L):
    return (1.0 - cmath.exp(w * L)) * cauchy_c(1j * w, d, xi)


def original_coeff(m, idx, d, xi, L, gammas):
    dm = 2.0 * math.pi * m / L
    total = 0j
    for gamma in gammas:
        for w in (1j * gamma, -1j * gamma):
            inner = 0j
            for n, dn, xn in zip(idx, d, xi):
                inner += xn * (phi(w, dm) - phi(w, dn)) / (math.pi * (n - m))
            total += (1.0 - cmath.exp(w * L)) * inner
    return total


def cauchy_coeff(m, d, xi, L, gammas):
    dm = 2.0 * math.pi * m / L
    total = 0j
    for gamma in gammas:
        for w in (1j * gamma, -1j * gamma):
            total += w * g_cancelled(w, d, xi, L) / (w * w + dm * dm)
    return -2j * total / L


def run():
    print("E72.391 tail Cauchy identity probe")
    print(" lam    L     M      m       |orig|      |cauchy|    absErr     relErr")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        M = int(np.max(np.abs(idx)))
        for m in (2 * M, 3 * M, 4 * M):
            orig = original_coeff(m, idx, d, xi, L, GAMMAS)
            cau = cauchy_coeff(m, d, xi, L, GAMMAS)
            err = abs(orig - cau)
            rel = err / max(abs(orig), 1e-30)
            print(
                f"{lam:4.0f} {L:6.3f} {M:5d} {m:6d} "
                f"{abs(orig):11.3e} {abs(cau):11.3e} {err:10.3e} {rel:10.3e}"
            )


if __name__ == "__main__":
    run()
