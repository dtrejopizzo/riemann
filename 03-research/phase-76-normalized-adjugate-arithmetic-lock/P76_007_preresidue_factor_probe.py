#!/usr/bin/env python3
"""Test whether critical selectivity exists before taking the ground residue."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp, vec_norm


def row(t, idx, L):
    return mp.matrix([1 / (t - 2 * mp.pi * n / L) for n in idx])


def residue_scaled(H, mu, delta, r):
    eye = mp.eye(H.rows)
    return delta * (r.T * ((mu + delta) * eye - H) ** -1 * r)[0] / (vec_norm(r) ** 2)


def run():
    mp.mp.dps = 70
    H, idx, L = build_mp(6, 5, 70)
    vals, vecs = mp.eigsy(H)
    mu = vals[0]
    gap = vals[1] - mu
    gamma = mp.mpf("14.134725141734693790")
    rc = row(gamma, idx, L)
    rn = row(gamma + mp.mpf("0.125"), idx, L)
    ac = abs((rc.T * vecs[:, 0])[0]) ** 2 / vec_norm(rc) ** 2
    an = abs((rn.T * vecs[:, 0])[0]) ** 2 / vec_norm(rn) ** 2

    print("P76.007 pre-residue factor probe")
    print("mu", mp.nstr(mu, 12), "gap", mp.nstr(gap, 12))
    print("residue Acrit", mp.nstr(ac, 12), "Anear", mp.nstr(an, 12), "ratio", mp.nstr(ac/an, 8))
    print("alpha=-delta/gap       Rcrit          Rnear       |ratio|")
    for alpha_text in ("1e-8", "1e-5", "1e-3", "0.1", "1", "10", "1e4"):
        alpha = mp.mpf(alpha_text)
        delta = -alpha * gap
        fc = residue_scaled(H, mu, delta, rc)
        fn = residue_scaled(H, mu, delta, rn)
        print(
            f"{alpha_text:>10} {mp.nstr(fc,10):>14}"
            f" {mp.nstr(fn,10):>14} {mp.nstr(abs(fc/fn),8):>12}"
        )


if __name__ == "__main__":
    run()
