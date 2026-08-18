#!/usr/bin/env python3
"""E79.48 - affine sigma-template audit for the first-packet residual."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "E79_44_multisigma_coupled_packet_results.json"
SIGMAS = [0.75, 1.0, 1.5, 2.0]


def affine_fit(xs, ys):
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    den = n * sxx - sx * sx
    a = (n * sxy - sx * sy) / den
    b = (sy - a * sx) / n
    return a, b


def fit_errors(xs, ys, a, b):
    fit = [a * x + b for x in xs]
    errs = [y - f for y, f in zip(ys, fit)]
    scale = max(abs(y) for y in ys) or 1.0
    max_abs = max(abs(e) for e in errs)
    rms = (sum(e * e for e in errs) / len(errs)) ** 0.5
    return fit, errs, max_abs / scale, rms / scale


def endpoint_line(xs, ys):
    a = (ys[-1] - ys[0]) / (xs[-1] - xs[0])
    b = ys[0] - a * xs[0]
    return a, b


def main():
    data = json.loads(SRC.read_text())
    out = {"statement": "E79.48 affine sigma-template audit", "source": str(SRC), "cases": []}
    for case in data["cases"]:
        rows = []
        for row in case["rows"]:
            rules = [v for v in row["rules"].values() if v["aggregator"] == "mean"]
            best = min(rules, key=lambda v: float(v["mean_mismatch"]))
            ys = [float(best["mismatches"][str(s)]) for s in SIGMAS]
            a_ls, b_ls = affine_fit(SIGMAS, ys)
            fit_ls, errs_ls, max_ls, rms_ls = fit_errors(SIGMAS, ys, a_ls, b_ls)
            a_ep, b_ep = endpoint_line(SIGMAS, ys)
            fit_ep, errs_ep, max_ep, rms_ep = fit_errors(SIGMAS, ys, a_ep, b_ep)
            rows.append(
                {
                    "N": row["N"],
                    "support_abs": best["support_abs"],
                    "mismatches": {str(s): best["mismatches"][str(s)] for s in SIGMAS},
                    "least_squares": {
                        "slope": a_ls,
                        "intercept": b_ls,
                        "fit": fit_ls,
                        "errors": errs_ls,
                        "normalized_max_error": max_ls,
                        "normalized_rms_error": rms_ls,
                    },
                    "endpoint": {
                        "slope": a_ep,
                        "intercept": b_ep,
                        "fit": fit_ep,
                        "errors": errs_ep,
                        "normalized_max_error": max_ep,
                        "normalized_rms_error": rms_ep,
                    },
                }
            )
        out["cases"].append({"label": case["label"], "rows": rows})

    out_path = HERE / "E79_48_affine_sigma_template_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    for case in out["cases"]:
        print(case["label"])
        for row in case["rows"]:
            ls = row["least_squares"]
            ep = row["endpoint"]
            print(
                f" N={row['N']:2d} ls_max={ls['normalized_max_error']:.6g} "
                f"ls_rms={ls['normalized_rms_error']:.6g} "
                f"ep_max={ep['normalized_max_error']:.6g} "
                f"support={row['support_abs']}"
            )
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
