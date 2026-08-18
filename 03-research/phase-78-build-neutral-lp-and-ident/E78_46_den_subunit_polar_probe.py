#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_40_den_real_im_split_results.json"


def summarize(values: list[float]) -> dict[str, float]:
    ordered = sorted(values)
    n = len(ordered)
    median = ordered[n // 2] if n % 2 == 1 else 0.5 * (ordered[n // 2 - 1] + ordered[n // 2])
    return {"min": ordered[0], "median": median, "max": ordered[-1]}


def main() -> None:
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Polar decomposition of the subunit denominator gap: "
            "1-Re(q_N) = (1-|q_N|) + |q_N|(1-cos(arg q_N))."
        ),
        "source": str(SRC),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = []
        modulus_terms = []
        angular_terms = []
        angular_shares = []
        max_reconstruction_error = 0.0

        for row in payload["rows"]:
            q = complex(row["quotient_re"], row["quotient_im"])
            mod = abs(q)
            arg = math.atan2(q.imag, q.real)
            gap = 1.0 - q.real
            modulus_term = 1.0 - mod
            angular_term = mod * (1.0 - math.cos(arg))
            reconstruction_error = abs(gap - (modulus_term + angular_term))
            max_reconstruction_error = max(max_reconstruction_error, reconstruction_error)

            angular_share = (angular_term / gap) if gap != 0 else math.nan

            rows.append(
                {
                    **row,
                    "quotient_abs": mod,
                    "quotient_arg": arg,
                    "subunit_gap": gap,
                    "modulus_gap_term": modulus_term,
                    "angular_gap_term": angular_term,
                    "angular_gap_share": angular_share,
                    "reconstruction_error": reconstruction_error,
                }
            )

            modulus_terms.append(modulus_term)
            angular_terms.append(angular_term)
            if math.isfinite(angular_share):
                angular_shares.append(angular_share)

        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max_reconstruction_error,
            "modulus_gap_term_stats": summarize(modulus_terms),
            "angular_gap_term_stats": summarize(angular_terms),
            "angular_gap_share_stats": summarize(angular_shares),
        }

    out_path = HERE / "E78_46_den_subunit_polar_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
