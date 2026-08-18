"""W3 task (2): ||Phi|| = ||Y_T X_T^dagger|| restricted to Ran(X_T), on P_T,
as a function of the pseudo-inverse spectral cutoff rtol.

Two independent computations, cross-checked against each other:

  (a) "cheap/exact" route: since Phi X = Y on Ran(X),
          ||Phi||^2 = sup_{v} (v^T L_P v) / (v^T R_P v)
                    = lambda_max( R_P^{dag/2} L_P R_P^{dag/2} )
      -- an exact Rayleigh-quotient identity, no need to ever build X, Y
      explicitly.  R_P, L_P are the restrictions of R_T, L_T to P_T (already
      validated against X^*X, Y^*Y in W3_task1_verify.py).

  (b) "explicit/SVD" route, matching the SPEC's literal prescription: build
      X_T, Y_T channel-by-channel (W3_build_xy.build_channels + restrict to
      P_T), stack into dense matrices, take the SVD of X, form the
      Moore-Penrose pseudoinverse at the SAME rtol cutoff, form
      Phi = Y X^dagger explicitly, and read off its top singular value.

(a) and (b) must agree to numerical precision; if they don't, something in
the explicit channel construction is wrong.  (b) is only run up to a size
cutoff (see MAX_EXPLICIT_ROWS below) since it requires materializing the full
codomain; (a) is run everywhere.

Galerkin bias: R_P, L_P (hence both routes) are Galerkin-projected (Rayleigh-
Ritz) restrictions of the true infinite-dimensional operators to a finite
piecewise-constant subspace of P_T.  For a Rayleigh quotient sup_v v^TL v /
v^TR v, restricting v to a subspace can only DECREASE the achievable sup (the
true sup over the full space is >= the sup over any subspace).  So the
Galerkin computation gives a LOWER bound on the true ||Phi||^2: measured
||Phi|| > 1 refutes; measured ||Phi|| <= 1 is consistent but not conclusive.
(This matches the SPEC Rules "state upper/lower bound direction"; note it is
the OPPOSITE direction from the lam_min_norm quantity of the threshold-step
formulation, which is a Schur complement quantity with a different monotonicity
-- lam_min_norm there is normalized so that mesh refinement DECREASES it,
i.e. gives an upper bound on that minimum. Here we are bounding a maximum
(||Phi||^2), so refinement can only increase the measured value towards the
truth from below.)

Run:  python3 W3_task2_phi_norm.py
"""
import math
import numpy as np
import W3_build_xy as W3

PRIME_POWER_THRESHOLDS = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
RTOLS = [1e-6, 1e-8, 1e-10, 1e-12]
MAX_EXPLICIT_ROWS = 20000   # cap for route (b), which materializes the codomain


def psd_pinv_isqrt(M, rtol):
    """Return (M^dagger)^{1/2} at spectral cutoff rtol*max(eig)."""
    w, V = np.linalg.eigh(0.5 * (M + M.T))
    thresh = rtol * max(w.max(), 1e-300)
    keep = w > thresh
    wi = np.where(keep, 1.0 / np.sqrt(np.where(keep, w, 1.0)), 0.0)
    return (V * wi) @ V.T, int(keep.sum())


def phi_norm_cheap(R_P, L_P, rtol):
    Rp_isqrt, rk = psd_pinv_isqrt(R_P, rtol)
    Mmat = Rp_isqrt @ L_P @ Rp_isqrt
    lam = np.linalg.eigvalsh(0.5 * (Mmat + Mmat.T))
    return float(max(lam.max(), 0.0)), rk


def phi_norm_explicit(rc, rtol):
    Xblocks = [rc['Xg_P']] + [rc['ant_P'][n] for n in rc['ns']]
    Yblocks = [rc['Y0_P']] + [rc['sym_P'][n] for n in rc['ns']]
    total_rows = sum(B.shape[0] for B in Xblocks) + sum(B.shape[0] for B in Yblocks)
    if total_rows > MAX_EXPLICIT_ROWS:
        return None
    Xmat = np.vstack(Xblocks)
    Ymat = np.vstack(Yblocks)
    U, S, Vt = np.linalg.svd(Xmat, full_matrices=False)
    keep = S > rtol * S.max()
    k = int(keep.sum())
    Xdag = (Vt[:k].T * (1.0 / S[:k])) @ U[:, :k].T   # dimP x rows_X
    Phi = Ymat @ Xdag                                 # rows_Y x rows_X
    sv = np.linalg.svd(Phi, compute_uv=False)
    return float(sv[0]) ** 2, k


def run(refines=(4, 8, 16, 32), thresholds=PRIME_POWER_THRESHOLDS, rtols=RTOLS):
    rows = []
    header = (f"{'q':>4} {'refine':>6} {'dimP':>5} {'rtol':>8} "
              f"{'rank(R_P)':>9} {'||Phi||^2 cheap':>16} {'||Phi|| cheap':>13} "
              f"{'||Phi||^2 explicit':>19} {'agree?':>8}")
    print(header)
    for refine in refines:
        for q in thresholds:
            T = 0.5 * math.log(q)
            ch = W3.build_channels(T, refine=refine)
            Z = W3.primitive_basis(ch['Tate'], ch['Gram'])
            rc = W3.restrict_channels(ch, Z)
            R_P, L_P = rc['R_P'], rc['L_P']
            for rtol in rtols:
                val_cheap, rk = phi_norm_cheap(R_P, L_P, rtol)
                val_expl_out = phi_norm_explicit(rc, rtol)
                if val_expl_out is not None:
                    val_expl, k_expl = val_expl_out
                    agree = abs(val_cheap - val_expl) < 1e-6 * max(val_cheap, 1e-12)
                    expl_str = f"{val_expl:19.10f}"
                    agree_str = 'YES' if agree else 'NO'
                else:
                    val_expl, k_expl = None, None
                    expl_str = f"{'skip(size)':>19}"
                    agree_str = '-'
                print(f"{q:>4} {refine:>6} {rc['dimP']:>5} {rtol:>8.0e} {rk:>9} "
                      f"{val_cheap:16.10f} {math.sqrt(max(val_cheap,0)):13.10f} "
                      f"{expl_str} {agree_str:>8}")
                rows.append(dict(q=q, refine=refine, dimP=rc['dimP'], rtol=rtol,
                                  rank_RP=rk, phi2_cheap=val_cheap,
                                  phi2_explicit=val_expl, k_explicit=k_expl))
    return rows


if __name__ == '__main__':
    run()
