#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
E70 = ROOT / "E79_70_linear_penalized_matching_rule_results.json"
OUT = ROOT / "E79_71_sign_pattern_robustness_results.json"


BASE = {
    "mismatch": 1.0,
    "cardinality": -1.0,
    "span": 0.78,
    "gaps": -0.64,
    "start": 0.36,
}

TARGET_SIGNS = {
    "cardinality": -1,
    "span": 1,
    "gaps": -1,
    "start": 1,
}


def score(coeffs, cand):
    return (
        coeffs["mismatch"] * cand["mismatch"]
        + coeffs["cardinality"] * cand["cardinality"]
        + coeffs["span"] * cand["span"]
        + coeffs["gaps"] * cand["gaps"]
        + coeffs["start"] * cand["start"]
    )


def exact_count(rows, coeffs):
    exact = 0
    picks = {}
    for row in rows:
        vals = []
        for name, cand in row["candidates"].items():
            vals.append((score(coeffs, cand), name, cand["support"]))
        vals.sort()
        best = vals[0]
        ok = best[2] == row["target_support"]
        exact += int(ok)
        picks[row["N"]] = {"name": best[1], "support": best[2], "exact": ok}
    return exact, picks


def main():
    e70 = json.loads(E70.read_text())
    rows = e70["rows"]

    # Small coordinate box around E79.70
    around = []
    good = []
    sign_preserving_total = 0
    sign_preserving_good = 0
    for dc in [i / 100 for i in range(-130, -69, 5)]:
        for sp in [i / 100 for i in range(55, 101, 5)]:
            for gp in [i / 100 for i in range(-90, -39, 5)]:
                for st in [i / 100 for i in range(15, 56, 5)]:
                    coeffs = {
                        "mismatch": 1.0,
                        "cardinality": dc,
                        "span": sp,
                        "gaps": gp,
                        "start": st,
                    }
                    signs = {
                        "cardinality": -1 if dc < 0 else (1 if dc > 0 else 0),
                        "span": -1 if sp < 0 else (1 if sp > 0 else 0),
                        "gaps": -1 if gp < 0 else (1 if gp > 0 else 0),
                        "start": -1 if st < 0 else (1 if st > 0 else 0),
                    }
                    sign_ok = signs == TARGET_SIGNS
                    if sign_ok:
                        sign_preserving_total += 1
                    exact, picks = exact_count(rows, coeffs)
                    rec = {
                        "coefficients": coeffs,
                        "sign_pattern": signs,
                        "sign_preserving": sign_ok,
                        "exact_match_count": exact,
                        "picks": picks,
                    }
                    around.append(rec)
                    if exact == len(rows):
                        good.append(rec)
                        if sign_ok:
                            sign_preserving_good += 1

    around.sort(key=lambda r: (-r["exact_match_count"], -int(r["sign_preserving"])))

    result = {
        "statement": "E79.71 local robustness around the E79.70 sign pattern",
        "source": str(E70),
        "base_coefficients": BASE,
        "target_sign_pattern": TARGET_SIGNS,
        "grid_summary": {
            "total_points": len(around),
            "exact_5_of_5_points": len(good),
            "sign_preserving_points": sign_preserving_total,
            "sign_preserving_exact_5_of_5_points": sign_preserving_good,
        },
        "examples_exact": good[:25],
        "top_configs": around[:25],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
