#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import slogdet, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def bordered_pairing(ce, a, b):
    top = np.column_stack([ce.astype(complex), b])
    bottom = np.concatenate([np.conjugate(a), np.array([0.0 + 0.0j])])[None, :]
    bordered = np.vstack([top, bottom])
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        sign_b, log_b = slogdet(bordered)
        sign_c, log_c = slogdet(ce.astype(complex))
    return -(sign_b / sign_c) * np.exp(log_b - log_c)


def run():
    print("E72.273 pole-even bordered minor identity")
    print("Checks <a,C^-1 b> = -det[[C,b],[a*,0]]/det(C) in corrected pole-even geometry.")
    s = 10.0 + 0.2j
    for lam, n_modes in [(16, 40), (20, 48), (24, 56)]:
        idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
        d = 2.0 * np.pi * idx / L
        r_even = s / (s * s - d * d)
        a = eb.T @ r_even

        # Use two explicit finite source vectors. This verifies the corrected algebraic minor identity
        # independently of the still-open HPAC source-vector derivation.
        sources = {
            "xi": eb.T @ xi,
            "ones": eb.T @ np.ones_like(d, dtype=complex),
        }
        for name, b in sources.items():
            direct = np.vdot(a, solve(c_actual, b))
            minor = bordered_pairing(c_actual, a, b)
            absdiff = abs(direct - minor)
            reldiff = absdiff / max(abs(direct), 1e-30)
            print(
                f"{lam:3.0f} {name:>5s} |solve|={abs(direct):.6e} "
                f"absdiff={absdiff:.3e} reldiff={reldiff:.3e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
