#!/usr/bin/env python3
"""Audit legacy cached CCM data; results require an entry-convention check."""

import json
from pathlib import Path

import mpmath as mp

from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data, xi_norm


CACHE = Path(__file__).resolve().parent.parent / "phase-61-open-problems" / ".cache_23F"


def load_matrix(lam, n_modes, kind):
    path = CACHE / f"build_lam{lam:.4f}_N{n_modes}_{kind}.json"
    data = json.loads(path.read_text())
    arch = data["Larch"]
    prime = data["Lpr"]
    size = len(arch)
    H = mp.matrix(size)
    for i in range(size):
        for j in range(size):
            H[i, j] = mp.mpf(arch[i][j]) - mp.mpf(prime[i][j])
    return H, data["idx"], mp.mpf(str(data["L"]))


def safe_error(H, idx, L):
    db, inner, x = right_transfer_data(H, idx)
    phi0 = entire_transfer(mp.mpf(0), db, inner, x, L)

    def psi(z):
        return entire_transfer(z, db, inner, x, L) * entire_transfer(-z, db, inner, x, L) / phi0**2

    points = [-1j * mp.mpf(v) for v in ("0.6", "0.75", "1.0", "1.5", "2.0")]
    errors = [abs(psi(z) - xi_norm(z) ** 2) / abs(xi_norm(z) ** 2) for z in points]
    return max(errors), errors


def run():
    mp.mp.dps = 45
    cases = [(8, 16), (10, 18), (12, 18), (14, 20), (16, 20), (18, 22), (20, 22), (22, 22)]
    print("P76.032 cached bilateral safe-axis scaling")
    print("kind lambda N N/L maxRel errors(.6,.75,1,1.5,2)")
    for kind in ("zeta", "DH"):
        for lam, n_modes in cases:
            H, idx, L = load_matrix(lam, n_modes, kind)
            worst, errors = safe_error(H, idx, L)
            print(
                f"{kind:4s} {lam:6d} {n_modes:2d} {mp.nstr(n_modes/L,6):>8}"
                f" {mp.nstr(worst,8):>10} " + ",".join(mp.nstr(e,5) for e in errors)
            )


if __name__ == "__main__":
    run()
