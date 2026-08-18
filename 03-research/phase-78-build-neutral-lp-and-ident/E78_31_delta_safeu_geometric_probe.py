#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE78 = HERE


def load_json(name: str):
    return json.loads((PHASE78 / name).read_text())


def main():
    src = load_json("E78_30_delta_safeu_ratio_results.json")
    result = {
        "statement": (
            "Audit of a raw geometric envelope for d_N = Delta safe_u_N: "
            "0 < d_{N+2} <= eta_* d_N"
        ),
        "source": str(PHASE78 / "E78_30_delta_safeu_ratio_results.json"),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = [r for r in payload["rows"] if r["sigma"] in ("1.0", "3.0")]
        eta_star = None
        out_rows = []
        for row in rows:
            ratio = row["delta_safeu_ratio"]
            ok = ratio is not None and ratio > 0 and ratio < 1
            if ok:
                eta_star = ratio if eta_star is None else max(eta_star, ratio)
            out_rows.append({**row, "positive_geometric_envelope": ok})
        result["builds"][build] = {
            "rows": out_rows,
            "positive_geometric_envelope_count": sum(1 for r in out_rows if r["positive_geometric_envelope"]),
            "positive_geometric_envelope_fail_count": sum(1 for r in out_rows if not r["positive_geometric_envelope"]),
            "eta_star_observed": eta_star,
        }

    out_path = HERE / "E78_31_delta_safeu_geometric_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
