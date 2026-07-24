#!/usr/bin/env python3
"""E77.7f fixed-mu block-growth and moving boundary-source audit."""

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


def section(Hmax: mp.matrix, idxmax: list[int], reference_modes: int, modes: int):
    offset = reference_modes - modes
    return (
        Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def centered_positions(reference_modes: int, modes: int):
    return {
        "left": -modes + reference_modes,
        "right": modes + reference_modes,
        "inner": [j + reference_modes for j in range(-modes + 1, modes)],
        "outer": [
            j + reference_modes
            for j in range(-reference_modes, reference_modes + 1)
            if abs(j) > modes
        ],
    }


def spectral_response(inner: mp.matrix, source: mp.matrix, mu: mp.mpf):
    values, vectors = mp.eigsy(inner)
    rows = []
    energy = mp.mpf("0")
    largest_fraction = mp.mpf("0")
    largest_index = 0
    largest_contribution = mp.mpf("0")
    for j in range(values.rows):
        vec = vectors[:, j]
        coeff = (vec.T * source)[0]
        gap = values[j] - mu
        contribution = abs(coeff) ** 2 / abs(gap) ** 2
        energy += contribution
        if contribution > largest_contribution:
            largest_contribution = contribution
            largest_index = j
    if energy != 0:
        largest_fraction = largest_contribution / energy
    ground_coeff = abs((vectors[:, 0].T * source)[0])
    ground_gap = values[0] - mu
    ground_contribution = abs(ground_coeff) ** 2 / abs(ground_gap) ** 2
    ground_fraction = ground_contribution / energy if energy != 0 else mp.mpf("0")
    return {
        "values": values,
        "vectors": vectors,
        "spectral_energy": energy,
        "ground_coeff_abs": ground_coeff,
        "ground_gap_abs": abs(ground_gap),
        "ground_gap_signed": ground_gap,
        "ground_trace_over_gap": ground_coeff / max(mp.mpf("1e-100"), abs(ground_gap)),
        "ground_contribution": ground_contribution,
        "ground_fraction": ground_fraction,
        "largest_mode_index": largest_index,
        "largest_contribution": largest_contribution,
        "largest_fraction": largest_fraction,
        "largest_gap_abs": abs(values[largest_index] - mu),
    }


def boundary_trace_balance(Hmax, idxmax, reference_modes, modes, mu, vref):
    pos = centered_positions(reference_modes, modes)
    left = pos["left"]
    right = pos["right"]
    inner_pos = pos["inner"]
    outer_pos = pos["outer"]
    v_inner = mp.matrix([vref[p] for p in inner_pos])
    b_right = mp.matrix([Hmax[p, right] for p in inner_pos])
    right_overlap = (v_inner.T * b_right)[0]
    diag_rhs = (mu - Hmax[right, right]) * vref[right]
    left_rhs = -Hmax[right, left] * vref[left]
    outer_sum = mp.fsum(Hmax[right, p] * vref[p] for p in outer_pos)
    outer_rhs = -outer_sum
    rhs = diag_rhs + left_rhs + outer_rhs
    defect = abs(right_overlap - rhs) / max(mp.mpf(1), abs(right_overlap) + abs(rhs))
    return {
        "reference_right_component_abs": abs(vref[right]),
        "reference_left_component_abs": abs(vref[left]),
        "projected_reference_inner_norm": norm(v_inner),
        "right_boundary_overlap_abs": abs(right_overlap),
        "diag_tail_term_abs": abs(diag_rhs),
        "left_boundary_term_abs": abs(left_rhs),
        "outer_tail_term_abs": abs(outer_rhs),
        "balance_relative_defect": defect,
    }


def run_build(label, lam, reference_modes, dps, planted, min_modes):
    Hmax, idxmax, L = build_mp(lam, reference_modes, dps, planted=planted)
    reference_values, reference_vectors = mp.eigsy(Hmax)
    mu_reference = reference_values[0]
    vref = reference_vectors[:, 0]
    if vref[reference_modes] < 0:
        vref = -vref
    rows = []
    prev_energy = None
    for modes in range(min_modes, reference_modes + 1):
        H, idx = section(Hmax, idxmax, reference_modes, modes)
        inner = H[1:-1, 1:-1]
        source = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
        A = inner - mu_reference * mp.eye(inner.rows)
        response = mp.lu_solve(A, source)
        energy = norm(response) ** 2
        spectral = spectral_response(inner, source, mu_reference)
        balance = boundary_trace_balance(Hmax, idxmax, reference_modes, modes, mu_reference, vref)
        spectral_defect = abs(energy - spectral["spectral_energy"]) / max(mp.mpf(1), abs(energy))
        growth_ratio = mp.mpf("0") if prev_energy is None else energy / prev_energy
        prev_energy = energy
        row = {
            "N": modes,
            "dim": H.rows,
            "mu_reference": serial(mu_reference),
            "fixed_mu_energy_S": serial(energy),
            "fixed_mu_radius_proxy": serial(1 / energy) if energy != 0 else "inf",
            "growth_ratio": serial(growth_ratio),
            "source_norm": serial(norm(source)),
            "response_norm": serial(norm(response)),
            "spectral_energy_defect": serial(spectral_defect),
            "inner_ground_gap_abs": serial(spectral["ground_gap_abs"]),
            "inner_ground_coeff_abs": serial(spectral["ground_coeff_abs"]),
            "inner_ground_trace_over_gap": serial(spectral["ground_trace_over_gap"]),
            "inner_ground_fraction_of_energy": serial(spectral["ground_fraction"]),
            "largest_mode_index": spectral["largest_mode_index"],
            "largest_mode_gap_abs": serial(spectral["largest_gap_abs"]),
            "largest_mode_fraction_of_energy": serial(spectral["largest_fraction"]),
            "reference_right_component_abs": serial(balance["reference_right_component_abs"]),
            "reference_left_component_abs": serial(balance["reference_left_component_abs"]),
            "projected_reference_inner_norm": serial(balance["projected_reference_inner_norm"]),
            "reference_right_overlap_abs": serial(balance["right_boundary_overlap_abs"]),
            "reference_diag_tail_term_abs": serial(balance["diag_tail_term_abs"]),
            "reference_left_boundary_term_abs": serial(balance["left_boundary_term_abs"]),
            "reference_outer_tail_term_abs": serial(balance["outer_tail_term_abs"]),
            "reference_balance_relative_defect": serial(balance["balance_relative_defect"]),
        }
        rows.append(row)
        print(
            f"{label:6s} N={modes:2d} S={serial(energy, 8):>13s} "
            f"g0={serial(spectral['ground_gap_abs'], 6):>10s} "
            f"c0={serial(spectral['ground_coeff_abs'], 6):>10s} "
            f"c0/g={serial(spectral['ground_trace_over_gap'], 6):>10s} "
            f"frac0={serial(spectral['ground_fraction'], 6):>9s} "
            f"vOv={serial(balance['right_boundary_overlap_abs'], 6):>10s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "reference_modes": reference_modes,
        "reference_dim": Hmax.rows,
        "mu_reference": serial(mu_reference),
        "reference_ground_gap": serial(reference_values[1] - reference_values[0])
        if reference_values.rows > 1
        else "NA",
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--reference-modes", type=int, default=18)
    parser.add_argument("--min-modes", type=int, default=6)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7f_fixed_mu_block_growth_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7f requires dps >= 60")
    if args.min_modes < 2 or args.min_modes > args.reference_modes:
        parser.error("need 2 <= min-modes <= reference-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "Fixed-mu block-growth and moving boundary-source audit",
        "parameters": {
            "lambda": args.lam,
            "reference_modes": args.reference_modes,
            "min_modes": args.min_modes,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "mu_reference and v_reference are finite-section surrogates, not the "
            "abstract infinite-volume mu_L and v0.  Boundary traces are tested "
            "against the exact finite reference eigen-equation."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(run_build(label, args.lam, args.reference_modes, args.dps, planted, args.min_modes))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
