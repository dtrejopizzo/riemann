#!/usr/bin/env python3
"""
Phase 110, Task 3 verifier.

Checks, numerically:
 (1) Proposition 110.3.1: replacing zeta(sigma) by an arbitrary bounded,
     zero-free dummy factor leaves the leading growth constant of
     log|xi(sigma)| (governing Theorem 110.2.4's obstruction) numerically
     UNCHANGED -- the obstruction does not depend on zeta's zero structure.
 (2) Proposition 110.3.2: replacing Gamma(sigma/2) by a bounded dummy
     DESTROYS the obstruction -- log|xi**(sigma)|/sigma converges to a
     finite value instead of diverging.
 (3) Baseline sanity: the true xi (no substitution) reproduces the
     divergent trend of 110_02, so (1)-(2) are read against a correctly
     behaving control, not a vacuous setup.

Standalone: `python3 110_03_is_this_rh_in_disguise.py`
"""
import sys
import mpmath as mp

mp.mp.dps = 50
PASS = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    PASS.append(bool(cond))
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))


def logxi_general(sigma, gamma_log_fn, zeta_log_fn):
    sigma = mp.mpf(sigma)
    return (mp.log(mp.mpf('0.5')) + mp.log(sigma) + mp.log(sigma - 1)
             - (sigma / 2) * mp.log(mp.pi) + gamma_log_fn(sigma) + zeta_log_fn(sigma))


true_gamma_log = lambda sigma: mp.loggamma(sigma / 2)
true_zeta_log = lambda sigma: mp.log(mp.zeta(sigma))

# a bounded, zero-free dummy standing in for zeta -- deliberately unlike zeta
dummy_zeta_log = lambda sigma: mp.sin(sigma)  # e^{sin(sigma)} has log = sin(sigma), bounded
# a bounded dummy standing in for Gamma(sigma/2) -- deliberately unlike Gamma's growth
dummy_gamma_log = lambda sigma: mp.sin(sigma)

C_pred = (mp.log(2) + 1 + mp.log(mp.pi)) / 2
sigmas = [mp.mpf(v) for v in [10000, 100000, 1000000]]

# ---------------------------------------------------------------------
print("=== Check 0 (baseline): true xi reproduces the divergent trend of 110_02 ===")
true_ratios = [logxi_general(s, true_gamma_log, true_zeta_log) / (s * mp.log(s)) for s in sigmas]
predicted_ratios = [mp.mpf('0.5') - C_pred / mp.log(s) for s in sigmas]
baseline_errs = [abs(true_ratios[i] - predicted_ratios[i]) for i in range(len(sigmas))]
baseline_matches = (all(baseline_errs[i + 1] < baseline_errs[i] for i in range(len(baseline_errs) - 1))
                      and baseline_errs[-1] < mp.mpf('1e-4'))
check("baseline: true xi's growth ratio matches predicted 1/2 - C/log(sigma) (sanity, not vacuous)",
      baseline_matches, f"true ratios = {[float(r) for r in true_ratios]}")

# ---------------------------------------------------------------------
print("\n=== Check 1: Proposition 110.3.1 -- swap zeta for a bounded zero-free dummy ===")
dummy_zeta_ratios = [logxi_general(s, true_gamma_log, dummy_zeta_log) / (s * mp.log(s)) for s in sigmas]
rel_diffs = [abs(dummy_zeta_ratios[i] - true_ratios[i]) for i in range(len(sigmas))]
# the difference should SHRINK under refinement (both converge to the same
# 1/2 asymptote, since the zeta-substitution only affects an O(1) term,
# negligible against sigma*log(sigma))
diffs_shrink = all(rel_diffs[i + 1] < rel_diffs[i] for i in range(len(rel_diffs) - 1))
diffs_small = rel_diffs[-1] < mp.mpf('1e-4')
check("swapping zeta for a bounded zero-free dummy leaves the growth ratio numerically unchanged, gap shrinking under refinement",
      diffs_shrink and diffs_small, f"|dummy-true| = {[float(d) for d in rel_diffs]}")

dummy_matches_prediction = abs(dummy_zeta_ratios[-1] - predicted_ratios[-1]) < mp.mpf('1e-4')
check("dummy-zeta growth ratio ALSO matches the predicted 1/2 - C/log(sigma) asymptotic (same law as true xi)",
      dummy_matches_prediction,
      f"predicted={float(predicted_ratios[-1]):.6f}, true->{float(true_ratios[-1]):.6f}, dummy->{float(dummy_zeta_ratios[-1]):.6f}")

# ---------------------------------------------------------------------
print("\n=== Check 2: Proposition 110.3.2 -- swap Gamma(sigma/2) for a bounded dummy ===")
no_gamma_ratios_over_sigma = [logxi_general(s, dummy_gamma_log, true_zeta_log) / s for s in sigmas]
# with Gamma's growth removed, log|xi**|/sigma should CONVERGE (bounded),
# not diverge like the true xi's log|xi|/sigma does.
bounded = max(abs(r) for r in no_gamma_ratios_over_sigma) < mp.mpf('2')
consecutive_diffs = [abs(no_gamma_ratios_over_sigma[i + 1] - no_gamma_ratios_over_sigma[i])
                      for i in range(len(no_gamma_ratios_over_sigma) - 1)]
converging = all(consecutive_diffs[i + 1] <= consecutive_diffs[i] + mp.mpf('1e-6')
                  for i in range(len(consecutive_diffs) - 1)) if len(consecutive_diffs) > 1 else True
converging = converging and consecutive_diffs[-1] < mp.mpf('1e-3')
check("removing Gamma's growth makes log|xi**(sigma)|/sigma BOUNDED and converging (not diverging)",
      bounded and converging,
      f"values = {[float(r) for r in no_gamma_ratios_over_sigma]}, consecutive diffs = {[float(d) for d in consecutive_diffs]}")

# control: contrast with the TRUE xi's log|xi|/sigma, which strictly diverges
# over the same sigma range (must NOT be bounded/converging by the same test)
true_ratios_over_sigma = [logxi_general(s, true_gamma_log, true_zeta_log) / s for s in sigmas]
true_diverges = all(true_ratios_over_sigma[i + 1] > true_ratios_over_sigma[i] + mp.mpf('1')
                      for i in range(len(true_ratios_over_sigma) - 1))
check("control: the TRUE xi's log|xi(sigma)|/sigma keeps growing over the same range (contrast confirmed)",
      true_diverges, f"true log|xi|/sigma = {[float(r) for r in true_ratios_over_sigma]}")

# ---------------------------------------------------------------------
print("\n" + "=" * 60)
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
else:
    print("VERDICT: FAILURES PRESENT")
    sys.exit(1)
