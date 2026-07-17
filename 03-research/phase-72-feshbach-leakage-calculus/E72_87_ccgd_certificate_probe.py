#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import setup  # noqa: E402


def run():
    s_values = [5 + 0.2j, 10 + 0.2j, 15 + 0.2j]
    hcuts = [8, 12, 18, 24]
    print("E72.87 CCGD finite quadratic certificate probe")
    print(" lam   N      s Hcut   direct-tail   quad-tail     diff")
    for lam, n_modes in [(12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, _, d, _, _, bq, ce = setup(lam, n_modes)
        for s in s_values:
            a = bq.T @ (s / (s * s - d * d))
            y = solve(ce, a)
            g = bq @ y
            total = norm(g) ** 2
            for hcut in hcuts:
                mask = (np.abs(d) > hcut).astype(float)
                tail_direct = np.sum(mask * np.abs(g) ** 2) / total
                tail_matrix = bq.T @ (mask[:, None] * bq)
                tail_quad = np.vdot(y, tail_matrix @ y).real / total
                print(
                    f"{lam:4.0f} {n_modes:3d} {s.real:6.1f} {hcut:4.0f} "
                    f"{tail_direct:13.3e} {tail_quad:12.3e} "
                    f"{abs(tail_direct-tail_quad):9.1e}"
                )


if __name__ == "__main__":
    run()
