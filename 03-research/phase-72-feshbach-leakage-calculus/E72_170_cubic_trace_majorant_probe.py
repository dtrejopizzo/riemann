#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_168_trace_asymmetry_probe import block_stats  # noqa: E402


def cubic_majorant(mat, a):
    vals = eigvalsh(mat)
    m = np.max(np.abs(vals))
    r2 = (1.0 - a) ** 2
    tr2 = float(np.sum(vals ** 2))
    tr3 = float(np.sum(vals ** 3))
    bound = tr2 - (1.0 - r2) * tr3 / max(m, 1e-30)
    exact = sum((r2 * v * v if v >= 0 else v * v) for v in vals)
    return exact, bound, m, tr2, tr3


def run():
    print("E72.170 cubic trace majorant probe")
    print("For ||K||<=M: E_a(K) <= Tr K^2 - (1-(1-a)^2)Tr K^3/M")
    print(" lam    L block  exactE   cubicB   slack   opM    Tr2    Tr3")
    for lam, n_modes in [
        (6, 18),
        (8, 24),
        (10, 28),
        (12, 32),
        (14, 36),
        (16, 40),
        (18, 44),
        (20, 48),
        (22, 52),
        (24, 56),
    ]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        total_exact = 0.0
        total_bound = 0.0
        for name, mat, weight in [("K0", k0, 0.70), ("K1", k1, 0.60)]:
            exact, bound, m, tr2, tr3 = cubic_majorant(mat, weight)
            total_exact += exact
            total_bound += bound
            print(
                f"{lam:4.0f} {L:5.2f} {name:>5s} "
                f"{exact:7.3f} {bound:8.3f} {bound-exact:7.3f} "
                f"{m:6.3f} {tr2:6.3f} {tr3:7.3f}"
            )
        print(
            f"{lam:4.0f} {L:5.2f} {'SUM':>5s} "
            f"{total_exact:7.3f} {total_bound:8.3f} "
            f"{total_bound-total_exact:7.3f}"
        )
        sys.stdout.flush()


if __name__ == "__main__":
    run()
