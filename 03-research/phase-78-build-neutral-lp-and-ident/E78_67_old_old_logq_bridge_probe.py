#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
ALIGN = HERE / "E78_66_old_old_alignment_results.json"
PHASE_G = PHASE77 / "E77_5g_schur_phase_increment_results.json"
PHASE_AC = {
    "zeta": PHASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json",
    "plant": PHASE77 / "E77_5ac_theta_logderiv_coupling_plant.json",
}


def to_complex(obj: dict[str, str] | dict[str, float]) -> complex:
    return complex(float(obj["re"]), float(obj["im"]))


def load_old_q(path: Path) -> dict[tuple[str, int], complex]:
    obj = json.loads(path.read_text())
    out: dict[tuple[str, int], complex] = {}
    for case in obj["cases"]:
        for point in case["points"]:
            if point["tag"] != "old":
                continue
            out[(point["sigma"], int(point["section_N"]))] = to_complex(point["one_minus_theta"])
    return out


def load_delta_log(build_is_plant: bool) -> dict[tuple[str, int], complex]:
    obj = json.loads(PHASE_G.read_text())
    case = None
    for candidate in obj["cases"]:
        if bool(candidate["planted"]) == build_is_plant:
            case = candidate
            break
    assert case is not None
    out: dict[tuple[str, int], complex] = {}
    for inc in case["increments"]:
        n = int(inc["from_N"])
        for row in inc["sigmas"]:
            sigma = str(row["sigma"])
            if sigma not in ("1.0", "3.0"):
                continue
            out[(sigma, n)] = to_complex(row["delta_log_one_minus_theta"])
    return out


def build_rows(build: str, pair_rows: list[dict[str, object]]) -> dict[str, object]:
    q_old = load_old_q(PHASE_AC[build])
    delta_log = load_delta_log(build == "plant")
    rows = []
    max_q_error = 0.0
    max_pair_error = 0.0
    for row in pair_rows:
        sigma = str(row["sigma"])
        n = int(row["N"])
        if (sigma, n) not in q_old or (sigma, n + 2) not in q_old or (sigma, n) not in delta_log:
            continue
        qn = q_old[(sigma, n)]
        qm = q_old[(sigma, n + 2)]
        dlog = delta_log[(sigma, n)]
        reconstructed_qm = qn * cmath.exp(-dlog)
        q_err = abs(qm - reconstructed_qm)
        pairnum = float(row["pairnum_from_cocycle"])
        pair_reconstructed = (abs(qn) ** 2) * (1 - cmath.exp(-dlog)).real
        pair_err = abs(pairnum - pair_reconstructed)
        max_q_error = max(max_q_error, q_err)
        max_pair_error = max(max_pair_error, pair_err)
        rows.append(
            {
                "sigma": sigma,
                "N": n,
                "to_N": n + 2,
                "delta_log_one_minus_theta": {"re": dlog.real, "im": dlog.imag},
                "q_next_error": q_err,
                "pairnum_from_alignment": pairnum,
                "pairnum_from_logq": pair_reconstructed,
                "pairnum_error": pair_err,
            }
        )
    return {
        "rows": rows,
        "max_q_next_error": max_q_error,
        "max_pairnum_error": max_pair_error,
    }


def main() -> None:
    align = json.loads(ALIGN.read_text())
    result = {
        "statement": (
            "Old-old log-q bridge: if Delta ell_N = log q_N - log q_{N+2}, then "
            "q_{N+2}=q_N exp(-Delta ell_N) and PAIRNUM_N = |q_N|^2 Re(1-exp(-Delta ell_N))."
        ),
        "sources": {
            "alignment": str(ALIGN),
            "phase_g": str(PHASE_G),
            "theta_zeta": str(PHASE_AC["zeta"]),
            "theta_plant": str(PHASE_AC["plant"]),
        },
        "builds": {
            "zeta": build_rows("zeta", align["builds"]["zeta"]["rows"]),
            "plant": build_rows("plant", align["builds"]["plant"]["rows"]),
        },
    }
    out_path = HERE / "E78_67_old_old_logq_bridge_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
