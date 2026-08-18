#!/usr/bin/env python3
"""E77.5af normalized sector margin drift audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def run(input_path: Path):
    data = json.loads(input_path.read_text(encoding="ascii"))
    result = {"statement": "Normalized cone margin drift", "source": str(input_path), "cases": []}
    for case in data["cases"]:
        profiles = []
        worst = None
        for prof in case["profiles"]:
            rows = prof["rows"]
            vals = [r["cone_normalized"] for r in rows]
            row_worst = min(rows, key=lambda r: r["cone_normalized"])
            if worst is None or row_worst["cone_normalized"] < worst["cone_normalized"]:
                worst = {"sigma": prof["sigma"], "mod4": prof["mod4"], **row_worst}
            drift = vals[-1] - vals[0]
            profiles.append(
                {
                    "sigma": prof["sigma"],
                    "mod4": prof["mod4"],
                    "first_margin": vals[0],
                    "last_margin": vals[-1],
                    "min_margin": min(vals),
                    "max_margin": max(vals),
                    "drift": drift,
                    "relative_drift": drift / vals[0] if vals[0] else float("inf"),
                    "rows": [{"N": r["N"], "margin": r["cone_normalized"]} for r in rows],
                }
            )
        result["cases"].append({"label": case["label"], "profiles": profiles, "worst_row": worst})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=HERE / "E77_5ae_sector_certificate_results.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5af_normalized_sector_margin_results.json")
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for prof in case["profiles"]:
            print(
                f"SIGMA {prof['sigma']} mod{prof['mod4']} "
                f"margin={prof['first_margin']:.9g}->{prof['last_margin']:.9g} "
                f"min={prof['min_margin']:.9g} relDrift={prof['relative_drift']:.9g}",
                flush=True,
            )
        w = case["worst_row"]
        print(
            f"WORST sigma={w['sigma']} mod{w['mod4']} N={w['N']} "
            f"margin={w['cone_normalized']:.9g}",
            flush=True,
        )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
