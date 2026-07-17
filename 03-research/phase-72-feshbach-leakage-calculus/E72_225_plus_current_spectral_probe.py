#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvals, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def run():
    print("E72.225 plus-current spectral phase probe")
    print("A=sum plus cells; reports trace powers and leading eigenvalue phases")
    print("lam block ReTrA2 ImTrA2 ReTrA3 ImTrA3 ||A||2 ||A||HS topEigAbs topEigArg")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block in [0, 1]:
            a = plus_sum(lam, idx, L, bq, c_model, 0.60, block)
            tr2 = np.trace(a @ a)
            tr3 = np.trace(a @ a @ a)
            s = svd(a, compute_uv=False)
            ev = eigvals(a)
            top = ev[np.argmax(np.abs(ev))]
            print(
                f"{lam:3.0f} {block:5d} "
                f"{tr2.real:+.6e} {tr2.imag:+.6e} "
                f"{tr3.real:+.6e} {tr3.imag:+.6e} "
                f"{s[0]:.3e} {norm(a,'fro'):.3e} "
                f"{abs(top):.3e} {np.angle(top):+.3f}",
                flush=True,
            )


if __name__ == "__main__":
    run()
