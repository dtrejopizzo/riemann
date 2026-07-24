#!/usr/bin/env python3
"""E78.154 - profile, sign and support of the spectral-shift difference M_N.

M_N(x) = (nu_N - nu_{N+2})((-inf, x]), piecewise constant, -> 0 at +-inf.
BOUND_N = int |M_N| w,  w(x)=sup_{sigma in K} 4 sigma|x|/(x^2+sigma^2)^2.

Diagnostics per step N->N+2, both builds:
  - sign structure: is M_N(x) odd (M_N*x single-signed)? report
      pos_mass = int_{M_N>0} |M_N| w,  neg_mass = int_{M_N<0} |M_N| w,
      and P = int over M_N*x>0 vs M_N*x<0 (the quantity that makes BOUND=TRUE).
  - support split: contribution to BOUND from interior |x|<=X_old vs edge
      |x|>X_old, X_old = 2 pi (N-2)/L (the previous outer mesh radius).
  - peak location of |M_N|.
This decides the summability route (single-sign + edge/bulk) and whether the
sign structure discriminates the builds.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402
from E78_153_spectral_shift_counting_sum_probe import nu_atoms, w_sup  # noqa: E402


def analyze(atoms_N, atoms_M, L, N):
    combined = [(p, w) for (p, w) in atoms_N] + [(p, -w) for (p, w) in atoms_M]
    combined.sort(key=lambda t: t[0])
    Xold = 2 * mp.pi * (N - 2) / L
    running = mp.mpf(0)
    pos = mp.mpf(0)   # contribution where M_N > 0
    neg = mp.mpf(0)   # where M_N < 0
    Pxpos = mp.mpf(0)  # where M_N * x > 0
    Pxneg = mp.mpf(0)
    interior = mp.mpf(0)
    edge = mp.mpf(0)
    peakval = mp.mpf(0)
    peakx = mp.mpf(0)
    for i in range(len(combined) - 1):
        running += combined[i][1]
        if abs(running) < mp.mpf("1e-30"):
            continue
        x0, x1 = combined[i][0], combined[i + 1][0]
        mids = 8
        seg = (x1 - x0) / mids
        acc = mp.mpf(0)
        for m in range(mids):
            a = x0 + m * seg
            b = a + seg
            acc += (seg / 6) * (w_sup(a) + 4 * w_sup((a + b) / 2) + w_sup(b))
        contrib = abs(running) * acc
        xm = (x0 + x1) / 2
        if running > 0:
            pos += contrib
        else:
            neg += contrib
        if running * xm > 0:
            Pxpos += contrib
        else:
            Pxneg += contrib
        if abs(xm) <= Xold:
            interior += contrib
        else:
            edge += contrib
        if abs(running) > peakval:
            peakval = abs(running)
            peakx = xm
    total = pos + neg
    return {
        "total": total, "pos": pos, "neg": neg,
        "Pxpos": Pxpos, "Pxneg": Pxneg,
        "interior": interior, "edge": edge,
        "peakval": peakval, "peakx": peakx, "Xold": Xold,
    }


def run(label, planted, lam_int, dps, max_modes):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    for N in range(8, max_modes - 1, 2):
        Hn, idxn = section(Hmax, idxmax, max_modes, N)
        Hm, idxm = section(Hmax, idxmax, max_modes, N + 2)
        aN, _ = nu_atoms(Hn, idxn, L)
        aM, _ = nu_atoms(Hm, idxm, L)
        r = analyze(aN, aM, L, N)
        f_edge = r["edge"] / r["total"] if r["total"] else mp.mpf(0)
        f_Mxpos = r["Pxpos"] / r["total"] if r["total"] else mp.mpf(0)
        print(f"{label:6s} {N:2d}->{N+2:2d}  total={mp.nstr(r['total'],5):>10s}  "
              f"M>0/M<0={mp.nstr(r['pos'],4)}/{mp.nstr(r['neg'],4)}  "
              f"Mx>0 frac={mp.nstr(f_Mxpos,4)}  edge frac={mp.nstr(f_edge,4)}  "
              f"peak|M|={mp.nstr(r['peakval'],4)} @x={mp.nstr(r['peakx'],4)} (Xold={mp.nstr(r['Xold'],4)})",
              flush=True)


def main():
    dps = 50
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        run(label, planted, 6, dps, 18)


if __name__ == "__main__":
    main()
