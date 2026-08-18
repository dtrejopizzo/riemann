#!/usr/bin/env python3

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
E69 = ROOT / "E79_69_relational_matching_selector_results.json"
E76 = ROOT / "E79_76_frontier_ratio_rule_results.json"
OUT = ROOT / "E79_77_sigma_rigid_excess_factor_results.json"


def infer_extra(row, sigma_key):
    best = None
    for picks in itertools.product([0, 1], repeat=3):
        xs = []
        for fam, pick in zip(["suffix", "pair", "triple"], picks):
            cand = row[fam]
            packet = cand[sigma_key]
            mismatch = cand["mismatch"]
            xs.append(packet * (1 - mismatch) if pick == 0 else packet / (1 - mismatch))
        spread = max(xs) - min(xs)
        if best is None or spread < best[0]:
            best = (spread, xs)
    return sum(best[1]) / 3.0


def main():
    d69 = json.loads(E69.read_text())
    d76 = json.loads(E76.read_text())
    rows69 = {row["N"]: row for row in d69["rows"]}

    rows_out = []
    for row in d76["rows"]:
        if row["N"] not in rows69:
            continue
        r69 = rows69[row["N"]]
        extra1 = infer_extra(r69, "packet_sigma1")
        extra2 = infer_extra(r69, "packet_sigma2")

        candidates = []
        for name in sorted({row.get("low", {}).get("name"), row.get("high", {}).get("name")} - {None}):
            cand = r69[name]
            eps1 = cand["packet_sigma1"] / extra1 - 1.0
            eps2 = cand["packet_sigma2"] / extra2 - 1.0
            candidates.append(
                {
                    "name": name,
                    "packet_sigma1": cand["packet_sigma1"],
                    "packet_sigma2": cand["packet_sigma2"],
                    "eps_sigma1": eps1,
                    "eps_sigma2": eps2,
                    "rigidity_defect": abs(eps1 - eps2),
                    "mismatch": cand["mismatch"],
                }
            )

        rows_out.append(
            {
                "N": row["N"],
                "kind": row["kind"],
                "extra_sigma1": extra1,
                "extra_sigma2": extra2,
                "candidates": candidates,
            }
        )

    result = {
        "statement": "E79.77 sigma-rigid excess factor",
        "sources": [str(E69), str(E76)],
        "rows": rows_out,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
