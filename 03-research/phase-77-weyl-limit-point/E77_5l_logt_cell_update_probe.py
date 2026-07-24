#!/usr/bin/env python3
"""E77.5l partition-invariant safe log-transfer update.

This probe measures the actual SR-LOG moving-section quantity

    2 Re(i[(T_N'/T_N)-(T_{N+2}'/T_{N+2})])

using the common-core moving-boundary transfer identity from E77.5k.  It
compares the invariant log-transfer update with the full section error
delta and the explicit external-tail delta.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_035_safe_log_derivative_probe import target_log_derivative  # noqa: E402
from P76_037_core_log_derivative_probe import external_tail  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, serial  # noqa: E402
from E77_5k_moving_boundary_four_node_probe import common_core_transfer_data, section  # noqa: E402


def section_error(logd, sigma: mp.mpf, L: mp.mpf, n_modes: int):
    base = L * mp.coth(sigma * L / 2)
    log_term = 2 * mp.re(1j * logd)
    ext = external_tail(sigma, L, n_modes)
    target = target_log_derivative(sigma)
    error = base + log_term - ext - target
    return base, log_term, ext, target, error


def run_build(label: str, lam_int: int, max_modes: int, dps: int, sigmas: list[mp.mpf], planted):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    increments = []
    for n_modes in range(8, max_modes - 1, 2):
        common_nodes = list(range(-n_modes + 2, n_modes - 1))
        Hn, idxn = section(Hmax, idxmax, max_modes, n_modes)
        Hm, idxm = section(Hmax, idxmax, max_modes, n_modes + 2)
        sigma_rows = []
        for sigma in sigmas:
            old = common_core_transfer_data(Hn, idxn, L, common_nodes, sigma)
            new = common_core_transfer_data(Hm, idxm, L, common_nodes, sigma)
            base_n, log_n, ext_n, target, err_n = section_error(
                old["log_derivative"], sigma, L, n_modes
            )
            base_m, log_m, ext_m, _target_m, err_m = section_error(
                new["log_derivative"], sigma, L, n_modes + 2
            )
            log_delta = log_n - log_m
            ext_delta = ext_n - ext_m
            base_delta = base_n - base_m
            error_delta = err_n - err_m
            recon = base_delta + log_delta - ext_delta
            recon_error = abs(error_delta - recon) / max(1, abs(error_delta))
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "logt_safe_delta": serial(log_delta),
                    "logt_safe_delta_abs": serial(abs(log_delta)),
                    "external_tail_delta": serial(ext_delta),
                    "external_tail_delta_abs": serial(abs(ext_delta)),
                    "base_delta": serial(base_delta),
                    "error_delta": serial(error_delta),
                    "error_delta_abs": serial(abs(error_delta)),
                    "log_over_external": serial(abs(log_delta) / abs(ext_delta) if ext_delta else mp.inf),
                    "error_reconstruction_error": serial(recon_error),
                    "old_identity_error": serial(old["identity_error"]),
                    "new_identity_error": serial(new["identity_error"]),
                }
            )
        max_log = max(mp.mpf(r["logt_safe_delta_abs"]) for r in sigma_rows)
        max_ext = max(mp.mpf(r["external_tail_delta_abs"]) for r in sigma_rows)
        max_err_delta = max(mp.mpf(r["error_delta_abs"]) for r in sigma_rows)
        max_recon = max(mp.mpf(r["error_reconstruction_error"]) for r in sigma_rows)
        max_id = max(
            max(mp.mpf(r["old_identity_error"]), mp.mpf(r["new_identity_error"]))
            for r in sigma_rows
        )
        increments.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "common_core": [common_nodes[0], common_nodes[-1]],
                "max_logt_safe_delta_abs": serial(max_log),
                "max_external_tail_delta_abs": serial(max_ext),
                "max_error_delta_abs": serial(max_err_delta),
                "max_log_over_external": serial(max_log / max_ext if max_ext else mp.inf),
                "max_error_reconstruction_error": serial(max_recon),
                "max_identity_error": serial(max_id),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:10s} {n_modes:2d}->{n_modes+2:2d} "
            f"dLogT={serial(max_log,8):>12s} dExt={serial(max_ext,8):>12s} "
            f"dErr={serial(max_err_delta,8):>12s} log/ext={serial(max_log/max_ext if max_ext else mp.inf,8):>12s} "
            f"id={serial(max_id,5)}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam_int,
        "N_max": max_modes,
        "dps": dps,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "increments": increments,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5l_logt_cell_update_results.json")
    args = parser.parse_args()
    if args.dps < 70:
        parser.error("E77.5l requires dps >= 70")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Partition-invariant safe log-transfer update",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(s) for s in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for label, planted in [
        (f"zeta-lam{args.lam}", None),
        (f"plant-lam{args.lam}", (GAMMA, "0.30", "5.0")),
    ]:
        print(f"BUILD {label}", flush=True)
        result["cases"].append(run_build(label, args.lam, args.max_modes, args.dps, sigmas, planted))
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
