#!/usr/bin/env python3
"""Test the projective leakage left by the Fourier-position transfer."""

from pathlib import Path
import sys

import mpmath as mp


RESEARCH = Path(__file__).resolve().parent.parent
P76 = RESEARCH / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(P76))

from P76_002_mp_entry_audit import build_mp  # noqa: E402


def submatrix(matrix, positions, rows, cols):
    return mp.matrix(
        [[matrix[positions[i], positions[j]] for j in cols] for i in rows]
    )


def boundary_data(block, rows, cols, length, z):
    size = len(cols)
    bordered = mp.matrix(size, size)
    for j in range(size):
        bordered[0, j] = 1
    for i in range(len(rows)):
        for j in range(size):
            bordered[i + 1, j] = block[i, j]

    d_cols = [2 * mp.pi * index / length for index in cols]
    c = mp.matrix([z / (z - value) for value in d_cols])
    dual = mp.lu_solve(bordered.T, c)
    boundary = dual[0]
    p = mp.matrix([dual[j + 1] for j in range(len(rows))])

    e0 = mp.matrix(size, 1)
    e0[0] = 1
    y = mp.lu_solve(bordered, e0)
    return boundary, p, y


def projective_leakage(
    arithmetic,
    prime,
    positions,
    length,
    n_modes,
    z,
    eta,
):
    rows = list(range(-n_modes, n_modes + 1))
    cols = list(range(-n_modes, n_modes + 2))
    block = submatrix(arithmetic, positions, rows, cols)
    direction = submatrix(prime, positions, rows, cols)
    boundary, p, y = boundary_data(block, rows, cols, length, z)

    d_rows = [2 * mp.pi * index / length for index in rows]
    d_cols = [2 * mp.pi * index / length for index in cols]
    zeta = z + eta
    g = mp.matrix([y[j] / (d_cols[j] - zeta) for j in range(len(cols))])
    hg = direction * g
    leakage = mp.fsum(
        p[i] * (d_rows[i] - zeta) * hg[i] for i in range(len(rows))
    )

    commutator = mp.matrix(len(rows), len(cols))
    for i in range(len(rows)):
        for j in range(len(cols)):
            commutator[i, j] = (
                d_rows[i] - d_cols[j]
            ) * direction[i, j]

    direct = mp.fsum(p[i] * (direction * y)[i] for i in range(len(rows)))
    transferred = leakage - mp.fsum(
        p[i] * (commutator * g)[i] for i in range(len(rows))
    )
    transfer_error = abs(direct - transferred)
    return leakage / boundary, transfer_error


def run():
    mp.mp.dps = 70
    lam = 6
    n_max = 5
    arithmetic, indices, length = build_mp(
        lam,
        n_max + 1,
        70,
        include_arith=True,
    )
    archimedean, indices_a, length_a = build_mp(
        lam,
        n_max + 1,
        70,
        include_arith=False,
    )
    if indices != indices_a or length != length_a:
        raise RuntimeError("incompatible builds")
    prime = archimedean - arithmetic
    positions = {index: j for j, index in enumerate(indices)}

    eta = mp.mpf("0.25")
    sigmas = [mp.mpf(value) for value in ("0.6", "0.75", "1", "1.5", "2")]
    reference = mp.mpf("1")
    print("N sigma bilateral_difference transfer_error")
    for n_modes in range(2, n_max + 1):
        values = {}
        errors = {}
        for sigma in sigmas:
            plus, err_plus = projective_leakage(
                arithmetic,
                prime,
                positions,
                length,
                n_modes,
                mp.j * sigma,
                eta,
            )
            minus, err_minus = projective_leakage(
                arithmetic,
                prime,
                positions,
                length,
                n_modes,
                -mp.j * sigma,
                eta,
            )
            values[sigma] = plus + minus
            errors[sigma] = max(err_plus, err_minus)
        for sigma in sigmas:
            difference = values[sigma] - values[reference]
            print(
                f"{n_modes:2d} {mp.nstr(sigma, 3):>5}"
                f" {mp.nstr(difference, 13):>24}"
                f" {mp.nstr(errors[sigma], 3):>14}"
            )


if __name__ == "__main__":
    run()
