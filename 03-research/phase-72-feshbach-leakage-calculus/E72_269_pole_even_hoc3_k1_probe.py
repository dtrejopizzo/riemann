#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import even_mode  # noqa: E402
from E72_233_low_two_block_tail_probe import orth_complement  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


WINDOWS = [(16, 40), (20, 48), (24, 56)]


def even_subspace_coords(idx, eb, modes):
    cols = []
    for m in modes:
        v = even_mode(idx, m)
        c = eb.T @ v
        if norm(c) > 1.0e-12:
            cols.append(c)
    q, r = np.linalg.qr(np.column_stack(cols))
    keep = np.abs(np.diag(r)) > 1.0e-10
    return q[:, keep]


def hoc3_row(lam, n_modes):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    a = plus_sum(lam, idx, L, eb, c_model, 0.60, 1)
    a = 0.5 * (a + a.conj().T)
    p = even_subspace_coords(idx, eb, [0, 1])
    r = orth_complement(p, a.shape[0])
    b = p.conj().T @ a @ p
    dmat = r.conj().T @ a @ r
    c = p.conj().T @ a @ r

    t = float(np.trace(b).real)
    s = float(np.trace(b @ b).real)
    trb3 = 0.5 * (3.0 * t * s - t**3)
    bcc = float((3.0 * np.trace(b @ c @ c.conj().T)).real)
    low_margin = -(trb3 + bcc)

    vals_d = eigvalsh(dmat)
    dpos = vals_d[vals_d > 1.0e-12]
    dpos_op = float(dpos[-1]) if len(dpos) else 0.0
    chs2 = float(norm(c, "fro") ** 2)
    tail_sharp = float(np.sum(dpos**3)) + 3.0 * dpos_op * chs2
    dop = float(max(abs(vals_d[0]), abs(vals_d[-1])))
    tail_full = dop * (float(np.trace(dmat @ dmat).real) + 3.0 * chs2)

    vals_a = eigvalsh(a)
    return {
        "lam": lam,
        "L": L,
        "dim": a.shape[0],
        "tr3": float(np.trace(a @ a @ a).real),
        "min_a": float(vals_a[0]),
        "max_a": float(vals_a[-1]),
        "t": t,
        "s": s,
        "low": low_margin,
        "tail_sharp": tail_sharp,
        "tail_full": tail_full,
        "margin_sharp": low_margin - tail_sharp,
        "margin_full": low_margin - tail_full,
        "k1_trace": t,
    }


def run():
    print("E72.269 pole-even HOC3/K1 probe")
    print("Corrected geometry: full even sector, pole energy subtracted; P=span{even modes 0,1}.")
    print("lam L dim TrA3 minA maxA tB sB low sharp full margSharp margFull K1sign")
    for lam, n_modes in WINDOWS:
        r = hoc3_row(lam, n_modes)
        print(
            f"{r['lam']:3.0f} {r['L']:.6f} {r['dim']:3d} "
            f"{r['tr3']:+.6e} {r['min_a']:+.6e} {r['max_a']:+.6e} "
            f"{r['t']:+.6e} {r['s']:.6e} {r['low']:.6e} "
            f"{r['tail_sharp']:.6e} {r['tail_full']:.6e} "
            f"{r['margin_sharp']:+.6e} {r['margin_full']:+.6e} "
            f"{'NEG' if r['k1_trace'] < 0 else 'POS'}",
            flush=True,
        )


if __name__ == "__main__":
    run()
