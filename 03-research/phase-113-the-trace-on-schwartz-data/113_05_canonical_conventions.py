#!/usr/bin/env python3
"""
113_05 verifier -- canonical conventions and the closed forms.

Checks:
 1. Lemma 2.2  (f star g)^(s) = fhat(s) ghat(s)
 2. Lemma 2.3  (gtilde)^(s) = conj( ghat(1 - conj(s)) )
 3. Theorem 3.1  hhat(s) = fhat(s) conj(ghat(1 - conj s)),  h = f star gtilde
 4. Corollary 3.2 is not vacuous: diagonal and mirrored forms differ
 5. Remark 3.3: on a synthetic off-line mirror pair the diagonal form is
    <= 0 while the mirrored form takes a POSITIVE value
 6. Proposition 4.1  h(1) = int_0^inf f conj(g) du
 7. Convention dictionary  fhat_A(w) = fhat_B(-w),  fhat_A(1) != fhat_B(1)

All integrals are over the log variable x = log u, i.e. over R with Lebesgue
measure, and are computed with a fixed Gauss-Legendre grid.  Every probe is
Gaussian, so Gauss-Legendre is spectrally exact; the residual is at the
float64 rounding level, not at a quadrature-truncation level.  No zero of
xi, no Li coefficient, and no positive part of any Weil-type form is used
anywhere in this file.
"""
import numpy as np

PASS = []


def check(name, cond, detail=""):
    PASS.append(bool(cond))
    print(("PASS" if cond else "FAIL") + f": {name}" + (f" ({detail})" if detail else ""))


# ----------------------------------------------------------------------
# quadrature grid on the log variable
# ----------------------------------------------------------------------
XCUT = 12.0
NGL = 600
_n, _w = np.polynomial.legendre.leggauss(NGL)
X = XCUT * _n                    # nodes on [-XCUT, XCUT]
W = XCUT * _w                    # weights


def integ(vals):
    """int_R vals(x) dx"""
    return np.dot(W, vals)


# ----------------------------------------------------------------------
# probes on R_+^x, given through their log-variable profiles
#   f(u) = f_prof(log u),  g(u) = g_prof(log u)
# ----------------------------------------------------------------------
def f_prof(x):
    return x * np.exp(-x * x)


def g_prof(x):                   # complex, so that conjugation genuinely bites
    return (1.0 + 0.4j * x) * np.exp(-0.7 * x * x)


def gt_prof(x):
    """profile of gtilde(u) = conj(g(1/u))/u , i.e. gt_prof(x) = conj(g_prof(-x)) e^{-x}"""
    return np.conj(g_prof(-x)) * np.exp(-x)


# ----------------------------------------------------------------------
# transforms
# ----------------------------------------------------------------------
def mellinB(prof, s):
    """convention B:  fhat(s) = int_0^inf f(u) u^s d^x u = int f~(x) e^{sx} dx"""
    return integ(prof(X) * np.exp(s * X))


def mellinA(prof, w):
    """convention A:  fhat_A(w) = int f~(x) e^{-wx} dx"""
    return integ(prof(X) * np.exp(-w * X))


# additive convolution in the log variable:
#   (f star g)(u) = int_0^inf f(y) g(u/y) dy/y  ->  (f~ * g~)(x)
_DIFF = X[:, None] - X[None, :]          # x_i - t_j


def conv_prof(p1, p2):
    """returns the array  (p1 * p2)(x_i)  on the grid"""
    return (p2(_DIFF) * (p1(X) * W)[None, :]).sum(axis=1)


FX = f_prof(X)
GX = g_prof(X)
GTX = gt_prof(X)
H_STAR_G = conv_prof(f_prof, g_prof)     # (f star g)~ on the grid
H_ON_GRID = conv_prof(f_prof, gt_prof)   # h~ = (f star gtilde)~ on the grid


def mellin_grid(vals, s):
    return integ(vals * np.exp(s * X))


# ----------------------------------------------------------------------
# 1. Lemma 2.2 -- convolution theorem
# ----------------------------------------------------------------------
for s in [0.3, 0.5 + 1.3j, 1.0]:
    lhs = mellin_grid(H_STAR_G, s)
    rhs = mellinB(f_prof, s) * mellinB(g_prof, s)
    check(f"Lemma 2.2 convolution theorem at s={s}",
          abs(lhs - rhs) < 1e-10 * (1 + abs(rhs)),
          f"|lhs-rhs|={abs(lhs-rhs):.3e}")

# ----------------------------------------------------------------------
# 2. Lemma 2.3 -- the adjoint reflection  s -> 1 - conj(s)
# ----------------------------------------------------------------------
for s in [0.3, 0.5 + 1.3j, 1.0, -0.4 + 2.0j]:
    lhs = mellinB(gt_prof, s)
    rhs = np.conj(mellinB(g_prof, 1 - np.conj(s)))
    check(f"Lemma 2.3 adjoint reflection at s={s}",
          abs(lhs - rhs) < 1e-10 * (1 + abs(rhs)),
          f"|lhs-rhs|={abs(lhs-rhs):.3e}")

# the WRONG (unmirrored) law must fail, otherwise the test is vacuous
s0 = 0.5 + 1.3j
wrong = np.conj(mellinB(g_prof, np.conj(s0)))
check("Lemma 2.3 discriminates: the unmirrored law conj(ghat(conj s)) is a different number",
      abs(mellinB(gt_prof, s0) - wrong) > 1e-3,
      f"gap={abs(mellinB(gt_prof, s0) - wrong):.4f}")

# ----------------------------------------------------------------------
# 3. Theorem 3.1
# ----------------------------------------------------------------------
for s in [0.0, 1.0, 0.5 + 2.1j]:
    lhs = mellin_grid(H_ON_GRID, s)
    rhs = mellinB(f_prof, s) * np.conj(mellinB(g_prof, 1 - np.conj(s)))
    check(f"Theorem 3.1  hhat(s)=fhat(s)conj(ghat(1-conj s)) at s={s}",
          abs(lhs - rhs) < 1e-10 * (1 + abs(rhs)),
          f"|lhs-rhs|={abs(lhs-rhs):.3e}")

# ----------------------------------------------------------------------
# 4./5. diagonal vs mirrored, on a SYNTHETIC zero configuration
#     (synthetic: no zero of xi is used -- this is pure linear algebra on
#      the coordinate model of 107_241 Lemma 2.2)
# ----------------------------------------------------------------------
rho = 0.7 + 3.0j
rhop = 1 - np.conj(rho)
check("synthetic mirror pair is genuinely off-line",
      abs(rho.real - 0.5) > 0.1, f"Re rho={rho.real}, Re rho'={rhop.real}")

v_rho, v_rhop = 1.0, -1.0        # a primitive vector; polar slots zero
Q_diag = -(abs(v_rho) ** 2 + abs(v_rhop) ** 2)
Q_mirr = -(v_rho * np.conj(v_rhop) + v_rhop * np.conj(v_rho))
check("Remark 3.3: the diagonal form is negative on this primitive vector",
      Q_diag.real < 0, f"Q_diag={Q_diag.real}")
check("Remark 3.3: the mirrored form is POSITIVE on the same vector (hence indefinite)",
      Q_mirr.real > 0, f"Q_mirr={Q_mirr.real}")
check("Corollary 3.2 is not vacuous: the two forms differ", abs(Q_diag - Q_mirr) > 1e-6)

rho_on = 0.5 + 3.0j
check("on-line zero: rho' = rho, so the two forms coincide there",
      abs((1 - np.conj(rho_on)) - rho_on) < 1e-14)

# ----------------------------------------------------------------------
# 6. Proposition 4.1   h(1) = int_0^inf f conj(g) du
# ----------------------------------------------------------------------
lhs = np.dot(W, gt_prof(-X) * f_prof(X))        # h~(0) = int f~(t) gt~(-t) dt
rhs = integ(f_prof(X) * np.conj(g_prof(X)) * np.exp(X))
check("Proposition 4.1  h(1) = int_0^inf f(u) conj(g(u)) du",
      abs(lhs - rhs) < 1e-12 * (1 + abs(rhs)), f"h(1)={lhs:.12g}")
check("Proposition 4.1: h(1) is not accidentally zero on this pair (test not vacuous)",
      abs(lhs) > 1e-3, f"|h(1)|={abs(lhs):.6f}")

# ----------------------------------------------------------------------
# 7. convention dictionary
# ----------------------------------------------------------------------
for w in [0.4, 1.0, 0.5 + 1.0j]:
    a, b = mellinA(f_prof, w), mellinB(f_prof, -w)
    check(f"Proposition 1.2  fhat_A(w)=fhat_B(-w) at w={w}",
          abs(a - b) < 1e-12 * (1 + abs(b)))

check("Proposition 1.2: fhat_A(0)=fhat_B(0) (the mass coordinate is shared)",
      abs(mellinA(f_prof, 0) - mellinB(f_prof, 0)) < 1e-14)
check("Proposition 1.2: fhat_A(1) != fhat_B(1) (the second polar slot genuinely differs)",
      abs(mellinA(f_prof, 1) - mellinB(f_prof, 1)) > 1e-3,
      f"A(1)={mellinA(f_prof,1):.8g}, B(1)={mellinB(f_prof,1):.8g}")

# ----------------------------------------------------------------------
print()
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
print("VERDICT: SOME CHECKS FAILED")
raise SystemExit(1)
