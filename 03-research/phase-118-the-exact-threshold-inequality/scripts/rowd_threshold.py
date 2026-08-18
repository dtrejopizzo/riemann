"""Threshold step: old core / newborn corona split, and the exact Schur target.

Implements, in the piecewise-constant Galerkin space of rowd_assembly:
  * Theorem thm:exactstep  (the step is exact; corona = annulus + 2 Tate modes)
  * eq:newdPhysicalBlocks / thm:newdThresholdCriterion
        R_0, L_0, r, l, A_0, H, S_E, Z_E, b_E
        target  S = S_E - Z_E^* Z_E - b_E^* A_0^dagger b_E
  * the normalized transfer contractivity  ||Theta||^2 = 1 - lambda_min(S_E^{-1/2} S S_E^{-1/2})
"""
import math
import numpy as np
import scipy.linalg as sla

import rowd_assembly as RA


def _nullspace(Mat, rtol=1e-11):
    u, s, vt = np.linalg.svd(Mat)
    if s.size == 0:
        return np.eye(Mat.shape[1])
    k = int(np.sum(s > rtol * s.max()))
    return vt[k:].T


def _psd_pinv(M, rtol=1e-11):
    w, V = np.linalg.eigh(0.5 * (M + M.T))
    keep = w > rtol * max(w.max(), 1e-300)
    wi = np.where(keep, 1.0 / np.where(keep, w, 1.0), 0.0)
    return V @ np.diag(wi) @ V.T


def _psd_isqrt(M, rtol=1e-11):
    w, V = np.linalg.eigh(0.5 * (M + M.T))
    keep = w > rtol * max(w.max(), 1e-300)
    wi = np.where(keep, 1.0 / np.sqrt(np.where(keep, w, 1.0)), 0.0)
    return V @ np.diag(wi) @ V.T, keep.sum()


def threshold_blocks(q_old, q_new, refine=8):
    """Assemble the step P_{tau_old} -> P_{tau_new} and return all blocks."""
    T_old = 0.5 * math.log(q_old)
    T_new = 0.5 * math.log(q_new)
    M = RA.assemble(T_new, refine=refine, extra_points=(T_old, -T_old))
    c, d, Gram = M['c'], M['d'], M['Gram']

    # primitive space at the new window
    Znew = _nullspace(M['Tate'])

    # old core C: primitive functions supported inside [-T_old, T_old]
    mid = 0.5 * (c + d)
    inside = (mid > -T_old) & (mid < T_old)
    Esup = np.zeros((len(c), int(inside.sum())))
    Esup[np.where(inside)[0], np.arange(inside.sum())] = 1.0
    # impose the (identical) Tate constraints on the old support
    Zc = Esup @ _nullspace(M['Tate'] @ Esup)

    # corona A = L^2-orthogonal complement of C inside P_new
    # project Znew onto the Gram-orthogonal complement of Zc
    Gc = Zc.T @ Gram @ Zc
    P_on_C = Zc @ np.linalg.solve(Gc, Zc.T @ Gram)
    resid = Znew - P_on_C @ Znew
    # orthonormalize the residual in the Gram metric
    Gr = resid.T @ Gram @ resid
    w, V = np.linalg.eigh(0.5 * (Gr + Gr.T))
    keep = w > 1e-10 * w.max()
    Za = resid @ V[:, keep] @ np.diag(1.0 / np.sqrt(w[keep]))

    def blk(F, U, V_):
        return U.T @ F @ V_

    R, L, A = M['R'], M['L'], M['A']
    out = dict(T_old=T_old, T_new=T_new, q_old=q_old, q_new=q_new,
               cells=len(c), dimP=Znew.shape[1], dimC=Zc.shape[1],
               dimA=Za.shape[1], M=M, Zc=Zc, Za=Za)

    out['R0'] = blk(R, Zc, Zc); out['L0'] = blk(L, Zc, Zc)
    out['r'] = blk(R, Zc, Za);  out['l'] = blk(L, Zc, Za)
    out['RE'] = blk(R, Za, Za); out['LE'] = blk(L, Za, Za)
    out['A0'] = out['R0'] - out['L0']
    out['Anew'] = out['RE'] - out['LE']
    out['B'] = blk(A, Zc, Za)
    out['Aold_direct'] = blk(A, Zc, Zc)
    return out


def schur_target(bk):
    """S_E - Z_E^* Z_E - b_E^* A_0^dagger b_E, plus diagnostics."""
    R0, L0, r, l = bk['R0'], bk['L0'], bk['r'], bk['l']
    RE, LE, A0 = bk['RE'], bk['LE'], bk['A0']
    R0p = _psd_pinv(R0)
    H = R0p @ r
    S_E = RE - r.T @ R0p @ r                      # eq:newdReferenceSchur
    ZtZ = LE - l.T @ H - H.T @ l + H.T @ L0 @ H   # Z_E^* Z_E
    b_E = L0 @ H - l                              # eq:newdOppositeResidual
    A0p = _psd_pinv(A0)
    pen = b_E.T @ A0p @ b_E                       # Schur penalty
    S = S_E - ZtZ - pen
    S = 0.5 * (S + S.T)

    # range/consistency diagnostics
    res_r = np.linalg.norm(r - R0 @ R0p @ r) / max(np.linalg.norm(r), 1e-300)
    res_b = np.linalg.norm(b_E - A0 @ A0p @ b_E) / max(np.linalg.norm(b_E), 1e-300)

    isq, rk = _psd_isqrt(S_E)
    Snorm = isq @ S @ isq
    lam = np.linalg.eigvalsh(0.5 * (Snorm + Snorm.T))
    lam = lam[-rk:] if rk < lam.size else lam
    return dict(S=S, S_E=S_E, ZtZ=ZtZ, b_E=b_E, pen=pen,
                lam_min_norm=float(lam.min()), rank_SE=int(rk),
                res_r=float(res_r), res_b=float(res_b),
                minA0=float(np.linalg.eigvalsh(0.5*(A0+A0.T)).min()),
                minSE=float(np.linalg.eigvalsh(0.5*(S_E+S_E.T)).min()))
