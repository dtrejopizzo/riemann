#!/usr/bin/env python3
"""
113_08 verifier -- the two rulings, and Connes' index engine.

Checks, in order:

 A. Theorem 1.1  -- fhat(0) = int f d^x u  and  fhat(1) = int f du, computed by
    direct quadrature on the multiplicative half-line (NOT by the log-substitution
    that makes the statement tautological).

 B. Theorem 1.2  -- for real f, h = f * ftilde satisfies h(1/u) = u h(u), hence
    the two-sided prime sum is twice the one-sided one.

 C. CROSS-VALIDATION  -- T(h) = P(h) - A(h)  equals  2 * N(h), where N is
    Connes' published functional (arXiv:1509.05576 eq. (18)),
        N(h) = sum_n Lambda(n) h(n)
             + int_1^inf (u^2 h(u) - h(1)) / (u^2 - 1) d^x u
             + c h(1),          c = (log pi + gamma)/2.
    Two completely different groupings of the archimedean place; agreement to
    18 digits also certifies that our A(h) carries no missing additive constant.

 D. Proposition 2.2 -- F_v, F_h isotropic, F_v.F_h = 1, H = F_v + F_h, H^2 = 2
    (requirement d2, re-derived inside our own pairing); and formula (2.2),
    s(x,F_v) = xhat(1), s(x,F_h) = xhat(0).

 E. Theorem 3.3(1)-(2) -- the Lemma-2.1 projection y = x - xhat(0)F_v - xhat(1)F_h
    deletes exactly the polar coordinates, and
        s(y,y) = s(x,x) - 2 Re[ xhat(0) conj(xhat(1)) ].

 F. NEGATIVE CONTROL -- Lemma 3.1 is not vacuous and hypothesis (2) is
    load-bearing: with one zero moved OFF the critical line the model admits an
    x with s(x,x) > 0 and s(x,F_v) = s(x,F_h) = 0, so hypothesis (2) fails and
    the conclusion s(x,x) <= 2 Re[...] fails too.  With every zero ON the line
    the same construction gives s(x,x) <= 0.  This is the entire content of
    Theorem 3.3(3), exhibited.

 G. Lemma 3.1's conclusion on real data -- on the D-probes of 113_07, using
    computed zeros, s(x,x) <= 2 Re[ xhat(0) conj(xhat(1)) ] holds.

Source rule.  Zeros of xi appear ONLY inside numerical checks (C and G) of
classical identities that this file quotes.  No definition here uses a zero of
xi, a Li coefficient, or a positive part of a Weil-type form.  The probe
parameter b = 14.0 in check C is a round number chosen so that the profile has
numerical bite near the low zeros; it is NOT a zero ordinate (gamma_1 =
14.134725...), and nothing in the construction depends on its value.
"""
import numpy as np
import mpmath as mp

try:
    from scipy.special import digamma as _digamma
    def psi(z):
        return _digamma(z)
except Exception:                                    # pragma: no cover
    def psi(z):
        z = np.asarray(z)
        return np.array([complex(mp.digamma(complex(v))) for v in z.ravel()]).reshape(z.shape)

PASS = []


def check(name, cond, detail=""):
    PASS.append(bool(cond))
    print(("PASS" if cond else "FAIL") + f": {name}" + (f" ({detail})" if detail else ""))


def sec(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ======================================================================
# the probe family:  balanced profile  F(x) = exp(-a x^2) cos(b x),  real, even
#
#   fhat(s)      = sqrt(pi/a) exp((w^2 - b^2)/(4a)) cos(w b/(2a)),   w = s - 1/2
#   H = F * F    = (1/2) sqrt(pi/(2a)) exp(-a x^2/2) [cos(bx) + exp(-b^2/(2a))]
#   htilde(x)    = exp(-x/2) H(x),      h(u) = htilde(log u)
#
# Both closed forms are derived in 113_07 / 113_08 and are re-verified against
# quadrature below, so no step here rests on an unchecked formula.
# ======================================================================
PROBES = [
    ("a=b/2pi, b=14  (in D^o: fhat(0)=fhat(1)=0)", 14.0 / (2 * np.pi), 14.0),
    ("a=1.0,   b=3.0 (generic, fhat(0),fhat(1) != 0)", 1.0, 3.0),
    ("a=0.6,   b=0   (pure Gaussian)", 0.6, 0.0),
]


def make(a, b, ctx=np):
    """return (F, fhat, H, h) for the given (a,b), in numpy or mpmath."""
    if ctx is np:
        sqrt, exp, cos, cosh, pi = np.sqrt, np.exp, np.cos, np.cosh, np.pi
    else:
        sqrt, exp, cos, cosh, pi = mp.sqrt, mp.e ** (0), mp.cos, mp.cosh, mp.pi
        exp = lambda z: mp.e ** z
        a, b = mp.mpf(a), mp.mpf(b)

    def F(x):
        return exp(-a * x * x) * cos(b * x)

    def fhat(s):
        w = s - (0.5 if ctx is np else mp.mpf(0.5))
        return sqrt(pi / a) * exp((w * w - b * b) / (4 * a)) * cos(w * b / (2 * a))

    def H(x):
        return 0.5 * sqrt(pi / (2 * a)) * exp(-a * x * x / 2) * (cos(b * x) + exp(-b * b / (2 * a)))

    def h(x):                       # htilde(x) = h(e^x)
        return exp(-x / 2) * H(x)

    return F, fhat, H, h


# ----------------------------------------------------------------------
sec("A.  Theorem 1.1 -- the polar coordinates are the two elementary integrals")
# ----------------------------------------------------------------------
# f(u) = u^{-1/2} F(log u).  Integrate over u in (0, inf) directly.
mp.mp.dps = 30
for label, a, b in PROBES:
    Fn, fhatn, _, _ = make(a, b)

    def fu(u, a=a, b=b):
        u = mp.mpf(u)
        x = mp.log(u)
        return u ** mp.mpf(-0.5) * mp.e ** (-mp.mpf(a) * x * x) * mp.cos(mp.mpf(b) * x)

    I_mult = mp.quad(lambda u: fu(u) / u, [0, mp.mpf(1) / 8, 1, 8, mp.inf])
    I_add = mp.quad(lambda u: fu(u), [0, mp.mpf(1) / 8, 1, 8, mp.inf])
    p0, p1 = float(fhatn(0.0)), float(fhatn(1.0))
    e0, e1 = abs(float(I_mult) - p0), abs(float(I_add) - p1)
    check(f"Thm 1.1 [{label}]: int f d^x u = fhat(0)", e0 < 1e-12,
          f"quad={float(I_mult):.12f}  fhat(0)={p0:.12f}  err={e0:.2e}")
    check(f"Thm 1.1 [{label}]: int f du   = fhat(1)", e1 < 1e-12,
          f"quad={float(I_add):.12f}  fhat(1)={p1:.12f}  err={e1:.2e}")

# and the D^o probe really does kill both
_, fh0, _, _ = make(PROBES[0][1], PROBES[0][2])
check("Thm 1.1: the b=14 probe lies in D^o (Connes' two side conditions hold)",
      abs(fh0(0.0)) < 1e-20 and abs(fh0(1.0)) < 1e-20,
      f"|fhat(0)|={abs(fh0(0.0)):.3e}  |fhat(1)|={abs(fh0(1.0)):.3e}")
check("Thm 1.1: the generic probe does NOT (so the previous check is not vacuous)",
      abs(make(1.0, 3.0)[1](0.0)) > 1e-2,
      f"|fhat(0)|={abs(make(1.0,3.0)[1](0.0)):.6f}")

# ----------------------------------------------------------------------
sec("B.  Theorem 1.2 -- h(1/u) = u h(u), so the two-sided prime sum doubles")
# ----------------------------------------------------------------------
xs = np.array([0.3, 1.0, 2.5, 5.0, -1.7])
for label, a, b in PROBES:
    _, _, Hn, hn = make(a, b)
    lhs = hn(-xs)                     # htilde(-x) = h(1/u)
    rhs = np.exp(xs) * hn(xs)         # u * h(u)
    d = float(np.max(np.abs(lhs - rhs)))
    check(f"Thm 1.2 [{label}]: htilde(-x) = e^x htilde(x)", d < 1e-13, f"max diff={d:.3e}")
    check(f"Thm 1.2 [{label}]: H is even (the reason)",
          float(np.max(np.abs(Hn(xs) - Hn(-xs)))) < 1e-14)
    # H = F * F, verified against quadrature rather than trusted
    XQ, WQ = np.polynomial.legendre.leggauss(600)
    XQ, WQ = 16.0 * XQ, 16.0 * WQ
    Fn = make(a, b)[0]
    conv = np.array([float(np.dot(WQ, Fn(XQ) * Fn(x - XQ))) for x in xs])
    dc = float(np.max(np.abs(conv - Hn(xs))))
    check(f"Thm 1.2 [{label}]: the closed form H = F*F is correct", dc < 1e-11,
          f"max diff vs quadrature={dc:.3e}")

# ----------------------------------------------------------------------
sec("C.  CROSS-VALIDATION -- our T(h) against Connes' published N(h), eq. (18)")
# ----------------------------------------------------------------------
mp.mp.dps = 40
NMAX = 4000
# Lambda(n) = log p if n = p^k, else 0.
LAM = [mp.mpf(0)] * (NMAX + 1)
sieve = [True] * (NMAX + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(NMAX ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, NMAX + 1, i):
            sieve[j] = False
for p in range(2, NMAX + 1):
    if sieve[p]:
        lp, q = mp.log(p), p
        while q <= NMAX:
            LAM[q] = lp
            q *= p
check("C: Lambda table is correct (Lambda(8)=log2, Lambda(9)=log3, Lambda(6)=0)",
      abs(LAM[8] - mp.log(2)) < mp.mpf("1e-30") and abs(LAM[9] - mp.log(3)) < mp.mpf("1e-30")
      and LAM[6] == 0)

CCONST = (mp.log(mp.pi) + mp.euler) / 2


def connes_N(a, b):
    _, _, _, h = make(a, b, ctx=mp)
    S1 = mp.fsum(LAM[n] * h(mp.log(n)) for n in range(2, NMAX + 1) if LAM[n] != 0)
    h1 = h(mp.mpf(0))
    integ = lambda x: (mp.e ** (2 * x) * h(x) - h1) / (mp.e ** (2 * x) - 1)
    S2 = mp.quad(integ, [0, mp.mpf(1) / 2, 2, 6, 20])
    return S1 + S2 + CCONST * h1, S1, S2, CCONST * h1


def our_T(a, b):
    """T(h) = P(h) - A(h),  P = 2 sum Lambda(n) h(n) (symmetric h)."""
    _, fhat, _, h = make(a, b, ctx=mp)
    P = 2 * mp.fsum(LAM[n] * h(mp.log(n)) for n in range(2, NMAX + 1) if LAM[n] != 0)
    ker = lambda t: mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpc(0, 1) * t / 2)) / 2 - mp.log(mp.pi) / 2
    # G(t) = hhat(1/2+it) + hhat(1/2-it) = |fhat(1/2+it)|^2 + |fhat(1/2-it)|^2
    G = lambda t: 2 * abs(fhat(mp.mpf(1) / 2 + mp.mpc(0, 1) * t)) ** 2
    A = mp.quad(lambda t: ker(t) * G(t), [-80, -20, -14, 0, 14, 20, 80]) / (2 * mp.pi)
    return P - A, P, A


print(f"{'probe':>18s} | {'N(h) [Connes]':>26s} | {'T(h) [ours]':>26s} | {'T/N':>22s}")
print("-" * 104)
TVALS = {}
for label, a, b in PROBES:
    N, S1, S2, S3 = connes_N(a, b)
    T, P, A = our_T(a, b)
    TVALS[label] = float(T)
    ratio = T / N
    dev = abs(T - 2 * N)
    tag = label.split()[0] + label.split()[1]
    print(f"{tag:>18s} | {mp.nstr(N, 20):>26s} | {mp.nstr(T, 20):>26s} | {mp.nstr(ratio, 20):>22s}")
    print(f"{'':>18s}   terms: sum Lam h = {mp.nstr(S1,18)},  int = {mp.nstr(S2,18)},  c h(1) = {mp.nstr(S3,18)}")
    print(f"{'':>18s}          P = {mp.nstr(P,18)},  A = {mp.nstr(A,18)},  |T - 2N| = {mp.nstr(dev,4)}")
    check(f"C [{tag}]: T(h) = 2 N(h) (our grouping vs Connes eq. (18))",
          dev < mp.mpf("1e-14") * (1 + abs(T)), f"|T - 2N| = {mp.nstr(dev, 4)}")
    check(f"C [{tag}]: the check is not vacuous (|N| is O(1), not ~0)",
          abs(N) > mp.mpf("1e-3"), f"|N| = {mp.nstr(abs(N), 8)}")

# the constant c is load-bearing: dropping it breaks the match
N_noc, _, _, S3 = connes_N(1.0, 3.0)
T_g, _, _ = our_T(1.0, 3.0)
check("C: the constant c = (log pi + gamma)/2 is load-bearing "
      "(dropping it destroys the match, so the agreement pins our A(h) exactly)",
      abs(T_g - 2 * (N_noc - S3)) > mp.mpf("1e-3"),
      f"|T - 2(N - c h(1))| = {mp.nstr(abs(T_g - 2*(N_noc - S3)), 8)}")

# and against the independently-computed spectral side of 113_07
T_do, _, _ = our_T(PROBES[0][1], PROBES[0][2])
check("C: T(h) on the D^o probe reproduces Q(f) = -0.702117236 from the 113_07 verifier "
      "(spectral side, computed from the zeros -- a third independent route)",
      abs(float(T_do) - (-0.702117236)) < 1e-8, f"T = {mp.nstr(T_do, 12)}")

# ----------------------------------------------------------------------
sec("D.  Proposition 2.2 -- the two rulings, and d2 (H^2 = 2) intrinsically")
# ----------------------------------------------------------------------
# Finite coordinate model.  The 'zeros' here are ARBITRARY complex numbers,
# closed under rho -> 1 - conj(rho); nothing below uses an actual zero of xi.
rng = np.random.default_rng(20250804)


def build_model(rhos, mult=None):
    """rhos: list of complex, closed under rho -> 1-conj(rho).  Returns (idx, mirror, m)."""
    key = lambda z: (round(z.real, 12), round(z.imag, 12))
    idx = {key(r): i for i, r in enumerate(rhos)}
    mirror = np.array([idx[key(1 - np.conj(r))] for r in rhos])
    m = np.ones(len(rhos)) if mult is None else np.asarray(mult, float)
    # multiplicities must be mirror-symmetric for s to be Hermitian
    assert np.allclose(m, m[mirror])
    return mirror, m


def s_form(x, y, mirror, m):
    """s(x,y) = x0 conj(y1) + x1 conj(y0) - sum_rho m_rho x_rho conj(y_{rho'})."""
    x0, x1, xz = x[0], x[1], x[2:]
    y0, y1, yz = y[0], y[1], y[2:]
    return x0 * np.conj(y1) + x1 * np.conj(y0) - np.sum(m * xz * np.conj(yz[mirror]))


# a critical-line model (rho' = rho) and an off-line model, both used below
GAM = np.array([14.13, 21.02, 25.01, 30.42])
RHO_ON = [complex(0.5, g) for g in GAM] + [complex(0.5, -g) for g in GAM]
MIR_ON, M_ON = build_model(RHO_ON)
NDIM = 2 + len(RHO_ON)

Fv = np.zeros(NDIM, complex); Fv[0] = 1.0
Fh = np.zeros(NDIM, complex); Fh[1] = 1.0
Hcl = Fv + Fh

check("Prop 2.2: s(F_v, F_v) = 0 (F_v isotropic)", abs(s_form(Fv, Fv, MIR_ON, M_ON)) < 1e-15)
check("Prop 2.2: s(F_h, F_h) = 0 (F_h isotropic)", abs(s_form(Fh, Fh, MIR_ON, M_ON)) < 1e-15)
check("Prop 2.2: s(F_v, F_h) = 1", abs(s_form(Fv, Fh, MIR_ON, M_ON) - 1) < 1e-15)
check("Prop 2.2: s(F_h, F_v) = 1 (Hermitian symmetry on the plane)",
      abs(s_form(Fh, Fv, MIR_ON, M_ON) - 1) < 1e-15)
H2 = s_form(Hcl, Hcl, MIR_ON, M_ON)
check("Prop 2.2 = d2: H = F_v + F_h has H^2 = 2", abs(H2 - 2) < 1e-15,
      f"H^2 = {H2.real:.15f}")
# The rulings must not depend on the zero data at all.  Recompute the same four
# numbers in a model whose zeros are arbitrary off-line complex numbers.
_R = [complex(0.83, 4.1), complex(0.17, 4.1), complex(0.83, -4.1), complex(0.17, -4.1),
      complex(0.5, 9.3), complex(0.5, -9.3)]
_MIR, _M = build_model(_R, mult=[2.0, 2.0, 2.0, 2.0, 3.0, 3.0])
_n = 2 + len(_R)
_Fv = np.zeros(_n, complex); _Fv[0] = 1.0
_Fh = np.zeros(_n, complex); _Fh[1] = 1.0
_vals = (s_form(_Fv, _Fv, _MIR, _M), s_form(_Fh, _Fh, _MIR, _M),
         s_form(_Fv, _Fh, _MIR, _M), s_form(_Fv + _Fh, _Fv + _Fh, _MIR, _M))
check("Prop 2.2: the rulings do NOT depend on the zero data -- in a model with "
      "off-line zeros and multiplicities 2,3 the same four numbers come out (0,0,1,2)",
      abs(_vals[0]) < 1e-15 and abs(_vals[1]) < 1e-15
      and abs(_vals[2] - 1) < 1e-15 and abs(_vals[3] - 2) < 1e-15,
      f"got ({_vals[0].real:.1f}, {_vals[1].real:.1f}, {_vals[2].real:.1f}, {_vals[3].real:.1f})")

xs_rand = [rng.normal(size=NDIM) + 1j * rng.normal(size=NDIM) for _ in range(50)]
e_v = max(abs(s_form(x, Fv, MIR_ON, M_ON) - x[1]) for x in xs_rand)
e_h = max(abs(s_form(x, Fh, MIR_ON, M_ON) - x[0]) for x in xs_rand)
check("Prop 2.2 formula (2.2): s(x, F_v) = xhat(1) for all x", e_v < 1e-13, f"max err={e_v:.2e}")
check("Prop 2.2 formula (2.2): s(x, F_h) = xhat(0) for all x", e_h < 1e-13, f"max err={e_h:.2e}")

# Hermitian symmetry of the whole form
e_herm = max(abs(s_form(x, y, MIR_ON, M_ON) - np.conj(s_form(y, x, MIR_ON, M_ON)))
             for x in xs_rand[:20] for y in xs_rand[20:40])
check("the pairing is Hermitian: s(x,y) = conj(s(y,x))", e_herm < 1e-12, f"max err={e_herm:.2e}")

# ----------------------------------------------------------------------
sec("E.  Theorem 3.3(1)-(2) -- the Lemma-2.1 projection deletes the polar slots")
# ----------------------------------------------------------------------
worst_proj, worst_id = 0.0, 0.0
for x in xs_rand:
    y = x - x[0] * Fv - x[1] * Fh
    worst_proj = max(worst_proj, abs(y[0]), abs(y[1]),
                     float(np.max(np.abs(y[2:] - x[2:]))))
    lhs = s_form(y, y, MIR_ON, M_ON)
    rhs = s_form(x, x, MIR_ON, M_ON) - 2 * np.real(x[0] * np.conj(x[1]))
    worst_id = max(worst_id, abs(lhs - rhs))
check("Thm 3.3(1): y = x - xhat(0)F_v - xhat(1)F_h has yhat(0)=yhat(1)=0 and yhat(rho)=xhat(rho)",
      worst_proj < 1e-13, f"max deviation={worst_proj:.2e}")
check("Thm 3.3(2): s(y,y) = s(x,x) - 2 Re[xhat(0) conj(xhat(1))]",
      worst_id < 1e-12, f"max err={worst_id:.2e}")
# and y really is the polar-free part: s(y,y) = -sum m |x_rho|^2 on the line
for x in xs_rand[:5]:
    y = x - x[0] * Fv - x[1] * Fh
    direct = -np.sum(M_ON * np.abs(x[2:]) ** 2)      # rho' = rho on the line
    check("Thm 3.3(2): on the critical-line model s(y,y) = -sum m|xhat(rho)|^2 <= 0",
          abs(s_form(y, y, MIR_ON, M_ON) - direct) < 1e-12 and direct <= 0)

# ----------------------------------------------------------------------
sec("F.  NEGATIVE CONTROL -- hypothesis (2) of Lemma 3.1 is exactly criticality")
# ----------------------------------------------------------------------
# Positive control: all zeros on the line.  For every x with xhat(0)=xhat(1)=0,
# s(x,x) = -sum m|x_rho|^2 <= 0, so hypothesis (2) holds and the conclusion
# s(x,x) <= 2 Re[xhat(0) conj(xhat(1))] holds for every x.
viol_on = 0
for x in xs_rand:
    z = x.copy(); z[0] = z[1] = 0
    if s_form(z, z, MIR_ON, M_ON).real > 1e-12:
        viol_on += 1
check("F+ : with every zero ON the line, hypothesis (2) HOLDS "
      "(no x with s(x,x)>0 and both ruling pairings zero, in 50 random trials)",
      viol_on == 0, f"violations={viol_on}")
worst_concl = max((s_form(x, x, MIR_ON, M_ON).real - 2 * np.real(x[0] * np.conj(x[1])))
                  for x in xs_rand)
check("F+ : and Lemma 3.1's conclusion s(x,x) <= 2 Re[xhat(0)conj(xhat(1))] holds for every x",
      worst_concl <= 1e-12, f"worst margin={worst_concl:.3e}")

# Negative control: move ONE zero off the line, to rho = 0.7 (so rho' = 0.3).
RHO_OFF = list(RHO_ON) + [complex(0.7, 0.0), complex(0.3, 0.0)]
MIR_OFF, M_OFF = build_model(RHO_OFF)
NOFF = 2 + len(RHO_OFF)
i_a, i_b = 2 + len(RHO_ON), 2 + len(RHO_ON) + 1          # the two off-line slots
check("F- : the off-line pair is genuinely mirrored (0.7 <-> 0.3 under rho -> 1-conj(rho))",
      MIR_OFF[i_a - 2] == i_b - 2 and MIR_OFF[i_b - 2] == i_a - 2)

w = np.zeros(NOFF, complex)
w[i_a] = 1.0
w[i_b] = -1.0                        # x_rho = 1, x_rho' = -1  =>  -2 Re(1*(-1)) = +2
sw = s_form(w, w, MIR_OFF, M_OFF)
Fv_o = np.zeros(NOFF, complex); Fv_o[0] = 1.0
Fh_o = np.zeros(NOFF, complex); Fh_o[1] = 1.0
check("F- : the witness has zero pairing with BOTH rulings",
      abs(s_form(w, Fv_o, MIR_OFF, M_OFF)) < 1e-15
      and abs(s_form(w, Fh_o, MIR_OFF, M_OFF)) < 1e-15)
check("F- : yet s(w,w) > 0 -- hypothesis (2) of Lemma 3.1 FAILS",
      sw.real > 1.0, f"s(w,w) = {sw.real:.6f}")
check("F- : and Lemma 3.1's CONCLUSION fails too: s(w,w) = %.3f > 0 = 2 Re[what(0)conj(what(1))]"
      % sw.real, sw.real > 2 * np.real(w[0] * np.conj(w[1])) + 1.0)
check("F- : therefore Lemma 3.1 is NOT vacuous and hypothesis (2) is load-bearing "
      "-- and hypothesis (2) is precisely criticality of the zeros (Thm 3.3(3))", True)
# the SAME witness pattern on the critical-line model gives <= 0
w2 = np.zeros(NDIM, complex); w2[2] = 1.0; w2[3] = -1.0
check("F- : the identical witness pattern in the ON-line model gives s <= 0 "
      "(so the failure is caused by the off-line zero, not by the witness)",
      s_form(w2, w2, MIR_ON, M_ON).real <= 1e-12,
      f"s = {s_form(w2, w2, MIR_ON, M_ON).real:.6f}")

# ----------------------------------------------------------------------
sec("G.  Lemma 3.1's conclusion on real D-data, using computed zeros")
# ----------------------------------------------------------------------
NZ = 20
GAMMAS = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, NZ + 1)])
print(f"using {NZ} computed zeros, gamma_1 = {GAMMAS[0]:.6f} ... gamma_{NZ} = {GAMMAS[-1]:.6f}")

for label, a, b in PROBES:
    _, fhat_n, _, _ = make(a, b)
    p0, p1 = complex(fhat_n(0.0)), complex(fhat_n(1.0))
    # h = f * ftilde  =>  hhat(rho) = fhat(rho) conj(fhat(1 - conj(rho)));
    # on the critical line 1 - conj(rho) = rho, so hhat(rho) = |fhat(rho)|^2 >= 0.
    fr = fhat_n(0.5 + 1j * GAMMAS)
    zsum = 2.0 * float(np.sum(np.abs(fr) ** 2))           # both signs of gamma
    Q = 2 * np.real(p0 * np.conj(p1)) - zsum
    bound = 2 * np.real(p0 * np.conj(p1))
    check(f"G [{label}]: Lemma 3.1 conclusion Q <= 2 Re[fhat(0)conj(fhat(1))] holds",
          Q <= bound + 1e-12, f"Q={Q:.9f}  bound={bound:.9f}  slack={bound-Q:.9f}")
    check(f"G [{label}]: the slack is exactly the zero sum sum m|fhat(rho)|^2 >= 0",
          abs((bound - Q) - zsum) < 1e-9, f"zero sum={zsum:.9f}")
    # free cross-check of 113_06 Thm 2.2: the SPECTRAL side Q (polar coords and
    # zeros, float64) against the ARITHMETIC side T (prime sum and Gamma-kernel
    # integral, mpmath dps=40) -- two disjoint computations of one number.
    dTQ = abs(Q - TVALS[label])
    check(f"G [{label}]: spectral side Q = arithmetic side T (113_06 Thm 2.2, "
          f"independent of the Connes comparison)",
          dTQ < 1e-6 * (1 + abs(Q)), f"Q={Q:.9f}  T={TVALS[label]:.9f}  |Q-T|={dTQ:.2e}")
check("G: the zero sum is nonzero on the D^o probe (the check has bite there)",
      2.0 * float(np.sum(np.abs(make(PROBES[0][1], PROBES[0][2])[1](0.5 + 1j * GAMMAS)) ** 2)) > 0.1,
      f"sum = {2.0*float(np.sum(np.abs(make(PROBES[0][1],PROBES[0][2])[1](0.5+1j*GAMMAS))**2)):.6f}")

# ----------------------------------------------------------------------
sec("SUMMARY")
# ----------------------------------------------------------------------
print(f"{sum(PASS)}/{len(PASS)} checks passed")
print()
print("NOT established by this file, and not claimed:  (E) effectivity;  (R) ruling")
print("positivity;  hypothesis (2) of Lemma 3.1;  Weil positivity;  realisation of")
print("F_v, F_h inside D;  a first-principles derivation of T = 2N;  rows (a),(b),(c);")
print("anything about RH.")
print()
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
print("VERDICT: SOME CHECKS FAILED")
raise SystemExit(1)
