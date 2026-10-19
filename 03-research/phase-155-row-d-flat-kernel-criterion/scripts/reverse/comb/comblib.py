"""comblib.py -- phase 155, R155_016: COMPACTLY SUPPORTED C^2 flat-top weights
with the comb-vanishing equalities  w(log n) = 0  for every prime power n with
2T < log n <= U   (Corollary D.2 of R155_013).

Difference from dlib.Win (R155_011): the psi-edge columns are GONE.  psi_s(v) has
infinite support, so supp w is not compact and E_at(w) is an infinite sum -- the
comb conditions could never be a finite set.  Here the whole weight is a cubic
spline on the uniform lattice u_j = 2T + j h:

    w(u) = 1                                  for |u| <= 2T,
    w(u) = B(u) + sum_{j=2}^{J} x_j beta((u-u_j)/h)   for u > 2T,
    B(u) = beta((u-u_{-1})/h) + beta((u-u_0)/h) + beta((u-u_1)/h).

The three unit coefficients x_{-1}=x_0=x_1=1 are forced (and are the ONLY solution)
by the C^2 matching at the window edge:
    g(2T)=1, g'(2T)=0, g''(2T)=0  <=>  x_{-1}=x_1, x_1=x_0, x_0=1
using beta(0)=2/3, beta(+-1)=1/6, beta'(+-1)=-+1/2, beta''(0)=-2, beta''(+-1)=1.
Hence w is globally C^2 (and C^2 across u=+-2T), even, and
    supp w subset [-U, U],   U = 2T + (J+2) h,
so E_at(w) is a FINITE sum and the comb conditions are J-1 -> finite equalities.

Zero side as in dlib:  f_w(tau) = 4 int_0^{Umax} w(u) cos(tau u) Z(u) du,
Z(u) = sum_{gamma>0} cos(gamma u) over the first NZ zeros.
Prime side: primeside.f_prime_fast (generic in `win`).

ALL NUMBERS DIAGNOSTIC unless stated certified.
"""
import numpy as np, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REV = os.path.abspath(os.path.join(HERE, "..", "..", "..",
      "03-research", "phase-155-row-d-flat-kernel-criterion", "scripts", "reverse"))
sys.path.insert(0, REV)
sys.path.insert(0, os.path.join(REV, "d1000"))
import revlib as R1, revlib2 as R2          # noqa: E402
import primeside as P                       # noqa: E402

bsp = R2.beta_spline


class WinC:
    """Compactly supported C^2 flat-top window, lattice h = 2T/M, support radius U."""

    def __init__(self, T, U, M=24, Umaxpad=6.0, dp=0.01, ngl=12):
        self.T = T; self.M = M; self.h = h = 2.0 * T / M
        self.J = J = int(np.floor((U - 2 * T) / h)) - 2      # last free spline index
        assert J >= 2, "support too short for the lattice"
        self.U = U_ = 2 * T + (J + 2) * h                    # true support radius
        self.ujs = 2 * T + h * np.arange(2, J + 1)           # free spline centres
        self.nX = len(self.ujs)
        self.Umax = U_ + Umaxpad
        self.A_T = R1.A_const(T)
        # ---- quadrature: knot-aligned Gauss-Legendre panels
        edges = [0.0, 2 * T] + list(2 * T + h * np.arange(1, J + 3)) + [self.Umax]
        edges = sorted(set(round(e, 12) for e in edges if e <= self.Umax + 1e-12))
        pans = []
        for a, b in zip(edges[:-1], edges[1:]):
            k = max(1, int(np.ceil((b - a) / dp)))
            xs = np.linspace(a, b, k + 1)
            pans += list(zip(xs[:-1], xs[1:]))
        xg, wg = np.polynomial.legendre.leggauss(ngl)
        A = np.array([p[0] for p in pans]); Bq = np.array([p[1] for p in pans])
        self.u = (0.5 * (Bq - A)[:, None] * xg[None, :] + 0.5 * (A + Bq)[:, None]).ravel()
        self.wq = (0.5 * (Bq - A)[:, None] * wg[None, :]).ravel()
        self.npan = len(pans); self.ngl = ngl

    # ---- the fixed base column (box + C^2 edge continuation)
    def base(self, u):
        u = np.asarray(u, float); T = self.T; h = self.h
        out = np.where(u <= 2 * T + 1e-13, 1.0, 0.0)
        m = u > 2 * T + 1e-13
        if m.any():
            v = u[m]
            out[m] = (bsp((v - (2 * T - h)) / h) + bsp((v - 2 * T) / h)
                      + bsp((v - (2 * T + h)) / h))
        return out

    def spl(self, u):
        """(nX, nu) matrix of the free spline columns, zero on |u| <= 2T."""
        u = np.asarray(u, float)
        m = (u > 2 * self.T + 1e-13).astype(float)
        return np.array([bsp((u - uj) / self.h) * m for uj in self.ujs])

    def basis_matrix(self):
        return np.vstack([self.base(self.u)[None, :], self.spl(self.u)])

    def w_of_u(self, u, x):
        return self.base(u) + (np.asarray(x, float) @ self.spl(u) if len(x) else 0.0)

    # ---- comb: prime powers strictly inside the shoulder
    def comb_nodes(self, ns, lam):
        logn = np.log(ns)
        sel = (logn > 2 * self.T) & (logn <= self.U + 1e-12)
        return logn[sel], 2 * lam[sel] / np.sqrt(ns[sel])


# ------------------------------------------------------------------ zero side
def Zfun(u, gam, chunk=256):
    u = np.asarray(u, float); out = np.zeros_like(u)
    for a in range(0, len(gam), chunk):
        out += np.cos(np.outer(gam[a:a + chunk], u)).sum(0)
    return out


def rows(win, Phi, Z, tau, tblk=4000, ublk=2000):
    nc = Phi.shape[0]; nt = len(tau)
    out = np.zeros((nc, nt))
    G = Phi * (4.0 * win.wq * Z)[None, :]
    for a in range(0, len(win.u), ublk):
        b = min(a + ublk, len(win.u)); uu = win.u[a:b]
        for c in range(0, nt, tblk):
            d = min(c + tblk, nt)
            out[:, c:d] += G[:, a:b] @ np.cos(np.outer(uu, tau[c:d]))
    return out


def fvals(win, Z, x, tau, tblk=8000, ublk=2000):
    g = 4.0 * win.wq * Z * win.w_of_u(win.u, x)
    out = np.zeros(len(tau))
    for a in range(0, len(win.u), ublk):
        b = min(a + ublk, len(win.u)); uu = win.u[a:b]
        for c in range(0, len(tau), tblk):
            d = min(c + tblk, len(tau))
            out[c:d] += g[a:b] @ np.cos(np.outer(uu, tau[c:d]))
    return out


def Zenvelope(win, gam, du=2e-5):
    n = int(np.ceil(win.Umax / du)) + 1
    ug = np.linspace(0.0, win.Umax, n)
    Zg = np.abs(Zfun(ug, gam))
    slack = float(np.sum(gam)) * du
    ngl = win.ngl; env = np.empty(len(win.u))
    for p in range(win.npan):
        sl = slice(p * ngl, (p + 1) * ngl)
        a, b = win.u[sl][0], win.u[sl][-1]
        i0 = max(0, int(np.floor(a / du)) - 1); i1 = min(n, int(np.ceil(b / du)) + 2)
        env[sl] = Zg[i0:i1].max() + slack
    return env


def d2_bound(win, x, Zenv):
    return float(4.0 * np.sum(win.wq * win.u**2 * np.abs(win.w_of_u(win.u, x)) * Zenv))


def ghat(T, tt, n=600):
    xs, ws = np.polynomial.legendre.leggauss(n)
    u = T * (xs + 1.0); wq = T * ws
    C = np.cos(np.outer(u, np.asarray(tt, float)))
    return np.vstack([2 * (wq * np.cosh(u / 2)) @ C, 2 * (wq * u * np.sinh(u / 2)) @ C])


# ------------------------------------------------------------------ Theorem D
def Dw_and_taustop(win, x, bet, du=2e-5):
    """D(w) = D_K + D_cosh and tau_stop of Theorem D / Cor D.2 (E_at = 0)."""
    T = win.T
    ug = np.arange(0.0, win.Umax + 2.0, du)
    wg = win.w_of_u(ug, x)
    W = wg * np.cosh(ug / 2)
    W2 = (W[2:] - 2 * W[1:-1] + W[:-2]) / du**2
    D_c = float(4 * np.trapz(np.abs(W2), ug[1:-1]))
    Kg = 0.5 / np.sinh(np.maximum(ug, 1e-12) / 2) + 0.5 / np.cosh(ug / 2)
    R = np.where(ug >= 2 * T, (1 - wg) * Kg, 0.0)
    R2_ = (R[2:] - 2 * R[1:-1] + R[:-2]) / du**2
    mm = ug[1:-1] >= 2 * T
    D_K = float(np.trapz(np.abs(R2_[mm]), ug[1:-1][mm]))
    Dtot = D_K + D_c
    b0, b1 = abs(bet[0]), abs(bet[1])
    A_T = win.A_T

    def L(t):
        k0 = 2 * np.cosh(T) / t + np.sinh(T) / t**2
        k1 = 8 * T * np.sinh(T) / t
        return (np.log(t / (2 * np.pi)) - 1 / t - 1 / (2 * t**2) - A_T
                - b0 * k0 - b1 * k1 - Dtot / t**2)
    lo, hi = 1.0, 1e80
    for _ in range(300):
        mid = np.sqrt(lo * hi)
        if L(mid) > 0: hi = mid
        else: lo = mid
    return D_K, D_c, Dtot, float(hi), L


# ------------------------------------------------------------------ prime side
def f_prime(win, x, tau, ns, lam, tblk=20000, ublk=2000):
    """Prime/Gamma side of Theorem Z (7.2) for a WinC weight; mirrors
    primeside.f_prime_fast with the WinC signature.  Full prime-power sum up to
    e^{Umax} (w vanishes beyond U), knot-aligned Gauss-Legendre for the integrals,
    exact analytic K-tail beyond Umax."""
    T = win.T; tau = np.asarray(tau, float)
    u = win.u; wq = win.wq; wu = win.w_of_u(u, x)
    K = 0.5 / np.sinh(np.maximum(u, 1e-12) / 2) + 0.5 / np.cosh(u / 2)
    inw = u >= 2 * T
    g = np.where(inw, wq * (1.0 - wu) * K, 0.0) + 4.0 * wq * wu * np.cosh(u / 2)
    out = np.zeros(len(tau))
    for a in range(0, len(u), ublk):
        b = min(a + ublk, len(u)); uu = u[a:b]
        for c in range(0, len(tau), tblk):
            d = min(c + tblk, len(tau))
            out[c:d] += g[a:b] @ np.cos(np.outer(uu, tau[c:d]))
    out += P.Ktail_beyond(tau, win.Umax)
    logn = np.log(ns); wn = win.w_of_u(logn, x) * (logn <= win.Umax)
    coef = 2 * lam / np.sqrt(ns) * wn
    nzm = np.abs(coef) > 1e-15; lnn = logn[nzm]; cf = coef[nzm]
    for a in range(0, len(lnn), 20000):
        b = min(a + 20000, len(lnn))
        out -= cf[a:b] @ np.cos(np.outer(lnn[a:b], tau))
    return R1.m_of_tau(tau) + out
