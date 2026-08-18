#!/usr/bin/env python3
"""E78.10 measure the numerator defect behind W-QUOTIENT-DELTA."""

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
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data, serial, two_generator_data  # noqa: E402


def cserial(z, digits: int = 24) -> dict[str, str]:
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def section(Hmax, idxmax, max_modes, modes):
    off = max_modes - modes
    return (
        Hmax[off : Hmax.rows - off, off : Hmax.cols - off],
        idxmax[off : len(idxmax) - off],
    )


def build_w_package(H: mp.matrix, idx: list[int], L: mp.mpf, lam: mp.mpf, planted, sigma: mp.mpf):
    _mu, A, db_idx, inner, _x = right_transfer_data(H, idx)
    d, u, v, db, aa, bb, ub, vb = two_generator_data(A, inner, db_idx, L, lam, planted)
    z = 1j * sigma
    U = mp.fsum(u[j] / (z - d[j]) for j in range(len(d)))
    V = mp.fsum(v[j] / (z - d[j]) for j in range(len(d)))
    Up = mp.fsum(-u[j] / (z - d[j]) ** 2 for j in range(len(d)))
    Vp = mp.fsum(-v[j] / (z - d[j]) ** 2 for j in range(len(d)))
    W = aa * (U + ub) + bb * (V + vb)
    Wp = aa * Up + bb * Vp
    return {"W": W, "Wp": Wp}


def run_case(label: str, planted, lam_int: int, max_modes: int, dps: int, sigmas: list[mp.mpf]):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    increments = []
    for n_modes in range(8, max_modes - 1, 2):
        Hn, idxn = section(Hmax, idxmax, max_modes, n_modes)
        Hm, idxm = section(Hmax, idxmax, max_modes, n_modes + 2)
        sigma_rows = []
        for sigma in sigmas:
            old = build_w_package(Hn, idxn, L, lam, planted, sigma)
            new = build_w_package(Hm, idxm, L, lam, planted, sigma)
            q_old = old["Wp"] / (1 + old["W"])
            q_new = new["Wp"] / (1 + new["W"])
            q_delta = q_old - q_new
            delta_w = old["W"] - new["W"]
            delta_wp = old["Wp"] - new["Wp"]
            numerator_defect = delta_wp - q_new * delta_w
            recon = numerator_defect / (1 + old["W"])
            scale = max(mp.mpf("1"), abs(q_delta))
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "q_delta_abs": serial(abs(q_delta)),
                    "numerator_defect_abs": serial(abs(numerator_defect)),
                    "delta_w_abs": serial(abs(delta_w)),
                    "delta_wp_abs": serial(abs(delta_wp)),
                    "old_den_abs": serial(abs(1 + old["W"])),
                    "new_q_abs": serial(abs(q_new)),
                    "reconstruction_relerr": serial(abs(q_delta - recon) / scale),
                    "q_delta": cserial(q_delta),
                    "numerator_defect": cserial(numerator_defect),
                }
            )
        increments.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "max_q_delta_abs": serial(max(mp.mpf(r["q_delta_abs"]) for r in sigma_rows)),
                "max_numdef_abs": serial(max(mp.mpf(r["numerator_defect_abs"]) for r in sigma_rows)),
                "max_delta_w_abs": serial(max(mp.mpf(r["delta_w_abs"]) for r in sigma_rows)),
                "max_delta_wp_abs": serial(max(mp.mpf(r["delta_wp_abs"]) for r in sigma_rows)),
                "min_old_den_abs": serial(min(mp.mpf(r["old_den_abs"]) for r in sigma_rows)),
                "max_reconstruction_relerr": serial(max(mp.mpf(r["reconstruction_relerr"]) for r in sigma_rows)),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:8s} {n_modes:2d}->{n_modes+2:2d} "
            f"|Qd|={serial(mp.mpf(increments[-1]['max_q_delta_abs']),8)} "
            f"|NumDef|={serial(mp.mpf(increments[-1]['max_numdef_abs']),8)} "
            f"min|den|={serial(mp.mpf(increments[-1]['min_old_den_abs']),8)} "
            f"recon={serial(mp.mpf(increments[-1]['max_reconstruction_relerr']),4)}",
            flush=True,
        )
    return {"label": label, "planted": None if planted is None else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]}, "increments": increments}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=10)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E78_10_w_numerator_defect_results.json")
    args = parser.parse_args()
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Numerator defect representation of W-QUOTIENT-DELTA",
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
