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
SHARP_WINDOWS = {32}


def bounds(lam, n_modes):
    idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
    a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
    a = 0.5 * (a + a.conj().T)
    p = subspace_coords(idx, k, bq, [0, 1])
    r = orth_complement(p, a.shape[0])
    b = p.conj().T @ a @ p
    dmat = r.conj().T @ a @ r
    c = p.conj().T @ a @ r

    t = float(np.trace(b).real)
    s = float(np.trace(b @ b).real)
    trb3_formula = 0.5 * (3.0 * t * s - t**3)
    bcc = float((3.0 * np.trace(b @ c @ c.conj().T)).real)
    low_margin = -(trb3_formula + bcc)

    vals = eigvalsh(dmat)
    dpos = vals[vals > 1.0e-12]
    dpos_op = float(dpos[-1]) if len(dpos) else 0.0
    chs2 = float(norm(c, "fro") ** 2)
    tail_sharp = float(np.sum(dpos**3)) + 3.0 * dpos_op * chs2
    dop = float(max(abs(vals[0]), abs(vals[-1])))
    tail_full = dop * (float(np.trace(dmat @ dmat).real) + 3.0 * chs2)
    return L, low_margin, tail_sharp, tail_full, float(np.trace(a @ a @ a).real)


def run():
    print("E72.242 hybrid HOC3 certificate")
    print("Use nonspectral full tail except declared sharp finite windows.")
    print("lam L low tailUsed mode margin TrA13 status")
    ok = True
    for lam, n_modes in WINDOWS:
        L, low, sharp, full, tr3 = bounds(lam, n_modes)
        if lam in SHARP_WINDOWS:
            tail = sharp
            mode = "sharp"
        else:
            tail = full
            mode = "full"
        margin = low - tail
        passed = margin >= 0.0 and tr3 <= 1.0e-12
        ok = ok and passed
        print(
            f"{lam:3.0f} {L:.6f} {low:.6e} {tail:.6e} "
            f"{mode:5s} {margin:.6e} {tr3:+.6e} {'PASS' if passed else 'FAIL'}",
            flush=True,
        )
    print(f"overall {'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    run()
