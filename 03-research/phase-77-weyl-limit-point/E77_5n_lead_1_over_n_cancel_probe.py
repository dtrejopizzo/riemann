#!/usr/bin/env python3
"""E77.5n leading 1/N coefficient audit for LOG-EXT-RATIO."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def fnum(x: str | float) -> float:
    return float(x)


def run(input_path: Path):
    data = json.loads(input_path.read_text(encoding="ascii"))
    result = {
        "statement": "Leading 1/N coefficient by sigma for R_N=Delta external-Delta logT",
        "source": str(input_path),
        "cases": [],
    }
    for case in data["cases"]:
        rows = []
        by_sigma: dict[str, list[dict]] = {}
        for inc in case["increments"]:
            n = inc["from_N"]
            sigma_rows = []
            for row in inc["sigmas"]:
                sigma = row["sigma"]
                ext = fnum(row["external_tail_delta"])
                logt = fnum(row["logt_safe_delta"])
                residual = ext - logt
                # The max table used absolute residual.  Here keep the signed
                # residual so the coefficient profile can reveal cancellations.
                coeff = n * residual
                coeff2 = n * n * residual
                item = {
                    "sigma": sigma,
                    "residual": residual,
                    "external": ext,
                    "logt": logt,
                    "coeff_N_residual": coeff,
                    "coeff_N2_residual": coeff2,
                    "residual_over_external": residual / ext if ext else float("inf"),
                }
                sigma_rows.append(item)
                by_sigma.setdefault(sigma, []).append({"N": n, **item})
            coeffs = [r["coeff_N_residual"] for r in sigma_rows]
            abs_coeffs = [abs(c) for c in coeffs]
            rows.append(
                {
                    "from_N": n,
                    "to_N": inc["to_N"],
                    "max_abs_coeff_N_residual": max(abs_coeffs),
                    "min_coeff_N_residual": min(coeffs),
                    "max_coeff_N_residual": max(coeffs),
                    "sigma_rows": sigma_rows,
                }
            )
        sigma_profiles = []
        for sigma, values in by_sigma.items():
            coeffs = [v["coeff_N_residual"] for v in values]
            diffs = [coeffs[j + 1] - coeffs[j] for j in range(len(coeffs) - 1)]
            sigma_profiles.append(
                {
                    "sigma": sigma,
                    "first_coeff": coeffs[0],
                    "last_coeff": coeffs[-1],
                    "range_coeff": max(coeffs) - min(coeffs),
                    "last_delta_coeff": diffs[-1] if diffs else None,
                    "max_abs_delta_coeff": max((abs(d) for d in diffs), default=0.0),
                    "values": values,
                }
            )
        result["cases"].append(
            {
                "label": case["label"],
                "rows": rows,
                "sigma_profiles": sigma_profiles,
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=HERE / "E77_5l_logt_cell_update_results.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5n_lead_1_over_n_cancel_results.json")
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for prof in case["sigma_profiles"]:
            print(
                f"SIGMA {prof['sigma']:>4s} first={prof['first_coeff']:.9g} "
                f"last={prof['last_coeff']:.9g} range={prof['range_coeff']:.9g} "
                f"lastDelta={prof['last_delta_coeff']:.9g}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
