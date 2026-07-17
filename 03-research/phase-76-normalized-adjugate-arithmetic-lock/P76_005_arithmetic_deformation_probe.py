#!/usr/bin/env python3
"""Track the normalized lock under H(t)=H_arch-t H_prime."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp, vec_norm


def qnorm(gamma, idx, L, xi):
    r = mp.matrix([1 / (gamma - 2 * mp.pi * n / L) for n in idx])
    return abs((r.T * xi)[0]) / vec_norm(r)


def run():
    mp.mp.dps = 60
    full, idx, L = build_mp(6, 4, 60, include_arith=True)
    arch, _, _ = build_mp(6, 4, 60, include_arith=False)
    prime = arch - full
    gamma = mp.mpf("14.134725141734693790")
    print("P76.005 arithmetic deformation H(t)=H_arch-t H_prime")
    print("t             mu             gap          qgamma          qnear")
    samples = (
        ("0", mp.mpf("0")),
        ("0.5", mp.mpf("0.5")),
        ("0.9", mp.mpf("0.9")),
        ("0.99", mp.mpf("0.99")),
        ("1-1e-4", 1 - mp.mpf("1e-4")),
        ("1-1e-8", 1 - mp.mpf("1e-8")),
        ("1-1e-12", 1 - mp.mpf("1e-12")),
        ("1-1e-15", 1 - mp.mpf("1e-15")),
        ("1", mp.mpf("1")),
    )
    for t_text, t in samples:
        H = arch - t * prime
        vals, vecs = mp.eigsy(H)
        xi = vecs[:, 0]
        qc = qnorm(gamma, idx, L, xi)
        qn = qnorm(gamma + mp.mpf("0.125"), idx, L, xi)
        print(
            f"{t_text:>8} {mp.nstr(vals[0],10):>14}"
            f" {mp.nstr(vals[1]-vals[0],10):>14}"
            f" {mp.nstr(qc,10):>15} {mp.nstr(qn,10):>15}"
        )


if __name__ == "__main__":
    run()
