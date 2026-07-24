#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
PHASE_G = PHASE77 / "E77_5g_schur_phase_increment_results.json"


def to_complex(obj: dict[str, str] | dict[str, float]) -> complex:
    return complex(float(obj["re"]), float(obj["im"]))


def load_sections(build_is_plant: bool) -> dict[tuple[str, int], complex]:
    obj = json.loads(PHASE_G.read_text())
    case = None
    for candidate in obj["cases"]:
        if bool(candidate["planted"]) == build_is_plant:
            case = candidate
            break
    assert case is not None
    out: dict[tuple[str, int], complex] = {}
    for sec in case["sections"]:
        n = int(sec["N"])
        for row in sec["sigmas"]:
            sigma = str(row["sigma"])
            out[(sigma, n)] = to_complex(row["theta"])
    return out


def load_base_rows(build_is_plant: bool) -> list[dict[str, object]]:
    obj = json.loads(PHASE_G.read_text())
    case = None
    for candidate in obj["cases"]:
        if bool(candidate["planted"]) == build_is_plant:
            case = candidate
            break
    assert case is not None
    rows = []
    for inc in case["increments"]:
        n = int(inc["from_N"])
        for row in inc["sigmas"]:
            if row["sigma"] == "0.550000000000000044408921":
                rows.append(
                    {
                        "sigma": row["sigma"],
                        "N": n,
                        "to_N": int(inc["to_N"]),
                        "re_delta_ell": float(row["delta_log_one_minus_theta"]["re"]),
                        "im_delta_ell": float(row["delta_log_one_minus_theta"]["im"]),
                    }
                )
    return rows


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def build_rows(build_is_plant: bool) -> dict[str, object]:
    thetas = load_sections(build_is_plant)
    rows = []
    max_error = 0.0
    ratios = []
    bases = []
    for row in load_base_rows(build_is_plant):
        sigma = row["sigma"]
        n = int(row["N"])
        m = int(row["to_N"])
        qn = abs(1 - thetas[(sigma, n)])
        qm = abs(1 - thetas[(sigma, m)])
        reconstructed = math.log(qn / qm)
        err = abs(reconstructed - float(row["re_delta_ell"]))
        max_error = max(max_error, err)
        ratios.append(qn / qm)
        bases.append(float(row["re_delta_ell"]))
        rows.append(
            {
                "sigma": sigma,
                "N": n,
                "to_N": m,
                "re_delta_ell_base": float(row["re_delta_ell"]),
                "old_abs_one_minus_theta": qn,
                "next_abs_one_minus_theta": qm,
                "radial_ratio": qn / qm,
                "reconstructed_base": reconstructed,
                "reconstruction_error": err,
            }
        )
    return {
        "rows": rows,
        "summary": {
            "re_delta_ell_base": summarize(bases),
            "radial_ratio": summarize(ratios),
        },
        "max_reconstruction_error": max_error,
    }


def main() -> None:
    result = {
        "statement": (
            "Basepoint radial identity at sigma0=0.55: "
            "Re Delta ell_N(i sigma0) = log(|1-theta_old(N)| / |1-theta_old(N+2)|)."
        ),
        "sources": {"phase_g": str(PHASE_G)},
        "builds": {
            "zeta": build_rows(False),
            "plant": build_rows(True),
        },
    }
    out_path = HERE / "E78_73_basepoint_radial_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
