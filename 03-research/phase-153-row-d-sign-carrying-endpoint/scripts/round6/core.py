"""R153 round 6: assembly of the body W_T.

Coordinates on the unit sphere of P_T (L^2(-T,T), two moment constraints):
  x_0 = <(G_{Gamma,T} - m_0) F, F>      multiplier  Re psi(1/4 + i tau/2) - log pi
  x_n = c_F(log n) = int F(t)F(t-log n) dt   multiplier cos(tau log n)
so that <A_T F,F> = x_0 - 2 sum_n w_n x_n,  w_n = Lambda(n)/sqrt(n).

Sine basis phi_k(t) = sin(k pi (t+T)/L), L = 2T, on (-T,T).
Gamma block: Fourier-multiplier quadrature (same scheme as scripts/audit/aud_spectral.py).
Shift blocks: EXACT closed form (no quadrature error).
"""
import math, numpy as np, scipy.linalg as sla
from scipy.special import psi as digamma
from numpy.polynomial.legendre import leggauss


def basis_hat(T, K, tau):
    L = 2 * T
    b = np.array([k * math.pi / L for k in range(1, K + 1)])
    tau = np.asarray(tau, dtype=float)
    den = (b[:, None] ** 2 - tau[None, :] ** 2)
    sgn = np.array([(-1) ** k for k in range(1, K + 1)])[:, None]
    num = b[:, None] * (1 - sgn * np.exp(-1j * tau[None, :] * L))
    out = np.where(np.abs(den) < 1e-9, 0.0 + 0.0j,
                   num / np.where(np.abs(den) < 1e-9, 1.0, den))
    for i in range(K):
        m = np.abs(den[i]) < 1e-9
        if m.any():
            t0 = tau[m]
            out[i, m] = (-1j * L * (-1) ** (i + 1) * np.exp(-1j * t0 * L) * b[i]) / (2 * b[i])
    return np.exp(1j * tau[None, :] * T) * out


def gamma_matrix(T, K, taumax=4000.0, npan=400, ng=24):
    """Galerkin matrix of the multiplier Re psi(1/4+i tau/2) - log pi."""
    edges = np.concatenate([np.linspace(0, 50, npan // 2 + 1)[:-1],
                            np.exp(np.linspace(math.log(50), math.log(taumax), npan // 2 + 1))])
    x, w = leggauss(ng)
    M = np.zeros((K, K))
    for lo, hi in zip(edges[:-1], edges[1:]):
        t = 0.5 * (hi - lo) * x + 0.5 * (hi + lo)
        ww = 0.5 * (hi - lo) * w
        H = basis_hat(T, K, t)
        s = np.real(digamma(0.25 + 0.5j * t)) - math.log(math.pi)
        M += np.real((H * (ww * s)) @ H.conj().T)
    M = 2 * M / (2 * math.pi)
    return 0.5 * (M + M.T)


def shift_matrix(T, K, a):
    """EXACT matrix of the quadratic form F -> int F(t) F(t-a) dt in the sine basis."""
    L = 2 * T
    if a >= L:
        return np.zeros((K, K))
    kk = np.arange(1, K + 1) * math.pi / L
    al = kk[:, None] * np.ones((1, K))   # alpha_j
    be = np.ones((K, 1)) * kk[None, :]   # beta_k
    p = al - be
    q = al + be
    # A = int_a^L cos(p u + beta a) du
    with np.errstate(divide='ignore', invalid='ignore'):
        A = np.where(np.abs(p) > 1e-14,
                     (np.sin(p * L + be * a) - np.sin(p * a + be * a)) / np.where(np.abs(p) > 1e-14, p, 1.0),
                     (L - a) * np.cos(be * a))
    B = (np.sin(q * L - be * a) - np.sin(q * a - be * a)) / q
    S = 0.5 * (A - B)
    return 0.5 * (S + S.T)


def moments(T, K, betas):
    L = 2 * T
    rows = []
    for bt in betas:
        r = []
        for k in range(1, K + 1):
            b = k * math.pi / L
            r.append(math.exp(-bt * T) * b * (1 - ((-1) ** k) * math.exp(bt * L)) / (bt ** 2 + b ** 2))
        rows.append(r)
    return np.array(rows)


class Body:
    """Assembled blocks, restricted to the null space of the moment constraints."""

    def __init__(self, T, K, contacts=None, taumax=4000.0, npan=400, ng=24, constrained=True):
        self.T, self.K = T, K
        if contacts is None:
            contacts = [n for n in (2, 3, 4, 5, 6, 7) if n < math.exp(2 * T) - 1e-13]
        self.contacts = contacts
        G = np.eye(K) * T
        Z = sla.null_space(moments(T, K, [-0.5, 0.5])) if constrained else np.eye(K)
        self.Z = Z
        self.G = Z.T @ G @ Z
        self.M0 = Z.T @ gamma_matrix(T, K, taumax, npan, ng) @ Z
        self.Mn = {n: Z.T @ shift_matrix(T, K, math.log(n)) @ Z for n in contacts}
        # symmetric Cholesky reduction to a standard eigenproblem
        self.R = np.linalg.cholesky(self.G)

    def op(self, u0, un):
        M = u0 * self.M0
        for n, c in un.items():
            M = M + c * self.Mn[n]
        return M

    def eig(self, u0, un, which='min'):
        M = self.op(u0, un)
        w, V = sla.eigh(M, self.G)
        i = 0 if which == 'min' else -1
        return w[i], self.Z @ V[:, i]

    def lmin(self, u0, un):
        return self.eig(u0, un, 'min')[0]

    def support(self, u0, un):
        """h_W(u) = max_{||F||=1} <u, x(F)>; finite only for u0 <= 0."""
        return self.eig(u0, un, 'max')[0]

    def coords(self, F):
        """x(F) for a coefficient vector F (in the full K-basis), normalised."""
        nrm = float(F @ (np.eye(self.K) * self.T) @ F)
        c = np.linalg.solve(self.Z.T @ self.Z, self.Z.T @ F) if self.Z.shape[1] < self.K else F
        x0 = float(c @ self.M0 @ c) / nrm
        xs = {n: float(c @ self.Mn[n] @ c) / nrm for n in self.contacts}
        return x0, xs


def wgt(n):
    p = {2: math.log(2), 3: math.log(3), 4: math.log(2), 5: math.log(5),
         7: math.log(7), 8: math.log(2), 9: math.log(3)}
    return p[n] / math.sqrt(n)
