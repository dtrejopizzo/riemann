#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def run():
    print("E72.133 complement coercivity split probe")
    print(
        " lam   L  minAct/L  minMod/L  ||Delta||/L  WeylLow/L  maxAct/L"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        ea = eigvalsh(c_actual)
        em = eigvalsh(c_model)
        delta_norm = norm(c_actual - c_model, 2)
        weyl = em[0] - delta_norm
        print(
            f"{lam:4.0f} {L:5.2f} "
            f"{ea[0]/L:9.3e} {em[0]/L:9.3e} {delta_norm/L:11.3e} "
            f"{weyl/L:10.3e} {ea[-1]/L:9.3e}"
        )


if __name__ == "__main__":
    run()
