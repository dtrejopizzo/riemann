#!/usr/bin/env python3
"""E77.5c cofinal SR-LOG-2SCALE probe.

Run explicit (lambda, Nmax) pairs and measure the coupled two-generator
SR-LOG-ERR.  This avoids the fixed-N trap diagnosed in E77.5b.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from E77_3c_two_generator_ident_probe import GAMMA, run_case, serial


HERE = Path(__file__).resolve().parent


def log_fit(xs: list[mp.mpf], ys: list[mp.mpf]) -> dict | None:
    if len(xs) < 3:
        return None
    xbar = mp.fsum(xs) / len(xs)
    logs = [mp.log(y) for y in ys]
    ybar = mp.fsum(logs) / len(logs)
    denom = mp.fsum((x - xbar) ** 2 for x in xs)
    if denom == 0:
        return None
    slope = mp.fsum((x - xbar) * (y - ybar) for x, y in zip(xs, logs)) / denom
    return {"slope": serial(slope), "points": len(xs)}


def parse_pairs(text: str) -> list[tuple[int, int]]:
    pairs = []
    for item in text.split(","):
        item = item.strip()
        if not item:
            continue
        lam, nmax = item.split(":")
        pairs.append((int(lam), int(nmax)))
    return pairs


def final_row(case: dict) -> dict:
    row = case["rows"][-1]
    return {
        "label": case["label"],
        "lambda": case["lambda"],
        "N": row["N"],
        "N_over_L": serial(mp.mpf(row["N"]) / (2 * mp.log(case["lambda"]))),
        "planted": case["planted"],
        "energy": row["energy"],
        "max_error": row["max_zeta_target_relative_error"],
        "identity_error": row["max_two_generator_identity_error"],
        "a_abs": row["a_abs"],
        "b_abs": row["b_abs"],
        "sigma_errors": [
            {"sigma": s["sigma"], "target_relative_error": s["target_relative_error"]}
            for s in row["sigmas"]
        ],
    }


def add_summary(result: dict) -> None:
    finals = result["final_rows"]
    zeta = [r for r in finals if r["planted"] is None]
    plant = [r for r in finals if r["planted"] is not None]
    for rows, key in [(zeta, "zeta"), (plant, "planted")]:
        xs_nl = [mp.mpf(r["N_over_L"]) for r in rows]
        xs_l = [mp.log(mp.mpf(r["lambda"])) for r in rows]
        ys = [mp.mpf(r["max_error"]) for r in rows]
        result["summary"][key] = {
            "log_error_vs_N_over_L": log_fit(xs_nl, ys),
            "log_error_vs_log_lambda": log_fit(xs_l, ys),
            "endpoint_errors": rows,
        }
    if zeta and plant:
        result["summary"]["separation"] = [
            {
                "lambda": z["lambda"],
                "N": z["N"],
                "plant_over_zeta_error": serial(mp.mpf(p["max_error"]) / mp.mpf(z["max_error"])),
            }
            for z, p in zip(zeta, plant)
        ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", default="6:20,7:20,8:20")
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5c_cofinal_sr_log_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.5c requires dps >= 50")
    pairs = parse_pairs(args.pairs)
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Cofinal SR-LOG-2SCALE grid",
        "parameters": {
            "pairs": [{"lambda": lam, "Nmax": nmax} for lam, nmax in pairs],
            "dps": args.dps,
            "sigmas": [serial(s) for s in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
        "final_rows": [],
        "summary": {},
    }
    for lam, nmax in pairs:
        for label, planted in [
            (f"zeta-lam{lam}-n{nmax}", None),
            (f"plant-lam{lam}-n{nmax}", (GAMMA, "0.30", "5.0")),
        ]:
            print(f"BUILD {label}", flush=True)
            case = run_case(label, lam, nmax, args.dps, sigmas, planted)
            result["cases"].append(case)
            result["final_rows"].append(final_row(case))
            add_summary(result)
            args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
