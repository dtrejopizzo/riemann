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


def load_old_points(path: Path) -> dict[tuple[str, int], dict[str, complex]]:
    obj = json.loads(path.read_text())
    out: dict[tuple[str, int], dict[str, complex]] = {}
    for case in obj["cases"]:
        for point in case["points"]:
            if point["tag"] != "old":
                continue
            key = (point["sigma"], int(point["section_N"]))
            out[key] = {
                "theta": to_complex(point["theta"]),
                "one_minus_theta": to_complex(point["one_minus_theta"]),
            }
    return out


def load_cocycle_rows() -> dict[tuple[bool, str, int], complex]:
    obj = json.loads(COCYCLE.read_text())
    out: dict[tuple[bool, str, int], complex] = {}
    for case in obj["cases"]:
        planted = bool(case["planted"])
        for inc in case["increments"]:
            n = int(inc["from_N"])
            for row in inc["sigmas"]:
                sigma = str(row["sigma"])
                out[(planted, sigma, n)] = to_complex(row["total"])
    return out


def build_rows(planted: bool, points: dict[tuple[str, int], dict[str, complex]], cocycle: dict[tuple[bool, str, int], complex]) -> dict[str, object]:
    rows = []
    max_theta_error = 0.0
    max_pairnum_error = 0.0
    for sigma in ("1.0", "3.0"):
        for n in (8, 10, 12, 14, 16, 18, 20):
            key = (planted, sigma, n)
            if key not in cocycle or (sigma, n) not in points or (sigma, n + 2) not in points:
                continue
            total = cocycle[key]
            theta_old = points[(sigma, n)]["theta"]
            theta_next_old = points[(sigma, n + 2)]["theta"]
            q_old = points[(sigma, n)]["one_minus_theta"]
            q_next_old = points[(sigma, n + 2)]["one_minus_theta"]
            aligned_delta = theta_old - theta_next_old
            pairnum = (-(total * q_old.conjugate())).real
            polarized = 0.5 * (abs(q_old) ** 2 - abs(q_next_old) ** 2 + abs(q_old - q_next_old) ** 2)
            theta_err = abs(total - aligned_delta)
            pairnum_err = abs(pairnum - polarized)
            max_theta_error = max(max_theta_error, theta_err)
            max_pairnum_error = max(max_pairnum_error, pairnum_err)
            rows.append(
                {
                    "sigma": sigma,
                    "N": n,
                    "to_N": n + 2,
                    "delta_theta_cocycle": {"re": total.real, "im": total.imag},
                    "delta_theta_old_old": {"re": aligned_delta.real, "im": aligned_delta.imag},
                    "theta_alignment_error": theta_err,
                    "pairnum_from_cocycle": pairnum,
                    "pairnum_from_old_old_polarization": polarized,
                    "pairnum_alignment_error": pairnum_err,
                }
            )
    return {
        "rows": rows,
        "max_theta_alignment_error": max_theta_error,
        "max_pairnum_alignment_error": max_pairnum_error,
    }


def main() -> None:
    cocycle = load_cocycle_rows()
    result = {
        "statement": (
            "Old-old alignment of the E77.5i cocycle with the stored E77.5ac shell rows, "
            "and consequent exact polarization formula for PAIRNUM on the old-old chain."
        ),
        "sources": {
            "cocycle": str(COCYCLE),
            "theta_zeta": str(THETA["zeta"]),
            "theta_plant": str(THETA["plant"]),
        },
        "builds": {
            "zeta": build_rows(False, load_old_points(THETA["zeta"]), cocycle),
            "plant": build_rows(True, load_old_points(THETA["plant"]), cocycle),
        },
    }
    out_path = HERE / "E78_66_old_old_alignment_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
