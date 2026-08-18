#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_47_den_radial_contraction_results.json"


def main() -> None:
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Normalized squared radial drop of the denominator norm: "
            "(|d_N|^2-|d_{N+2}|^2)/|d_N|^2 = (1-|q_N|)(1+|q_N|)."
        ),
        "source": str(SRC),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = []
        max_reconstruction_error = 0.0
        for row in payload["rows"]:
            old_sq = row["old_den_abs"] ** 2
            new_sq = row["new_den_abs"] ** 2
            normalized_sq_drop = (old_sq - new_sq) / old_sq
            reconstructed = row["radial_deficit"] * (1.0 + row["quotient_abs"])
            err = abs(normalized_sq_drop - reconstructed)
            max_reconstruction_error = max(max_reconstruction_error, err)
            rows.append(
                {
                    **row,
                    "old_den_abs_sq": old_sq,
                    "new_den_abs_sq": new_sq,
                    "normalized_squared_drop": normalized_sq_drop,
                    "reconstructed_from_radial_deficit": reconstructed,
                    "reconstruction_error": err,
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max_reconstruction_error,
        }

    out_path = HERE / "E78_48_den_squared_radial_drop_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
