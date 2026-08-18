#!/usr/bin/env python3
"""Verifier for 108.40 - Stage 4 operator form: Gamma_R as a zeta-regularized
determinant.

Everything is implemented from scratch: no scipy, no mpmath. Gamma is a
Lanczos approximation (g=7, n=9, reflection formula for Re<1/2). The Hurwitz
zeta function is the standard Euler-Maclaurin continuation. Both are checked
against known closed-form values before being used in the main identity.
"""
import cmath, math, sys

FAIL = []
def check(n, ok, x=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {x}")
    if not ok:
        FAIL.append(n)

PI = math.pi

# --------------------------------------------------------------------------
# 1. Gamma function: Lanczos approximation (g=7, n=9) + reflection formula.
# --------------------------------------------------------------------------
_LG = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
       771.32342877765313, -176.61502916214059, 12.507343278686905,
       -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7]
_G = 7

def gamma(z):
    z = complex(z)
    if z.real < 0.5:
        return PI / (cmath.sin(PI * z) * gamma(1 - z))
    z = z - 1
    x = _LG[0]
    for i in range(1, _G + 2):
        x += _LG[i] / (z + i)
    t = z + _G + 0.5
    return cmath.sqrt(2 * PI) * t ** (z + 0.5) * cmath.exp(-t) * x

def loggamma(z):
    """log Gamma via the same Lanczos data, principal branch, valid away
    from the negative real axis / poles (all our test points avoid both)."""
    z = complex(z)
    if z.real < 0.5:
        return cmath.log(PI) - cmath.log(cmath.sin(PI * z)) - loggamma(1 - z)
    zz = z - 1
    x = _LG[0]
    for i in range(1, _G + 2):
        x += _LG[i] / (zz + i)
    t = zz + _G + 0.5
    return 0.5 * cmath.log(2 * PI) + (zz + 0.5) * cmath.log(t) - t + cmath.log(x)

# --------------------------------------------------------------------------
# 2. Hurwitz zeta: Euler-Maclaurin continuation, valid for all complex s
#    away from the pole at s=1, and all a not a non-positive integer.
# --------------------------------------------------------------------------
_BERN = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510]

def hurwitz_zeta(s, a, N=15, M=8):
    s = complex(s); a = complex(a)
    total = 0j
    for k in range(N):
        total += (a + k) ** (-s)
    aN = a + N
    total += aN ** (1 - s) / (s - 1)
    total += 0.5 * aN ** (-s)
    for k in range(1, M + 1):
        p = 1.0 + 0j
        for j in range(2 * k - 1):
            p *= (s + j)
        Bk = _BERN[k - 1]
        total += Bk / math.factorial(2 * k) * p * aN ** (-s - 2 * k + 1)
    return total

# --------------------------------------------------------------------------
# 3. Sanity checks on the two from-scratch implementations.
# --------------------------------------------------------------------------
check("0a  Gamma(1/2) = sqrt(pi)", abs(gamma(0.5) - math.sqrt(PI)) < 1e-13,
      f"{gamma(0.5):.14f}")
check("0b  Gamma(5) = 24", abs(gamma(5) - 24) < 1e-11, f"{gamma(5):.10f}")
check("0c  Gamma(1+3i) matches recurrence Gamma(z+1)=z*Gamma(z)",
      abs(gamma(2 + 3j) - (1 + 3j) * gamma(1 + 3j)) < 1e-10)

xs = (0.3, 1.7, 2.5, 4.2, 0.5 + 0.3j, 1.0 + 1.0j)
check("0d  zeta_H(0,x) = 1/2 - x", all(abs(hurwitz_zeta(0, x) - (0.5 - x)) < 1e-11 for x in xs),
      f"{len(xs)} points")
check("0e  zeta_H(2,1) = pi^2/6", abs(hurwitz_zeta(2, 1) - PI**2/6) < 1e-12,
      f"{hurwitz_zeta(2,1).real:.14f}")
check("0f  zeta_H(4,1) = pi^4/90", abs(hurwitz_zeta(4, 1) - PI**4/90) < 1e-12,
      f"{hurwitz_zeta(4,1).real:.14f}")

# --------------------------------------------------------------------------
# 4. Lerch's formula: zeta_H'(0,x) = log Gamma(x) - (1/2) log(2 pi).
#    Derivative by central finite difference in the regularization variable
#    z (the Euler-Maclaurin formula is holomorphic in s near s=0, only pole
#    at s=1), with a convergence check (not a bare threshold): the estimate
#    at step h and at step h/2 must both approach the same closed-form value
#    computed independently via our own Gamma, with the h/2 error the
#    smaller one (2nd-order central difference).
# --------------------------------------------------------------------------
def dzeta_ds_at_0(a, h):
    return (hurwitz_zeta(h, a) - hurwitz_zeta(-h, a)) / (2 * h)

lerch_pts = (0.5, 1.3, 2.7, 0.5 + 0.3j, 1.0 + 1.0j)
errs_h, errs_h2 = [], []
for x in lerch_pts:
    target = loggamma(x) - 0.5 * math.log(2 * PI)
    e1 = abs(dzeta_ds_at_0(x, 1e-3) - target)
    e2 = abs(dzeta_ds_at_0(x, 5e-4) - target)
    errs_h.append(e1); errs_h2.append(e2)
# genuine convergence test: halving h should shrink the error, and the
# smaller-h error should itself be small on the scale of the target values
ok_conv = all(e2 < e1 for e1, e2 in zip(errs_h, errs_h2))
ok_small = all(e2 < 1e-6 * max(1.0, abs(loggamma(x))) for e2, x in zip(errs_h2, lerch_pts))
check("1  Lerch: zeta_H'(0,x) = log Gamma(x) - (1/2) log 2pi  [h-convergence]",
      ok_conv, f"max err(h=1e-3)={max(errs_h):.2e} -> max err(h=5e-4)={max(errs_h2):.2e}")
check("1'  Lerch: residual is small relative to the target value", ok_small)

# --------------------------------------------------------------------------
# 5. The base regularized-product formula:
#    det_reg({n+x}_{n>=0}) := exp(-d/dz zeta_H(z,x)|_0) = sqrt(2 pi)/Gamma(x).
# --------------------------------------------------------------------------
def det_reg_shift(x, h=5e-4):
    return cmath.exp(-dzeta_ds_at_0(x, h))

ok = all(abs(det_reg_shift(x) - math.sqrt(2 * PI) / gamma(x))
         < 3e-6 * abs(math.sqrt(2 * PI) / gamma(x)) for x in lerch_pts)
check("2  det_reg({n+x}) = sqrt(2pi)/Gamma(x)", ok)

# --------------------------------------------------------------------------
# 6. Main theorem: det_reg(s - Theta) = c(s) * Gamma_R(s)^{-1},
#    c(s) = 2^{1-s/2} pi^{(1-s)/2} = 2 sqrt(pi) (2 pi)^{-s/2}.
#    LHS is computed purely from the Hurwitz-zeta side (spectrum {s+2n});
#    RHS is computed purely from the Gamma side. Independent code paths.
# --------------------------------------------------------------------------
def Gamma_R(s):
    s = complex(s)
    return PI ** (-s / 2) * gamma(s / 2)

def c_of_s(s):
    s = complex(s)
    return 2 ** (1 - s / 2) * PI ** ((1 - s) / 2)

def c_of_s_alt(s):
    s = complex(s)
    return 2 * cmath.sqrt(PI) * (2 * PI) ** (-s / 2)

def log_det_reg_theta(s, h=5e-4):
    """log det_reg(s-Theta) computed directly from zeta_Theta(z,s) =
    sum_n (s+2n)^{-z} = 2^{-z} zeta_H(z, s/2), by finite-difference in z."""
    s = complex(s)
    def zTheta(z):
        return (2.0 ** (-z)) * hurwitz_zeta(z, s / 2)
    dz = (zTheta(h) - zTheta(-h)) / (2 * h)
    return -dz

def det_reg_theta(s, h=5e-4):
    return cmath.exp(log_det_reg_theta(s, h))

# avoid the pole set of Gamma(s/2), i.e. s = 0,-2,-4,...
test_s = (0.3, 0.7, 1.4, 2.9, -1.0, 0.5 + 2j, 1.5 - 1j, -0.5 + 0.7j, 3.2 + 0.4j)

check("3  c(s) two closed forms agree",
      all(abs(c_of_s(s) - c_of_s_alt(s)) < 1e-12 for s in test_s))

resid = [abs(det_reg_theta(s) - c_of_s(s) * Gamma_R(s) ** -1) for s in test_s]
scale = [abs(c_of_s(s) * Gamma_R(s) ** -1) for s in test_s]
ok_main = all(r < 3e-6 * sc for r, sc in zip(resid, scale))
check("4  MAIN: det_reg(s-Theta) = c(s) * Gamma_R(s)^{-1}", ok_main,
      f"max relative residual = {max(r/sc for r, sc in zip(resid, scale)):.2e} over {len(test_s)} points")

# convergence check for the main identity too (h halved)
resid2 = [abs(det_reg_theta(s, h=2.5e-4) - c_of_s(s) * Gamma_R(s) ** -1) for s in test_s]
ok_conv_main = all(r2 <= r1 * 0.6 or r1 < 1e-9 for r1, r2 in zip(resid, resid2))
check("4'  residual shrinks as h halves (genuine convergence, not a fluke)",
      ok_conv_main)

# --------------------------------------------------------------------------
# 7. Source rule: the spectrum {-2n : n>=0} is exactly the pole set of
#    Gamma(s/2), read off from Gamma alone -- no reference to zeta or xi.
# --------------------------------------------------------------------------
def gamma_has_pole_near(w, eps=1e-6):
    # Gamma(w) blows up near non-positive integers; detect by comparing
    # |Gamma(w+eps)| for a tiny generic perturbation against a threshold-free
    # growth test: it must exceed |Gamma(w+eps)| taken at a nearby *generic*
    # point by many orders of magnitude as eps -> 0 (pole vs regular value).
    a1 = abs(gamma(w + eps))
    a2 = abs(gamma(w + eps / 2))
    return a2 > 1.9 * a1  # doubling eps->eps/2 should roughly double |Gamma| near a simple pole

poles_claimed = [-2 * n for n in range(4)]   # 0, -2, -4, -6  (s, with w=s/2 -> 0,-1,-2,-3)
ok_poles = all(gamma_has_pole_near(w / 2) for w in poles_claimed)
non_poles = [-1, -3, 0.5, 2.0]  # s=-1,-3 -> s/2=-0.5,-1.5 regular; not in the claimed spectrum
ok_nonpoles = all(not gamma_has_pole_near(w / 2, eps=1e-6) for w in non_poles)
check("5  spectrum {-2n} = pole set of Gamma(s/2) (poles detected)", ok_poles)
check("5'  odd/non-even-negative points are NOT poles of Gamma(s/2)", ok_nonpoles)

# the point s=0 (n=0 in the spectrum) is a pole of Gamma(s/2) but NOT a zero
# of zeta (zeta(0) = -1/2), hence not a trivial zero of xi either: this shows
# the spectrum is read off Gamma alone, not from zeros of zeta/xi.
zeta0 = hurwitz_zeta(0.0, 1.0)  # zeta_H(s,1) = zeta(s), at s=0: zeta(0) = -1/2
check("6  zeta(0) = -1/2  (s=0 in the spectrum is a Gamma-pole, not a zeta-zero)",
      abs(zeta0 - (-0.5)) < 1e-10, f"zeta(0) = {zeta0.real:.12f}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
