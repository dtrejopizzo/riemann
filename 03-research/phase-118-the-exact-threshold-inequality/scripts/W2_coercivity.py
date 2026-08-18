"""W2 task (3): which block carries the refinement-decay of lam_min_norm, and
is lambda_min(M_aa) (the annulus block, S_E-normalized metric) coercive --
bounded away from 0, growing like log(1/delta_j)?

Reads W2_sweep_refine.json (all 25 PRIME_POWER_STEPS at refine 8/16/32/64,
rtol=1e-11) and W2_sweep.json (5 cheap steps, refine 8/16/32/64, rtol swept)
written by W2_sweep_refine.py / W2_sweep.py. Produces two analyses:

(A) REFINEMENT ATTRIBUTION, per step: compare, from refine=8 to refine=64,
    the ratio-of-decrease of lam_min_norm against that of lamM_aa and of
    min(eigM_tt) and of the Schur-complement min(tt - at' aa^dag at). The
    block whose ratio-of-decrease most closely matches lam_min_norm's is the
    one "carrying" the refinement fall.

(B) COERCIVITY REGRESSION, at fixed refine=64 (finest available across all 25
    steps): regress log(lamM_aa) against log(1/delta_j) across the 25 steps.
    Galerkin note: lamM_aa is a Rayleigh-quotient minimum over a FINITE-
    DIMENSIONAL subspace (the annulus-primitive Galerkin space at this mesh),
    which is a subspace of the true continuum annulus-primitive space; a
    variational minimum over a subspace is >= the minimum over the full
    space, so this is an UPPER bound on the continuum lambda_min(M_aa) at
    this delta_j -- same direction as lam_min_norm itself. Refining further
    can only lower it (nested meshes), so the true coercivity constant (if
    any) is <= every number reported here.

Command:
    python3 W2_coercivity.py
"""
import json
import numpy as np

with open('W2_sweep_refine.json') as f:
    broad = json.load(f)
with open('W2_sweep.json') as f:
    deep = json.load(f)

# ---- (A) attribution: refine=8 -> refine=64 decrease ratio, per quantity ---
by_step = {}
for r in broad:
    key = (r['q_old'], r['q_new'])
    by_step.setdefault(key, {})[r['refine']] = r

print("=== (A) refinement attribution: ratio (value at refine=64)/(value at refine=8) ===")
print(f"{'step':>10} {'delta':>8} {'lam(8->64)':>12} {'lamM_aa(8->64)':>15} "
      f"{'minTt(8->64)':>13} {'schurTt(8->64)':>15}")
rows = []
for key, d in by_step.items():
    if 8 not in d or 64 not in d:
        continue
    r8, r64 = d[8], d[64]
    ratio_lam = r64['lam_min_norm_ref'] / r8['lam_min_norm_ref']
    ratio_aa = r64['lamM_aa'] / r8['lamM_aa']
    ratio_tt = min(r64['eigM_tt']) / min(r8['eigM_tt'])
    ratio_schur = min(r64['schurM_tt_minus']) / min(r8['schurM_tt_minus'])
    rows.append((key, r8['delta'], ratio_lam, ratio_aa, ratio_tt, ratio_schur))
    print(f"{str(key):>10} {r8['delta']:8.4f} {ratio_lam:12.4f} {ratio_aa:15.4f} "
          f"{ratio_tt:13.4f} {ratio_schur:15.4f}")

ratios_lam = np.array([r[2] for r in rows])
ratios_aa = np.array([r[3] for r in rows])
ratios_tt = np.array([r[4] for r in rows])
ratios_schur = np.array([r[5] for r in rows])
print(f"\nmedian ratio lam_min_norm(64/8)  = {np.median(ratios_lam):.4f}")
print(f"median ratio lamM_aa(64/8)       = {np.median(ratios_aa):.4f}")
print(f"median ratio min(eigM_tt)(64/8)  = {np.median(ratios_tt):.4f}")
print(f"median ratio Schur-min(64/8)     = {np.median(ratios_schur):.4f}")
# correlation of log-ratios: which one tracks lam_min_norm's fall best?
for name, arr in [('lamM_aa', ratios_aa), ('min(eigM_tt)', ratios_tt), ('Schur-min', ratios_schur)]:
    c = np.corrcoef(np.log(ratios_lam), np.log(arr))[0, 1]
    print(f"corr(log ratio lam_min_norm, log ratio {name}) = {c:.4f}")

# ---- (B) coercivity regression at refine=64, across all steps -------------
print("\n=== (B) coercivity regression at refine=64: log(lamM_aa) vs log(1/delta_j) ===")
xs, ys, labels = [], [], []
for r in broad:
    if r['refine'] != 64:
        continue
    xs.append(np.log(1.0 / r['delta']))
    ys.append(np.log(r['lamM_aa']))
    labels.append((r['q_old'], r['q_new']))
xs = np.array(xs)
ys = np.array(ys)
A = np.vstack([xs, np.ones_like(xs)]).T
slope, intercept = np.linalg.lstsq(A, ys, rcond=None)[0]
resid = ys - (slope * xs + intercept)
ss_res = np.sum(resid**2)
ss_tot = np.sum((ys - ys.mean())**2)
r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float('nan')
print(f"fit: log(lamM_aa) = {slope:.4f} * log(1/delta) + {intercept:.4f}   R^2={r2:.4f}")
print(f"  (i.e. lamM_aa ~ delta^{-slope:.4f} at refine=64; hypothesis predicted"
      f" lamM_aa ~ log(1/delta), i.e. NOT a power law -- check both fits)")
# also fit against log(1/delta) directly is what we did (power law in 1/delta);
# additionally fit lamM_aa (not log) vs log(1/delta) linearly, to test the
# log-growth hypothesis literally:
A2 = np.vstack([np.log(1.0 / np.array([r['delta'] for r in broad if r['refine'] == 64])), np.ones(len(xs))]).T
yl = np.array([r['lamM_aa'] for r in broad if r['refine'] == 64])
slope2, intercept2 = np.linalg.lstsq(A2, yl, rcond=None)[0]
resid2 = yl - (slope2 * A2[:, 0] + intercept2)
r2b = 1 - np.sum(resid2**2) / np.sum((yl - yl.mean())**2)
print(f"linear-in-log fit: lamM_aa = {slope2:.5f} * log(1/delta) + {intercept2:.5f}   R^2={r2b:.4f}")

print(f"\nmin(lamM_aa) over all steps at refine=64: {min(r['lamM_aa'] for r in broad if r['refine']==64):.6e}")
print(f"max(lamM_aa) over all steps at refine=64: {max(r['lamM_aa'] for r in broad if r['refine']==64):.6e}")

# ---- also report the same two analyses for the PLAIN L2 metric (lamT_aa) --
print("\n=== same regression, PLAIN L2 metric (lamT_aa) at refine=64 ===")
ysT = np.array([np.log(r['lamT_aa']) for r in broad if r['refine'] == 64])
A = np.vstack([xs, np.ones_like(xs)]).T
slopeT, interceptT = np.linalg.lstsq(A, ysT, rcond=None)[0]
residT = ysT - (slopeT * xs + interceptT)
r2T = 1 - np.sum(residT**2) / np.sum((ysT - ysT.mean())**2)
print(f"fit: log(lamT_aa) = {slopeT:.4f} * log(1/delta) + {interceptT:.4f}   R^2={r2T:.4f}")
print(f"min(lamT_aa) at refine=64: {min(r['lamT_aa'] for r in broad if r['refine']==64):.6e}")
print(f"max(lamT_aa) at refine=64: {max(r['lamT_aa'] for r in broad if r['refine']==64):.6e}")

with open('W2_coercivity_summary.json', 'w') as f:
    json.dump(dict(
        attribution_rows=[dict(step=list(k), delta=d, ratio_lam=rl, ratio_aa=ra,
                                ratio_tt=rt, ratio_schur=rs)
                           for (k, d, rl, ra, rt, rs) in rows],
        power_law_fit_M=dict(slope=slope, intercept=intercept, r2=r2),
        linear_log_fit_M=dict(slope=slope2, intercept=intercept2, r2=r2b),
        power_law_fit_T=dict(slope=slopeT, intercept=interceptT, r2=r2T),
    ), f, indent=1)
print("\nwrote W2_coercivity_summary.json")
