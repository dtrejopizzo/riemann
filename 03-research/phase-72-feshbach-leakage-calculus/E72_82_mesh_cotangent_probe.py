#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402


def run():
    print("E72.82 mesh cotangent shortcut probe")
    print("   lam    N      tau    |beta1-i|     |beta1|       beta1")
    for lam, n_modes in [(8, 12), (12, 28), (16, 34), (20, 40)]:
        idx, L, d, xi, _, _, _ = setup(lam, n_modes)
        one = np.ones_like(xi)
        for tau in finite_roots(xi, d)[:4]:
            e_tau = np.exp(1j * tau * L)
            m1 = np.dot(1 / (tau - d), one)
            beta1 = (e_tau - 1) / L * m1
            print(
                f"{lam:6.1f} {n_modes:4d} {tau:8.3f} "
                f"{abs(beta1-1j):12.3e} {abs(beta1):11.3e} "
                f"{beta1.real:+.3e}{beta1.imag:+.3e}j"
            )


if __name__ == "__main__":
    run()
