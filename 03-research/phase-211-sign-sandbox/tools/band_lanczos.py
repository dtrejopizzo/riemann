"""Matrix-free top eigenvalue of the band compression A_tau^{(eta)} (phase 211, ROUND_017_B).  NUMERICAL tool.

Closed form (from the shift matrix of tools/A_tau_lmax.py, s = l > 0, a_k = k pi/2T, eps_k = (-1)^k):
  2T <e_j, Sh(l) e_k> = (sigma_k - eps_j eps_k sigma_j)/(a_j - a_k)  [j != k]
                      + (sigma_k + eps_j eps_k sigma_j)/(a_j + a_k)
                      + delta_jk (2T - l) cos(a_k l),          sigma_k = sin(a_k l).
Summing over n with c_n = v_n cos(tau l_n) only the vectors s1_k = sum c_n sin(a_k l_n) and
d_k = sum c_n (2T - l_n) cos(a_k l_n) survive:  E = (1/2T)[C S - De S C De + De S H De + H S + Dd],
C_jk = 1/(a_j - a_k) (Toeplitz, zero diagonal), H_jk = 1/(a_j + a_k) (Hankel), S = diag(s1), De = diag(eps),
and A_tau = (E + E^T)/2 on span{e_1..e_K}.  Matvec O(K log K) by FFT; top eigenpair by Lanczos (eigsh).
"""
import math, sys
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
from scipy.special import psi
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from A_tau_lmax import comb

def m_sym(t): return psi(0.25 + 0.5j * np.asarray(t, float)).real - math.log(math.pi)

class Band:
    def __init__(self, T, Kmax, scale=1.0):
        self.T = T; C = comb(T, scale)
        self.ln = np.array([math.log(n) for n, _, _ in C]); self.v = np.array([v for _, _, v in C])
        self.Kmax = Kmax; h = math.pi / (2 * T)
        aa = h * np.arange(1, Kmax + 1)
        self.SCm = np.sin(np.outer(aa, self.ln)); self.CCm = np.cos(np.outer(aa, self.ln))
        self.K = None
    def _prep(self, K):
        if K > self.Kmax: raise ValueError('K > Kmax')
        T = self.T; self.K = K; h = math.pi / (2 * T)
        self.a = h * np.arange(1, K + 1); self.eps = (-1.0) ** np.arange(1, K + 1)
        L = 1 << int(math.ceil(math.log2(2 * K + 2))); self.L = L  # >= 2K: no circular wrap for Toeplitz (|j-k| < K) or aligned Hankel (index <= 2K-2)
        # Toeplitz kernel t[m] = 1/(h m), m = j-k in [-(K-1), K-1], m != 0
        t = np.zeros(L); m = np.arange(1, K); t[m] = 1 / (h * m); t[L - m] = -1 / (h * m)
        self.Ft = np.fft.rfft(t)
        # Hankel: H_jk = 1/(h (j+k)), j+k in [2, 2K]; (Hx)_j = sum_k g[j+k] x_k
        g = np.zeros(L); s = np.arange(2, 2 * K + 1); g[s] = 1 / (h * s); self.Fg = np.fft.rfft(g)
        self.Fg2 = np.fft.rfft(np.roll(g, -2))  # g'[i] = g[i+2]: Hankel output aligned with Toeplitz output (index j-1)
        self.SC = self.SCm[:K]; self.CC = self.CCm[:K]
    def _C(self, x):
        return np.fft.irfft(np.fft.rfft(x, self.L) * self.Ft, self.L)[:self.K]
    def _H(self, x):
        # (Hx)_j = sum_k g[j+k] x_k, indices j,k from 1: use reversed x
        K = self.K; xr = np.zeros(self.L); xr[:K] = x[::-1]  # xr[K-k] = x_k (k=1..K) -> position K-k
        y = np.fft.irfft(np.fft.rfft(xr, self.L) * self.Fg, self.L)
        # sum_k g[j+k] xr[K-k]: conv index (j+k)+(K-k) = j+K
        return y[np.arange(1, K + 1) + K]
    def set_tau(self, tau, K):
        if K != self.K: self._prep(K)
        c = self.v * np.cos(tau * self.ln)
        self.s1 = self.SC @ c; self.dd = self.CC @ (c * (2 * self.T - self.ln))
    def E(self, x):
        s, e = self.s1, self.eps
        return (self._C(s * x) - e * s * self._C(e * x) + e * s * self._H(e * x) + self._H(s * x) + self.dd * x) / (2 * self.T)
    def Et(self, x):
        s, e = self.s1, self.eps
        return (-s * self._C(x) + e * self._C(s * e * x) + e * self._H(s * e * x) + s * self._H(x) + self.dd * x) / (2 * self.T)
    def A(self, x):
        # fused: 4 forward + 4 inverse FFTs. C x = irfft(Ft X); H x = irfft(Fg conj(X)) read at index j+1 (correlation),
        # since (Hx)_j = sum_k g[j+k] x_k with x stored at positions k-1.
        s, e, K, L = self.s1, self.eps, self.K, self.L
        X = np.fft.rfft(np.stack([s * x, e * x, x, s * e * x]), L, axis=1)
        Ft, Fg = self.Ft, self.Fg2
        Y = np.stack([Ft * X[0] + Fg * np.conj(X[0]), -Ft * X[1] + Fg * np.conj(X[1]),
                      -Ft * X[2] + Fg * np.conj(X[2]), Ft * X[3] + Fg * np.conj(X[3])])
        y = np.fft.irfft(Y, L, axis=1)
        y = y[:, :K]
        return (y[0] + e * s * y[1] + s * y[2] + e * y[3] + 2 * self.dd * x) / (4 * self.T)
    def top(self, tau, eta, v0=None, tol=1e-9):
        K = int(math.floor(2 * self.T * eta * tau / math.pi)); self.set_tau(tau, K)
        op = LinearOperator((K, K), matvec=self.A, dtype=float)
        # warm start alone can lock Lanczos onto a non-top eigenvector (observed: 6% of points at T = 2.5);
        # mix the previous vector with an equal-norm random vector.
        rng = np.random.default_rng(int(tau * 1000) % (2**32))
        r = rng.standard_normal(K); r /= np.linalg.norm(r)
        if v0 is None: v0 = r
        else:
            v0 = np.resize(v0, K) if len(v0) < K else v0[:K]; v0 = v0 / np.linalg.norm(v0) + r
        w, V = eigsh(op, k=1, which='LA', v0=v0, tol=tol, ncv=min(K - 1, 40))
        x = V[:, 0]; res = np.linalg.norm(self.A(x) - w[0] * x)
        return float(w[0]), x, res, K
