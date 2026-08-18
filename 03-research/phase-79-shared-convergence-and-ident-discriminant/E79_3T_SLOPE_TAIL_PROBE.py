#!/usr/bin/env python3
"""E79.3t - local-slope selector for the deep terminal tail.

Starting from the tau=0.4 onset, define the tail start as the first depth where
the local profile has dropped enough relative to the previous shell:

    a_r / a_{r-1} <= rho,

with rho in a short list of thresholds. This tests whether the onset of true
decay, rather than height alone, stabilizes the deep-edge / extra-root pairing.
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
RHOS = [mp.mpf("0.9"), mp.mpf("0.8"), mp.mpf("0.7"), mp.mpf("0.6"), mp.mpf("0.5")]


def rho_key(r):
    return mp.nstr(r, 12)


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

            rhos = {}
            for rho in RHOS:
                start = onset
                for j in range(max(onset + 1, 1), len(active)):
                    prev_amp = amps[j - 1]
                    curr_amp = amps[j]
                    if prev_amp != 0 and curr_amp / prev_amp <= rho:
                        start = j
                        break
                tail = mp.fsum(active[start:])
                minus = tail - extra_total
                scale = max(abs(tail), abs(extra_total))
                rhos[rho_key(rho)] = {
                    "start": start,
                    "take": len(active) - start,
                    "take_over_active": mp.nstr(mp.mpf(len(active) - start) / len(active), 12) if active else None,
                    "mismatch": None if scale == 0 else mp.nstr(abs(minus) / scale, 12),
                    "N2_abs_minus": mp.nstr((n**2) * abs(minus), 12),
                }

            row["sigmas"][str(sigma)] = {
                "active_len": len(active),
                "onset": onset,
                "rhos": rhos,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["rhos"]
        best = min((float(v["mismatch"]), k, v) for k, v in s1.items())
        print(
            f"{label:5s} N={n:2d} onset={row['sigmas']['1.0']['onset']} "
            f"best_rho={best[1]} take={best[2]['take']} mismatch={best[2]['mismatch']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3t slope-based tail selector", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3T_slope_tail_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
