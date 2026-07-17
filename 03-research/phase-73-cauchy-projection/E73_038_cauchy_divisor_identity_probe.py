#!/usr/bin/env python3
import sys
import numpy as np
import mpmath as mp
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return d, L, xi


def cauchy_mp(t, d, xi):
    tt = mp.mpf(t)
    return mp.fsum(mp.mpf(float(w)) / (tt - mp.mpf(float(p))) for p, w in zip(d, xi))


def numerator_over_denominator_mp(t, d, xi):
    tt = mp.mpf(t)
    den = mp.fprod(tt - mp.mpf(float(p)) for p in d)
    num = mp.mpf("0")
    for pole, weight in zip(d, xi):
        pp = mp.mpf(float(pole))
        ww = mp.mpf(float(weight))
        num += ww * mp.fprod(tt - mp.mpf(float(other)) for other in d if other != pole)
    return num / den


def run():
    mp.mp.dps = 100
    print("E73.038 finite Cauchy divisor identity probe")
    print("Checks C_x(t)=P_x(t)/D_x(t) at critical heights using high-precision products.")
    print("Monomial coefficient/root evaluation is intentionally avoided here.")
    print(" lam     L degree       maxAbs       maxRel")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        d, L, xi = setup_full(lam, n_modes)
        max_abs = mp.mpf("0")
        max_rel = mp.mpf("0")
        for gamma in GAMMAS[:6]:
            t = -gamma
            direct = cauchy_mp(t, d, xi)
            pd = numerator_over_denominator_mp(t, d, xi)
            err = abs(pd - direct)
            rel = err / max(abs(direct), mp.mpf("1e-80"))
            max_abs = max(max_abs, err)
            max_rel = max(max_rel, rel)
        print(
            f"{lam:4d} {L:7.3f} {len(d)-1:6d}"
            f" {float(max_abs):12.3e} {float(max_rel):12.3e}"
        )


if __name__ == "__main__":
    run()
