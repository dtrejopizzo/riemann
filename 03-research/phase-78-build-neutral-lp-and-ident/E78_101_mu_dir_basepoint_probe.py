#!/usr/bin/env python3
"""Probe the MU-DIR basepoint reduction on the audited safe ladder."""

import json
from pathlib import Path

import mpmath as mp

import sys

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.append(str(ROOT))

from P76_002_mp_entry_audit import build_mp
from P76_047_mu_freezing_probe import values


SIGMAS = [mp.mpf("0.6"), mp.mpf("1.0"), mp.mpf("2.0")]
PLANTED = ("14.134725141734693790", "0.30", "5.0")


def audit_build(name, planted, max_modes, dps, ns, eps):
    Hmax, idxmax, L = build_mp(6, max_modes, dps, planted=planted)
    rows = []
    for n_modes in ns:
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        mu = mp.eigsy(H, eigvals_only=True)[0]
        j_mu = values(H, idx, L, n_modes, mu, SIGMAS)
        j_0 = values(H, idx, L, n_modes, mp.mpf("0"), SIGMAS)
        defect = max(abs(a - b) for a, b in zip(j_mu, j_0))
        dmu_sup = mp.mpf("0")
        for t in (mp.mpf("0"), mu / 2, mu):
            jp = values(H, idx, L, n_modes, t + eps, SIGMAS)
            jm = values(H, idx, L, n_modes, t - eps, SIGMAS)
            dmu_sup = max(
                dmu_sup,
                max(abs((a - b) / (2 * eps)) for a, b in zip(jp, jm)),
            )
        rows.append(
            {
                "N": n_modes,
                "mu_N": mp.nstr(mu, 20),
                "max_abs_J_mu_minus_J_0": mp.nstr(defect, 20),
                "finite_diff_sup_dmu": mp.nstr(dmu_sup, 20),
                "abs_mu_times_sup_dmu": mp.nstr(abs(mu) * dmu_sup, 20),
            }
        )
    return {
        "build": name,
        "max_modes": max_modes,
        "dps": dps,
        "eps": mp.nstr(eps, 8),
        "sigmas": [mp.nstr(s, 8) for s in SIGMAS],
        "rows": rows,
    }


def main():
    mp.mp.dps = 50
    results = {
        "statement": "E78.101 MU-DIR basepoint reduction audit",
        "date": "2026-07-19",
        "zeta": audit_build(
            name="zeta",
            planted=None,
            max_modes=12,
            dps=50,
            ns=(6, 8, 10, 12),
            eps=mp.mpf("1e-6"),
        ),
        "plant": audit_build(
            name="plant",
            planted=PLANTED,
            max_modes=8,
            dps=40,
            ns=(6, 8),
            eps=mp.mpf("1e-5"),
        ),
    }
    out_path = Path(__file__).with_name("E78_101_mu_dir_basepoint_results.json")
    out_path.write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
