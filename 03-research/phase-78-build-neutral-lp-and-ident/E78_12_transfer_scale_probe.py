#!/usr/bin/env python3
"""E78.12 inspect transfer-scale amplification across consecutive sections."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, serial  # noqa: E402
from E77_5k_moving_boundary_four_node_probe import common_core_transfer_data  # noqa: E402


def section(Hmax, idxmax, max_modes, modes):
    off = max_modes - modes
    return (
        Hmax[off : Hmax.rows - off, off : Hmax.cols - off],
        idxmax[off : len(idxmax) - off],
    )


def run_case(label: str, planted, lam_int: int, max_modes: int, dps: int, sigmas: list[mp.mpf]):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    increments = []
    for n_modes in range(8, max_modes - 1, 2):
        Hn, idxn = section(Hmax, idxmax, max_modes, n_modes)
        Hm, idxm = section(Hmax, idxmax, max_modes, n_modes + 2)
        common_nodes = list(range(-n_modes + 2, n_modes - 1))
        sigma_rows = []
        for sigma in sigmas:
            old = common_core_transfer_data(Hn, idxn, L, common_nodes, sigma)
            new = common_core_transfer_data(Hm, idxm, L, common_nodes, sigma)
            theta_old = old["theta_common"]
            theta_new = new["theta_common"]
            t_abs_old = abs(old["T"])
            t_abs_new = abs(new["T"])
            om_abs_old = abs(1 - theta_old)
            om_abs_new = abs(1 - theta_new)
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "old_T_abs": serial(t_abs_old),
                    "new_T_abs": serial(t_abs_new),
                    "old_one_minus_theta_abs": serial(om_abs_old),
                    "new_one_minus_theta_abs": serial(om_abs_new),
                    "old_theta_abs": serial(abs(theta_old)),
                    "new_theta_abs": serial(abs(theta_new)),
                    "T_ratio": serial(t_abs_new / t_abs_old if t_abs_old else mp.inf),
                    "one_minus_theta_ratio": serial(om_abs_new / om_abs_old if om_abs_old else mp.inf),
                }
            )
        increments.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "max_T_ratio": serial(max(mp.mpf(r["T_ratio"]) for r in sigma_rows)),
                "min_T_ratio": serial(min(mp.mpf(r["T_ratio"]) for r in sigma_rows)),
                "max_one_minus_theta_ratio": serial(max(mp.mpf(r["one_minus_theta_ratio"]) for r in sigma_rows)),
                "min_one_minus_theta_ratio": serial(min(mp.mpf(r["one_minus_theta_ratio"]) for r in sigma_rows)),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:8s} {n_modes:2d}->{n_modes+2:2d} "
            f"T-ratio=[{increments[-1]['min_T_ratio']},{increments[-1]['max_T_ratio']}] "
            f"om-ratio=[{increments[-1]['min_one_minus_theta_ratio']},{increments[-1]['max_one_minus_theta_ratio']}]",
            flush=True,
        )
    return {"label": label, "planted": None if planted is None else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]}, "increments": increments}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=10)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E78_12_transfer_scale_results.json")
    args = parser.parse_args()
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Transfer-scale amplification audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(s) for s in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        result["cases"].append(run_case(label, planted, args.lam, args.max_modes, args.dps, sigmas))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
