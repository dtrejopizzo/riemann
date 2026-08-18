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


def ratio(num: float, den: float) -> float | None:
    if abs(den) < 1e-30:
        return None
    return abs(num) / abs(den)


def stats(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def build_rows(planted: bool, dens: dict[tuple[str, int], complex], cocycle: dict[tuple[bool, str, int], dict[str, complex]]) -> dict[str, object]:
    rows = []
    max_reconstruction_error = 0.0

    for sigma in ("1.0", "3.0"):
        for n in (8, 10, 12, 14, 16, 18, 20):
            key = (planted, sigma, n)
            den_key = (f"{sigma}|old", n)
            if key not in cocycle or den_key not in dens:
                continue
            d = dens[den_key]
            A = cocycle[key]["A"]
            B = cocycle[key]["B"]
            C = cocycle[key]["C"]

            pA = -(A * d.conjugate()).real
            pB = -(B * d.conjugate()).real
            pC = -(C * d.conjugate()).real
            total = pA + pB + pC
            pairAB = pA + pB
            pairAC = pA + pC
            pairBC = pB + pC
            recon_err = abs(total + ((A + B + C) * d.conjugate()).real)
            max_reconstruction_error = max(max_reconstruction_error, recon_err)

            rows.append(
                {
                    "sigma": sigma,
                    "N": n,
                    "to_N": n + 2,
                    "pairnum": total,
                    "pair_A": pA,
                    "pair_B": pB,
                    "pair_C": pC,
                    "pair_AB": pairAB,
                    "pair_AC": pairAC,
                    "pair_BC": pairBC,
                    "max_part_over_total": ratio(max(abs(pA), abs(pB), abs(pC)), total),
                    "best_pair_over_total": ratio(min(abs(pairAB), abs(pairAC), abs(pairBC)), total),
                    "reconstruction_error": recon_err,
                }
            )

    parts = [r["max_part_over_total"] for r in rows if r["max_part_over_total"] is not None]
    pairs = [r["best_pair_over_total"] for r in rows if r["best_pair_over_total"] is not None]

    return {
        "rows": rows,
        "summary": {
            "max_part_over_total": stats(parts),
            "best_pair_over_total": stats(pairs),
        },
        "max_reconstruction_error": max_reconstruction_error,
    }


def main() -> None:
    cocycle = load_cocycle_rows()
    result = {
        "statement": (
            "Ternary audit for PAIRNUM_N = -Re((A_N+B_N+C_N) conj(1-theta_N))."
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
    out_path = HERE / "E78_63_pairnum_ternary_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
