"""W4 exploratory probe (FLOATING POINT ONLY): parity and localization of the
near-null corona direction across several steps beyond log2.
Command: python3 W4_near_null_parity_scan.py
"""
import math
import numpy as np
import rowd_threshold as RT

def analyze(qo, qn, refine=24):
    bk = RT.threshold_blocks(qo, qn, refine=refine)
    st = RT.schur_target(bk)
    S_E = st['S_E']; S = st['S']
    w, V = np.linalg.eigh(0.5*(S_E+S_E.T))
    keep = w > 1e-11*w.max()
    isq = V[:, keep] @ np.diag(1/np.sqrt(w[keep])) @ V[:, keep].T
    Snorm = isq @ S @ isq
    lam, U = np.linalg.eigh(0.5*(Snorm+Snorm.T))
    kmin = np.argmin(lam)
    u = isq @ U[:, kmin]
    Za = bk['Za']; phys = Za @ u
    M = bk['M']; c, d = M['c'], M['d']; mid = 0.5*(c+d); Gram = M['Gram']
    norm = math.sqrt(phys @ Gram @ phys); phys = phys/norm
    order = np.argsort(mid); mid_s = mid[order]; phys_s = phys[order]
    phys_mirror = np.interp(-mid_s, mid_s, phys_s)
    even_frac = np.linalg.norm(0.5*(phys_s+phys_mirror))/np.linalg.norm(phys_s)
    T_old = bk['T_old']
    inside = np.abs(mid) < T_old
    mass_in = float(np.sum(Gram[inside,inside]*phys[inside]**2))
    idxmax = np.argmax(np.abs(phys))
    return st['lam_min_norm'], even_frac, mass_in, mid[idxmax]

for qo, qn in [(4,5),(5,7),(7,8),(8,9),(9,11),(11,13)]:
    lam, ev, min_, peak = analyze(qo, qn)
    print(f"({qo:2},{qn:2}) lam_min_norm={lam:.5f}  even_frac={ev:.4f}  "
          f"mass_in_old_core={min_:.4f}  peak_t={peak:+.4f}  (T_old={0.5*math.log(qo):.4f})")
