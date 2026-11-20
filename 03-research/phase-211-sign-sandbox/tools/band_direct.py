"""Direct, independent evaluation of a_T and W_T on f = beta cos(tau x), beta = top eigenvector of A_tau^{(eta)}
(phase 211, ROUND_017_B).  NUMERICAL tool.

beta(x) = sum_k b_k sin(a_k(x+T))/sqrt T is evaluated EXACTLY on the uniform grid x_i = -T + 2T i/M by DST-I, and
beta(x+l) by the addition formula (DST of b cos(a l) + DCT-I of b sin(a l)), set to 0 outside [-T,T].
f0 = beta cos(tau x); f = P_T f0 = f0 - c+ e^{x/2} - c- e^{-x/2} (Gram solve).
Comb:   sum_n v_n c_f(l_n), c_f(l) = int f(x) f(x+l) dx by trapezoid with exact shifted samples (no interpolation).
Arch 1 (FFT):  (1/2pi) int m |f^|^2 by zero-padded FFT of trapezoid-weighted samples.
Arch 2 (Levy): m(0)||f||^2 + int_0^inf 2 e^{-u/2}(||f||^2 - c_f(u))/(1-e^{-2u}) du  (from psi(s) = -gamma +
        int_0^inf (e^{-t}-e^{-st})/(1-e^{-t}) dt, s = 1/4 + i xi/2; c_f(u) = 0 for u > 2T), c_f(u) on the grid
        u_j = 2T j/M by exact discrete correlation (FFT), integral by trapezoid + analytic tail.
Returns per ||.||^2: lam, m - lam, Q (unprojected), W (projected), D+X (= 2 arch/||b||^2 - m), R, projection loss."""
import sys, math, numpy as np
from scipy.fft import dst, dct
from scipy.integrate import quad
from scipy.special import psi
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from band_lanczos import Band, m_sym

def sample(b, T, M, shift=0.0):
    K = len(b); a = (math.pi / (2 * T)) * np.arange(1, K + 1)
    bc, bs = np.zeros(M + 1), np.zeros(M + 1)
    bc[1:K + 1] = b * np.cos(a * shift); bs[1:K + 1] = b * np.sin(a * shift)
    # sum_k c_k sin(k pi i/M), i=0..M : DST-I on interior points (length M-1), via type-1 transforms
    S = np.zeros(M + 1); S[1:M] = dst(bc[1:M], type=1) / 2
    C = dct(bs, type=1) / 2 - (bs[0] + bs[M] * (-1.0) ** np.arange(M + 1)) / 2  # sum_{k=1}^{M-1} bs_k cos(k pi i/M)
    y = (S + C) / math.sqrt(T); x = -T + 2 * T * np.arange(M + 1) / M
    y[(x + shift > T + 1e-14) | (x + shift < -T - 1e-14)] = 0.0
    return y

def evaluate(T, tau, eta, M=2**18, pad=8, b=None, scale=1.0):
    B = Band(T, int(2 * T * eta * tau / math.pi) + 2, scale)
    if b is None: lam, b, res, K = B.top(tau, eta, tol=1e-13)
    else:
        B.set_tau(tau, len(b)); B._prep(len(b)); B.set_tau(tau, len(b)); lam = float(b @ B.A(b)) / float(b @ b); res = np.nan
    b = b / np.linalg.norm(b)
    h = 2 * T / M; x = -T + h * np.arange(M + 1); w = np.full(M + 1, h); w[0] = w[-1] = h / 2
    beta = sample(b, T, M); cosx = np.cos(tau * x); f0 = beta * cosx
    ep, em = np.exp(x / 2), np.exp(-x / 2)
    G = np.array([[np.sum(w*ep*ep), np.sum(w*ep*em)], [np.sum(w*em*ep), np.sum(w*em*em)]])
    cc = np.linalg.solve(G, [np.sum(w*f0*ep), np.sum(w*f0*em)])
    nb = float(np.sum(w * beta**2)); mt = float(m_sym(tau))
    out = dict(T=T, tau=tau, eta=eta, K=len(b), lam=lam, m=mt, margin=mt - lam, lanczos_res=res, normb_quad=nb)
    for tag, proj in (('Q', False), ('W', True)):
        f = f0 - cc[0]*ep - cc[1]*em if proj else f0
        nf = float(np.sum(w * f * f))
        # comb with exact shifted samples
        comb = 0.0
        for ln, v in zip(B.ln, B.v):
            bsh = sample(b, T, M, ln); fsh = bsh * np.cos(tau * (x + ln))
            if proj: fsh = fsh - (cc[0]*np.exp((x+ln)/2) + cc[1]*np.exp(-(x+ln)/2)) * (x + ln <= T + 1e-14)
            comb += v * np.sum(w * f * fsh)
        # arch, FFT
        L = pad * (M + 1); F = np.fft.rfft(w * f, n=L); t = 2*np.pi*np.arange(F.size)/(L*h); dt = t[1] - t[0]
        a1 = (2*np.sum(m_sym(t[1:])*np.abs(F[1:])**2) + m_sym(0.0)*abs(F[0])**2) * dt / (2*np.pi)
        # arch, Levy form
        n2 = 1 << int(math.ceil(math.log2(2 * (M + 1))))
        # trapezoid correlation c(u_j) = h sum_i f_i f_{i+j} (endpoint correction O(h f(T)^2), f(+-T) = O(proj))
        cf = np.fft.irfft(np.abs(np.fft.rfft(f, n2))**2, n2)[:M + 1] * h
        u = h * np.arange(M + 1); g = np.empty(M + 1)
        g[1:] = 2*np.exp(-u[1:]/2)*(cf[0] - cf[1:])/(-np.expm1(-2*u[1:])); g[0] = 0.0
        lev = np.sum(g[1:-1]) * h + 0.5 * h * g[-1]
        tail = cf[0] * quad(lambda s: 2*math.exp(-s/2)/(-math.expm1(-2*s)), 2*T, np.inf)[0]
        a2 = float(m_sym(0.0)) * cf[0] + lev + tail
        out[tag + '_fft'] = (a1 - comb) / nf; out[tag + '_levy'] = (a2 - comb) / nf
        if not proj:
            out['D+X_fft'] = 2 * a1 / nb - mt; out['D+X_levy'] = 2 * a2 / nb - mt; out['minusR'] = -(2 * comb / nb - lam)
        else: out['proj_loss'] = 1 - nf / float(np.sum(w * f0 * f0))
    return out

if __name__ == '__main__':
    T, tau, eta = map(float, sys.argv[1:4]); M = int(sys.argv[4]) if len(sys.argv) > 4 else 2**18
    r = evaluate(T, tau, eta, M)
    print(' '.join(f"{k}={v:.7g}" if isinstance(v, float) else f"{k}={v}" for k, v in r.items()), flush=True)
