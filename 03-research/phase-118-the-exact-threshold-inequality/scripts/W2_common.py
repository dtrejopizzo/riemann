"""W2 shared helpers: annulus/Tate splitting of the corona, and a
configurable-rtol reimplementation of schur_target's linear algebra so we can
sweep the pseudo-inverse cutoff (SPEC rule: cutoffs are load-bearing, never
report at one silent value).

Not a driver script.  Imported by W2_split.py, W2_blocks.py, W2_coercivity.py,
W2_tate_closedform.py.  Does NOT modify rowd_assembly.py / rowd_threshold.py.
"""
import math
import numpy as np
import rowd_assembly as RA
import rowd_threshold as RT


# --------------------------------------------------------------- linear algebra
def psd_pinv(M, rtol):
    w, V = np.linalg.eigh(0.5 * (M + M.T))
    keep = w > rtol * max(w.max(), 1e-300)
    wi = np.where(keep, 1.0 / np.where(keep, w, 1.0), 0.0)
    return V @ np.diag(wi) @ V.T, int(keep.sum()), w


def psd_isqrt(M, rtol):
    w, V = np.linalg.eigh(0.5 * (M + M.T))
    keep = w > rtol * max(w.max(), 1e-300)
    wi = np.where(keep, 1.0 / np.sqrt(np.where(keep, w, 1.0)), 0.0)
    return V @ np.diag(wi) @ V.T, int(keep.sum()), w


def orthonormalize(cols, Gram, rtol=1e-10):
    """Gram-orthonormal basis of span(cols); returns (basis, eigenvalues kept)."""
    Gr = cols.T @ Gram @ cols
    w, V = np.linalg.eigh(0.5 * (Gr + Gr.T))
    keep = w > rtol * max(w.max(), 1e-300)
    return cols @ V[:, keep] @ np.diag(1.0 / np.sqrt(w[keep])), w[keep]


# --------------------------------------------------------- annulus / Tate split
def annulus_tate_split(bk, rtol=1e-10):
    """Split corona basis bk['Za'] (Gram-orthonormal, dimA columns) into

        Za_ann  = primitives supported on cells whose midpoint lies in the
                  annulus tau_old < |t| < tau_new  (built directly, exactly
                  as Zc is built for the old core in rowd_threshold, but with
                  the complementary support mask)
        Za_tate = Gram-orthogonal complement of Za_ann inside span(Za)

    Returns dict with Za_ann, Za_tate, W (dimA x dimA orthogonal s.t.
    [Za_ann|Za_tate] = Za @ W), na = dim(Za_ann), nt = dim(Za_tate), and
    orthogonality/closure diagnostics.
    """
    M = bk['M']
    c, d, Gram = M['c'], M['d'], M['Gram']
    T_old = bk['T_old']
    mid = 0.5 * (c + d)
    inside = (mid > -T_old) & (mid < T_old)
    outside = ~inside                      # annulus cells (all within T_new by construction)

    Esup = np.zeros((len(c), int(outside.sum())))
    Esup[np.where(outside)[0], np.arange(outside.sum())] = 1.0
    ann_raw = Esup @ RT._nullspace(M['Tate'] @ Esup, rtol=rtol)
    Za_ann, ann_eigs = orthonormalize(ann_raw, Gram, rtol=rtol)

    Za = bk['Za']
    resid = Za - Za_ann @ (Za_ann.T @ Gram @ Za)
    Za_tate, tate_eigs = orthonormalize(resid, Gram, rtol=rtol)

    na, nt = Za_ann.shape[1], Za_tate.shape[1]
    Zcomb = np.hstack([Za_ann, Za_tate])
    Wm = Za.T @ Gram @ Zcomb           # dimA x (na+nt) coordinates of Zcomb in Za-basis
    orth_err = float(np.linalg.norm(Wm.T @ Wm - np.eye(na + nt))) if na + nt > 0 else 0.0
    cross_err = float(np.linalg.norm(Za_ann.T @ Gram @ Za_tate))
    closure_err = float(np.linalg.norm(Za @ Wm - Zcomb))  # Za@W reconstructs [Za_ann|Za_tate]
    return dict(Za_ann=Za_ann, Za_tate=Za_tate, W=Wm, na=na, nt=nt,
                dimA=bk['dimA'], orth_err=orth_err, cross_err=cross_err,
                closure_err=closure_err, ann_eigs=ann_eigs, tate_eigs=tate_eigs,
                n_outside_cells=int(outside.sum()), n_cells=len(c))


def phi_pm_raw_and_projected(bk):
    """e^{+-t/2}.1_{I_tau_old}, as the L2-best piecewise-constant vector on the
    mesh (cell value = cell average of e^{+-t/2}, zero outside the old core),
    and their Gram-orthogonal projections onto the corona span(Za)."""
    M = bk['M']
    c, d, Gram = M['c'], M['d'], M['Gram']
    T_old = bk['T_old']
    mid = 0.5 * (c + d)
    inside = (mid > -T_old) & (mid < T_old)
    w = d - c
    phi_p = np.zeros(len(c))
    phi_m = np.zeros(len(c))
    phi_p[inside] = 2.0 * (np.exp(d[inside] / 2) - np.exp(c[inside] / 2)) / w[inside]
    phi_m[inside] = 2.0 * (np.exp(-c[inside] / 2) - np.exp(-d[inside] / 2)) / w[inside]
    Za = bk['Za']
    proj_p = Za @ (Za.T @ Gram @ phi_p)
    proj_m = Za @ (Za.T @ Gram @ phi_m)
    return phi_p, phi_m, proj_p, proj_m


def principal_angles(U, V, Gram):
    """U, V: Gram-orthonormal bases (n x k1),(n x k2).  Returns angles in degrees."""
    Guv = U.T @ Gram @ V
    s = np.linalg.svd(Guv, compute_uv=False)
    s = np.clip(s, -1.0, 1.0)
    return np.degrees(np.arccos(s))


# ------------------------------------------------------- rtol-parametrized target
def schur_target_rtol(bk, rtol):
    """Same algebra as rowd_threshold.schur_target, with an explicit,
    independently chosen pseudo-inverse cutoff `rtol` (rather than the
    hard-coded 1e-11 default), so the cutoff dependence can be swept."""
    R0, L0, r_, l_ = bk['R0'], bk['L0'], bk['r'], bk['l']
    RE, LE, A0 = bk['RE'], bk['LE'], bk['A0']
    R0p, rk_R0, _ = psd_pinv(R0, rtol)
    H = R0p @ r_
    S_E = RE - r_.T @ R0p @ r_
    ZtZ = LE - l_.T @ H - H.T @ l_ + H.T @ L0 @ H
    b_E = L0 @ H - l_
    A0p, rk_A0, _ = psd_pinv(A0, rtol)
    pen = b_E.T @ A0p @ b_E
    S = S_E - ZtZ - pen
    S = 0.5 * (S + S.T)
    isq, rk_SE, w_SE = psd_isqrt(S_E, rtol)
    Mn = isq @ S @ isq
    Mn = 0.5 * (Mn + Mn.T)
    lam_full = np.linalg.eigvalsh(Mn)
    lam_active = lam_full[-rk_SE:] if rk_SE < lam_full.size else lam_full
    return dict(S=S, S_E=S_E, b_E=b_E, A0=A0, pen=pen, M=Mn,
                rk_R0=rk_R0, rk_A0=rk_A0, rk_SE=rk_SE,
                lam_min_norm=float(lam_active.min()) if lam_active.size else float('nan'))


def block_decompose(mat, Wm, na):
    """Congruence-transform `mat` (dimA x dimA, in Za-coordinates) by the
    orthogonal basis-change Wm into the [ann|tate] coordinates, and split
    into 2x2 blocks with the ann block first (size na) and tate second."""
    matn = Wm.T @ mat @ Wm
    matn = 0.5 * (matn + matn.T)
    aa = matn[:na, :na]
    at = matn[:na, na:]
    tt = matn[na:, na:]
    return aa, at, tt, matn


def schur_complement_min(tt, at, aa, rtol):
    aap, _, _ = psd_pinv(aa, rtol)
    C = tt - at.T @ aap @ at
    C = 0.5 * (C + C.T)
    return np.linalg.eigvalsh(C)


PRIME_POWER_STEPS = [
    (2, 3), (3, 4), (4, 5), (5, 7), (7, 8), (8, 9), (9, 11), (11, 13),
    (13, 16), (16, 17), (17, 19), (19, 23), (23, 25), (25, 27), (27, 29),
    (29, 31), (31, 32), (32, 37), (37, 41), (41, 43), (43, 47), (47, 49),
    (49, 53), (53, 59), (59, 61),
]


def delta_j(q_old, q_new):
    """Annulus width tau_new - tau_old = (1/2) log(q_new/q_old)."""
    return 0.5 * math.log(q_new / q_old)
