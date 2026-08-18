#!/usr/bin/env python3
"""Audit the exact spectral tail certificate for A^{-2}1."""

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


def vnorm(vec: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vec[j]) ** 2 for j in range(vec.rows)))


def spectral_tail_certificate(A: mp.matrix):
    vals, vecs = mp.eigsy(A)
    one = mp.matrix([1 for _ in range(A.rows)])
    coeff0 = (vecs[:, 0].T * one)[0]
    ground = coeff0 / (vals[0] ** 2) * vecs[:, 0]
    tail = mp.matrix([0 for _ in range(A.rows)])
    for j in range(1, A.rows):
        coeffj = (vecs[:, j].T * one)[0]
        tail += coeffj / (vals[j] ** 2) * vecs[:, j]
    gap_ratio = vals[1] / vals[0]
    tail_to_ground = vnorm(tail) / max(vnorm(ground), mp.mpf("1e-80"))
    certificate = (mp.sqrt(A.rows) / abs(coeff0)) * (vals[0] / vals[1]) ** 2
    return {
        "nu0": vals[0],
        "nu1": vals[1],
        "coeff0": coeff0,
        "tail_to_ground": tail_to_ground,
        "certificate": certificate,
        "certificate_over_actual": certificate / max(tail_to_ground, mp.mpf("1e-80")),
    }


def run_case(label, planted):
    mp.mp.dps = 50
    rows = []
    for n_modes in (6, 8, 10, 12):
        H, idx, _L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        audit = spectral_tail_certificate(A)
        rows.append(
            {
                "N": n_modes,
                "nu0": serialize(audit["nu0"]),
                "nu1": serialize(audit["nu1"]),
                "gap_ratio_nu1_over_nu0": serialize(audit["nu1"] / audit["nu0"]),
                "coeff0_abs": serialize(abs(audit["coeff0"])),
                "tail_to_ground": serialize(audit["tail_to_ground"]),
                "certificate_bound": serialize(audit["certificate"]),
                "certificate_over_actual": serialize(audit["certificate_over_actual"]),
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.109 groundmode tail certificate audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "bound": "||tail|| / ||ground|| <= (sqrt(N) / |<v0,1>|) * (nu0/nu1)^2",
    }
    out_path = Path(__file__).with_name("E78_109_groundmode_tail_gate_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
