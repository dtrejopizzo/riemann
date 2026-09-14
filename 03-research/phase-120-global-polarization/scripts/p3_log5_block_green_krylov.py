#!/usr/bin/env python3
"""Block-Green attack for the five delicate log(5)/2 directions.

Binary64 diagnostic only.  It applies the physical compressed operator,
projects away the primitive V260 chart, and uses block Krylov Galerkin solves
for (Q260 A Q260)^(-1).  At every Krylov level it reports the rigorous-form
template

    Green <= Galerkin_Green + delta^(-1) residual^* residual,

with delta=0.218 inherited from Q200.  Only intervalization is missing if
the resulting five-dimensional Schur margin is comfortably positive.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "base", HERE / "p3_log5_full_residual_diagnostic.py"
)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

T = 0.5 * np.log(5.0)


def main() -> None:
    data_path = Path(os.environ.get(
        "P3_LOG5_V260", "/tmp/p3_log5_v260_scalar_gap_2p21.npz"
    ))
    data = np.load(data_path)
    if "vectors" in data and "values" in data:
        # Directed D.148 output: the columns are already the physical Ritz
        # vectors and the finite compression is diagonal in this frame.
        frame = np.asarray(data["vectors"], dtype=float)
        finite = np.diag(np.asarray(data["values"], dtype=float))
    else:
        frame = np.asarray(data["frame"], dtype=float)
        finite = np.asarray(data["finite"], dtype=float)
    n_modes, width = frame.shape
    assert (n_modes, width) == (260, 258)

    delicate = int(os.environ.get("P3_LOG5_DELICATE", "5"))
    steps = int(os.environ.get("P3_LOG5_KRYLOV", "6"))
    points = int(os.environ.get("P3_LOG5_POINTS", str(2**20)))
    box = float(os.environ.get("P3_LOG5_BOX", "32"))
    cells = int(os.environ.get("P3_LOG5_CELLS", "6000"))
    qorder = int(os.environ.get("P3_LOG5_QORDER", "6"))
    delta = float(os.environ.get("P3_LOG5_DELTA", ".218"))

    # Diagonalize the measured V260 compression.  The first columns are the
    # dangerous finite directions; all other finite directions are already
    # eliminated by choosing the Ritz frame.
    finite = (finite + finite.T) / 2
    finite_e, finite_u = np.linalg.eigh(finite)
    dcoeff = frame @ finite_u[:, :delicate]

    breaks = {-T, T}
    for integer in (2, 3, 4):
        shift = np.log(float(integer))
        for point in (-T + shift, T - shift):
            if -T < point < T:
                breaks.add(point)
    coarse = np.linspace(-T, T, cells + 1)
    edges = np.unique(np.concatenate((coarse, np.array(sorted(breaks)))))
    nodes, weights = leggauss(qorder)
    mid = (edges[:-1] + edges[1:]) / 2
    half = (edges[1:] - edges[:-1]) / 2
    tq = (mid[:, None] + half[:, None] * nodes).reshape(-1)
    wq = (half[:, None] * np.broadcast_to(weights, (len(half), qorder))).reshape(-1)

    dx = box / points
    grid = (np.arange(points) - points // 2) * dx
    inside = np.flatnonzero(np.abs(grid) <= T)
    frequency = 2 * np.pi * np.fft.rfftfreq(points, d=dx)
    psi_q = base.digamma_complex(np.array([0.25]))[0].real
    symbol = base.digamma_complex(0.25 + 0.5j * frequency).real - psi_q
    m0 = np.log(np.pi) - psi_q

    chart_q = base.synthesize(tq / T, frame)
    chart_gram = chart_q.T @ (wq[:, None] * chart_q)
    moment_q = np.column_stack((np.exp(tq / 2), np.exp(-tq / 2)))
    moment_grid = np.zeros((points, 2), dtype=float)
    moment_grid[inside, 0] = np.exp(grid[inside] / 2)
    moment_grid[inside, 1] = np.exp(-grid[inside] / 2)
    moment_gram = moment_q.T @ (wq[:, None] * moment_q)

    def sample(values: np.ndarray) -> np.ndarray:
        return base.shifted(values, grid, tq)

    def apply_a(values: np.ndarray) -> np.ndarray:
        image = np.fft.irfft(
            np.fft.rfft(values, axis=0) * symbol[:, None], n=points, axis=0
        )
        image -= m0 * values
        for integer, mangoldt in ((2, np.log(2.0)), (3, np.log(3.0)),
                                  (4, np.log(2.0))):
            shift = np.log(float(integer))
            coefficient = mangoldt / np.sqrt(float(integer))
            image[inside] -= coefficient * (
                base.shifted(values, grid, grid[inside] + shift)
                + base.shifted(values, grid, grid[inside] - shift)
            )
        image[:inside[0]] = 0.0
        image[inside[-1] + 1:] = 0.0
        return image

    def project_q(values: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        values_q = sample(values)
        # First compress to the full two-Tate primitive Hilbert space.
        polar = np.linalg.solve(
            moment_gram, moment_q.T @ (wq[:, None] * values_q)
        )
        values = values - moment_grid @ polar
        values_q = values_q - moment_q @ polar
        # Then remove its finite primitive V260 chart.
        coeff = np.linalg.solve(
            chart_gram, chart_q.T @ (wq[:, None] * values_q)
        )
        projected = np.zeros_like(values)
        projected[inside] = base.synthesize(grid[inside] / T, frame @ coeff)
        qvalues = values - projected
        return qvalues, values_q - chart_q @ coeff

    def inner(left_q: np.ndarray, right_q: np.ndarray) -> np.ndarray:
        return left_q.T @ (wq[:, None] * right_q)

    def orthonormalize(values: np.ndarray, values_q: np.ndarray,
                       old: list[tuple[np.ndarray, np.ndarray]]) \
            -> tuple[np.ndarray, np.ndarray]:
        for _ in range(2):
            for old_grid, old_q in old:
                coefficient = inner(old_q, values_q)
                values -= old_grid @ coefficient
                values_q -= old_q @ coefficient
        gram = inner(values_q, values_q)
        gram = (gram + gram.T) / 2
        eigen, vectors = np.linalg.eigh(gram)
        keep = eigen > max(eigen[-1] * 1e-11, 1e-14)
        transform = vectors[:, keep] * (1 / np.sqrt(eigen[keep]))
        return values @ transform, values_q @ transform

    source = np.zeros((points, delicate), dtype=float)
    source[inside] = base.synthesize(grid[inside] / T, dcoeff)
    c_grid, c_q = project_q(apply_a(source))
    c_gram = inner(c_q, c_q)
    print("finite delicate values", finite_e[:delicate], flush=True)
    print("initial coupling Gram eigenvalues", np.linalg.eigvalsh(c_gram), flush=True)

    blocks: list[tuple[np.ndarray, np.ndarray]] = []
    actions: list[tuple[np.ndarray, np.ndarray]] = []
    first_grid, first_q = orthonormalize(c_grid.copy(), c_q.copy(), blocks)
    blocks.append((first_grid, first_q))

    for level in range(steps):
        w_grid, w_q_values = blocks[level]
        aw_grid, aw_q = project_q(apply_a(w_grid))
        actions.append((aw_grid, aw_q))

        all_wq = np.column_stack([item[1] for item in blocks])
        all_awq = np.column_stack([item[1] for item in actions])
        rhs = inner(all_wq, c_q)
        operator = inner(all_wq, all_awq)
        operator = (operator + operator.T) / 2
        op_e = np.linalg.eigvalsh(operator)
        if op_e[0] <= 0:
            print("level", level + 1, "indefinite Galerkin operator", op_e[0])
            break
        solution = np.linalg.solve(operator, rhs)
        green = rhs.T @ solution
        residual_q = c_q - all_awq @ solution
        residual_gram = inner(residual_q, residual_q)
        upper_green = green + residual_gram / delta
        gate = np.diag(finite_e[:delicate]) - upper_green
        gate = (gate + gate.T) / 2
        gate_e = np.linalg.eigvalsh(gate)
        print(
            "level", level + 1,
            "dimension", operator.shape[0],
            "Aq min", op_e[0],
            "residual trace", np.trace(residual_gram),
            "gate min/count", gate_e[0], int(np.sum(gate_e <= 0)),
            flush=True,
        )

        if level + 1 == steps:
            break
        candidate_grid, candidate_q = orthonormalize(
            aw_grid.copy(), aw_q.copy(), blocks
        )
        if candidate_grid.shape[1] == 0:
            print("Krylov space closed at level", level + 1)
            break
        blocks.append((candidate_grid, candidate_q))

    print("DIAGNOSTIC ONLY: block Green Krylov, no directed sign asserted")


if __name__ == "__main__":
    main()
