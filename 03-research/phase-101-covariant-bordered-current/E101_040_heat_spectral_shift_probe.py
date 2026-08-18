#!/usr/bin/env python3
"""Evaluate finite secular heat traces and the arithmetic heat defect."""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PHASE76 = ROOT / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = ROOT / "phase-77-weyl-limit-point"
PHASE78 = ROOT / "phase-78-build-neutral-lp-and-ident"
sys.path[:0] = [str(PHASE76), str(PHASE77), str(PHASE78)]

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402


def secular_roots(H, idx, L):
    _, _, db_idx, inner, x = right_transfer_data(H, idx)
    mesh = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    c = 1 - mp.fsum(x)
    K = mp.matrix(len(mesh))
    for a in range(len(mesh)):
        for b in range(len(mesh)):
            K[a, b] = (mesh[a] if a == b else 0) + x[a] * (mesh[b] - db) / c
    roots, _ = mp.eig(K)
    return [mp.re(z) for z in roots], max(abs(mp.im(z)) for z in roots)


def mangoldt(n):
    for p in range(2, n + 1):
        if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
            continue
        q = n
        while q % p == 0:
            q //= p
        if q == 1:
            return mp.log(p)
    return mp.mpf("0")


def arch_heat(v):
    epsilon = mp.mpf("1e-20")

    def integrand(u):
        return mp.exp(-u) / u - mp.exp(-u / 4 - u * u / (16 * v)) / (-mp.expm1(-u))

    integral = -mp.mpf("1.25") * epsilon + mp.quad(
        integrand, [epsilon, mp.mpf("0.01"), 1, mp.inf]
    )
    return (
        2 * mp.exp(v / 4)
        - mp.log(mp.pi) / (2 * mp.sqrt(mp.pi * v))
        + integral / (2 * mp.sqrt(mp.pi * v))
    )


def prime_heat(v, lam):
    return mp.fsum(
        mangoldt(m)
        * mp.mpf(m) ** (-mp.mpf("0.5"))
        * mp.exp(-(mp.log(m) ** 2) / (4 * v))
        for m in range(2, lam * lam + 1)
    ) / mp.sqrt(mp.pi * v)


def run_case(label, planted, lam=6, max_n=16, dps=60):
    mp.mp.dps = dps
    H, idx, L = build_mp(lam, max_n, dps, planted=planted)
    heat_times = [mp.mpf(x) for x in ("0.005", "0.01", "0.03", "0.1", "1")]
    target = {v: arch_heat(v) - prime_heat(v, lam) for v in heat_times}
    print(label, "L", mp.nstr(L, 12))
    for n in range(8, max_n + 1, 2):
        Hn, idxn = section(H, idx, max_n, n)
        roots, max_imag = secular_roots(Hn, idxn, L)
        values = [mp.fsum(mp.exp(-v * r * r) for r in roots) for v in heat_times]
        defects = [values[j] - target[v] for j, v in enumerate(heat_times)]
        print(
            "N",
            n,
            "max_imag",
            mp.nstr(max_imag, 5),
            "defects",
            " ".join(mp.nstr(z, 14) for z in defects),
            flush=True,
        )


def main():
    run_case("zeta", None)
    run_case("plant", (GAMMA, "0.30", "5.0"))


if __name__ == "__main__":
    main()
