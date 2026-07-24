#!/usr/bin/env python3
"""E79.3s - penalized scale-matched tail from the tau-onset.

Minimize a simple penalized objective over terminal tails starting at or after
the tau=0.4 onset:

    objective = mismatch_ratio + lambda * (take / active_len)

This tests whether a shortness penalty stabilizes the good deep-tail / extra-root
pairings seen in earlier probes.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
PHASE78 = HERE.parent / "phase-78-build-neutral-lp-and-ident"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))
sys.path.insert(0, str(PHASE78))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402

SIGMAS = [mp.mpf("1.0"), mp.mpf("2.0")]
TAU = mp.mpf("0.4")
LAMBDAS = [mp.mpf("0.0"), mp.mpf("0.05"), mp.mpf("0.10"), mp.mpf("0.20"), mp.mpf("0.30")]


def lambda_key(x):
    return mp.nstr(x, 12)


def p_kernel(a, sigma):
    return 2 * sigma / (a * a + sigma * sigma)


def kappas_for_section(H, idx, L):
    _, _, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    n = len(d)
    xv = mp.matrix([x[j] for j in range(n)])
    q = mp.matrix([d[j] - db for j in range(n)])
    c = 1 - mp.fsum(x[j] for j in range(n))
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf("0")) + xv[a] * q[b] / c
    eigvals, _ = mp.eig(K)
    return sorted([mp.re(ev) for ev in eigvals], key=lambda z: abs(z))


def run_case(label, planted, lam_int=6, max_n=18, dps=60):
    mp.mp.dps = dps
    H, idx, L = build_mp(lam_int, max_n, dps, planted=planted)
    cache = {}

    def get_kappas(n):
        if n not in cache:
            Hn, idxn = section(H, idx, max_n, n)
            cache[n] = kappas_for_section(Hn, idxn, L)
        return cache[n]

    rows = []
    for n in range(8, max_n - 1, 2):
        k_n = get_kappas(n)
        k_m = get_kappas(n + 2)
        dim_n = len(k_n)
        dim_m = len(k_m)
        dim_common = min(dim_n, dim_m)
        row = {"N": n, "dim_common": dim_common, "sigmas": {}}
        for sigma in SIGMAS:
            common_terms = [p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma) for j in range(dim_common)]
            common_total = mp.fsum(common_terms)
            extra_total = mp.fsum(p_kernel(k_m[j], sigma) for j in range(dim_common, dim_m))

            active = []
            running = mp.mpf("0")
            for r in range(dim_common):
                term = common_terms[dim_common - 1 - r]
                active.append(term)
                running += term
                if common_total != 0 and abs(running / common_total) >= mp.mpf("0.99"):
                    break

            amps = [abs((n**2) * term) for term in active]
            peak = max(amps) if amps else mp.mpf("0")
            onset = len(active) - 1
            cutoff = TAU * peak
            while onset >= 0 and amps[onset] <= cutoff:
                onset -= 1
            onset += 1

            lambdas = {}
            candidates = []
            for start in range(onset, len(active)):
                take = len(active) - start
                tail = mp.fsum(active[start:])
                minus = tail - extra_total
                scale = max(abs(tail), abs(extra_total))
                mismatch = mp.inf if scale == 0 else abs(minus) / scale
                rel_len = mp.mpf(take) / len(active) if active else mp.mpf("0")
                candidates.append((start, take, tail, minus, mismatch, rel_len))

            for lam in LAMBDAS:
                best = min(candidates, key=lambda item: item[4] + lam * item[5]) if candidates else None
                lambdas[lambda_key(lam)] = None if best is None else {
                    "start": best[0],
                    "take": best[1],
                    "take_over_active": mp.nstr(best[5], 12),
                    "mismatch": mp.nstr(best[4], 12),
                    "objective": mp.nstr(best[4] + lam * best[5], 12),
                    "N2_abs_minus": mp.nstr((n**2) * abs(best[3]), 12),
                }

            row["sigmas"][str(sigma)] = {
                "active_len": len(active),
                "onset": onset,
                "lambdas": lambdas,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["lambdas"]
        best = s1["0.1"] if "0.1" in s1 else s1["0.10"]
        if best is None:
            print(
                f"{label:5s} N={n:2d} onset={row['sigmas']['1.0']['onset']} no-candidate",
                flush=True,
            )
        else:
            print(
                f"{label:5s} N={n:2d} onset={row['sigmas']['1.0']['onset']} "
                f"take={best['take']} mismatch={best['mismatch']} obj={best['objective']}",
                flush=True,
            )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3s penalized scale-matched tail from tau-onset", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3S_penalized_tail_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
