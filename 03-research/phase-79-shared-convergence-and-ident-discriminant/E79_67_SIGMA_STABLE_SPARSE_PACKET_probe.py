#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPARSE = ROOT / "E79_3W_terminal_sparse_packet_results.json"
TWOBLOCK = ROOT / "E79_3V_terminal_two_block_results.json"
OUT = ROOT / "E79_67_sigma_stable_sparse_packet_results.json"


def best_sparse_per_sigma(sigmas):
    out = {}
    for sigma, data in sigmas.items():
        best_name, best_data = min(
            data["packets"].items(),
            key=lambda kv: float(kv[1]["mismatch"]),
        )
        out[sigma] = {
            "name": best_name,
            "support": best_data["support"],
            "mismatch": float(best_data["mismatch"]),
            "N2_abs_minus": float(best_data["N2_abs_minus"]),
        }
    return out


def best_two_block_per_sigma(sigmas):
    out = {}
    for sigma, data in sigmas.items():
        if not data["combos"]:
            out[sigma] = None
            continue
        best_name, best_data = min(
            data["combos"].items(),
            key=lambda kv: float(kv[1]["mismatch"]),
        )
        out[sigma] = {
            "name": best_name,
            "support": [
                best_data["block1_start"],
                best_data["block1_take"],
                best_data["gap"],
                best_data["block2_start"],
                best_data["block2_take"],
            ],
            "mismatch": float(best_data["mismatch"]),
            "N2_abs_minus": float(best_data["N2_abs_minus"]),
        }
    return out


def main():
    sparse = json.loads(SPARSE.read_text())
    two = json.loads(TWOBLOCK.read_text())

    two_map = {case["label"]: {row["N"]: row for row in case["rows"]} for case in two["cases"]}
    result = {
        "statement": "E79.67 sigma-stability audit for the sparse terminal packet",
        "sources": [str(SPARSE), str(TWOBLOCK)],
        "cases": [],
    }

    for case in sparse["cases"]:
        label = case["label"]
        rows = []
        stable_support_count = 0
        stable_rule_count = 0
        same_as_two_block_count = 0
        for row in case["rows"]:
            best_sparse = best_sparse_per_sigma(row["sigmas"])
            best_two = best_two_block_per_sigma(two_map[label][row["N"]]["sigmas"])
            sigmas = sorted(best_sparse.keys(), key=float)
            ref_sigma = sigmas[0]
            same_support = all(best_sparse[s]["support"] == best_sparse[ref_sigma]["support"] for s in sigmas[1:])
            same_rule = all(best_sparse[s]["name"] == best_sparse[ref_sigma]["name"] for s in sigmas[1:])
            same_as_two = all(
                best_two[s] is not None
                and abs(best_sparse[s]["mismatch"] - best_two[s]["mismatch"]) < 1e-15
                and abs(best_sparse[s]["N2_abs_minus"] - best_two[s]["N2_abs_minus"]) < 1e-15
                for s in sigmas
            )
            stable_support_count += int(same_support)
            stable_rule_count += int(same_rule)
            same_as_two_block_count += int(same_as_two)
            rows.append(
                {
                    "N": row["N"],
                    "best_sparse": best_sparse,
                    "best_two_block": best_two,
                    "sigma_stable_support": same_support,
                    "sigma_stable_rule": same_rule,
                    "sparse_matches_two_block_quality_each_sigma": same_as_two,
                }
            )
        result["cases"].append(
            {
                "label": label,
                "rows": rows,
                "summary": {
                    "num_rows": len(rows),
                    "sigma_stable_support_count": stable_support_count,
                    "sigma_stable_rule_count": stable_rule_count,
                    "sparse_matches_two_block_quality_count": same_as_two_block_count,
                },
            }
        )

    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
