"""Phase 155 round 2 -- shared double-precision machinery for the test-kernel ceiling.

Ceil(M,T) = sup_beta inf_{tau0} lambda_min(C_M(tau0,beta)),  C_M Hermitian Toeplitz with
c_l = P^{-1} int_{tau0}^{tau0+P} S_beta(tau) e^{i l d tau} dtau,  d = 2T/M, P = 2pi/d.
S_beta = sigma_T + beta0*g0hat + beta1*g1hat.  Affine in beta, so the three coefficient
families are precomputed once per (M,tau0) and reassembled for each beta.

Everything here is DOUBLE PRECISION and therefore DIAGNOSTIC.  The rigorous enclosure
lives in r2_a_enclosure.py.
"""
import numpy as np
from scipy.special import digamma
from scipy.linalg import toeplitz


def contacts(T):
    """N_T = {n>=2 : log n < 2T} with weights v_n = 2*Lambda(n)/sqrt(n)."""
    out = {}
    N = int(np.floor(np.exp(2.0 * T))) + 2
    for p in range(2, N + 1):
        if all(p % k for k in range(2, int(p ** 0.5) + 1)):
            q = p
            while np.log(q) < 2.0 * T - 1e-15:
                out[q] = 2.0 * np.log(p) / np.sqrt(q)
                q *= p
    return out


def m_arch(t):
    return np.real(digamma(0.25 + 0.5j * np.asarray(t))) - np.log(np.pi)


def make_S_parts(T):
    """Return (sigma_T, g0hat, g1hat) as vectorised callables."""
    cts = contacts(T)
    a = 2.0 * T

    def sigma(t):
        t = np.asarray(t, dtype=float)
        s = m_arch(t)
        for n, v in cts.items():
            s = s - v * np.cos(t * np.log(n))
        return s

    def I(s, t):           # int_0^a e^{s u} cos(t u) du
        c, sn = np.cos(t * a), np.sin(t * a)
        return (np.exp(s * a) * (s * c + t * sn) - s) / (s * s + t * t)

    def dIds(s, t):        # d/ds of the above
        c, sn = np.cos(t * a), np.sin(t * a)
        E = np.exp(s * a)
        D = s * s + t * t
        num = a * E * (s * c + t * sn) + E * c - 1.0
        return num / D - 2.0 * s * (E * (s * c + t * sn) - s) / D ** 2

    def g0h(t):
        t = np.asarray(t, dtype=float)
        return I(0.5, t) + I(-0.5, t)

    def g1h(t):
        t = np.asarray(t, dtype=float)
        return dIds(0.5, t) - dIds(-0.5, t)

    return sigma, g0h, g1h, cts


def coeff_families(T, M, tau0, n=1 << 16, parts=None):
    """Composite Simpson on one period, evaluated by one FFT per family.
    Returns three arrays of M complex Fourier coefficients c_l, l=0..M-1,
    for sigma_T, g0hat, g1hat."""
    if parts is None:
        parts = make_S_parts(T)[:3]
    d = 2.0 * T / M
    P = 2.0 * np.pi / d
    x = np.linspace(tau0, tau0 + P, n + 1)
    w = np.ones(n + 1)
    w[1:-1:2] = 4.0
    w[2:-1:2] = 2.0
    w *= (P / n) / 3.0
    ph0 = np.exp(1j * d * tau0 * np.arange(M))
    out = []
    for f in parts:
        fv = f(x) * w
        y = fv[:n].copy()
        y[0] += fv[n]                      # e^{i l d x_n} = e^{i l d x_0}
        F = np.fft.ifft(y) * n             # F[l] = sum_j y_j e^{2 pi i l j / n}
        out.append(F[:M] * ph0 / P)
    return out


def lam_min(cs_parts, beta):
    cs = cs_parts[0] + beta[0] * cs_parts[1] + beta[1] * cs_parts[2]
    C = toeplitz(np.conj(cs), cs)          # C[k,j] = c_{j-k}
    w, V = np.linalg.eigh(C)
    return w[0], V[:, 0]
