#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_071_packet_mellin_formula_verifier import mellin_quad, mellin_closed  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def pair_quad(z, w, L, d, xi):
    return mellin_quad(z, w, L, d, xi) + mellin_quad(z, -w, L, d, xi)


def pair_closed(z, w, L, d, xi):
    return mellin_closed(z, w, L, d, xi) + mellin_closed(z, -w, L, d, xi)


def run():
    print("E73.073 paired packet probe")
    print("Verifies Pair_z(w)=M_z(w)+M_z(-w) and reports pairing gain.")
    print(" lam     L   zIm    wIm       absErr    |pair|/max(|M|)      |pair|")
    tests = []
    for lam, n_modes in [(16, 20), (20, 24), (24, 28)]:
        for z_im in [GAMMAS[0], GAMMAS[1]]:
            for w_im in [GAMMAS[0], GAMMAS[1], GAMMAS[2]]:
                tests.append((lam, n_modes, 0.20 + 1j * z_im, 1j * w_im))
    for lam, n_modes, z, w in tests:
        d, L, xi, _ = setup_exact(lam, n_modes)
        pq = pair_quad(z, w, L, d, xi)
        pc = pair_closed(z, w, L, d, xi)
        m1 = mellin_closed(z, w, L, d, xi)
        m2 = mellin_closed(z, -w, L, d, xi)
        err = abs(pq - pc)
        gain = abs(pc) / max(abs(m1), abs(m2), 1e-300)
        print(
            f"{lam:4d} {L:7.3f} {z.imag:6.2f} {w.imag:7.2f}"
            f" {err:12.3e} {gain:17.3e} {abs(pc):11.3e}"
        )


if __name__ == "__main__":
    run()
