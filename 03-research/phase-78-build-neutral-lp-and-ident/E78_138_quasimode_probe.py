#!/usr/bin/env python3
"""E78.138 - von Mangoldt quasimode probe (Branch-B follow-up to E78.137).

E78.137 (corrected) found that for the genuine (zeta) build the whole low
inner-block tower nu_0^(N), nu_1^(N), ... collapses to 0 together (Branch B),
so the simple rank-one quasimode lemma from the original plan (uniform gap +
quasimode residual -> 0 implies mu_N -> 0) does not directly apply: there is
no isolated target eigenvalue to deflate against.

This probe still builds the concrete object needed either way: a quasimode
u_N on the mesh d_n = 2 pi n / L with components given by the von Mangoldt
function Lambda(|n|), and measures

    eps_N = ||A_N u_N|| / ||u_N||                     (Rayleigh-type residual)
    R_N   = <u_N, A_N u_N> / <u_N, u_N>                (Rayleigh quotient)

against the INNER block A_N = H[1:-1,1:-1] (the E77.7d/E78.1 operator, using
the same fix as E78.137: never diagonalize the full bordered H).

Reuses P76.002 build_mp verbatim; same builds/lambda/dps grid as E78.137 so
the two probes are directly comparable.
"""
import json
import sys
import mpmath as mp

sys.path.insert(0, "/Users/dt/riemann/03-research/phase-76-normalized-adjugate-arithmetic-lock")
from P76_002_mp_entry_audit import build_mp, primes_upto  # noqa: E402

PLANTED = ("14.134725141734693790", "0.30", "5.0")
DPS = 70
LAM = 6


def von_mangoldt_table(n_max):
    """Lambda(n) for n=1..n_max, exact (mpf), via prime powers."""
    tab = {n: mp.mpf(0) for n in range(1, n_max + 1)}
    for p in primes_upto(n_max):
        lp = mp.log(p)
        pk = p
        while pk <= n_max:
            tab[pk] = lp
            pk *= p
    return tab


def vec_norm(v):
    return mp.sqrt(sum(abs(v[j]) ** 2 for j in range(v.rows)))


def run_one(L_int, N, dps, planted):
    H, idx, L = build_mp(L_int, N, dps, planted=planted)
    inner_idx = idx[1:-1]  # -N+1 .. N-1
    inner = H[1:-1, 1:-1]
    n_max = max(abs(m) for m in inner_idx)
    Lam = von_mangoldt_table(n_max)

    u = mp.matrix(len(inner_idx), 1)
    for a, m in enumerate(inner_idx):
        am = abs(m)
        u[a, 0] = Lam[am] if am >= 1 else mp.mpf(0)

    nrm_u = vec_norm(u)
    if nrm_u == 0:
        return None
    Au = inner * u
    nrm_Au = vec_norm(Au)
    eps = nrm_Au / nrm_u
    rayleigh = (u.T * Au)[0] / (nrm_u ** 2)

    return {
        "N": N,
        "eps_N": mp.nstr(eps, 20),
        "rayleigh_N": mp.nstr(rayleigh, 20),
        "norm_u": mp.nstr(nrm_u, 12),
    }


def run():
    results = {"lambda": LAM, "dps": DPS, "L_values": [4, 6, 8], "builds": {}}
    for build_name, planted in (("zeta", None), ("plant", PLANTED)):
        results["builds"][build_name] = {}
        for L_int in (4, 6, 8):
            rows = []
            Ns = list(range(6, 17, 2))
            for N in Ns:
                try:
                    r = run_one(L_int, N, DPS, planted)
                    if r is not None:
                        rows.append(r)
                        print(build_name, "L=", L_int, r)
                except Exception as e:
                    print(build_name, "L=", L_int, "N=", N, "FAILED:", repr(e))
                    break
            ratios = []
            for i in range(1, len(rows)):
                try:
                    e_prev = mp.mpf(rows[i - 1]["eps_N"])
                    e_cur = mp.mpf(rows[i]["eps_N"])
                    if e_prev != 0:
                        ratios.append(mp.nstr(e_cur / e_prev, 12))
                    else:
                        ratios.append("undef")
                except Exception:
                    ratios.append("err")
            results["builds"][build_name][f"L={L_int}"] = {
                "rows": rows,
                "eps_ratio_consecutive": ratios,
            }
    with open(
        "/Users/dt/riemann/03-research/phase-78-build-neutral-lp-and-ident/E78_138_quasimode_results.json",
        "w",
    ) as f:
        json.dump(results, f, indent=2)
    print("WROTE JSON")


if __name__ == "__main__":
    run()
