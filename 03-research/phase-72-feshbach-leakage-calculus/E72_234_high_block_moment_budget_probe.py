#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def run():
    print("E72.234 high-block moment budget probe")
    print("A=A_1 high plus-current. posInf=max positive eigenvalue.")
    print("lam TrA TrA2 TrA3 posInf negInf posCube bound_posInf_TrA2")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        vals = eigvalsh(a)
        pos = vals[vals > 1.0e-12]
        tr1 = float(np.trace(a).real)
        tr2 = float(np.trace(a @ a).real)
        tr3 = float(np.trace(a @ a @ a).real)
        pos_inf = float(pos[-1]) if len(pos) else 0.0
        neg_inf = float(-vals[0])
        pos_cube = float(np.sum(pos**3))
        bound = pos_inf * tr2
        print(
            f"{lam:3.0f} {tr1:+.6e} {tr2:.6e} {tr3:+.6e} "
            f"{pos_inf:.6e} {neg_inf:.6e} {pos_cube:.6e} {bound:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
