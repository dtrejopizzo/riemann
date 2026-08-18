#!/usr/bin/env python3
"""E77.7e paired interlacing-gap audit."""

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


GAMMA = "14.134725141734693790"


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def norm(vector: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vector[j]) ** 2 for j in range(vector.rows)))


def section(Hmax, idxmax, max_modes, modes):
    offset = max_modes - modes
    return (
        Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def cauchy_pair(vector, inner, L, sigma):
    return mp.fsum(vector[j] / (1j * sigma - 2 * mp.pi * inner[j] / L) for j in range(vector.rows))


def run_build(label, lam, max_modes, dps, sigmas, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    max_values, _ = mp.eigsy(Hmax)
    mu_reference = max_values[0]
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        values, _ = mp.eigsy(H)
        mu_n = values[0]
        inner_block = H[1:-1, 1:-1]
        inner_values, inner_vectors = mp.eigsy(inner_block)
        nu_n = inner_values[0]
        v0 = inner_vectors[:, 0]
        gap = nu_n - mu_n
        b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
        overlap = abs((v0.T * b)[0])
        normalized_overlap = overlap / max(mp.mpf("1e-100"), norm(b))
        ground_component = overlap / gap

        moving_matrix = inner_block - mu_n * mp.eye(inner_block.rows)
        reference_matrix = inner_block - mu_reference * mp.eye(inner_block.rows)
        x_moving = mp.lu_solve(moving_matrix, b)
        x_reference = mp.lu_solve(reference_matrix, b)
        double_response = mp.lu_solve(moving_matrix, x_reference)
        delta_mu = mu_n - mu_reference
        vector_shift = delta_mu * double_response
        direct_shift = x_moving - x_reference
        identity_error = norm(direct_shift - vector_shift) / max(mp.mpf(1), norm(direct_shift))

        sigma_rows = []
        max_paired = mp.mpf(0)
        for sigma in sigmas:
            moving_pair = cauchy_pair(x_moving, idx[1:-1], L, sigma)
            double_pair = cauchy_pair(double_response, idx[1:-1], L, sigma)
            paired = abs(delta_mu * double_pair) / max(mp.mpf(1), abs(moving_pair))
            max_paired = max(max_paired, paired)
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "moving_pair_abs": serial(abs(moving_pair)),
                    "double_pair_abs": serial(abs(double_pair)),
                    "paired_freeze_ratio": serial(paired),
                }
            )

        low_width = min(5, v0.rows)
        low_mass = mp.fsum(abs(v0[j]) ** 2 for j in range(low_width))
        center = v0.rows // 2
        center_lo = max(0, center - 2)
        center_hi = min(v0.rows, center + 3)
        center_mass = mp.fsum(abs(v0[j]) ** 2 for j in range(center_lo, center_hi))
        rows.append(
            {
                "N": modes,
                "mu_N": serial(mu_n),
                "mu_reference": serial(mu_reference),
                "delta_mu_abs": serial(abs(delta_mu)),
                "inner_ground_nu": serial(nu_n),
                "interlacing_gap": serial(gap),
                "boundary_norm": serial(norm(b)),
                "ground_boundary_overlap": serial(overlap),
                "normalized_ground_boundary_overlap": serial(normalized_overlap),
                "ground_component_overlap_over_gap": serial(ground_component),
                "ground_vector_left_five_mass": serial(low_mass),
                "ground_vector_center_five_mass": serial(center_mass),
                "double_response_norm": serial(norm(double_response)),
                "prefactored_double_response_norm": serial(abs(delta_mu) * norm(double_response)),
                "max_paired_freeze_ratio": serial(max_paired),
                "resolvent_identity_relative_error": serial(identity_error),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"{label:6s} N={modes:2d} dmu={serial(abs(delta_mu), 7):>11s} "
            f"gap={serial(gap, 7):>11s} ov={serial(normalized_overlap, 7):>11s} "
            f"ov/g={serial(ground_component, 7):>11s} pair={serial(max_paired, 7):>11s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "reference_N": max_modes,
        "mu_reference": serial(mu_reference),
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.6,1.0,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_7e_dir_gap_pair_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7e requires dps >= 50")
    mp.mp.dps = args.dps
    sigmas = [mp.mpf(value) for value in args.sigmas.split(",") if value]
    result = {
        "statement": "Paired interlacing-gap audit for directional mu freezing",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(sigma) for sigma in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": "mu_reference is the largest measured section, not the abstract mu_L proved by E77.7d.",
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, args.max_modes, args.dps, sigmas, planted)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
