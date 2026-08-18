#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_36_quadratic_drift_polarization_results.json"
SRC35 = HERE / "E78_35_eps_quadratic_results.json"


def main():
    pol = json.loads(SRC.read_text())
    q35 = json.loads(SRC35.read_text())
    q35_map = {}
    for build, payload in q35["builds"].items():
        q35_map[build] = {}
        for row in payload["rows"]:
            if row["tag"] == "new":
                q35_map[build][(row["sigma"], row["section_N"])] = row["quadratic_defect"]

    result = {
        "statement": (
            "Cauchy control of denominator-direction drift by averaged "
            "misalignment size times normalized denominator direction increment"
        ),
        "sources": {
            "polarization": str(SRC),
            "quadratic_defect": str(SRC35),
        },
        "builds": {},
    }

    for build, payload in pol["builds"].items():
        rows = []
        max_ratio = 0.0
        for row in payload["rows"]:
            q_old = q35_map[build][(row["sigma"], row["N"])]
            q_new = q35_map[build][(row["sigma"], row["to_N"])]
            m_avg_norm = math.sqrt(q_old) + math.sqrt(q_new)
            dir_def = row["abs_den_over_abs_num"]  # placeholder overwritten below
            # Recover dir_def from half squared chord length of normalized denominator direction
            # using E78.35 data already encoded into E78.36 only through ratios, so re-open from q35 map not enough.
            # We instead infer delta_jb norm by polarization source if stored implicitly through exact identity:
            # DENDIR = -<m_avg, delta_jb>, hence |DENDIR| <= ||m_avg|| ||delta_jb||.
            # To certify with explicit ||delta_jb||, reconstruct it from denominator-direction term and ratio file?
            # Use the exact identity ||delta_jb|| = sqrt(2*dir_def), with dir_def recovered from
            # stored quotient in E78.36 unavailable. We will reload from the richer E78.35 file below.
            rows.append(
                {
                    **row,
                    "m_avg_norm_bound": m_avg_norm,
                }
            )

        # enrich with denominator direction chord data from E78.35
        qrows = [r for r in q35["builds"][build]["rows"] if r["tag"] == "new"]
        by_sigma = {}
        for r in qrows:
            by_sigma.setdefault(r["sigma"], []).append(r)
        dir_map = {}
        for sigma, arr in by_sigma.items():
            arr.sort(key=lambda r: r["section_N"])
            for old, new in zip(arr, arr[1:]):
                jb_old = old["j_b_hat"]
                jb_new = new["j_b_hat"]
                dx = jb_new[0] - jb_old[0]
                dy = jb_new[1] - jb_old[1]
                delta_norm = math.sqrt(dx * dx + dy * dy)
                dir_def = 0.5 * delta_norm * delta_norm
                dir_map[(sigma, old["section_N"], new["section_N"])] = (delta_norm, dir_def)

        enriched = []
        for row in rows:
            delta_norm, dir_def = dir_map[(row["sigma"], row["N"], row["to_N"])]
            cauchy_bound = row["m_avg_norm_bound"] * delta_norm
            ratio = abs(row["denominator_direction_term"]) / cauchy_bound if cauchy_bound else 0.0
            max_ratio = max(max_ratio, ratio)
            enriched.append(
                {
                    **row,
                    "den_direction_chord_norm": delta_norm,
                    "den_direction_quadratic_defect": dir_def,
                    "cauchy_bound": cauchy_bound,
                    "bound_utilization": ratio,
                }
            )

        result["builds"][build] = {
            "rows": enriched,
            "max_bound_utilization": max_ratio,
        }

    out_path = HERE / "E78_37_den_direction_control_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
