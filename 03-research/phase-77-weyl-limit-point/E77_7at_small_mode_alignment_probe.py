#!/usr/bin/env python3
"""E77.7at read even-block data and audit lock-predicted residual alignment."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_rows(path: Path):
    data = json.loads(path.read_text(encoding="ascii"))
    rows = []
    for case in data["cases"]:
        for row in case["rows"]:
            rows.append((case["label"], row))
    return rows


def even_block_from_row(row):
    schur_u = [[float(x) for x in r] for r in row["schur_u"]]
    a = schur_u[0][0]
    b = schur_u[0][2]
    c = schur_u[2][2]
    return a, b, c


def residual_from_row(row):
    names = row["basis_names"]
    return float(row["residual_u"][names[0]]), float(row["residual_u"][names[2]])


def norm2(v):
    return math.sqrt(sum(x * x for x in v))


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def serial(x):
    return format(x, ".18g")


def analyze_row(label, row):
    a, b, c = even_block_from_row(row)
    r1, r2 = residual_from_row(row)
    sgn = 1.0 if b >= 0 else -1.0
    small_pred = (math.sqrt(c), -sgn * math.sqrt(a))
    large_pred = (math.sqrt(a), sgn * math.sqrt(c))
    r = (r1, r2)
    nr = norm2(r)
    ns = norm2(small_pred)
    nl = norm2(large_pred)
    cos_small_orth = abs(dot(r, small_pred)) / max(nr * ns, 1e-300)
    cos_large_align = abs(dot(r, large_pred)) / max(nr * nl, 1e-300)
    return {
        "label": label,
        "old_modes": row["old_modes"],
        "new_modes": row["new_modes"],
        "a": serial(a),
        "b": serial(b),
        "c": serial(c),
        "rho": serial(b / math.sqrt(a * c)),
        "residual_ratio_r2_over_r1": serial(r2 / r1) if r1 else "inf",
        "predicted_large_ratio": serial((sgn * math.sqrt(c / a))),
        "cos_small_orth": serial(cos_small_orth),
        "cos_large_align": serial(cos_large_align),
        "raw_small_dot": serial(dot(r, small_pred)),
        "raw_large_dot": serial(dot(r, large_pred)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputs",
        nargs="+",
        type=Path,
        default=[
            HERE / "E77_7aq_even_odd_shell_results.json",
            HERE / "E77_7aq_even_odd_shell_plant_16_18.json",
        ],
    )
    parser.add_argument("--output", type=Path, default=HERE / "E77_7at_small_mode_alignment_results.json")
    args = parser.parse_args()

    rows = []
    for path in args.inputs:
        rows.extend(load_rows(path))
    out_rows = [analyze_row(label, row) for label, row in rows]
    result = {
        "statement": "Lock-predicted residual alignment audit in the even shell block",
        "inputs": [str(p) for p in args.inputs],
        "rows": out_rows,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for row in out_rows:
        print(
            f"{row['label']:6s} {row['old_modes']:2d}->{row['new_modes']:2d} "
            f"cos_small_orth={row['cos_small_orth']} "
            f"cos_large_align={row['cos_large_align']} "
            f"r2/r1={row['residual_ratio_r2_over_r1']} "
            f"pred={row['predicted_large_ratio']}",
            flush=True,
        )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
