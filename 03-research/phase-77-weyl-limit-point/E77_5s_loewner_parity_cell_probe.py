#!/usr/bin/env python3
"""E77.5s Loewner parity packages for the moving four-node cell."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))

from E77_2_commutator_probe import sine_symbol  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, serial  # noqa: E402


def q_lookup(qcase, sigma: str, n: int):
    for profile in qcase["profiles"]:
        if profile["sigma"] == sigma:
            cls = str(n % 4)
            for q in profile["classes"][cls]["Q_values"]:
                if q["N"] == n:
                    return q["value"]
    return None


def cell_package(n: int, L: mp.mpf, lam: mp.mpf, planted):
    nodes = [-n - 1, -n, n, n + 1]
    vals = []
    for node in nodes:
        d = 2 * mp.pi * node / L
        s = sine_symbol(d, L, lam, planted)
        vals.append({"node": node, "d": d, "s": s})
    left = vals[0]["s"] + vals[1]["s"]
    right = vals[2]["s"] + vals[3]["s"]
    odd = right - left
    even = right + left
    alt = vals[0]["s"] - vals[1]["s"] - vals[2]["s"] + vals[3]["s"]
    return {
        "nodes": nodes,
        "left_sum": left,
        "right_sum": right,
        "odd_lr": odd,
        "even_lr": even,
        "alt_shell": alt,
    }


def run(q_path: Path, lam_int: int, dps: int):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    L = 2 * mp.log(lam)
    qdata = json.loads(q_path.read_text(encoding="ascii"))
    out = {
        "statement": "Loewner parity packages for inserted four-node cells",
        "q_source": str(q_path),
        "lambda": lam_int,
        "L": serial(L),
        "cases": [],
    }
    for qcase, planted in [
        (qdata["cases"][0], None),
        (qdata["cases"][1], (GAMMA, "0.30", "5.0")),
    ]:
        rows = []
        for n in (8, 10, 12, 14, 16, 18):
            pkg = cell_package(n, L, lam, planted)
            q_sig1 = q_lookup(qcase, "1.0", n)
            q_sig3 = q_lookup(qcase, "3.0", n)
            rows.append(
                {
                    "N": n,
                    "mod4": n % 4,
                    "nodes": pkg["nodes"],
                    "odd_lr": serial(pkg["odd_lr"]),
                    "even_lr": serial(pkg["even_lr"]),
                    "alt_shell": serial(pkg["alt_shell"]),
                    "abs_odd_lr": serial(abs(pkg["odd_lr"])),
                    "abs_even_lr": serial(abs(pkg["even_lr"])),
                    "Q_sigma1": q_sig1,
                    "Q_sigma3": q_sig3,
                }
            )
        out["cases"].append({"label": qcase["label"], "rows": rows})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=Path, default=HERE / "E77_5q_mod4_drift_split_results.json")
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--output", type=Path, default=HERE / "E77_5s_loewner_parity_cell_results.json")
    args = parser.parse_args()
    result = run(args.q, args.lam, args.dps)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for row in case["rows"]:
            print(
                f"ROW N={row['N']:2d} mod4={row['mod4']} "
                f"|odd|={row['abs_odd_lr']:>12s} |even|={row['abs_even_lr']:>12s} "
                f"Q1={row['Q_sigma1']} Q3={row['Q_sigma3']}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
