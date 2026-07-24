#!/usr/bin/env python3
"""E79.44 - multisigma coupled packet functional.

Search for one support inside the last WINDOW active shells that matches
ZERO^extra simultaneously across several safe sigma slices.

We test whether the raw coupled packet rule from E79.43 survives a stronger
coherence demand, and whether any nonzero geometric penalty becomes necessary
once a single support must work across multiple sigma values.
"""

from __future__ import annotations

import itertools
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

SIGMAS = [mp.mpf("0.75"), mp.mpf("1.0"), mp.mpf("1.5"), mp.mpf("2.0")]
WINDOW = 4
LAMBDAS = [mp.mpf("0.0"), mp.mpf("0.01"), mp.mpf("0.05"), mp.mpf("0.10")]
MUS = [mp.mpf("0.0"), mp.mpf("0.01"), mp.mpf("0.05"), mp.mpf("0.10")]
AGGREGATORS = ["mean", "max"]


def p_kernel(a, sigma):
    return 2 * sigma / (a * a + sigma * sigma)


def param_key(lam, mu, agg):
    return f"{agg}-L{mp.nstr(lam,4)}-M{mp.nstr(mu,4)}"


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


def num_blocks(support):
    if not support:
        return 0
    blocks = 1
    for a, b in zip(support, support[1:]):
        if b != a + 1:
            blocks += 1
    return blocks


def packet_value(active, support):
    return mp.fsum(active[j] for j in support)


def normalized_mismatch(active, extra_total, support):
    packet = packet_value(active, support)
    minus = packet - extra_total
    scale = max(abs(packet), abs(extra_total))
    return mp.mpf("0") if scale == 0 else abs(minus) / scale


def score_support(sigma_data, support, lam, mu, agg):
    mismatches = [normalized_mismatch(active, extra_total, support) for active, extra_total in sigma_data]
    if agg == "mean":
        base = mp.fsum(mismatches) / len(mismatches)
    elif agg == "max":
        base = max(mismatches)
    else:
        raise ValueError(f"unknown aggregator {agg}")
    blocks = num_blocks(support)
    value = base + lam * (blocks - 1) + mu * len(support)
    return value, mismatches


def best_support(sigma_data, lam, mu, agg):
    min_active_len = min(len(active) for active, _ in sigma_data)
    w = min(WINDOW, min_active_len)
    starts = [len(active) - w for active, _ in sigma_data]
    # active lists can have slightly different lengths across sigma; align by
    # relative terminal window and express support in local terminal coordinates.
    terminal_indices = list(range(w))
    best = None
    for k in range(1, w + 1):
        for subset_local in itertools.combinations(terminal_indices, k):
            mismatches = []
            support_abs = None
            for (active, extra_total), start in zip(sigma_data, starts):
                subset = [start + j for j in subset_local]
                if support_abs is None:
                    support_abs = subset
                value = normalized_mismatch(active, extra_total, subset)
                mismatches.append(value)
            if agg == "mean":
                base = mp.fsum(mismatches) / len(mismatches)
            else:
                base = max(mismatches)
            blocks = num_blocks(subset_local)
            total = base + lam * (blocks - 1) + mu * len(subset_local)
            candidate = (-total, -len(subset_local), tuple(-j for j in subset_local), support_abs, mismatches, subset_local)
            if best is None or candidate > best:
                best = candidate
    assert best is not None
    return best[3], best[4], list(best[5])


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
        sigma_data = []
        sigma_summary = {}
        for sigma in SIGMAS:
            active, extra_total, dim_common = active_common_terms(k_n, k_m, sigma)
            sigma_data.append((active, extra_total))
            sigma_summary[str(sigma)] = {
                "dim_common": dim_common,
                "active_len": len(active),
                "extra": mp.nstr(extra_total, 12),
            }

        rules = {}
        for agg in AGGREGATORS:
            for lam in LAMBDAS:
                for mu in MUS:
                    support_abs, mismatches, support_local = best_support(sigma_data, lam, mu, agg)
                    rules[param_key(lam, mu, agg)] = {
                        "aggregator": agg,
                        "lambda": mp.nstr(lam, 6),
                        "mu": mp.nstr(mu, 6),
                        "support_abs": support_abs,
                        "support_local": support_local,
                        "blocks_local": num_blocks(support_local),
                        "size": len(support_local),
                        "mean_mismatch": mp.nstr(mp.fsum(mismatches) / len(mismatches), 12),
                        "max_mismatch": mp.nstr(max(mismatches), 12),
                        "mismatches": {
                            str(sigma): mp.nstr(mismatch, 12)
                            for sigma, mismatch in zip(SIGMAS, mismatches)
                        },
                    }
        row = {"N": n, "sigmas": sigma_summary, "rules": rules}
        rows.append(row)
        best = min(
            (
                float(v["mean_mismatch"]) if v["aggregator"] == "mean" else float(v["max_mismatch"]),
                k,
                v,
            )
            for k, v in rules.items()
            if v["aggregator"] == "mean"
        )
        print(
            f"{label:5s} N={n:2d} best_mean={best[1]} support={best[2]['support_abs']} "
            f"mean={best[2]['mean_mismatch']} max={best[2]['max_mismatch']}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.44 multisigma coupled packet functional", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_44_multisigma_coupled_packet_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
