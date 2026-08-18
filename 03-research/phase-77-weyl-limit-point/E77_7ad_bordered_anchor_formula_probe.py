#!/usr/bin/env python3
"""Compare bordered determinant with the kernel-anchor coupling scalar."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(HERE))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def section(Hmax, idxmax, max_modes, modes):
    off = max_modes - modes
    return (
        Hmax[off : Hmax.rows - off, off : Hmax.cols - off],
        idxmax[off : len(idxmax) - off],
    )


def bordered_shifted(H, idx, L, z0):
    mu, A, db_idx, inner, _x = right_transfer_data(H, idx)
    g = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    n = A.rows
    M = mp.matrix(n + 1)
    for i in range(n):
        for j in range(n):
            M[i, j] = A[i, j]
        M[i, n] = g[i]
    for j, m in enumerate(inner):
        M[n, j] = 1 / (z0 - 2 * mp.pi * m / L)
    M[n, n] = 1 / (z0 - 2 * mp.pi * db_idx / L)
    return mu, A, g, inner, db_idx, M


def kernel_anchor_scalar(H, idx, L, z0):
    mu, A, g, inner, db_idx, M = bordered_shifted(H, idx, L, z0)
    vals, vecs = mp.eighe(A)
    idx0 = min(range(len(vals)), key=lambda j: abs(vals[j]))
    lam0 = vals[idx0]
    v0 = mp.matrix([[vecs[j, idx0]] for j in range(A.rows)])
    overlap = mp.fsum(mp.conj(v0[j]) * g[j] for j in range(A.rows))
    rz = mp.matrix([[1 / (z0 - 2 * mp.pi * m / L) for m in inner]])
    row = (rz * v0)[0]
    scalar = overlap * row
    pprime = mp.mpf("1")
    for j in range(A.rows):
        if j != idx0:
            pprime *= -vals[j]
    detM = mp.det(M)
    return {
        "mu": mu,
        "lambda0": lam0,
        "overlap": overlap,
        "row": row,
        "scalar": scalar,
        "pprime": pprime,
        "detM": detM,
        "ratio": detM / scalar if scalar else mp.mpc("nan"),
        "ratio_over_pprime": detM / (pprime * scalar) if scalar and pprime else mp.mpc("nan"),
    }


def cserial(z, digits: int = 24):
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def run_build(label, lam, max_modes, dps, sigma0, planted):
    mp.mp.dps = dps
    z0 = 1j * sigma0
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        data = kernel_anchor_scalar(H, idx, L, z0)
        rows.append(
            {
                "N": modes,
                "lambda0_abs": serial(abs(data["lambda0"])),
                "overlap_abs": serial(abs(data["overlap"])),
                "row_abs": serial(abs(data["row"])),
                "scalar_abs": serial(abs(data["scalar"])),
                "pprime_abs": serial(abs(data["pprime"])),
                "detM_abs": serial(abs(data["detM"])),
                "ratio": cserial(data["ratio"]),
                "ratio_over_pprime": cserial(data["ratio_over_pprime"]),
            }
        )
        print(
            f"{label:8s} N={modes:2d} "
            f"|lam0|={serial(abs(data['lambda0']),8):>12s} "
            f"|scalar|={serial(abs(data['scalar']),8):>12s} "
            f"|detM|={serial(abs(data['detM']),8):>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "sigma0": serial(sigma0),
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=14)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--sigma0", default="1.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_7ad_bordered_anchor_formula_results.json")
    args = parser.parse_args()
    sigma0 = mp.mpf(args.sigma0)
    result = {
        "statement": "Bordered determinant versus kernel-anchor scalar",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigma0": serial(sigma0),
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        result["cases"].append(run_build(label, args.lam, args.max_modes, args.dps, sigma0, planted))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
