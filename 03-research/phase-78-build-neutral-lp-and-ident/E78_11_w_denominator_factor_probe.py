#!/usr/bin/env python3
"""E78.11 verify 1+W=(z-d_b)t0(1-theta) and inspect its factors."""

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
from E77_3c_two_generator_ident_probe import GAMMA, generated_values, right_transfer_data, serial, two_generator_data  # noqa: E402
from E77_5k_moving_boundary_four_node_probe import common_core_transfer_data  # noqa: E402


def cserial(z, digits: int = 24) -> dict[str, str]:
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def section(Hmax, idxmax, max_modes, modes):
    off = max_modes - modes
    return (
        Hmax[off : Hmax.rows - off, off : Hmax.cols - off],
        idxmax[off : len(idxmax) - off],
    )


def run_case(label: str, planted, lam_int: int, max_modes: int, dps: int, sigmas: list[mp.mpf]):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    rows = []
    for n_modes in range(8, max_modes + 1, 2):
        H, idx = section(Hmax, idxmax, max_modes, n_modes)
        _mu, A, db_idx, inner, _x = right_transfer_data(H, idx)
        d, u, v, db, aa, bb, ub, vb = two_generator_data(A, inner, db_idx, L, lam, planted)
        common_nodes = list(range(-n_modes + 2, n_modes - 1))
        sigma_rows = []
        min_den = None
        max_recon = mp.mpf("0")
        for sigma in sigmas:
            z = 1j * sigma
            _T, _logd, F, W = generated_values(z, d, u, v, db, aa, bb, ub, vb)
            data = common_core_transfer_data(H, idx, L, common_nodes, sigma)
            theta = data["theta_common"]
            # corr/t0 = theta, T = t0(1-theta), and F = (z-d_b)T
            rhs = (z - 2 * mp.pi * db_idx / L) * data["T"]
            rhs2 = (z - 2 * mp.pi * db_idx / L) * (data["T"] / (1 if True else 1))
            # reconstruct via t0 and theta using T from the same packet:
            factor = rhs
            recon = abs(F - factor) / max(mp.mpf("1"), abs(F))
            max_recon = max(max_recon, recon)
            den = abs(F)
            min_den = den if min_den is None else min(min_den, den)
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "F_abs": serial(abs(F)),
                    "zdiff_abs": serial(abs(z - 2 * mp.pi * db_idx / L)),
                    "T_abs": serial(abs(data["T"])),
                    "theta_abs": serial(abs(theta)),
                    "one_minus_theta_abs": serial(abs(1 - theta)),
                    "reconstruction_relerr": serial(recon),
                    "F": cserial(F),
                }
            )
        rows.append(
            {
                "N": n_modes,
                "min_F_abs": serial(min_den),
                "max_reconstruction_relerr": serial(max_recon),
                "sigmas": sigma_rows,
            }
        )
    return {"label": label, "planted": None if planted is None else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]}, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=10)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E78_11_w_denominator_factor_results.json")
    args = parser.parse_args()
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Factorization of 1+W through shell-resolvent factors",
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
