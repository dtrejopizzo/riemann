"""R154 round 4: rigorous interval-arithmetic (mpmath.iv) re-evaluation of the certificate.

Everything here is an ENCLOSURE.  No use of scipy/numpy floats except as input data
(the certificate coefficients, which are read as exact decimal strings).

m(tau) = Re psi(1/4 + i tau/2) - log pi is enclosed by
   Re psi(z) = Re psi(z+J) - sum_{j<J} Re 1/(z+j),      z = 1/4 + i y,  y = tau/2
   Re psi(w) = 1/2 log|w|^2/... via the asymptotic series with Stieltjes' remainder bound
      |R_N(w)| <= |B_{2N}| / (2N |w|^{2N}) * sec(theta/2)^{2N},  theta = arg w,
      sec(theta/2)^{2N} = (2|w|/(|w|+Re w))^N.
"""
import math
from mpmath import iv, mp, bernoulli

iv.dps = 40
mp.dps = 60

_B = None
def _bern(N):
    global _B
    if _B is None or len(_B) < N+1:
        _B = [mp.mpf(0)]*(2*N+2)
        for n in range(0, N+1):
            _B[2*n] = bernoulli(2*n)
    return _B


def _iv(x):
    return x if isinstance(x, iv.mpf) else iv.mpf(str(x))


def re_psi_iv(A, y, N=12):
    """Re psi(A + i y) by the asymptotic series, A large enough (A >= 2|y|+20)."""
    A = _iv(A); y = _iv(y)
    w2 = A*A + y*y                       # |w|^2
    absw = iv.sqrt(w2)
    s = iv.log(w2)/2 - A/(2*w2)
    # w^{-2n}: keep (re,im) of w^{-2}
    dr = (A*A - y*y)/(w2*w2); di = -2*A*y/(w2*w2)   # w^{-2} = conj(w)^2/|w|^4
    B = _bern(N)
    pr, pi_ = iv.mpf(1), iv.mpf(0)
    for n in range(1, N):
        pr, pi_ = pr*dr - pi_*di, pr*di + pi_*dr    # w^{-2n}
        s = s - _iv(mp.nstr(B[2*n], 40))/(2*n)*pr
    # remainder
    pr2, pi2 = pr*dr - pi_*di, pr*di + pi_*dr       # w^{-2N}
    modw2N = (absw**(-2*N))
    sec = (2*absw/(absw + A))**N
    R = _iv(abs(mp.nstr(B[2*N], 40, strip_zeros=False) and float(abs(B[2*N])))) if False else _iv(str(abs(B[2*N])))
    bnd = R/(2*N)*modw2N*sec
    return s + iv.mpf([-bnd.b, bnd.b])


def m_iv(tau, N=12):
    """enclosure of m(tau) = Re psi(1/4 + i tau/2) - log(pi)"""
    tau = _iv(tau)
    y = tau/2
    ymax = float(abs(y).b)
    J = int(2*ymax) + 30
    A0 = iv.mpf(1)/4
    s = re_psi_iv(A0 + J, y, N=N)
    for j in range(J):
        a = A0 + j
        s = s - a/(a*a + y*y)
    return s - iv.log(iv.pi)


def _sinh(x):
    e = iv.exp(x); return (e - 1/e)/2


def _cosh(x):
    e = iv.exp(x); return (e + 1/e)/2


def g0h_iv(tau, T):
    tau = _iv(tau); T = _iv(T); L = 2*T
    return 2*(_sinh(T)/2*iv.cos(L*tau) + tau*_cosh(T)*iv.sin(L*tau))/(tau*tau + iv.mpf(1)/4)


def _ReI(c, b, L):
    """Re[ L e^{(c+ib)L}/(c+ib) - (e^{(c+ib)L}-1)/(c+ib)^2 ]"""
    E = iv.exp(c*L); C = iv.cos(b*L); S = iv.sin(b*L)
    den = c*c + b*b
    t1 = L*E*(C*c + S*b)/den
    t2 = ((E*C - 1)*(c*c - b*b) + 2*b*c*E*S)/(den*den)
    return t1 - t2


def g1h_iv(tau, T):
    tau = _iv(tau); T = _iv(T); L = 2*T; h = iv.mpf(1)/2
    return _ReI(h, tau, L) - _ReI(-h, tau, L)


def nuhat_iv(tau, us, a):
    tau = _iv(tau); s = iv.mpf(0)
    for u, aj in zip(us, a):
        s = s + 2*_iv(aj)*iv.cos(_iv(u)*tau)
    return s


def f_iv(tau, T, us, a, b0, b1, v):
    tau = _iv(tau)
    s = m_iv(tau)
    for n, vn in v.items():
        s = s - _iv(vn)*iv.cos(tau*iv.log(_iv(n)))
    s = s + _iv(b0)*g0h_iv(tau, T) + _iv(b1)*g1h_iv(tau, T) + nuhat_iv(tau, us, a)
    return s


def G0_iv(T):
    T = _iv(T); L = 2*T
    return 2*(2*L*_sinh(L/2) - 4*(_cosh(L/2) - 1))


def G1_iv(T):
    T = _iv(T); L = 2*T
    F = lambda u: 2*u*u*_cosh(u/2) - 8*u*_sinh(u/2) + 16*_cosh(u/2)
    return 2*(F(L) - F(iv.mpf(0)))


def psi1_quarter_iv():
    """enclosure of psi'(1/4) = pi^2 + 8G  (G = Catalan)"""
    mp.dps = 60
    val = mp.polygamma(1, mp.mpf(1)/4)
    lo = mp.nstr(val*(1-mp.mpf(10)**-40), 40); hi = mp.nstr(val*(1+mp.mpf(10)**-40), 40)
    # independent closed form: psi'(1/4) = pi^2 + 8*Catalan
    chk = mp.pi**2 + 8*mp.catalan
    assert abs(chk - val) < mp.mpf(10)**-45, (chk, val)
    return iv.mpf([lo, hi])


def lip_iv(T, us, a, b0, b1, v):
    s = psi1_quarter_iv()/2
    for n, vn in v.items():
        s = s + _iv(vn)*iv.log(_iv(n))
    t = iv.mpf(0)
    for u, aj in zip(us, a):
        t = t + abs(_iv(aj))*_iv(u)
    s = s + 2*t + abs(_iv(b0))*G0_iv(T) + abs(_iv(b1))*G1_iv(T)
    return s


def tail_k_iv(T, taumax):
    T = _iv(T); tm = _iv(taumax)
    return (2*_cosh(T)/tm + _sinh(T)/(tm*tm), 8*T*_sinh(T)/tm)
