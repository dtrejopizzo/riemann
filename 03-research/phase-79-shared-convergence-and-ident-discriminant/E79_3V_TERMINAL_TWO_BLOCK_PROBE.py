#!/usr/bin/env python3
"""E79.3v - short unions of terminal blocks against ZERO^extra.

Test whether the deep-edge / extra-root cancellation lives on a union of two
short terminal blocks separated by a tiny gap, rather than on one contiguous
suffix. The selector remains purely combinatorial on the common-cloud shells.
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
LENS1 = [1, 2, 3]
GAPS = [0, 1, 2]
LENS2 = [1, 2, 3]


def p_kernel(a, sigma):
    return 2 * sigma / (a * a + sigma * sigma)


def combo_key(l1, g, l2):
    return f"{l1}+{g}+{l2}"


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


def two_block_sum(active, l1, gap, l2):
    m = len(active)
    if l1 + gap + l2 > m:
        return None
    tail2_start = m - l2
    tail1_end = tail2_start - gap
    tail1_start = tail1_end - l1
    if tail1_start < 0:
        return None
    block1 = active[tail1_start:tail1_end]
    block2 = active[tail2_start:m]
    return {
        "block1_start": tail1_start,
        "block1_take": l1,
        "gap": gap,
        "block2_start": tail2_start,
        "block2_take": l2,
        "sum": mp.fsum(block1) + mp.fsum(block2),
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
            combos = {}
            for l1 in LENS1:
                for gap in GAPS:
                    for l2 in LENS2:
                        data = two_block_sum(active, l1, gap, l2)
                        if data is None:
                            continue
                        tail = data["sum"]
                        minus = tail - extra_total
                        scale = max(abs(tail), abs(extra_total))
                        combos[combo_key(l1, gap, l2)] = {
                            "block1_start": data["block1_start"],
                            "block1_take": data["block1_take"],
                            "gap": data["gap"],
                            "block2_start": data["block2_start"],
                            "block2_take": data["block2_take"],
                            "take_total": data["block1_take"] + data["block2_take"],
                            "tail": mp.nstr(tail, 12),
                            "minus": mp.nstr(minus, 12),
                            "mismatch": None if scale == 0 else mp.nstr(abs(minus) / scale, 12),
                            "N2_abs_minus": mp.nstr((n**2) * abs(minus), 12),
                        }
            row["sigmas"][str(sigma)] = {
                "dim_common": dim_common,
                "active_len": len(active),
                "extra": mp.nstr(extra_total, 12),
                "combos": combos,
            }
        rows.append(row)
        s1 = row["sigmas"]["1.0"]["combos"]
        if s1:
            best = min((float(v["mismatch"]), k, v) for k, v in s1.items())
            print(
                f"{label:5s} N={n:2d} best={best[1]} total_take={best[2]['take_total']} "
                f"mismatch={best[2]['mismatch']}",
                flush=True,
            )
        else:
            print(f"{label:5s} N={n:2d} no-admissible-two-block-combo", flush=True)
    return {"label": label, "L": mp.nstr(L, 20), "dps": dps, "rows": rows}


def main():
    out = {"statement": "E79.3v terminal two-block sweep", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        out["cases"].append(run_case(label, planted))
    out_path = HERE / "E79_3V_terminal_two_block_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
