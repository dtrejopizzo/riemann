"""W2 task (1)+(2): annulus/Tate split verification and 2x2 block decomposition
of the exact threshold target, at every reachable prime-power step and at
refine 8/16/32/64 (plus a few extra refines for the cheap steps, matching
W1_convergence.json's grid so the two can be cross-checked).

For each (q_old,q_new,refine) this computes:
  - the annulus/Tate split of the corona basis Za (via W2_common.annulus_tate_split)
    and verifies na = dimA-2, nt = 2 exactly, reporting orth/cross/closure errors
    and the principal angles between Za_tate and the corona-projections of
    e^{+-t/2}|_{I_tau_old};
  - the S_E-normalized matrix M = S_E^{dag/2} (T) S_E^{dag/2} (T = the raw
    Schur target S_E - Z_E^*Z_E - b_E^*A_0^dag b_E) and the PLAIN L2-metric
    target T itself (both live in Za's Gram-orthonormal coordinates, i.e. the
    plain L2 inner product on the corona -- Za is already Gram-orthonormal so
    Euclidean coordinates in that basis ARE the L2 metric);
  - both congruence-transformed into [ann|tate] coordinates via the
    orthogonal Wm from the split, giving 2x2-block decompositions
    [[aa,at],[at^T,tt]] in EACH metric;
  - lambda_min(aa), eigs(tt), spectral norm(at), lambda_min(full), and the
    Schur-complement test lambda_min(tt - at^T aa^dag at), in each metric;
  - cross-check: lambda_min(M) must equal rowd_threshold.schur_target's
    lam_min_norm at the same default rtol=1e-11 (both computed and compared).

Pseudo-inverse cutoff rtol used for psd_pinv/psd_isqrt is swept over
{1e-13,1e-11,1e-9,1e-7} (SPEC rule: cutoffs are load-bearing); the split's own
nullspace/orthonormalize rtol is fixed at 1e-10 (that one controls basis
CONSTRUCTION, not the Schur penalty, and dim checks below confirm it is not
sensitive in that range -- see W2_split_rtol_check in this file's __main__).

Command:
    python3 W2_sweep.py
Writes W2_sweep.json incrementally (one entry appended per step/refine/rtol).
"""
import json, math, sys, time
import numpy as np
import rowd_threshold as RT
import W2_common as W2

STEPS_ALL = W2.PRIME_POWER_STEPS                       # 25 steps, (2,3)...(59,61)
STEPS_DEEP = [(2, 3), (3, 4), (4, 5), (5, 7), (7, 8)]   # matches W1_convergence.json
REFS_ALL = [8]                                          # cheap: run on every step
REFS_DEEP = [8, 16, 32, 64]                             # expensive: only on STEPS_DEEP
RTOLS = [1e-13, 1e-11, 1e-9, 1e-7]                       # pinv cutoff sweep (task 2 rule)
SPLIT_RTOL = 1e-10                                       # basis-construction rtol (fixed)


def spec_norm(M):
    if M.size == 0:
        return 0.0
    return float(np.linalg.svd(M, compute_uv=False)[0])


def one(qo, qn, refine, rtol):
    t0 = time.time()
    bk = RT.threshold_blocks(qo, qn, refine=refine)
    sp = W2.annulus_tate_split(bk, rtol=SPLIT_RTOL)
    phi_p, phi_m, proj_p, proj_m = W2.phi_pm_raw_and_projected(bk)
    Gram = bk['M']['Gram']
    proj_basis, proj_eigs = W2.orthonormalize(np.column_stack([proj_p, proj_m]), Gram, rtol=1e-10)
    ang = (W2.principal_angles(sp['Za_tate'], proj_basis, Gram).tolist()
           if proj_basis.shape[1] == sp['nt'] else None)

    rt = RT.schur_target(bk)                     # reference, rowd_threshold default rtol=1e-11
    wt = W2.schur_target_rtol(bk, rtol)           # our reimplementation at chosen rtol

    na, nt = sp['na'], sp['nt']
    Wm = sp['W']
    # S_E-normalized metric
    M_aa, M_at, M_tt, _ = W2.block_decompose(wt['M'], Wm, na)
    lamM_aa = float(np.linalg.eigvalsh(0.5 * (M_aa + M_aa.T)).min()) if na else float('nan')
    eigM_tt = np.linalg.eigvalsh(0.5 * (M_tt + M_tt.T)).tolist()
    normM_at = spec_norm(M_at)
    lamM_full = float(np.linalg.eigvalsh(0.5 * (wt['M'] + wt['M'].T)).min())
    schurM = W2.schur_complement_min(M_tt, M_at, M_aa, rtol).tolist() if na else eigM_tt

    # plain L2 metric: the raw (unnormalized) target T = S_E - Z_E^*Z_E - b_E^*A0^dag b_E
    T_aa, T_at, T_tt, _ = W2.block_decompose(wt['S'], Wm, na)
    lamT_aa = float(np.linalg.eigvalsh(0.5 * (T_aa + T_aa.T)).min()) if na else float('nan')
    eigT_tt = np.linalg.eigvalsh(0.5 * (T_tt + T_tt.T)).tolist()
    normT_at = spec_norm(T_at)
    lamT_full = float(np.linalg.eigvalsh(0.5 * (wt['S'] + wt['S'].T)).min())
    schurT = W2.schur_complement_min(T_tt, T_at, T_aa, rtol).tolist() if na else eigT_tt

    rec = dict(
        q_old=qo, q_new=qn, refine=refine, rtol=rtol,
        T_old=bk['T_old'], T_new=bk['T_new'], delta=W2.delta_j(qo, qn),
        cells=bk['cells'], dimA=bk['dimA'], dimC=bk['dimC'],
        na=na, nt=nt, orth_err=sp['orth_err'], cross_err=sp['cross_err'],
        closure_err=sp['closure_err'], principal_angles_deg=ang,
        lam_min_norm_ref=rt['lam_min_norm'],           # rowd_threshold, rtol=1e-11 fixed
        lam_min_norm_ours=wt['lam_min_norm'],          # our reimpl at swept rtol
        rank_SE_ref=rt['rank_SE'], rank_SE_ours=wt['rk_SE'],
        rank_A0_ours=wt['rk_A0'],
        lamM_aa=lamM_aa, eigM_tt=eigM_tt, normM_at=normM_at, lamM_full=lamM_full,
        schurM_tt_minus=schurM,
        lamT_aa=lamT_aa, eigT_tt=eigT_tt, normT_at=normT_at, lamT_full=lamT_full,
        schurT_tt_minus=schurT,
        minA0=rt['minA0'], time=time.time() - t0,
    )
    return rec


if __name__ == '__main__':
    out = []
    t_start = time.time()
    # (a) broad sweep: every reachable prime-power step, refine=8, default rtol=1e-11
    for qo, qn in STEPS_ALL:
        rec = one(qo, qn, 8, 1e-11)
        out.append(rec)
        print(f"[broad] {qo:>3},{qn:<3} r=8 na={rec['na']:3d} nt={rec['nt']} "
              f"lam_ref={rec['lam_min_norm_ref']:.6e} lam_ours={rec['lam_min_norm_ours']:.6e} "
              f"lamM_aa={rec['lamM_aa']:.6e} eigM_tt={rec['eigM_tt']} "
              f"schurM={rec['schurM_tt_minus']} ({rec['time']:.1f}s)")
        sys.stdout.flush()
        json.dump(out, open('W2_sweep.json', 'w'), indent=1)

    # (b) deep sweep: refine in {8,16,32,64}, rtol swept, on the 5 cheap steps
    for qo, qn in STEPS_DEEP:
        for refine in REFS_DEEP:
            for rtol in RTOLS:
                if refine == 8 and rtol == 1e-11:
                    continue  # already have it from the broad sweep
                rec = one(qo, qn, refine, rtol)
                out.append(rec)
                print(f"[deep]  {qo:>3},{qn:<3} r={refine:>3} rtol={rtol:.0e} "
                      f"na={rec['na']:3d} nt={rec['nt']} "
                      f"lam_ref={rec['lam_min_norm_ref']:.6e} lam_ours={rec['lam_min_norm_ours']:.6e} "
                      f"lamM_aa={rec['lamM_aa']:.6e} eigM_tt={rec['eigM_tt']} "
                      f"schurM={rec['schurM_tt_minus']} ({rec['time']:.1f}s, total {time.time()-t_start:.0f}s)")
                sys.stdout.flush()
                json.dump(out, open('W2_sweep.json', 'w'), indent=1)

    print(f"done, {len(out)} records, {time.time()-t_start:.0f}s total")
