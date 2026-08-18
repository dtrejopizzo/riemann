#!/usr/bin/env python3
"""E79.40 - terminal barycenter/dispersion selectors against ZERO^extra.

Test whether the sparse terminal packet can be approximated by simple support
templates centered at the terminal mass barycenter, optionally widened by a
dispersion estimate. This is a relational statistic, but still much smaller
than subset search.
"""

from __future__ import annotations

import json
import math
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
WINDOWS = [4, 5, 6]


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


def active_common_terms(k_n, k_m, sigma):
    dim_common = min(len(k_n), len(k_m))
    common_terms = [p_kernel(k_m[j], sigma) - p_kernel(k_n[j], sigma) for j in range(dim_common)]
    common_total = mp.fsum(common_terms)
    active = []
    running = mp.mpf("0")
    for r in range(dim_common):
        term = common_terms[dim_common - 1 - r]
        active.append(term)
        running += term
        if common_total != 0 and abs(running / common_total) >= mp.mpf("0.99"):
            break
    extra_total = mp.fsum(p_kernel(k_m[j], sigma) for j in range(dim_common, len(k_m)))
    return active, extra_total, dim_common


def audit_support(active, extra_total, support):
    support = sorted(set(j for j in support if 0 <= j < len(active)))
    packet = mp.fsum(active[j] for j in support)
    minus = packet - extra_total
    scale = max(abs(packet), abs(extra_total))
    return {
        "support": support,
        "packet": mp.nstr(packet, 12),
        "minus": mp.nstr(minus, 12),
        "mismatch": None if scale == 0 else mp.nstr(abs(minus) / scale, 12),
    }


def supports_from_mass(local_weights, start):
    total = mp.fsum(local_weights)
    if total == 0:
        return {"B1": [start]}
    coords = [mp.mpf(i) for i in range(len(local_weights))]
    mu = mp.fsum(w * x for w, x in zip(local_weights, coords)) / total
    var = mp.fsum(w * (x - mu) ** 2 for w, x in zip(local_weights, coords)) / total
    sigma = mp.sqrt(var)
    c = int(mp.nint(mu))
    supports = {}
    supports["B1"] = [start + c]
    supports["B2adj"] = [start + c, start + min(len(local_weights) - 1, c + 1)] if c + 1 < len(local_weights) else [start + max(0, c - 1), start + c]
    rad = max(0, min(len(local_weights) - 1, int(mp.nint(sigma))))
    supports["Bdisp"] = [start + max(0, c - rad), start + c, start + min(len(local_weights) - 1, c + rad)]
    # two-point around barycenter with nearest left/right shells
    left = max(0, int(mp.floor(mu)))
    right = min(len(local_weights) - 1, int(mp.ceil(mu)))
    supports["Bfloorceil"] = [start + left, start + right]
    return {k: sorted(set(v)) for k, v in supports.items()}


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
        row = {"N": n, "sigmas": {}}
        for sigma in SIGMAS:
            active, extra_total, dim_common = active_common_terms(k_n, k_m, sigma)
            rules = {}
            m = len(active)
            for w in WINDOWS:
                ww = min(w, m)
                start = m - ww
                local_weights = [abs(active[j]) for j in range(start, m)]
                for name, support in supports_from_mass(local_weights, start).items():
                    out = audit_support(active, extra_total, support)
                    out["window"] = ww
                    rules[f"{name}-W{ww}"] = out
            row["sigmas"][str(sigma)] = {
                "dim_common": dim_common,
                "active_len": m,
                "extra": mp.nstr(extra_total, 12),
                "rules": rules,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["rules"]
        best = min((float(v["mismatch"]), k, v) for k, v in s1.items())
        print(f"{label:5s} N={n:2d} best={best[1]} support={best[2]['support']} mismatch={best[2]['mismatch']}", flush=True)
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.40 terminal barycenter selectors", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_40_terminal_barycenter_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
