"""Experimento: reparto local dependiente de la ventana en T=0.5925, primos 2 y 3.
Arch(F) = C0||F||^2 + int_0^inf eps_F K du
        = int W(t)F^2 dt + (1/4) iint_{IxI} K(|t-s|)(F(t)-F(s))^2 dt ds,  W = C0 + V_out/2.
Clase LK   : r_2 = c2||F||^2 + int_0^{2T} th(u) K eps_F du,      0<=th<=1.
Clase DIR  : r_2 = int W2(t)F^2 + (1/4) iint th(t,s) K (F(t)-F(s))^2, 0<=th<=1, W2 libre.
Se maximiza tau con  r_2 - Pi_2 >= tau,  Arch - r_2 - Pi_3 >= tau  sobre P_T (Galerkin de senos).
"""
import numpy as np, sys, pickle
from numpy.polynomial.legendre import leggauss
from scipy.optimize import linprog
from scipy.special import digamma

T = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5925
N = int(sys.argv[2]) if len(sys.argv) > 2 else 20      # modos
NC = int(sys.argv[3]) if len(sys.argv) > 3 else 20     # celdas
MG = int(sys.argv[5]) if len(sys.argv) > 5 else 100
C0 = digamma(0.25) - np.log(np.pi)
K = lambda u: 0.5/np.sinh(u/2) + 0.5/np.cosh(u/2)
G = lambda u: np.log(np.tanh(u/4)) + 2*np.arctan(np.exp(u/2))
om = np.pi/(2*T)
def S(t):  # (N, len t)
    t = np.atleast_1d(t)
    k = np.arange(1, N+1)[:, None]
    out = np.sin(k*om*(t[None, :]+T))/np.sqrt(T)
    out[:, (t <= -T) | (t >= T)] = 0.0
    return out

xg = (2*np.arange(MG)+1)/MG - 1.0; wg = np.full(MG, 2.0/MG)   # punto medio compuesto
edges = np.linspace(-T, T, NC+1)
tn = np.concatenate([(edges[i]+edges[i+1])/2 + (edges[i+1]-edges[i])/2*xg for i in range(NC)])
tw = np.concatenate([(edges[i+1]-edges[i])/2*wg for i in range(NC)])
cell = np.repeat(np.arange(NC), MG)
St = S(tn)                       # N x n
Gram = (St*tw) @ St.T
print("ortonormalidad err", np.abs(Gram-np.eye(N)).max())

# restricciones de Tate
M = np.vstack([(St*tw) @ np.exp(tn/2), (St*tw) @ np.exp(-tn/2)])
U, sv, Vt = np.linalg.svd(M)
Z = Vt[2:].T                     # N x (N-2), base ortonormal de P_T (Galerkin)

# --- construccion doble integral ---
dt = np.abs(tn[:, None]-tn[None, :])
Kmat = np.where(dt > 0, K(np.where(dt > 0, dt, 1.0)), 0.0)
Wtot = C0 + 0.5*((np.pi-G(T-tn)) + (np.pi-G(T+tn)))
Pot = [ (St[:, cell == i]*tw[cell == i]) @ St[:, cell == i].T for i in range(NC)]
PotW = (St*(tw*Wtot)) @ St.T
pairs = [(i, j) for i in range(NC) for j in range(i, NC)]
Gij = {}
for (i, j) in pairs:
    a = np.where(cell == i)[0]; b = np.where(cell == j)[0]
    D = St[:, a][:, :, None] - St[:, b][:, None, :]          # N x ma x mb
    Wt = tw[a][:, None]*tw[b][None, :]*Kmat[np.ix_(a, b)]
    Gm = 0.25*np.einsum('kab,lab,ab->kl', D, D, Wt)
    Gij[(i, j)] = Gm if i == j else 2*Gm
Arch_D = PotW + sum(Gij.values())

# --- construccion por autocorrelacion (independiente) ---
def Cmat(u):   # sym int s_k(t)s_l(t-u) dt
    X = St; Y = S(tn-u)
    A = (X*tw) @ Y.T
    return 0.5*(A+A.T)
NB = NC
ue = np.linspace(0, 2*T, NB+1)
mu = 40; xu, wu = leggauss(mu)
Eb = []
for b in range(NB):
    un = (ue[b]+ue[b+1])/2 + (ue[b+1]-ue[b])/2*xu; uw = (ue[b+1]-ue[b])/2*wu
    Eb.append(sum(w*K(u)*(np.eye(N)-Cmat(u)) for u, w in zip(un, uw)))
tail = np.pi - G(2*T)
Arch_L = C0*np.eye(N) + sum(Eb) + tail*np.eye(N)
print("Arch: dos construcciones, dif max", np.abs(Arch_D-Arch_L).max(), " escala", np.abs(Arch_L).max())

v = lambda n, lam: 2*lam/np.sqrt(n)
Pi2 = v(2, np.log(2))*Cmat(np.log(2)); Pi3 = v(3, np.log(3))*Cmat(np.log(3))
pr = lambda A: Z.T @ A @ Z
for nm, Ar in (("L", Arch_L), ("D", Arch_D)):
    print(nm, "lam_min Arch|P", np.linalg.eigvalsh(pr(Ar))[0],
          " lam_min a|P", np.linalg.eigvalsh(pr(Ar-Pi2-Pi3))[0],
          " lam_min (Arch-Pi2)|P", np.linalg.eigvalsh(pr(Ar-Pi2))[0])

def kelley(Bs, lo, hi, Arch, label, cscale=1.0, maxit=int(sys.argv[4]) if len(sys.argv) > 4 else 600):
    """max tau: sum x_j Bs_j - Pi2 >= tau, Arch - sum x_j Bs_j - Pi3 >= tau  on P."""
    PB = np.array([pr(B) for B in Bs]); P2 = pr(Pi2); P3 = pr(Pi3); PA = pr(Arch)
    n = len(Bs); d = PA.shape[0]
    Aub = []; bub = []
    def add(u, which):
        co = np.einsum('i,jik,k->j', u, PB, u)
        if which == 2:   # u'(sum xB - P2)u >= tau  ->  -co.x + tau <= -u'P2u
            Aub.append(np.append(-co, 1.0)); bub.append(-u @ P2 @ u)
        else:            # u'(PA - sum xB - P3)u >= tau -> co.x + tau <= u'(PA-P3)u
            Aub.append(np.append(co, 1.0)); bub.append(u @ (PA-P3) @ u)
    for k in range(d):
        e = np.zeros(d); e[k] = 1; add(e, 2); add(e, 3)
    x = None; best = -1e9; xbest = None; it = -1; tau = np.nan
    for it in range(maxit):
        c = np.zeros(n+1); c[-1] = -1
        res = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub),
                      bounds=[(l, h) for l, h in zip(lo, hi)]+[(-50, 50)], method='highs')
        x = res.x[:n]; tau = res.x[-1]
        Q2 = np.tensordot(x, PB, 1) - P2; Q3 = PA - np.tensordot(x, PB, 1) - P3
        w2, V2 = np.linalg.eigh(Q2); w3, V3 = np.linalg.eigh(Q3)
        val = min(w2[0], w3[0])
        if val > best: best = val; xbest = x.copy()
        if it % 25 == 0: print(label, it, tau, best, len(bub), flush=True)
        if tau - best < 2e-6: break
        for k in range(4):
            if w2[k] < tau - 1e-9: add(V2[:, k], 2)
            if w3[k] < tau - 1e-9: add(V3[:, k], 3)
    print(f"[{label}] iters {it+1}  cota superior tau={tau:.3e}  mejor factible={best:.3e}")
    return xbest, best, tau


from scipy.optimize import minimize
from scipy.linalg import eigh
def softmin(Bs, lo, hi, Arch, label, x0):
    PB = np.array([pr(B) for B in Bs]); P2 = pr(Pi2); P3 = pr(Pi3); PA = pr(Arch)
    def parts(x):
        R = np.tensordot(x, PB, 1); return R - P2, PA - R - P3
    def val(x):
        Q2, Q3 = parts(x); return min(np.linalg.eigvalsh(Q2)[0], np.linalg.eigvalsh(Q3)[0])
    x = np.array(x0, float)
    for beta in (3e2, 3e3, 3e4, 3e5, 3e6, 3e7):
        def f(x):
            Q2, Q3 = parts(x)
            w2, V2 = eigh(Q2); w3, V3 = eigh(Q3)
            m = min(w2[0], w3[0])
            e2 = np.exp(-beta*(w2-m)); e3 = np.exp(-beta*(w3-m)); Zs = e2.sum()+e3.sum()
            r2 = (V2*e2) @ V2.T/Zs; r3 = (V3*e3) @ V3.T/Zs
            g = -np.einsum('ab,jab->j', r2, PB) + np.einsum('ab,jab->j', r3, PB)
            return -m + np.log(Zs)/beta, g
        res = minimize(f, x, jac=True, method='L-BFGS-B', bounds=list(zip(lo, hi)),
                       options=dict(maxiter=4000, maxfun=6000, ftol=1e-15, gtol=1e-12))
        x = res.x
        print(label, "beta", beta, "tau factible", val(x), "nit", res.nit, flush=True)
    Q2, Q3 = parts(x)
    print(f"[{label}] tau={val(x):.4e}  techo lam_min(a)/2={np.linalg.eigvalsh(PA-P2-P3)[0]/2:.4e}", flush=True)
    return x, val(x), Q2, Q3

Bs = Eb + [np.eye(N)]
xL, bestL, tauL = kelley(Bs, [0]*NB+[-60], [1]*NB+[60], Arch_L, "LK")
Wc = np.array([Wtot[cell == i].mean() for i in range(NC)])
Bs = [Gij[p] for p in pairs] + Pot
xD, bestD, Q2D, Q3D = softmin(Bs, [0]*len(pairs)+[-300]*NC, [1]*len(pairs)+[300]*NC, Arch_D, "DIR",
                              [0.5]*len(pairs)+list(Wc/2))
Bs = [sum(Gij[(i, j)] for (i, j) in pairs if j-i == dd) for dd in range(NC)] + Pot
xM, bestM, Q2M, Q3M = softmin(Bs, [0]*NC+[-300]*NC, [1]*NC+[300]*NC, Arch_D, "TH(dist)+W2(t)", [0.5]*NC+list(Wc/2))
# clase sin reparto del nucleo dependiente de posicion: th constante, W2(t) libre
Bs = [sum(Gij.values())] + Pot
xP, bestP, _, _ = softmin(Bs, [0]+[-300]*NC, [1]+[300]*NC, Arch_D, "TH const+W2(t)", [0.5]+list(Wc/2))
pickle.dump(dict(T=T, N=N, NC=NC, edges=edges, pairs=pairs, xL=xL, xD=xD, xM=xM, xP=xP, bestL=bestL, bestD=bestD,
                 bestM=bestM, bestP=bestP, Wc=Wc, Q2D=Q2D, Q3D=Q3D, Z=Z, PA=pr(Arch_D), P2=pr(Pi2), P3=pr(Pi3)),
            open(f"window_split_{T}_{N}_{NC}.pkl", "wb"))
