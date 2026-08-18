#!/usr/bin/env python3
"""E79.1 - extend the ZERO-side exponent audit to larger N.

This probe measures

    ZERO_N(sigma) = sum_{kappa in spec K_{N+2}} P_sigma(kappa)
                  - sum_{kappa in spec K_N}     P_sigma(kappa),

with P_sigma(a) = 2 sigma / (a^2 + sigma^2),

for both the zeta and planted builds. It reports:
  - ZERO_N(sigma)
  - N^2 * ZERO_N(sigma)
  - local step exponents from consecutive ratios
  - sliding-window log-log least-squares fits

The output is purely observational. It is meant to decide whether the live
GAP-Z target looks summable (p > 1), marginal (p ~ 1), or non-summable.
"""

from __future__ import annotations

import argparse
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


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lambda-int", type=int, default=6)
    ap.add_argument("--dps", type=int, default=70)
    ap.add_argument("--max-n", type=int, default=34)
    ap.add_argument("--min-n", type=int, default=8)
    ap.add_argument("--sigmas", nargs="+", default=["0.55", "1.0", "2.0", "3.0"])
    ap.add_argument("--window", type=int, default=4)
    ap.add_argument(
        "--build",
        choices=["both", "zeta", "plant"],
        default="both",
    )
    return ap.parse_args()


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
    return [mp.re(ev) for ev in eigvals]


def local_ratio_exponent(n_prev, z_prev, n_cur, z_cur):
    if z_prev == 0 or z_cur == 0:
        return None
    if mp.sign(z_prev) != mp.sign(z_cur):
        return None
    ratio = abs(z_cur / z_prev)
    if ratio <= 0:
        return None
    return -mp.log(ratio) / mp.log(mp.mpf(n_cur) / mp.mpf(n_prev))


def window_fit(ns, zs):
    pts = [(float(n), float(abs(z))) for n, z in zip(ns, zs) if z != 0]
    if len(pts) < 2:
        return None
    xs = [math.log(n) for n, z in pts]
    ys = [math.log(z) for n, z in pts]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx == 0:
        return None
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    slope = sxy / sxx
    intercept = my - slope * mx
    rss = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
    return {
        "p_fit": -slope,
        "logC_fit": intercept,
        "rss": rss,
    }


def run_case(label, planted, lam_int, dps, min_n, max_n, sigmas, window):
    mp.mp.dps = dps
    H, idx, L = build_mp(lam_int, max_n, dps, planted=planted)
    cache = {}

    def get_kappas(n):
        if n not in cache:
            Hn, idxn = section(H, idx, max_n, n)
            cache[n] = kappas_for_section(Hn, idxn, L)
        return cache[n]

    rows = []
    for n in range(min_n, max_n - 1, 2):
        k_n = get_kappas(n)
        k_m = get_kappas(n + 2)
        rec = {"N": n}
        for sigma in sigmas:
            z = mp.fsum(p_kernel(k, sigma) for k in k_m) - mp.fsum(p_kernel(k, sigma) for k in k_n)
            rec[str(sigma)] = {
                "ZERO": mp.nstr(z, 12),
                "absZERO": mp.nstr(abs(z), 12),
                "N2ZERO": mp.nstr((n * n) * z, 12),
            }
        rows.append(rec)
        s1 = rec[str(sigmas[1] if len(sigmas) > 1 else sigmas[0])]
        print(
            f"{label:5s} N={n:2d} ZERO(sig={sigmas[1] if len(sigmas) > 1 else sigmas[0]})="
            f"{s1['ZERO']:>16s} N2ZERO={s1['N2ZERO']:>16s}",
            flush=True,
        )

    analyses = {}
    ns = [row["N"] for row in rows]
    for sigma in sigmas:
        key = str(sigma)
        vals = [mp.mpf(row[key]["ZERO"]) for row in rows]
        series = []
        for i, n in enumerate(ns):
            item = {
                "N": n,
                "ZERO": rows[i][key]["ZERO"],
                "absZERO": rows[i][key]["absZERO"],
                "N2ZERO": rows[i][key]["N2ZERO"],
            }
            if i > 0:
                p_loc = local_ratio_exponent(ns[i - 1], vals[i - 1], n, vals[i])
                item["p_local"] = None if p_loc is None else mp.nstr(p_loc, 10)
            else:
                item["p_local"] = None
            if i + 1 >= window:
                fit = window_fit(ns[i + 1 - window:i + 1], vals[i + 1 - window:i + 1])
                if fit is not None:
                    item["p_window"] = f"{fit['p_fit']:.10f}"
                    item["rss_window"] = f"{fit['rss']:.6e}"
                else:
                    item["p_window"] = None
                    item["rss_window"] = None
            else:
                item["p_window"] = None
                item["rss_window"] = None
            series.append(item)
        analyses[key] = series

    return {
        "label": label,
        "L": mp.nstr(L, 20),
        "dps": dps,
        "min_n": min_n,
        "max_n": max_n,
        "rows": rows,
        "analysis": analyses,
    }


def main():
    args = parse_args()
    sigmas = [mp.mpf(s) for s in args.sigmas]
    out = {
        "statement": "E79.1 extended ZERO-side exponent audit",
        "lambda_int": args.lambda_int,
        "dps": args.dps,
        "min_n": args.min_n,
        "max_n": args.max_n,
        "sigmas": [str(s) for s in sigmas],
        "window": args.window,
        "cases": [],
    }
    out_path = HERE / "E79_1_zero_exponent_results.json"
    existing_cases = {}
    if args.build != "both" and out_path.exists():
        try:
            old = json.loads(out_path.read_text())
            for case in old.get("cases", []):
                existing_cases[case.get("label")] = case
        except Exception:
            existing_cases = {}
    cases = [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]
    if args.build == "zeta":
        cases = [cases[0]]
    elif args.build == "plant":
        cases = [cases[1]]
    for label, planted in cases:
        existing_cases[label] = run_case(
            label, planted, args.lambda_int, args.dps, args.min_n, args.max_n, sigmas, args.window
        )
    if args.build == "both":
        out["cases"] = [existing_cases["zeta"], existing_cases["plant"]]
    else:
        labels = ["zeta", "plant"]
        out["cases"] = [existing_cases[label] for label in labels if label in existing_cases]
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
