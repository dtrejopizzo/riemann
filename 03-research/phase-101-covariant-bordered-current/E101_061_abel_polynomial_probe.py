#!/usr/bin/env python3
"""Measure the bilateral Abel polynomials in canonical rectangular CCM blocks."""

from pathlib import Path
import sys

import mpmath as mp


RESEARCH = Path(__file__).resolve().parent.parent
P76 = RESEARCH / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(P76))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_009_prolate_overlap_probe import coefficients  # noqa: E402


def dot(row, col):
    return mp.fsum(row[j] * col[j] for j in range(len(row)))


def norm2(values):
    return mp.sqrt(mp.fsum(abs(value) ** 2 for value in values))


def horner(coeff, value):
    total = mp.mpc(0)
    for item in reversed(coeff):
        total = total * value + item
    return total


def submatrix(matrix, positions_r, positions_c):
    out = mp.matrix(len(positions_r), len(positions_c))
    for i, row in enumerate(positions_r):
        for j, col in enumerate(positions_c):
            out[i, j] = matrix[row, col]
    return out


def symbol_value(matrix, positions, index, length):
    if index == 0:
        return mp.mpf(0)
    pos = positions[index]
    zero = positions[0]
    d_index = 2 * mp.pi * index / length
    return -(length / 2) * d_index * matrix[pos, zero]


def polynomial_norm(coeff, grid_size=2048):
    best = mp.mpf(0)
    where = mp.mpf(0)
    for j in range(grid_size + 1):
        t = mp.mpf(j) / grid_size
        value = abs(horner(coeff, t))
        if value > best:
            best = value
            where = t
    return best, where


def section_data(matrix, all_indices, length, coeff, n_modes, z):
    positions = {index: j for j, index in enumerate(all_indices)}
    rows = list(range(-n_modes, n_modes + 1))
    cols = list(range(-n_modes, n_modes + 2))
    row_pos = [positions[index] for index in rows]
    col_pos = [positions[index] for index in cols]
    block = submatrix(matrix, row_pos, col_pos)

    size = len(cols)
    bordered = mp.matrix(size, size)
    for j in range(size):
        bordered[0, j] = 1
    for i in range(len(rows)):
        for j in range(size):
            bordered[i + 1, j] = block[i, j]

    c = [z / (z - 2 * mp.pi * index / length) for index in cols]
    x = mp.lu_solve(bordered.T, mp.matrix(c))
    boundary = x[0]
    p = [x[j + 1] for j in range(len(rows))]

    e0 = mp.matrix(size, 1)
    e0[0] = 1
    y = mp.lu_solve(bordered, e0)

    kraw = [coeff[index] for index in cols]
    alpha = mp.fsum(kraw)
    k = [value / alpha for value in kraw]
    b_model = dot(c, k)

    q = [c[j] - boundary for j in range(size)]
    dual_residual = []
    for j in range(size):
        dual_residual.append(
            mp.fsum(p[i] * block[i, j] for i in range(len(rows))) - q[j]
        )

    row_symbol = {
        index: symbol_value(matrix, positions, index, length) for index in rows
    }
    col_symbol = {
        index: symbol_value(matrix, positions, index, length) for index in cols
    }
    a = 2 / length
    displacement_residual = []
    for i, row_index in enumerate(rows):
        d_row = 2 * mp.pi * row_index / length
        for j, col_index in enumerate(cols):
            d_col = 2 * mp.pi * col_index / length
            displacement_residual.append(
                (d_row - d_col) * block[i, j]
                + a * (row_symbol[row_index] - col_symbol[col_index])
            )

    model_residual = [
        mp.fsum(block[i, j] * k[j] for j in range(size))
        for i in range(len(rows))
    ]
    scalar_residual = dot(p, model_residual) / b_model

    normalizations = {
        "Bk": b_model,
        "By": boundary,
        "p2": norm2(p),
    }
    polynomial_data = {}
    for name, scale in normalizations.items():
        p_scaled = {rows[j]: p[j] / scale for j in range(len(rows))}
        pa = []
        pb = []
        for r in range(2 * n_modes + 1):
            right = n_modes - r
            left = r - n_modes
            pa.append(
                p_scaled[right] * row_symbol[right]
                - p_scaled[left] * row_symbol[left]
            )
            pb.append(p_scaled[right] + p_scaled[left])
        pa_norm, pa_where = polynomial_norm(pa)
        pb_norm, pb_where = polynomial_norm(pb)
        polynomial_data[name] = (pa_norm, pa_where, pb_norm, pb_where)

    return {
        "boundary": boundary,
        "b_model": b_model,
        "alpha": alpha,
        "p_norm": norm2(p),
        "dual_residual": norm2(dual_residual),
        "displacement_residual": max(abs(value) for value in displacement_residual),
        "scalar_residual": scalar_residual,
        "polynomials": polynomial_data,
        "normalization": abs(dot(c, [y[j] for j in range(size)]) - boundary),
    }


def run_build(label, planted, n_max=6, dps=70):
    mp.mp.dps = dps
    matrix, indices, length = build_mp(
        6,
        n_max + 1,
        dps,
        planted=planted,
    )
    coeff = coefficients(mp.mpf(6), n_max + 1, length)
    z = mp.j
    print(label)
    print(
        "N PA_Bk PB_Bk PA_By PB_By PA_p2 PB_p2 "
        "dual displacement scalar"
    )
    for n_modes in range(3, n_max + 1):
        data = section_data(matrix, indices, length, coeff, n_modes, z)
        bk = data["polynomials"]["Bk"]
        by = data["polynomials"]["By"]
        p2 = data["polynomials"]["p2"]
        print(
            f"{n_modes:2d}"
            f" {mp.nstr(bk[0], 7):>11} {mp.nstr(bk[2], 7):>11}"
            f" {mp.nstr(by[0], 7):>11} {mp.nstr(by[2], 7):>11}"
            f" {mp.nstr(p2[0], 7):>11} {mp.nstr(p2[2], 7):>11}"
            f" {mp.nstr(data['dual_residual'], 3):>9}"
            f" {mp.nstr(data['displacement_residual'], 3):>12}"
            f" {mp.nstr(abs(data['scalar_residual']), 5):>11}"
        )
    print()


def run():
    run_build("zeta", None)
    run_build(
        "inserted quartet",
        ("14.134725141734693790", "0.30", "5.0"),
    )


if __name__ == "__main__":
    run()
