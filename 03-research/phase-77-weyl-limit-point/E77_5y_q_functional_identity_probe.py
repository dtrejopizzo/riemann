#!/usr/bin/env python3
"""E77.5y exact Q_N functional identity from signed log/external deltas."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def f(x):
    return float(x)


def by_sigma_increment(case):
    rows = {}
    for inc in case["increments"]:
        n = inc["from_N"]
        for srow in inc["sigmas"]:
            sigma = srow["sigma"]
            ext = f(srow["external_tail_delta"])
            logt = f(srow["logt_safe_delta"])
            residual = ext - logt
            rows[(sigma, n)] = {
                "N": n,
                "to_N": inc["to_N"],
                "sigma": sigma,
                "external": ext,
                "logt": logt,
                "residual": residual,
                "C": n * residual,
                "C_external": n * ext,
                "C_logt": n * logt,
            }
    return rows


def q_lookup(qcase, sigma, n):
    for profile in qcase["profiles"]:
        if profile["sigma"] == sigma:
            cls = str(n % 4)
            for q in profile["classes"][cls]["Q_values"]:
                if q["N"] == n:
                    return float(q["value"])
    return None


def component_rows(log_case, qcase):
    table = by_sigma_increment(log_case)
    out = []
    for (sigma, n), row in sorted(table.items(), key=lambda x: (float(x[0][0]), x[0][1])):
        nxt = table.get((sigma, n + 2))
        q_ref = q_lookup(qcase, sigma, n)
        if nxt is None or q_ref is None:
            continue
        q_external = n * n * (row["C_external"] - nxt["C_external"])
        q_logt = n * n * (row["C_logt"] - nxt["C_logt"])
        q_recon = q_external - q_logt
        denom = max(1.0, abs(q_ref))
        out.append(
            {
                "sigma": sigma,
                "N": n,
                "mod4": n % 4,
                "Q_reference": q_ref,
                "Q_reconstructed": q_recon,
                "Q_identity_error": abs(q_recon - q_ref) / denom,
                "Q_external_component": q_external,
                "Q_logt_component": q_logt,
                "component_cancellation_index": (abs(q_external) + abs(q_logt)) / max(abs(q_recon), 1e-300),
                "external_share_signed": q_external / q_recon if q_recon else float("inf"),
                "logt_share_signed": q_logt / q_recon if q_recon else float("inf"),
                "R_N": row["residual"],
                "R_N_plus_2": nxt["residual"],
                "C_N": row["C"],
                "C_N_plus_2": nxt["C"],
            }
        )
    return out


def summarize(rows):
    by_sigma = {}
    for row in rows:
        by_sigma.setdefault(row["sigma"], []).append(row)
    profiles = []
    for sigma, vals in sorted(by_sigma.items(), key=lambda x: float(x[0])):
        q_abs = max(abs(v["Q_reference"]) for v in vals)
        max_id = max(v["Q_identity_error"] for v in vals)
        max_cancel = max(v["component_cancellation_index"] for v in vals)
        spike = max(vals, key=lambda v: abs(v["Q_reference"]))
        profiles.append(
            {
                "sigma": sigma,
                "max_abs_Q": q_abs,
                "max_identity_error": max_id,
                "max_component_cancellation_index": max_cancel,
                "max_abs_Q_row": spike,
            }
        )
    return profiles


def run(log_path: Path, q_path: Path):
    log_data = json.loads(log_path.read_text(encoding="ascii"))
    q_data = json.loads(q_path.read_text(encoding="ascii"))
    result = {
        "statement": "Exact finite identity Q_N = Q_ext_N - Q_logT_N",
        "log_source": str(log_path),
        "q_source": str(q_path),
        "cases": [],
    }
    for log_case, qcase in zip(log_data["cases"], q_data["cases"]):
        rows = component_rows(log_case, qcase)
        result["cases"].append({"label": log_case["label"], "rows": rows, "profiles": summarize(rows)})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", type=Path, default=HERE / "E77_5l_logt_cell_update_results.json")
    parser.add_argument("--q", type=Path, default=HERE / "E77_5q_mod4_drift_split_results.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5y_q_functional_identity_results.json")
    args = parser.parse_args()
    result = run(args.log, args.q)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for prof in case["profiles"]:
            if prof["sigma"] in {"1.0", "3.0"}:
                row = prof["max_abs_Q_row"]
                print(
                    f"SIGMA {prof['sigma']} maxId={prof['max_identity_error']:.3e} "
                    f"maxCancel={prof['max_component_cancellation_index']:.6g} "
                    f"spike N={row['N']} Q={row['Q_reference']:.9g} "
                    f"Qext={row['Q_external_component']:.9g} Qlog={row['Q_logt_component']:.9g}",
                    flush=True,
                )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
