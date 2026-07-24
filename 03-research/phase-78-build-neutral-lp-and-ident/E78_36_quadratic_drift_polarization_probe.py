#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_35_eps_quadratic_results.json"


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def sub(a, b):
    return [a[0] - b[0], a[1] - b[1]]


def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def scale(c, a):
    return [c * a[0], c * a[1]]


def main():
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Exact polarization of the quadratic-defect drift into normalized "
            "theta-prime and rotated normalized denominator contributions"
        ),
        "source": str(SRC),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = [r for r in payload["rows"] if r["tag"] == "new"]
        by_sigma = {}
        for row in rows:
            by_sigma.setdefault(row["sigma"], []).append(row)

        out_rows = []
        max_reconstruction_error = 0.0
        max_den_over_num = 0.0
        for sigma, sigma_rows in by_sigma.items():
            sigma_rows.sort(key=lambda r: r["section_N"])
            for old, new in zip(sigma_rows, sigma_rows[1:]):
                m_old = sub(old["a_hat"], old["j_b_hat"])
                m_new = sub(new["a_hat"], new["j_b_hat"])
                m_avg = scale(0.5, add(m_old, m_new))
                delta_a = sub(new["a_hat"], old["a_hat"])
                delta_jb = sub(new["j_b_hat"], old["j_b_hat"])
                delta_m = sub(delta_a, delta_jb)

                lhs = new["quadratic_defect"] - old["quadratic_defect"]
                num_term = dot(m_avg, delta_a)
                den_term = -dot(m_avg, delta_jb)
                rhs = num_term + den_term
                err = abs(lhs - rhs)
                max_reconstruction_error = max(max_reconstruction_error, err)
                den_over_num = abs(den_term) / abs(num_term) if abs(num_term) else None
                if den_over_num is not None:
                    max_den_over_num = max(max_den_over_num, den_over_num)

                out_rows.append(
                    {
                        "sigma": sigma,
                        "N": old["section_N"],
                        "to_N": new["section_N"],
                        "old_quadratic_defect": old["quadratic_defect"],
                        "new_quadratic_defect": new["quadratic_defect"],
                        "delta_quadratic_defect": lhs,
                        "numerator_direction_term": num_term,
                        "denominator_direction_term": den_term,
                        "reconstructed_delta": rhs,
                        "reconstruction_error": err,
                        "abs_den_over_abs_num": den_over_num,
                    }
                )

        result["builds"][build] = {
            "rows": out_rows,
            "max_reconstruction_error": max_reconstruction_error,
            "max_abs_den_over_abs_num": max_den_over_num,
        }

    out_path = HERE / "E78_36_quadratic_drift_polarization_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
