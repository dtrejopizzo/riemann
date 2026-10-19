"""(4) rango de g -> Q_g[b]/||g||^2 y de g -> D(g)/||g||^2 sobre P_T (float, Legendre grado < N, Gauss);
(5) Q_{g*}[b] en el extremal de Mori mu=15. NUMERICO."""
import os, sys, json, numpy as np
from numpy.polynomial import legendre as leg
HERE = os.path.dirname(os.path.abspath(__file__))
L2 = {4: 2*np.log(2)/2*1, 6: 2*np.log(6), 9: 2*np.log(9), 14: 2*np.log(14), 16: (2/3)/2*np.log(16)*1, 21: 4*np.log(21), 24: (4/3)/2*np.log(24)}
L2[4] = 0.5*1*np.log(4)  # (b*b)(4)=b_2^2=1
L2[16] = 0.5*(2/3)*np.log(16)  # 2 b_2 b_8 = 2/3
L2[24] = 0.5*(4/3)*np.log(24)  # 2 b_3 b_8 = 4/3
Lc = {4: np.log(2), 6: 2*np.log(6), 9: 2*np.log(9), 14: 2*np.log(14), 16: np.log(2), 21: 4*np.log(21)}  # exact, n<=24
def mats(T, N, nodes=400):
    x, wq = leg.leggauss(nodes)
    def B(t):  # basis values at t (array), zero outside [-T,T]
        V = leg.legvander(np.clip(t / T, -1, 1), N - 1); V[np.abs(t) > T] = 0; return V
    t = T * x; Wt = T * wq; V0 = B(t)
    G = V0.T @ (Wt[:, None] * V0)
    def A(u):  # c_g(u) = int g(t) g(t+u) dt, symmetrized
        tt = (T - u / 2) * x - u / 2; ww = (T - u / 2) * wq  # t in [-T, T-u]
        M = B(tt).T @ (ww[:, None] * B(tt + u)); return (M + M.T) / 2
    tate = np.array([V0.T @ (Wt * np.exp(t / 2)), V0.T @ (Wt * np.exp(-t / 2))])
    return G, A, tate
def extremes(T, N, comb):
    G, A, tate = mats(T, N)
    Qm = sum(-2 * a / np.sqrt(n) * A(np.log(n)) for n, a in comb.items() if np.log(n) < 2 * T)  # D-type: -sum 2a c/sqrt n
    _, _, Vt = np.linalg.svd(tate); Z = Vt[2:].T  # null space of Tate conditions = P_T
    Gz, Qz = Z.T @ G @ Z, Z.T @ Qm @ Z
    Lc_ = np.linalg.cholesky(Gz); Li = np.linalg.inv(Lc_)
    e = np.linalg.eigvalsh(Li @ Qz @ Li.T); return e.min(), e.max()
for T in (1.0, 1.6, 2.0):
    print('T=%.2f  -Q_g[b]/||g||^2 in [%.4f, %.4f];  D(g)/||g||^2 in [%.4f, %.4f]' % ((T,) + extremes(T, 30, L2) + extremes(T, 30, Lc)))
# Mori g*
D = os.path.join(HERE, '../../phase-199-frontier-pattern/proof-L-sharp/MORI15_EXTREMAL_001_data')
E = json.load(open(os.path.join(D, 'p0_eig.json'))); v = np.array([float(z) for z in E['vectors'][0]])
Lh = np.log(15) / 2; Nn = 1664; coef = np.zeros(Nn)
for t, j in enumerate(range(0, Nn, 2)): coef[j] = v[t] * np.sqrt((2 * j + 1) / (2 * Lh))
M = 2 ** 16; x = np.linspace(-Lh, Lh, M + 1); h = x[1] - x[0]; g = leg.legval(x / Lh, coef)
F2 = np.fft.rfft(g, 4 * M); c = np.fft.irfft(np.abs(F2) ** 2, 4 * M)[:M + 1] * h; u = np.arange(M + 1) * h
ci = lambda s: np.interp(s, u, c)
for name, comb in (('-Q_{g*}[b] (orden 2)', L2), ('defecto exacto', Lc)):
    terms = {n: -2 * a / np.sqrt(n) * ci(np.log(n)) for n, a in comb.items() if np.log(n) < 2 * Lh}
    print('Mori mu=15:', name, '= %.4e' % sum(terms.values()), {n: '%.3e' % t for n, t in terms.items()}, ' c(0)=%.4f' % c[0])
