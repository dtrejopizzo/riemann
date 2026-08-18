#!/usr/bin/env python3
"""Audit the signed five-shell coefficients of v_2 on the positive half-axis."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(ROOT))

from P76_002_mp_entry_audit import build_mp  # noqa: E402


PLANTED = ("14.134725141734693790", "0.30", "5.0")


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def run_case(label, planted):
    mp.mp.dps = 50
    rows = []
    for n_modes in (8, 12):
        H, idx, _L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        _vals, vecs = mp.eigsy(A)
        v2 = vecs[:, 2]
        inner = idx[1:-1]
        slots = [j for j, n in enumerate(inner) if n >= 0][:6]
        coeffs = [v2[j] for j in slots]
        anchor = mp.sign(mp.re(coeffs[0])) if mp.re(coeffs[0]) != 0 else mp.mpf("1")
        aligned = [anchor * c for c in coeffs]
        rows.append(
            {
                "N": n_modes,
                "coeffs": [serialize(c) for c in coeffs],
                "aligned_coeffs": [serialize(c) for c in aligned],
                "aligned_signs": [
                    "+" if mp.re(c) > 0 else "-" if mp.re(c) < 0 else "0" for c in aligned
                ],
                "aligned_mag_ratios": [
                    serialize(abs(aligned[j + 1]) / abs(aligned[j])) for j in range(len(aligned) - 1)
                ],
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.127 five-shell signature audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "quantity": "signed coefficients of v_2 on the nonnegative half-axis",
    }
    out_path = Path(__file__).with_name("E78_127_five_shell_signature_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
