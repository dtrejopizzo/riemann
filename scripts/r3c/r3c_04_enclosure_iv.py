"""R155.026 round 3c, HARDENED (amended 2026-09-22 per R155_028 §2):
a genuinely rigorous enclosure of  w11 = W_T[F*]  at  T = log 2,
for the ARCHIVED coefficient vector of F* read back from scripts/r3c/r3c_02.json.

Nothing is recomputed from arch_core: the archived vector `a` is the data of the theorem.
Every arithmetic step below is mpmath interval arithmetic (mp.iv) or carries a proved bound.
There is NO error budget: the EPS = 1e-9 slack of r3c_02_enclosure.py is gone.

Levy form (Paper 47 thm:A + thm:S(iii)), exact for any F in L^2(-T,T):
  W_T[F] = 2A(F)B(F) + C0*c(0) + int_0^{2T}(c(0)-c(u))K(u)du + c(0)*Ktail(2T)
           - sum_{n < e^{2T}} v_n c(log n),   K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)).

Structure of the proof carried out by this script.
 (1) F*(Tx) = p(x)/sqrt(T) with p(x) = sum_k a_k sqrt((2k+1)/2) P_k(x); the integer
     coefficients of the Legendre polynomials P_k are exact, the a_k are exact decimals,
     so p has interval coefficients of width ~1e-58.  Substituting u = T s,
        c(Ts) = q(s) = int_{-1+s}^{1} p(x) p(x-s) dx,
     which is computed here as an EXACT polynomial identity (binomial expansion +
     term-by-term integration) in interval coefficients.  q has degree <= 35.
 (2) G(s) := q(0) - q(s) >= 0 on [0,2] (Cauchy-Schwarz) and G(0) = 0, so G(s) <= C1 s
     with C1 = sum |coefficients of G' in the exact Chebyshev basis on [0,2]| >= sup |G'|.
 (3) Singular end [0,delta]:  K(u) <= 1/u + 1/2 (sinh x >= x, 1/(2cosh) <= 1/2), hence
        0 <= T int_0^delta G(s)K(Ts) ds <= C1 (delta + T delta^2/4),  delta = 1e-6.
 (4) Body [delta,2]: K_s(u) = 1/(2 sinh(u/2)) is CONVEX on (0,inf)
     ((1/sinh)'' = (cosh^2+1)/sinh^3 > 0) and K_c(u) = 1/(2 cosh(u/2)) is CONCAVE for
     u/2 < arccosh(sqrt 2) = 0.8814 (sech'' = sech(1-2 sech^2)), and 2T/2 = 0.693 < 0.8814.
     On each panel we therefore sandwich K between two AFFINE functions of s
     (tangent at the midpoint / chord at the endpoints, one way round for the convex
     summand and the other for the concave one).  Since G >= 0, the panel integral is
     enclosed by integrating G against those two affine functions, and int G and int sG
     over a panel are evaluated EXACTLY from the interval antiderivatives of q.
     No derivative bound on G and no quadrature rule is used.
 (5) Ktail(2T) = log coth(T/2) + pi - 2 arctan(e^T) in intervals;
     C0 = psi(1/4) - log pi = -gamma - 3 log 2 - pi/2 - log pi in intervals;
     the atoms v_2 q(log2/T), v_3 q(log3/T) in intervals;
     the pole defect |2 A(F*) B(F*)| <= 2|A||B| with A, B themselves enclosed by exact
     interval integration of the polynomial p against the entire functions e^{+-t/2}
     (Taylor series with a proved tail bound).
"""
import json, os, time
from fractions import Fraction
from math import comb
from mpmath import iv, mp

t0 = time.time()
iv.dps = 60
mp.dps = 80
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- 0. archived data
arch = json.load(open(os.path.join(HERE, 'r3c_02.json')))
a = arch['coef']                      # THE archived coefficient vector of F*
N = len(a)
assert N == 18, N
A_ = [iv.mpf(repr(x)) for x in a]     # exact decimal -> thin interval

T = iv.log(iv.mpf(2))                 # T = log 2
TWO = iv.mpf(2)

def ivsum(xs):
    s = iv.mpf(0)
    for x in xs: s = s + x
    return s

# ---------------------------------------------------------------- 1. p(x) and q(s)
# exact integer/rational Legendre coefficients
def legendre_coeffs(n):
    # P_n(x) = sum_m c_m x^m, exact Fractions
    P0 = [Fraction(1)]
    if n == 0: return P0
    P1 = [Fraction(0), Fraction(1)]
    if n == 1: return P1
    for k in range(1, n):
        nxt = [Fraction(0)]*(k+2)
        for i, ci in enumerate(P1):
            nxt[i+1] += Fraction(2*k+1, k+1)*ci
        for i, ci in enumerate(P0):
            nxt[i] -= Fraction(k, k+1)*ci
        P0, P1 = P1, nxt
    return P1

pc = [iv.mpf(0)]*N                                   # coefficients of p in x
for k in range(N):
    sc = A_[k]*iv.sqrt(iv.mpf(2*k+1)/iv.mpf(2))
    for m, cm in enumerate(legendre_coeffs(k)):
        pc[m] = pc[m] + sc*iv.mpf(cm.numerator)/iv.mpf(cm.denominator)

# p(x-s) = sum_{m,j} A2[m][j] x^m s^j
A2 = [[iv.mpf(0) for _ in range(N)] for _ in range(N)]
for k in range(N):
    for m in range(k+1):
        j = k-m
        term = pc[k]*iv.mpf(comb(k, m))
        if j % 2: term = -term
        A2[m][j] = A2[m][j] + term

# R[i][j] = coefficient of x^i s^j in p(x) p(x-s)
DX = 2*N-1
R = [[iv.mpf(0) for _ in range(N)] for _ in range(DX)]
for i in range(N):
    if pc[i] == 0: pass
    for m in range(N):
        for j in range(N):
            v = A2[m][j]
            if v == 0: continue
            R[i+m][j] = R[i+m][j] + pc[i]*v

# q(s) = sum_{i,j} R[i][j] s^j (1 - (s-1)^{i+1})/(i+1)
QD = (DX-1) + N + DX          # generous upper degree
q = [iv.mpf(0) for _ in range(QD+1)]
for i in range(DX):
    inv = iv.mpf(1)/iv.mpf(i+1)
    for j in range(N):
        Rij = R[i][j]
        if Rij == 0: continue
        base = Rij*inv
        q[j] = q[j] + base
        for n in range(i+2):
            t = base*iv.mpf(comb(i+1, n))
            if (i+1-n) % 2: t = -t
            q[j+n] = q[j+n] - t
# true degree <= 2N-1 = 35: check the tail contains 0 and is negligible
tailmax = max(max(abs(q[k].a), abs(q[k].b)) for k in range(36, QD+1))
assert tailmax < mp.mpf('1e-30'), tailmax
DEG = 35

c0 = q[0]                                            # c(0) = ||F*||^2
# G(s) = q(0) - q(s):  G_k = -q_k for k>=1, G_0 = 0
Gp = [iv.mpf(0)] + [-q[k] for k in range(1, DEG+1)]
# G(0) = 0 and G >= 0, so G(s) <= C1 s with C1 = sup_[0,2] |G'| (coefficient bound)
# rigorous sup_[0,2] |G'| via the EXACT Chebyshev expansion of G on [0,2] (|T_k| <= 1).
def to_cheb(mono):
    """monomial coefficients in s on [0,2]  ->  Chebyshev coefficients in y = s-1."""
    n = len(mono)-1
    sh = [iv.mpf(0)]*(n+1)                       # G(1+y) = sum sh[m] y^m
    for k in range(n+1):
        if mono[k] == 0: continue
        for m in range(k+1):
            sh[m] = sh[m] + mono[k]*iv.mpf(comb(k, m))
    ch = [iv.mpf(0)]*(n+1)
    for m in range(n+1):
        if sh[m] == 0: continue
        for j in range(m//2+1):
            kk = m-2*j
            f = iv.mpf(comb(m, j))/iv.mpf(2)**m
            if kk > 0: f = f*iv.mpf(2)
            ch[kk] = ch[kk] + sh[m]*f
    return ch
def chebder(ch):
    n = len(ch)-1
    d = [iv.mpf(0)]*(n+2)
    for k in range(n, 0, -1):
        d[k-1] = d[k+1] + iv.mpf(2*k)*ch[k]
    d[0] = d[0]/iv.mpf(2)
    return d[:n]
C2 = ivsum([abs(x) for x in chebder(to_cheb(Gp))])   # G1 >= sup|G'|; G(s) <= G1 s

# interval antiderivatives:  Gint = int_0^s G,  Hint = int_0^s t G(t) dt
Gint = [iv.mpf(0)]*(DEG+2)
Hint = [iv.mpf(0)]*(DEG+3)
for k in range(DEG+1):
    Gint[k+1] = Gp[k]/iv.mpf(k+1)
    Hint[k+2] = Gp[k]/iv.mpf(k+2)

def horner(co, x):
    r = co[-1]
    for k in range(len(co)-2, -1, -1):
        r = r*x + co[k]
    return r

# ---------------------------------------------------------------- 2. kernel pieces
half = iv.mpf(1)/iv.mpf(2)
def Ks(u):  return half/iv.sinh(u*half) if hasattr(iv, 'sinh') else iv.mpf(1)/(iv.exp(u*half) - iv.exp(-u*half))
def Kc(u):  return iv.mpf(1)/(iv.exp(u*half) + iv.exp(-u*half))
def Ks_(u):
    e, f = iv.exp(u*half), iv.exp(-u*half)
    sh, ch = (e-f)*half, (e+f)*half
    return -ch/(iv.mpf(4)*sh*sh)
def Kc_(u):
    e, f = iv.exp(u*half), iv.exp(-u*half)
    sh, ch = (e-f)*half, (e+f)*half
    return -sh/(iv.mpf(4)*ch*ch)
def Ksv(u):
    e, f = iv.exp(u*half), iv.exp(-u*half)
    return iv.mpf(1)/(e-f)

# ---------------------------------------------------------------- 3. the body integral
DELTA = iv.mpf('1e-6')
M = int(os.environ.get('R3C_PANELS', 8000))
Lg = iv.log(TWO/DELTA)
lo = C2*iv.mpf(0)                       # singular-end lower bound is 0 (integrand >= 0)
hi_sing = C2*(DELTA + T*DELTA**2/iv.mpf(4))

edges = [DELTA*iv.exp(Lg*iv.mpf(i)/iv.mpf(M)) for i in range(M+1)]
edges[-1] = TWO
Gv = [horner(Gint, e) for e in edges]
Hv = [horner(Hint, e) for e in edges]
Kse = [Ksv(T*e) for e in edges]
Kce = [Kc(T*e) for e in edges]

I_lo = iv.mpf(0); I_hi = iv.mpf(0)
for i in range(M):
    al, be = edges[i], edges[i+1]
    h = be - al
    m = (al+be)*half
    dG = Gv[i+1] - Gv[i]
    dH = Hv[i+1] - Hv[i]
    # convex summand K_s: tangent at m (lower), chord (upper); in the variable s
    fs_m = Ksv(T*m); fs_m_ = T*Ks_(T*m)
    s_lo0, s_lo1 = fs_m - fs_m_*m, fs_m_
    s_hi1 = (Kse[i+1] - Kse[i])/h; s_hi0 = Kse[i] - s_hi1*al
    # concave summand K_c: chord (lower), tangent at m (upper)
    c_lo1 = (Kce[i+1] - Kce[i])/h; c_lo0 = Kce[i] - c_lo1*al
    fc_m = Kc(T*m); fc_m_ = T*Kc_(T*m)
    c_hi0, c_hi1 = fc_m - fc_m_*m, fc_m_
    I_lo = I_lo + (s_lo0 + c_lo0)*dG + (s_lo1 + c_lo1)*dH
    I_hi = I_hi + (s_hi0 + c_hi0)*dG + (s_hi1 + c_hi1)*dH
I_lo = T*I_lo
I_hi = T*I_hi + hi_sing
INT = iv.mpf([I_lo.a, I_hi.b])

# ---------------------------------------------------------------- 4. the finite terms
def ivatan(z):
    """arctan on (0,1) by its alternating Taylor series; remainder <= first omitted term."""
    s_ = iv.mpf(0); zp = z
    NA = 200
    for n in range(NA):
        s_ = s_ + (zp/iv.mpf(2*n+1) if n % 2 == 0 else -zp/iv.mpf(2*n+1))
        zp = zp*z*z
    tl = abs(zp)/iv.mpf(2*NA+1)
    return s_ + iv.mpf([-tl.b, tl.b])

gamma_ = iv.mpf(mp.nstr(mp.euler, 60)) + iv.mpf([-1e-55, 1e-55])
pi_ = iv.pi
C0 = -gamma_ - iv.mpf(3)*iv.log(iv.mpf(2)) - pi_/iv.mpf(2) - iv.log(pi_)
eT = iv.exp(T)
# pi - 2 arctan(e^T) = 2 arctan(e^{-T});  log coth(T/2) = log((e^T+1)/(e^T-1))
Ktail = iv.log((eT + iv.mpf(1))/(eT - iv.mpf(1))) + iv.mpf(2)*ivatan(iv.mpf(1)/eT)

l2, l3 = iv.log(iv.mpf(2)), iv.log(iv.mpf(3))
v2 = iv.mpf(2)*l2/iv.sqrt(iv.mpf(2)); v3 = iv.mpf(2)*l3/iv.sqrt(iv.mpf(3))
qs = lambda s: horner(q[:DEG+1], s)
prim = -(v2*qs(l2/T) + v3*qs(l3/T))          # N_T = {2,3}: log 4 = 2T excluded, q(2)=0

# A(F*), B(F*) by exact interval integration of p against e^{+-Tx/2}
def mom(sgn):
    # int_{-1}^{1} p(x) e^{sgn*T*x/2} dx  = sum_k pc[k] * int x^k e^{a x} dx, a = sgn*T/2
    aa = T*half if sgn > 0 else -T*half
    tot = iv.mpf(0)
    NT = 90
    for k in range(N):
        # int_{-1}^1 x^k e^{a x} dx = sum_{n>=0} a^n/n! * int x^{k+n} = sum_{n: k+n even} a^n/n! * 2/(k+n+1)
        ssum = iv.mpf(0); term = iv.mpf(1)
        for n in range(NT):
            if (k+n) % 2 == 0:
                ssum = ssum + term*iv.mpf(2)/iv.mpf(k+n+1)
            term = term*aa/iv.mpf(n+1)
        # tail: |sum_{n>=NT}| <= 2 * |a|^NT/NT! * e^{|a|}
        tl = abs(term)*iv.mpf(2)*iv.exp(abs(aa))
        ssum = ssum + iv.mpf([-tl.b, tl.b])
        tot = tot + pc[k]*ssum
    return tot*iv.sqrt(T)       # dt = T dx and F = p/sqrt(T)
Aq, Bq = mom(+1), mom(-1)
polebound = iv.mpf(2)*abs(Aq)*abs(Bq)
pole = iv.mpf([-polebound.b, polebound.b])

W = pole + C0*c0 + INT + c0*Ktail + prim
rt = time.time()-t0
fmt = lambda z: '[%.10f, %.10f]' % (float(z.a), float(z.b))
print('c(0)           =', fmt(c0))
print('C1 (G<=C1 s)  = %.4f    panels M = %d   delta = 1e-6' % (float(C2.b), M))
print('|A|,|B|        <= %.2e, %.2e   |pole| <= %.2e' % (float(abs(Aq).b), float(abs(Bq).b), float(polebound.b)))
print('C0             =', fmt(C0))
print('Ktail(2T)      =', fmt(Ktail))
print('prime atoms    =', fmt(prim))
print('Levy integral  =', fmt(INT), ' width %.2e' % (float(INT.b)-float(INT.a)))
print('w11            =', fmt(W), ' width %.2e' % (float(W.b)-float(W.a)))
print('unit-norm w11  =', fmt(W/c0))
print('VERDICT: w11 > 0 rigorously:', bool(W.a > 0))
json.dump(dict(T=float(T.a), N=N, source='r3c_02.json:coef', method='mpmath mp.iv, dps=60',
               panels=M, delta=1e-6, C2=float(C2.b), deg_c=DEG,
               c0=[float(c0.a), float(c0.b)], C0=[float(C0.a), float(C0.b)],
               Ktail=[float(Ktail.a), float(Ktail.b)], prim=[float(prim.a), float(prim.b)],
               pole_bound=float(polebound.b),
               I=[float(INT.a), float(INT.b)], w11=[float(W.a), float(W.b)],
               runtime_s=rt),
          open(os.path.join(HERE, 'r3c_04_enclosure_iv.json'), 'w'), indent=1)
print('runtime %.1fs' % rt)
