#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def signature(vals, tol=1.0e-10):
    return (
        int(np.sum(vals > tol)),
        int(np.sum(vals < -tol)),
        int(np.sum(np.abs(vals) <= tol)),
    )


def run():
    print("E72.226 plus-current Hermitian/normality probe")
    print("A=sum plus cells; H=(A+A*)/2, S=(A-A*)/(2i)")
    print(
        "lam block ReTrA3 TrH3 ratio minH maxH posH negH "
        "||S||F/||H||F ||[A,A*]||F/||A||F^2"
    )
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block in [0, 1]:
            a = plus_sum(lam, idx, L, bq, c_model, 0.60, block)
            ah = a.conj().T
            h = 0.5 * (a + ah)
            s = (a - ah) / (2.0j)
            tr_a3 = float(np.real(np.trace(a @ a @ a)))
            tr_h3 = float(np.real(np.trace(h @ h @ h)))
            ratio = tr_h3 / tr_a3 if abs(tr_a3) > 1.0e-14 else np.nan
            he = eigvalsh(h)
            pos, neg, zero = signature(he)
            comm = a @ ah - ah @ a
            nf = norm(a, "fro")
            print(
                f"{lam:3.0f} {block:5d} "
                f"{tr_a3:+.6e} {tr_h3:+.6e} {ratio:+.3f} "
                f"{he[0]:+.3e} {he[-1]:+.3e} {pos:4d} {neg:4d} "
                f"{norm(s,'fro')/max(norm(h,'fro'),1e-300):.3e} "
                f"{norm(comm,'fro')/max(nf*nf,1e-300):.3e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
