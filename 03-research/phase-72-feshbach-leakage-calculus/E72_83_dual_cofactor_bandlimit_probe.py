#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import setup  # noqa: E402


def run():
    s = 10 + 0.2j
    bands = [2, 4, 8, 16]
    print("E72.83 dual cofactor bandlimit probe")
    print("   lam    N " + " ".join([f"E<= {m:2d}" for m in bands]))
    for lam, n_modes in [(12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, _, d, _, _, bq, ce = setup(lam, n_modes)
        a = bq.T @ (s / (s * s - d * d))
        g = bq @ solve(ce, a)
        total = norm(g) ** 2
        vals = []
        for m in bands:
            vals.append(np.sum(np.abs(g[np.abs(idx) <= m]) ** 2) / total)
        print(f"{lam:6.1f} {n_modes:4d} " + " ".join(f"{v:7.3f}" for v in vals))


if __name__ == "__main__":
    run()
