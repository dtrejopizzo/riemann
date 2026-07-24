#!/usr/bin/env python3
"""E78.155 - trajectories of the escaped eigenvalue kappa_esc(N) and c_N.

Tests, per build and N=8..18:
  - c_N = 1 - sum x_j = F_N(infinity): does it -> 0 (zeta) geometrically, or stay
    O(1) (plant)?
  - kappa_esc(N): the eigenvalue of K_N = D + (1/c) x q^T farthest from the mesh
    [-2piN/L, 2piN/L]. Does it converge to a stable isolated point (zeta) or not?
  - leading rank-one escape estimate kappa_hat = (q^T x)/c + mean(d): how well does
    it predict kappa_esc?
  - gap_N = dist(kappa_esc, mesh): isolation margin (should stay bounded below for
    zeta -> genuine isolated spectral point).
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402


def data(H, idx, L):
    mu, A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    n = len(d)
    xv = [x[j] for j in range(n)]
    q = [d[j] - db for j in range(n)]
    c = 1 - mp.fsum(xv)
    qTx = mp.fsum(q[j] * xv[j] for j in range(n))
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf(0)) + xv[a] * q[b] / c
    E, _ = mp.eig(K)
    kap = [mp.re(e) for e in E]
    mesh_r = max(abs(dj) for dj in d)
    # escaped = eigenvalue farthest outside the mesh
    kesc = max(kap, key=lambda v: abs(v))
    gap = min(abs(kesc - dj) for dj in d)
    kap_hat = qTx / c + mp.fsum(d) / n
    return c, qTx, kesc, gap, mesh_r, kap_hat


def run(label, planted, dps, max_modes):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(6, max_modes, dps, planted=planted)
    prev_c = None
    for N in range(8, max_modes + 1, 2):
        H, idx = section(Hmax, idxmax, max_modes, N)
        c, qTx, kesc, gap, mesh_r, kap_hat = data(H, idx, L)
        cratio = "" if prev_c is None else mp.nstr(abs(c / prev_c), 4)
        prev_c = c
        print(f"{label:6s} N={N:2d}  c={mp.nstr(c,5):>12s} (ratio {cratio:>8s})  "
              f"kappa_esc={mp.nstr(kesc,7):>11s}  gap={mp.nstr(gap,4):>8s}  "
              f"mesh_r={mp.nstr(mesh_r,4):>7s}  kappa_hat={mp.nstr(kap_hat,7):>11s}",
              flush=True)


def main():
    dps = 50
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        run(label, planted, dps, 18)


if __name__ == "__main__":
    main()
