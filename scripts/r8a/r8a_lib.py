"""R155 round 8a: rigorous (mpmath interval) pieces for the negative index of the archimedean
form A_inf on the primitive subspace P_T, per parity sector.

Everything here is interval arithmetic (mpmath.iv, dps = IVDPS); every truncation is bounded
in closed form.  No quadrature, no special-function library call enters a proved number:
  * C0 = -gamma - 3 log 2 - pi/2 - log pi                              (closed form)
  * m(tau) - C0 = sum_k s/(a_k (a_k^2 + s)), a_k = k+1/4, s = tau^2/4  (Paper 47 thm:S(i));
    tail after K0 terms bracketed by integrals of the decreasing summand.
  * m''(tau) = sum_k a_k (a_k^2 - 3s)/(2(a_k^2+s)^3) <= sum_k a_k (a_k^2/2 - s)/(a_k^2+s)^3 ; each summand is decreasing-then-increasing
    in s, so its sup on a band is attained at an endpoint; positive tail <= 1/(4 (K0-3/4)^2).
  * I_p^{(ij)}(c) = int_0^c x^p j_i(x) j_j(x) dx, p = 0,1, from the product series
    j_i j_j = sum_k (-1)^k beta_k x^{i+j+2k}, beta_0 = 1/((2i+1)!!(2j+1)!!),
    beta_{k+1}/beta_k = (a+2k)(a+2k+1) / (4 (k+1)(i+k+3/2)(j+k+3/2)(a+k)), a = i+j+2
    (DLMF 10.8.3 with mu = i+1/2, nu = j+1/2; beta_k rational, computed exactly).
    Term ratio <= 1/2 for k >= max(a, 2c); the tail after the last term is <= |last term|.
  * g_l = <cosh(t/2) or sinh(t/2), e_l> = sqrt((2l+1)/2T) T 2 i_l(T/2), i_l the modified spherical
    Bessel function, positive-term series with ratio <= 1/2 (T/2 < 1/2).
Legendre basis e_l(t) = sqrt((2l+1)/2T) P_l(t/T), orthonormal in L^2(-T,T); hat e_l(tau) =
sqrt((2l+1)/2T) 2T (-i)^l j_l(tau T), so for l-i even
  (1/2pi) int_{|tau|<s} hat e_i conj(hat e_l) = (2/pi) sqrt((2i+1)(2l+1)) (-1)^{(l-i)/2} I_0(Ts),
  (1/2pi) int_{|tau|<s} |tau| hat e_i conj(hat e_l) = (2/pi) sqrt(...) (-1)^{(l-i)/2} I_1(Ts)/T,
and 0 for l-i odd.
"""
from fractions import Fraction
from mpmath import iv, mp

IVDPS = 40
iv.dps = IVDPS
mp.dps = IVDPS + 10


def ivf(x):
    return iv.mpf(x)


def C0_interval():
    g = iv.mpf(mp.nstr(mp.euler, IVDPS + 5)) + iv.mpf([-mp.mpf(10) ** (-IVDPS - 3), mp.mpf(10) ** (-IVDPS - 3)])
    return -g - iv.mpf(3) * iv.log(iv.mpf(2)) - iv.pi / iv.mpf(2) - iv.log(iv.pi)


def m_interval(tau, C0, K0=3000):
    """rigorous enclosure of m(tau) = C0 + sum_{k>=0} s/(a_k(a_k^2+s)), s = tau^2/4."""
    tau = ivf(tau)
    if tau == 0:
        return C0
    s = tau * tau / iv.mpf(4)
    tot = iv.mpf(0)
    for k in range(K0):
        a = iv.mpf(k) + iv.mpf(1) / iv.mpf(4)
        tot = tot + s / (a * (a * a + s))
    # tail: f(x) = s/((x+1/4)((x+1/4)^2+s)) decreasing; int_X^inf f = (1/2) log(1 + s/(X+1/4)^2)
    X = iv.mpf(K0) + iv.mpf(1) / iv.mpf(4)
    lo = iv.log(iv.mpf(1) + s / (X * X)) / iv.mpf(2)
    fK0 = s / (X * (X * X + s))
    tail = iv.mpf([lo.a, (lo + fK0).b])
    return C0 + tot + tail


def m2sup_band(ta, tb, K0=3000):
    """rigorous upper bound M2 >= sup_{tau in [ta,tb]} m''(tau) (may be negative).
    NOTE (R155_052 Lemma 2.3): the summand used here, a(a^2/2 - s)/(a^2+s)^3, is NOT the summand
    of m'' (which is a(a^2 - 3s)/(2(a^2+s)^3)); it dominates it termwise for s >= 0, and is itself
    decreasing-then-increasing in s, so the returned number is still a valid upper bound."""
    sa, sb = ivf(ta) ** 2 / iv.mpf(4), ivf(tb) ** 2 / iv.mpf(4)
    tot = iv.mpf(0)
    for k in range(K0):
        a = iv.mpf(k) + iv.mpf(1) / iv.mpf(4)
        ta_ = a * (a * a / iv.mpf(2) - sa) / (a * a + sa) ** 3
        tb_ = a * (a * a / iv.mpf(2) - sb) / (a * a + sb) ** 3
        tot = tot + iv.mpf([min(ta_.a, tb_.a), max(ta_.b, tb_.b)])   # >= max of the two
    X = iv.mpf(K0) - iv.mpf(3) / iv.mpf(4)
    tail = iv.mpf(1) / (iv.mpf(4) * X * X)   # positive part of the tail, sum_{k>=K0} 1/(2 a_k^3)
    return (tot + iv.mpf([0, tail.b])).b


def m2sup_band_exact(ta, tb, K0=3000):
    """rigorous upper bound M2 >= sup_{tau in [ta,tb]} m''(tau), from the EXACT second derivative
    m''(tau) = sum_k a_k (a_k^2 - 3s) / (2 (a_k^2+s)^3),  s = tau^2/4.
    Each summand has s-derivative proportional to (s - a_k^2): decreasing then increasing in s, so
    its sup on a band is attained at an endpoint; the positive tail is <= sum_{k>=K0} 1/(2 a_k^3)
    <= 1/(4 (K0-3/4)^2).  (m2sup_band above uses the larger summand a(a^2/2 - s)/(a^2+s)^3, which
    is also a valid -- more conservative -- upper bound; it is kept unchanged for the default runs.)"""
    sa, sb = ivf(ta) ** 2 / iv.mpf(4), ivf(tb) ** 2 / iv.mpf(4)
    tot = iv.mpf(0)
    for k in range(K0):
        a = iv.mpf(k) + iv.mpf(1) / iv.mpf(4)
        ta_ = a * (a * a - iv.mpf(3) * sa) / (iv.mpf(2) * (a * a + sa) ** 3)
        tb_ = a * (a * a - iv.mpf(3) * sb) / (iv.mpf(2) * (a * a + sb) ** 3)
        tot = tot + iv.mpf([min(ta_.a, tb_.a), max(ta_.b, tb_.b)])
    X = iv.mpf(K0) - iv.mpf(3) / iv.mpf(4)
    tail = iv.mpf(1) / (iv.mpf(4) * X * X)
    return (tot + iv.mpf([0, tail.b])).b


def beta_coeffs(i, j, kmax):
    """exact rational beta_k, k = 0..kmax, for j_i j_j = sum (-1)^k beta_k x^{i+j+2k}."""
    a = i + j + 2
    b0 = Fraction(1)
    for n in range(1, 2 * i + 2, 2):
        b0 /= n
    for n in range(1, 2 * j + 2, 2):
        b0 /= n
    out = [b0]
    for k in range(kmax):
        r = Fraction((a + 2 * k) * (a + 2 * k + 1), 4) / (Fraction(k + 1) * (Fraction(2 * i + 2 * k + 3, 2)) * (Fraction(2 * j + 2 * k + 3, 2)) * (a + k))
        out.append(out[-1] * r)
    return out


class BesselMoments(object):
    """I_p^{(ij)}(c) for all c in a list, p in {0,1}; c interval; rigorous tails."""

    def __init__(self, cs, K2, tol_exp=34):
        self.cs = [ivf(c) for c in cs]
        self.K2 = K2
        cmax = max(float(c.b) for c in self.cs)
        self.kstar = int(2 * cmax) + 2
        self.tol = iv.mpf(10) ** (-tol_exp)
        # powers c^n, n = 0..NP shared by all pairs
        self.NP = 2 * K2 + 2 * (self.kstar + 60) + 6
        self.cpow = []
        for c in self.cs:
            p = [iv.mpf(1)]
            for n in range(self.NP):
                p.append(p[-1] * c)
            self.cpow.append(p)
        self.inv = [None] + [iv.mpf(1) / iv.mpf(n) for n in range(1, self.NP + 2)]

    def moments(self, i, j):
        """returns lists I0[a], I1[a] (intervals) over the c list, for the pair (i,j)."""
        a = i + j + 2
        kst = max(a, self.kstar)
        KM = kst + 60
        beta = beta_coeffs(i, j, KM)
        betaiv = [iv.mpf(b.numerator) / iv.mpf(b.denominator) for b in beta]
        I0, I1 = [], []
        for ci, c in enumerate(self.cs):
            cp = self.cpow[ci]
            s0 = iv.mpf(0); s1 = iv.mpf(0)
            k = 0
            while True:
                n = a + 2 * k - 1               # power of x in j_i j_j: i+j+2k = n-1 ... integral of x^{n-1}: c^n/n
                u = betaiv[k] * cp[n]           # beta_k c^{i+j+2k+1}
                t0 = u * self.inv[n]            # int_0^c x^{i+j+2k} = c^n/n
                t1 = u * c * self.inv[n + 1]    # int_0^c x^{i+j+2k+1} = c^{n+1}/(n+1)
                if k % 2:
                    s0 = s0 - t0; s1 = s1 - t1
                else:
                    s0 = s0 + t0; s1 = s1 + t1
                if k >= kst and t0.b < self.tol.a and t1.b < self.tol.a:
                    break
                k += 1
                if k > KM:
                    raise RuntimeError("series did not converge; enlarge KM")
            # tail bound: ratio <= 1/2 beyond k >= kst, so remaining sum <= |last term|
            s0 = s0 + iv.mpf([-t0.b, t0.b]); s1 = s1 + iv.mpf([-t1.b, t1.b])
            I0.append(s0); I1.append(s1)
        return I0, I1


def g_coeffs(T, K2, par):
    """g_l = <g, e_l>, g = cosh(t/2) (par 0) or sinh(t/2) (par 1), for l < K2 of that parity;
    others 0.  g_l = sqrt((2l+1)/(2T)) * T * 2 i_l(T/2), i_l(z) = sum_k z^{l+2k} 2^l (l+k)!/(k!(2l+2k+1)!)."""
    T = ivf(T)
    z = T / iv.mpf(2)
    assert z.b < 0.5
    out = [iv.mpf(0)] * K2
    for l in range(par, K2, 2):
        # term_0 = z^l 2^l l!/(2l+1)! = z^l/(2l+1)!!
        term = z ** l
        for n in range(1, 2 * l + 2, 2):
            term = term / iv.mpf(n)
        tot = iv.mpf(0)
        k = 0
        while True:
            tot = tot + term
            # ratio z^2 (l+k+1)/((k+1)(2l+2k+2)(2l+2k+3)) = z^2 / (2 (k+1)(2l+2k+3)) <= 1/2
            term = term * z * z / (iv.mpf(2) * iv.mpf(k + 1) * iv.mpf(2 * l + 2 * k + 3))
            k += 1
            if term.b < 1e-45:
                break
        tot = tot + iv.mpf([0, term.b])          # geometric tail <= last omitted term (ratio <= 1/2)... times 2 for safety
        tot = tot + iv.mpf([0, term.b])
        out[l] = iv.sqrt((iv.mpf(2 * l + 1)) / (iv.mpf(2) * T)) * T * iv.mpf(2) * tot
    return out


def gnorm2(T, par):
    T = ivf(T)
    sh = (iv.exp(T) - iv.exp(-T)) / iv.mpf(2)
    return (T + sh) if par == 0 else (sh - T)


# ---------------- interval linear algebra
def cholesky_pd(Mx, mu=None):
    """True if every real symmetric matrix in the interval matrix Mx - mu I is positive definite."""
    n = len(Mx)
    L = [[iv.mpf(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = Mx[i][j] - (mu if (i == j and mu is not None) else iv.mpf(0))
            for k in range(j):
                s = s - L[i][k] * L[j][k]
            if i == j:
                if not (s.a > 0):
                    return False
                L[i][i] = iv.sqrt(s)
            else:
                L[i][j] = s / L[j][j]
    return True


def congruence(U, Mx):
    """U^T Mx U for a real (float) matrix U (columns) and interval matrix Mx."""
    n = len(Mx); r = len(U[0])
    Uiv = [[iv.mpf(repr(float(U[i][k]))) for k in range(r)] for i in range(n)]
    MU = [[sum((Mx[i][j] * Uiv[j][k] for j in range(n)), iv.mpf(0)) for k in range(r)] for i in range(n)]
    return [[sum((Uiv[i][k] * MU[i][l] for i in range(n)), iv.mpf(0)) for l in range(r)] for k in range(r)]


def lo(x):
    return float(mp.mpf(x.a))


def hi(x):
    return float(mp.mpf(x.b))


def mid(x):
    return 0.5 * (lo(x) + hi(x))


def wid(x):
    return hi(x) - lo(x)
