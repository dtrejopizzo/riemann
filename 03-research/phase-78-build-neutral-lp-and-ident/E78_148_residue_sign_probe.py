#!/usr/bin/env python3
"""E78.148 - residue sign-definiteness test for the Herglotz/interlacing route.

F_{L,N}(z) = 1 + sum_n r_n/(z - d_n),  d_n = 2 pi n / L,  r_n = a_N u_n + b_N v_n.

If the residues r_n are sign-definite (all same sign), F_{L,N} is (up to sign)
a Herglotz/Nevanlinna function: its zeros then strictly interlace the symmetric
mesh {d_n}, one zero per gap. On a symmetric mesh the interlaced zeros pair up
(+/-), so the zero-sum in (log F)' organizes into +/- pairs 2z/(z^2 - .) = O(1/N^2),
matching the pole-pair term. This is the rigorous route for the zeta zero-side
of E78.147.

This probe extracts r_n for both builds and reports:
  - the sign pattern (fraction positive / negative)
  - whether sign-definite (Herglotz) or sign-mixed (interlacing broken)
Prediction: zeta sign-definite (true zero on the line preserves symmetry),
plant sign-mixed (off-line planted zero breaks it).
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data, two_generator_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402


def residues(H, idx, L, lam, planted):
    _mu, A, db_idx, inner, _x = right_transfer_data(H, idx)
    d, u, v, db, aa, bb, ub, vb = two_generator_data(A, inner, db_idx, L, lam, planted)
    r = [aa * u[j] + bb * v[j] for j in range(len(d))]
    return d, r


def run_case(label, planted, lam_int, dps, Ns, max_modes):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    for N in Ns:
        Hn, idxn = section(Hmax, idxmax, max_modes, N)
        d, r = residues(Hn, idxn, L, lam, planted)
        reals = [mp.re(x) for x in r]
        npos = sum(1 for x in reals if x > 0)
        nneg = sum(1 for x in reals if x < 0)
        total = len(reals)
        # sign-definite if all same sign (allow tiny zeros)
        definite = (npos == 0 or nneg == 0)
        # also report max |Im r| to confirm residues are real
        maximag = max(abs(mp.im(x)) for x in r)
        print(f"{label:6s} N={N:2d}  total={total:3d}  pos={npos:3d} neg={nneg:3d}  "
              f"{'SIGN-DEFINITE' if definite else 'sign-mixed':13s}  max|Im r|={mp.nstr(maximag,3)}",
              flush=True)


def main():
    dps = 50
    lam_int = 6
    max_modes = 16
    Ns = [8, 10, 12, 14, 16]
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        run_case(label, planted, lam_int, dps, Ns, max_modes)


if __name__ == "__main__":
    main()
