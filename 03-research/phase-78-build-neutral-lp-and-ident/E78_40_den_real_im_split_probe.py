#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_39_den_quotient_skew_results.json"


def main():
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Real-imag split for denominator quotient skew: positive real floor "
            "plus small imaginary part imply phase rigidity"
        ),
        "source": str(SRC),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = []
        min_re = None
        max_abs_im = 0.0
        max_phase_upper = 0.0
        for row in payload["rows"]:
            qre = row["quotient_re"]
            qim = row["quotient_im"]
            re_floor = min(1.0, qre) if qre > 0 else 0.0
            skew_upper = abs(qim) / re_floor if re_floor > 0 else math.inf
            phase = row["abs_phase_step"]
            max_phase_upper = max(max_phase_upper, skew_upper if math.isfinite(skew_upper) else 0.0)
            min_re = qre if min_re is None else min(min_re, qre)
            max_abs_im = max(max_abs_im, abs(qim))
            rows.append(
                {
                    **row,
                    "re_floor_against_one": re_floor,
                    "phase_upper_from_real_im": skew_upper,
                    "upper_gap": (skew_upper - phase) if math.isfinite(skew_upper) else math.inf,
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "min_quotient_re": min_re,
            "max_abs_quotient_im": max_abs_im,
            "max_phase_upper_from_real_im": max_phase_upper,
        }

    out_path = HERE / "E78_40_den_real_im_split_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
