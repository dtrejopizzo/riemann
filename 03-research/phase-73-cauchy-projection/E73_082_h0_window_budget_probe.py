#!/usr/bin/env python3
import sys
import math

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_071_packet_mellin_formula_verifier import h0  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def bexp(value, L):
    if value <= 0:
        return float("-inf")
    return math.log(value) / math.log(L)


def hsum(d, xi, gammas):
    total = 0.0
    maxv = 0.0
    for gamma in gammas:
        w = 1j * gamma
        v = abs(h0(w, d, xi)) + abs(h0(-w, d, xi))
        total += v
        maxv = max(maxv, v)
    return total, maxv


def run():
    print("E73.082 H0 zero-window budget probe")
    print("Measures sum_{w in Z_T/+-} (|H0(w)|+|H0(-w)|).")
    print(" lam     L nwin      sumB      maxB        sum        max")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        for nwin in [3, 5, 8, 10]:
            total, maxv = hsum(d, xi, GAMMAS[:nwin])
            print(
                f"{lam:4d} {L:7.3f} {nwin:4d}"
                f" {bexp(total, L):9.3f} {bexp(maxv, L):9.3f}"
                f" {total:10.3e} {maxv:10.3e}"
            )


if __name__ == "__main__":
    run()
