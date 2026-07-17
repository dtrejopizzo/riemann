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
    print("E72.241 nonspectral tail bound probe")
    print("tail <= ||D||op Tr(D^2) + 3||D||op ||C||HS^2, no D_+ split")
    print("lam lowMargin tailExact tailPlusBound tailFullBound full/plus low/full status")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        b = p.conj().T @ a @ p
        d = r.conj().T @ a @ r
        c = p.conj().T @ a @ r

        low_margin = -float((np.trace(b @ b @ b) + 3.0 * np.trace(b @ c @ c.conj().T)).real)
        tail_exact = float((np.trace(d @ d @ d) + 3.0 * np.trace(d @ c.conj().T @ c)).real)

        vals = eigvalsh(d)
        dpos = vals[vals > 1.0e-12]
        dpos_op = float(dpos[-1]) if len(dpos) else 0.0
        tail_plus = float(np.sum(dpos**3)) + 3.0 * dpos_op * float(norm(c, "fro") ** 2)

        dop = float(max(abs(vals[0]), abs(vals[-1])))
        tail_full = dop * (float(np.trace(d @ d).real) + 3.0 * float(norm(c, "fro") ** 2))
        status = "PASS" if low_margin >= tail_full else "FAIL"
        print(
            f"{lam:3.0f} {low_margin:.6e} {tail_exact:+.6e} {tail_plus:.6e} "
            f"{tail_full:.6e} {tail_full/max(tail_plus,1e-300):.3f} "
            f"{low_margin/max(tail_full,1e-300):.3f} {status}",
            flush=True,
        )


if __name__ == "__main__":
    run()
