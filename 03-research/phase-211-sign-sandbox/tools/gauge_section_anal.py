"""Analysis of cache/gsec_*.npz (ROUND_020_A).  NUMERICAL.  usage: python3 gauge_section_anal.py npz"""
import sys, numpy as np, scipy.linalg as sl
Z = np.load(sys.argv[1]); nw, ng = int(Z['nw']), int(Z['ng']); nb = nw + ng
Ar, Cb, Ta, G0, I, Lg, Y2 = [Z[k] for k in ['Ar', 'Cb', 'Ta', 'G0', 'I', 'Lg', 'Y2']]
AP = Ar + Ta; W = AP - Cb
null = lambda M: sl.null_space(np.atleast_2d(M))
# gauge space
Gg = null(I[nw:][None, :]); G = np.zeros((nb, Gg.shape[1])); G[nw:] = Gg
# radical check: W(G, v) vs Ar(G, v) for admissible v (window bump + int fix)
p = nw  # pivot gauge bump for the int constraint
def adm_win(a):
    v = np.zeros(nb); v[:nw] = a; v[p] = -(I[:nw] @ a)/I[p]; return v
Vw = np.array([adm_win(e) for e in np.eye(nw)]).T
for name, V in [('gauge-gauge', G), ('gauge-window', Vw)]:
    r = np.abs(G.T @ W @ V).max(); s = np.abs(G.T @ Ar @ V).max(); s2 = np.abs(G.T @ Cb @ V).max()
    print(f"radical check {name}: max|W| {r:.3e}  max|Arch| {s:.3e}  max|Comb| {s2:.3e}")
# class space: window, P_T, int fixed by pivot
X = null(np.array([Z['Aw'][:nw], Z['Bw'][:nw]]))
F0 = Vw @ X                                   # nb x dX base representatives
Mw = X.T @ Z['Mw'][:nw, :nw] @ X               # window norm on classes
Ld, U = np.linalg.eigh(Mw); Sq = U @ np.diag(Ld**-0.5) @ U.T   # Mw-orthonormalise classes
F0 = F0 @ Sq
print(f"dim classes {F0.shape[1]}, gauge rank {G.shape[1]}")
wcls = np.linalg.eigvalsh(F0.T @ W @ F0); print("a_T = W-hat on classes (window-normalised): min", wcls.min(), "max", wcls.max())
# gauge-restricted comb = AP on radicals: sign
cg = np.linalg.eigvalsh(G.T @ Cb @ G / 1.0); ag = np.linalg.eigvalsh(G.T @ AP @ G)
print("Comb on gauge: min %.3e max %.3e ; AP on gauge: min %.3e max %.3e" % (cg.min(), cg.max(), ag.min(), ag.max()))
gn = np.linalg.eigvalsh(G.T @ G0 @ G); print("tail L2 on gauge: min %.3e max %.3e" % (gn.min(), gn.max()))
def section(Q, F):   # minimise F + G phi in quadratic Q
    QG = G.T @ Q @ G; phi = -np.linalg.lstsq(QG, G.T @ Q @ F, rcond=1e-13)[0]; return F + G @ phi
Y2g = np.zeros_like(Y2); Y2g[nw:, nw:] = Y2[nw:, nw:]
secs = {'none': F0, 'ell': section(Lg, F0), 'f2': section(Y2g, F0), 'tail': section(G0, F0)}
cs = np.linspace(-3, 8, 1101)
for k, S in secs.items():
    Ws, Cs, As = S.T @ W @ S, S.T @ Cb @ S, S.T @ AP @ S
    mins = np.array([np.linalg.eigvalsh(As - c*Cs).min() for c in cs])
    okc = cs[mins >= -1e-12*max(1, np.abs(Ws).max())]
    iv = (okc.min(), okc.max()) if len(okc) else (np.nan, np.nan)
    # margin delta = inf W/|C| over the section
    ev = sl.eigh(Cs, Ws + 1e-300*np.eye(len(Ws)), eigvals_only=True) if np.linalg.eigvalsh(Ws).min() > 0 else [np.nan]
    print(f"section {k:5s}: W min {np.linalg.eigvalsh(Ws).min():.4e}; |Psi|^2 max {np.linalg.eigvalsh(S.T@G0@S).max():.3e}; "
          f"ell max {np.linalg.eigvalsh(S.T@Lg@S).max():.3e}; Comb eig [{np.linalg.eigvalsh(Cs).min():.3e},{np.linalg.eigvalsh(Cs).max():.3e}]; "
          f"c-interval of AP-cC>=0: [{iv[0]:.2f},{iv[1]:.2f}]; delta=1/max|C/W| = {1/np.max(np.abs(ev)):.4f}")
# comb-balanced representative: for each unit class e_k, find phi with Comb[Psi]=0
GC = G.T @ Cb @ G; e, V = np.linalg.eigh(GC); vp, vm = G @ V[:, -1], G @ V[:, 0]
cnt = 0
for k in range(F0.shape[1]):
    F = F0[:, k]; q = lambda v: v @ Cb @ v
    for d in (vp, vm):
        a2, a1, a0 = q(d), 2*(F @ Cb @ d), q(F)
        disc = a1*a1 - 4*a2*a0
        if disc >= 0: cnt += 1; break
print(f"classes (basis) admitting a comb-null representative on one gauge line: {cnt}/{F0.shape[1]}")
