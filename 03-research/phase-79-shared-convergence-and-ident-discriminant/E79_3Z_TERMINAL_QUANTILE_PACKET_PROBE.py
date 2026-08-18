#!/usr/bin/env python3
"""E79.3z - terminal quantile packets against ZERO^extra.

Use cumulative mass quantiles inside the last few active-edge shells to define a
small support intrinsically. This is more elastic than one-point rankings or a
fixed motif dictionary, but still much smaller than unrestricted subset search.
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
WINDOWS = [4, 5, 6]
QUANTILE_SETS = {
    "Q50": [mp.mpf("0.50")],
    "Q25Q75": [mp.mpf("0.25"), mp.mpf("0.75")],
    "Q25Q50Q75": [mp.mpf("0.25"), mp.mpf("0.50"), mp.mpf("0.75")],
    "Q20Q50Q80": [mp.mpf("0.20"), mp.mpf("0.50"), mp.mpf("0.80")],
}


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


def quantile_support(active, window, quantiles):
    m = len(active)
    w = min(window, m)
    start = m - w
    local = [abs(active[j]) for j in range(start, m)]
    total = mp.fsum(local)
    if total == 0:
        return [start]
    support = []
    for q in quantiles:
        target = q * total
        run = mp.mpf("0")
        chosen = start
        for r, a in enumerate(local):
            run += a
            if run >= target:
                chosen = start + r
                break
        support.append(chosen)
    return sorted(set(support))


def audit_support(active, extra_total, support):
    packet = mp.fsum(active[j] for j in support)
    minus = packet - extra_total
    scale = max(abs(packet), abs(extra_total))
    return {
        "support": support,
        "packet": mp.nstr(packet, 12),
        "minus": mp.nstr(minus, 12),
        "mismatch": None if scale == 0 else mp.nstr(abs(minus) / scale, 12),
    }


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
            for w in WINDOWS:
                for name, quantiles in QUANTILE_SETS.items():
                    support = quantile_support(active, w, quantiles)
                    out = audit_support(active, extra_total, support)
                    out["window"] = min(w, len(active))
                    out["quantiles"] = [mp.nstr(q, 6) for q in quantiles]
                    rules[f"{name}-W{min(w, len(active))}"] = out
            row["sigmas"][str(sigma)] = {
                "dim_common": dim_common,
                "active_len": len(active),
                "extra": mp.nstr(extra_total, 12),
                "rules": rules,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["rules"]
        best = min((float(v["mismatch"]), k, v) for k, v in s1.items())
        print(
            f"{label:5s} N={n:2d} best={best[1]} support={best[2]['support']} "
            f"mismatch={best[2]['mismatch']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3z terminal quantile packet rules", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3Z_terminal_quantile_packet_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
