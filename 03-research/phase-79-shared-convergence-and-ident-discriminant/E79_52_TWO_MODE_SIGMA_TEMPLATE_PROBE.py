#!/usr/bin/env python3
"""E79.52 - minimal two-mode sigma template audit.

Fit the first-packet residual with

    residual(sigma; N) ~ a_N sigma + b_N + g_N q(sigma),

where q(sigma) = (sigma-sigma_c)^2 and sigma_c is fixed at the midpoint of the
audited safe grid.
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "E79_44_multisigma_coupled_packet_results.json"
SIGMAS = [0.75, 1.0, 1.5, 2.0]
SIGMA_C = (SIGMAS[0] + SIGMAS[-1]) / 2.0


def solve3(mat, rhs):
    a = [row[:] for row in mat]
    b = rhs[:]
    n = 3
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[piv] = a[piv], a[i]
        b[i], b[piv] = b[piv], b[i]
        pivv = a[i][i]
        for j in range(i, n):
            a[i][j] /= pivv
        b[i] /= pivv
        for r in range(n):
            if r == i:
                continue
            fac = a[r][i]
            for j in range(i, n):
                a[r][j] -= fac * a[i][j]
            b[r] -= fac * b[i]
    return b


def least_squares_three(xs, ys):
    feats = [[x, 1.0, (x - SIGMA_C) ** 2] for x in xs]
    gram = [[0.0] * 3 for _ in range(3)]
    rhs = [0.0] * 3
    for f, y in zip(feats, ys):
        for i in range(3):
            rhs[i] += f[i] * y
            for j in range(3):
                gram[i][j] += f[i] * f[j]
    return solve3(gram, rhs)


def fit_errors(xs, ys, coeffs):
    a, b, g = coeffs
    fit = [a * x + b + g * (x - SIGMA_C) ** 2 for x in xs]
    errs = [y - f for y, f in zip(ys, fit)]
    scale = max(abs(y) for y in ys) or 1.0
    max_abs = max(abs(e) for e in errs)
    rms = (sum(e * e for e in errs) / len(errs)) ** 0.5
    return fit, errs, max_abs / scale, rms / scale


def main():
    data = json.loads(SRC.read_text())
    out = {
        "statement": "E79.52 minimal two-mode sigma template audit",
        "source": str(SRC),
        "sigma_center": SIGMA_C,
        "cases": [],
    }
    for case in data["cases"]:
        rows = []
        for row in case["rows"]:
            rules = [v for v in row["rules"].values() if v["aggregator"] == "mean"]
            best = min(rules, key=lambda v: float(v["mean_mismatch"]))
            ys = [float(best["mismatches"][str(s)]) for s in SIGMAS]
            coeffs = least_squares_three(SIGMAS, ys)
            fit, errs, max_err, rms_err = fit_errors(SIGMAS, ys, coeffs)
            rows.append(
                {
                    "N": row["N"],
                    "support_abs": best["support_abs"],
                    "mismatches": {str(s): best["mismatches"][str(s)] for s in SIGMAS},
                    "coefficients": {
                        "slope": coeffs[0],
                        "intercept": coeffs[1],
                        "curvature_mode": coeffs[2],
                    },
                    "fit": fit,
                    "errors": errs,
                    "normalized_max_error": max_err,
                    "normalized_rms_error": rms_err,
                    "scaled_curvature_abs": row["N"] * row["N"] * abs(coeffs[2]),
                }
            )
        out["cases"].append({"label": case["label"], "rows": rows})

    out_path = HERE / "E79_52_two_mode_sigma_template_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    for case in out["cases"]:
        print(case["label"])
        for row in case["rows"]:
            c = row["coefficients"]["curvature_mode"]
            print(
                f" N={row['N']:2d} max={row['normalized_max_error']:.6g} "
                f"rms={row['normalized_rms_error']:.6g} "
                f"g={c:.6g} N2|g|={row['scaled_curvature_abs']:.6g}"
            )
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
