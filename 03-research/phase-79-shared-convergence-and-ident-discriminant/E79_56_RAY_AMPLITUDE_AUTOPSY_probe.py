#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "E79_55_modal_ray_reduction_results.json"
OUT = ROOT / "E79_56_ray_amplitude_autopsy_results.json"


def summarize(values):
    return {
        "min": min(values),
        "max": max(values),
        "ratio": max(values) / min(values),
        "mean": sum(values) / len(values),
    }


def best_simple_sign_misses(points):
    signs = {pt["N"]: "+" if pt["Na"] > 0 else "-" for pt in points}
    patterns = {
        "constant_plus": lambda n: "+",
        "constant_minus": lambda n: "-",
        "alternating_from_first": lambda n: "+" if ((n - min(signs)) // 2) % 2 == 0 else "-",
        "alternating_from_first_flipped": lambda n: "-" if ((n - min(signs)) // 2) % 2 == 0 else "+",
    }
    out = {}
    for name, fn in patterns.items():
        misses = sum(1 for n, s in signs.items() if fn(n) != s)
        out[name] = misses
    return out


def build_case(case):
    k = case["signed_ray_slope"]
    denom = 1.0 + k * k
    rows = []
    for pt in case["points"]:
        rho = (pt["Na"] + k * pt["Ng"]) / denom
        rows.append(
            {
                "N": pt["N"],
                "rho": rho,
                "abs_rho": abs(rho),
                "N_abs_rho": pt["N"] * abs(rho),
                "sign": "+" if rho > 0 else "-",
            }
        )

    return {
        "label": case["label"],
        "ray_slope": k,
        "rows": rows,
        "abs_rho_band": summarize([r["abs_rho"] for r in rows]),
        "N_abs_rho_band": summarize([r["N_abs_rho"] for r in rows]),
        "simple_sign_pattern_misses": best_simple_sign_misses(case["points"]),
    }


def main():
    source = json.loads(SOURCE.read_text())
    result = {
        "statement": "E79.56 ray-amplitude autopsy",
        "source": str(SOURCE),
        "cases": [build_case(case) for case in source["cases"]],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
