#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402
from E72_233_low_two_block_tail_probe import orth_complement  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def pos_square_trace(vals):
    p = vals[vals > 1.0e-12]
    return float(np.sum(p**2))


def pos_cube_trace(vals):
    p = vals[vals > 1.0e-12]
    return float(np.sum(p**3))


def run():
    print("E72.238 tail operator bound probe")
    print("tailPlus = Tr(D^3)+3Tr(D C*C); bound uses D_+ operator and HS coupling.")
    print("lam tailPlus DposCube DposOp Dpos2 C_HS2 bound ratio lowMargin/bound")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        b = p.conj().T @ a @ p
        d = r.conj().T @ a @ r
        c = p.conj().T @ a @ r
        vals = eigvalsh(d)
        dpos_op = float(max(vals[-1], 0.0))
        dpos2 = pos_square_trace(vals)
        dpos3 = pos_cube_trace(vals)
        chs2 = float(norm(c, "fro") ** 2)
        tail_plus = float((np.trace(d @ d @ d) + 3.0 * np.trace(d @ c.conj().T @ c)).real)
        bound = dpos3 + 3.0 * dpos_op * chs2
        low = float((np.trace(b @ b @ b) + 3.0 * np.trace(b @ c @ c.conj().T)).real)
        print(
            f"{lam:3.0f} {tail_plus:+.6e} {dpos3:.6e} {dpos_op:.6e} "
            f"{dpos2:.6e} {chs2:.6e} {bound:.6e} "
            f"{bound/max(tail_plus,1e-300):.3f} {(-low)/max(bound,1e-300):.3f}",
            flush=True,
        )


if __name__ == "__main__":
    run()
