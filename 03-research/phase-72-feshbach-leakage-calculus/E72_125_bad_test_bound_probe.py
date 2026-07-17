#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, qr

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import sigma_packet  # noqa: E402
from E72_117_bad_subspace_gram_probe import bad_columns  # noqa: E402


def orthonormal_bad_basis(L, idx, d, k, bq, c_actual, qbad):
    cols = bad_columns(L, idx, d, k, bq, c_actual, qbad=qbad)
    q, r = qr(cols)
    keep = np.abs(np.diag(r)) > 1e-12
    return q[:, keep]


def test_values(e, d, rgrid):
    n = len(d)
    a = np.conj(e[:n])
    b = np.conj(e[n:])
    phases = np.outer(d, rgrid)
    return a @ np.sin(phases) + b @ (rgrid[None, :] * np.cos(phases))


def test_stats(qbasis, d, L):
    rgrid = np.linspace(0.0, L, 4001)
    dr = rgrid[1] - rgrid[0]
    l2_vals = []
    linf_vals = []
    h1_vals = []
    end_vals = []
    for a in range(qbasis.shape[1]):
        vals = test_values(qbasis[:, a], d, rgrid)
        deriv = np.gradient(vals, dr)
        l2 = np.sqrt(np.trapezoid(np.abs(vals) ** 2, rgrid))
        h1 = np.sqrt(np.trapezoid(np.abs(vals) ** 2 + np.abs(deriv) ** 2, rgrid))
        l2_vals.append(l2)
        h1_vals.append(h1)
        linf_vals.append(np.max(np.abs(vals)))
        end_vals.append(max(abs(vals[0]), abs(vals[-1])))
    return max(l2_vals), max(linf_vals), max(h1_vals), max(end_vals)


def run(qbad=3):
    print(f"E72.125 bad-test bound probe q={qbad}")
    print(
        " lam   L dimB roots  maxBTB/x  maxPB/sqrtx  maxComp/sqrtx  "
        "max||T||2  max||T||inf  max||T||H1  maxEnd"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        x = np.exp(L)
        sqrtx = np.sqrt(x)
        qbasis = orthonormal_bad_basis(L, idx, d, k, bq, c_actual, qbad)
        max_l2, max_linf, max_h1, max_end = test_stats(qbasis, d, L)
        max_btb = 0.0
        max_pb = 0.0
        max_comp = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            comps = np.conj(qbasis).T @ y
            pb = norm(comps)
            max_btb = max(max_btb, (pb * pb) / x)
            max_pb = max(max_pb, pb / sqrtx)
            max_comp = max(max_comp, np.max(np.abs(comps)) / sqrtx)
        print(
            f"{lam:4.0f} {L:5.2f} {qbasis.shape[1]:4d} {len(roots):5d} "
            f"{max_btb:9.3e} {max_pb:12.3e} {max_comp:14.3e} "
            f"{max_l2:9.3e} {max_linf:12.3e} {max_h1:11.3e} {max_end:7.2e}"
        )


if __name__ == "__main__":
    run()
