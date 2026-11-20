"""ROUND_031_B: (1) Arch on L^2(-T,T) vs on P_T (interlacing); (2) span of the compressed
translations C_n on the negative block of Arch|P_T; minimal-norm weight cancelling the block."""
import sys, numpy as np
from math import log
from numpy.polynomial.legendre import leggauss
import forms as F

def full_arch(T, N, nu=240):
    I = np.eye(N); x, wq = leggauss(nu); u = T*(x+1); wu = wq*T
    K = lambda s: 2*np.exp(-s/2)/(1-np.exp(-2*s))
    M = F.C0*I
    for uk, wk in zip(u, wu): M += wk*K(uk)*(I-F.corr(T, N, uk))
    M += (np.log(1/np.tanh(T/2))+np.pi-2*np.arctan(np.exp(T)))*I
    return (M+M.T)/2

def svec(X):
    i, j = np.triu_indices(X.shape[0]); s = np.where(i == j, 1.0, np.sqrt(2)); return X[i, j]*s

def study(T, N, eta=0.0, alpha=0.05, odd=False):
    M0, Cn, ns, v = F.build(T, N)
    Mf = full_arch(T, N)
    ef = np.linalg.eigvalsh(Mf); e, U = np.linalg.eigh(M0)
    print(f"T={T} N={N}  full: neg={np.sum(ef<0)} low={ef[:4].round(4)} | P_T: neg={np.sum(e<0)} low={e[:4].round(4)}")
    sel = [k for k, n in enumerate(ns) if (not odd or n % 2)]
    B = U[:, e < eta]; Cc = U[:, e >= eta]; d = B.shape[1]
    A = np.array([svec(B.T@Cn[k]@B) for k in sel]).T   # (d(d+1)/2) x #n
    s = np.linalg.svd(A, compute_uv=False)
    print(f"  odd={odd} d={d} symdim={d*(d+1)//2} #n={len(sel)} rank={np.sum(s>1e-10*s[0])} smax={s[0]:.3g} smin={s[-1] if len(s)>=d*(d+1)//2 else 0:.3g}")
    if d == 0: return
    target = svec(B.T@M0@B - alpha*np.eye(d))
    w, *_ = np.linalg.lstsq(A, target, rcond=None)
    res = np.linalg.norm(A@w-target)
    W = np.zeros(len(ns)); W[sel] = w
    Mw = M0 - sum(wi*c for wi, c in zip(W, Cn))
    lb = np.linalg.eigvalsh(B.T@Mw@B)[0]; lc = np.linalg.eigvalsh(Cc.T@Mw@Cc)[0]
    print(f"  min-norm w: |w|_1={np.abs(w).sum():.3g} res={res:.2e} BB_min={lb:.3f} CC_min={lc:.3f} full_min={np.linalg.eigvalsh(Mw)[0]:.3f} (CC_min before={e[e>=eta][0]:.3f})")

if __name__ == "__main__":
    for T, N in [(0.6, 24), (0.9, 28), (1.2, 32), (1.6, 40)]:
        for odd in (False, True): study(T, N, odd=odd)

def parity_report(T, N):
    """parity of the negative eigenvectors and nonzero singular values of the compressed family."""
    M0, Cn, ns, v = F.build(T, N)
    e, U = np.linalg.eigh(M0); B = U[:, e < 0]
    # parity via Legendre coefficients: reflection acts as diag((-1)^k) in the full basis; P_T basis Z
    from numpy.polynomial.legendre import leggauss as lg
    xg, wg = lg(N+40); t = T*xg; P = F.basis(T, N, t)
    A_ = P.T@(wg*T*np.exp(t/2)); B_ = P.T@(wg*T*np.exp(-t/2))
    Z = np.linalg.svd(np.vstack([A_, B_]))[2][2:].T
    R = Z.T@np.diag((-1.0)**np.arange(N))@Z
    par = np.round(np.diag(B.T@R@B), 3)
    for odd in (False, True):
        sel = [k for k, n in enumerate(ns) if (not odd or n % 2)]
        A = np.array([svec(B.T@Cn[k]@B) for k in sel]).T
        s = np.linalg.svd(A, compute_uv=False); s = s[s > 1e-10*s[0]]
        print(f"T={T} parity={par} odd_only={odd} nonzero sv: max={s[0]:.3g} min={s[-1]:.3g} count={len(s)}")

if __name__ == "__main__" and len(sys.argv) > 1:
    for T, N in [(1.2, 32), (1.6, 40)]: parity_report(T, N)
