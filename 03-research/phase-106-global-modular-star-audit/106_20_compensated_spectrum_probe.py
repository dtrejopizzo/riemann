#!/usr/bin/env python3
"""Galerkin diagnostic for the compensated Phase-106.19 inequality.

This is a float64 diagnostic, not a proof or a certified computation.  It
uses exactly the Fourier matrices and source normalization of
``106_04_cofinal_weil_defect_probe.py`` and independently assembles

    W = E_* - c_* I - A_Delta.

Here ``E_*`` is the positive compensated Gamma jump form and ``A_Delta``
is the signed Stieltjes discrepancy form against ``d(psi(x)-x)``.  Besides
checking the matrix identity, the script computes the largest generalized
Rayleigh quotient

    (v^* (A_Delta+c_*I) v) / (v^* E_* v),

and diagnoses its extremal vector in Fourier and physical coordinates.  It
also reports how much of its arithmetic value is carried by the largest
individual prime-power atoms.

Only Python and NumPy are required.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
from pathlib import Path
import sys
from dataclasses import dataclass

import numpy as np


EULER_GAMMA = 0.577215664901532860606512090082402431
C_STAR = EULER_GAMMA + math.pi / 2.0 + 3.0 * math.log(2.0) + math.log(math.pi) - 4.0


def load_phase_106_04():
    path = Path(__file__).with_name("106_04_cofinal_weil_defect_probe.py")
    spec = importlib.util.spec_from_file_location("phase106_weil_source", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOURCE = load_phase_106_04()


def nu_star_tail(length: float) -> float:
    """Integral_L^infinity exp(-5u/2)/(1-exp(-2u)) du."""
    total = 0.0
    for j in range(100_000):
        rate = 2.5 + 2.0 * j
        term = math.exp(-rate * length) / rate
        total += term
        if term < 2.0e-17 * max(1.0, total):
            return total
    raise RuntimeError("nu_* tail series did not converge")


@dataclass
class Components:
    weil: np.ndarray
    e_star: np.ndarray
    a_delta: np.ndarray
    prime: np.ndarray
    main: np.ndarray
    gamma_compensated: np.ndarray
    atom_matrices: list[tuple[int, float, np.ndarray]]
    length: float


def compensated_components(
    lam: float, max_mode: int, quadrature_order: int
) -> Components:
    """Assemble W, E_*, and A_Delta in one Fourier Galerkin basis."""
    weil, length = SOURCE.build_weil_matrix(lam, max_mode, quadrature_order)
    indices = np.arange(-max_mode, max_mode + 1, dtype=float)
    dim = indices.size
    identity = np.eye(dim)
    omega_zero = SOURCE.omega_matrix(0.0, indices, length)

    nodes, weights = np.polynomial.legendre.leggauss(quadrature_order)
    xs = 0.5 * length * (nodes + 1.0)
    ws = 0.5 * length * weights
    e_star = np.zeros((dim, dim), dtype=float)
    main = np.zeros((dim, dim), dtype=float)
    for x, weight in zip(xs, ws):
        x = float(x)
        omega = SOURCE.omega_matrix(x, indices, length)
        density_star = math.exp(-2.5 * x) / (-math.expm1(-2.0 * x))
        e_star += weight * density_star * (omega_zero - omega)
        main += weight * math.exp(0.5 * x) * omega

    # For u >= L the zero-extended correlation vanishes, so the jump
    # integrand is exactly omega(0)=2I.
    e_star += nu_star_tail(length) * omega_zero

    cutoff = int(math.floor(math.exp(length) + 1.0e-12))
    mangoldt = SOURCE.von_mangoldt(cutoff)
    prime = np.zeros((dim, dim), dtype=float)
    atoms: list[tuple[int, float, np.ndarray]] = []
    for n in np.flatnonzero(mangoldt):
        if n <= 1:
            continue
        weight = float(mangoldt[n] / math.sqrt(int(n)))
        atom = SOURCE.omega_matrix(math.log(int(n)), indices, length)
        prime += weight * atom
        atoms.append((int(n), weight, atom))

    a_delta = prime - main
    gamma_compensated = e_star - C_STAR * identity

    # Symmetrize only after independent assembly.  This removes roundoff
    # antisymmetry without hiding a normalization mismatch.
    for matrix in (e_star, main, prime, a_delta, gamma_compensated):
        matrix[:] = 0.5 * (matrix + matrix.T)

    return Components(
        weil=weil,
        e_star=e_star,
        a_delta=a_delta,
        prime=prime,
        main=main,
        gamma_compensated=gamma_compensated,
        atom_matrices=atoms,
        length=length,
    )


def central_slice(matrix: np.ndarray, max_mode: int, mode: int) -> np.ndarray:
    start = max_mode - mode
    stop = max_mode + mode + 1
    return matrix[start:stop, start:stop]


def generalized_extremal(
    e_star: np.ndarray, target: np.ndarray
) -> tuple[float, np.ndarray, float, float, int]:
    """Largest target/E_* quotient and diagnostics of its top eigenspace."""
    evals, basis = np.linalg.eigh(e_star)
    minimum = float(evals[0])
    if minimum <= 5.0e-13 * max(1.0, float(evals[-1])):
        raise ValueError(
            f"E_* is too ill-conditioned for float64 inversion: min={minimum:.3e}, "
            f"max={evals[-1]:.3e}"
        )
    inverse_root = (basis / np.sqrt(evals)) @ basis.T
    normalized = inverse_root @ target @ inverse_root
    normalized = 0.5 * (normalized + normalized.T)
    ratios, vectors = np.linalg.eigh(normalized)
    y = vectors[:, -1]
    vector = inverse_root @ y
    vector /= np.linalg.norm(vector)
    separation = float(ratios[-1] - ratios[-2]) if ratios.size > 1 else math.inf
    near_count = int(np.sum(ratios >= ratios[-1] - 1.0e-10))
    return float(ratios[-1]), vector, minimum, separation, near_count


def physical_boundary_fraction(coefficients: np.ndarray, length: float, fraction: float = 0.1) -> float:
    mode = (coefficients.size - 1) // 2
    indices = np.arange(-mode, mode + 1, dtype=float)
    grid = np.linspace(-0.5 * length, 0.5 * length, 16_385)
    values = np.exp(2j * np.pi * np.outer(grid, indices) / length) @ coefficients
    density = np.abs(values) ** 2 / length
    total = float(np.trapz(density, grid))
    boundary = np.abs(grid) >= (0.5 - fraction) * length
    boundary_mass = float(np.trapz(density * boundary, grid))
    return boundary_mass / total


def mode_diagnostics(
    vector: np.ndarray,
    length: float,
    atoms: list[tuple[int, float, np.ndarray]],
) -> dict[str, float | str]:
    mode = (vector.size - 1) // 2
    indices = np.arange(-mode, mode + 1, dtype=float)
    mass = np.abs(vector) ** 2
    mass /= np.sum(mass)
    rms_index = float(np.sqrt(np.sum(indices * indices * mass)))
    central_mass = float(np.sum(mass[np.abs(indices) <= max(1, mode // 4)]))
    edge_mass = float(np.sum(mass[np.abs(indices) >= max(1, math.ceil(0.8 * mode))]))
    reversal = vector[::-1]
    even_error = float(np.linalg.norm(vector - reversal))
    odd_error = float(np.linalg.norm(vector + reversal))
    parity = "even" if even_error <= odd_error else "odd"
    parity_error = min(even_error, odd_error)

    atom_values: list[tuple[float, int, float]] = []
    for n, weight, full_atom in atoms:
        atom = full_atom
        value = float(weight * (vector @ atom @ vector))
        atom_values.append((abs(value), n, value))
    atom_values.sort(reverse=True)
    total_absolute = sum(item[0] for item in atom_values)
    top_absolute = sum(item[0] for item in atom_values[: min(5, len(atom_values))])
    top_label = ",".join(str(item[1]) for item in atom_values[:3]) or "none"
    return {
        "rms_index": rms_index,
        "central_mass": central_mass,
        "fourier_edge_mass": edge_mass,
        "physical_boundary_mass": physical_boundary_fraction(vector, length),
        "parity": parity,
        "parity_error": parity_error,
        "atom_top5_fraction": top_absolute / total_absolute if total_absolute else 0.0,
        "top_atoms": top_label,
    }


def rayleigh(matrix: np.ndarray, vector: np.ndarray) -> float:
    return float(vector @ matrix @ vector)


def parse_csv_numbers(text: str, cast):
    return [cast(piece.strip()) for piece in text.split(",") if piece.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lambdas", default="1.5,2.2,3,5,10")
    parser.add_argument("--modes", default="2,4,6,8,10")
    parser.add_argument("--quadrature", type=int, default=512)
    args = parser.parse_args()
    lambdas = parse_csv_numbers(args.lambdas, float)
    modes = parse_csv_numbers(args.modes, int)
    if not lambdas or min(lambdas) <= 1.0:
        parser.error("all lambdas must exceed 1")
    if not modes or min(modes) < 1:
        parser.error("all Fourier cutoffs must be positive")
    if args.quadrature < 64:
        parser.error("quadrature order must be at least 64")
    max_mode = max(modes)

    print("Phase 106.19 compensated-spectrum probe (float64; NOT A PROOF)")
    print(f"c_*={C_STAR:.15g}, modes={modes}, Gauss order={args.quadrature}")
    print(
        " lambda   L      K  identity     min(W)      max-ratio  gen-margin "
        "  E_min  sep-top nrad rms-k  low-mass edge-k boundary parity  atom5  top-atoms"
    )
    worst_identity = 0.0
    for lam in lambdas:
        components = compensated_components(lam, max_mode, args.quadrature)
        for mode in modes:
            w = central_slice(components.weil, max_mode, mode)
            e_star = central_slice(components.e_star, max_mode, mode)
            a_delta = central_slice(components.a_delta, max_mode, mode)
            prime = central_slice(components.prime, max_mode, mode)
            main_term = central_slice(components.main, max_mode, mode)
            identity = np.eye(2 * mode + 1)
            assembled = e_star - C_STAR * identity - a_delta
            residual = float(
                np.linalg.norm(w - assembled, ord="fro")
                / max(1.0, np.linalg.norm(w, ord="fro"))
            )
            worst_identity = max(worst_identity, residual)
            minimum_w = float(np.linalg.eigvalsh(w)[0])

            ratio, vector, minimum_e, top_separation, near_count = generalized_extremal(
                e_star, a_delta + C_STAR * identity
            )
            smooth_ratio, _, _, _, _ = generalized_extremal(
                e_star, -main_term + C_STAR * identity
            )
            leave_one_out: list[tuple[float, int]] = []
            for n, weight, full_atom in components.atom_matrices:
                atom = central_slice(full_atom, max_mode, mode)
                omitted_ratio, _, _, _, _ = generalized_extremal(
                    e_star,
                    a_delta - weight * atom + C_STAR * identity,
                )
                leave_one_out.append((omitted_ratio, n))
            worst_omission, worst_omitted_atom = max(
                leave_one_out, default=(smooth_ratio, 0)
            )
            violating_omissions = sum(
                omitted_ratio > 1.0 + 1.0e-8
                for omitted_ratio, _ in leave_one_out
            )
            diagnostics = mode_diagnostics(
                vector,
                components.length,
                [
                    (n, weight, central_slice(atom, max_mode, mode))
                    for n, weight, atom in components.atom_matrices
                ],
            )
            # These values make visible whether A_Delta is a small residual
            # or a cancellation of two much larger prime/PNT components.
            p_value = rayleigh(prime, vector)
            m_value = rayleigh(main_term, vector)
            delta_value = rayleigh(a_delta, vector)
            cancellation = abs(delta_value) / max(1.0e-300, abs(p_value) + abs(m_value))
            print(
                f"{lam:7.2f} {components.length:6.3f} {mode:3d} "
                f"{residual:9.1e} {minimum_w:11.3e} {ratio:11.8f} "
                f"{1.0-ratio:10.2e} {minimum_e:8.2e} {top_separation:8.1e} "
                f"{near_count:4d} "
                f"{diagnostics['rms_index']:6.2f} {diagnostics['central_mass']:8.3f} "
                f"{diagnostics['fourier_edge_mass']:6.3f} "
                f"{diagnostics['physical_boundary_mass']:8.3f} "
                f"{str(diagnostics['parity'])[0]}:{diagnostics['parity_error']:.1e} "
                f"{diagnostics['atom_top5_fraction']:6.3f} {diagnostics['top_atoms']}"
            )
            print(
                f"          extremal arithmetic: prime={p_value:+.5e}, "
                f"PNT-main={m_value:+.5e}, Delta={delta_value:+.5e}, "
                f"|Delta|/(|prime|+|main|)={cancellation:.3e}, "
                f"without atoms={smooth_ratio:.5f}, "
                f"worst one-atom omission={worst_omission:.5f}@n={worst_omitted_atom}, "
                f"violating omissions={violating_omissions}/{len(leave_one_out)}"
            )

    print(f"worst relative matrix-identity residual: {worst_identity:.3e}")
    if worst_identity > 2.0e-8:
        raise SystemExit("FAIL: compensated and source Weil matrices disagree")
    print(
        "PASS: the independent compensated assembly matches the 106.04 Weil "
        "matrix.  Spectral margins and mode labels above are diagnostics only."
    )


if __name__ == "__main__":
    main()
