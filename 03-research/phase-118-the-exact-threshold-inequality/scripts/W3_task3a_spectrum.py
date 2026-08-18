"""W3 task (3) spectral part + task (5): singular values of Phi = Y X^dagger
restricted to Ran(X_T), and the near-maximizing direction as a function of t.

Since Phi X_T = Y_T on the domain P_T (Douglas), for any domain vector v,
  ||Phi(X_T v)||^2 / ||X_T v||^2 = (v^T L_P v) / (v^T R_P v).
So the squared singular values of Phi|_{Ran(X_T)} are exactly the generalized
eigenvalues of the pencil (L_P, R_P), and the "singular vectors of Phi as
functions of t" are, pulled back through X_T, exactly the generalized
eigenvectors v (piecewise-constant functions F = Z@v on the mesh of I_T).
This needs no explicit codomain construction -- only R_P, L_P, which are
already validated against X^*X, Y^*Y in W3_task1_verify.py.

This is also literally task (5): the top generalized eigenvector (closest
eigenvalue to 1, i.e. lam_min_norm closest to 0) IS the near-maximizing F.

Run:  python3 W3_task3a_spectrum.py
"""
import math
import numpy as np
import scipy.linalg as sla
import W3_build_xy as W3

THRESHOLDS = [2, 3, 5, 8, 13, 19, 32, 37]
REFINES = [8, 16]


def spectrum_and_top_modes(q, refine, n_report=6):
    T = 0.5 * math.log(q)
    ch = W3.build_channels(T, refine=refine)
    Z = W3.primitive_basis(ch['Tate'], ch['Gram'])
    rc = W3.restrict_channels(ch, Z)
    R_P, L_P = rc['R_P'], rc['L_P']
    R_P = 0.5 * (R_P + R_P.T)
    L_P = 0.5 * (L_P + L_P.T)
    # generalized eig: L_P v = lam R_P v  (R_P should be pos. def.)
    lam, V = sla.eigh(L_P, R_P)
    order = np.argsort(lam)[::-1]
    lam = lam[order]
    V = V[:, order]
    c, d = ch['c'], ch['d']
    mid = 0.5 * (c + d)
    modes = []
    for k in range(min(n_report, V.shape[1])):
        v = V[:, k]
        F = Z @ v  # values on the mesh, as an actual function of t
        # normalize sign: make the value at largest |F| positive
        F = F * np.sign(F[np.argmax(np.abs(F))])
        modes.append(F)
    return dict(T=T, q=q, refine=refine, mid=mid, c=c, d=d, lam=lam, modes=modes,
                dimP=R_P.shape[0], minR=float(np.linalg.eigvalsh(R_P).min()))


def describe_mode(mid, F, T):
    """Cheap description: support, sign changes, endpoint behaviour, peak loc."""
    absF = np.abs(F)
    thresh = 0.02 * absF.max()
    active = absF > thresh
    if not active.any():
        return "~0 everywhere"
    lo, hi = mid[active].min(), mid[active].max()
    sgn = np.sign(F[active])
    nsign = int(np.sum(np.diff(sgn) != 0))
    peak = mid[np.argmax(absF)]
    edge_frac = 0.1 * T
    near_edge = np.abs(mid[active]) > (T - edge_frac)
    edge_share = float(near_edge.sum()) / float(active.sum())
    val_at_0_idx = np.argmin(np.abs(mid))
    return (f"support~[{lo:+.2f},{hi:+.2f}] (T={T:.2f}), sign changes~{nsign}, "
            f"peak at t={peak:+.3f}, |F|max={absF.max():.3g}, "
            f"F(t~0)={F[val_at_0_idx]:+.3g}, edge-active-frac={edge_share:.2f}")


def run():
    rows = []
    for refine in REFINES:
        for q in THRESHOLDS:
            r = spectrum_and_top_modes(q, refine)
            lam = r['lam']
            near1 = int(np.sum(lam > 1 - 1e-3))
            print(f"q={q:3d} refine={refine:3d} dimP={r['dimP']:4d} minR={r['minR']:.3e}  "
                  f"top lam: {['%.6f'%x for x in lam[:6]]}  #(>1-1e-3)={near1}")
            for k, F in enumerate(r['modes'][:3]):
                desc = describe_mode(r['mid'], F, r['T'])
                print(f"    mode[{k}] lam={lam[k]:.6f}: {desc}")
            rows.append(dict(q=q, refine=refine, dimP=r['dimP'], minR=r['minR'],
                              lam_top=lam[:10].tolist(), near1=near1))
    return rows


if __name__ == '__main__':
    run()
