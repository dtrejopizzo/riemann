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


def certificate(lam, n_modes):
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

    vals_d = eigvalsh(dmat)
    dpos = vals_d[vals_d > 1.0e-12]
    dpos_op = float(dpos[-1]) if len(dpos) else 0.0
    dpos_cube = float(np.sum(dpos**3))
    chs2 = float(norm(c, "fro") ** 2)
    tail_bound = dpos_cube + 3.0 * dpos_op * chs2

    hoc3 = float(np.trace(a @ a @ a).real)
    return {
        "L": L,
        "t": t,
        "s": s,
        "gap": 3.0 * s - t * t,
        "low_margin": low_margin,
        "tail_bound": tail_bound,
        "margin": low_margin - tail_bound,
        "hoc3": hoc3,
    }


def run():
    print("E72.240 HOC3 finite certificate")
    print("PASS iff t<0, 3s-t^2>0, and lowMargin>=tailBound.")
    print("lam L tB gap lowMargin tailBound certMargin TrA13 status")
    ok = True
    for lam, n_modes in WINDOWS:
        c = certificate(lam, n_modes)
        passed = c["t"] < 0.0 and c["gap"] > 0.0 and c["margin"] >= 0.0 and c["hoc3"] <= 1.0e-12
        ok = ok and passed
        print(
            f"{lam:3.0f} {c['L']:.6f} {c['t']:+.6e} {c['gap']:+.6e} "
            f"{c['low_margin']:.6e} {c['tail_bound']:.6e} {c['margin']:.6e} "
            f"{c['hoc3']:+.6e} {'PASS' if passed else 'FAIL'}",
            flush=True,
        )
    print(f"overall {'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    run()
