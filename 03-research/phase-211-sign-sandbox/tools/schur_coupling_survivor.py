"""Survivor f_* of the five-prolate block (psi_0..psi_8, even) cut by f(0), Ff(0), A(Ef), B(Ef); edge data for its
Poisson tail; Galerkin Schur data of the survivor against its complement in P_T.  NUMERICAL tool (ROUND_017_A).
usage: python3 schur_coupling_survivor.py T Nb dps   -> cache/surv_T{T}_N{Nb}.pkl"""
import sys, os, pickle, math, time, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galerkin_mp as G
from prolate_defect import prolate
T = float(sys.argv[1]); Nb = int(sys.argv[2]); dps = int(sys.argv[3])
D = G.build(T, Nb, dps=dps, verbose=False); mp.mp.dps = dps + 20
Tm = D['T']; lam = mp.exp(Tm); NN = lam**2; c = 2*mp.pi*NN
ks, De = prolate(c, dps=dps+20, parity=0, nfun=7)          # same call as prolate_eproj.py
P = pickle.load(open(f'cache/eproj_T{T}_N{Nb}.pkl', 'rb'))
Csin = [[mp.mpf(x) for x in r] for r in P['C']]
nP = 5
# prolate operator matrix (for chi_ode)
def chi_ode(d):
    dg = [k*(k+1) + c**2*mp.mpf(2*k*(k+1)-1)/((2*k+3)*(2*k-1)) for k in ks]
    of = [c**2*mp.mpf((k+2)*(k+1))/((2*k+3)*mp.sqrt(mp.mpf((2*k+1)*(2*k+5)))) for k in ks[:-1]]
    Md = mp.fsum(d[i]*(dg[i]*d[i] + (of[i]*d[i+1] if i+1 < len(d) else 0) + (of[i-1]*d[i-1] if i else 0)) for i in range(len(d)))
    return Md/mp.fsum(x*x for x in d)
def leg_all(x, kmax):
    v = [mp.mpf(1), x]; a, b = v
    for k in range(2, kmax+1): a, b = b, ((2*k-1)*x*b-(k-1)*a)/k; v.append(b)
    return v
kmax = ks[-1]
sq = {k: mp.sqrt(k+mp.mpf(1)/2) for k in ks}
def phi(i, t):
    v = leg_all(t, kmax); return mp.fsum(d*sq[k]*v[k] for d, k in zip(De[i], ks))
def int_phi(i, a):   # int_a^1 phi_i(t) dt via (P_{k-1}-P_{k+1})/(2k+1)
    v = leg_all(a, kmax+1); s = mp.mpf(0)
    for d, k in zip(De[i], ks):
        s += d*sq[k]*((1 - a) if k == 0 else (v[k-1]-v[k+1])/(2*k+1))
    return s
# functionals on psi_i(x) = lam^{-1/2} phi_i(x/lam)
rows = [[], [], [], []]
for i in range(nP):
    rows[0].append(phi(i, mp.mpf(0))/mp.sqrt(lam))                      # f(0)
    rows[1].append(mp.sqrt(lam)*2*int_phi(i, mp.mpf(0)))                 # Ff(0) = int psi
    A = mp.mpf(0); B = mp.mpf(0); n = 1
    while n < NN:
        a = n/NN                                                          # n/lam in units of lam
        A += mp.sqrt(lam)*int_phi(i, a)/n
        B += mp.quad(lambda t: phi(i, t)/t, [a, 1])/mp.sqrt(lam)
        n += 1
    rows[2].append(A); rows[3].append(B)
M4 = mp.matrix(rows)
U, S, V = mp.svd_r(mp.matrix(rows+[[0]*nP]))
a = [V[4, j] for j in range(nP)]                                         # null vector (last right singular vector)
nr = mp.sqrt(mp.fsum(x*x for x in a)); a = [x/nr for x in a]
if a[4] < 0: a = [-x for x in a]
print("T", T, "sing vals of constraint matrix", [mp.nstr(s, 4) for s in S], " residual", mp.nstr(mp.norm(M4*mp.matrix(a)), 3))
print("survivor coefficients on psi_0,2,4,6,8:", [mp.nstr(x, 8) for x in a])
# edge data: phi_i(1), chi_ode, Frobenius coefficients at t = 1 (phi(1+s) = sum q_j s^j)
chis = [chi_ode(De[i]) for i in range(nP)]
JF = 400
def frob(i):
    q = [phi(i, mp.mpf(1)), None, None]; chi = chis[i]
    q[1] = (chi - c**2)*q[0]/2
    out = [q[0], q[1]]
    for j in range(1, JF):
        qm1 = out[j-1]; qm2 = out[j-2] if j >= 2 else mp.mpf(0)
        out.append(((chi - c**2 - j*(j+1))*out[j] - 2*c**2*qm1 - c**2*qm2)/(2*(j+1)**2))
    return out
FR = [frob(i) for i in range(nP)]
# check Frobenius against Legendre series at t = 0.9 (inside) and Bessel-series Fourier extension at t = 1.3
for i in [0, 4]:
    s = mp.mpf('-0.1'); fv = mp.fsum(FR[i][j]*s**j for j in range(JF)); print(f" psi_{2*i}: Frobenius at 0.9 {mp.nstr(fv,12)} vs Legendre {mp.nstr(phi(i, mp.mpf('0.9')),12)}")
# scale: u_i(xi) = F(psi_i 1)(xi) = lam^{1/2} int_{-1}^1 phi_i(s) e^{-i c t s} ds, t = xi/lam  = lam^{1/2} sum_k d_k sq_k 2 (-1)^{k/2} j_k(c t)
def u_bessel(i, t):
    z = c*t; return mp.sqrt(lam)*mp.fsum(d*sq[k]*2*(-1)**(k//2)*mp.sqrt(mp.pi/(2*z))*mp.besselj(k+mp.mpf(1)/2, z) for d, k in zip(De[i], ks))
scale = []
for i in range(nP):
    t0 = mp.mpf('1.3'); fr = mp.fsum(FR[i][j]*(t0-1)**j for j in range(JF))
    sc = u_bessel(i, t0)/fr; scale.append(sc)
    t1 = mp.mpf('1.7'); fr1 = mp.fsum(FR[i][j]*(t1-1)**j for j in range(JF))
    print(f" psi_{2*i}: phi(1) {mp.nstr(FR[i][0],6)}, chi_ode {mp.nstr(chis[i],12)}, scale u/phi_ext {mp.nstr(sc,12)}, check at 1.7: {mp.nstr(u_bessel(i,t1)/(sc*fr1)-1,3)}, predicted (-1)^(k/2)sqrt(2pi/c)*lam^.5 {mp.nstr((-1)**i*mp.sqrt(2*mp.pi/c)*mp.sqrt(lam),12)}")
# Galerkin vector of Ef_* and Schur data
F = mp.matrix([mp.fsum(a[i]*Csin[i][j] for i in range(nP)) for j in range(Nb)])
Aw = (D['A'].T*F)[0]; Bw = (D['B'].T*F)[0]
print(" A(trunc Ef*), B(trunc Ef*):", mp.nstr(Aw, 4), mp.nstr(Bw, 4), " |F|^2", mp.nstr((F.T*F)[0], 8), " captured", mp.nstr((F.T*F)[0]/mp.fsum(a[i]*a[j]*0 for i in range(1) for j in range(1)) if False else 0, 2))
pickle.dump(dict(T=T, Nb=Nb, a=[mp.nstr(x, dps+15) for x in a], chis=[mp.nstr(x, dps+15) for x in chis],
                 FR=[[mp.nstr(x, dps+15) for x in r] for r in FR], scale=[mp.nstr(x, dps+15) for x in scale],
                 F=[mp.nstr(F[j], dps+15) for j in range(Nb)], lam=mp.nstr(lam, dps+15), c=mp.nstr(c, dps+15)),
            open(f'cache/surv_T{T}_N{Nb}.pkl', 'wb'))
