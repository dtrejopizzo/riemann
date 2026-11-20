"""Direct value of W_T on a packet projected to P_T (phase 211).  NUMERICAL tool.

g0(x) = beta(x/T) cos(tau0 x) on I_T;  f = projection of g0 onto P_T = {A(f) = B(f) = 0},
A(f) = int f e^{x/2}, B(f) = int f e^{-x/2} (Paper 47 eq:W pairings, as in galerkin_mp.py).
W_T(f) = (1/2pi) int m |f^|^2 - sum_n v_n c_f(log n)   (A = B = 0 on P_T; form (3.1) of ROUND_010_A).
Arch by FFT quadrature in tau (zero padding), comb by the exact autocorrelation on the x-grid.
"""
import numpy as np, math, sys
from packet_margin import m_sym, comb, PROFILES, XS, rho_fn, Pfun

def direct(T, name, tau0, M=2**16, pad=64):
    b = PROFILES[name]()
    x = np.linspace(-T, T, M + 1); dx = x[1] - x[0]
    beta = np.interp(x / T, XS, b)
    g0 = beta * np.cos(tau0 * x)
    ep, em = np.exp(x / 2), np.exp(-x / 2)
    G = np.array([[np.trapz(ep * ep, x), np.trapz(ep * em, x)], [np.trapz(em * ep, x), np.trapz(em * em, x)]])
    rhs = np.array([np.trapz(g0 * ep, x), np.trapz(g0 * em, x)])
    c = np.linalg.solve(G, rhs); f = g0 - c[0] * ep - c[1] * em
    w = np.full(M + 1, dx); w[0] = w[-1] = dx / 2          # trapezoid weights
    nf = float(np.sum(w * f * f)); ng = float(np.sum(w * g0 * g0))
    # Fourier transform on a padded grid: f^(tau) = int f(x) e^{-i tau x} dx
    L = pad * M; F = np.fft.rfft(w * f, n=L); tau = 2 * np.pi * np.arange(F.size) / (L * dx)
    arch = 2 * np.sum(m_sym(tau[1:]) * np.abs(F[1:]) ** 2) * (tau[1] - tau[0]) / (2 * np.pi) \
           + m_sym(0.0) * abs(F[0]) ** 2 * (tau[1] - tau[0]) / (2 * np.pi)
    # comb: c_f(u) = int f(x) f(x+u) dx on the grid
    ac = np.fft.irfft(np.abs(np.fft.rfft(w * f, n=2 * (M + 1))) ** 2 / 1.0, n=2 * (M + 1))[:M + 1] / dx
    # correction: irfft of |rfft(w f)|^2 gives sum_x w f(x) w f(x+u); divide by dx to get ~ int f f(.+u)
    C = comb(T); Pi = 0.0
    for n, p, v in C:
        u = math.log(n); Pi += v * np.interp(u, np.arange(M + 1) * dx, ac)
    W = arch - Pi
    rho, _ = rho_fn(name); P, *_ = Pfun(T, rho)
    pred = float(m_sym(tau0) - P(tau0)[0])
    return dict(T=T, profile=name, tau0=tau0, W_over_norm=W / nf, pred=pred, diff=W / nf - pred,
                arch_over=arch / nf, comb_over=Pi / nf, m=float(m_sym(tau0)), Prho=float(P(tau0)[0]),
                proj_rel=math.sqrt(max(ng - nf, 0) / ng), AB=(rhs / math.sqrt(ng)).tolist())

if __name__ == '__main__':
    T, name, tau0 = float(sys.argv[1]), sys.argv[2], float(sys.argv[3])
    r = direct(T, name, tau0)
    print(' '.join(f"{k}={v:.6g}" if isinstance(v, float) else f"{k}={v}" for k, v in r.items()))
