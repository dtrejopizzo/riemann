"""Exact Schur balance of the survivor against the rungs in the complete tail form, and the collapsed-weight test
log N -> c log N in the tail form only (ROUND_018_B).  NUMERICAL tool; reads cache/rung_tail_*.npz.
usage: python3 rung_gram_schur.py npzfile lamA_Galerkin"""
import sys, numpy as np, mpmath as mp
mp.mp.dps = 60
Z = np.load(sys.argv[1]); lamG = mp.mpf(sys.argv[2])
nP = Z['Ar'].shape[0]
M = lambda X: mp.matrix([[mp.mpf(float(x)) for x in r] for r in X])
Ar, Cb, Mw = M(Z['Ar']), M(Z['Cb']), M(Z['Mw']); A = [mp.mpf(float(x)) for x in Z['A']]; B = [mp.mpf(float(x)) for x in Z['B']]
Ta = mp.matrix(nP, nP)
for i in range(nP):
    for j in range(nP): Ta[i, j] = A[i]*B[j] + B[i]*A[j]
s = mp.matrix([mp.mpf(float(x)) for x in Z['surv']])
Vn = mp.matrix([[mp.mpf(float(x)) for x in r] for r in Z['null']]).T            # nP x 7 admissible basis
s = Vn*mp.lu_solve(Vn.T*Vn, Vn.T*s)                                          # put the survivor exactly in the admissible span
def W(cw): return Ar - cw*Cb + Ta
q = lambda X, u, v: (u.T*X*v)[0]
ns = mp.sqrt(q(Mw, s, s)); F = s/ns
def parts(u, v): return [q(Ar, u, v), q(Cb, u, v), q(Ta, u, v)]
pa = parts(F, F)
print(f"|Ef*|^2 = {mp.nstr(ns**2, 8)}; unit survivor: Arch {mp.nstr(pa[0],6)}, Comb {mp.nstr(pa[1],6)}, Tate {mp.nstr(pa[2],6)}, "
      f"|Psi*|^2 {mp.nstr(q(M(Z['G0']),F,F),6)}")
rho = q(W(1), F, F); print(f"exact ledger rho = W[Psi*] + 2A B = {mp.nstr(rho, 8)};  rho/lamA(Gal) = {mp.nstr(rho/lamG, 6)}")
# complement of F inside the admissible space, M-orthonormal
Y = Vn - F*(F.T*Mw*Vn)
G = Y.T*Mw*Y; E, Q = mp.eigsy(G)
keep = [k for k in range(len(E)) if E[k] > mp.mpf(10)**-12]
Bm = mp.matrix(nP, len(keep))
for jj, k in enumerate(keep):
    col = Y*Q[:, k]/mp.sqrt(E[k])
    for i in range(nP): Bm[i, jj] = col[i]
def analyse(cw, verbose=True):
    Wc = W(cw); rc = q(Wc, F, F); C = Bm.T*Wc*Bm; b = Bm.T*Wc*F
    mu, V = mp.eigsy(C); order = sorted(range(len(mu)), key=lambda k: mu[k])
    out = []
    for k in order:
        v = V[:, k]; g = Bm*v; bv = (v.T*b)[0]
        # parity weight: mass on k = 2 mod 4 prolates (F-odd) in the window norm
        godd = mp.matrix([g[i] if i % 2 == 1 else 0 for i in range(nP)])
        par = q(Mw, godd, godd)
        out.append((mu[k], bv, par, g))
    schur = sum(bv**2/m for m, bv, par, g in out)
    Cfull = mp.matrix(len(keep)+1, len(keep)+1); basis = [F] + [Bm[:, j] for j in range(len(keep))]
    lmin = min(mp.eigsy(mp.matrix([[q(Wc, x, y) for y in basis] for x in basis]))[0])
    return rc, out, schur, lmin
rc, out, schur, lmin = analyse(1)
print(f"Ritz min on admissible span (dim {len(keep)+1}) = {mp.nstr(lmin,8)}   [Galerkin lamA {mp.nstr(lamG,6)}]")
print(f"Schur: rho - b^T C^-1 b = {mp.nstr(rc - schur, 8)}, share b^T C^-1 b / rho = {mp.nstr(schur/rc, 6)}")
print(" rung  mu_g              b_g             share b^2/(mu rho)   det2/(rho mu)     F-odd mass of g")
for k, (m, bv, par, g) in enumerate(out):
    print(f" {k}  {mp.nstr(m,6):>14} {mp.nstr(bv,6):>14}  {mp.nstr(bv**2/(m*rc),6):>14}  {mp.nstr(1-bv**2/(m*rc),8):>14}  {mp.nstr(par,4):>10}")
# entrywise decomposition of the 2x2 on the first two rungs
for k in range(min(4, len(out))):
    g = out[k][3]
    print(f" rung {k}: <F,F>: Arch {mp.nstr(pa[0],6)} Comb {mp.nstr(pa[1],6)} Tate {mp.nstr(pa[2],6)} | <F,g>: "
          + " ".join(mp.nstr(x, 6) for x in parts(F, g)) + " | <g,g>: " + " ".join(mp.nstr(x, 6) for x in parts(g, g)))
print("collapsed-weight test log N -> c log N (tail form only; rungs and survivor fixed at c = 1):")
ev_idx = [k for k, o in enumerate(out) if o[2] < mp.mpf('0.5')][:2]
print(' even rungs used: indices', ev_idx, 'mu', [mp.nstr(out[k][0], 5) for k in ev_idx])
gs = [out[k][3] for k in ev_idx]
for cw in [mp.mpf(x) for x in ['0', '0.5', '0.9', '0.99', '0.999', '1', '1.001', '1.01', '1.1', '2']]:
    Wc = W(cw); r = q(Wc, F, F)
    dets = []
    for g in gs:
        G2 = mp.matrix([[r, q(Wc, F, g)], [q(Wc, g, F), q(Wc, g, g)]]); dets.append(mp.det(G2)/(r*q(W(1), g, g)) if r != 0 else mp.nan)
    rc_, out_, schur_, lmin_ = analyse(cw)
    print(f" c={mp.nstr(cw,4):>6}: rho^c/rho {mp.nstr(r/rho,8):>12}  det2(g1),det2(g2) normalised {mp.nstr(dets[0],8):>12} {mp.nstr(dets[1],8):>12}"
          f"  | re-optimised rungs: mu_1 {mp.nstr(out_[0][0],5)}, Schur rho-bC^-1b {mp.nstr(rc_-schur_,6)}, Ritz min {mp.nstr(lmin_,6)}")
# thresholds: roots in c of det2 for g1, g2 and of rho^c
for k, g in enumerate(gs):
    a0 = [q(Ar + Ta, x, y) for x, y in [(F, F), (F, g), (g, g)]]; a1 = [q(Cb, x, y) for x, y in [(F, F), (F, g), (g, g)]]
    # det(c) = (a0ff - c a1ff)(a0gg - c a1gg) - (a0fg - c a1fg)^2
    p2 = a1[0]*a1[2] - a1[1]**2; p1 = -(a0[0]*a1[2] + a0[2]*a1[0]) + 2*a0[1]*a1[1]; p0 = a0[0]*a0[2] - a0[1]**2
    roots = mp.polyroots([p2, p1, p0]) if p2 != 0 else [-p0/p1]
    print(f" rung {k+1}: det2(c) zeros at c = {[mp.nstr(x, 10) for x in roots]};  Comb Gram on (F,g) det {mp.nstr(p2,5)} (sign of the c^2 term)")
print(f" rho^c zero at c = {mp.nstr(q(Ar+Ta,F,F)/q(Cb,F,F), 12)}")
