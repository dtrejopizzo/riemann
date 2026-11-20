"""P124 laboratory: the localized Weil form of a Gamma-Euler model, its
primitive compression, the Tate block and the Schur complement Sigma(T).

This module GENERALIZES the phase-118 assembly `rowd_assembly.py` from zeta to
a family of models sharing the same analytic shape:

    W_T(F,F) = <A_T F, F> + polar(F),
    A_T      = G_{Gamma,T} - m_0 I - sum_{2<=n<e^{2T}} w_n (S_{log n}+S_{-log n}),
    polar(F) = 2 sum_{pole pairs (u,-u)} M_u(F) M_{-u}(F),
    M_u(F)   = int_{I_T} e^{u t} F(t) dt.

Models (all with their own Gamma parameters, weights and pole set):

  zeta : xi(s).                w_n = Lambda(n)/sqrt(n),
         Gamma parameter a=1/4 (one family),  poles u = +-1/2.
  xi_a : Xi_a(s)=xi(s+a)xi(s-a).  w_n = Lambda(n)(n^a+n^{-a})/sqrt(n),
         Gamma parameters a=1/4+a/2 and 1/4-a/2, poles u=+-(1/2+a), +-(1/2-a).
         Its zeros are the zeta zeros shifted by +-a, hence OFF the critical
         line for a>0 (under RH).  It is the shifted-pair falsifier of
         P122_D_SPECIFICATION section 5.
  dh   : Davenport-Heilbronn.  Functional equation, no Euler product; used
         QUALITATIVELY only (RH2017_RH9_AUDIT retires it as a quantitative
         control).

Everything is a real symmetric form matrix in the piecewise-constant Galerkin
basis of `rowd_assembly.build_mesh`.  No positivity, no zero of zeta and no
row-(d) statement is used anywhere in this file.

Conventions are those of paper 42 eq:localizedprimitiveoperator and
P123_036 (1.1):  q_T(F) = <A_T F,F> is the PRIMITIVE form (row d target) and
W_T is the FULL Weil form including the polar packet.
"""
import math
import numpy as np
from scipy.special import polygamma, exp1, digamma


# ------------------------------------------------------------------ arithmetic
def von_mangoldt(N):
    lam = [0.0] * (N + 1)
    sieve = [True] * (N + 1)
    for p in range(2, N + 1):
        if sieve[p]:
            for m in range(p * p, N + 1, p):
                sieve[m] = False
            q, lp = p, math.log(p)
            while q <= N:
                lam[q] = lp
                q *= p
    return lam


def prime_powers_upto(N):
    lam = von_mangoldt(N)
    return [n for n in range(2, N + 1) if lam[n] > 0]


def dirichlet_inverse(a, N):
    b = np.zeros(N + 1)
    b[1] = 1.0 / a[1]
    for n in range(2, N + 1):
        s, d = 0.0, 1
        while d * d <= n:
            if n % d == 0:
                e = n // d
                if d != n:
                    s += a[e] * b[d]
                if e != n and e != d:
                    s += a[d] * b[e]
            d += 1
        b[n] = -s / a[1]
    return b


def dh_lambda(N):
    """Lambda_DH(n): coefficients of -f'/f for the Davenport-Heilbronn series.

    Same construction as phase-119 scripts/dh_contact.py (period 5, kappa the
    standard constant).  Kept here so the lab is self-contained.
    """
    kappa = (math.sqrt(10 - 2 * math.sqrt(5)) - 2) / (math.sqrt(5) - 1)
    per = [0.0, 1.0, kappa, -kappa, -1.0, 0.0]
    a = np.zeros(N + 1)
    for n in range(1, N + 1):
        r = n % 5
        a[n] = per[5] if r == 0 else per[r]
    alog = np.array([0.0] + [a[n] * math.log(n) for n in range(1, N + 1)])
    return dirichlet_conv(alog, dirichlet_inverse(a, N), N)


def dirichlet_conv(a, b, N):
    c = np.zeros(N + 1)
    for d in range(1, N + 1):
        if a[d] == 0:
            continue
        for e in range(1, N // d + 1):
            c[d * e] += a[d] * b[e]
    return c


# --------------------------------------------------------------- Gamma channel
def psi_kernel(D, b0, J0=400):
    """Psi_{b0}(D) = sum_{j>=0} exp(-a_j|D|)/a_j^2 with a_j = 2j + b0.

    Second differences of Psi_{b0} over mesh cells give the form matrix of the
    multiplier g(tau) = sum_j [2/a_j - 2a_j/(a_j^2+tau^2)], i.e. of
    Re psi(b0/2 + i tau/2) - psi(b0/2).   b0 = 1/2 recovers the zeta case of
    `rowd_assembly.psi_kernel`.
    """
    D = np.abs(np.asarray(D, dtype=float))
    scalar = (D.ndim == 0)
    D = np.atleast_1d(D)

    j = np.arange(J0)
    a = 2.0 * j + b0
    out = (np.exp(-D[:, None] * a[None, :]) / a[None, :] ** 2).sum(axis=1)

    aJ = 2.0 * J0 + b0
    fJ = np.exp(-D * aJ) / aJ ** 2
    fpJ = np.exp(-D * aJ) * (-2.0 * D / aJ ** 2 - 4.0 / aJ ** 3)
    integral = 0.5 * (np.exp(-D * aJ) / aJ - D * exp1(np.where(D > 0, D * aJ, 1.0)))
    integral = np.where(D > 0, integral, 0.5 / aJ)
    out += integral + 0.5 * fJ - fpJ / 12.0
    out = np.where(D == 0.0, 0.25 * polygamma(1, b0 / 2.0), out)
    return float(out[0]) if scalar else out


def gamma_form(c, d, b0):
    """[G]_ij = Psi(c_i-c_j) - Psi(c_i-d_j) - Psi(d_i-c_j) + Psi(d_i-d_j)."""
    pairs = [(c[:, None] - c[None, :], +1.0), (c[:, None] - d[None, :], -1.0),
             (d[:, None] - c[None, :], -1.0), (d[:, None] - d[None, :], +1.0)]
    allD = np.concatenate([np.abs(X).ravel() for X, _ in pairs])
    uniq = np.unique(np.round(allD, 12))
    tab = dict(zip(uniq.tolist(), np.atleast_1d(psi_kernel(uniq, b0)).tolist()))

    def P(X):
        keys = np.round(np.abs(X), 12)
        out = np.empty_like(keys)
        flat = out.ravel()
        for i, k in enumerate(keys.ravel()):
            flat[i] = tab[k]
        return out

    return sum(sgn * P(X) for X, sgn in pairs)


# -------------------------------------------------------------------- meshing
def build_mesh(T, refine=4, extra_points=()):
    """Cell edges of I_T=(-T,T) breaking at every +-log n and extra point."""
    N = int(math.floor(math.exp(2 * T)))
    pts = {-T, T, 0.0}
    for n in prime_powers_upto(max(N, 2)):
        for s in (+1, -1):
            x = s * math.log(n)
            if -T < x < T:
                pts.add(x)
    for x in extra_points:
        if -T < x < T:
            pts.add(x)
    base = np.array(sorted(pts))
    edges = []
    for lo, hi in zip(base[:-1], base[1:]):
        edges.extend(np.linspace(lo, hi, refine + 1)[:-1])
    edges.append(base[-1])
    edges = np.array(edges)
    return edges[:-1], edges[1:]


def shift_form(c, d, a):
    """[S_a]_ij = <S_a F_j, F_i> = |[c_j-a,d_j-a] cap [c_i,d_i]|."""
    lo = np.maximum(c[:, None], c[None, :] - a)
    hi = np.minimum(d[:, None], d[None, :] - a)
    return np.maximum(hi - lo, 0.0)


def exp_moments(c, d, u):
    """M_u(F_i) = int_{c_i}^{d_i} e^{u t} dt, for the cell indicator basis."""
    if abs(u) < 1e-14:
        return d - c
    return (np.exp(u * d) - np.exp(u * c)) / u


# --------------------------------------------------------------------- models
class Model:
    """A Gamma-Euler model: Gamma parameters, prime weights and pole pairs."""

    def __init__(self, name, gamma_b0, m0, weight_fn, pole_us, has_euler=True):
        self.name = name
        self.gamma_b0 = list(gamma_b0)   # list of b0 for each Gamma family
        self.m0 = m0                     # constant subtracted (log pi terms)
        self.weight_fn = weight_fn       # n -> w_n
        self.pole_us = list(pole_us)     # list of u>0; each gives a pair (u,-u)
        self.has_euler = has_euler


def model_zeta():
    m0 = math.log(math.pi) - digamma(0.25)
    lam_cache = {}

    def w(n, N):
        if N not in lam_cache:
            lam_cache[N] = von_mangoldt(N)
        return lam_cache[N][n] / math.sqrt(n)

    return Model("zeta", [0.5], m0, w, [0.5])


def model_xi_a(a):
    """Xi_a(s) = xi(s+a) xi(s-a);  zeros off the critical line for a>0."""
    if not (0.0 <= a < 0.5):
        raise ValueError("need 0 <= a < 1/2")
    m0 = 2 * math.log(math.pi) - digamma(0.25 + a / 2) - digamma(0.25 - a / 2)
    lam_cache = {}

    def w(n, N):
        if N not in lam_cache:
            lam_cache[N] = von_mangoldt(N)
        return lam_cache[N][n] * (n ** a + n ** (-a)) / math.sqrt(n)

    return Model("xi_a[a=%g]" % a, [0.5 + a, 0.5 - a], m0, w, [0.5 + a, 0.5 - a])


def model_dh():
    """Davenport-Heilbronn.  Functional equation with the same Gamma type as a
    Dirichlet L-function mod 5 (odd character combination); NO Euler product,
    NO poles.  Used qualitatively only."""
    lam_cache = {}

    def w(n, N):
        if N not in lam_cache:
            lam_cache[N] = dh_lambda(N)
        return lam_cache[N][n] / math.sqrt(n)

    # DH is entire: no polar packet at all.  Gamma factor of an odd character
    # mod 5 gives parameter 3/4 in our normalization (b0 = 3/2).
    m0 = math.log(5.0 / math.pi) - digamma(0.75)
    return Model("dh", [1.5], m0, w, [], has_euler=False)


MODELS = {"zeta": model_zeta, "xi_a": model_xi_a, "dh": model_dh}


# ------------------------------------------------------------------- assembly
def assemble(model, T, refine=4):
    """All form matrices on the mesh of I_T.

    Returns dict with:
      c,d    cell edges;  Gram = diag(d-c)
      A      form matrix of A_T  (the PRIMITIVE operator before compression)
      Tate   (k,N) matrix of the pole moments M_u, u running over
             [+u for u in pole_us] + [-u for u in pole_us]
      Polar  (N,N) form matrix of the polar packet
      W      A + Polar   (full Weil form matrix)
    """
    c, d = build_mesh(T, refine)
    N = int(math.floor(math.exp(2 * T)))
    Gram = np.diag(d - c)

    A = -model.m0 * Gram.copy()
    for b0 in model.gamma_b0:
        A += gamma_form(c, d, b0)

    ns = [n for n in prime_powers_upto(max(N, 2)) if n < math.exp(2 * T) - 1e-13]
    ws = {}
    for n in ns:
        wn = model.weight_fn(n, max(N, 2))
        ws[n] = wn
        if wn == 0.0:
            continue
        S = shift_form(c, d, math.log(n))
        A -= wn * (S + S.T)

    us = [+u for u in model.pole_us] + [-u for u in model.pole_us]
    Tate = np.vstack([exp_moments(c, d, u) for u in us]) if us else np.zeros((0, len(c)))

    # polar packet = 2 * sum over pole pairs of M_u(F) M_{-u}(F)
    Polar = np.zeros_like(Gram)
    for k, u in enumerate(model.pole_us):
        mp = Tate[k]
        mm = Tate[k + len(model.pole_us)]
        Polar += np.outer(mp, mm) + np.outer(mm, mp)

    return dict(model=model.name, T=T, refine=refine, c=c, d=d, Gram=Gram,
                A=A, Tate=Tate, us=us, Polar=Polar, W=A + Polar, ns=ns, ws=ws)


# ------------------------------------------------- primitive / Tate splitting
def primitive_basis(Tate, Gram, rtol=1e-11):
    """Gram-orthonormal basis Z of P_T = ker(Tate):  Z^T Gram Z = I."""
    if Tate.shape[0] == 0:
        w, V = np.linalg.eigh(Gram)
        return V * (1.0 / np.sqrt(w))
    u, s, vt = np.linalg.svd(Tate)
    k = int(np.sum(s > rtol * max(s.max(), 1e-300)))
    Zraw = vt[k:].T
    Gq = Zraw.T @ Gram @ Zraw
    wq, Vq = np.linalg.eigh(0.5 * (Gq + Gq.T))
    keep = wq > 1e-12 * max(wq.max(), 1e-300)
    Gq_isqrt = (Vq[:, keep] * (1.0 / np.sqrt(wq[keep]))) @ Vq[:, keep].T
    return Zraw @ Gq_isqrt


def tate_basis(Tate, Gram, rtol=1e-11):
    """Gram-orthonormal basis Y of the span of the pole representers e^{u t}
    (the Gram-orthogonal complement of P_T)."""
    if Tate.shape[0] == 0:
        return np.zeros((Gram.shape[0], 0))
    # representer of M_u in the Gram metric is Gram^{-1} Tate[k]
    R = np.linalg.solve(Gram, Tate.T)          # (N,k)
    Gq = R.T @ Gram @ R
    wq, Vq = np.linalg.eigh(0.5 * (Gq + Gq.T))
    keep = wq > 1e-12 * max(wq.max(), 1e-300)
    return R @ (Vq[:, keep] * (1.0 / np.sqrt(wq[keep])))


def blocks(asm, rtol=1e-11):
    """The Schur data of the full Weil form in the splitting P_T (+) Tate.

    L    = primitive compression of A_T          (dim P x dim P)
    X    = crossblock <W phi, F>                 (dim P x k)
    B    = Tate block of W                       (k x k)
    Both blocks are taken of the FULL form W; on P_T the polar packet vanishes,
    so the (1,1) block of W equals the (1,1) block of A_T, i.e. L_T.
    """
    Gram, W, A, Tate = asm['Gram'], asm['W'], asm['A'], asm['Tate']
    Z = primitive_basis(Tate, Gram, rtol)
    Y = tate_basis(Tate, Gram, rtol)
    L = Z.T @ A @ Z
    L = 0.5 * (L + L.T)
    X = Z.T @ W @ Y
    B = Y.T @ W @ Y
    B = 0.5 * (B + B.T)
    # rho_u = primitive part of the collar column, in the Z coordinates
    return dict(Z=Z, Y=Y, L=L, X=X, B=B, dimP=Z.shape[1], k=Y.shape[1])


def schur(L, X, B, tol=1e-11):
    """Sigma = B - X^T L^dagger X, plus the range obstruction ||Pi_ker X||.

    Returns (Sigma, ker_norm, lam_min_L, cond_note).  Sigma is computed on the
    pseudo-inverse of L restricted to its numerically nonzero eigenvalues.
    """
    w, V = np.linalg.eigh(0.5 * (L + L.T))
    scale = max(abs(w).max(), 1e-300)
    small = np.abs(w) <= tol * scale
    XV = V.T @ X
    ker_norm = float(np.linalg.norm(XV[small])) if small.any() else 0.0
    inv = np.where(small, 0.0, 1.0 / np.where(small, 1.0, w))
    Sigma = B - XV.T @ (inv[:, None] * XV)
    return 0.5 * (Sigma + Sigma.T), ker_norm, float(w.min()), int(small.sum())
