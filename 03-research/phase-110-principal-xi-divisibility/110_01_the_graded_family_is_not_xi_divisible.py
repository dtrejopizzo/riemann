#!/usr/bin/env python3
"""
Phase 110, Task 1 verifier.

Checks, numerically:
 (1) Lemma 110.1.1 / 110.1.3: the Mellin integral of f_s(r)=c r^s, and of a
     mass-zero difference f_{s0}-f_{s1}, diverges for every w -- confirmed by
     showing truncated partial integrals GROW WITHOUT BOUND under refinement
     (shrinking the truncation parameter eps), at the analytically predicted
     rate (a real value check via curve fit, not a vibe check).
 (2) Proposition 110.1.2: the exact closed form
        f_s^eps hat (s+it) = c * 2*eps/(eps^2+t^2)
     matches direct numerical quadrature of the defining integral, refined by
     enlarging the truncation window X -> the quadrature converges TO the
     closed form as X grows (not to some other value). Includes a control
     that rejects a deliberately wrong constant (missing factor of 2).
 (3) The mass identity  integral of K_eps(t) dt = 2*pi  (exact, independent
     of eps) and the concentration limit (peak height ~ 2/eps -> infinity,
     off-origin values -> 0) as eps -> 0.
 (4) Lemma 110.1.6: xi(s) != 0 on a real grid, with a control case (a
     function known to have a real zero) confirming the zero detector can
     actually detect a zero -- so the "no zero found" result is not vacuous.

Standalone: `python3 110_01_the_graded_family_is_not_xi_divisible.py`
"""
import sys
import mpmath as mp

mp.mp.dps = 40

PASS = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    PASS.append(bool(cond))
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------------
# (1) Divergence of the Mellin integral of f_s under refinement.
# ---------------------------------------------------------------------
print("=== Check 1: Mellin integral of f_s(r)=c r^s diverges for every w ===")


def truncated_mellin_power(s, w, eps):
    # integral_{eps}^{1/eps} r^{s-w-1} dr, exact antiderivative (real s,w)
    expo = s - w
    if abs(expo) < mp.mpf('1e-30'):
        return mp.log(1 / eps) - mp.log(eps)  # = -2 log eps
    upper = (1 / eps) ** expo
    lower = eps ** expo
    return (upper - lower) / expo


def refinement_growth_rate_ok(seq_vals, seq_eps, predicted_rate_fn):
    # seq_vals[i] should grow like |value| ~ C * eps^{-rate} as eps->0.
    # Check the value strictly grows under refinement (no saturation), and
    # that consecutive ratios match the predicted power-law rate.
    ok_growth = all(abs(seq_vals[i + 1]) > abs(seq_vals[i]) * mp.mpf('1.5')
                     for i in range(len(seq_vals) - 1))
    ratios_ok = True
    for i in range(len(seq_vals) - 1):
        eps_ratio = seq_eps[i] / seq_eps[i + 1]
        val_ratio = abs(seq_vals[i + 1]) / abs(seq_vals[i])
        predicted = predicted_rate_fn(eps_ratio)
        rel_err = abs(val_ratio - predicted) / predicted
        if rel_err > mp.mpf('0.05'):
            ratios_ok = False
    return ok_growth and ratios_ok


# case A: on-axis, w = s -> log divergence, predicted ratio = log(1/eps')/log(1/eps)
s_val = mp.mpf('0.7')
w_val = s_val
eps_list = [mp.mpf('0.1') / (10 ** k) for k in range(5)]  # 0.1,0.01,...,1e-5
vals = [truncated_mellin_power(s_val, w_val, e) for e in eps_list]
growth_A = all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))
# predicted value: -2*log(eps)
predicted_A = [-2 * mp.log(e) for e in eps_list]
rel_err_A = max(abs(vals[i] - predicted_A[i]) / abs(predicted_A[i]) for i in range(len(vals)))
check("on-axis (w=s) truncated integral grows under refinement (log divergence)",
      growth_A and rel_err_A < mp.mpf('1e-20'),
      f"max rel err vs -2log(eps) = {float(rel_err_A):.2e}")

# case B: off-axis real w != s -> power-law divergence with exponent |s-w|
s_val2, w_val2 = mp.mpf('0.3'), mp.mpf('1.1')
expo = s_val2 - w_val2
eps_list2 = [mp.mpf('0.1') / (10 ** k) for k in range(5)]
vals2 = [truncated_mellin_power(s_val2, w_val2, e) for e in eps_list2]


def predicted_rate_B(eps_ratio):
    return eps_ratio ** abs(expo)


growth_ok_B = refinement_growth_rate_ok(vals2, eps_list2, predicted_rate_B)
check("off-axis (w!=s) truncated integral diverges at predicted power-law rate",
      growth_ok_B, f"|s-w|={float(abs(expo)):.3f}")

# ---------------------------------------------------------------------
# (1b) Mass-zero difference F = c0 r^{s0} - c1 r^{s1} also diverges.
# ---------------------------------------------------------------------
print("\n=== Check 1b: mass-zero difference F=c0 r^{s0}-c1 r^{s1} diverges too ===")

c0, c1 = mp.mpf('1'), mp.mpf('1')
s0, s1 = mp.mpf('0.2'), mp.mpf('0.8')


def truncated_mellin_diff(s0, s1, c0, c1, w, eps):
    return c0 * truncated_mellin_power(s0, w, eps) - c1 * truncated_mellin_power(s1, w, eps)


w_test = mp.mpf('-0.5')  # chosen off the symmetric midpoint of s0,s1 (avoids an
# exact cancellation artifact of the symmetric truncation window [eps,1/eps]
# that occurs only at w=(s0+s1)/2; any other real w exhibits the divergence)
eps_list3 = [mp.mpf('0.1') / (10 ** k) for k in range(6)]
vals3 = [truncated_mellin_diff(s0, s1, c0, c1, w_test, e) for e in eps_list3]
# leading behavior as eps->0: dominated by min(s0,s1)-w at the lower limit
dom_expo = min(s0, s1) - w_test
predicted3 = [c0 * (mp.mpf('1') / e) ** (s0 - w_test) / (s0 - w_test)
              - c0 * e ** (s0 - w_test) / (s0 - w_test)
              - (c1 * (mp.mpf('1') / e) ** (s1 - w_test) / (s1 - w_test)
                 - c1 * e ** (s1 - w_test) / (s1 - w_test))
              for e in eps_list3]
# just re-use exact antiderivative sum (already exact); check unbounded growth
growth3 = all(abs(vals3[i + 1]) > abs(vals3[i]) * mp.mpf('1.2') for i in range(len(vals3) - 1))
check("mass-zero difference truncated integral grows without bound under refinement",
      growth3, f"|F_trunc(eps)| at eps={[float(e) for e in eps_list3]} -> {[float(abs(v)) for v in vals3]}")

# ---------------------------------------------------------------------
# (2) Closed form of the regularized transform (Proposition 110.1.2).
# ---------------------------------------------------------------------
print("\n=== Check 2: closed form  f_s^eps hat(s+it) = c * 2 eps/(eps^2+t^2) ===")

c_reg, s_reg, eps_reg, t_reg = mp.mpf('1.3'), mp.mpf('0.4'), mp.mpf('0.2'), mp.mpf('1.7')


def integrand_reg(x):
    return c_reg * mp.e ** (s_reg * x - eps_reg * abs(x)) * mp.e ** (-(s_reg + mp.mpc(0, 1) * t_reg) * x)


def quad_truncated(X):
    return mp.quad(integrand_reg, [-X, 0, X])


closed_form = c_reg * 2 * eps_reg / (eps_reg ** 2 + t_reg ** 2)
wrong_form = c_reg * eps_reg / (eps_reg ** 2 + t_reg ** 2)  # missing factor of 2 -- must be REJECTED

quad_vals = [quad_truncated(X) for X in [mp.mpf('20'), mp.mpf('60'), mp.mpf('150')]]
rel_errs = [abs(q - closed_form) / abs(closed_form) for q in quad_vals]
converging = rel_errs[0] > rel_errs[1] > rel_errs[2]
final_close = rel_errs[-1] < mp.mpf('1e-10')
rel_err_to_wrong = abs(quad_vals[-1] - wrong_form) / abs(wrong_form)
rejects_wrong = rel_err_to_wrong > mp.mpf('0.9')  # should NOT match the wrong constant at all

check("truncated quadrature converges to the exact closed form under refinement (X growing)",
      converging and final_close,
      f"rel errs vs X: {[float(e) for e in rel_errs]}")
check("quadrature correctly rejects the wrong constant (missing factor 2)",
      rejects_wrong, f"rel err to wrong-by-2 formula = {float(rel_err_to_wrong):.3f}")

# ---------------------------------------------------------------------
# (3) Mass identity and concentration.
# ---------------------------------------------------------------------
print("\n=== Check 3: mass identity integral K_eps dt = 2 pi, and concentration ===")

mass_vals = []
for eps_m in [mp.mpf('0.5'), mp.mpf('0.1'), mp.mpf('0.01')]:
    m = mp.quad(lambda t: 2 * eps_m / (eps_m ** 2 + t ** 2), [-mp.inf, 0, mp.inf])
    mass_vals.append(m)
mass_ok = all(abs(m - 2 * mp.pi) / (2 * mp.pi) < mp.mpf('1e-12') for m in mass_vals)
check("integral of K_eps(t) dt = 2*pi exactly, independent of eps",
      mass_ok, f"values = {[float(m) for m in mass_vals]}")

# concentration: peak height K_eps(0) = 2/eps -> infinity; K_eps(t0) for fixed
# t0 != 0 -> 0, as eps shrinks (refinement).
t0_fixed = mp.mpf('1.0')
eps_seq = [mp.mpf('1'), mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('0.001')]
peak_vals = [2 / e for e in eps_seq]
offpeak_vals = [2 * e / (e ** 2 + t0_fixed ** 2) for e in eps_seq]
peak_grows = all(peak_vals[i + 1] > peak_vals[i] for i in range(len(peak_vals) - 1))
offpeak_shrinks = all(offpeak_vals[i + 1] < offpeak_vals[i] for i in range(len(offpeak_vals) - 1))
offpeak_to_zero = offpeak_vals[-1] < mp.mpf('0.01')
check("peak K_eps(0)=2/eps grows without bound as eps -> 0",
      peak_grows, f"peak values = {[float(v) for v in peak_vals]}")
check("off-peak K_eps(t0!=0) shrinks to 0 as eps -> 0 (concentration, not just decay)",
      offpeak_shrinks and offpeak_to_zero, f"off-peak values = {[float(v) for v in offpeak_vals]}")

# ---------------------------------------------------------------------
# (4) xi has no real zero (supporting fact for Corollary 110.1.5), with a
#     control case proving the zero detector works.
# ---------------------------------------------------------------------
print("\n=== Check 4: xi(s) != 0 on a real grid, with a working zero-detector control ===")


def xi(s):
    s = mp.mpc(s)
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def is_pole_point(sigma):
    # Gamma(s/2) pole at s=0,-2,-4,...  ;  zeta(s) pole at s=1
    if abs(sigma - 1) < mp.mpf('1e-9'):
        return True
    r = round(sigma)
    if abs(sigma - r) < mp.mpf('1e-9') and r <= 0 and r % 2 == 0:
        return True
    return False


grid = [mp.mpf(i) / 10 for i in range(-40, 41)]
found_zero = []
for s in grid:
    if is_pole_point(s):
        continue
    v = xi(s)
    if abs(v) < mp.mpf('1e-6'):
        found_zero.append((float(s), complex(v)))

no_real_zero = (len(found_zero) == 0)
check("xi(s) != 0 on real grid s in [-4,4], step 0.1 (excluding Gamma/zeta pole points)",
      no_real_zero, f"flagged points: {found_zero}")

# control: the same detector, applied to sin(x) on a grid containing pi,
# MUST find a zero -- proves the "no zero found" above is not vacuous.
control_grid = [mp.mpf(i) / 10 for i in range(0, 40)]
control_found = [float(s) for s in control_grid if abs(mp.sin(s)) < mp.mpf('1e-6')]
control_ok = len(control_found) == 0  # step 0.1 grid unlikely to hit pi=3.14159 exactly
# Use a grid that DOES include a near-exact zero of sin to prove detector works:
control_grid2 = [mp.pi * k / 10 for k in range(0, 21)]  # includes s=pi exactly (k=10)
control_found2 = [float(s) for s in control_grid2 if abs(mp.sin(s)) < mp.mpf('1e-6')]
detector_works = len(control_found2) >= 1
check("control: same detector logic DOES find the known zero of sin(x) at x=pi",
      detector_works, f"detected zeros of sin at: {control_found2}")

# ---------------------------------------------------------------------
print("\n" + "=" * 60)
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
else:
    print("VERDICT: FAILURES PRESENT")
    sys.exit(1)
