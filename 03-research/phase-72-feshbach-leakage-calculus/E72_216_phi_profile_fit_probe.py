#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def raw_scaled(idx, L, bq, u):
    raw = bq.T @ u_matrix(idx, L, u * L) @ bq
    return float(norm(raw, "fro") ** 2 / (L * L))


def phi(u, kind):
    if kind == "linear":
        return 1.0 - u
    if kind == "quad":
        return (1.0 - u) ** 2
    if kind == "sqrt":
        return np.sqrt(max(0.0, 1.0 - u))
    if kind == "mix":
        return (1.0 - u) * (1.0 + 0.5 * u)
    raise ValueError(kind)


def run():
    print("E72.216 Phi profile fit probe")
    print("finds K such that rawHS/L^2 <= K Phi(u) on grid u in [0.02,0.98]")
    print("kind maxK at lam,u meanK")
    samples = []
    grid = np.linspace(0.02, 0.98, 97)
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for u in grid:
            samples.append((lam, float(u), raw_scaled(idx, L, bq, float(u))))
    for kind in ["sqrt", "linear", "mix", "quad"]:
        ratios = []
        for lam, u, val in samples:
            ratios.append((val / max(phi(u, kind), 1e-300), lam, u, val))
        maxr = max(ratios, key=lambda t: t[0])
        meanr = float(np.mean([r[0] for r in ratios]))
        print(f"{kind:6s} {maxr[0]:.4f} at {maxr[1]:.0f},{maxr[2]:.3f} {meanr:.4f}")

    print("\nRecommended envelope check: rawHS/L^2 <= 0.75 sqrt(1-u)")
    print("violations count and worst slack")
    viol = []
    for lam, u, val in samples:
        bound = 0.75 * phi(u, "sqrt")
        if val > bound:
            viol.append((val - bound, lam, u, val, bound))
    if not viol:
        print("no violations")
    else:
        worst = max(viol, key=lambda t: t[0])
        print(f"violations={len(viol)} worst={worst}")


if __name__ == "__main__":
    run()
