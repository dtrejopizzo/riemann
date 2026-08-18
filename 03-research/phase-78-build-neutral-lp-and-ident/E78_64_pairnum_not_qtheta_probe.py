#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
PAIRNUM = HERE / "E78_63_pairnum_ternary_results.json"


def stats(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def build_rows(build: str, pair_rows: list[dict[str, object]]) -> dict[str, object]:
    theta = json.loads((PHASE77 / f"E77_5ac_theta_logderiv_coupling_{build}.json").read_text())["cases"][0]
    deltas = {(r["sigma"], int(r["N"])): r for r in theta["deltas"]}
    qrows = {(r["sigma"], int(r["N"])): r for r in theta["qrows"]}

    rows = []
    pair_over_delta = []
    pair_over_qtheta = []
    for row in pair_rows:
        key = (row["sigma"], int(row["N"]))
        if key not in deltas or key not in qrows:
            continue
        pairnum = float(row["pairnum"])
        delta = float(deltas[key]["delta_u_safe"])
        qtheta = float(qrows[key]["Q_theta"])
        r1 = pairnum / delta if abs(delta) > 1e-30 else None
        r2 = pairnum / qtheta if abs(qtheta) > 1e-30 else None
        if r1 is not None:
            pair_over_delta.append(r1)
        if r2 is not None:
            pair_over_qtheta.append(r2)
        rows.append(
            {
                "sigma": row["sigma"],
                "N": row["N"],
                "to_N": row["to_N"],
                "pairnum": pairnum,
                "delta_safe_u": delta,
                "Q_theta": qtheta,
                "pairnum_over_delta_safe_u": r1,
                "pairnum_over_Q_theta": r2,
            }
        )
    return {
        "rows": rows,
        "summary": {
            "pairnum_over_delta_safe_u": stats(pair_over_delta),
            "pairnum_over_Q_theta": stats(pair_over_qtheta),
        },
    }


def main() -> None:
    pair = json.loads(PAIRNUM.read_text())
    result = {
        "statement": (
            "Audit that PAIRNUM_N = -Re((A+B+C) conj(1-theta_N)) is not a constant multiple "
            "of either Delta safe_u_N or Q_theta,N on the common certified ladder."
        ),
        "sources": {
            "pairnum": str(PAIRNUM),
            "theta_zeta": str(PHASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json"),
            "theta_plant": str(PHASE77 / "E77_5ac_theta_logderiv_coupling_plant.json"),
        },
        "builds": {
            "zeta": build_rows("zeta", pair["builds"]["zeta"]["rows"]),
            "plant": build_rows("plant", pair["builds"]["plant"]["rows"]),
        },
    }
    out_path = HERE / "E78_64_pairnum_not_qtheta_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
