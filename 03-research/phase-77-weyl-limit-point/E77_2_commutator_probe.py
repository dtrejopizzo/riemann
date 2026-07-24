#!/usr/bin/env python3
"""E77.2 finite commutator audit for the CCM mesh operator.

RDP-1 gives an exact rank-two displacement commutator.  This probe checks
the identity and measures the size of the blind subspace left by the two
generator moments.  The goal is to decide whether the raw commutator can
support a Mourre/Kato-Putnam absence-of-eigenvalue proof.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_011_loewner_identity_probe import symbols  # noqa: E402


GAMMA = "14.134725141734693790"


def frobenius(M: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(M[i, j]) ** 2 for i in range(M.rows) for j in range(M.cols)))


def vec_norm(v: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def serial(x: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(x, digits)


def sine_symbol(t: mp.mpf, L: mp.mpf, lam: mp.mpf, planted) -> mp.mpf:
    value = symbols(t, L, lam)[0]
    if planted is None:
        return value
    gamma0, beta, strength = (mp.mpf(x) for x in planted)
    spectral_point = gamma0 - 1j * beta
    planted_sine = mp.quad(lambda y: mp.sin(t * y) * mp.cos(spectral_point * y), [0, L])
    return value + strength * 2 * mp.re(planted_sine)


def run_case(lam_int: int, n_modes: int, dps: int, planted=None) -> dict:
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    H, idx, L = build_mp(lam_int, n_modes, dps, planted=planted)
    d = mp.matrix([2 * mp.pi * n / L for n in idx])
    D = mp.diag(d)
    s = mp.matrix([sine_symbol(d[j], L, lam, planted) for j in range(len(idx))])
    one = mp.matrix([1 for _ in idx])

    comm = D * H - H * D
    rank_two = -(2 / L) * (s * one.T - one * s.T)
    rel_error = frobenius(comm - rank_two) / frobenius(comm)
    rank_two_norm = frobenius(rank_two)

    # The commutator vanishes on vectors orthogonal to both generators.
    G = mp.matrix(
        [
            [(one.T * one)[0], (one.T * s)[0]],
            [(s.T * one)[0], (s.T * s)[0]],
        ]
    )
    blind_dim = len(idx) - 2
    vals, vecs = mp.eigsy(H)
    eigen_rows = []
    sn = vec_norm(s)
    on = vec_norm(one)
    for j in range(min(6, vals.rows)):
        v = vecs[:, j]
        one_moment = abs((one.T * v)[0]) / (on * vec_norm(v))
        s_moment = abs((s.T * v)[0]) / (sn * vec_norm(v))
        generator_mass = mp.matrix([[one_moment], [s_moment]])
        eigen_rows.append(
            {
                "j": j,
                "eigenvalue": serial(vals[j]),
                "one_moment_normalized": serial(one_moment),
                "s_moment_normalized": serial(s_moment),
                "generator_mass_l2": serial(vec_norm(generator_mass)),
            }
        )

    return {
        "lambda": lam_int,
        "N": n_modes,
        "dim": len(idx),
        "dps": dps,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "commutator_relative_error": serial(rel_error),
        "commutator_frobenius": serial(frobenius(comm)),
        "rank_two_frobenius": serial(rank_two_norm),
        "blind_subspace_dimension": blind_dim,
        "blind_fraction": serial(mp.mpf(blind_dim) / len(idx)),
        "generator_gram_det": serial(G[0, 0] * G[1, 1] - G[0, 1] * G[1, 0]),
        "lowest_eigenvectors": eigen_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambdas", default="6,7,8")
    parser.add_argument("--modes", default="8,12,16,18")
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--output", type=Path, default=HERE / "E77_2_commutator_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.2 requires dps >= 50")

    lambdas = [int(x) for x in args.lambdas.split(",") if x]
    modes = [int(x) for x in args.modes.split(",") if x]
    cases = []
    for lam in lambdas:
        for n_modes in modes:
            print(f"CASE zeta lambda={lam} N={n_modes}", flush=True)
            cases.append(run_case(lam, n_modes, args.dps))
            print(f"CASE planted lambda={lam} N={n_modes}", flush=True)
            cases.append(run_case(lam, n_modes, args.dps, planted=(GAMMA, "0.30", "5.0")))
            args.output.write_text(json.dumps({"cases": cases}, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
