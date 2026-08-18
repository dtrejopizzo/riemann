#!/usr/bin/env python3
"""E77.5o profile drift diagnostics for C_N(sigma)=N R_N(sigma)."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def run(input_path: Path):
    data = json.loads(input_path.read_text(encoding="ascii"))
    out = {
        "statement": "Profile drift diagnostics for leading 1/N coefficient",
        "source": str(input_path),
        "cases": [],
    }
    for case in data["cases"]:
        profiles = []
        for profile in case["sigma_profiles"]:
            values = profile["values"]
            drifts = []
            prev = None
            for a, b in zip(values, values[1:]):
                n = a["N"]
                drift = a["coeff_N_residual"] - b["coeff_N_residual"]
                item = {
                    "from_N": n,
                    "to_N": b["N"],
                    "drift": drift,
                    "abs_drift": abs(drift),
                    "N_drift": n * drift,
                    "N2_drift": n * n * drift,
                }
                if prev is not None and abs(prev["drift"]) > 0 and abs(drift) > 0:
                    item["local_power_slope"] = math.log(abs(drift) / abs(prev["drift"])) / math.log(n / prev["from_N"])
                else:
                    item["local_power_slope"] = None
                drifts.append(item)
                prev = item
            profiles.append(
                {
                    "sigma": profile["sigma"],
                    "max_abs_drift": max((d["abs_drift"] for d in drifts), default=0.0),
                    "last_abs_drift": drifts[-1]["abs_drift"] if drifts else 0.0,
                    "last_N_drift": drifts[-1]["N_drift"] if drifts else 0.0,
                    "last_N2_drift": drifts[-1]["N2_drift"] if drifts else 0.0,
                    "drifts": drifts,
                }
            )
        out["cases"].append({"label": case["label"], "profiles": profiles})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=HERE / "E77_5n_lead_1_over_n_cancel_results.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5o_profile_drift_results.json")
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for p in case["profiles"]:
            print(
                f"SIGMA {p['sigma']:>4s} maxD={p['max_abs_drift']:.9g} "
                f"lastD={p['last_abs_drift']:.9g} lastN*D={p['last_N_drift']:.9g} "
                f"lastN2*D={p['last_N2_drift']:.9g}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
