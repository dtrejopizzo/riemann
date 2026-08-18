#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
COCYCLE = PHASE77 / "E77_5i_schur_cocycle_cell_results.json"
THETA = {
    "zeta": PHASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json",
    "plant": PHASE77 / "E77_5ac_theta_logderiv_coupling_plant.json",
}


def load_denominators(path: Path) -> dict[tuple[str, int], complex]:
    obj = json.loads(path.read_text())
    out: dict[tuple[str, int], complex] = {}
    for case in obj["cases"]:
        for point in case["points"]:
            sigma = point["sigma"]
            section_n = int(point["section_N"])
            tag = point["tag"]
            one_minus_theta = complex(
                float(point["one_minus_theta"]["re"]),
                float(point["one_minus_theta"]["im"]),
            )
            out[(sigma, section_n)] = one_minus_theta
            out[(f"{sigma}|{tag}", section_n)] = one_minus_theta
    return out


def load_cocycle_rows() -> dict[tuple[bool, str, int], dict[str, complex]]:
    obj = json.loads(COCYCLE.read_text())
    out: dict[tuple[bool, str, int], dict[str, complex]] = {}
    for case in obj["cases"]:
        planted = bool(case["planted"])
        for inc in case["increments"]:
            from_n = int(inc["from_N"])
            for row in inc["sigmas"]:
                sigma = str(row["sigma"])
                out[(planted, sigma, from_n)] = {
                    "delta": to_complex(row["delta_theta"]),
                    "A": to_complex(row["A_tau"]),
                    "B": to_complex(row["B_v"]),
                    "C": to_complex(row["C_core"]),
                }
    return out


def to_complex(obj: dict[str, str] | dict[str, float]) -> complex:
    return complex(float(obj["re"]), float(obj["im"]))


def ratio(num: float, den: float) -> float | None:
    if abs(den) < 1e-30:
        return None
    return num / abs(den)


def summarize(rows: list[dict[str, object]]) -> dict[str, float | int | None]:
    def collect(key: str) -> list[float]:
        return [float(r[key]) for r in rows if r[key] is not None]

    def stats(values: list[float]) -> dict[str, float | int | None]:
        if not values:
            return {"count": 0, "min": None, "median": None, "max": None}
        vals = sorted(values)
        mid = len(vals) // 2
        median = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
        return {"count": len(vals), "min": vals[0], "median": median, "max": vals[-1]}

    return {
        "max_real_part_over_realw": stats(collect("max_real_part_over_realw")),
        "best_real_pair_over_realw": stats(collect("best_real_pair_over_realw")),
        "max_signed_part_over_realw": stats(collect("max_signed_part_over_realw")),
        "best_signed_pair_over_realw": stats(collect("best_signed_pair_over_realw")),
    }


def build_rows(build: str, planted: bool, dens: dict[tuple[str, int], complex], cocycle: dict[tuple[bool, str, int], dict[str, complex]]) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    common_sigmas = ("1.0", "3.0")
    common_ns = (8, 10, 12, 14, 16, 18, 20)

    max_reconstruction_error = 0.0
    for sigma in common_sigmas:
        for n in common_ns:
            key = (planted, sigma, n)
            den_key = (f"{sigma}|old", n)
            if key not in cocycle or den_key not in dens:
                continue
            den = dens[den_key]
            A = -cocycle[key]["A"] / den
            B = -cocycle[key]["B"] / den
            C = -cocycle[key]["C"] / den
            w = A + B + C
            recon_error = abs(w + cocycle[key]["delta"] / den)
            max_reconstruction_error = max(max_reconstruction_error, recon_error)

            real_w = w.real
            real_A = A.real
            real_B = B.real
            real_C = C.real
            pair_reals = {
                "AB": (A + B).real,
                "AC": (A + C).real,
                "BC": (B + C).real,
            }
            signed_parts = [abs(real_A), abs(real_B), abs(real_C)]
            signed_pairs = [abs(v) for v in pair_reals.values()]

            rows.append(
                {
                    "sigma": sigma,
                    "N": n,
                    "to_N": n + 2,
                    "Re_w": real_w,
                    "Im_w": w.imag,
                    "abs_w": abs(w),
                    "Re_A_star": real_A,
                    "Re_B_star": real_B,
                    "Re_C_star": real_C,
                    "Re_AB_star": pair_reals["AB"],
                    "Re_AC_star": pair_reals["AC"],
                    "Re_BC_star": pair_reals["BC"],
                    "max_real_part_over_realw": ratio(max(signed_parts), real_w),
                    "best_real_pair_over_realw": ratio(min(signed_pairs), real_w),
                    "max_signed_part_over_realw": ratio(max(signed_parts), real_w),
                    "best_signed_pair_over_realw": ratio(min(signed_pairs), real_w),
                    "reconstruction_error": recon_error,
                }
            )

    return {
        "rows": rows,
        "summary": summarize(rows),
        "max_reconstruction_error": max_reconstruction_error,
    }


def main() -> None:
    cocycle = load_cocycle_rows()
    result = {
        "statement": (
            "Real-part audit of the normalized ternary cocycle: "
            "w_N = -(A_N+B_N+C_N)/(1-theta_N), with the denominator core controlled by Re(w_N)."
        ),
        "sources": {
            "cocycle": str(COCYCLE),
            "theta_zeta": str(THETA["zeta"]),
            "theta_plant": str(THETA["plant"]),
        },
        "builds": {
            "zeta": build_rows("zeta", False, load_denominators(THETA["zeta"]), cocycle),
            "plant": build_rows("plant", True, load_denominators(THETA["plant"]), cocycle),
        },
    }

    out_path = HERE / "E78_61_real_normalized_ternary_cocycle_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
