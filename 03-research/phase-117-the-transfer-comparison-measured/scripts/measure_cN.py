"""Measure, at each arithmetic threshold N -> N+1:

  src   : lambda_min of the source defect D_N = E_{GammaT,N} - L_N^*L_N,
          normalized by ||L_N||^2   (>=0  <=>  the unit source estimate holds)
  rho_N : the Schur angle  b_N^* C_N^dag b_N / d_N   of prop:newdMeanZeroSchur
  lam   : lambda_min of the normalized PHYSICAL Schur target
          S_E^{-1/2}(S_E - Z_E^*Z_E - b_E^*A_0^dag b_E)S_E^{-1/2}
  c_N   : best constant in   S >= c_N * Xi^* D_N Xi   (Problem: transfer comparison)

Xi is the identification of the newborn corona with the one-wing model cell.
Three natural choices are reported, since the choice IS the open problem.
"""
import math
import numpy as np

import rowd_assembly as RA
import rowd_threshold as RT
import rowd_source as RS


def _pinv_isqrt(M, rtol=1e-10):
    w, V = np.linalg.eigh(0.5 * (M + M.T))
    keep = w > rtol * max(w.max(), 1e-300)
    wi = np.where(keep, 1.0 / np.sqrt(np.where(keep, w, 1.0)), 0.0)
    return V @ np.diag(wi) @ V.T, keep


def measure(N, refine=6):
    bk = RT.threshold_blocks(N, N + 1, refine=refine)
    st = RT.schur_target(bk)
    M = bk['M']
    c, d = M['c'], M['d']
    mid = 0.5 * (c + d)
    T_old, T_new = bk['T_old'], bk['T_new']

    right = np.where((mid > T_old) & (mid < T_new))[0]
    left = np.where((mid > -T_new) & (mid < -T_old))[0]
    left = left[::-1]                      # mirror so cell k pairs with right cell k
    nc = len(right)

    EG, LL = RS.source_defect(N, ncell=nc)
    DN = EG - LL

    # the source-side conjecture, normalized by the leakage norm
    iL, keep = _pinv_isqrt(LL)
    src = float(np.linalg.eigvalsh(0.5 * (iL @ DN @ iL + (iL @ DN @ iL).T))[keep.sum() * 0:].min()) \
        if keep.any() else float('nan')

    # mean / oscillation split of the source defect  (prop:newdMeanZeroSchur)
    delta = 0.5 * math.log((N + 1) / N)
    h = delta / nc
    u = np.ones(nc) / math.sqrt(delta)                       # u_N, L2-normalized
    Gs = h * np.eye(nc)
    # basis of the zero-mean subspace in L^2(0,delta)
    ones = np.ones((1, nc))
    U_, S_, Vt = np.linalg.svd(ones)
    E0 = Vt[1:].T
    dN_ = float(u @ DN @ u)
    bN = E0.T @ DN @ u
    CN = E0.T @ DN @ E0
    wC = np.linalg.eigvalsh(0.5 * (CN + CN.T))
    CNp = np.linalg.pinv(0.5 * (CN + CN.T), rcond=1e-11)
    rho = float(bN @ CNp @ bN / dN_) if dN_ != 0 else float('nan')

    Za = bk['Za']
    out = dict(N=N, refine=refine, nc=nc, dimA=bk['dimA'],
               lam=st['lam_min_norm'], src=src, rho=rho,
               dN=dN_, minC=float(wC.min()))

    S = st['S']
    for name, Xi in (('right', Za[right, :]),
                     ('sym', (Za[right, :] + Za[left, :]) / math.sqrt(2)),
                     ('anti', (Za[right, :] - Za[left, :]) / math.sqrt(2))):
        W = Xi.T @ DN @ Xi
        W = 0.5 * (W + W.T)
        iW, kp = _pinv_isqrt(W)
        if not kp.any():
            out['c_' + name] = float('nan')
            continue
        Msym = iW @ S @ iW
        ev = np.linalg.eigvalsh(0.5 * (Msym + Msym.T))
        out['c_' + name] = float(ev[-int(kp.sum()):].min())
    return out


if __name__ == '__main__':
    PP = [n for n in RA.prime_powers_upto(32)]
    print("threshold measurements   (Galerkin, piecewise constant)")
    print(f"{'N':>4} {'ref':>4} {'nc':>3} {'src':>10} {'rho_N':>9} {'rho*logN':>9} "
          f"{'lam(phys)':>10} {'c_right':>9} {'c_sym':>9} {'c_anti':>9}")
    for N in PP:
        for refine in (4, 8):
            try:
                r = measure(N, refine=refine)
            except Exception as e:
                print(f"{N:>4} {refine:>4}  FAILED {type(e).__name__}: {e}")
                continue
            print(f"{r['N']:>4} {r['refine']:>4} {r['nc']:>3} {r['src']:>10.4f} "
                  f"{r['rho']:>9.5f} {r['rho']*math.log(r['N']):>9.5f} "
                  f"{r['lam']:>10.5f} {r['c_right']:>9.4f} {r['c_sym']:>9.4f} "
                  f"{r['c_anti']:>9.4f}")
        print()
