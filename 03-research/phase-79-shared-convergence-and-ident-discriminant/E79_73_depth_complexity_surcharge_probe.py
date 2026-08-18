#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "E79_70_linear_penalized_matching_rule_results.json"
OUT = ROOT / "E79_73_depth_complexity_surcharge_results.json"


def score(cand):
    mismatch = cand["mismatch"]
    surcharge = (
        -0.22 * cand["cardinality"]
        + 0.14 * cand["gaps"]
        + 0.36 * cand["start"]
    )
    return mismatch + surcharge, mismatch, surcharge


def main():
    data = json.loads(SRC.read_text())
    rows_out = []
    exact = 0

    for row in data["rows"]:
        cands = []
        for name, cand in row["candidates"].items():
            total, mismatch, surcharge = score(cand)
            cands.append(
                {
                    "name": name,
                    "support": cand["support"],
                    "score": total,
                    "mismatch": mismatch,
                    "surcharge": surcharge,
                    "size_cost": -0.22 * cand["cardinality"],
                    "spread_cost": 0.14 * cand["gaps"],
                    "delay_cost": 0.36 * cand["start"],
                }
            )
        cands.sort(key=lambda rec: rec["score"])
        best = cands[0]
        is_exact = best["support"] == row["target_support"]
        exact += int(is_exact)
        rows_out.append(
            {
                "N": row["N"],
                "target_support": row["target_support"],
                "best": best,
                "exact": is_exact,
                "candidates": cands,
                "hard_margin_vs_second": cands[1]["score"] - cands[0]["score"],
            }
        )

    result = {
        "statement": "E79.73 mismatch plus depth-complexity surcharge",
        "source": str(SRC),
        "exact_match_count": exact,
        "rows": rows_out,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
