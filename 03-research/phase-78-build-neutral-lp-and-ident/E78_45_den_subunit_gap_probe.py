#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC_Q = HERE / "E78_40_den_real_im_split_results.json"
SRC_W = HERE / "E78_44_den_centered_quotient_results.json"


def main() -> None:
    qsrc = json.loads(SRC_Q.read_text())
    wsrc = json.loads(SRC_W.read_text())

    result = {
        "statement": (
            "Subunit real-gap form of denominator horizontality: "
            "1-Re(q_N) = -Re(Delta d_N/d_N), with skew measured by "
            "|Im(q_N)|/(1-Re(q_N))."
        ),
        "sources": {
            "q": str(SRC_Q),
            "w": str(SRC_W),
        },
        "builds": {},
    }

    for build in ("zeta", "plant"):
        qrows = {(row["sigma"], row["N"]): row for row in qsrc["builds"][build]["rows"]}
        rows = []
        max_gap_identity_error = 0.0
        max_skew_identity_error = 0.0

        for wrow in wsrc["builds"][build]["rows"]:
            key = (wrow["sigma"], wrow["N"])
            qrow = qrows[key]
            gap = 1.0 - qrow["quotient_re"]
            gap_identity_error = abs(gap + wrow["centered_quotient_re"])
            max_gap_identity_error = max(max_gap_identity_error, gap_identity_error)

            skew_to_gap = abs(qrow["quotient_im"]) / gap if gap > 0 else None
            if skew_to_gap is not None and wrow["im_over_neg_re"] == wrow["im_over_neg_re"]:
                max_skew_identity_error = max(
                    max_skew_identity_error,
                    abs(skew_to_gap - wrow["im_over_neg_re"]),
                )

            rows.append(
                {
                    "sigma": wrow["sigma"],
                    "N": wrow["N"],
                    "to_N": wrow["to_N"],
                    "quotient_re": qrow["quotient_re"],
                    "quotient_im": qrow["quotient_im"],
                    "subunit_gap": gap,
                    "centered_real_floor": -wrow["centered_quotient_re"],
                    "gap_identity_error": gap_identity_error,
                    "imag_over_gap": skew_to_gap,
                    "directional_increment_defect_abs": abs(wrow["directional_increment_defect"]),
                    "gap_skew_minus_directional": (
                        (skew_to_gap - abs(wrow["directional_increment_defect"]))
                        if skew_to_gap is not None
                        else None
                    ),
                }
            )

        result["builds"][build] = {
            "rows": rows,
            "max_gap_identity_error": max_gap_identity_error,
            "max_skew_identity_error": max_skew_identity_error,
        }

    out_path = HERE / "E78_45_den_subunit_gap_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
