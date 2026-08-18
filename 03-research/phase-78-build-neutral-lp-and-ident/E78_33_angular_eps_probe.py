#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_json(name: str):
    return json.loads((HERE / name).read_text())


def main():
    src = load_json("E78_32_delta_safeu_polar_results.json")
    result = {
        "statement": (
            "Exact epsilon-drift form of the angular correction: "
            "angular_N = 2 |u_N| (eps_N - eps_N+2), eps_N = 1 - Im(u_N)/|u_N|"
        ),
        "source": str(HERE / "E78_32_delta_safeu_polar_results.json"),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = []
        max_rel_ang_over_mod = 0.0
        for row in payload["rows"]:
            eps_old = 1.0 - row["old_im_share"]
            eps_new = 1.0 - row["new_im_share"]
            eps_drift = eps_old - eps_new
            reconstructed = 2.0 * row["old_abs_u"] * eps_drift
            rel_ang_over_mod = (
                abs(row["angular_term"]) / abs(row["modulus_term"])
                if row["modulus_term"] != 0.0
                else None
            )
            if rel_ang_over_mod is not None:
                max_rel_ang_over_mod = max(max_rel_ang_over_mod, rel_ang_over_mod)
            rows.append(
                {
                    **row,
                    "eps_old": eps_old,
                    "eps_new": eps_new,
                    "eps_drift": eps_drift,
                    "angular_from_eps": reconstructed,
                    "angular_eps_error": abs(reconstructed - row["angular_term"]),
                    "abs_angular_over_abs_modulus": rel_ang_over_mod,
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "max_angular_eps_error": max(r["angular_eps_error"] for r in rows),
            "max_abs_angular_over_abs_modulus": max_rel_ang_over_mod,
        }

    out_path = HERE / "E78_33_angular_eps_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
