"""Analysis for the parity/Fourier selection rule and the sector leakage test (NUMERICAL tool).
Usage: python3 prolate_sector_anal.py T Nb dps KMAX"""
import sys, os, pickle, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); KMAX = int(sys.argv[4])
D = G.build(T, Nb, dps=dps, verbose=False); mp.mp.dps = dps + 20
P = pickle.load(open(os.path.join(G.CACHE, f'sector_T{T}_N{Nb}_K{KMAX}.pkl'), 'rb'))
ks = P['ks']; d = [mp.mpf(x) for x in P['d']]; nP = len(ks)
V = [mp.matrix([mp.mpf(x) for x in r]) for r in P['C']]; nrm = [mp.mpf(x) for x in P['nrm']]
Pr = G.projector(D); M = D['Arch'] - D['Pi']; N = mp.e**(2*mp.mpf(T))
def dot(a, b): return mp.fsum(a[i]*b[i] for i in range(Nb))
def par(v, s):  # s=+1 even part (sine index odd), s=-1 odd part
    w = mp.matrix(v)
    for j in range(Nb):
        if (j % 2 == 0) != (s == 1): w[j] = 0
    return w
lamA, _, res = G.lambda_A(D); lev = res['ev'][0]; lod = res['odd'][0]
uev = res['ev'][1]; uev = uev/mp.sqrt(dot(uev, uev)); uod = res['odd'][1]; uod = uod/mp.sqrt(dot(uod, uod))
print(f"# T={T} N={mp.nstr(N,5)} 4N={mp.nstr(4*N,4)} Nb={Nb} lambda_A^ev={mp.nstr(lev,4)} lambda_A^odd={mp.nstr(lod,4)}")
g = [Pr*v for v in V]
print("## (1) selection rule: wrong-sector part of Pi_T E psi_k")
print(" k  eps  capt  |g_k|  |P_wrong g_k|  sqrt(d_k)  ratio  a_T(P_wrong g)/|P_wrong g|^2")
for i, k in enumerate(ks):
    eps = 1 if k % 4 == 0 else -1
    wr = par(g[i], -eps); nw = mp.sqrt(dot(wr, wr)); ng = mp.sqrt(dot(g[i], g[i]))
    q = dot(wr, M*wr)/nw**2 if nw > 0 else 0
    print(f" {k:2d} {eps:+d} {mp.nstr(dot(V[i],V[i])/nrm[i],5)} {mp.nstr(ng,4)} {mp.nstr(nw,4)} {mp.nstr(mp.sqrt(d[i]),4)} {mp.nstr(nw/mp.sqrt(d[i]),4)} {mp.nstr(q,4)}")
def gen_min(Mm, Dd):
    n = Mm.rows; S = mp.matrix(n, n)
    for a in range(n):
        for b in range(n): S[a, b] = Mm[a, b]/mp.sqrt(Dd[a]*Dd[b])
    E, W = mp.eigsy(S); i0 = min(range(n), key=lambda i: E[i]); return E[i0], W[:, i0]
def sector(s, cls):
    idx = [i for i, k in enumerate(ks) if (k % 4 == 0) == (cls == 1)]
    U = [par(g[i], s) for i in idx]; MU = [M*u for u in U]
    n = len(idx); Mm = mp.matrix(n, n); Gm = mp.matrix(n, n)
    for a in range(n):
        for b in range(n): Mm[a, b] = dot(U[a], MU[b]); Gm[a, b] = dot(U[a], U[b])
    return idx, U, Mm, Gm
def ritz(Mm, Gm, n):
    Ms = Mm[:n, :n]; Gs = Gm[:n, :n]
    E, W = mp.eigsy(Gs); keep = [i for i in range(n) if E[i] > max(E)*mp.mpf(10)**(-(dps-8))]
    B = mp.matrix(n, len(keep))
    for c_, i in enumerate(keep):
        for a in range(n): B[a, c_] = W[a, i]/mp.sqrt(E[i])
    H = B.T*Ms*B; E2, W2 = mp.eigsy(H); j = min(range(len(E2)), key=lambda i: E2[i]); return E2[j], B*W2[:, j]
for s, cls, lab, lref, uref in ((1, 1, "EVEN sector, class +1 (k=0 mod 4)", lev, uev), (-1, -1, "ODD sector, class -1 (k=2 mod 4)", lod, uod)):
    idx, U, Mm, Gm = sector(s, cls); dd = [d[i] for i in idx]; kk = [ks[i] for i in idx]; n = len(idx)
    print(f"## (2) {lab}: k = {kk}")
    print("  top k | dim | Ritz bottom/lambda | gen. min of (M, D) | angle(u, span)")
    for t in range(2, n+1):
        e, a = ritz(Mm, Gm, t)
        gm, _ = gen_min(Mm[:t, :t], dd[:t])
        Ub = mp.matrix(Nb, t)
        for c_ in range(t):
            for j in range(Nb): Ub[j, c_] = U[c_][j]
        # angle of u to span: least squares
        Gs = Gm[:t, :t]; rhs = mp.matrix([dot(U[c_], uref) for c_ in range(t)])
        try:
            co = mp.lu_solve(Gs, rhs); pu = Ub*co; ang = mp.acos(min(1, mp.sqrt(max(0, dot(pu, uref)))))
        except ZeroDivisionError: ang = mp.nan
        print(f"   {kk[t-1]:2d} | {t} | {mp.nstr(e/lref,4)} | {mp.nstr(gm,4)} | {mp.nstr(ang,3)}")
    # low block = first three; coupling of its bottom to the rest
    L = 3; e, a = ritz(Mm, Gm, L)
    a = a/mp.sqrt(mp.fsum(x*x for x in a)); leak = mp.fsum(a[i]**2*dd[i] for i in range(L))
    val = mp.fsum(a[i]*a[j]*Mm[i, j] for i in range(L) for j in range(L))
    print(f"  low block {kk[:L]}: bottom value {mp.nstr(val,4)} (= {mp.nstr(val/lref,4)} lambda), coeffs {[mp.nstr(x,3) for x in a]}, value/leak = {mp.nstr(val/leak,4)}, leak/d_{kk[L-1]} = {mp.nstr(leak/dd[L-1],4)}")
    print("   k | M_kk/d_k | coupling c_k=|M(b,u_k)|/sqrt(val*M_kk) | gamma_k=|M(b,u_k)|/sqrt(leak(b) d_k) | M_kk")
    for t in range(L, n):
        cb = mp.fsum(a[i]*Mm[i, t] for i in range(L))
        print(f"   {kk[t]:2d} | {mp.nstr(Mm[t,t]/dd[t],4)} | {mp.nstr(abs(cb)/mp.sqrt(val*Mm[t,t]),4)} | {mp.nstr(abs(cb)/mp.sqrt(leak*dd[t]),4)} | {mp.nstr(Mm[t,t],4)}")
    # Schur data in D-normalised coordinates
    for top in range(L+1, n+1):
        Sm = mp.matrix(top, top)
        for i in range(top):
            for j in range(top): Sm[i, j] = Mm[i, j]/mp.sqrt(dd[i]*dd[j])
        aL = min(mp.eigsy(Sm[:L, :L], eigvals_only=True)); aH = min(mp.eigsy(Sm[L:top, L:top], eigvals_only=True))
        X = Sm[:L, L:top]; XL = X.T*mp.inverse(Sm[:L, :L])*X; Gam = mp.sqrt(max(mp.eigsy(XL, eigvals_only=True)))
        rH = min(mp.eigsy(Sm[L:top, L:top] - XL, eigvals_only=True))
        kf = min(mp.eigsy(Sm, eigvals_only=True))
        print(f"   Schur top k={kk[top-1]}: alpha_L={mp.nstr(aL,4)} alpha_H={mp.nstr(aH,4)} Gamma1={mp.nstr(Gam,4)} rho_H={mp.nstr(rH,4)} kappa_full={mp.nstr(kf,4)}")
pickle.dump(dict(g=[[mp.nstr(x, dps+10) for x in v] for v in g]), open(os.path.join(G.CACHE, f'sector_g_T{T}_N{Nb}_K{KMAX}.pkl'), 'wb'))
