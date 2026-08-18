#!/usr/bin/env python3
"""E77.5m residual-ratio diagnostics from the invariant LOGT-CELL output."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def run(input_path: Path):
    data = json.loads(input_path.read_text(encoding="ascii"))
    out = {
        "statement": "LOG-EXT-RATIO residual scaling diagnostics",
        "source": str(input_path),
        "cases": [],
    }
    for case in data["cases"]:
        rows = []
        prev = None
        for inc in case["increments"]:
            n = inc["from_N"]
            residual = float(inc["max_error_delta_abs"])
            external = float(inc["max_external_tail_delta_abs"])
            logt = float(inc["max_logt_safe_delta_abs"])
            rel = residual / external if external else float("inf")
            local_slope = None
            if prev is not None:
                n0, r0 = prev
                local_slope = math.log(residual / r0) / math.log(n / n0)
            rows.append(
                {
                    "N": n,
                    "to_N": inc["to_N"],
                    "residual": residual,
                    "external": external,
                    "logt": logt,
                    "residual_over_external": rel,
                    "N_residual": n * residual,
                    "N2_residual": n * n * residual,
                    "local_power_slope": local_slope,
                }
            )
            prev = (n, residual)
        out["cases"].append(
            {
                "label": case["label"],
                "rows": rows,
                "tail_N_residual_range": [
                    min(r["N_residual"] for r in rows[-4:]),
                    max(r["N_residual"] for r in rows[-4:]),
                ],
                "tail_N2_residual_range": [
                    min(r["N2_residual"] for r in rows[-4:]),
                    max(r["N2_residual"] for r in rows[-4:]),
                ],
            }
        )
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=HERE / "E77_5l_logt_cell_update_results.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5m_log_ext_ratio_results.json")
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for r in case["rows"]:
            slope = "" if r["local_power_slope"] is None else f"{r['local_power_slope']:.4g}"
            print(
                f"ROW N={r['N']:2d}->{r['to_N']:2d} "
                f"R={r['residual']:.9g} R/ext={r['residual_over_external']:.9g} "
                f"N*R={r['N_residual']:.9g} N2*R={r['N2_residual']:.9g} slope={slope}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
