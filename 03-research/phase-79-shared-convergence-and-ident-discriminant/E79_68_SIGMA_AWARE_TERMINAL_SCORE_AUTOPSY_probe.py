#!/usr/bin/env python3
"""E79.68 - sigma-aware terminal score autopsy.

Reconstruct the zeta-side active common-cloud shells at sigma=1,2 and test a
small family of intrinsic terminal scores that use only local size/drop/laplacian
information plus sigma-coupling and optional tail bias.
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
sys.path.insert(0, str(HERE))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402
from E79_3W_TERMINAL_SPARSE_PACKET_PROBE import active_common_terms, kappas_for_section  # noqa: E402


OUT = HERE / "E79_68_sigma_aware_terminal_score_autopsy_results.json"
SIGMAS = [mp.mpf("1.0"), mp.mpf("2.0")]
TARGET = {
    8: [6, 7, 8],
    10: [5],
    12: [7],
    14: [10, 11, 12],
    16: [11, 13],
}


def features(arr, i):
    m = len(arr)
    x = arr[i]
    prev = arr[i - 1] if i > 0 else mp.mpf("0")
    nxt = arr[i + 1] if i + 1 < m else mp.mpf("0")
    return {
        "x": x,
        "drop": max(x - nxt, mp.mpf("0")),
        "lap": max(2 * x - prev - nxt, mp.mpf("0")),
        "tail": mp.mpf(m - i),
    }


def score_family(active_rows):
    configs = []
    for sigma_mode in ["sum", "prod", "min"]:
        for base1, base2 in [("x", "drop"), ("x", "lap"), ("drop", "lap"), ("x", "x")]:
            for p1 in [0, 1, 2]:
                for p2 in [0, 1, 2]:
                    for tailpow in [0, 1]:
                        rows = []
                        hits = 0
                        total_rank_error = 0
                        for n in sorted(active_rows):
                            arr1 = active_rows[n]["1.0"]
                            arr2 = active_rows[n]["2.0"]
                            values = []
                            for i in range(len(arr1)):
                                f1 = features(arr1, i)
                                f2 = features(arr2, i)
                                s1 = f1[base1] * f1[base2]
                                s2 = f2[base1] * f2[base2]
                                if p1:
                                    s1 *= f1["x"] ** p1
                                if p2:
                                    s2 *= f2["x"] ** p2
                                if tailpow:
                                    s1 *= f1["tail"] ** tailpow
                                    s2 *= f2["tail"] ** tailpow
                                if sigma_mode == "sum":
                                    s = s1 + s2
                                elif sigma_mode == "prod":
                                    s = s1 * s2
                                else:
                                    s = min(s1, s2)
                                values.append(s)
                            k = len(TARGET[n])
                            pick = sorted(sorted(range(len(values)), key=lambda i: values[i], reverse=True)[:k])
                            ok = pick == TARGET[n]
                            hits += int(ok)
                            total_rank_error += sum(abs(a - b) for a, b in zip(pick, TARGET[n]))
                            rows.append(
                                {
                                    "N": n,
                                    "target": TARGET[n],
                                    "pick": pick,
                                    "exact_match": ok,
                                }
                            )
                        configs.append(
                            {
                                "sigma_mode": sigma_mode,
                                "base1": base1,
                                "base2": base2,
                                "sigma1_x_power": p1,
                                "sigma2_x_power": p2,
                                "tail_power": tailpow,
                                "exact_match_count": hits,
                                "total_rank_error": total_rank_error,
                                "rows": rows,
                            }
                        )
    configs.sort(key=lambda c: (-c["exact_match_count"], c["total_rank_error"]))
    return configs


def main():
    mp.mp.dps = 60
    H, idx, L = build_mp(6, 18, 60, planted=None)
    cache = {}

    def get_kappas(n):
        if n not in cache:
            Hn, idxn = section(H, idx, 18, n)
            cache[n] = kappas_for_section(Hn, idxn, L)
        return cache[n]

    active_rows = {}
    for n in sorted(TARGET):
        sigma_map = {}
        for sigma in SIGMAS:
            active, extra_total, dim_common = active_common_terms(get_kappas(n), get_kappas(n + 2), sigma)
            sigma_map[str(sigma)] = [float(x) for x in active]
        active_rows[n] = sigma_map

    configs = score_family(active_rows)
    result = {
        "statement": "E79.68 sigma-aware intrinsic terminal score autopsy",
        "active_rows": active_rows,
        "target_supports": TARGET,
        "top_configs": configs[:20],
        "best_exact_match_count": configs[0]["exact_match_count"],
        "best_total_rank_error": configs[0]["total_rank_error"],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
