#!/usr/bin/env python3
"""Audit anchor-blindness of the simple zero mode on zeta sections."""

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
from E77_3c_two_generator_ident_probe import right_transfer_data  # noqa: E402


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def section(Hmax, idxmax, max_modes, modes):
    off = max_modes - modes
    return (
        Hmax[off : Hmax.rows - off, off : Hmax.cols - off],
        idxmax[off : len(idxmax) - off],
    )


def run_case(lam: int, max_modes: int, dps: int, sigma0: mp.mpf):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam, max_modes, dps)
    z0 = 1j * sigma0
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        mu, A, db_idx, inner, _x = right_transfer_data(H, idx)
        vals, vecs = mp.eighe(A)
        j0 = min(range(len(vals)), key=lambda j: abs(vals[j]))
        v0 = vecs[:, j0]
        rz = mp.fsum(v0[j] / (z0 - 2 * mp.pi * inner[j] / L) for j in range(len(inner)))
        rows.append(
            {
                "N": modes,
                "lambda0_abs": serial(abs(vals[j0])),
                "anchor_abs": serial(abs(rz)),
                "anchor": {"re": serial(mp.re(rz)), "im": serial(mp.im(rz))},
            }
        )
        print(
            f"N={modes:2d} |lam0|={serial(abs(vals[j0]),8):>12s} "
            f"|r0v|={serial(abs(rz),8):>12s}",
            flush=True,
        )
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=14)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--sigma0", default="1.0")
    parser.add_argument(
        "--output", type=Path, default=HERE / "E77_7ag_anchor_blindness_results.json"
    )
    args = parser.parse_args()
    sigma0 = mp.mpf(args.sigma0)
    result = {
        "statement": "Anchor-blindness audit for simple inner zero mode",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigma0": serial(sigma0),
        },
        "rows": run_case(args.lam, args.max_modes, args.dps, sigma0),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
