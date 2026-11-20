"""Direct W_T on g = (top eigenvector of A_tau) * cos(tau x), projected to P_T (phase 211, ROUND_015_C).  NUMERICAL tool.

f = top eigenvector of the Nb-mode sine-Galerkin matrix of A_tau (tools/A_tau_lmax.py), evaluated on a fine x-grid;
g0 = f cos(tau x) (and, as a control, g0 = f itself); g = projection of g0 onto P_T = {int g e^{+-x/2} = 0}.
W_T(g) = (1/2pi) int m |g^|^2 - sum_n v_n c_g(log n)   (pole pairings vanish on P_T), as in tools/packet_direct.py.
Arch by zero-padded FFT quadrature, comb by exact grid autocorrelation (linear interpolation in u).
Also reports the spectral content of f (fraction of |f^|^2 above frequency tau/2), which controls the packet reduction.
"""
import math, sys
import numpy as np
from A_tau_lmax import ATau, m_sym, comb

def direct(T, tau, Nb=400, M=2**15, pad=32, modulate=True):
    op = ATau(T, Nb); A = op.matrix(tau); A = 0.5 * (A + A.T)
    w_, V = np.linalg.eigh(A); lam = w_[-1]; co = V[:, -1]
    x = np.linspace(-T, T, M + 1); dx = x[1] - x[0]
    k = np.arange(1, Nb + 1)
    f = np.zeros_like(x)
    for i0 in range(0, M + 1, 4096):
        sl = slice(i0, i0 + 4096)
        f[sl] = np.sin(np.outer(x[sl] + T, k) * math.pi / (2 * T)) @ co / math.sqrt(T)
    g0 = f * np.cos(tau * x) if modulate else f.copy()
    wq = np.full(M + 1, dx); wq[0] = wq[-1] = dx / 2
    ep, em = np.exp(x / 2), np.exp(-x / 2)
    G = np.array([[np.sum(wq*ep*ep), np.sum(wq*ep*em)], [np.sum(wq*em*ep), np.sum(wq*em*em)]])
    rhs = np.array([np.sum(wq*g0*ep), np.sum(wq*g0*em)])
    c = np.linalg.solve(G, rhs); g = g0 - c[0]*ep - c[1]*em
    ng0 = float(np.sum(wq*g0*g0)); ng = float(np.sum(wq*g*g))
    L = pad * (M + 1); F = np.fft.rfft(wq*g, n=L); t = 2*np.pi*np.arange(F.size)/(L*dx); dt = t[1]-t[0]
    arch = (2*np.sum(m_sym(t[1:])*np.abs(F[1:])**2) + m_sym(0.0)*abs(F[0])**2) * dt / (2*np.pi)
    ac = np.fft.irfft(np.abs(np.fft.rfft(wq*g, n=2*(M+1)))**2, n=2*(M+1))[:M+1] / dx
    Pi = sum(v*np.interp(math.log(n), np.arange(M+1)*dx, ac) for n, p, v in comb(T))
    Ff = np.abs(np.fft.rfft(wq*f, n=L))**2
    hi = float(np.sum(Ff[t > tau/2]) / np.sum(Ff))
    return dict(T=T, tau=tau, Nb=Nb, lam=lam, m=float(m_sym(tau)), pred=float(m_sym(tau))-lam,
                W=(arch-Pi)/ng, arch=arch/ng, comb=Pi/ng, proj_loss=1-ng/ng0, f_hifreq=hi)

if __name__ == '__main__':
    T, tau = float(sys.argv[1]), float(sys.argv[2]); Nb = int(sys.argv[3]) if len(sys.argv) > 3 else 400
    for mod in (True, False):
        r = direct(T, tau, Nb, modulate=mod)
        print('modulated' if mod else 'bare', ' '.join(f"{a}={b:.6g}" for a, b in r.items()))
