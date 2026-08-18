#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_42_den_increment_area_results.json"


def main():
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Normalized directional form of the denominator increment area: "
            "det(Delta d_N,d_N) / (|Delta d_N| |d_N|)"
        ),
        "source": str(SRC),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = []
        max_abs_directional = 0.0
        for row in payload["rows"]:
            denom = row["delta_d_abs"] * row["old_d_abs"]
            directional = row["increment_area_numerator"] / denom if denom else math.nan
            angle = math.asin(max(-1.0, min(1.0, directional))) if math.isfinite(directional) else math.nan
            max_abs_directional = max(max_abs_directional, abs(directional))
            rows.append(
                {
                    **row,
                    "directional_increment_defect": directional,
                    "directional_increment_angle": angle,
                }
            )

        result["builds"][build] = {
            "rows": rows,
            "max_abs_directional_increment_defect": max_abs_directional,
        }

    out_path = HERE / "E78_43_den_directional_increment_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
