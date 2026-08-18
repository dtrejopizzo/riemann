#!/usr/bin/env python3
"""E77.7ap compare projected Schur source against shell energy."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(HERE))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, serial  # noqa: E402
from E77_5aa_schur_logt_functional_probe import prepare_schur, section, schur_logt_parts  # noqa: E402
from E77_7h_shorted_shell_energy_probe import analyze_pair  # noqa: E402


def safe_scalar(z):
    return 2 * mp.re(1j * z)


def find_point(case_data, step_n: int, section_n: int, sigma: str, tag: str):
    for row in case_data["points"]:
        if row["step_N"] == step_n and row["section_N"] == section_n and row["sigma"] == sigma and row["tag"] == tag:
            return row
    raise KeyError((step_n, section_n, sigma, tag))


def bridge_row(Hmax, idxmax, L, max_modes: int, step_n: int, sigma: mp.mpf):
    common_nodes = list(range(-step_n + 2, step_n - 1))
    Hold, idxold = section(Hmax, idxmax, max_modes, step_n)
    Hnew, idxnew = section(Hmax, idxmax, max_modes, step_n + 2)

    old_prep = prepare_schur(Hold, idxold, common_nodes)
    new_prep = prepare_schur(Hnew, idxnew, common_nodes)
    old = schur_logt_parts(old_prep, L, sigma)
    new = schur_logt_parts(new_prep, L, sigma)

    shell = analyze_pair(Hmax, idxmax, 14, step_n, step_n + 2)
    energy = mp.mpf(shell["fixed_shell_increment_schur"]) if "fixed_shell_increment_schur" in shell else None
    if energy is None:
        energy = mp.mpf(shell["shorted_energy"])
    eta = mp.mpf(shell["eta"])
    shell_energy_over_eta = mp.mpf(shell["energy_over_eta"] if "energy_over_eta" in shell else shell["shell_increment_over_eta_new"])

    old_u = old["theta_part"]
    new_u = new["theta_part"]
    delta_u_safe = safe_scalar(old_u) - safe_scalar(new_u)
    old_corr = old["theta"] * (1 / (1j * sigma - (2 * mp.pi * old_prep["db_idx"] / L)) - 0)  # placeholder not used
    return {
        "N": step_n,
        "to_N": step_n + 2,
        "old_tau_y_abs": abs(old["theta"] * 1),  # proxy: theta already normalized projection
        "new_tau_y_abs": abs(new["theta"] * 1),
        "old_theta_abs": abs(old["theta"]),
        "new_theta_abs": abs(new["theta"]),
        "old_u_abs": abs(old_u),
        "new_u_abs": abs(new_u),
        "delta_u_safe": delta_u_safe,
        "shell_energy_over_eta": shell_energy_over_eta,
        "shell_energy_abs": abs(energy) if energy is not None else None,
        "ratio_shell_over_du": abs(shell_energy_over_eta) / max(mp.mpf("1e-100"), abs(delta_u_safe)),
        "ratio_shell_over_new_u": abs(shell_energy_over_eta) / max(mp.mpf("1e-100"), abs(new_u)),
        "ratio_shell_over_new_theta": abs(shell_energy_over_eta) / max(mp.mpf("1e-100"), abs(new["theta"])),
        "old": old,
        "new": new,
    }


def run_build(label, planted, lam: int, max_modes: int, dps: int, sigmas: list[mp.mpf], steps: list[int]):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for sigma in sigmas:
        for step_n in steps:
            row = bridge_row(Hmax, idxmax, L, max_modes, step_n, sigma)
            rows.append(
                {
                    "sigma": serial(sigma),
                    "N": step_n,
                    "to_N": step_n + 2,
                    "old_theta_abs": serial(row["old_theta_abs"]),
                    "new_theta_abs": serial(row["new_theta_abs"]),
                    "old_u_abs": serial(row["old_u_abs"]),
                    "new_u_abs": serial(row["new_u_abs"]),
                    "delta_u_safe": serial(row["delta_u_safe"]),
                    "shell_energy_over_eta": serial(row["shell_energy_over_eta"]),
                    "ratio_shell_over_du": serial(row["ratio_shell_over_du"]),
                    "ratio_shell_over_new_u": serial(row["ratio_shell_over_new_u"]),
                    "ratio_shell_over_new_theta": serial(row["ratio_shell_over_new_theta"]),
                }
            )
            print(
                f"ROW {label:6s} s={serial(sigma)} N={step_n:2d}->{step_n+2:2d} "
                f"E/eta={serial(row['shell_energy_over_eta'], 8)} "
                f"|du|={serial(abs(row['delta_u_safe']), 8)} "
                f"|u_new|={serial(row['new_u_abs'], 8)} "
                f"|th_new|={serial(row['new_theta_abs'], 8)} "
                f"E/du={serial(row['ratio_shell_over_du'], 8)}",
                flush=True,
            )
    return {"label": label, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--sigmas", default="1.0,3.0")
    parser.add_argument("--steps", default="16,18")
    parser.add_argument("--case", choices=["zeta", "plant", "both"], default="both")
    parser.add_argument("--output", type=Path, default=HERE / "E77_7ap_projected_shell_bridge_results.json")
    args = parser.parse_args()
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    steps = [int(x) for x in args.steps.split(",") if x]
    result = {
        "statement": "Projected Schur source versus shell energy bridge audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(s) for s in sigmas],
            "steps": steps,
        },
        "cases": [],
    }
    specs = []
    if args.case in {"zeta", "both"}:
        specs.append(("zeta", None))
    if args.case in {"plant", "both"}:
        specs.append(("plant", (GAMMA, "0.30", "5.0")))
    for label, planted in specs:
        result["cases"].append(run_build(label, planted, args.lam, args.max_modes, args.dps, sigmas, steps))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
