#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup  # noqa: E402


GAMMAS = [
    14.134725141734693790,
    21.022039638771554993,
    25.010857580145688763,
    30.424876125859513210,
    32.935061587739189691,
    37.586178158825671257,
]


def phi(w, d):
    return d / (w * w + d * d)


def paired_lcal_coeff(m, idx, d, xi, L, gammas):
    dm = 2.0 * math.pi * m / L
    total = 0j
    for gamma in gammas:
        for w in (1j * gamma, -1j * gamma):
            inner = 0j
            for n, dn, xn in zip(idx, d, xi):
                inner += xn * (phi(w, dm) - phi(w, dn)) / (math.pi * (n - m))
            total += (1.0 - cmath.exp(w * L)) * inner
    return total


def parity_moment(idx, d, xi, gamma):
    w = 1j * gamma
    return sum(xn * phi(w, dn) for dn, xn in zip(d, xi))


def run():
    print("E72.390 parity tail probe")
    print(" lam    L     M    max|S1|       m      |Lc|        m|Lc|      m^2|Lc|")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        M = int(np.max(np.abs(idx)))
        max_s1 = max(abs(parity_moment(idx, d, xi, g)) for g in GAMMAS)
        for m in (2 * M, 3 * M, 4 * M):
            lc = paired_lcal_coeff(m, idx, d, xi, L, GAMMAS)
            print(
                f"{lam:4.0f} {L:6.3f} {M:5d} {max_s1:11.3e} "
                f"{m:6d} {abs(lc):11.3e} {m*abs(lc):11.3e} {m*m*abs(lc):11.3e}"
            )


if __name__ == "__main__":
    run()
