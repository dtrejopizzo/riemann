"""Prolate data for the rung tail Gram (ROUND_018_B).  NUMERICAL tool.
Even prolates psi_0..psi_{2(nP-1)} at c = 2 pi e^{2T}: Legendre coefficients, ODE eigenvalues, Frobenius edge series at t = 1,
Fourier scale (checked against the Bessel series), the four exact constraint rows f(0), Ff(0), A(Ef), B(Ef) (as in
schur_coupling_survivor.py), the survivor (null vector in psi_0..psi_8) and the null space of the constraints in all nP.
usage: python3 rung_gram_prep.py T nP [dps]  -> cache/rung_prep_T{T}_P{nP}.pkl"""
import sys, os, pickle, time, mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prolate_defect import prolate
T = float(sys.argv[1]); nP = int(sys.argv[2]); dps = int(sys.argv[3]) if len(sys.argv) > 3 else 60
mp.mp.dps = dps
Tm = mp.mpf(T); lam = mp.exp(Tm); NN = lam**2; c = 2*mp.pi*NN
ks, De = prolate(c, dps=dps, parity=0, nfun=nP)
kmax = ks[-1]; sq = {k: mp.sqrt(k+mp.mpf(1)/2) for k in ks}
def leg_all(x, km):
    v = [mp.mpf(1), x]; a, b = v
    for k in range(2, km+1): a, b = b, ((2*k-1)*x*b-(k-1)*a)/k; v.append(b)
    return v
def phi(i, t):
    v = leg_all(t, kmax); return mp.fsum(d*sq[k]*v[k] for d, k in zip(De[i], ks))
def int_phi(i, a):
    v = leg_all(a, kmax+1); s = mp.mpf(0)
    for d, k in zip(De[i], ks): s += d*sq[k]*((1 - a) if k == 0 else (v[k-1]-v[k+1])/(2*k+1))
    return s
def chi_ode(d):
    dg = [k*(k+1) + c**2*mp.mpf(2*k*(k+1)-1)/((2*k+3)*(2*k-1)) for k in ks]
    of = [c**2*mp.mpf((k+2)*(k+1))/((2*k+3)*mp.sqrt(mp.mpf((2*k+1)*(2*k+5)))) for k in ks[:-1]]
    Md = mp.fsum(d[i]*(dg[i]*d[i] + (of[i]*d[i+1] if i+1 < len(d) else 0) + (of[i-1]*d[i-1] if i else 0)) for i in range(len(d)))
    return Md/mp.fsum(x*x for x in d)
t0 = time.time()
rows = [[], [], [], []]
for i in range(nP):
    rows[0].append(phi(i, mp.mpf(0))/mp.sqrt(lam))
    rows[1].append(mp.sqrt(lam)*2*int_phi(i, mp.mpf(0)))
    A = mp.mpf(0); B = mp.mpf(0); n = 1
    while n < NN:
        a = n/NN
        A += mp.sqrt(lam)*int_phi(i, a)/n
        B += mp.quad(lambda t: phi(i, t)/t, [a, (1+a)/2, 1])/mp.sqrt(lam)
        n += 1
    rows[2].append(A); rows[3].append(B)
print(f"constraint rows {time.time()-t0:.0f}s", flush=True)
def nullvec(cols):
    M = mp.matrix([[rows[r][j] for j in cols] for r in range(4)] + [[0]*len(cols)]*(len(cols)-4))
    U, S, V = mp.svd_r(M)
    return S, [[V[q, j] for j in range(len(cols))] for q in range(4, len(cols))]
S5, nv = nullvec(list(range(5))); a = nv[0]; nr = mp.sqrt(mp.fsum(x*x for x in a)); a = [x/nr for x in a]
if a[4] < 0: a = [-x for x in a]
print("survivor sing vals", [mp.nstr(s, 3) for s in S5], "coeffs", [mp.nstr(x, 6) for x in a])
Sall, Nall = nullvec(list(range(nP)))
print("all-nP constraint sing vals", [mp.nstr(s, 3) for s in Sall])
chis = [chi_ode(De[i]) for i in range(nP)]
JF = 400
def frob(i):
    q0 = phi(i, mp.mpf(1)); chi = chis[i]; out = [q0, (chi - c**2)*q0/2]
    for j in range(1, JF):
        qm1 = out[j-1]
        out.append(((chi - c**2 - j*(j+1))*out[j] - 2*c**2*qm1 - c**2*(out[j-2] if j >= 2 else 0))/(2*(j+1)**2))
    return out
FR = [frob(i) for i in range(nP)]
def u_bessel(i, t):
    z = c*t; return mp.sqrt(lam)*mp.fsum(d*sq[k]*2*(-1)**(k//2)*mp.sqrt(mp.pi/(2*z))*mp.besselj(k+mp.mpf(1)/2, z) for d, k in zip(De[i], ks))
scale = []
for i in range(nP):
    t0_ = mp.mpf('1.3'); fr = mp.fsum(FR[i][j]*(t0_-1)**j for j in range(JF)); sc = u_bessel(i, t0_)/fr; scale.append(sc)
    t1 = mp.mpf('1.7'); fr1 = mp.fsum(FR[i][j]*(t1-1)**j for j in range(JF))
    print(f" psi_{2*i}: phi(1) {mp.nstr(FR[i][0],6)}, check at 1.7 {mp.nstr(u_bessel(i,t1)/(sc*fr1)-1,3)}", flush=True)
s = lambda x: mp.nstr(x, dps-5)
pickle.dump(dict(T=T, nP=nP, ks=ks, De=[[s(x) for x in r] for r in De], chis=[s(x) for x in chis], FR=[[s(x) for x in r] for r in FR],
                 scale=[s(x) for x in scale], rows=[[s(x) for x in r] for r in rows], surv=[s(x) for x in a],
                 null=[[s(x) for x in r] for r in Nall], lam=s(lam), c=s(c)), open(f'cache/rung_prep_T{T}_P{nP}.pkl', 'wb'))
print(f"done {time.time()-t0:.0f}s")
