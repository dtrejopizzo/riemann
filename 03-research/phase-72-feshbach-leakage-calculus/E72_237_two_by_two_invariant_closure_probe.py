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


def pos_part_trace3(m):
    vals = eigvalsh(0.5 * (m + m.conj().T))
    return float(np.sum(vals[vals > 1.0e-12] ** 3))


def run():
    print("E72.237 two-by-two invariant closure probe")
    print("For 2x2 B: TrB3 = (3 t s - t^3)/2, t=TrB, s=TrB2.")
    print("lam tB sB gap3s-t2 TrB3 formulaErr tailPlus lhsLow lhsLow/tail")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        b = p.conj().T @ a @ p
        d = r.conj().T @ a @ r
        c = p.conj().T @ a @ r
        t = float(np.trace(b).real)
        s = float(np.trace(b @ b).real)
        trb3 = float(np.trace(b @ b @ b).real)
        formula = 0.5 * (3.0 * t * s - t**3)
        tail = float((np.trace(d @ d @ d) + 3.0 * np.trace(d @ c.conj().T @ c)).real)
        low = float((trb3 + 3.0 * np.trace(b @ c @ c.conj().T)).real)
        ratio = (-low) / max(tail, 1.0e-300) if tail > 0 else np.inf
        print(
            f"{lam:3.0f} {t:+.6e} {s:.6e} {3*s-t*t:+.6e} "
            f"{trb3:+.6e} {abs(trb3-formula):.1e} {tail:+.6e} "
            f"{low:+.6e} {ratio:.3f}",
            flush=True,
        )


if __name__ == "__main__":
    run()
