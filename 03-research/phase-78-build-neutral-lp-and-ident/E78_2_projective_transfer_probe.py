#!/usr/bin/env python3
"""E78.2 - Genuine PROJECTIVE-MU-TRANSFER target test.

Item 2 asks: sup_z |Pi_N(z;mu_L) - Pi_N(z;0)| -> 0, where
  Pi_N(z;mu) = T_N(z;mu)/T_N(z0;mu),  T_N(z;mu) = r_z A_N(mu)^{-1} b_N.
The Phase-76 family lives at mu=0; the LP family lives at mu=mu_L. This probe
compares the mu = (section inner-block bottom eigenvalue, an honest mu_L proxy)
family against the mu = 0 family, and reports the projective defect vs N, to
decide whether the item-2 statement is even TRUE (defect -> 0) or plateaus.

Reuses P76.002 build_mp and P76.018 transfer verbatim.
"""

import sys
from pathlib import Path

import mpmath as mp

PHASE76 = Path(
    "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock"
)
sys.path.insert(0, str(PHASE76))
from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_018_boundary_characteristic_probe import transfer  # noqa: E402

GAMMA = "14.134725141734693790"
PLANT = (GAMMA, "0.30", "5.0")


def response(H, idx, mu):
    inner = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    source = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return idx[-1], idx[1:-1], mp.lu_solve(inner, source)


def prof(db, inner, x, L, sigmas, sigma0):
    anchor = transfer(1j * sigma0, db, inner, x, L)
    return anchor, [transfer(1j * s, db, inner, x, L) / anchor for s in sigmas]


def run():
    dps = 55
    mp.mp.dps = dps
    sigmas = [mp.mpf(s) for s in ("0.6", "1.0", "2.0", "3.0")]
    sigma0 = mp.mpf("1.0")
    for label, planted in (("zeta", None), ("plant", PLANT)):
        print(f"===== {label} dps={dps} =====")
        for N in (6, 8, 10, 12, 14, 16):
            H, idx, L = build_mp(6, N, dps, planted=planted)
            inner_eigs, _ = mp.eigsy(H[1:-1, 1:-1])
            mu_bottom = inner_eigs[0]
            db, inner, x_mu = response(H, idx, mu_bottom)
            _, _, x_0 = response(H, idx, mp.mpf(0))
            a_mu, p_mu = prof(db, inner, x_mu, L, sigmas, sigma0)
            a_0, p_0 = prof(db, inner, x_0, L, sigmas, sigma0)
            rel = [
                abs(p_mu[j] - p_0[j]) / max(1, abs(p_mu[j]), abs(p_0[j]))
                for j in range(len(sigmas))
            ]
            print(
                f"N={N:2d} mu_bottom={mp.nstr(mu_bottom,6):>12s} "
                f"|anchor0|={mp.nstr(abs(a_0),5):>11s} "
                f"maxProjDefect(mu_L vs 0)={mp.nstr(max(rel),6)}"
            )


if __name__ == "__main__":
    run()
