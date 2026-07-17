#!/usr/bin/env python3
"""Test the entire even boundary transfer as a canonical Xi approximant."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp


def xi_norm(t):
    s = mp.mpf("0.5") + 1j * t
    xi = mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    s0 = mp.mpf("0.5")
    xi0 = mp.mpf("0.5") * s0 * (s0 - 1) * mp.power(mp.pi, -s0 / 2) * mp.gamma(s0 / 2) * mp.zeta(s0)
    return mp.re(xi / xi0)


def right_transfer_data(H, idx):
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return idx[-1], idx[1:-1], A ** -1 * b


def transfer(z, db_idx, inner_idx, x, L):
    db = 2 * mp.pi * db_idx / L
    return 1 / (z - db) - sum(x[j] / (z - 2 * mp.pi * inner_idx[j] / L) for j in range(x.rows))


def entire_transfer(z, db_idx, inner_idx, x, L):
    if z == 0:
        zero_pos = inner_idx.index(0)
        return -(L / 2) * x[zero_pos]
    return mp.sin(z * L / 2) * transfer(z, db_idx, inner_idx, x, L)


def run():
    mp.mp.dps = 70
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 70)
    grid = [mp.mpf(j) / 2 for j in range(25)]
    target = [xi_norm(t) for t in grid]
    target_norm = mp.sqrt(sum(abs(v) ** 2 for v in target))
    print("P76.018 even entire boundary characteristic")
    print("N       relL2(Xi)      relSup(Xi)      odd/evenL2       valueAtGamma")
    gamma = mp.mpf("14.134725141734693790")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        db, inner, x = right_transfer_data(H, idx)
        phi0 = entire_transfer(mp.mpf(0), db, inner, x, L)
        even_vals = []
        odd_vals = []
        for t in grid:
            plus = entire_transfer(t, db, inner, x, L)
            minus = entire_transfer(-t, db, inner, x, L)
            even_vals.append((plus + minus) / (2 * phi0))
            odd_vals.append((plus - minus) / (2 * phi0))
        errors = [even_vals[j] - target[j] for j in range(len(grid))]
        rel_l2 = mp.sqrt(sum(abs(e) ** 2 for e in errors)) / target_norm
        rel_sup = max(abs(e) for e in errors) / max(abs(v) for v in target)
        odd_ratio = mp.sqrt(sum(abs(v) ** 2 for v in odd_vals)) / mp.sqrt(
            sum(abs(v) ** 2 for v in even_vals)
        )
        gplus = entire_transfer(gamma, db, inner, x, L)
        gminus = entire_transfer(-gamma, db, inner, x, L)
        gnorm = abs((gplus + gminus) / (2 * phi0))
        print(
            f"{n_modes:2d} {mp.nstr(rel_l2,9):>16} {mp.nstr(rel_sup,9):>16}"
            f" {mp.nstr(odd_ratio,9):>16} {mp.nstr(gnorm,9):>18}"
        )


if __name__ == "__main__":
    run()
