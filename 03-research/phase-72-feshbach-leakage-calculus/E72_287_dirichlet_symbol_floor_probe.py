#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_284_upper_complement_split_probe import upper_split  # noqa: E402
from E72_285_apcb_autocorrelation_probe import prime_weights  # noqa: E402


def symbol_floor(lam, n_modes, omega_max=80.0, n_grid=20001):
    r = upper_split(lam, n_modes)
    L = r["L"]
    weights = prime_weights(lam, L)
    y = np.array([yy for _, _, yy in weights])
    a = np.array([w for _, w, _ in weights])
    omegas = np.linspace(0.0, omega_max, n_grid)
    vals = np.zeros_like(omegas)
    for i in range(0, len(omegas), 1000):
        om = omegas[i : i + 1000]
        vals[i : i + 1000] = np.sum(a[:, None] * np.cos(y[:, None] * om[None, :]), axis=0)
    j = int(np.argmin(vals))
    return L, r["delta_pos"], -2.0 * vals[j], omegas[j], vals[j]


def run():
    print("E72.287 Dirichlet-symbol floor probe")
    print("P_L(omega)=sum Lambda(n)n^-1/2 exp(i omega log n), n<=e^L.")
    print("APCB follows from -2 min_omega Re P_L(omega)=O(L^2).")
    print("lam L posDelta/L2 symbolFloor/L2 argMin minRe")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, pos_delta, floor, arg, min_re = symbol_floor(lam, n_modes)
        L2 = L * L
        print(
            f"{lam:3.0f} {L:.6f} {pos_delta / L2:.6e} "
            f"{floor / L2:.6e} {arg:.6e} {min_re:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
