#!/usr/bin/env python3
"""
Phase 110 master verifier.

Re-runs the three task verifiers as subprocesses and confirms each exits 0
with its own ALL CHECKS PASS verdict, then performs two additional,
independent headline checks tying the whole phase together:
 (a) xi's growth constant C = (log2+1+log(pi))/2 (Theorem 110.2.2), computed
     fresh here (not by importing 110_02's code), matches to high precision.
 (b) the admissible/xi-divisible incompatibility (Theorem 110.2.4) widens,
     not saturates, under refinement of both the bump support and the
     sigma-range -- the structural signature of an unbounded (not merely
     "large") obstruction.

Standalone: `python3 110_99_verify_all.py`
"""
import subprocess
import sys
import os
import mpmath as mp

mp.mp.dps = 50
PASS = []
HERE = os.path.dirname(os.path.abspath(__file__))


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    PASS.append(bool(cond))
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))


def run_subverifier(fname):
    path = os.path.join(HERE, fname)
    result = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=600)
    ok = (result.returncode == 0) and ("VERDICT: ALL CHECKS PASS" in result.stdout)
    return ok, result.stdout, result.returncode


print("=== Re-running task verifiers as subprocesses ===")
for fname in ["110_01_the_graded_family_is_not_xi_divisible.py",
              "110_02_what_xi_divisibility_requires.py",
              "110_03_is_this_rh_in_disguise.py"]:
    ok, out, rc = run_subverifier(fname)
    check(f"{fname} exits 0 with VERDICT: ALL CHECKS PASS", ok, f"returncode={rc}")

# ---------------------------------------------------------------------
print("\n=== Headline check (a): xi's growth constant, computed fresh ===")


def logxi(sigma):
    sigma = mp.mpf(sigma)
    return (mp.log(mp.mpf('0.5')) + mp.log(sigma) + mp.log(sigma - 1)
             - (sigma / 2) * mp.log(mp.pi) + mp.loggamma(sigma / 2) + mp.log(mp.zeta(sigma)))


C_pred = (mp.log(2) + 1 + mp.log(mp.pi)) / 2
sigmas = [mp.mpf(v) for v in [1000, 10000, 100000, 1000000]]
errs = [abs(logxi(s) / (s * mp.log(s)) - (mp.mpf('0.5') - C_pred / mp.log(s))) for s in sigmas]
shrinking = all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
tiny = errs[-1] < mp.mpf('1e-5')
check("fresh computation: log|xi(sigma)|/(sigma log sigma) -> 1/2 - C/log(sigma), C=(log2+1+logpi)/2",
      shrinking and tiny, f"errors = {[float(e) for e in errs]}")

# control: a plausible wrong value of C (e.g. C=2) must be rejected -- its
# residual must NOT shrink towards 0 the way the correct C's does.
C_wrong = mp.mpf('2')
errs_wrong = [abs(logxi(s) / (s * mp.log(s)) - (mp.mpf('0.5') - C_wrong / mp.log(s))) for s in sigmas]
wrong_not_shrinking_to_zero = errs_wrong[-1] > mp.mpf('0.03') and errs_wrong[-1] > errs[-1] * 1000
check("control: wrong constant C=2 is rejected (its residual stays orders of magnitude above the correct C's)",
      wrong_not_shrinking_to_zero,
      f"final residual with C=2: {float(errs_wrong[-1]):.4f} vs correct-C residual: {float(errs[-1]):.2e}")

# ---------------------------------------------------------------------
print("\n=== Headline check (b): admissible/xi-divisible incompatibility widens under refinement ===")


def bump_on(a, b, x):
    if x <= a or x >= b:
        return mp.mpf(0)
    return mp.e ** (-1 / ((x - a) * (b - x)))


def ghat_bump_on(a, b, w):
    f = lambda x: bump_on(a, b, x) * mp.e ** (-w * x)
    mid = (a + b) / 2
    q1 = a + (b - a) * mp.mpf('0.25')
    q3 = b - (b - a) * mp.mpf('0.25')
    return mp.quad(f, [a, q1, mid, q3, b])


# For three genuinely different admissible supports (confirmed distinct by
# their own transform values, a sanity check against a degenerate/vacuous
# test), confirm f^=xi*ghat's OWN growth ratio log|f^(sigma)|/sigma is
# unbounded (widens under refinement) in every case -- Theorem 110.2.4's
# obstruction is not an artifact of one particular choice of g.
# (Algebraic note: since f^=xi*ghat exactly, log|f^|/sigma - log|ghat|/sigma
# = log|xi|/sigma identically for ANY admissible g -- so the *increment*
# contributed by xi is support-independent by construction; what is checked
# here instead is that the resulting absolute growth ratios of f^, which DO
# depend on the support through ghat's own O(sigma) contribution, are
# unbounded in every case, and that the three supports give numerically
# distinct ghat values, so this is not a vacuous re-test of one case.)
supports = [(mp.mpf('1'), mp.mpf('2')), (mp.mpf('0.5'), mp.mpf('3')), (mp.mpf('2'), mp.mpf('2.5'))]
sigmas_b = [mp.mpf(v) for v in [10, 80, 640]]

widening_confirmed_for_all_supports = True
detail_lines = []
ghat_values_at_10 = []
for (a, b) in supports:
    fhat_ratios = []
    for sig in sigmas_b:
        lf = logxi(sig) + mp.log(abs(ghat_bump_on(a, b, sig)))
        fhat_ratios.append(lf / sig)
    is_widening = all(fhat_ratios[i + 1] > fhat_ratios[i] for i in range(len(fhat_ratios) - 1))
    widening_confirmed_for_all_supports = widening_confirmed_for_all_supports and is_widening
    detail_lines.append(f"support=({float(a)},{float(b)}): f^ ratios={[float(g) for g in fhat_ratios]}")
    ghat_values_at_10.append(ghat_bump_on(a, b, sigmas_b[0]))

supports_are_distinct = all(
    abs(ghat_values_at_10[i] - ghat_values_at_10[j]) / max(abs(ghat_values_at_10[i]), abs(ghat_values_at_10[j])) > mp.mpf('0.1')
    for i in range(3) for j in range(i + 1, 3)
)
check("the three supports give numerically DISTINCT ghat values at sigma=10 (test is not vacuous)",
      supports_are_distinct, f"ghat(10) values: {[float(v) for v in ghat_values_at_10]}")
check("f^=xi*ghat's growth ratio log|f^(sigma)|/sigma is unbounded (widens under refinement) for all three supports",
      widening_confirmed_for_all_supports, "; ".join(detail_lines))

# ---------------------------------------------------------------------
print("\n" + "=" * 60)
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
else:
    print("VERDICT: FAILURES PRESENT")
    sys.exit(1)
