#!/usr/bin/env python3
"""E79.45 - residual second-packet audit after the multisigma raw packet.

Fix the best multisigma raw packet S1 from E79.44. Then ask whether a second
support S2 inside the same terminal window materially improves the fit to
ZERO^extra, or whether the remainder is already small / structurally unstable.
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


def packet_value(active, support):
    return mp.fsum(active[j] for j in support)


def normalized_mismatch(packet, target):
    scale = max(abs(packet), abs(target))
    return mp.mpf("0") if scale == 0 else abs(packet - target) / scale


def best_first_support(sigma_data):
    min_active_len = min(len(active) for active, _ in sigma_data)
    w = min(WINDOW, min_active_len)
    starts = [len(active) - w for active, _ in sigma_data]
    best = None
    for k in range(1, w + 1):
        for subset_local in itertools.combinations(range(w), k):
            mismatches = []
            support_abs = None
            for (active, extra_total), start in zip(sigma_data, starts):
                subset = [start + j for j in subset_local]
                if support_abs is None:
                    support_abs = subset
                packet = packet_value(active, subset)
                mismatches.append(normalized_mismatch(packet, extra_total))
            mean = mp.fsum(mismatches) / len(mismatches)
            candidate = (-mean, -len(subset_local), tuple(-j for j in subset_local), support_abs, list(subset_local), mismatches)
            if best is None or candidate > best:
                best = candidate
    assert best is not None
    return best[3], best[4], best[5]


def best_second_support(sigma_data, first_local):
    min_active_len = min(len(active) for active, _ in sigma_data)
    w = min(WINDOW, min_active_len)
    starts = [len(active) - w for active, _ in sigma_data]
    allowed_local = [j for j in range(w) if j not in first_local]

    # Empty second packet is allowed.
    best = None
    for k in range(0, len(allowed_local) + 1):
        for subset_local in itertools.combinations(allowed_local, k):
            improvement_ratios = []
            total_mismatches = []
            support_abs = None
            for (active, extra_total), start in zip(sigma_data, starts):
                first_abs = [start + j for j in first_local]
                second_abs = [start + j for j in subset_local]
                if support_abs is None:
                    support_abs = second_abs
                first_packet = packet_value(active, first_abs)
                second_packet = packet_value(active, second_abs)
                first_err = abs(first_packet - extra_total)
                total_packet = first_packet + second_packet
                total_mis = normalized_mismatch(total_packet, extra_total)
                total_mismatches.append(total_mis)
                if first_err == 0:
                    improvement_ratios.append(mp.mpf("0") if abs(total_packet - extra_total) == 0 else mp.mpf("1"))
                else:
                    improvement_ratios.append(abs(total_packet - extra_total) / first_err)
            mean_total = mp.fsum(total_mismatches) / len(total_mismatches)
            mean_ratio = mp.fsum(improvement_ratios) / len(improvement_ratios)
            candidate = (-mean_total, -mean_ratio, -len(subset_local), tuple(-j for j in subset_local), support_abs, list(subset_local), total_mismatches, improvement_ratios)
            if best is None or candidate > best:
                best = candidate
    assert best is not None
    return best[4], best[5], best[6], best[7]


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
        sigma_details = {}
        for sigma in SIGMAS:
            active, extra_total, dim_common = active_common_terms(k_n, k_m, sigma)
            sigma_data.append((active, extra_total))
            sigma_details[str(sigma)] = {
                "dim_common": dim_common,
                "active_len": len(active),
                "extra": mp.nstr(extra_total, 12),
            }
        first_abs, first_local, first_mismatches = best_first_support(sigma_data)
        second_abs, second_local, total_mismatches, improvement_ratios = best_second_support(sigma_data, first_local)

        first_mean = mp.fsum(first_mismatches) / len(first_mismatches)
        total_mean = mp.fsum(total_mismatches) / len(total_mismatches)
        ratio_mean = mp.fsum(improvement_ratios) / len(improvement_ratios)
        row = {
            "N": n,
            "sigmas": sigma_details,
            "first_support_abs": first_abs,
            "first_support_local": first_local,
            "first_mean_mismatch": mp.nstr(first_mean, 12),
            "first_mismatches": {
                str(sigma): mp.nstr(mismatch, 12)
                for sigma, mismatch in zip(SIGMAS, first_mismatches)
            },
            "second_support_abs": second_abs,
            "second_support_local": second_local,
            "total_mean_mismatch": mp.nstr(total_mean, 12),
            "total_mismatches": {
                str(sigma): mp.nstr(mismatch, 12)
                for sigma, mismatch in zip(SIGMAS, total_mismatches)
            },
            "improvement_ratio_mean": mp.nstr(ratio_mean, 12),
            "improvement_ratios": {
                str(sigma): mp.nstr(ratio, 12)
                for sigma, ratio in zip(SIGMAS, improvement_ratios)
            },
        }
        rows.append(row)
        print(
            f"{label:5s} N={n:2d} first={first_abs} mean1={mp.nstr(first_mean,6)} "
            f"second={second_abs} mean12={mp.nstr(total_mean,6)} ratio={mp.nstr(ratio_mean,6)}",
            flush=True,
        )
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.45 residual second-packet audit", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_45_residual_second_packet_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
