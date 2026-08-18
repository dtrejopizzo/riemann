#!/usr/bin/env python3
"""E77.5q mod-4 split for coefficient/drift hierarchy."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def run(coeff_path: Path, q_path: Path):
    coeff = json.loads(coeff_path.read_text(encoding="ascii"))
    qdata = json.loads(q_path.read_text(encoding="ascii"))
    out = {
        "statement": "Mod-4 split for C_N, D_N, Q_N profiles",
        "coeff_source": str(coeff_path),
        "q_source": str(q_path),
        "cases": [],
    }
    for case, qcase in zip(coeff["cases"], qdata["cases"]):
        profiles = []
        for prof, qprof in zip(case["sigma_profiles"], qcase["profiles"]):
            by_class = {}
            for v in prof["values"]:
                cls = str(v["N"] % 4)
                by_class.setdefault(cls, {"C": [], "Q": []})
                by_class[cls]["C"].append({"N": v["N"], "value": v["coeff_N_residual"]})
            for q in qprof["values"]:
                cls = str(q["from_N"] % 4)
                by_class.setdefault(cls, {"C": [], "Q": []})
                by_class[cls]["Q"].append({"N": q["from_N"], "value": q["Q"]})
            classes = {}
            for cls, vals in by_class.items():
                cvals = [x["value"] for x in vals["C"]]
                qvals = [x["value"] for x in vals["Q"]]
                classes[cls] = {
                    "C_first": cvals[0] if cvals else None,
                    "C_last": cvals[-1] if cvals else None,
                    "C_range": max(cvals) - min(cvals) if cvals else None,
                    "Q_first": qvals[0] if qvals else None,
                    "Q_last": qvals[-1] if qvals else None,
                    "Q_range": max(qvals) - min(qvals) if qvals else None,
                    "C_values": vals["C"],
                    "Q_values": vals["Q"],
                }
            profiles.append({"sigma": prof["sigma"], "classes": classes})
        out["cases"].append({"label": case["label"], "profiles": profiles})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coeff", type=Path, default=HERE / "E77_5n_lead_1_over_n_cancel_results.json")
    parser.add_argument("--q", type=Path, default=HERE / "E77_5p_second_coeff_results.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5q_mod4_drift_split_results.json")
    args = parser.parse_args()
    result = run(args.coeff, args.q)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for p in case["profiles"]:
            if p["sigma"] in {"1.0", "2.0", "3.0"}:
                bits = []
                for cls in sorted(p["classes"]):
                    c = p["classes"][cls]
                    bits.append(
                        f"mod{cls}:C {c['C_first']:.4g}->{c['C_last']:.4g} "
                        f"Qr={c['Q_range']:.4g}"
                    )
                print(f"SIGMA {p['sigma']} " + " | ".join(bits), flush=True)
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
