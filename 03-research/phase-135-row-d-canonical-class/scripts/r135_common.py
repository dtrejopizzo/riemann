"""Shared numerics for phase 135 (row D, the canonical class).

Conventions are Paper 46 (1.7)-(1.9):

    Phi_g(s) = int g(t) e^{(s-1/2)t} dt
    I_infty(F,G) = Phi_F(0)Phi_G(1) + Phi_F(1)Phi_G(0) - sum_rho Phi_F(rho)Phi_G(1-rho)
    deg F = Phi_F(0) + Phi_F(1)

The canonical class K is Polya's kernel (Titchmarsh, *The Theory of the
Riemann Zeta-Function*, 2nd ed., section 10.1, eq. (10.1.4)):

    K(t) = sum_{n>=1} (4 pi^2 n^4 e^{9t/2} - 6 pi n^2 e^{5t/2}) e^{-pi n^2 e^{2t}},

so that Phi_K(s) = xi(s) with xi(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s).

NUMERICS ILLUSTRATE AND FALSIFY.  THEY PROVE NOTHING, AND NO NUMBER BELOW IS
EVIDENCE FOR ANY SIGN.
"""
import mpmath as mp

DPS = 30


def xi(s):
    """Completed zeta xi(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s), entire."""
    s = mp.mpmathify(s)
    if s == 0 or s == 1:
        return mp.mpf(1) / 2
    # Gamma(s/2) = 2/s * Gamma(s/2+1) removes the pole at s=0 cleanly.
    return mp.mpf(1) / 2 * s * (s - 1) * mp.pi ** (-s / 2) * (2 / s) * mp.gamma(s / 2 + 1) * mp.zeta(s)


def K(t, dps=DPS + 10):
    """Polya kernel, evaluated through K(t) = K(|t|) (evenness is classical and
    is re-checked in polya_class.py; using |t| avoids the catastrophic
    cancellation of the series for t -> -infinity)."""
    with mp.workdps(dps):
        t = abs(mp.mpf(t))
        x = mp.e ** (2 * t)
        s = mp.mpf(0)
        cut = (mp.mpf(dps) + 40) * mp.log(10) + 5 * abs(t)
        n = 1
        while n <= 4000:
            ex = mp.pi * n * n * x
            if ex > cut:
                break
            s += (4 * mp.pi ** 2 * n ** 4 * mp.e ** (mp.mpf(9) * t / 2)
                  - 6 * mp.pi * n ** 2 * mp.e ** (mp.mpf(5) * t / 2)) * mp.e ** (-ex)
            n += 1
        return +s


def Kraw(t, dps=120):
    """The series evaluated literally at t (no evenness shortcut)."""
    with mp.workdps(dps):
        t = mp.mpf(t)
        x = mp.e ** (2 * t)
        s = mp.mpf(0)
        cut = (mp.mpf(dps) + 40) * mp.log(10) + 5 * abs(t)
        n = 1
        while n <= 6000:
            ex = mp.pi * n * n * x
            if ex > cut:
                break
            s += (4 * mp.pi ** 2 * n ** 4 * mp.e ** (mp.mpf(9) * t / 2)
                  - 6 * mp.pi * n ** 2 * mp.e ** (mp.mpf(5) * t / 2)) * mp.e ** (-ex)
            n += 1
        return +s


# ---------------------------------------------------------------- test class

def bump(t, T=1.0):
    """A real even C^infty bump supported in [-T,T], normalised to max 1."""
    t = mp.mpmathify(t)
    if abs(t) >= T:
        return mp.mpf(0)
    return mp.e * mp.e ** (-1 / (1 - (t / T) ** 2))


def Pi_of(g, h=mp.mpf('1e-5')):
    """(Pi g)(t) = -g''(t) + g(t)/4, by a central second difference."""
    def f(t):
        t = mp.mpmathify(t)
        return -(g(t + h) - 2 * g(t) + g(t - h)) / h ** 2 + g(t) / 4
    return f


def Phi(g, s, a=-1.0, b=1.0, pts=None):
    """Phi_g(s) = int g(t)e^{(s-1/2)t}dt, by quadrature over [a,b]."""
    s = mp.mpmathify(s)
    nodes = pts if pts is not None else [a, 0, b]
    return mp.quad(lambda t: g(t) * mp.e ** ((s - mp.mpf(1) / 2) * t), nodes)


# ------------------------------------------------- explicit-formula machinery

def arch_term(hhat, tau_max=60):
    """(1/2pi) int_R hhat(tau) [Re psi(1/4 + i tau/2) - log pi] dtau,
    the archimedean term of Paper 45 (9.6a)."""
    f = lambda tau: hhat(tau) * (mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * tau / 2)) - mp.log(mp.pi))
    return mp.quad(f, [-tau_max, -8, -1, 0, 1, 8, tau_max]) / (2 * mp.pi)


def vonmangoldt(n):
    f = mp.libmp.libintmath.ifac  # placeholder, unused
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            return mp.log(p) if m == 1 else mp.mpf(0)
        p += 1
    return mp.log(n) if n > 1 else mp.mpf(0)


def prime_term(h, nmax):
    """sum_{2<=n<=nmax} Lambda(n) n^{-1/2} [h(log n) + h(-log n)]."""
    s = mp.mpf(0)
    for n in range(2, nmax + 1):
        L = vonmangoldt(n)
        if L == 0:
            continue
        s += L * mp.mpf(n) ** mp.mpf('-0.5') * (h(mp.log(n)) + h(-mp.log(n)))
    return s


# ---------------------------------------------------------------------------
# [phase 135, R135_004]  Fast float64 layer.
#
# The mpmath layer above is the reference; it is exact to `DPS` digits and slow.
# The layer below reproduces the same quantities in float64 with fixed
# Gauss-Legendre panels, so that `--fast` runs finish in seconds.  Every number
# printed by a `--fast` run is accompanied by the tolerance it is checked at,
# and no number below is evidence for any sign.
# ---------------------------------------------------------------------------
import numpy as _np

# K(t) = sum_n (a_n e^{9t/2} + b_n e^{5t/2}) e^{-c_n e^{2t}},
#   a_n = 4 pi^2 n^4, b_n = -6 pi n^2, c_n = pi n^2.
_NMAX_K = 60


def Kf(t):
    """K(t) in float64, vectorised; uses evenness K(t)=K(|t|)."""
    t = _np.abs(_np.asarray(t, dtype=float))
    u = _np.exp(2.0 * t)
    e9 = _np.exp(4.5 * t)
    e5 = _np.exp(2.5 * t)
    out = _np.zeros_like(t)
    for n in range(1, _NMAX_K + 1):
        c = _np.pi * n * n
        ex = c * u
        m = ex < 700.0
        if not m.any():
            break
        L = 4 * _np.pi ** 2 * n ** 4 * e9[m] - 6 * _np.pi * n * n * e5[m]
        out[m] += L * _np.exp(-ex[m])
    return out


def PiKf(t):
    """(Pi K)(t) = -K''(t) + K(t)/4 in float64, by term-by-term differentiation
    of (11.7) (no finite differences)."""
    t = _np.asarray(t, dtype=float)
    s = _np.abs(t)                      # K is even, so K'' is even too
    u = _np.exp(2.0 * s)
    e9 = _np.exp(4.5 * s)
    e5 = _np.exp(2.5 * s)
    K = _np.zeros_like(s)
    K2 = _np.zeros_like(s)
    for n in range(1, _NMAX_K + 1):
        a = 4 * _np.pi ** 2 * n ** 4
        b = -6 * _np.pi * n * n
        c = _np.pi * n * n
        ex = c * u
        m = ex < 700.0
        if not m.any():
            break
        A, B = a * e9[m], b * e5[m]
        L = A + B
        L1 = 4.5 * A + 2.5 * B
        L2 = 20.25 * A + 6.25 * B
        cu = c * u[m]
        M = _np.exp(-ex[m])
        M1 = -2.0 * cu * M
        M2 = (-4.0 * cu + 4.0 * cu * cu) * M
        K[m] += L * M
        K2[m] += L2 * M + 2.0 * L1 * M1 + L * M2
    return -K2 + K / 4.0


def gl_panels(a, b, npanel, order=24):
    """Composite Gauss-Legendre nodes and weights on [a,b]."""
    x, w = _np.polynomial.legendre.leggauss(order)
    edges = _np.linspace(a, b, npanel + 1)
    lo, hi = edges[:-1, None], edges[1:, None]
    nodes = (0.5 * (hi - lo) * x[None, :] + 0.5 * (hi + lo)).ravel()
    wts = (0.5 * (hi - lo) * w[None, :]).ravel()
    return nodes, wts


def bumpf(t, T=1.0):
    """The bump of `bump()` in float64, vectorised."""
    t = _np.asarray(t, dtype=float)
    v = 1.0 - (t / T) ** 2
    out = _np.zeros_like(t)
    m = v > 0
    out[m] = _np.e * _np.exp(-1.0 / v[m])
    return out


def Pibumpf(t, T=1.0):
    """(Pi bump)(t) = -bump'' + bump/4, analytically (bump = e.exp(-1/v),
    v = 1-(t/T)^2, so bump' = bump.v'/v^2 and
    bump'' = bump.[(v'/v^2)^2 + v''/v^2 - 2 v'^2/v^3])."""
    t = _np.asarray(t, dtype=float)
    v = 1.0 - (t / T) ** 2
    out = _np.zeros_like(t)
    m = v > 0
    vv = v[m]
    v1 = -2.0 * t[m] / T ** 2
    v2 = -2.0 / T ** 2
    b = _np.e * _np.exp(-1.0 / vv)
    g = v1 / vv ** 2
    b2 = b * (g * g + v2 / vv ** 2 - 2.0 * v1 * v1 / vv ** 3)
    out[m] = -b2 + b / 4.0
    return out
