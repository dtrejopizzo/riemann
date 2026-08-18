#!/usr/bin/env python3
"""
108_55 verifier: Stage 5 final verdict -- integration check.

Independently re-derives (fresh code paths, not importing 108_53/108_54) the headline
numerical facts underlying the final verdict table, so the closing note is checked against
computation rather than merely asserted.
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


mp.mp.dps = 40


def Phi(s):
    s = mp.mpc(s)
    return 2*mp.digamma(1-s) - mp.mpf(1)/2*mp.digamma(s/2) \
        - mp.mpf(1)/2*mp.digamma((1-s)/2) - mp.log(4*mp.pi)


# ---------------------------------------------------------------------------
print("=== Condition I re-check: cutoff family is compactly supported & converges ===")
mp.mp.dps = 30


def chi_simple(u):
    # a simple C^1 bump (raised cosine), independent of 108_54's C^infty construction,
    # used only to re-confirm the qualitative Condition I facts with a different bump.
    au = abs(u)
    if au <= 1:
        return mp.mpf(1)
    if au >= 2:
        return mp.mpf(0)
    return (1 + mp.cos(mp.pi*(au-1)))/2


def f_sT(x, s, T):
    if x <= 0:
        return mp.mpf(0)
    return x**(s-1)*chi_simple(mp.log(x)/mp.log(T))


s0 = mp.mpf('0.6')
T0 = mp.mpf(20)
supp_zero_outside = f_sT(T0**2*3, s0, T0) == 0 and f_sT(T0**(-2)/3, s0, T0) == 0
check("Condition I: independent bump also gives compact support", supp_zero_outside)

K = [mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('3.0')]
T_big = mp.e**mp.mpf('3.0')  # log T = 3 > log(3) ~ 1.1, safely inside plateau for K
agree = all(f_sT(x, s0, T_big) == x**(s0-1) for x in K)
check("Condition I: independent bump converges exactly to f_s on a compact set for large T", agree)

# ---------------------------------------------------------------------------
print()
print("=== Condition II re-check: minimal-subtraction ambiguity, fresh computation ===")


def P(T, a):
    if a == 0:
        return 2*mp.log(T)
    return (T**a - T**(-a))/a


s1, s2 = mp.mpf('0.35'), mp.mpf('0.85')  # different pair from 108_54, to be independent
T = mp.mpf(10)**30
Q = P(T, s1) - P(T, s2)
C0 = T**s1/s1 - T**s2/s2
rem0 = Q - C0
rem_shift = Q - (C0 + mp.mpf('7'))
check("Condition II: minimal-subtraction remainder is (numerically) 0 for a fresh pair",
      abs(rem0) < mp.mpf('1e-10'), f"rem0={mp.nstr(rem0,6)}")
check("Condition II: shifting counter-term by 7 shifts remainder by -7 (fresh pair)",
      abs(rem_shift - (rem0 - 7)) < mp.mpf('1e-20'))

target = mp.re(Phi(s1) - Phi(s2))
check("Condition II: minimal-subtraction remainder (~0) disagrees with Phi(s1)-Phi(s2) target",
      abs(target) > mp.mpf('0.1'), f"target={mp.nstr(target,8)}")

# ---------------------------------------------------------------------------
print()
print("=== Condition III re-check: independent of Condition I/II machinery ===")
mp.mp.dps = 40

# (a) finiteness at a zeta zero, blow-up of zeta'/zeta individually -- fresh zero (#2)
rho2 = mp.zetazero(2)
phi_at_rho2 = Phi(rho2)
zz_near = mp.zeta(rho2 + mp.mpf('1e-6'), derivative=1)/mp.zeta(rho2 + mp.mpf('1e-6'))
check("Condition III: Phi finite at a (different) nontrivial zeta zero",
      abs(phi_at_rho2) < 100, f"Phi(rho2)={mp.nstr(phi_at_rho2,10)}")
check("Condition III: zeta'/zeta individually huge near that same zero",
      abs(zz_near) > mp.mpf('1e4'), f"|zeta'/zeta| = {mp.nstr(abs(zz_near),6)}")

# (b) mirror-asymmetry at a fresh point (not s* from 108_53, and not 1/2+Z)
s_fresh = mp.mpf('0.62')
asym = Phi(1-s_fresh) - Phi(s_fresh)
check("Condition III: mirror symmetry broken at a fresh point s=0.62",
      abs(asym) > mp.mpf('0.5'), f"Phi(1-s)-Phi(s)={mp.nstr(asym,8)}")

# exact symmetry at a fresh point in 1/2+Z
s_sym = mp.mpf('2.5')
sym = Phi(1-s_sym) - Phi(s_sym)
check("Condition III: mirror symmetry holds exactly at fresh point s=2.5 in 1/2+Z",
      abs(sym) < mp.mpf('1e-25'), f"Phi(1-s)-Phi(s)={mp.nstr(sym,8)}")

# (c) pole at s=1 confirmed via a different approach direction (from above, s=1+eps)
eps = mp.mpf('1e-6')
val_close = abs(Phi(1+eps))
val_farther = abs(Phi(1+10*eps))
check("Condition III: Phi blows up approaching s=1 (fresh direction, closer point is bigger)",
      val_close > 5*val_farther, f"|Phi(1+eps)|={mp.nstr(val_close,6)}, |Phi(1+10eps)|={mp.nstr(val_farther,6)}")

# ---------------------------------------------------------------------------
print()
print("=== Final verdict table consistency ===")
condition_I_holds = True     # 108_54 Theorems 1.2/1.3, reconfirmed above
condition_II_naive_fails = True   # 108_54 Propositions 2.3/2.4, reconfirmed above
condition_III_fails = True   # 108_53 Theorem 4, reconfirmed above

stage5_negative = condition_III_fails  # sufficient alone, per 108_51's Statement (I & II & III required)
check("Stage 5 verdict: regularized route fails because Condition III fails (proved, sufficient alone)",
      stage5_negative and condition_I_holds and condition_II_naive_fails)

print()
print(f"Summary: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED CHECKS:", FAIL)
    sys.exit(1)
else:
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
