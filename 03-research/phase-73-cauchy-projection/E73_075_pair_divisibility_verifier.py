#!/usr/bin/env python3
import sys
import cmath

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_071_packet_mellin_formula_verifier import mellin_closed, h0  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def pair_closed(z, w, L, d, xi):
    return mellin_closed(z, w, L, d, xi) + mellin_closed(z, -w, L, d, xi)


def pair_div(z, w, L, d, xi):
    ez = cmath.exp(z * L)
    ew = cmath.exp(w * L)
    emw = cmath.exp(-w * L)
    a = 1j * ((ew - 1.0) + ez * (emw - 1.0)) / (w - z)
    b = -1j * (ez * (ew - 1.0) + (emw - 1.0)) / (w + z)
    return a * h0(w, d, xi) + b * h0(-w, d, xi)


def run():
    print("E73.075 exact pair divisibility verifier")
    print("Checks Pair_z^infty(w)=A H0(w)+B H0(-w).")
    print(" lam     L   zIm    wIm       absErr      relErr")
    tests = []
    for lam, n_modes in [(16, 20), (20, 24), (24, 28)]:
        for z_im in [GAMMAS[0], 17.30]:
            for w_im in [3.70, GAMMAS[0], GAMMAS[1], 28.40]:
                tests.append((lam, n_modes, 0.20 + 1j * z_im, 1j * w_im))
    for lam, n_modes, z, w in tests:
        d, L, xi, _ = setup_exact(lam, n_modes)
        lhs = pair_closed(z, w, L, d, xi)
        rhs = pair_div(z, w, L, d, xi)
        err = abs(lhs - rhs)
        rel = err / max(abs(lhs), abs(rhs), 1e-300)
        print(f"{lam:4d} {L:7.3f} {z.imag:6.2f} {w.imag:7.2f} {err:11.3e} {rel:11.3e}")


if __name__ == "__main__":
    run()
