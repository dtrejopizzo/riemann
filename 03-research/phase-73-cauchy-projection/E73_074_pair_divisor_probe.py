#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_071_packet_mellin_formula_verifier import mellin_closed, h0  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def pair_closed(z, w, L, d, xi):
    return mellin_closed(z, w, L, d, xi) + mellin_closed(z, -w, L, d, xi)


def run():
    print("E73.074 pair divisor probe")
    print("Tests whether Pair_z(w) is small when the Cauchy divisor H0(w) is small.")
    print(" lam     L   zIm     wIm      |Pair|       |H0(w)|    ratio")
    w_tests = [3.70, 11.11, GAMMAS[0], GAMMAS[1], GAMMAS[2], 28.40]
    for lam, n_modes in [(16, 20), (20, 24), (24, 28)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        for z_im in [GAMMAS[0], 17.30]:
            z = 0.20 + 1j * z_im
            for w_im in w_tests:
                w = 1j * w_im
                pair = abs(pair_closed(z, w, L, d, xi))
                div = abs(h0(w, d, xi))
                ratio = pair / max(div, 1e-300)
                print(f"{lam:4d} {L:7.3f} {z_im:6.2f} {w_im:7.2f} {pair:11.3e} {div:11.3e} {ratio:9.3e}")


if __name__ == "__main__":
    run()
