#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import setup  # noqa: E402


def energy(vec, mask):
    total = norm(vec) ** 2
    if total == 0:
        return np.nan
    return np.sum(np.abs(vec[mask]) ** 2) / total


def run():
    s_values = [2 + 0.2j, 5 + 0.2j, 10 + 0.2j, 15 + 0.2j]
    height_bands = [4, 8, 12, 18, 24]
    print("E72.84 dual cofactor physical-height tightness probe")
    for lam, n_modes in [(12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, _, d, _, _, bq, ce = setup(lam, n_modes)
        print(f"\nlambda={lam:.1f}, N={n_modes}, max|d|={np.max(np.abs(d)):.3f}")
        print("       s " + " ".join([f"E|d|<={h:2d}" for h in height_bands]) + "   E|n|<=16")
        for s in s_values:
            a = bq.T @ (s / (s * s - d * d))
            g = bq @ solve(ce, a)
            vals = [energy(g, np.abs(d) <= h) for h in height_bands]
            n16 = energy(g, np.abs(idx) <= 16)
            print(
                f"{s.real:7.1f} "
                + " ".join(f"{v:9.3f}" for v in vals)
                + f" {n16:10.3f}"
            )


if __name__ == "__main__":
    run()
