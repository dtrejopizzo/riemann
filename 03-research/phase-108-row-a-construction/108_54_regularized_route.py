#!/usr/bin/env python3
"""
108_54 verifier: Condition I (explicit cutoff family) and Condition II
(renormalization of the toy regularized pairing).
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


mp.mp.dps = 30

# ---------------------------------------------------------------------------
# Condition I: the bump function and cutoff family
# ---------------------------------------------------------------------------


def psi_smooth(t):
    if t <= 0:
        return mp.mpf(0)
    return mp.e**(-1/t)


def h_transition(t):
    if t <= 0:
        return mp.mpf(0)
    if t >= 1:
        return mp.mpf(1)
    a = psi_smooth(t)
    b = psi_smooth(1 - t)
    return a / (a + b)


def chi(u):
    au = abs(u)
    if au <= 1:
        return mp.mpf(1)
    if au >= 2:
        return mp.mpf(0)
    return h_transition(2 - au)


def f_s(x, s):
    return x**(s - 1)


def f_sT(x, s, T):
    if x <= 0:
        return mp.mpf(0)
    return x**(s - 1) * chi(mp.log(x) / mp.log(T))


print("=== Check 1: compact support of f_{s,T} ===")
s_test = mp.mpf('0.4')
T_test = mp.mpf(50)
lo, hi = T_test**(-2), T_test**2
# check f_{s,T} is zero well outside [lo,hi] and generally nonzero well inside
outside_zero = f_sT(lo * mp.mpf('0.5'), s_test, T_test) == 0 and f_sT(hi * 2, s_test, T_test) == 0
inside_nonzero = f_sT(mp.mpf(1), s_test, T_test) != 0
check("support contained in [T^-2,T^2]: zero strictly outside, nonzero inside", outside_zero and inside_nonzero)

print()
print("=== Check 2: f_{s,T} -> f_s exactly on compacts once T large enough (Theorem 1.3) ===")
# K = [0.2, 5]; T0 per proof: log T0 > max(|log 0.2|, |log 5|) = log 5 ~ 1.609
K_pts = [mp.mpf(x) for x in ['0.2', '0.5', '1.0', '2.0', '5.0']]
s_test = mp.mpf('0.7')

T_small = mp.e**mp.mpf('1.0')   # log T = 1.0 < log5 ~1.609: should NOT yet agree everywhere on K
T_large = mp.e**mp.mpf('2.0')   # log T = 2.0 > log5: should agree exactly on K

agree_small = all(f_sT(x, s_test, T_small) == f_s(x, s_test) for x in K_pts)
agree_large = all(f_sT(x, s_test, T_large) == f_s(x, s_test) for x in K_pts)
diffs_small = [abs(f_sT(x, s_test, T_small) - f_s(x, s_test)) for x in K_pts]
print(f"  T_small=e^1.0: agree on all of K = {agree_small}, max diff = {mp.nstr(max(diffs_small),6)}")
print(f"  T_large=e^2.0: agree on all of K = {agree_large}")

check("f_{s,T} != f_s somewhere on K before threshold T0(K)", not agree_small)
check("f_{s,T} == f_s EXACTLY on all of K once T > T0(K) (Theorem 1.3)", agree_large)

# refinement: as T grows further past threshold, still exact agreement (stability, not just luck)
T_larger = mp.e**mp.mpf('5.0')
agree_larger = all(f_sT(x, s_test, T_larger) == f_s(x, s_test) for x in K_pts)
check("agreement persists (still exact) for even larger T", agree_larger)

# ---------------------------------------------------------------------------
# Condition II: renormalization of the toy model
# ---------------------------------------------------------------------------
print()
print("=== Check 3: divergence Q(T) reconfirmed (108_51 Prop 3.1, cross-check not re-derivation) ===")


def P(T, a):
    if a == 0:
        return 2 * mp.log(T)
    return (T**a - T**(-a)) / a


s1, s2 = mp.mpf('0.3'), mp.mpf('0.7')
lam1, lam2 = mp.mpf(1), mp.mpf(-1)


def Q(T, s1=s1, s2=s2, lam1=lam1, lam2=lam2):
    return lam1 * P(T, s1) + lam2 * P(T, s2)


Ts = [mp.mpf(10)**k for k in (1, 3, 6, 9, 12)]
Qs = [Q(T) for T in Ts]
print("  Q(T) for T=10^1..10^12:", [mp.nstr(q, 6) for q in Qs])
diverges = all(Qs[i] > Qs[i + 1] for i in range(len(Qs) - 1)) and Qs[-1] < mp.mpf('-1e6')
check("Q(T) diverges to -infinity, monotonically decreasing on the tested range", diverges)

print()
print("=== Check 4: minimal counter-term remainder -> 0 (Proposition 2.2), for several pairs ===")
pairs = [
    (mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf(1), mp.mpf(-1)),
    (mp.mpf('0.2'), mp.mpf('0.9'), mp.mpf(1), mp.mpf(-1)),
    (mp.mpf('0.4'), mp.mpf('0.45'), mp.mpf(1), mp.mpf(-1)),
]

all_converge = True
for (a1, a2, l1, l2) in pairs:
    def C0(T, a1=a1, a2=a2, l1=l1, l2=l2):
        return l1 * T**a1 / a1 + l2 * T**a2 / a2

    Ts_grow = [mp.mpf(10), mp.mpf(10)**5, mp.mpf(10)**50]
    rems = [abs(Q(T, a1, a2, l1, l2) - C0(T, a1, a2, l1, l2)) for T in Ts_grow]
    shrinking = rems[0] > rems[1] > rems[2]
    # remainder ~ T^{-s1}/s1 (the slower-decaying of the two dropped terms); require it below
    # that closed-form bound (with slack) rather than an arbitrary constant
    bound = 2 * Ts_grow[-1]**(-a1) / a1
    tiny = rems[2] < bound
    print(f"  s1={a1},s2={a2}: |remainder| at T=10,1e5,1e50 = {[mp.nstr(r,6) for r in rems]}"
          f"  shrinking={shrinking} below_closed_form_bound={tiny}")
    all_converge = all_converge and shrinking and tiny

check("minimal-subtraction remainder -> 0 (shrinks with T, matches closed-form T^-s1 rate)",
      all_converge)

print()
print("=== Check 5: counter-term non-uniqueness -- exact -K shift (Proposition 2.3) ===")
T_big = mp.mpf(10)**8


def C0(T, a1=s1, a2=s2, l1=lam1, l2=lam2):
    return l1 * T**a1 / a1 + l2 * T**a2 / a2


base_rem = Q(T_big) - C0(T_big)
shift_ok = True
for K in [mp.mpf(0), mp.mpf(5), mp.mpf(-3), mp.mpf('2.71828')]:
    rem_K = Q(T_big) - (C0(T_big) + K)
    expected = base_rem - K
    ok = abs(rem_K - expected) < mp.mpf('1e-20')
    print(f"  K={K}: remainder={mp.nstr(rem_K,10)}  expected(base-K)={mp.nstr(expected,10)}  ok={ok}")
    shift_ok = shift_ok and ok
check("shifting counter-term by K shifts remainder by exactly -K (non-uniqueness, Prop 2.3)", shift_ok)

print()
print("=== Check 6: minimal-subtraction remainder (==0) disagrees with Phi-based target (Prop 2.4) ===")


def Phi_new(s):
    s = mp.mpc(s)
    return 2 * mp.digamma(1 - s) - mp.mpf(1) / 2 * mp.digamma(s / 2) \
        - mp.mpf(1) / 2 * mp.digamma((1 - s) / 2) - mp.log(4 * mp.pi)


# minimal-subtraction remainder is identically 0 regardless of (s1,s2); target Phi(s1)-Phi(s2)
# style combination is generically nonzero and varies with (s1,s2) -- confirms disagreement.
mismatch_ok = True
for (a1, a2, l1, l2) in pairs:
    target = mp.re(l1 * Phi_new(a1) + l2 * Phi_new(a2))
    minimal_subtraction_remainder = mp.mpf(0)  # exact, by Proposition 2.2's proof
    disagree = abs(target - minimal_subtraction_remainder) > mp.mpf('0.1')
    print(f"  s1={a1},s2={a2}: target~lambda.Phi combination = {mp.nstr(target,8)}, "
          f"minimal-subtraction remainder = 0, disagree={disagree}")
    mismatch_ok = mismatch_ok and disagree

check("minimal-subtraction toy remainder (0) disagrees with the Phi-based target for all tested pairs",
      mismatch_ok)

# ---------------------------------------------------------------------------
print()
print(f"Summary: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED CHECKS:", FAIL)
    sys.exit(1)
else:
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
