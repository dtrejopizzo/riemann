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
    print("E72.251 normalization/power table")
    print("All quantities use model-relative compression. tailFull=||D||op(TrD2+3||C||HS2).")
    print(
        "lam L dim minC minC/L minC/L2 tB tB*L sB sB*L "
        "low low*L low*L2 tailFull tail*L tail*L2"
    )
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        min_c = float(eigvalsh(c_model)[0])
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        b = p.conj().T @ a @ p
        dmat = r.conj().T @ a @ r
        c = p.conj().T @ a @ r
        t = float(np.trace(b).real)
        s = float(np.trace(b @ b).real)
        low = -float((np.trace(b @ b @ b) + 3.0 * np.trace(b @ c @ c.conj().T)).real)
        vals = eigvalsh(dmat)
        dop = float(max(abs(vals[0]), abs(vals[-1])))
        tail = dop * (float(np.trace(dmat @ dmat).real) + 3.0 * float(norm(c, "fro") ** 2))
        print(
            f"{lam:3.0f} {L:.6f} {bq.shape[1]:3d} "
            f"{min_c:.6e} {min_c/L:.6e} {min_c/(L*L):.6e} "
            f"{t:+.6e} {t*L:+.6e} {s:.6e} {s*L:.6e} "
            f"{low:.6e} {low*L:.6e} {low*L*L:.6e} "
            f"{tail:.6e} {tail*L:.6e} {tail*L*L:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
