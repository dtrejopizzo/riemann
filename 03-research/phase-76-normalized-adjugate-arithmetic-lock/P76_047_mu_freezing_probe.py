#!/usr/bin/env python3
"""Test whether the safe core log trace is stable when mu_N is frozen at zero."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import transfer
from P76_035_safe_log_derivative_probe import transfer_prime
from P76_037_core_log_derivative_probe import external_tail


def transfer_data_mu(H, idx, mu):
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return idx[-1], idx[1:-1], A ** -1 * b


def values(H, idx, L, n_modes, mu, sigmas):
    db, inner, x = transfer_data_mu(H, idx, mu)
    result = []
    for sigma in sigmas:
        z = 1j * sigma
        t = transfer(z, db, inner, x, L)
        tp = transfer_prime(z, db, inner, x, L)
        result.append(
            L * mp.coth(sigma * L / 2)
            + 2 * mp.re(1j * tp / t)
            - external_tail(sigma, L, n_modes)
        )
    return result


def run():
    mp.mp.dps = 100
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 100)
    sigmas = [mp.mpf(v) for v in ("0.6", "0.75", "1", "1.5", "2")]
    print("P76.047 mu-freezing audit, lambda=6")
    print("N             mu_N        max|J(mu)-J(0)|")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        vals, _ = mp.eigsy(H)
        mu = vals[0]
        actual = values(H, idx, L, n_modes, mu, sigmas)
        frozen = values(H, idx, L, n_modes, mp.mpf(0), sigmas)
        defect = max(abs(actual[j] - frozen[j]) for j in range(len(sigmas)))
        print(f"{n_modes:2d} {mp.nstr(mu,12):>18} {mp.nstr(defect,12):>23}")


if __name__ == "__main__":
    run()
