#!/usr/bin/env python3
"""Audit how HALF-AXIS-MODE2(t) accumulates over the positive half-axis."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(ROOT))

from P76_002_mp_entry_audit import build_mp  # noqa: E402


PLANTED = ("14.134725141734693790", "0.30", "5.0")
TS = [mp.mpf("0.6"), mp.mpf("1.0"), mp.mpf("2.0")]


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def run_case(label, planted):
    mp.mp.dps = 50
    rows = []
    for n_modes in (8, 12):
        H, idx, L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        _vals, vecs = mp.eigsy(A)
        v2 = vecs[:, 2]
        inner = idx[1:-1]
        d = [2 * mp.pi * n / L for n in inner]
        zero = [j for j, n in enumerate(inner) if n == 0][0]
        pos = [j for j, n in enumerate(inner) if n > 0]
        point_rows = []
        for t in TS:
            total = -v2[zero] / t + mp.fsum((-2 * t * v2[j]) / (t * t + d[j] * d[j]) for j in pos)
            part0 = -v2[zero] / t
            partial = part0
            accum = []
            for k, j in enumerate(pos[:5], start=1):
                partial += (-2 * t * v2[j]) / (t * t + d[j] * d[j])
                accum.append(
                    {
                        "k": k,
                        "partial_over_full": serialize(abs(partial) / max(abs(total), mp.mpf("1e-80"))),
                    }
                )
            point_rows.append(
                {
                    "t": serialize(t),
                    "zero_over_full": serialize(abs(part0) / max(abs(total), mp.mpf("1e-80"))),
                    "partials": accum,
                }
            )
        rows.append({"N": n_modes, "points": point_rows})
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.125 half-axis localization audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "quantity": "partial sums of HALF-AXIS-MODE2(t) over the first positive shells",
    }
    out_path = Path(__file__).with_name("E78_125_half_axis_localization_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
