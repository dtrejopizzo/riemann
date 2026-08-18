#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "E79_76_frontier_ratio_rule_results.json"
OUT = ROOT / "E79_80_margin_extremum_autopsy_results.json"


def support_stats(support):
    start = support[0]
    card = len(support)
    span = support[-1] - support[0] + 1
    return start - card, span


def main():
    data = json.loads(SRC.read_text())
    rows = [row for row in data["rows"] if row["N"] in [10, 12, 16]]

    best = None
    current = None
    admissible_count = 0

    for ai in range(81):
        a = ai / 100.0
        for bi in range(81):
            b = bi / 100.0
            margins = []
            ok = True
            for row in rows:
                low = row["low"]
                high = row["high"]
                low_u, low_v = support_stats(low["support"])
                high_u, high_v = support_stats(high["support"])
                delta_cost = a * (high_u - low_u) + b * (high_v - low_v)
                delta_m = row["delta_mismatch"]
                margin = (delta_m - delta_cost) if row["winner_is_high"] else (delta_cost - delta_m)
                if margin <= 0:
                    ok = False
                    break
                margins.append(margin)
            if not ok:
                continue
            admissible_count += 1
            rec = {
                "a": a,
                "b": b,
                "min_margin": min(margins),
                "margins": margins,
            }
            if best is None or rec["min_margin"] > best["min_margin"]:
                best = rec
            if a == 0.36 and b == 0.14:
                current = rec

    result = {
        "statement": "E79.80 margin extremum autopsy",
        "source": str(SRC),
        "admissible_count": admissible_count,
        "best": best,
        "current": current,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
