#!/usr/bin/env python3
import sys

from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_210_cell_energy_factor_probe import cells  # noqa: E402
from E72_222_even_leading_sum_probe import beta_sum_weight  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def run():
    print("E72.223 resonant ELR closure probe")
    print("bound = dim_even/minC^2 * sum beta2*(1-u)")
    print("lam block actual bound ratio dimEven minC")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        dim_even = bq.shape[1] + 1
        minc = float(eigvalsh(c_model)[0])
        rs = cells(lam, idx, L, bq, c_model)
        for block in [0, 1]:
            actual = sum(r[6] for r in rs if r[3] == block)
            s1 = beta_sum_weight(lam, L, block, power=1.0)
            bound = dim_even * s1 / (minc * minc)
            print(
                f"{lam:3.0f} {block:5d} {actual:.6e} {bound:.6e} "
                f"{bound/actual:.2f} {dim_even:4d} {minc:.3e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
