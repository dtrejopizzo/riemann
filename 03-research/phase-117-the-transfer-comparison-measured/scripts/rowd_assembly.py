"""Physical assembly of the localized primitive operator A_T of paper 42.

Piecewise-constant basis on an explicit mesh of I_T=(-T,T).  Every matrix is
exact in closed form except the Gamma channel, which is exact up to the
truncation of an absolutely convergent series with a controlled tail.

Conventions follow main.tex eq:localizedprimitiveoperator:
    A_T = G_{Gamma,T} - m_0 I - sum_{2<=n<e^{2T}} w_n (S_{log n} + S_{-log n})
    w_n = Lambda(n)/sqrt(n),  m_0 = log pi + gamma + pi/2 + 3 log 2
and the balanced factorization thm:balancedfactorization:
    R_T = G + sum w_n (I - Re S_n),   L_T = m_0 I + sum w_n (I + Re S_n).
"""
import math
import numpy as np
from scipy.special import polygamma, exp1

EULER = 0.57721566490153286060651209008240243104215933593992
M0 = math.log(math.pi) + EULER + math.pi / 2 + 3 * math.log(2)


# ---------------------------------------------------------------- arithmetic
def von_mangoldt(N):
    """Lambda(n) for n<=N."""
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


# ------------------------------------------------------------ Gamma channel
def psi_kernel(D, J0=400):
    """Psi(D) = sum_{j>=0} exp(-a_j|D|)/a_j^2,  a_j = 2j+1/2.  Vectorized.

    Equals (1/pi) int_0^inf g_Gamma(tau) cos(tau D)/tau^2 dtau.

    Head: j < J0 summed exactly.  Tail: Euler-Maclaurin,
        sum_{j>=J0} f(j) = int_{J0}^inf f + f(J0)/2 - f'(J0)/12 + ...
    with f(j) = exp(-a_j D)/a_j^2 and, for a = a_{J0},
        int_{J0}^inf f dj = (1/2)[ exp(-aD)/a - D*E_1(a D) ].
    At D=0 this reduces to the exact sum_{j>=J0} 1/a_j^2 = (1/4) psi'(J0+1/4).
    """
    D = np.abs(np.asarray(D, dtype=float))
    scalar = (D.ndim == 0)
    D = np.atleast_1d(D)

    j = np.arange(J0)
    a = 2.0 * j + 0.5
    head = np.exp(-D[:, None] * a[None, :]) / a[None, :] ** 2
    out = head.sum(axis=1)

    aJ = 2.0 * J0 + 0.5
    fJ = np.exp(-D * aJ) / aJ**2
    # d/dj of exp(-(2j+1/2)D)/(2j+1/2)^2  at j=J0
    fpJ = np.exp(-D * aJ) * (-2.0 * D / aJ**2 - 4.0 / aJ**3)
    integral = 0.5 * (np.exp(-D * aJ) / aJ - D * exp1(np.where(D > 0, D * aJ, 1.0)))
    integral = np.where(D > 0, integral, 0.5 / aJ)
    out += integral + 0.5 * fJ - fpJ / 12.0

    # exact value at D=0 (avoids any tail-model error on the diagonal)
    out = np.where(D == 0.0, 0.25 * polygamma(1, 0.25), out)
    return float(out[0]) if scalar else out


def psi_table(deltas, tol=1e-15):
    """Psi on a set of |Delta| values (cached), vectorized."""
    uniq = np.unique(np.round(np.abs(np.asarray(deltas)), 12))
    vals = psi_kernel(uniq)
    return dict(zip(uniq.tolist(), np.atleast_1d(vals).tolist()))


# ------------------------------------------------------------------- meshing
def build_mesh(T, extra_points=(), refine=4):
    """Breakpoints on [-T,T] from +-log n and any extra points, each interval
    subdivided into `refine` equal cells.  Returns cell edges (c_i,d_i)."""
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


# ------------------------------------------------------------------ matrices
def gram_matrix(c, d):
    return np.diag(d - c)


def shift_form(c, d, a):
    """[S_a]_ij = <S_a F_j, F_i> = |[c_j-a,d_j-a] cap [c_i,d_i]|."""
    lo = np.maximum(c[:, None], c[None, :] - a)
    hi = np.minimum(d[:, None], d[None, :] - a)
    return np.maximum(hi - lo, 0.0)


def gamma_form(c, d, tol=1e-15):
    """[G]_ij = Psi(c_i-c_j) - Psi(c_i-d_j) - Psi(d_i-c_j) + Psi(d_i-d_j)."""
    allD = np.concatenate([
        (c[:, None] - c[None, :]).ravel(), (c[:, None] - d[None, :]).ravel(),
        (d[:, None] - c[None, :]).ravel(), (d[:, None] - d[None, :]).ravel()])
    tab = psi_table(allD, tol)

    def P(X):
        keys = np.round(np.abs(X), 12)
        out = np.empty_like(keys)
        flat = out.ravel()
        for i, k in enumerate(keys.ravel()):
            flat[i] = tab[k]
        return out

    return (P(c[:, None] - c[None, :]) - P(c[:, None] - d[None, :])
            - P(d[:, None] - c[None, :]) + P(d[:, None] - d[None, :]))


def tate_moments(c, d):
    """M_-(F_i)=int e^{-t/2}, M_+(F_i)=int e^{+t/2} over cell i."""
    mm = 2.0 * (np.exp(-c / 2) - np.exp(-d / 2))
    mp = 2.0 * (np.exp(d / 2) - np.exp(c / 2))
    return np.vstack([mm, mp])


# --------------------------------------------------------------- the operator
def assemble(T, refine=4, extra_points=()):
    """Return dict with mesh, Gram, Gamma, R, L, A (form matrices) and Tate."""
    c, d = build_mesh(T, extra_points, refine)
    N = int(math.floor(math.exp(2 * T)))
    G = gamma_form(c, d)
    Gram = gram_matrix(c, d)
    lam = von_mangoldt(max(N, 2))
    R = G.copy()
    L = M0 * Gram.copy()
    A = G - M0 * Gram
    for n in prime_powers_upto(max(N, 2)):
        if not (n < math.exp(2 * T) - 1e-13):
            continue
        w = lam[n] / math.sqrt(n)
        S = shift_form(c, d, math.log(n))
        sym = S + S.T                      # S_{log n} + S_{-log n}
        A -= w * sym
        R += w * (Gram - 0.5 * sym)        # w (I - Re S)
        L += w * (Gram + 0.5 * sym)        # w (I + Re S)
    return dict(c=c, d=d, Gram=Gram, G=G, R=R, L=L, A=A,
                Tate=tate_moments(c, d), T=T, N=N)
