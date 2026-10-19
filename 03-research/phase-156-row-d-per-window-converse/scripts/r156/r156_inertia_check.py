"""R156_001 DIAGNOSTIC: check n_-(W) = n_-(a|P_T) + n_-(G_T) on Galerkin matrices, G_T = diag(kappa_+ + 2, kappa_- - 2),
and cross-check the odd witness F(t)=t (= T*sqrt(2T/3) e_1) against r156_odd_witness.py."""
import numpy as np, math
from r156_green_matrix import build, bordered_kappa
def nneg(M): return int(np.sum(np.linalg.eigvalsh(M) < 0))
def restr(a, C):
    Q, _ = np.linalg.qr(C.T, mode='complete'); Z = Q[:, C.shape[0]:]; return Z.T @ a @ Z
N = 16
for T, pr in [(0.40, False), (0.45, False), (0.5493061443, False), (0.5493061443, True), (0.70, False), (0.9, False)]:
    a, Wm, A, B = build(T, N, pr)
    C = np.vstack([A, B])
    c = 0.5*(A+B); s = 0.5*(A-B); ev = np.arange(0, N, 2); od = np.arange(1, N, 2)
    gp = bordered_kappa(a[np.ix_(ev, ev)], c[ev]) + 2; gm = bordered_kappa(a[np.ix_(od, od)], s[od]) - 2
    print(f"T={T} primes={pr}: n-(W)={nneg(Wm)}  n-(a|P)={nneg(restr(a, C))}  n-(G)={int(gp<0)+int(gm<0)}  (g+={gp:+.3e}, g-={gm:+.3e})")
T = math.log(3)/2; a, Wm, A, B = build(T, N, False)
print("W_inf(t) via Galerkin =", Wm[1, 1] * (T * math.sqrt(2*T/3))**2)
