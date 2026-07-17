#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402
from E72_233_low_two_block_tail_probe import orth_complement  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72), (36, 80)]


def run():
    print("E72.244 low-margin decomposition probe")
    print("lowMargin=-TrB3-3BCC; auto gap check: 3s-t^2 >= s for 2x2 Hermitian.")
    print("lam -TrB3 -3BCC lowMargin s gap gap/s bccHelpFrac")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        b = p.conj().T @ a @ p
        c = p.conj().T @ a @ r
        t = float(np.trace(b).real)
        s = float(np.trace(b @ b).real)
        trb3 = 0.5 * (3.0 * t * s - t**3)
        bcc = float((3.0 * np.trace(b @ c @ c.conj().T)).real)
        low = -(trb3 + bcc)
        help_frac = (-bcc) / max(low, 1.0e-300)
        print(
            f"{lam:3.0f} {-trb3:.6e} {-bcc:+.6e} {low:.6e} "
            f"{s:.6e} {3*s-t*t:.6e} {(3*s-t*t)/max(s,1e-300):.3f} "
            f"{help_frac:+.3f}",
            flush=True,
        )


if __name__ == "__main__":
    run()
