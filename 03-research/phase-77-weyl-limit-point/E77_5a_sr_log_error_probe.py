#!/usr/bin/env python3
"""E77.5a SR-LOG-ERR probe.

This is the first IDENT-facing probe after E77.3c.  It keeps the
two-generator expression coupled and measures the safe logarithmic
derivative error by sigma, including an N=20 core extension.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from E77_3c_two_generator_ident_probe import GAMMA, run_case, serial


HERE = Path(__file__).resolve().parent


def log_fit(ns: list[int], vals: list[mp.mpf]) -> dict | None:
    if len(ns) < 3:
        return None
    nbar = mp.fsum(ns) / len(ns)
    logs = [mp.log(v) for v in vals]
    ybar = mp.fsum(logs) / len(logs)
    denom = mp.fsum((n - nbar) ** 2 for n in ns)
    slope = mp.fsum((n - nbar) * (y - ybar) for n, y in zip(ns, logs)) / denom
    return {"c": serial(slope), "points": len(ns)}


def add_sigma_fits(case: dict) -> None:
    sigmas = [row["sigma"] for row in case["rows"][0]["sigmas"]]
    fits = {}
    ns = [row["N"] for row in case["rows"]]
    max_errors = [mp.mpf(row["max_zeta_target_relative_error"]) for row in case["rows"]]
    fits["max_error"] = log_fit(ns, max_errors)
    for idx, sigma in enumerate(sigmas):
        vals = [mp.mpf(row["sigmas"][idx]["target_relative_error"]) for row in case["rows"]]
        fits[f"sigma_{sigma}"] = log_fit(ns, vals)
    case["error_fits"] = fits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5a_sr_log_error_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.5a requires dps >= 50")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "SR-LOG-ERR coupled two-generator measurement",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(s) for s in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for label, planted in [
        (f"zeta-lam{args.lam}", None),
        (f"plant-lam{args.lam}", (GAMMA, "0.30", "5.0")),
    ]:
        print(f"BUILD {label}", flush=True)
        case = run_case(label, args.lam, args.max_modes, args.dps, sigmas, planted)
        add_sigma_fits(case)
        result["cases"].append(case)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
