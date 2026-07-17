#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402
from E72_285_apcb_autocorrelation_probe import prime_weights  # noqa: E402


def band_profile(lam, n_modes):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    delta = c_actual - c_model
    vals, vecs = eigh(delta)
    u = vecs[:, -1]
    coeff = eb @ u
    d = 2.0 * np.pi * idx / L
    mass = np.abs(coeff) ** 2
    mass = mass / np.sum(mass)

    weights = prime_weights(lam, L)
    y = np.array([yy for _, _, yy in weights])
    a = np.array([w for _, w, _ in weights])
    omegas = np.linspace(0.0, 4.0, 4001)
    sym = np.sum(a[:, None] * np.cos(y[:, None] * omegas[None, :]), axis=0)
    bad_arg = float(omegas[int(np.argmin(sym))])

    return {
        "L": L,
        "pos": float(vals[-1]),
        "bad_arg": bad_arg,
        "mean_abs_d": float(np.sum(np.abs(d) * mass)),
        "rms_d": float(np.sqrt(np.sum(d * d * mass))),
        "low": float(np.sum(mass[np.abs(d) < 2.0])),
        "mid": float(np.sum(mass[(np.abs(d) >= 2.0) & (np.abs(d) < 8.0)])),
        "high": float(np.sum(mass[np.abs(d) >= 8.0])),
    }


def run():
    print("E72.289 APCB band-exclusion probe")
    print("Top positive Delta_arith eigenvector mass in mesh frequency d=2pi n/L.")
    print("badArg is the low-frequency minimizer of the full-line Dirichlet symbol on [0,4].")
    print("lam L pos/L2 badArg mean|d| rmsD mass|d|<2 mass2<=|d|<8 mass|d|>=8")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        r = band_profile(lam, n_modes)
        L2 = r["L"] * r["L"]
        print(
            f"{lam:3.0f} {r['L']:.6f} {r['pos'] / L2:.6e} "
            f"{r['bad_arg']:.6e} {r['mean_abs_d']:.6e} {r['rms_d']:.6e} "
            f"{r['low']:.6e} {r['mid']:.6e} {r['high']:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
