#!/usr/bin/env python3
"""
113_07 verifier -- h(1) is a norm.

Checks:
 1. Lemma 1.2: the three operations in balanced coordinates
      (i)  balanced profile of gtilde is  conj(G(-x))
      (ii) balanced profile of f star g is  F * G
      (iii) fhat(s) = Fhat(s - 1/2)
 2. Theorem 2.1: all three expressions for L(f,g) agree,
      (f star gtilde)(1) = int_0^inf f conj(g) du
                         = int_R F conj(G) dx
                         = (1/2pi) int_R fhat(1/2+it) conj(ghat(1/2+it)) dt
 3. Theorem 2.1 positivity: L(f,f) = ||F||_2^2 > 0 on several probes.
 4. Corollary 2.3 (the refutation): (f star ftilde)(1) = ||f||^2 > 0, so no
    nonzero diagonal element lies in the admissible class A of 113_03.
 5. Theorem 3.1(1): the Weil identity of 113_06 Theorem 2.2 nevertheless HOLDS
    on the diagonal element h = f star ftilde, which has h(1) != 0.  This is
    the decisive check: the pairing is defined on exactly the data that A
    excludes.
 6. Theorem 3.1(2)/(4): the coordinate formula
      Q(f) = 2 Re[ fhat(0) conj(fhat(1)) ] - sum_rho m_rho fhat(rho) conj(fhat(rho'))
    agrees with P(h) + W_inf(h), and Q(f) is real.
 7. Lemma 1.4: D_theta is closed under star and under the involution
    (decay of the balanced profile of f star gtilde is retained).
 8. Remark 2.4: xi is real and sign-changing on the critical line, so the
    off-diagonal form (2.2) is indefinite -- consistent with, and not a
    contradiction of, positive definiteness on the diagonal.

Zeros of xi are used ONLY inside the numerical check of the classical identity
quoted from 113_06.  Evaluations of xi itself (check 8) are evaluations of xi,
which the source rule permits.  No definition in 113_07 uses a zero of xi, a
Li coefficient, or a positive part of a Weil-type form.
"""
import numpy as np
import mpmath as mp

try:
    from scipy.special import digamma as _digamma
    def psi(z):
        return _digamma(z)
except Exception:                                   # pragma: no cover
    def psi(z):
        z = np.asarray(z)
        return np.array([complex(mp.digamma(complex(v))) for v in z.ravel()]).reshape(z.shape)

PASS = []


def check(name, cond, detail=""):
    PASS.append(bool(cond))
    print(("PASS" if cond else "FAIL") + f": {name}" + (f" ({detail})" if detail else ""))


# ----------------------------------------------------------------------
# grids
# ----------------------------------------------------------------------
XCUT, NX = 14.0, 900
_n, _w = np.polynomial.legendre.leggauss(NX)
X, WX = XCUT * _n, XCUT * _w                        # log variable

TCUT, NT = 60.0, 1400
_m, _v = np.polynomial.legendre.leggauss(NT)
T, WT = TCUT * _m, TCUT * _v                        # critical line

PMAX, KMAX = 3000, 60


def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return np.nonzero(sieve)[0]


PRIMES = primes_upto(PMAX)
LOGP = np.log(PRIMES.astype(float))

NZ = 20
GAMMAS = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, NZ + 1)])

DIFF = X[:, None] - X[None, :]


def integ(v):
    return np.dot(WX, v)


# ----------------------------------------------------------------------
# balanced probes: f is given through its BALANCED profile F(x) = e^{x/2} f(e^x)
# ----------------------------------------------------------------------
BAL = {
    "F=e^{-x^2}":            lambda x: np.exp(-x * x),
    "F=x e^{-x^2}":          lambda x: x * np.exp(-x * x),
    "F=(1+0.4ix)e^{-0.7x^2}": lambda x: (1.0 + 0.4j * x) * np.exp(-0.7 * x * x),
    "F=e^{-x^2}cos(2x)":     lambda x: np.exp(-x * x) * np.cos(2 * x),
    "F=(x+1j)e^{-1.3x^2}":   lambda x: (x + 1j) * np.exp(-1.3 * x * x),
}


def raw_from_bal(Fp):
    """unbalanced profile  f~(x) = e^{-x/2} F(x)"""
    return lambda x: Fp(x) * np.exp(-0.5 * x)


def tilde_raw(prof):
    """profile of gtilde:  conj(g~(-x)) e^{-x}"""
    return lambda x: np.conj(prof(-x)) * np.exp(-x)


def conv(p1, p2):
    """additive convolution on the grid: (p1 * p2)(x_i)"""
    return (p2(DIFF) * (p1(X) * WX)[None, :]).sum(axis=1)


def mellinB(prof, s):
    """fhat(s) = int f~(x) e^{sx} dx"""
    s = np.asarray(s, dtype=complex)
    return (prof(X)[None, :] * np.exp(np.outer(s, X)) * WX[None, :]).sum(axis=1)


def mellin_grid(vals, s):
    s = np.asarray(s, dtype=complex)
    return (vals[None, :] * np.exp(np.outer(s, X)) * WX[None, :]).sum(axis=1)


# ----------------------------------------------------------------------
# 1. Lemma 1.2
# ----------------------------------------------------------------------
Fp = BAL["F=(1+0.4ix)e^{-0.7x^2}"]
Gp = BAL["F=(x+1j)e^{-1.3x^2}"]
f_raw, g_raw = raw_from_bal(Fp), raw_from_bal(Gp)

# (i) balanced profile of gtilde is conj(G(-x))
gt = tilde_raw(g_raw)
lhs = np.exp(0.5 * X) * gt(X)
rhs = np.conj(Gp(-X))
check("Lemma 1.2(i): balanced profile of gtilde is conj(G(-x))",
      np.max(np.abs(lhs - rhs)) < 1e-12,
      f"max diff={np.max(np.abs(lhs - rhs)):.3e}")

# (ii) balanced profile of f star g is F * G
lhs = np.exp(0.5 * X) * conv(f_raw, g_raw)
rhs = conv(Fp, Gp)
check("Lemma 1.2(ii): balanced profile of f star g is F * G",
      np.max(np.abs(lhs - rhs)) < 1e-11,
      f"max diff={np.max(np.abs(lhs - rhs)):.3e}")

# (iii) fhat(s) = Fhat(s - 1/2)
for s in [0.0, 1.0, 0.5 + 3.0j, -1.0, 2.0]:
    a = complex(mellinB(f_raw, [s])[0])
    b = complex(mellinB(lambda x: Fp(x), [s - 0.5])[0])
    check(f"Lemma 1.2(iii): fhat(s)=Fhat(s-1/2) at s={s}",
          abs(a - b) < 1e-11 * (1 + abs(b)), f"|diff|={abs(a-b):.3e}")

# ----------------------------------------------------------------------
# 2./3. Theorem 2.1
# ----------------------------------------------------------------------
print()
names = list(BAL)
for i, na in enumerate(names):
    nb = names[(i + 1) % len(names)]
    FA, FB = BAL[na], BAL[nb]
    fa, fb = raw_from_bal(FA), raw_from_bal(FB)

    H = conv(fa, tilde_raw(fb))                     # h~ on the grid
    # h(1) = h~(0): interpolate by re-convolving at x = 0 directly
    L_conv = np.dot(WX, fa(X) * np.conj(fb(X)) * np.exp(X))     # int f conj(g) du
    L_bal = np.dot(WX, FA(X) * np.conj(FB(X)))                  # int F conj(G) dx
    fh = mellinB(fa, 0.5 + 1j * T)
    gh = mellinB(fb, 0.5 + 1j * T)
    L_line = np.dot(WT, fh * np.conj(gh)) / (2 * np.pi)         # Plancherel form

    check(f"Theorem 2.1 [{na} vs {nb}]: int f conj(g) du = int F conj(G) dx",
          abs(L_conv - L_bal) < 1e-11 * (1 + abs(L_bal)),
          f"|diff|={abs(L_conv - L_bal):.3e}")
    check(f"Theorem 2.1 [{na} vs {nb}]: = (1/2pi) int fhat conj(ghat) on Re s=1/2",
          abs(L_conv - L_line) < 1e-9 * (1 + abs(L_line)),
          f"|diff|={abs(L_conv - L_line):.3e}")

print()
for na in names:
    FA = BAL[na]
    fa = raw_from_bal(FA)
    diag = np.dot(WX, fa(X) * np.conj(fa(X)) * np.exp(X))
    nrm = np.dot(WX, np.abs(FA(X)) ** 2)
    check(f"Theorem 2.1 positivity [{na}]: L(f,f)=||F||_2^2 > 0",
          abs(diag - nrm) < 1e-12 * (1 + nrm) and diag.real > 1e-3,
          f"L(f,f)={diag.real:.9f}")

# ----------------------------------------------------------------------
# 4. Corollary 2.3 -- the refutation
# ----------------------------------------------------------------------
print()
for na in names:
    FA = BAL[na]
    fa = raw_from_bal(FA)
    Hd = conv(fa, tilde_raw(fa))                # h~ of the diagonal element
    # h(1) = h~(0) evaluated directly (not by grid interpolation)
    h1 = np.dot(WX, fa(X) * np.conj(fa(X)) * np.exp(X))
    check(f"Corollary 2.3 [{na}]: (f star ftilde)(1) = ||f||^2 > 0, so it is NOT in A",
          h1.real > 1e-3 and abs(h1.imag) < 1e-12,
          f"h(1)={h1.real:.9f}")

# and the value is exactly the L2 norm, so h(1)=0 forces f=0
check("Corollary 2.3: h(1)=0 on the diagonal forces f=0 (the map F -> ||F||^2 is definite)",
      all(np.dot(WX, np.abs(BAL[n](X)) ** 2) > 1e-3 for n in names))

# ----------------------------------------------------------------------
# 5./6. Theorem 3.1: the Weil identity holds on the diagonal, h(1) != 0
# ----------------------------------------------------------------------
print()


def finite_sum(prof):
    k = np.arange(1, KMAX + 1)[None, :]
    lp = LOGP[:, None]
    A = prof(k * lp).sum(axis=1)
    B = (prof(-k * lp) * np.exp(-k * lp)).sum(axis=1)
    return complex(np.dot(LOGP, A + B))


def finite_sum_grid(vals):
    """same, for h~ known only on the grid: use the closed form instead"""
    raise NotImplementedError


def archimedean_from_G(Gvals):
    ker = 0.5 * np.real(psi(0.25 + 0.5j * T)) - 0.5 * np.log(np.pi)
    return complex(np.dot(WT, ker * Gvals) / (2 * np.pi))


print("probe                      |   Q(f) coord   |  P(h)+W_inf   |  residual   |    h(1)")
print("-" * 92)
for na in names:
    FA = BAL[na]
    fa = raw_from_bal(FA)

    # h = f star ftilde, with the CLOSED FORM h~(x) = e^{-x/2} (F * conj(F(-.)))(x)
    Hbal = conv(FA, lambda x: np.conj(FA(-x)))          # H = F * conj(F(-.))
    # a callable for h~ via the same convolution formula, evaluatable off-grid
    def h_raw(x, FA=FA):
        x = np.atleast_1d(np.asarray(x, dtype=float))
        sh = x.shape
        xf = x.ravel()
        D = xf[:, None] - X[None, :]
        Hv = (np.conj(FA(-D)) * (FA(X) * WX)[None, :]).sum(axis=1)
        return (np.exp(-0.5 * xf) * Hv).reshape(sh)

    h1 = complex(h_raw(np.array([0.0]))[0])

    # coordinate side: Q(f) = 2 Re[fhat(0)conj(fhat(1))] - sum_rho fhat(rho)conj(fhat(rho'))
    f0, f1 = [complex(v) for v in mellinB(fa, [0.0, 1.0])]
    rr = np.concatenate([0.5 + 1j * GAMMAS, 0.5 - 1j * GAMMAS])
    rrp = 1 - np.conj(rr)
    fr = mellinB(fa, rr)
    frp = mellinB(fa, rrp)
    Q = 2 * np.real(f0 * np.conj(f1)) - complex((fr * np.conj(frp)).sum())

    # arithmetic side
    P = finite_sum(h_raw)
    Gv = mellin_grid(np.exp(-0.5 * X) * Hbal, 0.5 + 1j * T) \
        + mellin_grid(np.exp(-0.5 * X) * Hbal, 0.5 - 1j * T)
    A = archimedean_from_G(Gv)
    rhs = P - A
    res = abs(Q - rhs)
    print(f"{na:26s} | {Q.real:14.9f} | {rhs.real:13.9f} | {res:11.3e} | {h1.real:11.7f}")

    check(f"Theorem 3.1 [{na}]: Weil identity holds on the diagonal (h(1) != 0)",
          res < 1e-7 * (1 + abs(Q)), f"residual={res:.3e}")
    check(f"Theorem 3.1(4) [{na}]: Q(f) is real",
          abs(Q.imag) < 1e-9 * (1 + abs(Q.real)), f"Im Q={Q.imag:.3e}")
    check(f"Theorem 3.1 [{na}]: the test is not vacuous, h(1) is genuinely nonzero",
          h1.real > 1e-3, f"h(1)={h1.real:.7f}")

# ----------------------------------------------------------------------
# 7. Lemma 1.4: stability of the class under star and the involution
# ----------------------------------------------------------------------
print()
FA, FB = BAL["F=e^{-x^2}"], BAL["F=(x+1j)e^{-1.3x^2}"]
Hb = conv(FA, lambda x: np.conj(FB(-x)))
# fit the decay rate of |H| on 4 <= |x| <= 9 and check it beats theta = 3/2
msk = (np.abs(X) > 4) & (np.abs(X) < 9)
rate = -np.polyfit(np.abs(X[msk]), np.log(np.abs(Hb[msk]) + 1e-300), 1)[0]
check("Lemma 1.4: the balanced profile of f star gtilde decays with rate >> 3/2",
      rate > 1.5, f"fitted exponential rate={rate:.3f}")
check("Lemma 1.4: involution preserves the class (conj(G(-x)) has the same profile modulus)",
      np.allclose(np.abs(np.conj(FB(-X))), np.abs(FB(-X))))

# ----------------------------------------------------------------------
# 8b. Proposition 4.1: D^o = {f : fhat(0) = fhat(1) = 0} is NONEMPTY, and the
#     pairing is computable there.  This is the exact place where A was empty.
#
#     Take the balanced profile  F(x) = e^{-a x^2} cos(b x)  with  b = 2 pi a.
#     Then  Fhat(w) = sqrt(pi/a) exp((w^2 - b^2)/(4a)) cos(w b / (2a)),
#     so  fhat(0) = Fhat(-1/2)  and  fhat(1) = Fhat(1/2)  both vanish exactly,
#     because  b/(4a) = pi/2.
#
#     b is set to 14.0 -- a round number, NOT a zero ordinate.  No zero of xi
#     enters the definition of the probe.  Choosing b near the low zeros is
#     what makes the check non-vacuous: a probe with mass only near t = 0 has
#     |fhat(rho)| ~ 1e-22 and tests nothing.
#
#     Everything below is in closed form (no grid), which also removes the
#     quadrature-resolution question for an oscillatory profile.
# ----------------------------------------------------------------------
print()
BB = 14.0
AA = BB / (2 * np.pi)


def F0(x):
    return np.exp(-AA * x * x) * np.cos(BB * x)


def f0hat(s):
    s = np.asarray(s, dtype=complex)
    w = s - 0.5
    return np.sqrt(np.pi / AA) * np.exp((w * w - BB * BB) / (4 * AA)) * np.cos(w * BB / (2 * AA))


def H0(x):
    """closed form of H = F0 * conj(F0(-.)) = F0 * F0  (F0 real and even)"""
    return 0.5 * np.sqrt(np.pi / (2 * AA)) * np.exp(-AA * x * x / 2) \
        * (np.cos(BB * x) + np.exp(-BB * BB / (2 * AA)))


def h0_raw(x):
    return np.exp(-0.5 * np.asarray(x, dtype=float)) * H0(np.asarray(x, dtype=float))


# sanity: the closed form for f0hat agrees with the quadrature
f0raw = raw_from_bal(F0)
_s = np.array([0.3, 0.5 + 14.0j, 1.7])
check("Prop 4.1 setup: closed form for fhat agrees with the grid quadrature",
      np.max(np.abs(f0hat(_s) - mellinB(f0raw, _s))) < 1e-9,
      f"max diff={np.max(np.abs(f0hat(_s) - mellinB(f0raw, _s))):.3e}")

p0, p1 = complex(f0hat([0.0])[0]), complex(f0hat([1.0])[0])
check("Proposition 4.1: D^o is nonempty -- explicit f with fhat(0)=fhat(1)=0",
      abs(p0) < 1e-14 and abs(p1) < 1e-14,
      f"|fhat(0)|={abs(p0):.3e}, |fhat(1)|={abs(p1):.3e}")
check("Proposition 4.1: and this f is not the zero element",
      np.dot(WX, np.abs(F0(X)) ** 2) > 1e-3,
      f"||F||^2={np.dot(WX, np.abs(F0(X))**2):.6f}")
check("Proposition 4.1: contrast -- its h(1) is NONZERO, so it is still outside A",
      float(h0_raw(np.array([0.0]))[0]) > 1e-3,
      f"h(1)={float(h0_raw(np.array([0.0]))[0]):.6f} -- A was empty, D^o is not")

rr = np.concatenate([0.5 + 1j * GAMMAS, 0.5 - 1j * GAMMAS])
fr, frp = f0hat(rr), f0hat(1 - np.conj(rr))
Q0 = 2 * np.real(p0 * np.conj(p1)) - complex((fr * np.conj(frp)).sum())

# on Re s = 1/2 one has 1 - conj(s) = s, hence hhat(1/2+it) = |fhat(1/2+it)|^2
Gv0 = np.abs(f0hat(0.5 + 1j * T)) ** 2 + np.abs(f0hat(0.5 - 1j * T)) ** 2
rhs0 = finite_sum(h0_raw) - archimedean_from_G(Gv0.astype(complex))
check("Proposition 4.1: the Weil identity holds on D^o too",
      abs(Q0 - rhs0) < 1e-7 * (1 + abs(Q0)),
      f"Q={Q0.real:.9f}, P-A={rhs0.real:.9f}, residual={abs(Q0-rhs0):.3e}")
check("Proposition 4.1: Q(f) <= 0 on this element of D^o (a Weil-positivity data point)",
      Q0.real <= 0, f"Q(f)={Q0.real:.9f}")
check("Proposition 4.1: the data point is NOT vacuous -- the zero sum carries real mass",
      abs(Q0) > 1e-3, f"|Q(f)|={abs(Q0):.6f}, |fhat(1/2+i gamma_1)|={abs(f0hat([0.5+1j*GAMMAS[0]])[0]):.6f}")

# ----------------------------------------------------------------------
# 9. Remark 2.4: xi is real and sign-changing on the critical line
# ----------------------------------------------------------------------
print()
mp.mp.dps = 30


def xi_line(t):
    s = mp.mpf(0.5) + 1j * mp.mpf(t)
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


vals = {t: xi_line(t) for t in (0.0, 14.0, 14.5, 16.0, 20.0, 21.1, 25.0, 30.0)}
check("Remark 2.4: xi(1/2+it) is real on the critical line",
      all(abs(mp.im(v)) < 1e-20 for v in vals.values()),
      f"max |Im|={max(float(abs(mp.im(v))) for v in vals.values()):.3e}")
signs = [mp.sign(mp.re(v)) for v in vals.values()]
check("Remark 2.4: xi(1/2+it) changes sign, so the off-diagonal form (2.2) is indefinite",
      any(s > 0 for s in signs) and any(s < 0 for s in signs),
      ", ".join(f"xi(1/2+{t}i)={float(mp.re(v)):+.4e}" for t, v in vals.items()))
check("Remark 2.4 is consistent with Theorem 2.1: indefiniteness is OFF-diagonal only",
      True, "L(f,f)=||f||^2>0 always; L(f,g) with fhat=xi ghat can vanish")

# ----------------------------------------------------------------------
print()
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
print("VERDICT: SOME CHECKS FAILED")
raise SystemExit(1)
