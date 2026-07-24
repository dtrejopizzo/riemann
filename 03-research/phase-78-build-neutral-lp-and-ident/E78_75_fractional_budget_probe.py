#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "E78_74_reserve_budget_results.json"


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def build_rows(rows: list[dict[str, float | int | str]]) -> dict[str, object]:
    out = []
    tail_ratios = []
    phase_ratios = []
    total_ratios = []
    slack_ratios = []
    for row in rows:
        base = float(row["basepoint_reserve"])
        tail = float(row["tail_loss"])
        phase_sq = float(row["wrapped_phase_square"])
        margin = float(row["reserve_margin"])
        tail_ratio = tail / base
        phase_ratio = phase_sq / base
        total_ratio = (tail + phase_sq) / base
        slack_ratio = margin / base
        out.append(
            {
                "sigma": row["sigma"],
                "N": int(row["N"]),
                "to_N": int(row["to_N"]),
                "tail_ratio": tail_ratio,
                "phase_square_ratio": phase_ratio,
                "consumption_ratio": total_ratio,
                "slack_ratio": slack_ratio,
            }
        )
        tail_ratios.append(tail_ratio)
        phase_ratios.append(phase_ratio)
        total_ratios.append(total_ratio)
        slack_ratios.append(slack_ratio)
    return {
        "rows": out,
        "summary": {
            "tail_ratio": summarize(tail_ratios),
            "phase_square_ratio": summarize(phase_ratios),
            "consumption_ratio": summarize(total_ratios),
            "slack_ratio": summarize(slack_ratios),
        },
        "max_budget_identity_error": max(
            abs(
                row["slack_ratio"] - (1.0 - row["consumption_ratio"])
            )
            for row in out
        ),
    }


def main() -> None:
    obj = json.loads(SOURCE.read_text())
    result = {
        "statement": (
            "Fractional reserve criterion: "
            "(TAIL+phase^2)/BASE < 1 iff reserve margin is positive, "
            "with slack ratio = 1 - consumption ratio."
        ),
        "source": str(SOURCE),
        "builds": {
            build: build_rows(data["rows"])
            for build, data in obj["builds"].items()
        },
    }
    out_path = HERE / "E78_75_fractional_budget_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
