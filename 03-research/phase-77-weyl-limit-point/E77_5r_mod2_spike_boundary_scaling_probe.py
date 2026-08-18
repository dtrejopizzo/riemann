#!/usr/bin/env python3
"""E77.5r physical boundary scaling audit for the mod-2 spike."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def run(q_path: Path, lam: float):
    L = 2.0 * math.log(lam)
    factor = 2.0 * math.pi / L
    data = json.loads(q_path.read_text(encoding="ascii"))
    out = {
        "statement": "Physical boundary scaling audit d_N=2*pi*N/L",
        "source": str(q_path),
        "lambda": lam,
        "L": L,
        "d_factor": factor,
        "cases": [],
    }
    for case in data["cases"]:
        profiles = []
        for prof in case["profiles"]:
            classes = {}
            for cls, clsdata in prof["classes"].items():
                scaled_q = []
                for q in clsdata["Q_values"]:
                    n = q["N"]
                    d_n = factor * n
                    # Since d_N is proportional to N at fixed lambda, this
                    # explicitly verifies whether physical scaling changes
                    # the mod-4 spike.  The normalized value removes the
                    # constant factor from N^2.
                    scaled_q.append(
                        {
                            "N": n,
                            "d_N": d_n,
                            "Q_N": q["value"],
                            "Q_d": q["value"] / (factor * factor),
                        }
                    )
                qd_vals = [x["Q_d"] for x in scaled_q]
                classes[cls] = {
                    "Qd_first": qd_vals[0] if qd_vals else None,
                    "Qd_last": qd_vals[-1] if qd_vals else None,
                    "Qd_range": max(qd_vals) - min(qd_vals) if qd_vals else None,
                    "scaled_Q": scaled_q,
                }
            profiles.append({"sigma": prof["sigma"], "classes": classes})
        out["cases"].append({"label": case["label"], "profiles": profiles})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=Path, default=HERE / "E77_5q_mod4_drift_split_results.json")
    parser.add_argument("--lambda", dest="lam", type=float, default=6.0)
    parser.add_argument("--output", type=Path, default=HERE / "E77_5r_mod2_spike_boundary_scaling_results.json")
    args = parser.parse_args()
    result = run(args.q, args.lam)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"L={result['L']:.12g} d_factor={result['d_factor']:.12g}")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for p in case["profiles"]:
            if p["sigma"] in {"1.0", "3.0"}:
                bits = []
                for cls in sorted(p["classes"]):
                    c = p["classes"][cls]
                    bits.append(f"mod{cls}:Qd {c['Qd_first']:.5g}->{c['Qd_last']:.5g} range={c['Qd_range']:.5g}")
                print(f"SIGMA {p['sigma']} " + " | ".join(bits), flush=True)
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
