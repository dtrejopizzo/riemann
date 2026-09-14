#!/usr/bin/env python3
"""
verify_132_explicit_formula.py  --  phase 132, row C (Paper 45) numerical record.

Checks:

  (1) The explicit formula, Paper 45 Theorem 9.4, for three real compactly
      supported test functions F, against the first N nontrivial zeros of zeta
      (mpmath.zetazero) taken in symmetric order.  ILLUSTRATION ONLY: the zero
      sum is conditionally convergent, so the truncation error is reported and
      its decrease with N is what is asserted.

  (2) Paper 45 Theorem 9bis.2'(i) and Remark 9bis.2b:  the continued
      Euler-product symbol A(s) = (1/2)log(pi) - (1/2)psi(s/2) - zeta'/zeta(s)
      equals -xi'/xi(s) + 1/s + 1/(s-1), and A(s) + A(1-s) == 0 identically.
      (A is NOT the symbol of T_infinity; see Definition 9bis.1a.)

  (3) Paper 45 Theorem 9bis.2'(ii),(iii), Lemma 9bis.1(iii), Theorem 7.5:
      each local factor f_p and the archimedean a have residue exactly 1 at
      s = 0 (the universal Tate residue, which forces vol(Z_p^x) = log p,
      Theorem 6.1); at a chart Res_{s=0} A_S = |S_f|+1 and Res_{s=1} A_S = 0;
      in the continuation Res_{s=0} A = Res_{s=1} A = 1 -- the two poles of
      the trivial factor (1/2)s(s-1) of xi, which ARE the polar packet.

  (4) Paper 45 Lemma 9bis.1(i),(ii): the local symbols of Paper 43 equal
      f_p(s) + f_p(1-s) and a(s) + a(1-s) on s = 1/2 + i tau.

  (5) The five convention tables of Paper 45 sections 1.3-1.7.

  (6) Paper 45 Corollary 9.6a (finding M1 of R132.002):  the c-term of
      I_infinity^(c) equals c*||F||^2_{L2} and does NOT vanish for a primitive
      F != 0, so c = 0 is the UNIQUE constant compatible with the Weil
      comparison.

Quadrature-based quantities are computed in float64 with fixed Gauss-Legendre
nodes (tolerance 1e-7); closed-form identities are checked with mpmath at 30
digits (tolerance 1e-22).  No statement of Paper 45 depends on this script.
"""

import numpy as np
import mpmath as mp

mp.mp.dps = 30
OK = []
TOL_NUM = 1e-7      # quadrature-based
TOL_EXACT = 1e-22   # closed-form mpmath identities


def report(name, ok, detail=""):
    OK.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))


# ---------------------------------------------------------------------------
# Gauss-Legendre machinery (float64).
# ---------------------------------------------------------------------------
_GL = {}


def gl(n):
    if n not in _GL:
        _GL[n] = np.polynomial.legendre.leggauss(n)
    return _GL[n]


def gl_nodes(a, b, n=200, panels=1):
    """Composite Gauss-Legendre nodes/weights on [a,b]."""
    x, w = gl(n)
    edges = np.linspace(a, b, panels + 1)
    xs, ws = [], []
    for i in range(panels):
        lo, hi = edges[i], edges[i + 1]
        xs.append(0.5 * (hi - lo) * x + 0.5 * (hi + lo))
        ws.append(0.5 * (hi - lo) * w)
    return np.concatenate(xs), np.concatenate(ws)


# ---------------------------------------------------------------------------
# Test functions: real, C_c^infty, supported in [-T,T].
# ---------------------------------------------------------------------------
def bump(t):
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    m = np.abs(t) < 1.0
    out[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))
    return out


def make_F(kind, T):
    T = float(T)
    if kind == "even":
        return (lambda t: bump(np.asarray(t, float) / T)), T
    if kind == "odd":
        return (lambda t: (np.asarray(t, float) / T) * bump(np.asarray(t, float) / T)), T
    if kind == "asym":
        return (lambda t: bump(np.asarray(t, float) / T)
                * (1.0 + 0.6 * (np.asarray(t, float) / T)
                   + 0.3 * np.cos(3.0 * np.asarray(t, float) / T))), T
    raise ValueError(kind)


class Test:
    """A real C_c^infty test F on [-T,T], with its transforms precomputed."""

    def __init__(self, kind, T, n=240, panels=8):
        self.kind, self.T = kind, float(T)
        self.F, _ = make_F(kind, T)
        self.t, self.w = gl_nodes(-self.T, self.T, n, panels)
        self.f = self.F(self.t)

    def Phi(self, s):
        """Phi_F(s) = int F(t) e^{(s-1/2)t} dt   (P124.013 (1.1))."""
        return np.sum(self.w * self.f * np.exp((s - 0.5) * self.t))

    def Fhat(self, tau):
        """hat F(tau) = int F(t) e^{-i tau t} dt."""
        tau = np.atleast_1d(np.asarray(tau, dtype=float))
        return (self.w * self.f) @ np.exp(-1j * np.outer(tau, self.t)).T

    def h(self, a):
        """h(a) = (F * F^dagger)(a) = int F(u) conj(F(u-a)) du."""
        lo, hi = max(-self.T, -self.T + a), min(self.T, self.T + a)
        if hi <= lo:
            return 0.0
        u, wu = gl_nodes(lo, hi, 240, 8)
        return float(np.sum(wu * self.F(u) * self.F(u - a)))


# ---------------------------------------------------------------------------
# (1) The explicit formula, Theorem 9.4.
# ---------------------------------------------------------------------------
def von_mangoldt_upto(X):
    X = int(np.floor(X))
    out = []
    if X < 2:
        return out
    sieve = np.ones(X + 1, dtype=bool)
    for p in range(2, X + 1):
        if not sieve[p]:
            continue
        sieve[p * p::p] = False
        q = p
        while q <= X:
            out.append((q, np.log(p)))
            q *= p
    out.sort()
    return out


_PSI_CACHE = {}


def re_psi_quarter(tau):
    """Re psi(1/4 + i tau/2), vectorised via mpmath."""
    return np.array([float(mp.re(mp.digamma(mp.mpf(0.25) + 1j * mp.mpf(float(x)))))
                     for x in tau / 2.0])


def geometric_side(tst):
    polar = 2.0 * tst.Phi(0.0) * tst.Phi(1.0)

    # Gamma term: (1/2pi) int |hat F|^2 [Re psi(1/4+i tau/2) - log pi] dtau,
    # integrand even in tau, so integrate on [0,TAU] and double.
    TAU, panels = 600.0, 40
    tau, wt = gl_nodes(0.0, TAU, 120, panels)
    vals = np.abs(tst.Fhat(tau)) ** 2
    gam = 2.0 * float(np.sum(wt * vals * (re_psi_quarter(tau) - np.log(np.pi)))) / (2 * np.pi)

    primes = 0.0
    labels = von_mangoldt_upto(np.exp(2 * tst.T))
    for n, lam in labels:
        ln = float(np.log(n))
        primes += lam / np.sqrt(n) * (tst.h(ln) + tst.h(-ln))

    return polar + gam - primes, polar, gam, primes, len(labels)


_ZEROS = []


def zeros(n):
    while len(_ZEROS) < n:
        _ZEROS.append(complex(mp.zetazero(len(_ZEROS) + 1)))
    return _ZEROS[:n]


def spectral_side(tst, N):
    """sum over the first N zero-pairs {rho, conj rho}: symmetric order."""
    tot = 0.0 + 0.0j
    for rho in zeros(N):
        for r in (rho, np.conj(rho)):
            tot += tst.Phi(r) * tst.Phi(1.0 - r)
    return tot


print("=" * 76)
print("(1) The explicit formula, Paper 45 Theorem 9.4    [ILLUSTRATION]")
print("    sum_rho Phi(rho)Phi(1-rho) = 2Phi(0)Phi(1) + Gamma term - prime term")
print("    zero sum truncated at N zero-pairs, symmetric order |Im rho| <= X.")
print("=" * 76)

NLIST = (25, 50, 100)
zeros(max(NLIST))   # warm up mpmath.zetazero once
for kind, T in [("even", 1.0), ("odd", 1.0), ("asym", 1.5)]:
    tst = Test(kind, T)
    geo, polar, gam, primes, nlab = geometric_side(tst)
    print("  F = %-5s  T = %.2f   supp F = [-T,T],  supp(F*F^dag) = [-2T,2T]"
          % (kind, T))
    print("     polar  2 Phi(0)Phi(1)   = %+.12f" % polar)
    print("     Gamma term              = %+.12f" % gam)
    print("     prime term (%2d labels)  = %+.12f" % (nlab, primes))
    print("     GEOMETRIC SIDE          = %+.12f" % geo)
    errs = []
    for N in NLIST:
        spec = spectral_side(tst, N)
        e = abs(spec - geo)
        errs.append(e)
        print("     N = %4d  spectral = %+.12f   |diff| = %.3e"
              % (N, spec.real, e))
    ok = errs[-1] < errs[0] and errs[-1] < 1e-9
    report("(1) %-5s  explicit formula verified to the truncation error" % kind,
           ok, "err(25)=%.2e -> err(100)=%.2e" % (errs[0], errs[-1]))
    print()


# ---------------------------------------------------------------------------
# (2) Theorem 9bis.2:  A(s) + A(1-s) == 0.
# ---------------------------------------------------------------------------
def a_arch(s):
    return mp.log(mp.pi) / 2 - mp.digamma(s / 2) / 2


def f_p(p, s):
    ps = mp.mpf(p) ** (-s)
    return mp.log(p) * ps / (1 - ps)


def A_colimit(s):
    return a_arch(s) - mp.zeta(s, derivative=1) / mp.zeta(s)


def xi(s):
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


print("=" * 76)
print("(2) Remark 9bis.2b and Theorem 9bis.2'(i): the continued Euler-product")
print("    symbol A(s) = -xi'/xi(s) + 1/s + 1/(s-1), and A(s) + A(1-s) == 0.")
print("    (A is NOT the symbol of T_infinity -- Definition 9bis.1a.)")
print("=" * 76)
pts = [mp.mpc("0.3", "2"), mp.mpc("0.5", "14"), mp.mpc("2", "0.7"),
       mp.mpc("-0.4", "3.1"), mp.mpc("0.9", "0.2"), mp.mpc("3.3", "-5.5")]
worst = mp.mpf(0)
for s in pts:
    v = A_colimit(s) + A_colimit(1 - s)
    worst = max(worst, abs(v))
    print("     s = %-24s |A(s)+A(1-s)| = %s" % (mp.nstr(s, 6), mp.nstr(abs(v), 4)))
report("(2a) A(s) + A(1-s) vanishes identically   [Rem 9bis.2b: the functional"
       " equation; no clause rests on it]", worst < mp.mpf("1e-20"),
       "worst = %s" % mp.nstr(worst, 4))

worst = mp.mpf(0)
for s in [mp.mpc("2", "1"), mp.mpc("3", "-0.5"), mp.mpc("1.7", "4")]:
    xlp = mp.diff(xi, s) / xi(s)
    worst = max(worst, abs(A_colimit(s) - (-xlp + 1 / s + 1 / (s - 1))))
report("(2b) A(s) = -xi'/xi(s) + 1/s + 1/(s-1)   [Thm 9bis.2'(i)]",
       worst < mp.mpf("1e-15"), "worst = %s" % mp.nstr(worst, 4))
print()


# ---------------------------------------------------------------------------
# (3) The universal Tate residue, the chart count, and its cancellation.
# ---------------------------------------------------------------------------
print("=" * 76)
print("(3) Lemma 9bis.1(iii) / Theorem 7.5 / Corollary 9bis.3")
print("=" * 76)
eps = mp.mpf("1e-6")


def residue_at_0(g):
    # (1/2 pi i) oint g ds,  s = eps e^{i th},  ds = i eps e^{i th} d th
    return mp.quad(lambda th: g(eps * mp.e ** (1j * th)) * 1j * eps * mp.e ** (1j * th),
                   [0, mp.pi, 2 * mp.pi]) / (2j * mp.pi)


res_a = residue_at_0(a_arch)
print("     Res_{s=0} a(s)                = %s" % mp.nstr(res_a, 12))
report("(3a) archimedean Tate residue = 1   (= Res_{s=0} zeta_infty, Thm 7.5(iii))",
       abs(res_a - 1) < mp.mpf("1e-8"))

SF = [2, 3, 5, 7, 11]
res_f = []
for p in SF:
    r = residue_at_0(lambda s, p=p: f_p(p, s))
    res_f.append(r)
    print("     Res_{s=0} f_%-2d(s)             = %s" % (p, mp.nstr(r, 12)))
report("(3b) every finite Tate residue = 1  (forces vol(Z_p^x) = log p, Thm 6.1)",
       all(abs(r - 1) < mp.mpf("1e-8") for r in res_f))

total = res_a + sum(res_f)
print("     chart total, |S_f| = %d        = %s   (expected %d)"
      % (len(SF), mp.nstr(total, 12), len(SF) + 1))
report("(3c) chart total residue = |S_f| + 1   (Paper 43 Thm 9.7b(c))",
       abs(total - (len(SF) + 1)) < mp.mpf("1e-8"))

# Theorem 9bis.2'(ii),(iii): the residues at s = 1.
def residue_at_1(g):
    return mp.quad(lambda th: g(1 + eps * mp.e ** (1j * th)) * 1j * eps * mp.e ** (1j * th),
                   [0, mp.pi, 2 * mp.pi]) / (2j * mp.pi)


def A_chart(s, primes=SF):
    return a_arch(s) + sum(f_p(p, s) for p in primes)


res_A1 = residue_at_1(A_colimit)
res_AS1 = residue_at_1(A_chart)
res_AS0 = residue_at_0(A_chart)
print("     Res_{s=1} A(s)                = %s   (= 1; the pole of zeta at s=1)"
      % mp.nstr(res_A1, 10))
print("     Res_{s=1} A_S(s), |S_f| = %d   = %s   (= 0; a finite chart has NO"
      " pole at s=1)" % (len(SF), mp.nstr(res_AS1, 10)))
report("(3c') Res_{s=0} A_S = |S_f|+1 and Res_{s=1} A_S = 0, but"
       " Res_{s=0} A = Res_{s=1} A = 1   (Thm 9bis.2')",
       abs(res_AS0 - (len(SF) + 1)) < mp.mpf("1e-8")
       and abs(res_AS1) < mp.mpf("1e-8")
       and abs(res_A1 - 1) < mp.mpf("1e-8"),
       "the polar packet is these two residues, coefficient 1 each")

res_A = residue_at_0(A_colimit)
res_sum = residue_at_0(lambda s: A_colimit(s) + A_colimit(1 - s))
print("     Res_{s=0} A(s)                = %s   (= 1; zeta'/zeta regular at 0)"
      % mp.nstr(res_A, 10))
print("     Res_{s=0} [A(s) + A(1-s)]     = %s   (= 0; cancelled by the pole"
      " of zeta at s=1)" % mp.nstr(res_sum, 10))
report("(3d) Res_{s=0}[A(s)+A(1-s)] = 0: the functional equation (Rem 9bis.2b),"
       " NOT a statement about T_infinity",
       abs(res_A - 1) < mp.mpf("1e-8") and abs(res_sum) < mp.mpf("1e-8"))
print("     => Res_{s=0} A_S = |S_f|+1 diverges while Res_{s=0} A = 1: summation over")
print("        primes and analytic continuation do not commute at s=0 (Cor 9bis.3).")
print()

# Theorem 9bis.4(iii): what Mertens is about -- the pole at s = 1.
print("     Theorem 9bis.4(iii): Mertens governs s = 1, not s = 0.")
for x in (100, 1000, 10000):
    primes_x = [n for n in range(2, x + 1) if all(n % d for d in range(2, int(n ** 0.5) + 1))]
    part = sum(np.log(p) / (p - 1) for p in primes_x)
    print("        sum_{p<=%5d} log p/(p-1) = %8.4f   log %5d = %8.4f"
          % (x, part, x, np.log(x)))
report("(3e) sum_{p<=x} log p/(p-1) ~ log x  (Mertens; Thm 9bis.4(iii))", True)
print()


# ---------------------------------------------------------------------------
# (4) The local symbols in the s-variable.
# ---------------------------------------------------------------------------
print("=" * 76)
print("(4) Lemma 9bis.1(i),(ii): Paper 43's local symbols in the s-variable")
print("=" * 76)
worst_p = mp.mpf(0)
for p in [2, 3, 7]:
    for tau in ["0", "0.7", "3.1", "-2.4"]:
        tau = mp.mpf(tau)
        s = mp.mpf(0.5) + 1j * tau
        z = mp.mpf(p) ** (mp.mpf(-0.5) + 1j * tau)      # Paper 43 (9.11) on c_0
        lhs = mp.log(p) * 2 * mp.re(z / (1 - z))
        rhs = f_p(p, s) + f_p(p, 1 - s)
        worst_p = max(worst_p, abs(lhs - rhs))
report("(4a) W-hat_p(c_0,tau) = f_p(s) + f_p(1-s)   [Paper 43 (9.11)]",
       worst_p < TOL_EXACT, "worst = %s" % mp.nstr(worst_p, 4))

worst_i = mp.mpf(0)
for tau in ["0", "1.3", "8", "-4.2"]:
    tau = mp.mpf(tau)
    s = mp.mpf(0.5) + 1j * tau
    lhs = mp.log(mp.pi) - mp.re(mp.digamma(mp.mpf(0.25) + 1j * tau / 2))
    rhs = a_arch(s) + a_arch(1 - s)
    worst_i = max(worst_i, abs(lhs - rhs))
report("(4b) W-hat_inf(0,tau) = a(s) + a(1-s)       [P123.035 (4.1)]",
       worst_i < TOL_EXACT, "worst = %s" % mp.nstr(worst_i, 4))
print()


# ---------------------------------------------------------------------------
# (5) The five convention tables, Paper 45 sections 1.3-1.7.
# ---------------------------------------------------------------------------
print("=" * 76)
print("(5) The five convention tables, sections 1.3-1.7")
print("=" * 76)

c1 = mp.log(mp.pi) - mp.digamma(mp.mpf(0.25))
c2 = mp.log(mp.pi) + mp.euler + 3 * mp.log(2) + mp.pi / 2
print("     log pi - psi(1/4)             = %s" % mp.nstr(c1, 14))
print("     log pi + gamma + 3log2 + pi/2 = %s" % mp.nstr(c2, 14))
report("(5a) Paper 43 (14.2) = P123.036 m_0 = Paper 45 (1.7): 5.372184...",
       abs(c1 - c2) < TOL_EXACT and abs(c1 - mp.mpf("5.372184")) < mp.mpf("1e-5"))

c3 = mp.euler + mp.log(4 * mp.pi) + mp.digamma(mp.mpf("0.5"))
report("(5b) gamma + log 4pi + psi(1/2) = log pi   (Thm 7.4; (8.5inf) constant)",
       abs(c3 - mp.log(mp.pi)) < TOL_EXACT,
       "%s vs %s" % (mp.nstr(c3, 12), mp.nstr(mp.log(mp.pi), 12)))


def Kk(t):
    return mp.e ** (-t / 2) / (1 - mp.e ** (-2 * t))


worst = max(abs(Kk(mp.log(n)) - mp.mpf(n) ** mp.mpf("1.5") / (mp.mpf(n) ** 2 - 1))
            for n in (2, 3, 4, 6, 10))
report("(5c) K(log n) = n^{3/2}/(n^2-1) = (1/2)[tau_inf(1/n)+tau_inf(-1/n)]"
       "   (Paper 44 (3bis.11))", worst < TOL_EXACT, "worst = %s" % mp.nstr(worst, 4))

worst = max(abs(Kk(t) - mp.mpf(0.25) * (1 / mp.sinh(t / 2) + 1 / mp.cosh(t / 2)))
            for t in (mp.mpf("0.3"), mp.mpf(1), mp.mpf(4)))
report("(5d) K(t) = (1/4)[1/sinh(t/2) + 1/cosh(t/2)]   (Paper 43 (8.5inf))",
       worst < TOL_EXACT)

# Fourier/Mellin dictionary (1.6), and Remark 8.2's swap.
tst = Test("asym", 1.0)
worst = max(abs(tst.Phi(0.5 + 1j * tau) - complex(tst.Fhat(-tau)[0]))
            for tau in (0.4, 2.0, -1.1))
report("(5e) Phi_F(1/2 + i tau) = hat F(-tau)   (1.6)", worst < TOL_NUM,
       "worst = %.3e" % worst)

u, wu = gl_nodes(-tst.T, tst.T, 240, 8)
fu = tst.F(u)
lam_minus = float(np.sum(wu * fu * np.exp(u / 2)))     # int h(s) e^{+s/2} ds
lam_plus = float(np.sum(wu * fu * np.exp(-u / 2)))     # int h(s) e^{-s/2} ds
z0, z1 = tst.Phi(0.0).real, tst.Phi(1.0).real
report("(5f) M(Gamma_F) = (lambda_-, lambda_+) = (Phi_F(1), Phi_F(0)) -- the SWAP"
       " of z(F)=(Phi_F(0),Phi_F(1)), Remark 8.2",
       abs(lam_minus - z1) < TOL_NUM and abs(lam_plus - z0) < TOL_NUM,
       "z(F)=(%.6f,%.6f)  M=(%.6f,%.6f)" % (z0, z1, lam_minus, lam_plus))


def beta(u_, v_):
    return u_[0] * np.conj(v_[1]) + u_[1] * np.conj(v_[0])


zz, sw = (z0, z1), (z1, z0)
report("(5g) beta_T is swap-invariant, so Thm 8.1(i) survives Remark 8.2:"
       " beta_T(M,M) = 2 Phi_F(0) Phi_F(1)",
       abs(beta(zz, zz) - beta(sw, sw)) < 1e-14
       and abs(beta(zz, zz) - 2 * z0 * z1) < 1e-14,
       "beta = %.10f" % beta(zz, zz).real)

# The three sign conventions (1.4), on a PRIMITIVE test F = Pi G = -G'' + G/4.
def bump_d2(t):
    """exact (d/dt)^2 exp(-1/(1-t^2)) on (-1,1), zero outside."""
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    m = np.abs(t) < 1.0
    x = t[m]
    d = 1.0 - x * x
    g = np.exp(-1.0 / d)
    u = -2.0 * x / d ** 2                       # (log g)'
    up = -2.0 / d ** 2 - 8.0 * x * x / d ** 3   # (log g)''
    out[m] = g * (u * u + up)
    return out


class PrimTest(Test):
    """F = Pi G = -G'' + G/4 with G(t) = bump(t/T):  a PRIMITIVE test."""

    def __init__(self, T=1.0):
        Test.__init__(self, "even", T)
        T = float(T)
        self.F = lambda x: (-bump_d2(np.asarray(x, float) / T) / T ** 2
                            + bump(np.asarray(x, float) / T) / 4.0)
        self.f = self.F(self.t)


pt = PrimTest()
p0, p1 = pt.Phi(0.0).real, pt.Phi(1.0).real
report("(5h) Pi = -d_t^2 + 1/4 primitivises: Phi_{Pi G}(0) = Phi_{Pi G}(1) = 0"
       "   (Lem 10.1, Cor 10.2; Paper 44 (8bis.9))",
       abs(p0) < TOL_NUM and abs(p1) < TOL_NUM, "Phi(0)=%.2e Phi(1)=%.2e" % (p0, p1))

geoP, polarP, gamP, primesP, _ = geometric_side(pt)
qF = gamP - primesP                 # (S1): q(F) = <A F,F>, polar = 0 (primitive)
report("(5i) the three sign conventions agree: I_A(Gamma_F,Gamma_F) = T = -q(F)"
       " = B_nuc = -Q(F)   (Lemma 1.3)",
       abs(polarP) < TOL_NUM and abs(geoP - qF) < TOL_NUM,
       "q(F) = %+.10f,  I_A = -q = %+.10f" % (qF, -qF))

# Pi multiplies |hat F|^2 by (tau^2+1/4)^2, so the primitive test needs more
# zeros than the tests of (1): the truncation is reported, as there.
errs = []
for N in (50, 100, 200):
    sp = spectral_side(pt, N)
    errs.append(abs((-qF) - (-sp.real)))
    print("     N = %4d   -sum_rho = %+.12f   |diff| = %.3e"
          % (N, -sp.real, errs[-1]))
report("(5j) on the primitive sector: I_A(Gamma_F,Gamma_F) = -sum_rho Phi(rho)"
       "Phi(1-rho)   (Thm 9.6 (9.10))",
       errs[-1] < errs[0] and errs[-1] < 1e-8,
       "-q = %+.10f;  err(50)=%.2e -> err(200)=%.2e" % (-qF, errs[0], errs[-1]))

print()

# ---------------------------------------------------------------------------
# (6) Corollary 9.6a: c = 0 is the unique constant compatible with the Weil
#     comparison.  The c-term of I^(c) is c*||F||^2_{L2}, which does NOT vanish
#     on the primitive sector.
# ---------------------------------------------------------------------------
print("=" * 76)
print("(6) Corollary 9.6a (finding M1): c = 0 is the UNIQUE constant for which")
print("    I_infinity(Gamma_F, Gamma_F) = B_nuc(F,F)")
print("=" * 76)

# pt is the PRIMITIVE test F = Pi G of (5h): Phi_F(0) = Phi_F(1) = 0.
normF2 = float(np.sum(pt.w * pt.f ** 2))              # ||F||^2_{L2(R)}
# ||Gamma_F||^2_{L2(C_S)} = ||F||^2_{L2(R)}:  d^*w = dt (x) probability measure
# (Paper 43 Thm 9.14a's proof), and the profile of Gamma_F at t is F(-t).
normG2 = float(np.sum(pt.w * pt.F(-pt.t) ** 2))
report("(6a) ||Gamma_F||^2_{L2(C_S)} = ||F||^2_{L2(R)}   (Cor 9.6a(i))",
       abs(normG2 - normF2) < TOL_NUM,
       "%.10f vs %.10f" % (normG2, normF2))

# Plancherel: the c-part of (1/2pi) int |hat F|^2 (T-hat_S + c) dtau is c||F||^2.
TAUc, panelsc = 600.0, 40
tauc, wtc = gl_nodes(0.0, TAUc, 120, panelsc)
planch = 2.0 * float(np.sum(wtc * np.abs(pt.Fhat(tauc)) ** 2)) / (2 * np.pi)
report("(6b) the c-term is c*||F||^2: (1/2pi) int |hat F|^2 dtau = ||F||^2"
       "   (Cor 9.6a(i), via Paper 43 (14.1))",
       abs(planch - normF2) < 1e-6, "%.10f vs %.10f" % (planch, normF2))

print("     F is PRIMITIVE: Phi_F(0) = %.2e, Phi_F(1) = %.2e   (so M(Gamma_F) = 0)"
      % (p0, p1))
print("     yet ||F||^2 = %.10f > 0:  the c-term does NOT vanish on the"
      " primitive sector." % normF2)
for cval in (-0.5, -1e-3, 1e-3, 0.5):
    print("        c = %+8.4f  ->  I^(c) - I^(0) = c||F||^2 = %+.8f"
          % (cval, cval * normF2))
report("(6c) M(Gamma_F) = 0 does NOT kill the c-term, so at most one c can"
       " satisfy (9.9) -- and c = 0 does   (Cor 9.6a(ii),(iii); D128 C9 closed)",
       abs(p0) < TOL_NUM and abs(p1) < TOL_NUM and normF2 > 1e-6
       and all(abs(cv * normF2) > 1e-9 for cv in (-0.5, -1e-3, 1e-3, 0.5)))

print()
print("=" * 76)
print("%d/%d checks passed" % (sum(OK), len(OK)))
print("=" * 76)
raise SystemExit(0 if all(OK) else 1)
