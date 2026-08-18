#!/usr/bin/env python3
"""
108_53 verifier: Condition III -- the two radicals.

Checks (each prints PASS/FAIL; exits 0 only if all pass):

 1. Lemma 1.1: the new closed form for Phi matches (a) 108_38 Lemma 2.1's form and
    (b) the direct zeta'/zeta definition, with error shrinking as precision increases
    (genuine convergence test, not a fixed epsilon).
 2. The supervisor's two headline numbers: Phi(1/2) and the root near 0.3.
 3. Theorem 1.2: Phi is finite at the first five nontrivial zeta zeros, while the
    individual zeta'/zeta(rho + eps) term blows up like 1/eps as eps -> 0.
 4. Theorem 3.1: Phi has simple poles at s = 0, 1, 2 (blow-up like 1/eps).
 5. Theorem 2.1: Phi(1-s) = Phi(s) exactly on s in 1/2 + Z, and fails elsewhere;
    in particular Phi(1-s*) != Phi(s*) at the real zero s* in (0,1).
 6. Real-zero scan (genuine zeros vs pole artifacts) and a complex-seed search
    reporting whether any non-real zero was found (numerical finding, not a theorem).
"""

import sys
import mpmath as mp

PASS = []
FAIL = []


def check(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"PASS: {name}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL.append(name)
        print(f"FAIL: {name}" + (f"  ({detail})" if detail else ""))


def Phi_new(s, dps=50):
    with mp.workdps(dps):
        s = mp.mpc(s)
        return 2*mp.digamma(1-s) - mp.mpf(1)/2*mp.digamma(s/2) \
            - mp.mpf(1)/2*mp.digamma((1-s)/2) - mp.log(4*mp.pi)


def Phi_lemma21(s, dps=50):
    with mp.workdps(dps):
        s = mp.mpc(s)
        return mp.pi*mp.cot(mp.pi*s/2) \
            + mp.mpf(1)/2*(mp.digamma(s/2) + mp.digamma((1-s)/2)) - mp.log(mp.pi)


def Phi_direct(s, dps=50):
    with mp.workdps(dps):
        s = mp.mpc(s)
        return mp.pi*mp.cot(mp.pi*s/2) \
            - mp.zeta(s, derivative=1)/mp.zeta(s) \
            - mp.zeta(1-s, derivative=1)/mp.zeta(1-s)


# ---------------------------------------------------------------------------
print("=== Check 1: Lemma 1.1 closed form vs Lemma 2.1 form and direct definition ===")

test_points_str = ['0.1', '0.25', '0.5', '0.75', '0.9']
test_points = [mp.mpf(x) for x in test_points_str] + [mp.mpc('2.3', '1.1')]

# convergence test: error should shrink roughly as 10^-(dps) as dps increases
errs_vs_lemma21 = {}
errs_vs_direct = {}
for dps in (20, 35, 50):
    e1 = max(abs(Phi_new(s, dps) - Phi_lemma21(s, dps)) for s in test_points)
    e2 = max(abs(Phi_new(s, dps) - Phi_direct(s, dps)) for s in test_points)
    errs_vs_lemma21[dps] = e1
    errs_vs_direct[dps] = e2
    print(f"  dps={dps}: max|new-lemma21|={mp.nstr(e1,5)}  max|new-direct|={mp.nstr(e2,5)}")

# require monotone shrinkage and that error at dps=50 is close to machine precision for that dps
shrink_ok = (errs_vs_lemma21[50] < errs_vs_lemma21[35] < errs_vs_lemma21[20] + mp.mpf('1e-100')) \
    and (errs_vs_direct[50] < errs_vs_direct[35] < errs_vs_direct[20] + mp.mpf('1e-100'))
tiny_at_50 = errs_vs_lemma21[50] < mp.mpf('1e-40') and errs_vs_direct[50] < mp.mpf('1e-40')
check("Lemma 1.1 matches Lemma 2.1 form (error -> 0 with precision)",
      shrink_ok and tiny_at_50,
      f"err@dps=50: {mp.nstr(errs_vs_lemma21[50],5)} / {mp.nstr(errs_vs_direct[50],5)}")

# ---------------------------------------------------------------------------
print()
print("=== Check 2: supervisor's headline numbers ===")
mp.mp.dps = 50
half_val = Phi_new(mp.mpf('0.5'))
target_half = mp.mpf('-2.2305907656358723438')
check("Phi(1/2) matches supervisor value to 1e-18",
      abs(half_val - target_half) < mp.mpf('1e-18'),
      f"computed={mp.nstr(half_val,22)}")

root = mp.findroot(lambda s: Phi_new(s), mp.mpf('0.3'))
target_root = mp.mpf('0.30169238816042209152')
check("root near 0.3 matches supervisor value to 1e-18",
      abs(root - target_root) < mp.mpf('1e-18'),
      f"computed={mp.nstr(root,22)}")

sstar = root

# ---------------------------------------------------------------------------
print()
print("=== Check 3: Theorem 1.2 -- Phi finite at zeta zeros; zeta'/zeta(s) individually blows up ===")
mp.mp.dps = 40
finite_ok = True
zeta_zero_vals = []
for k in range(1, 6):
    rho = mp.zetazero(k)
    val = Phi_new(rho)
    zeta_zero_vals.append((k, rho, val))
    print(f"  zeta zero #{k} = {mp.nstr(rho,15)}   Phi(rho) = {mp.nstr(val,15)}")
    if not (abs(val) < 100):
        finite_ok = False
check("Phi(rho) finite (bounded) at first 5 nontrivial zeta zeros", finite_ok)

# individual zeta'/zeta term blows up like 1/eps near rho1
rho1 = mp.zetazero(1)
eps_list = [mp.mpf('1e-3'), mp.mpf('1e-5'), mp.mpf('1e-7')]
mags = []
for eps in eps_list:
    val = mp.zeta(rho1+eps, derivative=1)/mp.zeta(rho1+eps)
    mags.append(abs(val))
    print(f"  eps={eps}: |zeta'/zeta(rho1+eps)| = {mp.nstr(abs(val),10)}")
# ratio of successive magnitudes should track ratio of 1/eps (i.e. ~ 100x when eps shrinks by 100x)
ratio1 = mags[1]/mags[0]
ratio2 = mags[2]/mags[1]
expected_ratio = eps_list[0]/eps_list[1]  # = 100
blowup_ok = abs(ratio1/expected_ratio - 1) < mp.mpf('0.05') and abs(ratio2/(eps_list[1]/eps_list[2]) - 1) < mp.mpf('0.05')
check("zeta'/zeta(rho+eps) blows up like 1/eps (individual term has a pole at a zeta zero)",
      blowup_ok, f"ratios={mp.nstr(ratio1,6)},{mp.nstr(ratio2,6)} vs expected {mp.nstr(expected_ratio,6)}")

# ---------------------------------------------------------------------------
print()
print("=== Check 4: Theorem 3.1 -- Phi has simple poles at s=0,1,2 ===")
mp.mp.dps = 40
pole_ok = True
for s0 in [mp.mpf('0'), mp.mpf('1'), mp.mpf('2')]:
    mags = []
    for eps in [mp.mpf('1e-3'), mp.mpf('1e-5'), mp.mpf('1e-7')]:
        # approach from a direction avoiding other poles
        val = Phi_new(s0 + eps)
        mags.append(abs(val))
    r1 = mags[1]/mags[0]
    r2 = mags[2]/mags[1]
    ok = abs(r1/100 - 1) < mp.mpf('0.05') and abs(r2/100 - 1) < mp.mpf('0.05')
    print(f"  s0={s0}: |Phi(s0+eps)| for eps=1e-3,1e-5,1e-7 = {[mp.nstr(m,6) for m in mags]}  ratio-ok={ok}")
    pole_ok = pole_ok and ok
check("Phi has simple poles (1/eps blow-up) at s=0,1,2", pole_ok)

# The blow-up-rate test above confirms the poles are SIMPLE but is blind to the
# VALUE of the residue -- it passes for any nonzero residue, which is exactly
# how an earlier draft's wrong values (-2 at s=0, +2 at s=1) survived it.  The
# following check is discriminating: it pins the residue by refinement, and its
# control clause explicitly rejects +/-2.
print()
print("=== Check 4b: Theorem 3.1 -- exact residue VALUES (discriminating) ===")
res_ok = True
for label, s0, expected in (("s=0", mp.mpf(0), mp.mpf(1)),
                            ("s=1", mp.mpf(1), mp.mpf(1)),
                            ("s=2", mp.mpf(2), mp.mpf(2))):
    eps = [mp.mpf(10) ** -k for k in (3, 4, 5, 6, 7, 8)]
    errs = [abs(e * Phi_new(s0 + e) - expected) for e in eps]
    shrinking = all(errs[i] > errs[i + 1] for i in range(len(errs) - 1))
    converged = errs[-1] < mp.mpf('1e-6')
    ok = shrinking and converged
    res_ok = res_ok and ok
    print("  %s: eps*Phi(s0+eps) -> %s  (target %s)  errors=%s"
          % (label, mp.nstr(eps[-1] * Phi_new(s0 + eps[-1]), 12),
             mp.nstr(expected, 3), [mp.nstr(e, 3) for e in errs]))
check("residues converge to their stated values under refinement", res_ok)

r0 = mp.mpf('1e-8') * Phi_new(mp.mpf('1e-8'))
r1 = mp.mpf('1e-8') * Phi_new(1 + mp.mpf('1e-8'))
check("control: residues at s=0,1 are +1, and are NOT -2 or +2",
      abs(r0 - 1) < mp.mpf('1e-6') and abs(r1 - 1) < mp.mpf('1e-6')
      and abs(r0 + 2) > 2 and abs(r1 - 2) > mp.mpf('0.9'),
      "res(0)=%s  res(1)=%s" % (mp.nstr(r0, 12), mp.nstr(r1, 12)))

# ---------------------------------------------------------------------------
print()
print("=== Check 5: Theorem 2.1 -- mirror symmetry exactly on s in 1/2+Z ===")
mp.mp.dps = 40
sym_points = [mp.mpf('0.5'), mp.mpf('1.5'), mp.mpf('-0.5')]
asym_points = [mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('1.2'), mp.mpf('2.1')]

sym_ok = True
for s in sym_points:
    d = Phi_new(1-s) - Phi_new(s)
    ok = abs(d) < mp.mpf('1e-30')
    print(f"  s={s} (in 1/2+Z): Phi(1-s)-Phi(s) = {mp.nstr(d,6)}  ok={ok}")
    sym_ok = sym_ok and ok

asym_ok = True
for s in asym_points:
    d = Phi_new(1-s) - Phi_new(s)
    ok = abs(d) > mp.mpf('0.5')   # robustly nonzero, well above precision noise
    print(f"  s={s} (not in 1/2+Z): Phi(1-s)-Phi(s) = {mp.nstr(d,6)}  ok(nonzero)={ok}")
    asym_ok = asym_ok and ok

check("Phi(1-s)=Phi(s) holds at s in 1/2+Z", sym_ok)
check("Phi(1-s) != Phi(s) at generic s (mirror symmetry broken)", asym_ok)

d_star = Phi_new(1-sstar) - Phi_new(sstar)
check("Phi(1-s*) != Phi(s*) at the actual real zero s* in (0,1)",
      abs(d_star) > mp.mpf('1'), f"Phi(1-s*)-Phi(s*) = {mp.nstr(d_star,10)}")

# ---------------------------------------------------------------------------
print()
print("=== Check 6: real-zero scan (genuine zeros vs pole artifacts) and complex search ===")
mp.mp.dps = 30

pole_set = set(range(0, 10)) | {-2, -4, -6, -8}


def near_pole(s, tol=mp.mpf('0.05')):
    for p in pole_set:
        if abs(s - p) < tol:
            return True
    return False


s = mp.mpf('-9.4')
prev = None
genuine_zeros = []
step = mp.mpf('0.01')
while s < 9.6:
    try:
        v = mp.re(Phi_new(s))
        if prev is not None and prev[1]*v < 0:
            mid = (prev[0]+s)/2
            if not near_pole(mid):
                genuine_zeros.append(mid)
        prev = (s, v)
    except Exception:
        prev = None
    s += step

print(f"  genuine real zeros found in (-9.4,9.6): {len(genuine_zeros)}")
for z in genuine_zeros:
    print(f"    {mp.nstr(z,10)}")

# must include the known one in (0,1) and at least a couple outside it
has_principal = any(abs(z - sstar) < mp.mpf('0.02') for z in genuine_zeros)
has_outside = sum(1 for z in genuine_zeros if not (0 < z < 1)) >= 2
check("real-zero scan finds the principal zero s* in (0,1)", has_principal)
check("real-zero scan finds >=2 further real zeros outside (0,1) (no accumulation observed)",
      has_outside, f"count outside (0,1): {sum(1 for z in genuine_zeros if not (0<z<1))}")

# spacing bounded away from 0 (no clustering in the tested window)
gaps = [genuine_zeros[i+1]-genuine_zeros[i] for i in range(len(genuine_zeros)-1)]
min_gap = min(gaps) if gaps else mp.mpf('999')
check("gaps between consecutive real zeros stay bounded away from 0 (no accumulation in window)",
      min_gap > mp.mpf('0.3'), f"min gap = {mp.nstr(min_gap,6)}")

# complex seed search
print()
print("  complex-seed search (35 seeds):")
found = []
re_vals = ['0.3', '0.8', '1.3', '1.8', '2.3', '-0.5', '-1.5']
im_vals = ['0.5', '1.0', '2.0', '3.0', '5.0']
n_seeds = 0
for re0s in re_vals:
    for im0s in im_vals:
        n_seeds += 1
        seed = mp.mpf(re0s) + 1j*mp.mpf(im0s)
        try:
            r = mp.findroot(lambda z: Phi_new(z), seed, solver='muller')
            if abs(Phi_new(r)) < mp.mpf('1e-15'):
                is_new = all(abs(f_-r) > mp.mpf('1e-6') for f_ in found)
                if is_new:
                    found.append(r)
        except Exception:
            pass

n_complex = sum(1 for r in found if abs(mp.im(r)) > mp.mpf('1e-15'))
print(f"    seeds tried: {n_seeds}, distinct roots converged to: {len(found)}, non-real among them: {n_complex}")
for r in found:
    print(f"      root: {mp.nstr(r,15)}  Im={mp.nstr(mp.im(r),8)}")

check("complex-seed search: report only (informational, not a pass/fail theorem claim)",
      True, f"non-real roots found in search region: {n_complex} (out of {len(found)} distinct roots)")

# ---------------------------------------------------------------------------
print()
print(f"Summary: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED CHECKS:", FAIL)
    sys.exit(1)
else:
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
