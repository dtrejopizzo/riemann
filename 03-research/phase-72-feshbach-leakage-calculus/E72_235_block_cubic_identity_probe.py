#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402
from E72_233_low_two_block_tail_probe import orth_complement  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def run():
    print("E72.235 block cubic identity probe")
    print("P=Q-projected even modes {0,1}; A=[[B,C],[C*,D]].")
    print("TrA3 = TrB3 + TrD3 + 3Tr(BCC*) + 3Tr(D C*C)")
    print("lam TrA3 TrB3 TrD3 3BCC 3DCC check")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        b = p.conj().T @ a @ p
        d = r.conj().T @ a @ r
        c = p.conj().T @ a @ r
        tr_a = float(np.trace(a @ a @ a).real)
        tr_b = float(np.trace(b @ b @ b).real)
        tr_d = float(np.trace(d @ d @ d).real)
        term_bcc = float((3.0 * np.trace(b @ c @ c.conj().T)).real)
        term_dcc = float((3.0 * np.trace(d @ c.conj().T @ c)).real)
        check = tr_b + tr_d + term_bcc + term_dcc
        print(
            f"{lam:3.0f} {tr_a:+.6e} {tr_b:+.6e} {tr_d:+.6e} "
            f"{term_bcc:+.6e} {term_dcc:+.6e} {check:+.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
