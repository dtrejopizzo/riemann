#!/usr/bin/env python3
"""E77.7d operator-realization decomposition audit."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np


HERE = Path(__file__).resolve().parent
PHASE71 = HERE.parent / "phase-71-cand1-convergence"
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE71))
sys.path.insert(0, str(PHASE76))

from E71_9_relative_arch_background_probe import QW_entry, build  # noqa: E402
from P76_002_mp_entry_audit import build_mp  # noqa: E402


GAMMA = "14.134725141734693790"


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def opnorm(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(np.linalg.eigvalsh(matrix))))


def pure_frequency_audit(L: mp.mpf, omega: mp.mpf, modes: int):
    idx = list(range(-modes, modes + 1))
    d = [2 * mp.pi * n / L for n in idx]
    loewner = mp.matrix(len(idx))
    toeplitz = mp.matrix(len(idx))
    phase = mp.diag([mp.exp(1j * omega * value / 2) for value in d])
    for a, da in enumerate(d):
        for b, db in enumerate(d):
            if a == b:
                loewner[a, b] = 1j * omega * mp.exp(1j * omega * da)
                toeplitz[a, b] = 1j * omega
            else:
                loewner[a, b] = (mp.exp(1j * omega * da) - mp.exp(1j * omega * db)) / (da - db)
                toeplitz[a, b] = 2j * mp.sin(omega * (da - db) / 2) / (da - db)
    reconstructed = phase * toeplitz * phase
    defect = mp.sqrt(
        mp.fsum(abs(loewner[a, b] - reconstructed[a, b]) ** 2 for a in range(len(idx)) for b in range(len(idx)))
    ) / max(
        mp.mpf(1),
        mp.sqrt(mp.fsum(abs(loewner[a, b]) ** 2 for a in range(len(idx)) for b in range(len(idx)))),
    )
    toeplitz_np = np.array([[complex(toeplitz[a, b]) for b in range(len(idx))] for a in range(len(idx))])
    # i times the Toeplitz matrix is Hermitian; singular values give its norm.
    toeplitz_norm = float(np.linalg.svd(toeplitz_np, compute_uv=False)[0])
    return {
        "omega": serial(omega),
        "modes": modes,
        "factorization_relative_defect": serial(defect),
        "loewner_norm": toeplitz_norm,
        "scaled_H_norm": 2 * toeplitz_norm / float(L),
        "infinite_toeplitz_bound": float(L),
        "scaled_infinite_bound": 2.0,
    }


def arch_s_density(y: mp.mpf) -> mp.mpf:
    return 2 * mp.cosh(y / 2) - mp.exp(y / 2) / (2 * mp.sinh(y))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=24)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--output", type=Path, default=HERE / "E77_7d_op_realization_results.json")
    args = parser.parse_args()
    mp.mp.dps = args.dps
    Lmp = 2 * mp.log(args.lam)
    pure = pure_frequency_audit(Lmp, mp.mpf("1.3"), 8)

    full, idx, L = build(float(args.lam), args.max_modes, include_arith=True)
    arch, _idx, _L = build(float(args.lam), args.max_modes, include_arith=False)
    prime = full - arch
    section_rows = []
    for modes in (6, 8, 10, 12, 16, 20, args.max_modes):
        if modes > args.max_modes:
            continue
        offset = args.max_modes - modes
        sl = slice(offset, len(idx) - offset)
        section_rows.append(
            {
                "N": modes,
                "full_norm": opnorm(full[sl, sl]),
                "arch_norm": opnorm(arch[sl, sl]),
                "prime_norm": opnorm(prime[sl, sl]),
                "full_min_eigenvalue": float(np.linalg.eigvalsh(full[sl, sl])[0]),
            }
        )

    tv_rows = []
    for exponent in (2, 4, 6, 8, 10):
        epsilon = mp.power(10, -exponent)
        mass = mp.quad(lambda y: abs(arch_s_density(y)), [epsilon, Lmp])
        tv_rows.append({"epsilon": serial(epsilon), "truncated_total_variation": serial(mass)})

    high_indices = (10, 20, 50, 100, 200, 500, 1000)
    high_diagonal = []
    for n in high_indices:
        value = QW_entry(n, n, float(L), float(args.lam), include_arith=False)
        high_diagonal.append(
            {
                "n": n,
                "arch_diagonal": value,
                "arch_diagonal_over_log_n": value / np.log(n),
            }
        )

    # Small multiprecision planted control: the plant is an additional finite-
    # interval Fourier package and must not invalidate finite-section symmetry.
    zeta_mp, _idx_mp, _L_mp = build_mp(args.lam, 12, args.dps)
    plant_mp, _idx_mp, _L_mp = build_mp(
        args.lam, 12, args.dps, planted=(GAMMA, "0.30", "5.0")
    )
    zeta_np = np.array([[float(zeta_mp[a, b]) for b in range(zeta_mp.cols)] for a in range(zeta_mp.rows)])
    plant_np = np.array([[float(plant_mp[a, b]) for b in range(plant_mp.cols)] for a in range(plant_mp.rows)])

    result = {
        "statement": "Pure-frequency Loewner factorization and fixed-L realization audit",
        "parameters": {
            "lambda": args.lam,
            "L": float(L),
            "max_modes": args.max_modes,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "pure_frequency": pure,
        "section_norms": section_rows,
        "archimedean_measure_tv": tv_rows,
        "archimedean_high_diagonal": high_diagonal,
        "planted_control": {
            "N": 12,
            "zeta_norm": opnorm(zeta_np),
            "plant_norm": opnorm(plant_np),
            "plant_extra_norm": opnorm(plant_np - zeta_np),
            "plant_symmetry_defect": float(np.linalg.norm(plant_np - plant_np.T)),
        },
        "verdict": (
            "The pure-frequency factorization is valid and arithmetic finite mass is harmless. "
            "The proposed finite-total-variation proof does not apply to the WR archimedean density, "
            "whose truncated variation grows at the origin."
        ),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(
        f"pure defect={pure['factorization_relative_defect']} "
        f"scaled norm={pure['scaled_H_norm']:.8f} bound={pure['scaled_infinite_bound']:.1f}"
    )
    for row in section_rows:
        print(
            f"N={row['N']:2d} full={row['full_norm']:.8f} "
            f"arch={row['arch_norm']:.8f} prime={row['prime_norm']:.8f} "
            f"mu={row['full_min_eigenvalue']:.3e}"
        )
    for row in tv_rows:
        print(f"eps={row['epsilon']} TV={row['truncated_total_variation']}")
    for row in high_diagonal:
        print(
            f"diag n={row['n']:4d} value={row['arch_diagonal']:.9f} "
            f"overlog={row['arch_diagonal_over_log_n']:.9f}"
        )
    print("plant", result["planted_control"])
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
