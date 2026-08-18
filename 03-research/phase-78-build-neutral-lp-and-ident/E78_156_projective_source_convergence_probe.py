#!/usr/bin/env python3
"""E78.156 - PROJECTIVE-SOURCE-CONVERGENCE (point 2, option ii).

Tests whether the source-selected normalized response
    v_N^res = P_N b_N / ell_0(P_N b_N)
converges in the safe Cauchy topology as N -> infinity, EVEN as the residue
alpha_N = ell_0(P_N b_N) collapses. This is the route (E78.151) that closes
point-2 existence WITHOUT needing simplicity of the ground eigenspace and
WITHOUT a c_0 lower bound.

P_N = spectral projection onto the k lowest-|eigenvalue| modes of the inner
block A_N (k=1 and k=2, to probe near-degeneracy robustness).
ell_0 = safe Cauchy row at z0 = i*1.0.  Test profile at z = i*sigma.
Convergence measure: max_sigma |profile_N(sigma) - profile_{N+2}(sigma)|.
If summable -> projective source direction converges -> point-2 existence
closes via option (ii).  Both builds.
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

from P76_002_mp_entry_audit import build_mp, vec_norm  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402

TESTSIG = [mp.mpf(x) for x in ["0.55", "0.75", "1.5", "2.0", "3.0"]]
Z0 = 1j * mp.mpf("1.0")


def crow(z, inner, L):
    return [1 / (z - 2 * mp.pi * n / L) for n in inner]


def response_profiles(H, idx, L, k):
    mu, A, db_idx, inner, x = right_transfer_data(H, idx)
    # eigen-decomposition of the inner block A (symmetric)
    vals, vecs = mp.eigsy(A)
    order = sorted(range(len(vals)), key=lambda j: abs(vals[j]))
    n = A.rows
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(n)])
    # P_N b = sum over k lowest modes of <e_j,b> e_j
    Pb = mp.matrix(n, 1)
    for jj in order[:k]:
        coeff = mp.fsum(vecs[t, jj] * b[t] for t in range(n))
        for t in range(n):
            Pb[t] += vecs[t, jj] * coeff
    r0 = crow(Z0, inner, L)
    alpha = mp.fsum(r0[t] * Pb[t] for t in range(n))
    if abs(alpha) < mp.mpf("1e-120"):
        return None, alpha
    v = mp.matrix([Pb[t] / alpha for t in range(n)])
    prof = {}
    for s in TESTSIG:
        rz = crow(1j * s, inner, L)
        prof[str(s)] = mp.fsum(rz[t] * v[t] for t in range(n))
    return prof, alpha


def run(label, planted, dps, max_modes, k):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(6, max_modes, dps, planted=planted)
    prev = None
    for N in range(8, max_modes + 1, 2):
        H, idx = section(Hmax, idxmax, max_modes, N)
        prof, alpha = response_profiles(H, idx, L, k)
        if prof is None:
            print(f"{label} k={k} N={N} alpha too small")
            continue
        if prev is not None:
            diff = max(abs(prof[str(s)] - prev[str(s)]) for s in TESTSIG)
        else:
            diff = None
        prev = prof
        ds = "n/a" if diff is None else mp.nstr(diff, 5)
        print(f"{label:6s} k={k} N={N:2d}  |alpha|={mp.nstr(abs(alpha),4):>10s}  "
              f"prof(1.5)={mp.nstr(prof['1.5'],6):>12s}  max|dprof|={ds:>11s}",
              flush=True)


def main():
    dps = 50
    for k in [1, 2]:
        for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
            run(label, planted, dps, 16, k)


if __name__ == "__main__":
    main()
