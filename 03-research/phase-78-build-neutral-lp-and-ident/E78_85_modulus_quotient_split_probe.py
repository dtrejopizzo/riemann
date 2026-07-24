#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
POLAR = HERE / "E78_32_delta_safeu_polar_results.json"
QUOT = HERE / "E78_83_weighted_quotient_results.json"


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def main() -> None:
    polar_rows = {
        (row["sigma"], int(row["N"])): row
        for row in json.loads(POLAR.read_text())["builds"]["zeta"]["rows"]
    }
    quot_rows = json.loads(QUOT.read_text())["rows"]

    rows = []
    errors = []
    factors = []
    shares = []
    relangs = []
    for row in quot_rows:
        key = (row["sigma"], int(row["N"]))
        p = polar_rows.get(key)
        if p is None:
            continue
        modulus_quot = row["minus_SAFEDELTA"] / p["modulus_term"]
        factor = p["modulus_share_of_delta"]
        reconstructed = modulus_quot * factor
        err = abs(reconstructed - row["quotient"])
        rows.append(
            {
                "sigma": row["sigma"],
                "N": int(row["N"]),
                "quotient": row["quotient"],
                "modulus_quotient": modulus_quot,
                "angular_den_factor": factor,
                "modulus_share_of_delta": p["modulus_share_of_delta"],
                "relative_angular_correction": p["relative_angular_correction"],
                "reconstructed_quotient": reconstructed,
                "reconstruction_error": err,
            }
        )
        errors.append(err)
        factors.append(factor)
        shares.append(p["modulus_share_of_delta"])
        relangs.append(p["relative_angular_correction"])

    result = {
        "statement": (
            "Exact split of the endpoint quotient into a modulus quotient and an angular denominator factor."
        ),
        "sources": {
            "polar_delta_safeu": str(POLAR),
            "weighted_quotient": str(QUOT),
        },
        "rows": rows,
        "max_reconstruction_error": max(errors) if errors else None,
        "summary": {
            "modulus_share_of_delta": summarize(shares),
            "relative_angular_correction": summarize(relangs),
            "angular_den_factor": summarize(factors),
        },
    }
    out_path = HERE / "E78_85_modulus_quotient_split_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
