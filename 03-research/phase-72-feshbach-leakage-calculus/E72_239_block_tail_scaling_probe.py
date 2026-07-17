#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402
from E72_233_low_two_block_tail_probe import orth_complement  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]


def run():
    print("E72.239 block/tail scaling probe")
    print("Reports core finite quantities against L. low=-[TrB3+3BCC], tailBound=TOB.")
    print("lam L low tailBound tB sB C_HS2 DposOp low*L tail*L tB*L sB*L")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        b = p.conj().T @ a @ p
        d = r.conj().T @ a @ r
        c = p.conj().T @ a @ r
        vals_d = eigvalsh(d)
        dpos = vals_d[vals_d > 1.0e-12]
        dpos_op = float(dpos[-1]) if len(dpos) else 0.0
        dpos_cube = float(np.sum(dpos**3))
        chs2 = float(norm(c, "fro") ** 2)
        tail_bound = dpos_cube + 3.0 * dpos_op * chs2
        low = -float((np.trace(b @ b @ b) + 3.0 * np.trace(b @ c @ c.conj().T)).real)
        t = float(np.trace(b).real)
        s = float(np.trace(b @ b).real)
        print(
            f"{lam:3.0f} {L:.6f} {low:.6e} {tail_bound:.6e} "
            f"{t:+.6e} {s:.6e} {chs2:.6e} {dpos_op:.6e} "
            f"{low*L:.6e} {tail_bound*L:.6e} {t*L:+.6e} {s*L:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
