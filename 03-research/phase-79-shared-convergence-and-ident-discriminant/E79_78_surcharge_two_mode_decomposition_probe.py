#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "E79_76_frontier_ratio_rule_results.json"
OUT = ROOT / "E79_78_surcharge_two_mode_decomposition_results.json"


def support_stats(support):
    start = support[0]
    card = len(support)
    span = support[-1] - support[0] + 1
    return start, card, span


def main():
    data = json.loads(SRC.read_text())
    rows_out = []

    for row in data["rows"]:
        if row["kind"] != "tradeoff":
            continue

        low = row["low"]
        high = row["high"]
        lstart, lcard, lspan = support_stats(low["support"])
        hstart, hcard, hspan = support_stats(high["support"])

        d_anchor_minus_mass = (hstart - hcard) - (lstart - lcard)
        d_span = hspan - lspan
        recomposed = 0.36 * d_anchor_minus_mass + 0.14 * d_span

        rows_out.append(
            {
                "N": row["N"],
                "low": low,
                "high": high,
                "delta_surcharge": row["delta_surcharge"],
                "delta_anchor_minus_mass": d_anchor_minus_mass,
                "delta_span": d_span,
                "anchor_minus_mass_contribution": 0.36 * d_anchor_minus_mass,
                "span_contribution": 0.14 * d_span,
                "recomposed_delta_surcharge": recomposed,
            }
        )

    result = {
        "statement": "E79.78 surcharge two-mode decomposition",
        "source": str(SRC),
        "rows": rows_out,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
