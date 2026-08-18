"""W1 task 2: sensitivity of lam_min_norm to the A_0 pseudo-inverse cutoff.

`schur_target` in rowd_threshold.py hardcodes rtol=1e-11 in `_psd_pinv(A0)`.
This script recomputes the whole pipeline (locally, not touching
rowd_threshold.py) with rtol swept over 1e-14..1e-6, at several refine
values, and records lam_min_norm together with the number of A_0
eigenvalues retained by the cutoff (and A_0's actual eigenvalue list,
so we can see exactly which ones are being kept/dropped).

Command:
    python3 W1_pinv_sweep_run.py

Writes W1_pinv_sweep.json.
"""
import json, time, sys
import numpy as np
import rowd_threshold as RT

STEPS = [(2, 3), (5, 7), (7, 8)]
REFS = [8, 16, 32, 64]
RTOLS = [1e-14, 1e-13, 1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6]


def schur_target_rtol(bk, rtol):
    """Reimplementation of RT.schur_target with an explicit, variable rtol
    on the A_0 pseudo-inverse only (S_E, Z_E use the fixed default 1e-11,
    since the question under test is specifically the A_0 cutoff -- A_0 is
    the block with the near-null directions per SPEC.md section 2)."""
    R0, L0, r, l = bk['R0'], bk['L0'], bk['r'], bk['l']
    RE, LE, A0 = bk['RE'], bk['LE'], bk['A0']
    R0p = RT._psd_pinv(R0)
    H = R0p @ r
    S_E = RE - r.T @ R0p @ r
    ZtZ = LE - l.T @ H - H.T @ l + H.T @ L0 @ H
    b_E = L0 @ H - l
    A0s = 0.5 * (A0 + A0.T)
    wA, VA = np.linalg.eigh(A0s)
    keepA = wA > rtol * max(wA.max(), 1e-300)
    wiA = np.where(keepA, 1.0 / np.where(keepA, wA, 1.0), 0.0)
    A0p = VA @ np.diag(wiA) @ VA.T
    pen = b_E.T @ A0p @ b_E
    S = S_E - ZtZ - pen
    S = 0.5 * (S + S.T)
    isq, rk = RT._psd_isqrt(S_E)
    Snorm = isq @ S @ isq
    lam = np.linalg.eigvalsh(0.5 * (Snorm + Snorm.T))
    lam = lam[-rk:] if rk < lam.size else lam
    return dict(lam_min_norm=float(lam.min()), n_A0_kept=int(keepA.sum()),
                n_A0_total=int(wA.size), A0_eigs=wA.tolist())


if __name__ == '__main__':
    out = {}
    for qo, qn in STEPS:
        key = f"{qo},{qn}"
        out[key] = []
        for r in REFS:
            bk = RT.threshold_blocks(qo, qn, refine=r)
            row = dict(refine=r, dimA=bk['dimA'], dimC=bk['dimC'])
            A0 = bk['A0']
            wA0 = np.linalg.eigvalsh(0.5 * (A0 + A0.T))
            row['A0_eig_min'] = float(wA0.min())
            row['A0_eig_max'] = float(wA0.max())
            row['A0_all_eigs'] = wA0.tolist()
            row['sweep'] = []
            for rtol in RTOLS:
                res = schur_target_rtol(bk, rtol)
                row['sweep'].append(dict(rtol=rtol,
                                          lam_min_norm=res['lam_min_norm'],
                                          n_A0_kept=res['n_A0_kept'],
                                          n_A0_total=res['n_A0_total']))
                print(f"{qo},{qn} refine={r:>3} rtol={rtol:.0e} "
                      f"kept={res['n_A0_kept']:>3}/{res['n_A0_total']:<3} "
                      f"lam={res['lam_min_norm']:.8e}")
                sys.stdout.flush()
            out[key].append(row)
    with open('W1_pinv_sweep.json', 'w') as f:
        json.dump(out, f, indent=1)
    print("wrote W1_pinv_sweep.json")
