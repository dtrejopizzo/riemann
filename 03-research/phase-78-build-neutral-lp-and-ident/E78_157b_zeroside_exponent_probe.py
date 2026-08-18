#!/usr/bin/env python3
"""E78.157b - pin the ZERO-SIDE decay exponent to larger N.

Zero-side  Z_N(sigma) = sum_{kappa in N+2} P(kappa) - sum_{kappa in N} P(kappa),
P(a)=2 sigma/(a^2+sigma^2). Reported: Z_N, its step-ratio, the implied local
exponent p from Z_N ~ C N^{-p}  (p = -log(ratio)/log((N+2)/N)), for both builds,
sigma in {0.55,1,2}. Compare to MESH+BND (rigorous O(N^-2)) and the total.
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
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section       # noqa: E402

SIGMAS = [mp.mpf(s) for s in ["0.55", "1.0", "2.0"]]


def kappas(H, idx, L):
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
    return [mp.re(e) for e in E], d, db


def P(a, s):
    return 2 * s / (a * a + s * s)


def run(label, planted, lam, dps, maxN):
    mp.mp.dps = dps
    H, idx, L = build_mp(lam, maxN, dps, planted=planted)
    cache = {}
    def kap(N):
        if N not in cache:
            Hn, idxn = section(H, idx, maxN, N)
            cache[N] = kappas(Hn, idxn, L)
        return cache[N]
    rows = []
    prev = {str(s): None for s in SIGMAS}
    for N in range(8, maxN - 1, 2):
        kN, dN, dbN = kap(N)
        kM, dM, dbM = kap(N + 2)
        rec = {"N": N}
        for s in SIGMAS:
            Z = mp.fsum(P(k, s) for k in kM) - mp.fsum(P(k, s) for k in kN)
            mesh = -(mp.fsum(P(dd, s) for dd in dM) - mp.fsum(P(dd, s) for dd in dN))
            p = ""
            if prev[str(s)] is not None and Z != 0:
                r = Z / prev[str(s)]
                if r > 0:
                    p = mp.nstr(-mp.log(r) / mp.log(mp.mpf(N + 2) / N), 4)
            prev[str(s)] = Z
            rec[str(s)] = {"Z": mp.nstr(Z, 6), "N2Z": mp.nstr(N * N * Z, 5),
                           "p": p, "N2mesh": mp.nstr(N * N * mesh, 5)}
        rows.append(rec)
        r1 = rec["1.0"]
        print(f"{label:5s} N={N:2d} sig1: Z={r1['Z']:>11s} N2Z={r1['N2Z']:>8s} p={r1['p']:>7s} "
              f"| N2mesh={r1['N2mesh']}", flush=True)
    return {"label": label, "rows": rows}


def main():
    dps, lam, maxN = 60, 6, 26
    out = {"stmt": "zero-side exponent to N=24", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run(label, planted, lam, dps, maxN))
    (HERE / "E78_157b_zeroside_exponent_results.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="ascii")
    print("WROTE results")


if __name__ == "__main__":
    main()
