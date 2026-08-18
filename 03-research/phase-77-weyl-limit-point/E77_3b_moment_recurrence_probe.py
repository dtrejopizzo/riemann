#!/usr/bin/env python3
"""E77.3b exact moment-recurrence audit.

For A = H_inner - mu I and the canonical boundary response A x = b,
RDP-2 gives the exact finite recurrence

    A D^k x = D^k b + (2/L) sum_{r=0}^{k-1} D^r
              (s <1,D^{k-1-r}x> - 1 <s,D^{k-1-r}x>).

This probe verifies the identity and measures whether the generator source
is a small/cancelling package for zeta and the planted falsifier.
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
from E77_2_commutator_probe import sine_symbol  # noqa: E402


GAMMA = "14.134725141734693790"


def serial(x: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(x, digits)


def norm(v: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def canonical_system(H: mp.matrix):
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    x = mp.lu_solve(A, b)
    return mu, A, b, x


def dpow_vec(d: mp.matrix, power: int, v: mp.matrix) -> mp.matrix:
    return mp.matrix([mp.power(d[j], power) * v[j] for j in range(v.rows)])


def recurrence_source(
    d: mp.matrix,
    s: mp.matrix,
    one: mp.matrix,
    x: mp.matrix,
    b: mp.matrix,
    L: mp.mpf,
    k: int,
) -> tuple[mp.matrix, mp.matrix, mp.matrix]:
    boundary = dpow_vec(d, k, b)
    generator = mp.matrix(x.rows, 1)
    if k > 0:
        for r in range(k):
            ell = k - 1 - r
            dx = dpow_vec(d, ell, x)
            m0 = (one.T * dx)[0]
            ms = (s.T * dx)[0]
            term = s * m0 - one * ms
            generator += dpow_vec(d, r, term)
        generator *= 2 / L
    return boundary + generator, boundary, generator


def run_case(label: str, lam_int: int, n_modes: int, dps: int, kmax: int, planted) -> dict:
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    H, idx, L = build_mp(lam_int, n_modes, dps, planted=planted)
    mu, A, b, x = canonical_system(H)
    inner_idx = idx[1:-1]
    d = mp.matrix([2 * mp.pi * n / L for n in inner_idx])
    s = mp.matrix([sine_symbol(d[j], L, lam, planted) for j in range(len(inner_idx))])
    one = mp.matrix([1 for _ in inner_idx])
    rows = []
    for k in range(kmax + 1):
        lhs = A * dpow_vec(d, k, x)
        rhs, boundary, generator = recurrence_source(d, s, one, x, b, L, k)
        residual = norm(lhs - rhs)
        rhs_norm = norm(rhs)
        boundary_norm = norm(boundary)
        generator_norm = norm(generator)
        cancellation = rhs_norm / (boundary_norm + generator_norm) if boundary_norm + generator_norm else mp.mpf(0)
        rows.append(
            {
                "k": k,
                "lhs_norm": serial(norm(lhs)),
                "rhs_norm": serial(rhs_norm),
                "boundary_norm": serial(boundary_norm),
                "generator_norm": serial(generator_norm),
                "relative_residual": serial(residual / rhs_norm if rhs_norm else residual),
                "cancellation_ratio": serial(cancellation),
            }
        )
        print(
            f"ROW {label:10s} lam={lam_int} N={n_modes:2d} k={k} "
            f"rel={serial(residual / rhs_norm if rhs_norm else residual, 8):>12s} "
            f"bn={serial(boundary_norm, 8):>12s} gn={serial(generator_norm, 8):>12s} "
            f"cancel={serial(cancellation, 8):>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam_int,
        "N": n_modes,
        "dps": dps,
        "mu": serial(mu),
        "energy": serial(norm(x) ** 2),
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambdas", default="6,7,8")
    parser.add_argument("--modes", default="12,16,18")
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--kmax", type=int, default=6)
    parser.add_argument("--output", type=Path, default=HERE / "E77_3b_moment_recurrence_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.3b requires dps >= 50")
    result = {
        "statement": "Exact RDP-2 moment recurrence for A D^k x",
        "parameters": {
            "lambdas": [int(x) for x in args.lambdas.split(",") if x],
            "modes": [int(x) for x in args.modes.split(",") if x],
            "dps": args.dps,
            "kmax": args.kmax,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for lam in result["parameters"]["lambdas"]:
        for n_modes in result["parameters"]["modes"]:
            for label, planted in [
                (f"zeta-l{lam}-n{n_modes}", None),
                (f"plant-l{lam}-n{n_modes}", (GAMMA, "0.30", "5.0")),
            ]:
                print(f"CASE {label}", flush=True)
                result["cases"].append(run_case(label, lam, n_modes, args.dps, args.kmax, planted))
                args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
