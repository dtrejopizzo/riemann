#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import setup  # noqa: E402


def run():
    s_values = [2 + 0.2j, 5 + 0.2j, 10 + 0.2j, 15 + 0.2j, 20 + 0.2j]
    print("E72.121 height-normalized graph energy probe")
    print(" lam   N      s   GraphE   Graph/(1+|s|^2)")
    for lam, n_modes in [(12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, _, d, _, _, bq, ce = setup(lam, n_modes)
        for s in s_values:
            a = bq.T @ (s / (s * s - d * d))
            y = solve(ce, a)
            g = bq @ y
            total = max(norm(g) ** 2, 1e-30)
            graph = float(np.sum((d * d) * np.abs(g) ** 2) / total)
            scale = 1.0 + abs(s) ** 2
            print(f"{lam:4.0f} {n_modes:3d} {s.real:6.1f} {graph:8.2e} {graph/scale:18.3e}")


if __name__ == "__main__":
    run()
