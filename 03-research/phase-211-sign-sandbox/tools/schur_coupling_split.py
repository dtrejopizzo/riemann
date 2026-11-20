"""Split of the survivor's coupling vector b(G) = a_T(Ef_*, G), G in P_T, G ⟂ Ef_*, and of its Schur functional (ROUND_017_A).
NUMERICAL tool.  usage: python3 schur_coupling_split.py T Nb dps
  Galerkin side: b_Gal = Gc^T (Arch - Pi) f (window split Arch / Pi; Tate part is 0 on P_T).
  Tail side (exact survivor): b = arch + comb, arch = 1/2 int K(u) <Psi, G(.+u)> du, comb = sum Lambda(n) n^{-1/2} <Psi, G(.+log n)>."""
import sys, os, pickle, math, numpy as np, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3]); mp.mp.dps = dps + 20; mpf = mp.mpf
S = pickle.load(open(f'cache/schur_T{T}_N{Nb}.pkl', 'rb')); Z = np.load(f'cache/tail_T{T}_N{Nb}.npz')
Gc = mp.matrix([[mpf(x) for x in r] for r in S['Gc']]); C = mp.matrix([[mpf(x) for x in r] for r in S['C']])
CP = mp.matrix([[mpf(x) for x in r] for r in S['CP']])
bA = mp.matrix([mpf(x) for x in S['bA']]); bP = mp.matrix([mpf(x) for x in S['bP']]); b = bA - bP
lamA = mpf(S['lamA']); rhoP = mpf(S['rhoP']); rho = mpf(S['rhoA']) - rhoP
m = C.rows; Gn = np.array([[float(Gc[i, j]) for j in range(m)] for i in range(Nb)])
ev = [j for j in range(m) if np.sum(Gn[1::2, j]**2) < 0.5]; od = [j for j in range(m) if j not in ev]
def proj(vec): return mp.matrix([mpf(float(x)) for x in (Gn.T @ vec)])
def sch(x, y, Cm=C, sh=0): return (x.T*mp.lu_solve(Cm - sh*mp.eye(Cm.rows), y))[0]
def sub(v, I): return mp.matrix([v[i] for i in I])
def subM(M, I): return mp.matrix([[M[i, j] for j in I] for i in I])
Y = Z['Y']; n = Z['n']; p = Z['p']
ba = proj(Z['Ar']); bc = proj(Y.sum(0)); bt = ba + bc
print(f"T={T} Nb={Nb}: rho = {mp.nstr(rho,6)}, lambda_A = {mp.nstr(lamA,6)}, rho/lambda_A = {mp.nstr(rho/lamA,5)}; complement dim {m} (even {len(ev)}, odd {len(od)})")
print(f" |b_Gal| = {mp.nstr(mp.norm(b),5)} (even {mp.nstr(mp.norm(sub(b,ev)),4)}, odd {mp.nstr(mp.norm(sub(b,od)),4)}); window split |b_Arch| = {mp.nstr(mp.norm(bA),5)}, |b_Pi| = {mp.nstr(mp.norm(bP),5)}")
print(f" |b_tail| = {mp.nstr(mp.norm(bt),5)} (even {mp.nstr(mp.norm(sub(bt,ev)),4)}, odd {mp.nstr(mp.norm(sub(bt,od)),4)}); |arch| {mp.nstr(mp.norm(ba),4)}, |comb| {mp.nstr(mp.norm(bc),4)}; |b_tail-b_Gal|/|b_Gal| = {mp.nstr(mp.norm(bt-b)/mp.norm(b),3)}")
Sg = sch(b, b); Se = sch(sub(b, ev), sub(b, ev), subM(C, ev)); So = sch(sub(b, od), sub(b, od), subM(C, od))
print(f" Galerkin Schur b^T C^-1 b = {mp.nstr(Sg/rho,5)} rho (even sector {mp.nstr(Se/rho,5)}, odd sector {mp.nstr(So/rho,5)}); check rho - S(lambda_A) - lambda_A = {mp.nstr(rho - sch(b,b,C,lamA) - lamA,3)}")
St = sch(bt, bt); Ste = sch(sub(bt, ev), sub(bt, ev), subM(C, ev)); Sto = sch(sub(bt, od), sub(bt, od), subM(C, od))
print(f" tail Schur b^T C^-1 b = {mp.nstr(St/rho,5)} rho_Gal (even {mp.nstr(Ste/rho,5)}, odd {mp.nstr(Sto/rho,5)})")
print(f" window split shares (Galerkin): Arch-Arch {mp.nstr(sch(bA,bA)/rho,4)}, Pi-Pi {mp.nstr(sch(bP,bP)/rho,4)}, 2 cross {mp.nstr(-2*sch(bA,bP)/rho,4)}")
print(f" tail split shares: arch-arch {mp.nstr(sch(ba,ba)/rho,5)}, comb-comb {mp.nstr(sch(bc,bc)/rho,5)}, 2 arch-comb {mp.nstr(2*sch(ba,bc)/rho,5)}; Tate 0")
E, V = mp.eigsy(C); o = sorted(range(len(E)), key=lambda i: E[i])
print(" eigen-resolution: mu, sector, Galerkin share, tail share, v.arch, v.comb (cancellation ratio |v.b|/|v.comb|)")
for i in o[:10]:
    v = V[:, i]; sec = 'odd' if sum(v[j]**2 for j in od) > 0.5 else 'ev'
    pg = (v.T*b)[0]; pt = (v.T*bt)[0]; pa = (v.T*ba)[0]; pc = (v.T*bc)[0]
    print(f"   {mp.nstr(E[i],4):>10} {sec:>3}  {mp.nstr(pg**2/E[i]/rho,4):>10} {mp.nstr(pt**2/E[i]/rho,4):>10}  {mp.nstr(pa,4):>11} {mp.nstr(pc,4):>11}  {mp.nstr(abs(pt)/abs(pc),3)}")
# 15B two-threshold model on the recorded five-prolate block: X = sum_g Pi(F_b,g)^2/(mu_g - lambda)
Pq = pickle.load(open(f'cache/eproj_T{T}_N{Nb}.pkl', 'rb')); Vv = [[mpf(x) for x in r] for r in Pq['C']]
D = G.build(T, Nb, dps=dps, verbose=False); Pr = G.projector(D)
Sm = mp.matrix(Nb, 5)
for i in range(5):
    for j in range(Nb): Sm[j, i] = Vv[i][j]
U_, s_, _ = mp.svd_r(Pr*Sm); Ub = mp.matrix([[U_[aa, bb] for bb in range(len(s_))] for aa in range(Nb)])
Ab = Ub.T*D['Arch']*Ub; Pb = Ub.T*D['Pi']*Ub; Eb, Wb = mp.eigsy(Ab - Pb); ob = sorted(range(len(Eb)), key=lambda i: Eb[i])
w0 = Wb[:, ob[0]]; Xb = mp.fsum(((w0.T*Pb*Wb[:, i])[0])**2/(Eb[i] - Eb[ob[0]]) for i in ob[1:])
print(f" five-prolate block: bottom {mp.nstr(Eb[ob[0]],4)}, Pi(F_b) = {mp.nstr((w0.T*Pb*w0)[0],5)}, X = {mp.nstr(Xb,5)}; terms: " +
      ", ".join(f"mu={mp.nstr(Eb[i],3)}: {mp.nstr(((w0.T*Pb*Wb[:, i])[0])**2/(Eb[i]-Eb[ob[0]]),4)}" for i in ob[1:]))
# falsifiers on the full Galerkin P_T problem.  c Lambda: a^c = a_T + (1-c) Pi
Qa_ev = G.sector_basis(D, 'ev'); Mev = Qa_ev.T*(D['Arch'] - D['Pi'])*Qa_ev; Pev = Qa_ev.T*D['Pi']*Qa_ev
print(" c Lambda, full even Galerkin bottom / bottom of the complement block C^c / survivor diagonal rho^c:")
Ce = subM(C, ev); CPe = subM(CP, ev); be = sub(b, ev); Pe = sub(bP, ev)
for k in [4, 6, 8, 10, 12, 14, 16, 18, 20, 22]:
    for sgn in (+1, -1):
        e = sgn*mpf(10)**(-k)               # e = 1 - c
        lo = min(mp.eigsy(Mev + e*Pev, eigvals_only=True)); loC = min(mp.eigsy(Ce + e*CPe, eigvals_only=True))
        print(f"   c = 1{'-' if sgn > 0 else '+'}1e-{k}: bottom {mp.nstr(lo,4):>11}  C^c bottom {mp.nstr(loC,4):>11}  rho^c {mp.nstr(rho + e*rhoP,4):>11}")
X = Pe + sub(bc, ev)
print(f" radical-defect vector X = Pi_T(Ef,.) + comb = A_inf(Phi_f,.): |X| = {mp.nstr(mp.norm(X),6)} vs |Pi_T(Ef,.)| = {mp.nstr(mp.norm(Pe),6)}, |comb| = {mp.nstr(mp.norm(sub(bc,ev)),4)}")
# a_3 (p = 2 deleted)
comb2 = [(x, v) for x, v in G.lambda_comb(T) if int(round(float(mp.exp(x)))) in (2, 4, 8, 16, 32, 64)]
D2 = G.build(T, Nb, dps=dps, comb=comb2, verbose=False); P2 = D2['Pi']
f = mp.matrix([mpf(x) for x in S['f']]); r2 = (f.T*P2*f)[0]
lo3 = min(mp.eigsy(Mev + Qa_ev.T*P2*Qa_ev, eigvals_only=True))
b2 = Gc.T*(P2*f)
print(f" a_3: atoms {[int(round(float(mp.exp(x)))) for x, v in comb2]}; rho^(a3) = rho + Pi^(2)(f) = {mp.nstr(rho + r2,6)}; |Pi^(2)(f,.)| = {mp.nstr(mp.norm(b2),5)} vs |comb part of p=2 in b| = {mp.nstr(mp.norm(proj(Y[p==2].sum(0))),4)}; full even bottom {mp.nstr(lo3,6)}")
