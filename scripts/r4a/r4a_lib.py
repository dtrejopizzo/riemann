"""Interval-arithmetic enclosure of the Levy/Weil form W_T[F] for an explicit
polynomial F given by its coefficients in the orthonormal Legendre basis of (-T,T).

This is r3c_04_enclosure_iv.py refactored so that the expensive part -- the affine
sandwich of K over the panels -- is done ONCE, as two linear functionals L_lo, L_hi
on the monomial coefficients of G(s) = c(0) - c(Ts):

      T * int_delta^2 G(s) K(Ts) ds  in  [ <L_lo, G>, <L_hi, G> ]        (*)

valid for EVERY G >= 0 on [delta,2] (which holds for every autocorrelation, by
Cauchy-Schwarz), because the panelwise affine bounds K_lo <= K <= K_hi are
independent of G and G >= 0.  Hence the matrix of the form can be enclosed by
polarisation at the cost of one 36-dimensional dot product per evaluation.

All other steps are those of r3c_04_enclosure_iv.py, unchanged in substance:
exact Legendre/Fraction algebra for p, exact polynomial autocorrelation q,
G(s) <= G1 s from the exact Chebyshev derivative bound, K <= 1/u + 1/2 at the
singular end, exact closed forms for C0 and Ktail, interval prime atoms, and the
pole defect PAID FOR (not assumed zero).
"""
import os
from fractions import Fraction
from math import comb
from mpmath import iv, mp

iv.dps = 60
mp.dps = 80


def legendre_coeffs(n):
    P0 = [Fraction(1)]
    if n == 0: return P0
    P1 = [Fraction(0), Fraction(1)]
    if n == 1: return P1
    for k in range(1, n):
        nxt = [Fraction(0)]*(k+2)
        for i, ci in enumerate(P1): nxt[i+1] += Fraction(2*k+1, k+1)*ci
        for i, ci in enumerate(P0): nxt[i]   -= Fraction(k, k+1)*ci
        P0, P1 = P1, nxt
    return P1


def horner(co, x):
    r = co[-1]
    for k in range(len(co)-2, -1, -1): r = r*x + co[k]
    return r


def to_cheb(mono):
    n = len(mono)-1
    sh = [iv.mpf(0)]*(n+1)
    for k in range(n+1):
        if mono[k] == 0: continue
        for m in range(k+1): sh[m] = sh[m] + mono[k]*iv.mpf(comb(k, m))
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
    for k in range(n, 0, -1): d[k-1] = d[k+1] + iv.mpf(2*k)*ch[k]
    d[0] = d[0]/iv.mpf(2)
    return d[:n]


class LevyForm(object):
    """W_T[.] enclosures on span of Legendre basis of degree < N, at fixed T."""

    def __init__(self, T_str, N, panels=8000, delta='1e-6'):
        self.N = N
        self.T = iv.mpf(T_str) if isinstance(T_str, str) else T_str
        T = self.T
        self.DEG = 2*N-1
        self.LEG = [legendre_coeffs(k) for k in range(N)]
        self.half = iv.mpf(1)/iv.mpf(2)
        self.DELTA = iv.mpf(delta)
        self.M = panels
        self._panels()
        self._constants()

    # ---------------- kernel pieces
    def _Ksv(self, u):
        e, f = iv.exp(u*self.half), iv.exp(-u*self.half)
        return iv.mpf(1)/(e-f)

    def _Kc(self, u):
        return iv.mpf(1)/(iv.exp(u*self.half) + iv.exp(-u*self.half))

    def _Ks_(self, u):
        e, f = iv.exp(u*self.half), iv.exp(-u*self.half)
        sh, ch = (e-f)*self.half, (e+f)*self.half
        return -ch/(iv.mpf(4)*sh*sh)

    def _Kc_(self, u):
        e, f = iv.exp(u*self.half), iv.exp(-u*self.half)
        sh, ch = (e-f)*self.half, (e+f)*self.half
        return -sh/(iv.mpf(4)*ch*ch)

    # ---------------- ONE-TIME: the two linear functionals of (*)
    def _panels(self):
        T, M, D = self.T, self.M, self.DELTA
        nk = self.DEG + 1
        self.L_lo = [iv.mpf(0)]*nk
        self.L_hi = [iv.mpf(0)]*nk
        Lg = iv.log(iv.mpf(2)/D)
        edges = [D*iv.exp(Lg*iv.mpf(i)/iv.mpf(M)) for i in range(M+1)]
        edges[-1] = iv.mpf(2)
        Kse = [self._Ksv(T*e) for e in edges]
        Kce = [self._Kc(T*e) for e in edges]
        # powers alpha^{k+1}, beta^{k+1}, and alpha^{k+2}, beta^{k+2}
        for i in range(M):
            al, be = edges[i], edges[i+1]
            h = be - al
            m = (al+be)*self.half
            fs_m, fs_d = self._Ksv(T*m), T*self._Ks_(T*m)
            s_lo0, s_lo1 = fs_m - fs_d*m, fs_d                    # convex: tangent below
            s_hi1 = (Kse[i+1]-Kse[i])/h; s_hi0 = Kse[i] - s_hi1*al  # chord above
            c_lo1 = (Kce[i+1]-Kce[i])/h; c_lo0 = Kce[i] - c_lo1*al  # concave: chord below
            fc_m, fc_d = self._Kc(T*m), T*self._Kc_(T*m)
            c_hi0, c_hi1 = fc_m - fc_d*m, fc_d                    # tangent above
            a0, a1 = s_lo0 + c_lo0, s_lo1 + c_lo1
            b0, b1 = s_hi0 + c_hi0, s_hi1 + c_hi1
            ap, bp = al, be                # alpha^{k+1}, beta^{k+1} running
            for k in range(nk):
                ap = ap*al if k else al
                bp = bp*be if k else be
                m0 = (bp - ap)/iv.mpf(k+1)            # int_al^be s^k ds
                m1 = (bp*be - ap*al)/iv.mpf(k+2)      # int_al^be s^{k+1} ds
                self.L_lo[k] = self.L_lo[k] + a0*m0 + a1*m1
                self.L_hi[k] = self.L_hi[k] + b0*m0 + b1*m1
        for k in range(nk):
            self.L_lo[k] = self.L_lo[k]*T
            self.L_hi[k] = self.L_hi[k]*T

    def _constants(self):
        T = self.T
        gamma_ = iv.mpf(mp.nstr(mp.euler, 60)) + iv.mpf([-1e-55, 1e-55])
        self.C0 = -gamma_ - iv.mpf(3)*iv.log(iv.mpf(2)) - iv.pi/iv.mpf(2) - iv.log(iv.pi)
        eT = iv.exp(T)
        self.Ktail = iv.log((eT+iv.mpf(1))/(eT-iv.mpf(1))) + iv.mpf(2)*self._atan(iv.mpf(1)/eT)
        # prime atoms n with log n < 2T
        self.atoms = []
        import math
        nmax = int(math.exp(2*float(T.b)))+2
        lam = {}
        for pr in range(2, nmax+1):
            if all(pr % d for d in range(2, int(pr**0.5)+1)):
                qq = pr
                while qq <= nmax:
                    lam[qq] = pr; qq *= pr
        for n in sorted(lam):
            ln = iv.log(iv.mpf(n))
            if ln.b < (iv.mpf(2)*T).a:
                v = iv.mpf(2)*iv.log(iv.mpf(lam[n]))/iv.sqrt(iv.mpf(n))
                self.atoms.append((n, v, ln/T))

    @staticmethod
    def _atan(z):
        s_ = iv.mpf(0); zp = z
        NA = 200
        for n in range(NA):
            s_ = s_ + (zp/iv.mpf(2*n+1) if n % 2 == 0 else -zp/iv.mpf(2*n+1))
            zp = zp*z*z
        tl = abs(zp)/iv.mpf(2*NA+1)
        return s_ + iv.mpf([-tl.b, tl.b])

    # ---------------- per-function
    def pcoef(self, a):
        """a = list of exact decimals (strings or floats) -> interval coeffs of p(x)."""
        N = self.N
        A_ = [iv.mpf(repr(x)) if not isinstance(x, str) else iv.mpf(x) for x in a]
        pc = [iv.mpf(0)]*N
        for k in range(N):
            sc = A_[k]*iv.sqrt(iv.mpf(2*k+1)/iv.mpf(2))
            for m, cm in enumerate(self.LEG[k]):
                pc[m] = pc[m] + sc*iv.mpf(cm.numerator)/iv.mpf(cm.denominator)
        return pc

    def autocorr(self, pc):
        """exact interval polynomial q(s) = int_{-1+s}^1 p(x)p(x-s)dx, deg <= 2N-1."""
        N = self.N
        A2 = [[iv.mpf(0) for _ in range(N)] for _ in range(N)]
        for k in range(N):
            for m in range(k+1):
                j = k-m
                term = pc[k]*iv.mpf(comb(k, m))
                if j % 2: term = -term
                A2[m][j] = A2[m][j] + term
        DX = 2*N-1
        R = [[iv.mpf(0) for _ in range(N)] for _ in range(DX)]
        for i in range(N):
            pi_ = pc[i]
            for m in range(N):
                row = A2[m]
                for j in range(N):
                    v = row[j]
                    if v == 0: continue
                    R[i+m][j] = R[i+m][j] + pi_*v
        QD = (DX-1) + N + DX
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
        tail = max(max(abs(q[k].a), abs(q[k].b)) for k in range(2*N, QD+1))
        assert tail < mp.mpf('1e-25'), tail
        return q[:2*N]

    def moments(self, pc):
        """A(F), B(F) as intervals (exact series with proved factorial tail)."""
        T = self.T
        out = []
        for sgn in (+1, -1):
            aa = T*self.half if sgn > 0 else -T*self.half
            tot = iv.mpf(0)
            NT = 90
            for k in range(self.N):
                ssum = iv.mpf(0); term = iv.mpf(1)
                for n in range(NT):
                    if (k+n) % 2 == 0: ssum = ssum + term*iv.mpf(2)/iv.mpf(k+n+1)
                    term = term*aa/iv.mpf(n+1)
                tl = abs(term)*iv.mpf(2)*iv.exp(abs(aa))
                tot = tot + pc[k]*(ssum + iv.mpf([-tl.b, tl.b]))
            out.append(tot*iv.sqrt(T))
        return out

    def W(self, a):
        """rigorous two-sided enclosure of W_T[F], F = sum a_k phi_k."""
        T = self.T
        pc = self.pcoef(a)
        q = self.autocorr(pc)
        DEG = len(q)-1
        c0 = q[0]
        G = [iv.mpf(0)] + [-q[k] for k in range(1, DEG+1)]
        # body, via the precomputed functionals (valid because G >= 0)
        lo = iv.mpf(0); hi = iv.mpf(0)
        for k in range(DEG+1):
            if G[k] == 0: continue
            lo = lo + self.L_lo[k]*G[k]
            hi = hi + self.L_hi[k]*G[k]
        # singular end [0,delta]: 0 <= T int <= G1 (delta + T delta^2/4)
        G1 = iv.mpf(0)
        for x in chebder(to_cheb(G)): G1 = G1 + abs(x)
        hi = hi + G1*(self.DELTA + T*self.DELTA**2/iv.mpf(4))
        INT = iv.mpf([lo.a, hi.b])
        prim = iv.mpf(0)
        for n, v, sn in self.atoms:
            prim = prim - v*horner(q, sn)
        Aq, Bq = self.moments(pc)
        pb = iv.mpf(2)*abs(Aq)*abs(Bq)
        pole = iv.mpf([-pb.b, pb.b])
        return pole + self.C0*c0 + INT + c0*self.Ktail + prim, dict(
            c0=c0, INT=INT, prim=prim, G1=G1, pole=pb)


# ---------------- interval linear algebra
def ivmat_scale(Mx, s):
    return [[x*s for x in row] for row in Mx]


def cholesky_pd(Mx, mu):
    """True if the interval symmetric matrix Mx - mu*I is certainly positive definite
    (rigorous interval Cholesky: success => every real matrix in Mx - mu I is PD)."""
    n = len(Mx)
    L = [[iv.mpf(0)]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            s = Mx[i][j] - (mu if i == j else iv.mpf(0))
            for k in range(j):
                s = s - L[i][k]*L[j][k]
            if i == j:
                if not (s.a > 0): return False
                L[i][i] = iv.sqrt(s)
            else:
                L[i][j] = s/L[j][j]
    return True


def lam_min_lower(Mx, lo=0.0, hi=1.0, iters=40):
    """rigorous lower bound on lambda_min of every real symmetric matrix in Mx."""
    if not cholesky_pd(Mx, iv.mpf(0)): return None
    a, b = lo, hi
    for _ in range(iters):
        m = 0.5*(a+b)
        if cholesky_pd(Mx, iv.mpf(repr(m))): a = m
        else: b = m
    return a
