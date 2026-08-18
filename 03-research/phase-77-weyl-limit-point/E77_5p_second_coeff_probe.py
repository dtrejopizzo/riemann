#!/usr/bin/env python3
"""E77.5p second coefficient diagnostics for profile drift."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def run(input_path: Path):
    data = json.loads(input_path.read_text(encoding="ascii"))
    out = {
        "statement": "Second coefficient Q_N=N^2(C_N-C_{N+2}) diagnostics",
        "source": str(input_path),
        "cases": [],
    }
    for case in data["cases"]:
        profiles = []
        for profile in case["profiles"]:
            drifts = profile["drifts"]
            q_values = []
            for d in drifts:
                q_values.append(
                    {
                        "from_N": d["from_N"],
                        "to_N": d["to_N"],
                        "Q": d["N2_drift"],
                        "abs_Q": abs(d["N2_drift"]),
                    }
                )
            q_deltas = [q_values[j + 1]["Q"] - q_values[j]["Q"] for j in range(len(q_values) - 1)]
            local_slopes = []
            for prev, cur in zip(q_values, q_values[1:]):
                if prev["abs_Q"] > 0 and cur["abs_Q"] > 0:
                    local_slopes.append(
                        math.log(cur["abs_Q"] / prev["abs_Q"]) / math.log(cur["from_N"] / prev["from_N"])
                    )
            profiles.append(
                {
                    "sigma": profile["sigma"],
                    "first_Q": q_values[0]["Q"] if q_values else None,
                    "last_Q": q_values[-1]["Q"] if q_values else None,
                    "range_Q": (max(q["Q"] for q in q_values) - min(q["Q"] for q in q_values)) if q_values else None,
                    "last_delta_Q": q_deltas[-1] if q_deltas else None,
                    "max_abs_delta_Q": max((abs(x) for x in q_deltas), default=0.0),
                    "tail_local_slope": local_slopes[-1] if local_slopes else None,
                    "values": q_values,
                }
            )
        out["cases"].append({"label": case["label"], "profiles": profiles})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=HERE / "E77_5o_profile_drift_results.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5p_second_coeff_results.json")
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for p in case["profiles"]:
            print(
                f"SIGMA {p['sigma']:>4s} firstQ={p['first_Q']:.9g} "
                f"lastQ={p['last_Q']:.9g} rangeQ={p['range_Q']:.9g} "
                f"lastDeltaQ={p['last_delta_Q']:.9g}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
