#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_44_den_centered_quotient_results.json"


def main() -> None:
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Quadratic radial increment residual for the denominator shell: "
            "|1+w_N|<1 iff 2 Re(w_N)+|w_N|^2<0."
        ),
        "source": str(SRC),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = []
        max_reconstruction_error = 0.0
        for row in payload["rows"]:
            w_re = row["centered_quotient_re"]
            w_im = row["centered_quotient_im"]
            w_abs_sq = w_re * w_re + w_im * w_im
            quadratic_residual = 2.0 * w_re + w_abs_sq
            reconstructed = (1.0 + w_re) ** 2 + w_im * w_im - 1.0
            err = abs(quadratic_residual - reconstructed)
            max_reconstruction_error = max(max_reconstruction_error, err)
            rows.append(
                {
                    **row,
                    "centered_quotient_abs_sq": w_abs_sq,
                    "quadratic_radial_residual": quadratic_residual,
                    "reconstructed_from_unit_gap": reconstructed,
                    "reconstruction_error": err,
                    "negative_quadratic_margin": -quadratic_residual,
                }
            )

        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max_reconstruction_error,
        }

    out_path = HERE / "E78_50_den_quadratic_radial_increment_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
