#!/usr/bin/env python3
"""Audit the ground-mode contribution to the paired MU derivative route."""

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.append(str(ROOT))

from P76_002_mp_entry_audit import build_mp


SIGMAS = [mp.mpf("0.6"), mp.mpf("1.0"), mp.mpf("2.0")]
PLANTED = ("14.134725141734693790", "0.30", "5.0")


def audit_case(name, planted, ns, dps):
    rows = []
    for n_modes in ns:
        H, idx, L = build_mp(6, n_modes, dps, planted=planted)
        vals, _vecs = mp.eigsy(H)
        mu = vals[0]
        A = H[1:-1, 1:-1]
        inner_vals, inner_vecs = mp.eigsy(A)
        nu0 = inner_vals[0]
        v0 = inner_vecs[:, 0]
        b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
        inner_idx = idx[1:-1]
        nodes = [2 * mp.pi * n / L for n in inner_idx]
        sigma_rows = []
        for sigma in SIGMAS:
            rz = mp.matrix([[1 / (1j * sigma - dj) for dj in nodes]])
            ov_r = abs((rz * v0)[0])
            ov_b = abs((v0.T * b)[0])
            sigma_rows.append(
                {
                    "sigma": mp.nstr(sigma, 8),
                    "abs_r_v0": mp.nstr(ov_r, 20),
                    "abs_v0_b": mp.nstr(ov_b, 20),
                    "ground_term_over_gap": mp.nstr((ov_r * ov_b) / nu0, 20),
                    "ground_term_over_gap_sq": mp.nstr((ov_r * ov_b) / (nu0 * nu0), 20),
                }
            )
        rows.append(
            {
                "N": n_modes,
                "mu_N": mp.nstr(mu, 20),
                "inner_ground_nu0": mp.nstr(nu0, 20),
                "sigmas": sigma_rows,
            }
        )
    return {"build": name, "dps": dps, "rows": rows}


def main():
    mp.mp.dps = 60
    results = {
        "statement": "E78.102 ground-mode audit for paired d_mu route",
        "date": "2026-07-19",
        "zeta": audit_case("zeta", None, (6, 8, 10, 12), 60),
        "plant": audit_case("plant", PLANTED, (6, 8), 50),
    }
    out_path = Path(__file__).with_name("E78_102_paired_dmu_groundmode_results.json")
    out_path.write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
