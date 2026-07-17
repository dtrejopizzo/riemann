#!/usr/bin/env python3
import sys
import math
import cmath

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_071_packet_mellin_formula_verifier import h0  # noqa: E402
from E73_075_pair_divisibility_verifier import pair_closed  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def bexp(value, L):
    if value <= 0:
        return float("-inf")
    return math.log(value) / math.log(L)


def coeffs(z, w, L):
    ez = cmath.exp(z * L)
    ew = cmath.exp(w * L)
    emw = cmath.exp(-w * L)
    a = 1j * ((ew - 1.0) + ez * (emw - 1.0)) / (w - z)
    b = -1j * (ez * (ew - 1.0) + (emw - 1.0)) / (w + z)
    return a, b


def run():
    print("E73.077 pair coefficient budget probe")
    print("Measures Pair=A H0(w)+B H0(-w) term sizes at critical heights.")
    print(" lam     L   zIm    wIm      pairB   AH+BHB    ABmaxB    HmaxB    pair")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        for z_im in [GAMMAS[0], GAMMAS[1], 17.30]:
            z = 0.20 + 1j * z_im
            for w_im in [GAMMAS[0], GAMMAS[1], GAMMAS[2], 28.40]:
                w = 1j * w_im
                a, b = coeffs(z, w, L)
                hw = h0(w, d, xi)
                hmw = h0(-w, d, xi)
                pair = abs(pair_closed(z, w, L, d, xi))
                sep = abs(a * hw) + abs(b * hmw)
                abmax = max(abs(a), abs(b))
                hmax = max(abs(hw), abs(hmw))
                print(
                    f"{lam:4d} {L:7.3f} {z_im:6.2f} {w_im:7.2f}"
                    f" {bexp(pair, L):8.3f} {bexp(sep, L):8.3f}"
                    f" {bexp(abmax, L):8.3f} {bexp(hmax, L):8.3f}"
                    f" {pair:9.2e}"
                )


if __name__ == "__main__":
    run()
