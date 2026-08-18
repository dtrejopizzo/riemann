"""W4 exploratory probe (FLOATING POINT ONLY) of the near-null direction
structure at the T=(1/2)log5 step (first step beyond the certified log2
endpoint), per SPEC section 2 point 3: "what is the minimizing direction,
and does it stay on the positive side."

Command:
  cd .../phase-118-the-exact-threshold-inequality/scripts
  python3 W4_near_null_structure.py
"""
import math
import numpy as np
import rowd_threshold as RT
import rowd_assembly as RA

qo, qn, refine = 4, 5, 32
bk = RT.threshold_blocks(qo, qn, refine=refine)
st = RT.schur_target(bk)
print(f"step ({qo},{qn}): T_old={bk['T_old']:.5f} T_new={bk['T_new']:.5f} "
      f"dimC={bk['dimC']} dimA={bk['dimA']} lam_min_norm={st['lam_min_norm']:.6f}")

# Recover the normalized minimizer in the corona (dimA-dim) space.
S_E = st['S_E']; S = st['S']
w, V = np.linalg.eigh(0.5*(S_E+S_E.T))
keep = w > 1e-11*w.max()
isq = V[:, keep] @ np.diag(1/np.sqrt(w[keep])) @ V[:, keep].T
Snorm = isq @ S @ isq
lam, U = np.linalg.eigh(0.5*(Snorm+Snorm.T))
kmin = np.argmin(lam)
u = isq @ U[:, kmin]  # in corona coefficient space (w.r.t Za basis)
print("min eigval check:", lam[kmin], "vs reported", st['lam_min_norm'])

# Express corona vector back in the physical piecewise-constant basis.
Za = bk['Za']
phys = Za @ u  # coefficients (Gram-form) over the full new mesh
M = bk['M']
c, d = M['c'], M['d']
mid = 0.5*(c+d)
Gram = M['Gram']
norm = math.sqrt(phys @ Gram @ phys)
phys = phys/norm

# Report mass distribution: fraction of L2 norm inside old window vs annulus,
# and how much overlaps the two Tate directions restricted to old core.
T_old = bk['T_old']; T_new = bk['T_new']
inside = np.abs(mid) < T_old
mass_in = float(np.sum(Gram[inside,inside]*phys[inside]**2))
mass_out = float(np.sum(Gram[~inside,~inside]*phys[~inside]**2))
print(f"L2 mass fraction inside old core |t|<T_old:  {mass_in:.5f}")
print(f"L2 mass fraction in annulus T_old<=|t|<T_new: {mass_out:.5f}")

# overlap with e^{-t/2}, e^{t/2} restricted to annulus (the two Tate directions
# defining the corona's non-annulus piece)
em = np.exp(-mid/2); ep = np.exp(mid/2)
ov_m = float(phys @ Gram @ em) / math.sqrt(em @ Gram @ em)
ov_p = float(phys @ Gram @ ep) / math.sqrt(ep @ Gram @ ep)
print(f"normalized overlap with e^(-t/2): {ov_m:.5f},  with e^(+t/2): {ov_p:.5f}")

# crude parity check (even/odd in t)
neg_idx = np.argsort(mid)
# reflect: compare phys(t) vs phys(-t) via interpolation on the mesh (piecewise const -> match cell by cell using mirrored midpoints)
order = np.argsort(mid)
mid_s = mid[order]; phys_s = phys[order]
phys_mirror = np.interp(-mid_s, mid_s, phys_s)
even_part = 0.5*(phys_s+phys_mirror)
odd_part = 0.5*(phys_s-phys_mirror)
print(f"||even part||/||full||: {np.linalg.norm(even_part)/np.linalg.norm(phys_s):.4f}, "
      f"||odd part||/||full||: {np.linalg.norm(odd_part)/np.linalg.norm(phys_s):.4f}")

# where in the annulus does |phys| peak?
ann = ~inside
if ann.sum():
    idxmax = np.where(ann)[0][np.argmax(np.abs(phys[ann]))]
    print(f"annulus |phys| peak at t={mid[idxmax]:.4f} (T_old={T_old:.4f}, T_new={T_new:.4f})")
