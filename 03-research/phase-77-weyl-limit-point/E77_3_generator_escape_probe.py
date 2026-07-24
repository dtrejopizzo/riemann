#!/usr/bin/env python3
"""E77.3 generator-escape probe.

E77.2 showed that the raw rank-two commutator is blind on the codimension-2
subspace orthogonal to the generators 1 and s.  This probe measures whether
the canonical boundary response escapes that blind sector after applying
low mesh powers D^k, which is the finite object needed for an explicit
displacement-kernel theorem.
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


def canonical_solution(H: mp.matrix) -> mp.matrix:
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return mp.lu_solve(A, b)


def fit(ns: list[int], values: list[mp.mpf]) -> dict | None:
    if len(ns) < 3:
        return None
    logs = [mp.log(v) for v in values]
    nbar = mp.fsum(ns) / len(ns)
    ybar = mp.fsum(logs) / len(logs)
    denom = mp.fsum((n - nbar) ** 2 for n in ns)
    slope = mp.fsum((n - nbar) * (y - ybar) for n, y in zip(ns, logs)) / denom
    return {"c": serial(slope), "points": len(ns)}


def run_case(label: str, lam_int: int, max_modes: int, dps: int, planted) -> dict:
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    rows = []
    for n_modes in range(6, max_modes + 1):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        inner_idx = idx[1:-1]
        x = canonical_solution(H)
        d = mp.matrix([2 * mp.pi * n / L for n in inner_idx])
        s = mp.matrix([sine_symbol(d[j], L, lam, planted) for j in range(len(inner_idx))])
        one = mp.matrix([1 for _ in inner_idx])
        xn = norm(x)
        sn = norm(s)
        on = norm(one)
        moment_rows = []
        for k in range(5):
            dkx = mp.matrix([mp.power(d[j], k) * x[j] for j in range(x.rows)])
            dkxn = norm(dkx)
            one_m = abs((one.T * dkx)[0]) / (on * dkxn)
            s_m = abs((s.T * dkx)[0]) / (sn * dkxn)
            moment_rows.append(
                {
                    "k": k,
                    "one": serial(one_m),
                    "s": serial(s_m),
                    "escape_l2": serial(mp.sqrt(one_m**2 + s_m**2)),
                }
            )
        rows.append(
            {
                "N": n_modes,
                "energy": serial(xn**2),
                "escape_k0": moment_rows[0]["escape_l2"],
                "escape_k1": moment_rows[1]["escape_l2"],
                "escape_k2": moment_rows[2]["escape_l2"],
                "escape_k3": moment_rows[3]["escape_l2"],
                "escape_k4": moment_rows[4]["escape_l2"],
                "moments": moment_rows,
            }
        )
        print(
            f"ROW {label:12s} lam={lam_int} N={n_modes:2d} "
            f"E={serial(xn**2, 10):>13s} esc0={moment_rows[0]['escape_l2']:>12s} "
            f"esc2={moment_rows[2]['escape_l2']:>12s} esc4={moment_rows[4]['escape_l2']:>12s}",
            flush=True,
        )
    ns = [r["N"] for r in rows]
    return {
        "label": label,
        "lambda": lam_int,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
        "fits": {
            "energy": fit(ns, [mp.mpf(r["energy"]) for r in rows]),
            "escape_k0": fit(ns, [mp.mpf(r["escape_k0"]) for r in rows]),
            "escape_k2": fit(ns, [mp.mpf(r["escape_k2"]) for r in rows]),
            "escape_k4": fit(ns, [mp.mpf(r["escape_k4"]) for r in rows]),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambdas", default="6,7,8")
    parser.add_argument("--max-modes", type=int, default=18)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--output", type=Path, default=HERE / "E77_3_generator_escape_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.3 requires dps >= 50")
    result = {"cases": []}
    for lam in [int(x) for x in args.lambdas.split(",") if x]:
        for label, planted in [
            (f"zeta-lam{lam}", None),
            (f"plant-lam{lam}", (GAMMA, "0.30", "5.0")),
        ]:
            print(f"BUILD {label}", flush=True)
            result["cases"].append(run_case(label, lam, args.max_modes, args.dps, planted))
            args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
