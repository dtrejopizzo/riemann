#!/usr/bin/env python3
"""Verifier for 111.02 -- the two directions.

Checks Theorem 2.1 (real-axis growth), Theorem 2.2 (critical-line decay to
-pi/4), Corollary 2.3 (they are compatible, opposite signs for the same xi),
Propositions 3.1 and 3.2.

Discipline: every rate is tested by REFINEMENT against its predicted limit,
and every check carries a control clause that would reject the opposite
conclusion, so no check can pass unconditionally.
"""
import sys

import mpmath as mp

mp.mp.dps = 30
PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print("[%s] %s  %s" % ("PASS" if ok else "FAIL", name, detail))


def xi(s):
    return (s * (s - 1) / 2) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


ghat = lambda w: mp.sqrt(mp.pi) * mp.e ** (w ** 2 / 4)
fhat = lambda w: xi(w) * ghat(w)

print("=" * 68)
print("Theorem 2.1 -- real axis: log|xi(sigma)|/sigma -> +infinity")
print("=" * 68)
sig = [mp.mpf(v) for v in (10, 100, 1000, 10000)]
rates_r = [mp.log(abs(xi(s))) / s for s in sig]
for s, r in zip(sig, rates_r):
    print("    sigma=%-8s  log|xi|/sigma = %s" % (mp.nstr(s, 6), mp.nstr(r, 8)))
check("Thm 2.1: the real-axis rate increases without bound (refinement)",
      all(rates_r[i] < rates_r[i + 1] for i in range(len(rates_r) - 1))
      and rates_r[-1] > 3,
      "rates = %s" % [mp.nstr(r, 5) for r in rates_r])
check("control: the real-axis rate is POSITIVE (growth, not decay)",
      all(r > 0 for r in rates_r))

print()
print("=" * 68)
print("Theorem 2.2 -- critical line: log|xi(1/2+it)|/t -> -pi/4")
print("=" * 68)
target = -mp.pi / 4
ts = [mp.mpf(v) for v in (10, 50, 200, 1000, 5000)]
rates_c = [mp.log(abs(xi(mp.mpc('0.5', t)))) / t for t in ts]
errs = [abs(r - target) for r in rates_c]
for t, r in zip(ts, rates_c):
    print("    t=%-8s  log|xi|/t = %s" % (mp.nstr(t, 6), mp.nstr(r, 8)))
check("Thm 2.2: the critical-line rate converges to -pi/4 (errors shrink)",
      all(errs[i] > errs[i + 1] for i in range(len(errs) - 1))
      and errs[-1] < mp.mpf('0.01'),
      "target=%s  errors=%s" % (mp.nstr(target, 8), [mp.nstr(e, 3) for e in errs]))
# control: the limit is -pi/4, NOT -pi/2 or 0 -- a discriminating clause
check("control: the rate is -pi/4, not -pi/2 and not 0",
      abs(rates_c[-1] - target) < mp.mpf('0.01')
      and abs(rates_c[-1] + mp.pi / 2) > mp.mpf('0.5')
      and abs(rates_c[-1]) > mp.mpf('0.5'),
      "rate at t=5000 = %s" % mp.nstr(rates_c[-1], 10))

print()
print("=" * 68)
print("Corollary 2.3 -- the SAME xi grows one way and decays the other")
print("=" * 68)
check("Cor 2.3: opposite signs, same function (no tension)",
      rates_r[-1] > 0 > rates_c[-1],
      "real-axis %s  vs  critical-line %s"
      % (mp.nstr(rates_r[-1], 6), mp.nstr(rates_c[-1], 6)))

print()
print("=" * 68)
print("zeta contributes nothing to either rate (the rates are Gamma's)")
print("=" * 68)
lz = [abs(mp.log(mp.zeta(s))) for s in sig]
check("log|zeta(sigma)| -> 0 on the real axis",
      lz[-1] < mp.mpf('1e-20') and lz[0] > lz[-1],
      "values = %s" % [mp.nstr(v, 3) for v in lz])
# On the critical line the claim proved in 2.2 is log|zeta| = O(log t), NOT
# that log|zeta|/t decreases monotonically -- |zeta(1/2+it)| fluctuates (it
# passes near zeros), so a monotonicity test would be testing something the
# proof never claims.  Test the actual claim: |log|zeta||/log t stays bounded,
# hence the CONTRIBUTION to the exponential rate, |log|zeta||/t, is o(1).
zc_log = [abs(mp.log(abs(mp.zeta(mp.mpc('0.5', t))))) / mp.log(t) for t in ts]
zc_rate = [abs(mp.log(abs(mp.zeta(mp.mpc('0.5', t))))) / t for t in ts]
check("log|zeta(1/2+it)| = O(log t) on the critical line",
      max(zc_log) < 1, "|log|zeta||/log t = %s" % [mp.nstr(v, 3) for v in zc_log])
check("hence zeta contributes o(1) to the exponential rate (so it is Gamma's)",
      max(zc_rate[2:]) < mp.mpf('1e-2'),
      "|log|zeta||/t = %s" % [mp.nstr(v, 3) for v in zc_rate])
# control: Gamma's own contribution does NOT go to zero -- it is the whole rate
g_rate = [abs(mp.log(abs(mp.gamma(mp.mpc('0.25', t / 2))))) / t for t in ts]
check("control: Gamma's contribution to the rate does NOT vanish (it is the rate)",
      min(g_rate) > mp.mpf('0.3'),
      "|log|Gamma(1/4+it/2)||/t = %s" % [mp.nstr(v, 4) for v in g_rate])

print()
print("=" * 68)
print("Prop 3.1 -- the xi-divisible probe decays superexponentially")
print("=" * 68)
probe = [(t, abs(fhat(mp.mpc('0.5', t)))) for t in (1, 10, 50, 200)]
for t, v in probe:
    print("    t=%-5d |fhat(1/2+it)| = %s" % (t, mp.nstr(v, 8)))
vals = [v for _, v in probe]
check("Prop 3.1: probe decays, and faster than exp(-t^2/4)",
      all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
      and vals[-1] < mp.e ** (-mp.mpf(200) ** 2 / 4),
      "value at t=200 = %s" % mp.nstr(vals[-1], 6))

print()
print("=" * 68)
print("Prop 3.2 -- xi(0)=xi(1)=1/2, so xi-divisibility alone is not membership")
print("=" * 68)
e = mp.mpf('1e-15')
x0, x1 = xi(e), xi(1 + e)
check("xi(0) = xi(1) = 1/2 (value test, not merely 'nonzero')",
      abs(x0 - mp.mpf('0.5')) < mp.mpf('1e-12')
      and abs(x1 - mp.mpf('0.5')) < mp.mpf('1e-12'),
      "xi(0)=%s  xi(1)=%s" % (mp.nstr(x0, 12), mp.nstr(x1, 12)))
f0, f1 = fhat(e), fhat(1 + e)
check("Prop 3.2: the probe's fhat(0), fhat(1) are NONZERO (extra condition needed)",
      abs(f0) > mp.mpf('0.1') and abs(f1) > mp.mpf('0.1'),
      "fhat(0)=%s  fhat(1)=%s" % (mp.nstr(f0, 8), mp.nstr(f1, 8)))

print()
print("Summary: %d passed, %d failed" % (len(PASS), len(FAIL)))
if FAIL:
    print("FAILED:", FAIL)
    print("VERDICT: FAILURES PRESENT")
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")
sys.exit(0)
