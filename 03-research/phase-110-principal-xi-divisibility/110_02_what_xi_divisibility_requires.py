#!/usr/bin/env python3
"""
Phase 110, Task 2 verifier.

Checks, numerically:
 (1) Lemma 110.2.1: |ghat(sigma)| <= C e^{A|sigma|} for a compactly
     supported bump on [1,2], with A matching the predicted support-based
     bound.
 (2) Theorem 110.2.2: log|xi(sigma)| ~ (sigma/2) log(sigma) - C*sigma with
     C = (log2+1+log(pi))/2, verified across five decades of sigma, with a
     control that REJECTS a wrong constant.
 (3) Example 110.2.6: closed form ghat(w) = sqrt(pi) e^{w^2/4} for
     g~(x)=e^{-x^2}, verified by refinement of a truncated quadrature; and
     the superexponential decay of f^(w)=xi(w) ghat(w) on the vertical line
     Re(w)=1/2.
 (4) Fact 110.2.A: the exponential decay rate of a smooth bump's transform,
     as sigma -> +infinity, matches the (negative of the) left endpoint of
     its support, refined across increasing sigma, with a control that
     rejects a wrong endpoint.
 (5) Theorem 110.2.4's numerical core: f^=xi*ghat for a compactly supported
     g retains xi's infinite-type growth (does NOT become finite type) --
     i.e. log|f^(sigma)|/sigma is unbounded (grows), just as for xi alone,
     confirming compact support cannot be recovered.

Standalone: `python3 110_02_what_xi_divisibility_requires.py`
"""
import sys
import mpmath as mp

mp.mp.dps = 50
PASS = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    PASS.append(bool(cond))
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))


def xi(s):
    s = mp.mpc(s)
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


# ---------------------------------------------------------------------
# (1) Lemma 110.2.1: finite exponential type bound for compactly supported g.
# ---------------------------------------------------------------------
print("=== Check 1: Lemma 110.2.1 -- finite exponential type bound ===")

alpha, beta = mp.mpf(1), mp.mpf(2)


def bump(x):
    if x <= alpha or x >= beta:
        return mp.mpf(0)
    return mp.e ** (-1 / ((x - alpha) * (beta - x)))


def ghat_bump(w):
    f = lambda x: bump(x) * mp.e ** (-w * x)
    return mp.quad(f, [alpha, alpha + (beta - alpha) * mp.mpf('0.25'),
                        (alpha + beta) / 2,
                        beta - (beta - alpha) * mp.mpf('0.25'), beta])


A_bound = max(abs(alpha), abs(beta))
l1_norm = mp.quad(bump, [alpha, (alpha + beta) / 2, beta])
sigmas_test = [mp.mpf(v) for v in [5, 20, 60, -5, -20, -60]]
bound_ok = True
for sig in sigmas_test:
    val = abs(ghat_bump(sig))
    predicted_upper = l1_norm * mp.e ** (A_bound * abs(sig))
    if val > predicted_upper * mp.mpf('1.0001'):  # allow tiny numerical slack
        bound_ok = False
check("|ghat(sigma)| <= ||g||_1 * e^{A|sigma|} for all tested sigma (A=max(|alpha|,|beta|)=2)",
      bound_ok, f"A={float(A_bound)}, tested sigma={[float(s) for s in sigmas_test]}")

# ---------------------------------------------------------------------
# (2) Theorem 110.2.2: growth constant of xi along the real axis.
# ---------------------------------------------------------------------
print("\n=== Check 2: Theorem 110.2.2 -- log|xi(sigma)| ~ (sigma/2)log(sigma) - C*sigma ===")


def logxi(sigma):
    sigma = mp.mpf(sigma)
    return (mp.log(mp.mpf('0.5')) + mp.log(sigma) + mp.log(sigma - 1)
             - (sigma / 2) * mp.log(mp.pi) + mp.loggamma(sigma / 2) + mp.log(mp.zeta(sigma)))


C_pred = (mp.log(2) + 1 + mp.log(mp.pi)) / 2
sigmas = [mp.mpf(v) for v in [100, 1000, 10000, 100000, 1000000]]
errs = []
for sig in sigmas:
    lx = logxi(sig)
    ratio = lx / (sig * mp.log(sig))
    pred = mp.mpf('0.5') - C_pred / mp.log(sig)
    errs.append(abs(ratio - pred))

errs_shrinking = all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
final_small = errs[-1] < mp.mpf('1e-5')
check("log|xi(sigma)|/(sigma log sigma) matches 1/2 - C/log(sigma) with C=(log2+1+logpi)/2, error shrinking under refinement",
      errs_shrinking and final_small, f"errors = {[float(e) for e in errs]}")

# control: reject a wrong constant C'=1 (instead of C~1.4189...)
C_wrong = mp.mpf('1.0')
errs_wrong = []
for sig in sigmas:
    lx = logxi(sig)
    ratio = lx / (sig * mp.log(sig))
    pred_wrong = mp.mpf('0.5') - C_wrong / mp.log(sig)
    errs_wrong.append(abs(ratio - pred_wrong))
wrong_rejected = errs_wrong[-1] > mp.mpf('0.01')  # does not converge to 0 like the correct one did
check("control: wrong constant C=1 is REJECTED (residual does not vanish)",
      wrong_rejected, f"final residual with wrong C = {float(errs_wrong[-1]):.6f}")

# unboundedness of log|xi(sigma)|/sigma (infinite type)
ratios_over_sigma = [logxi(sig) / sig for sig in sigmas]
unbounded = all(ratios_over_sigma[i + 1] > ratios_over_sigma[i] for i in range(len(ratios_over_sigma) - 1))
check("log|xi(sigma)|/sigma strictly increasing across 5 decades (infinite type, no leveling off)",
      unbounded, f"values = {[float(r) for r in ratios_over_sigma]}")

# ---------------------------------------------------------------------
# (3) Example 110.2.6: closed form and vertical decay.
# ---------------------------------------------------------------------
print("\n=== Check 3: Example 110.2.6 -- ghat(w)=sqrt(pi) e^{w^2/4}, vertical decay of f^ ===")


def ghat_gauss_direct(w, X):
    f = lambda x: mp.e ** (-x ** 2) * mp.e ** (-w * x)
    return mp.quad(f, [-X, 0, X])


def ghat_gauss_closed(w):
    return mp.sqrt(mp.pi) * mp.e ** (w ** 2 / 4)


test_ws = [mp.mpc('0.3', '0'), mp.mpc('0.5', '2.1'), mp.mpc('-1.2', '5.0')]
rel_errs_gauss = []
for w in test_ws:
    Xs = [mp.mpf(v) for v in [8, 12, 18]]
    vals = [ghat_gauss_direct(w, X) for X in Xs]
    closed = ghat_gauss_closed(w)
    rel_errs_here = [abs(v - closed) / abs(closed) for v in vals]
    rel_errs_gauss.append(rel_errs_here)

gauss_converges = all(re[0] >= re[1] >= re[2] and re[2] < mp.mpf('1e-25') for re in rel_errs_gauss)
check("truncated quadrature converges to closed form sqrt(pi) e^{w^2/4} under refinement",
      gauss_converges, f"final rel errs = {[float(re[-1]) for re in rel_errs_gauss]}")

sigma_line = mp.mpf('0.5')
taus = [mp.mpf(v) for v in [0, 5, 10, 20, 40, 80]]
fhat_vals = []
for tau in taus:
    w = mp.mpc(sigma_line, tau)
    fhat_vals.append(abs(xi(w) * ghat_gauss_closed(w)))

decay_monotone = all(fhat_vals[i + 1] < fhat_vals[i] for i in range(len(fhat_vals) - 1))
superexp_small = fhat_vals[-1] < mp.mpf('1e-100')
check("|f^(1/2+i*tau)| decays superexponentially as tau grows (Weil-sum-ready)",
      decay_monotone and superexp_small, f"values at tau={[float(t) for t in taus]}: "
      f"{[float(v) if v > 1e-300 else 0.0 for v in fhat_vals]} (last ~ 1e-719 in true precision)")

# ---------------------------------------------------------------------
# (4) Fact 110.2.A: exponential rate matches support endpoint, with control.
# ---------------------------------------------------------------------
print("\n=== Check 4: Fact 110.2.A -- exponential rate of ghat matches -alpha, refined ===")

sigmas_rate = [mp.mpf(v) for v in [10, 40, 160, 640]]
log_over_sigma = [mp.log(abs(ghat_bump(sig))) / sig for sig in sigmas_rate]
target = -alpha
errs_rate = [abs(v - target) for v in log_over_sigma]
rate_refines = all(errs_rate[i + 1] < errs_rate[i] for i in range(len(errs_rate) - 1))
rate_close = errs_rate[-1] < mp.mpf('0.2')
check("log|ghat(sigma)|/sigma -> -alpha (=-1) under refinement, error shrinking",
      rate_refines and rate_close, f"errors = {[float(e) for e in errs_rate]}")

# control: reject a wrong endpoint (e.g. -beta = -2, or 0)
wrong_target = -beta
errs_wrong_rate = [abs(v - wrong_target) for v in log_over_sigma]
wrong_rate_rejected = errs_wrong_rate[-1] > mp.mpf('0.5')
check("control: wrong endpoint -beta=-2 is REJECTED (residual stays large)",
      wrong_rate_rejected, f"final residual vs wrong endpoint = {float(errs_wrong_rate[-1]):.4f}")

# ---------------------------------------------------------------------
# (5) Theorem 110.2.4's numerical core: f^ = xi*ghat_bump retains infinite type.
# ---------------------------------------------------------------------
print("\n=== Check 5: f^=xi*ghat_bump retains xi's infinite-type growth ===")

sigmas5 = [mp.mpf(v) for v in [10, 40, 160, 640]]
fhat_over_sigma = []
for sig in sigmas5:
    lf = logxi(sig) + mp.log(abs(ghat_bump(sig)))
    fhat_over_sigma.append(lf / sig)

grows_unbounded = all(fhat_over_sigma[i + 1] > fhat_over_sigma[i] for i in range(len(fhat_over_sigma) - 1))
# also compare directly to a genuinely finite-type reference (ghat_bump alone),
# confirming f^ grows strictly FASTER in this ratio, i.e. multiplying by xi
# does not tame it back down to finite type.
ghat_alone_over_sigma = [mp.log(abs(ghat_bump(sig))) / sig for sig in sigmas5]
gaps = [fhat_over_sigma[i] - ghat_alone_over_sigma[i] for i in range(len(sigmas5))]
# f^'s growth ratio must exceed ghat's alone at every scale (xi's extra growth
# is present throughout), and the gap must widen under refinement (xi's
# infinite-type contribution grows without bound, not a fixed finite offset)
f_exceeds_g_growth = (all(g > 0 for g in gaps)
                        and all(gaps[i + 1] > gaps[i] for i in range(len(gaps) - 1)))
check("log|f^(sigma)|/sigma is unbounded (increasing across refinement) -- f^ is NOT finite type",
      grows_unbounded, f"values = {[float(v) for v in fhat_over_sigma]}")
check("f^'s growth ratio strictly exceeds ghat's alone, by a WIDENING margin under refinement (xi's infinite type is not absorbed/cancelled)",
      f_exceeds_g_growth,
      f"gaps={[float(g) for g in gaps]}")

# ---------------------------------------------------------------------
print("\n" + "=" * 60)
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
else:
    print("VERDICT: FAILURES PRESENT")
    sys.exit(1)
