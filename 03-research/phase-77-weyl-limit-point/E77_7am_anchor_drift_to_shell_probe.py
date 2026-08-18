#!/usr/bin/env python3
"""Compare shorted shell energy with Phase-5 anchor/drift functionals."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_json(path: Path):
    return json.loads(path.read_text(encoding="ascii"))


def index_qrows(case):
    rows = case.get("qrows", case.get("rows", []))
    return {(row["sigma"], row["N"]): row for row in rows}


def index_udata(case):
    rows = case.get("qrows", case.get("rows", []))
    return {(str(row["sigma"]), int(row["N"])): row for row in rows}


def run(shell_path: Path, q_path: Path, uz_path: Path, up_path: Path):
    shell = load_json(shell_path)
    qdata = load_json(q_path)
    uz = load_json(uz_path)
    up = load_json(up_path)
    out = {"statement": "Anchor/drift to shell alignment audit", "cases": []}
    for shell_case, q_case in zip(shell["cases"], qdata["cases"]):
        u_case = uz["cases"][0] if "zeta" in shell_case["label"] else up["cases"][0]
        qidx = index_qrows(q_case)
        uidx = index_udata(u_case)
        rows = []
        for row in shell_case["rows"]:
            n_old = int(row["old_modes"])
            sigma = row["eta"]  # no sigma stored here; use eta-independent shell rows only
            # compare using the phase-5 sigma=1.0 and 3.0 spikes at the same old shell
            comps = {}
            for s in ("1.0", "3.0"):
                qrow = qidx.get((s, n_old))
                urow = uidx.get((s, n_old))
                if qrow and urow:
                    comps[s] = {
                        "Q_abs": abs(qrow["Q_reference"]),
                        "Q_logt_abs": abs(qrow["Q_logt_component"]),
                        "Q_cancel_index": qrow["component_cancellation_index"],
                        "Q_theta_abs": abs(urow["Q_theta"]),
                        "one_minus_theta_new": abs(urow["one_minus_theta_abs_new"]),
                    }
            rows.append(
                {
                    "old_modes": n_old,
                    "new_modes": int(row["new_modes"]),
                    "energy_over_eta": float(row["energy_over_eta"]),
                    "cancellation_ratio": float(row["cancellation_ratio"]),
                    "crude_bound_over_energy": float(row["crude_bound_over_energy"]),
                    "comparisons": comps,
                }
            )
        out["cases"].append({"label": shell_case["label"], "rows": rows})
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--shell",
        type=Path,
        default=HERE / "E77_7h_shorted_shell_energy_results.json",
    )
    parser.add_argument(
        "--q",
        type=Path,
        default=HERE / "E77_5y_q_functional_identity_results.json",
    )
    parser.add_argument(
        "--uz",
        type=Path,
        default=HERE / "E77_5aa_schur_logt_functional_zeta.json",
    )
    parser.add_argument(
        "--up",
        type=Path,
        default=HERE / "E77_5aa_schur_logt_functional_plant.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7am_anchor_drift_to_shell_results.json",
    )
    args = parser.parse_args()
    result = run(args.shell, args.q, args.uz, args.up)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for row in case["rows"]:
            comps = row["comparisons"]
            s3 = comps.get("3.0", {})
            print(
                f"ROW {row['old_modes']:2d}->{row['new_modes']:2d} "
                f"E/eta={row['energy_over_eta']:.6g} "
                f"resRatio={row['cancellation_ratio']:.6g} "
                f"Q3={s3.get('Q_abs', float('nan')):.6g} "
                f"Qtheta3={s3.get('Q_theta_abs', float('nan')):.6g} "
                f"|1-th|3={s3.get('one_minus_theta_new', float('nan')):.6g}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
