#!/usr/bin/env python3
"""E78.152 - verify the bordered-determinant / rank-one spectral-shift identities
and test whether the zeros kappa_j of K_N are REAL.

Identities (verified by hand; here checked numerically):
  T_N(z) = 1/(z-d_b) - sum_j x_j/(z-d_j)            (actual transfer, P76.018)
  F_N(z) = (z-d_b) T_N(z)
  q_j = d_j - d_b,  c = 1 - sum_j x_j,  D = diag(d_j)
  F_N(z) = det([zI-D, x; q^T, c]) / det(zI-D)                      (BD)
  K_N = D + (1/c) x q^T   (real, NON-symmetric rank-one update)
  F_N(z) = c det(zI-K_N)/det(zI-D)                                 (R1)
  T_N'/T_N = Tr(zI-K_N)^{-1} - Tr(zI-D)^{-1} - 1/(z-d_b)           (TR)

CRITICAL TEST: eigenvalues kappa_j of K_N. If all real, the spectral-shift
measure nu_N = sum delta_{kappa_j} - sum delta_{d_j} - delta_{d_b} is a real
signed measure and the SPECTRAL-SHIFT-COUNTING reformulation is well posed.
If some are complex (E78.148 warned F_N is not Herglotz), the representation
needs the complex zeros handled.
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
from P76_018_boundary_characteristic_probe import transfer  # noqa: E402
from P76_035_safe_log_derivative_probe import transfer_prime  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402


def build_KN(H, idx, L):
    mu, A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    n = len(d)
    xv = mp.matrix([x[j] for j in range(n)])
    q = mp.matrix([d[j] - db for j in range(n)])
    c = 1 - mp.fsum(x[j] for j in range(n))
    D = mp.matrix(n, n)
    for j in range(n):
        D[j, j] = d[j]
    K = mp.matrix(n, n)
    for a in range(n):
        for bb in range(n):
            K[a, bb] = D[a, bb] + xv[a] * q[bb] / c
    return d, db, xv, q, c, D, K


def tr_resolvent(M, z):
    n = M.rows
    R = (z * mp.eye(n) - M) ** -1
    return mp.fsum(R[j, j] for j in range(n))


def run(label, planted, lam_int, dps, Ns, max_modes):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    sigma = mp.mpf("1.0")
    z = 1j * sigma
    for N in Ns:
        H, idx = section(Hmax, idxmax, max_modes, N)
        mu, A, db_idx, inner, x = right_transfer_data(H, idx)
        d, db, xv, q, c, D, K = build_KN(H, idx, L)
        # transfer identities
        T = transfer(z, db_idx, inner, x, L)
        Tp = transfer_prime(z, db_idx, inner, x, L)
        F = (z - db) * T
        # (TR) formula
        tr_form = tr_resolvent(K, z) - tr_resolvent(D, z) - 1 / (z - db)
        err_TR = abs(tr_form - Tp / T) / max(1, abs(Tp / T))
        # eigenvalues of K_N -- reality test
        try:
            E, _ = mp.eig(K)
            maximag = max(abs(mp.im(e)) for e in E)
            ncomplex = sum(1 for e in E if abs(mp.im(e)) > mp.mpf("1e-20"))
        except Exception as ex:
            maximag = mp.nan
            ncomplex = -1
        print(f"{label:6s} N={N:2d}  |c|={mp.nstr(abs(c),4):>9s}  "
              f"err_TR={mp.nstr(err_TR,3):>10s}  "
              f"max|Im kappa|={mp.nstr(maximag,4):>11s}  "
              f"#complex={ncomplex}/{K.rows}", flush=True)


def main():
    dps = 50
    lam_int = 6
    max_modes = 14
    Ns = [8, 10, 12]
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        run(label, planted, lam_int, dps, Ns, max_modes)


if __name__ == "__main__":
    main()
