#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
COCYCLE = PHASE77 / "E77_5i_schur_cocycle_cell_results.json"
THETA = {
    "zeta": PHASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json",
    "plant": PHASE77 / "E77_5ac_theta_logderiv_coupling_plant.json",
}


def to_complex(obj: dict[str, str] | dict[str, float]) -> complex:
    return complex(float(obj["re"]), float(obj["im"]))


def load_denominators(path: Path) -> dict[tuple[str, int], complex]:
    obj = json.loads(path.read_text())
    out: dict[tuple[str, int], complex] = {}
    for case in obj["cases"]:
        for point in case["points"]:
            sigma = point["sigma"]
            n = int(point["section_N"])
            out[(f"{sigma}|{point['tag']}", n)] = complex(
                float(point["one_minus_theta"]["re"]),
                float(point["one_minus_theta"]["im"]),
            )
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
                    "A": to_complex(row["A_tau"]),
                    "B": to_complex(row["B_v"]),
                    "C": to_complex(row["C_core"]),
                }
    return out


def build_rows(planted: bool, dens: dict[tuple[str, int], complex], cocycle: dict[tuple[bool, str, int], dict[str, complex]]) -> dict[str, object]:
    rows = []
    max_error = 0.0
    for sigma in ("1.0", "3.0"):
        for n in (8, 10, 12, 14, 16, 18, 20):
            key = (planted, sigma, n)
            den_key = (f"{sigma}|old", n)
            if key not in cocycle or den_key not in dens:
                continue
            d = dens[den_key]
            t = cocycle[key]["A"] + cocycle[key]["B"] + cocycle[key]["C"]
            lhs = (-(t / d)).real
            numerator = -(t * d.conjugate()).real
            rhs = numerator / (abs(d) ** 2)
            err = abs(lhs - rhs)
            max_error = max(max_error, err)
            rows.append(
                {
                    "sigma": sigma,
                    "N": n,
                    "to_N": n + 2,
                    "real_normalized_cocycle": lhs,
                    "pairing_numerator": numerator,
                    "positive_denominator": abs(d) ** 2,
                    "reconstructed_real_cocycle": rhs,
                    "reconstruction_error": err,
                }
            )
    return {"rows": rows, "max_reconstruction_error": max_error}


def main() -> None:
    cocycle = load_cocycle_rows()
    result = {
        "statement": (
            "Exact coupled-pairing formula for the real normalized ternary cocycle: "
            "Re(-(A+B+C)/(1-theta)) = -Re((A+B+C) conj(1-theta)) / |1-theta|^2."
        ),
        "sources": {
            "cocycle": str(COCYCLE),
            "theta_zeta": str(THETA["zeta"]),
            "theta_plant": str(THETA["plant"]),
        },
        "builds": {
            "zeta": build_rows(False, load_denominators(THETA["zeta"]), cocycle),
            "plant": build_rows(True, load_denominators(THETA["plant"]), cocycle),
        },
    }
    out_path = HERE / "E78_62_real_coupled_pairing_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
