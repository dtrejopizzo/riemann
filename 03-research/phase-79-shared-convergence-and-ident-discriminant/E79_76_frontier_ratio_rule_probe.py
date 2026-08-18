#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "E79_75_pareto_frontier_reduction_results.json"
OUT = ROOT / "E79_76_frontier_ratio_rule_results.json"


def main():
    data = json.loads(SRC.read_text())
    rows_out = []

    for row in data["rows"]:
        frontier = row["frontier"]
        cands = row["candidates"]
        if len(frontier) != 2:
            rows_out.append(
                {
                    "N": row["N"],
                    "kind": "degenerate",
                    "frontier": frontier,
                    "best_rule": row["best_rule"],
                }
            )
            continue

        a, b = frontier
        ca, cb = cands[a], cands[b]
        if ca["surcharge"] <= cb["surcharge"]:
            low_name, low = a, ca
            high_name, high = b, cb
        else:
            low_name, low = b, cb
            high_name, high = a, ca

        delta_m = low["mismatch"] - high["mismatch"]
        delta_s = high["surcharge"] - low["surcharge"]
        ratio = None if delta_s == 0 else delta_m / delta_s

        rows_out.append(
            {
                "N": row["N"],
                "kind": "tradeoff" if delta_s != 0 and delta_m != 0 else "degenerate",
                "low": {"name": low_name, **low},
                "high": {"name": high_name, **high},
                "delta_mismatch": delta_m,
                "delta_surcharge": delta_s,
                "ratio": ratio,
                "best_rule": row["best_rule"],
                "winner_is_high": row["best_rule"] == high_name,
            }
        )

    result = {
        "statement": "E79.76 frontier ratio rule",
        "source": str(SRC),
        "rows": rows_out,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
