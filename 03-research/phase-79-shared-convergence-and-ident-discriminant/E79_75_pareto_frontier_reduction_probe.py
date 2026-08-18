#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "E79_70_linear_penalized_matching_rule_results.json"
OUT = ROOT / "E79_75_pareto_frontier_reduction_results.json"


def surcharge(cand):
    return -0.22 * cand["cardinality"] + 0.14 * cand["gaps"] + 0.36 * cand["start"]


def dominates(a, b):
    ma, sa = a["mismatch"], a["surcharge"]
    mb, sb = b["mismatch"], b["surcharge"]
    return (ma <= mb and sa <= sb) and (ma < mb or sa < sb)


def main():
    data = json.loads(SRC.read_text())
    rows_out = []
    all_two_point = True

    for row in data["rows"]:
        cands = {}
        for name, cand in row["candidates"].items():
            cands[name] = {
                "support": cand["support"],
                "mismatch": cand["mismatch"],
                "surcharge": surcharge(cand),
                "score": cand["score"],
                "exact_match": cand["exact_match"],
            }

        dominated = {}
        frontier = []
        for name, cand in cands.items():
            dom_by = [other for other, oc in cands.items() if other != name and dominates(oc, cand)]
            dominated[name] = dom_by
            if not dom_by:
                frontier.append(name)

        frontier.sort(key=lambda name: (cands[name]["surcharge"], cands[name]["mismatch"], name))
        if len(frontier) > 2:
            all_two_point = False

        rows_out.append(
            {
                "N": row["N"],
                "target_support": row["target_support"],
                "frontier": frontier,
                "dominated": dominated,
                "candidates": cands,
                "best_rule": row["best_rule"]["name"],
            }
        )

    result = {
        "statement": "E79.75 Pareto frontier reduction",
        "source": str(SRC),
        "summary": {
            "num_rows": len(rows_out),
            "all_rows_reduce_to_at_most_two_frontier_points": all_two_point,
        },
        "rows": rows_out,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
