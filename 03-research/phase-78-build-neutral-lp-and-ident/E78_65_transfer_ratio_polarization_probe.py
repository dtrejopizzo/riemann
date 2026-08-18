#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
PAIRNUM = HERE / "E78_63_pairnum_ternary_results.json"
THETA = {
    "zeta": PHASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json",
    "plant": PHASE77 / "E77_5ac_theta_logderiv_coupling_plant.json",
}


def to_complex(obj: dict[str, str] | dict[str, float]) -> complex:
    return complex(float(obj["re"]), float(obj["im"]))


def load_points(path: Path) -> dict[tuple[str, int, str], complex]:
    obj = json.loads(path.read_text())
    out: dict[tuple[str, int, str], complex] = {}
    for case in obj["cases"]:
        for point in case["points"]:
            out[(point["sigma"], int(point["section_N"]), point["tag"])] = to_complex(point["one_minus_theta"])
    return out


def build_rows(points: dict[tuple[str, int, str], complex], pair_rows: list[dict[str, object]]) -> dict[str, object]:
    rows = []
    max_error = 0.0
    for row in pair_rows:
        sigma = str(row["sigma"])
        n = int(row["N"])
        m = int(row["to_N"])
        old_q = points[(sigma, n, "old")]
        new_q = points[(sigma, m, "new")]
        reconstructed = 0.5 * (abs(old_q) ** 2 - abs(new_q) ** 2 + abs(old_q - new_q) ** 2)
        pairnum = float(row["pairnum"])
        err = abs(reconstructed - pairnum)
        max_error = max(max_error, err)
        rows.append(
            {
                "sigma": sigma,
                "N": n,
                "to_N": m,
                "old_q_abs": abs(old_q),
                "new_q_abs": abs(new_q),
                "delta_q_abs": abs(old_q - new_q),
                "reconstructed_pairnum": reconstructed,
                "pairnum": pairnum,
                "reconstruction_error": err,
            }
        )
    return {"rows": rows, "max_reconstruction_error": max_error}


def main() -> None:
    pair = json.loads(PAIRNUM.read_text())
    result = {
        "statement": (
            "Exact transfer-ratio polarization for PAIRNUM_N: with q_N := 1-theta_N = T_N/t0_N, "
            "PAIRNUM_N = (|q_N|^2 - |q_{N+2}|^2 + |q_N-q_{N+2}|^2)/2."
        ),
        "sources": {
            "pairnum": str(PAIRNUM),
            "theta_zeta": str(THETA["zeta"]),
            "theta_plant": str(THETA["plant"]),
        },
        "builds": {
            "zeta": build_rows(load_points(THETA["zeta"]), pair["builds"]["zeta"]["rows"]),
            "plant": build_rows(load_points(THETA["plant"]), pair["builds"]["plant"]["rows"]),
        },
    }
    out_path = HERE / "E78_65_transfer_ratio_polarization_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
