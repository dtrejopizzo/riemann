#!/usr/bin/env python3
import sys
import math
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, cauchy_real  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def phi_value(s, L, d, xi):
    return (2.0 / math.sqrt(L)) * math.sin(s * L / 2.0) * cauchy_real(s, d, xi)


def run():
    print("E73.127 characteristic CSV probe")
    print("Phi_N(s)=(2/sqrt(L))sin(sL/2)C_x(s), evaluated at s=-gamma.")
    print(" lam     L gamma        CB      phiB    sineB")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        for gamma in GAMMAS[:3]:
            s = -gamma
            c = abs(cauchy_real(s, d, xi))
            sine_factor = abs((2.0 / math.sqrt(L)) * math.sin(s * L / 2.0))
            phi = abs(phi_value(s, L, d, xi))
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(c, L):9.3f} {bexp(phi, L):9.3f} {bexp(sine_factor, L):8.3f}"
            )


if __name__ == "__main__":
    run()
