#!/usr/bin/env python3
"""E77.5e shell-update decomposition for SECTION-LAG.

For fixed lambda, decompose consecutive section changes

    E_N(sigma)-E_{N+2}(sigma)

into the coupled two-generator log term and the explicit external sine-zero
tail term.  This names the part of SECTION-LAG that still needs a summable
envelope.
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
from E77_3c_two_generator_ident_probe import (  # noqa: E402
    GAMMA,
    generated_values,
    right_transfer_data,
    serial,
    two_generator_data,
)


def section_values(Hmax, idxmax, L, lam, n_modes, sigmas, planted):
    offset = (len(idxmax) - (2 * n_modes + 1)) // 2
    H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
    idx = idxmax[offset : len(idxmax) - offset]
    _mu, A, db_idx, inner, _x = right_transfer_data(H, idx)
    d, u, v, db, aa, bb, ub, vb = two_generator_data(A, inner, db_idx, L, lam, planted)
    rows = []
    for sigma in sigmas:
        z = 1j * sigma
        _T, logd, _F, _package = generated_values(z, d, u, v, db, aa, bb, ub, vb)
        log_term = 2 * mp.re(1j * logd)
        ext = external_tail(sigma, L, n_modes)
        base = L * mp.coth(sigma * L / 2)
        target = target_log_derivative(sigma)
        error = base + log_term - ext - target
        rows.append(
            {
                "sigma": serial(sigma),
                "error": error,
                "abs_rel_error": abs(error) / abs(target),
                "base": base,
                "log_term": log_term,
                "external_tail": ext,
                "target": target,
            }
        )
    return rows


def max_abs(items, key):
    best = max(items, key=lambda item: abs(item[key]))
    return best, abs(best[key])


def run_build(label, lam_int, max_modes, dps, sigmas, planted):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    sections = {}
    for n_modes in range(8, max_modes + 1, 2):
        sections[n_modes] = section_values(Hmax, idxmax, L, lam, n_modes, sigmas, planted)
    updates = []
    for n_modes in range(8, max_modes - 1, 2):
        left = sections[n_modes]
        right = sections[n_modes + 2]
        sigma_updates = []
        for a, b in zip(left, right):
            error_delta = a["error"] - b["error"]
            log_delta = a["log_term"] - b["log_term"]
            ext_delta = a["external_tail"] - b["external_tail"]
            rel_delta = a["abs_rel_error"] - b["abs_rel_error"]
            sigma_updates.append(
                {
                    "sigma": a["sigma"],
                    "error_delta": serial(error_delta),
                    "log_delta": serial(log_delta),
                    "external_tail_delta": serial(ext_delta),
                    "relative_error_delta": serial(rel_delta),
                    "abs_log_over_abs_ext": serial(abs(log_delta) / abs(ext_delta) if ext_delta else mp.inf),
                }
            )
        _best_err, max_error_delta = max_abs(
            [{"v": mp.mpf(u["relative_error_delta"])} for u in sigma_updates], "v"
        )
        _best_log, max_log_delta = max_abs(
            [{"v": mp.mpf(u["log_delta"])} for u in sigma_updates], "v"
        )
        _best_ext, max_ext_delta = max_abs(
            [{"v": mp.mpf(u["external_tail_delta"])} for u in sigma_updates], "v"
        )
        updates.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "max_relative_error_delta": serial(max_error_delta),
                "max_log_delta_abs": serial(max_log_delta),
                "max_external_tail_delta_abs": serial(max_ext_delta),
                "max_log_over_external": serial(max_log_delta / max_ext_delta if max_ext_delta else mp.inf),
                "sigmas": sigma_updates,
            }
        )
        print(
            f"ROW {label:10s} {n_modes:2d}->{n_modes+2:2d} "
            f"drel={serial(max_error_delta, 8):>12s} "
            f"dlog={serial(max_log_delta, 8):>12s} "
            f"dext={serial(max_ext_delta, 8):>12s}",
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
        "updates": updates,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5e_shell_update_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.5e requires dps >= 50")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Shell-update decomposition of SECTION-LAG",
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
