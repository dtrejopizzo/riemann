"""Galerkin Schur data of the survivor Ef_* against its complement in P_T (window split Arch / Pi / Tate).
NUMERICAL tool (ROUND_017_A).  usage: python3 schur_coupling_galerkin.py T Nb dps -> cache/schur_T{T}_N{Nb}.pkl"""
import sys, os, pickle, time, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3])
D = G.build(T, Nb, dps=dps, verbose=False); mp.mp.dps = dps + 20
S = pickle.load(open(f'cache/surv_T{T}_N{Nb}.pkl', 'rb'))
F = mp.matrix([mp.mpf(x) for x in S['F']])
Q = G.sector_basis(D, 'ev'); R = G.sector_basis(D, 'odd')
Qa = mp.matrix(Nb, Q.cols + R.cols)
for i in range(Nb):
    for j in range(Q.cols): Qa[i, j] = Q[i, j]
    for j in range(R.cols): Qa[i, Q.cols + j] = R[i, j]
phi = Qa.T*F; nf = mp.norm(phi); phi = phi/nf
print("T", T, "|PF|/|F| =", mp.nstr(nf/mp.norm(F), 12), " odd-sector weight", mp.nstr(mp.fsum(phi[Q.cols+j]**2 for j in range(R.cols)), 4))
m = phi.rows
w = phi.copy(); w[0] -= 1; nw2 = mp.fsum(x*x for x in w)
H = mp.eye(m) - 2*(w*w.T)/nw2           # H e_0 = phi; columns 1.. = orthonormal complement
Hc = mp.matrix(m, m-1)
for i in range(m):
    for j in range(1, m): Hc[i, j-1] = H[i, j]
f = Qa*phi                               # unit survivor (Galerkin coordinates)
Gc = Qa*Hc                               # complement basis in sine coordinates (Nb x m-1)
Ar, Pi = D['Arch'], D['Pi']
t0 = time.time()
rhoA = (f.T*Ar*f)[0]; rhoP = (f.T*Pi*f)[0]; rho = rhoA - rhoP
bA = Gc.T*(Ar*f); bP = Gc.T*(Pi*f); b = bA - bP
CA = Gc.T*Ar*Gc; CP = Gc.T*Pi*Gc; C = CA - CP
E = mp.eigsy(C, eigvals_only=True); E = sorted(E)
Mfull = Qa.T*(Ar - Pi)*Qa; lamA = min(mp.eigsy(Mfull, eigvals_only=True))
print(f" rho = {mp.nstr(rho,8)}, Arch(f) = {mp.nstr(rhoA,10)}, Pi(f) = {mp.nstr(rhoP,10)}, lambda_A(Gal, full P_T) = {mp.nstr(lamA,8)}, rho/lambda_A = {mp.nstr(rho/lamA,6)}")
print(f" C bottom eigenvalues {[mp.nstr(x,4) for x in E[:6]]}  ({time.time()-t0:.0f}s)")
x0 = mp.lu_solve(C, b); S0 = (b.T*x0)[0]
xl = mp.lu_solve(C - lamA*mp.eye(m-1), b); Sl = (b.T*xl)[0]
print(f" Schur b^T C^-1 b = {mp.nstr(S0,8)} ({mp.nstr(S0/rho,5)} of rho); with shift lambda_A: {mp.nstr(Sl,8)}; rho - S(lambda_A) - lambda_A = {mp.nstr(rho-Sl-lamA,3)}")
print(f" |b| = {mp.nstr(mp.norm(b),5)}, |b_Arch| = {mp.nstr(mp.norm(bA),5)}, |b_Pi| = {mp.nstr(mp.norm(bP),5)}")
pickle.dump(dict(T=T, Nb=Nb, f=[mp.nstr(x, dps+15) for x in f], Gc=[[mp.nstr(Gc[i, j], dps+15) for j in range(m-1)] for i in range(Nb)],
                 bA=[mp.nstr(x, dps+15) for x in bA], bP=[mp.nstr(x, dps+15) for x in bP],
                 C=[[mp.nstr(C[i, j], dps+15) for j in range(m-1)] for i in range(m-1)], CP=[[mp.nstr(CP[i, j], dps+15) for j in range(m-1)] for i in range(m-1)],
                 rhoA=mp.nstr(rhoA, dps+15), rhoP=mp.nstr(rhoP, dps+15), lamA=mp.nstr(lamA, dps+15)), open(f'cache/schur_T{T}_N{Nb}.pkl', 'wb'))
