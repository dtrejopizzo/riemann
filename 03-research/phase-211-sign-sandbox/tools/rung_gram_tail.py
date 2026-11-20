"""Tail Grams of the even prolates psi_0..psi_{2(nP-1)} for the rung test (ROUND_018_B).  NUMERICAL tool.
Psi_i(x) = e^{-x/2} sum_m u_i(m e^{-x}) on (-T-L, -T), u_i = F(psi_i 1) off the band (prolate ODE + edge series + Bernoulli
closed forms, as schur_coupling_tail.py), on a uniform midpoint grid of step h.  Bilinear forms (galerkin_mp conventions):
  Ar_ij = C_0<Psi_i,Psi_j> + int_0^inf (c_ij(0) - c^sym_ij(u)) K(u) du        (Levy, trapezoid in u + closed-form tail of K)
  Cb_ij = sum_{n prime power} (2 Lambda(n)/sqrt n) c^sym_ij(log n)             (comb on tails, uncollapsed = collapsed log N)
  A_i = int Psi_i e^{x/2}, B_i = int Psi_i e^{-x/2} (+ closed-form remainder of the sawtooth beyond -T-L)
  Mw_ij = <E psi_i, E psi_j> on the window (Gauss on the pieces between T - log n).
usage: python3 rung_gram_tail.py T nP h L -> cache/rung_tail_T{T}_P{nP}_h{h}_L{L}.npz"""
import sys, os, pickle, math, time, numpy as np, mpmath as mp
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from numpy.polynomial import legendre as LG
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
T = float(sys.argv[1]); nP = int(sys.argv[2]); h = float(sys.argv[3]); L = float(sys.argv[4])
S = pickle.load(open(f'cache/rung_prep_T{T}_P{nP}.pkl', 'rb'))
mp.mp.dps = 50
lam_m = mp.mpf(S['lam']); c_m = mp.mpf(S['c']); lam = float(lam_m); c = float(c_m); NN = lam*lam
FR = [[mp.mpf(x) for x in r] for r in S['FR']]; chis = [float(mp.mpf(x)) for x in S['chis']]; sc = [mp.mpf(x) for x in S['scale']]
ks = S['ks']; De = [[mp.mpf(x) for x in r] for r in S['De']]
t0c = time.time()
Xi = 8*math.pi*lam**3; tmax = Xi/lam*1.0001; s0 = 0.02
rmax = math.sqrt(tmax**2 - 1); hr = 2*math.pi/(c*48); rg = np.arange(0, rmax + hr, hr); tg = np.sqrt(1 + rg**2)
def _ode(i):
    q0 = FR[i][0]; qn = [float(x/q0) for x in FR[i]]
    def frob(s, der=0):
        if der == 0: return sum(qn[j]*s**j for j in range(len(qn)))
        return sum(j*qn[j]*s**(j-1) for j in range(1, len(qn)))
    chi = chis[i]
    def rhs(t, y): return [y[1], (2*t*y[1] - (chi - c*c*t*t)*y[0])/(1 - t*t)]
    near = tg <= 1 + s0; far = ~near
    vals = np.zeros_like(rg); vals[near] = [frob(t - 1) for t in tg[near]]
    sol = solve_ivp(rhs, (1 + s0, tg[-1]), [frob(s0), frob(s0, 1)], method='DOP853', rtol=1e-12, atol=1e-14, t_eval=tg[far])
    vals[far] = sol.y[0]; return float(sc[i]*q0)*vals
ucache = f'cache/rung_u_T{T}_P{nP}.npy'
if os.path.exists(ucache): U = np.load(ucache)
else:
    from multiprocessing import Pool
    with Pool(nP) as pool: U = np.array(pool.map(_ode, range(nP)))
    np.save(ucache, U)
print(f"  ODE done {time.time()-t0c:.0f}s", flush=True)
Usp = CubicSpline(rg, U.T)
def u_tab(xi):
    t = xi/lam; return Usp(np.sqrt(np.maximum(t*t - 1, 0))).T      # nP x len
PA = 14
fder = np.array([[float(lam_m**(-mp.mpf(1)/2 - p)*mp.factorial(p)*FR[i][p]) for p in range(2*PA + 2)] for i in range(nP)])  # nP x 2PA+2
def u_asym(xi):
    A = 2*np.pi*xi; s = np.sin(2*np.pi*lam*xi); co = np.cos(2*np.pi*lam*xi); out = 0
    for j in range(PA): out = out + 2*(-1)**j*(np.outer(fder[:, 2*j], s/A**(2*j+1)) + np.outer(fder[:, 2*j+1], co/A**(2*j+2)))
    return out
for xi in [Xi/4, Xi*0.999]:
    a1 = u_tab(np.array([xi]))[:, 0]; a2 = u_asym(np.array([xi]))[:, 0]
    print(f"  u check at xi={xi:.1f}: max rel diff table/asym {np.max(np.abs(a1-a2)/np.maximum(np.abs(a2),1e-300)):.2e}")
def bern(n, x):
    co = [float(mp.binomial(n, k)*mp.bernoulli(k)) for k in range(n+1)]
    return sum(co[k]*x**(n-k) for k in range(n+1))
def Ssin(p, x): return (-1)**(p+1)*(2*np.pi)**(2*p+1)*bern(2*p+1, x)/(2*float(math.factorial(2*p+1)))
def Scos(p, x): return (-1)**(p+1)*(2*np.pi)**(2*p)*bern(2*p, x)/(2*float(math.factorial(2*p)))
def rho(w):
    w = np.asarray(w, float); x0 = np.mod(lam*w, 1.0); M = np.floor(Xi/w).astype(int); Mmax = int(M.max()) if M.size else 0
    out = np.zeros((nP, len(w))); ps = [np.zeros_like(w) for _ in range(PA)]; pc = [np.zeros_like(w) for _ in range(PA)]
    for m in range(1, Mmax + 1):
        msk = M >= m
        if not msk.any(): break
        out[:, msk] += u_tab(w[msk]*m)
        mf = float(m); th = 2*np.pi*mf*x0[msk]; sn = np.sin(th); cs = np.cos(th)
        for j in range(PA): ps[j][msk] += sn/mf**(2*j+1); pc[j][msk] += cs/mf**(2*j+2)
    A = 2*np.pi*w
    for j in range(PA):
        out += 2*(-1)**j*(np.outer(fder[:, 2*j], (Ssin(j, x0) - ps[j])/A**(2*j+1)) + np.outer(fder[:, 2*j+1], (Scos(j+1, x0) - pc[j])/A**(2*j+2)))
    return out
def Psi(x): return np.exp(-x/2)[None, :]*rho(np.exp(-x))
# validation on the survivor (admissible) against the finite Poisson sum
a5 = [mp.mpf(x) for x in S['surv']] + [mp.mpf(0)]*(nP - 5)
kmaxd = ks[-1]
def fval(xx):
    t = xx/lam_m
    if abs(t) >= 1: return mp.mpf(0)
    v = [mp.mpf(1), t]; A0, B0 = v
    for k in range(2, kmaxd+1): A0, B0 = B0, ((2*k-1)*t*B0-(k-1)*A0)/k; v.append(B0)
    return mp.fsum(a5[i]*mp.fsum(d*mp.sqrt(k+mp.mpf(1)/2)*v[k] for d, k in zip(De[i], ks)) for i in range(5))/mp.sqrt(lam_m)
with mp.workdps(70):
    for xv in [-T-0.05, -T-0.7, -T-2.1]:
        X = mp.mpf(xv); e = mp.exp(X); s_ = mp.fsum(fval(n*e) for n in range(1, int(lam_m/e)+2))
        tf = np.array(a5[:nP], float) @ Psi(np.array([xv]))[:, 0]
        print(f"  Psi_surv({xv:.3f}): Poisson sum {mp.nstr(mp.exp(X/2)*s_,9)}  tail formula {tf:.9e}", flush=True)
n = int(round(L/h)); xs = -T - L + (np.arange(n) + 0.5)*h
P = np.zeros((nP, n)); B = 50000
for s in range(0, n, B): P[:, s:s+B] = Psi(xs[s:s+B])
print(f"  Psi on {n} points {time.time()-t0c:.0f}s", flush=True)
Aint = h*(P @ np.exp(xs/2)); Bint = h*(P @ np.exp(-xs/2))
y0 = lam*math.exp(T + L); Pf = lambda y: ((y % 1) - (y % 1)**2)/2 - 1/12
fl = fder[:, 0]; Bint = Bint - fl*Pf(y0)/y0
C0 = float(mp.digamma(mp.mpf(1)/4) - mp.log(mp.pi))
Kf = lambda u: 1/(2*np.sinh(u/2)) + 1/(2*np.cosh(u/2)); Ktail = lambda q: -math.log(math.tanh(q/4)) + math.pi - 2*math.atan(math.exp(q/2))
def Lam(m):
    for p in range(2, int(math.isqrt(m)) + 1):
        if m % p == 0:
            r = m
            while r % p == 0: r //= p
            return p if r == 1 else 0
    return m
pps = [(m, Lam(m)) for m in range(2, int(math.exp(L)) + 1) if Lam(m)]
NF = 1 << int(math.ceil(math.log2(2*n)))
FT = np.fft.rfft(P, NF, axis=1)
uu = np.arange(1, n)*h; Ku = Kf(uu)
Ar = np.zeros((nP, nP)); Cb = np.zeros((nP, nP)); G0 = np.zeros((nP, nP))
for i in range(nP):
    for j in range(i, nP):
        cr = np.fft.irfft(np.conj(FT[i])*FT[j], NF)*h      # cr[k] = sum_x P_i(x) P_j(x + k h) h ; cr[-k] = c_ij(-kh)
        cp = cr[:n]; cm = np.r_[cr[0], cr[NF-1:NF-n:-1]]
        csym = 0.5*(cp + cm); c0 = cp[0]
        g = (c0 - csym[1:])*Ku
        g0 = 2*g[0] - g[1]
        lev = h*(0.5*g0 + g[:-1].sum() + 0.5*g[-1]) + c0*Ktail(n*h)
        Ar[i, j] = Ar[j, i] = C0*c0 + lev
        cb = 0.0
        for m, p in pps:
            ell = math.log(m)/h; k = int(ell); fr = ell - k
            if k + 1 < n: cb += 2*math.log(p)/math.sqrt(m)*((1-fr)*csym[k] + fr*csym[k+1])
        Cb[i, j] = Cb[j, i] = cb; G0[i, j] = G0[j, i] = c0
print(f"  Grams {time.time()-t0c:.0f}s; {len(pps)} prime powers", flush=True)
# window Gram <E psi_i, E psi_j>
Dfl = [np.zeros(ks[-1]+1) for _ in range(nP)]
for i in range(nP):
    for d, k in zip(De[i], ks): Dfl[i][k] = float(d)*math.sqrt(k+0.5)
bps = sorted(set([-T, T] + [T - math.log(m) for m in range(2, int(NN) + 1) if T - math.log(m) > -T]))
gx, gw = LG.leggauss(40); Mw = np.zeros((nP, nP))
for a_, b_ in zip(bps[:-1], bps[1:]):
    npan = int((b_ - a_)/0.05) + 1; hh = (b_ - a_)/npan
    for p_ in range(npan):
        x = a_ + p_*hh + hh*(gx + 1)/2; w = gw*hh/2; ex = np.exp(x); Ef = np.zeros((nP, len(x))); m = 1
        while m*ex[0] < lam:
            t = m*ex/lam; ok = t < 1
            for i in range(nP): Ef[i, ok] += LG.legval(t[ok], Dfl[i])
            m += 1
        Ef *= np.exp(x/2)/math.sqrt(lam)
        Mw += (Ef*w) @ Ef.T
np.savez(f'cache/rung_tail_T{T}_P{nP}_h{h}_L{L}.npz', Ar=Ar, Cb=Cb, G0=G0, A=Aint, B=Bint, Mw=Mw, fl=fl, surv=np.array(a5[:nP], float),
         null=np.array([[float(mp.mpf(x)) for x in r] for r in S['null']]), rows=np.array([[float(mp.mpf(x)) for x in r] for r in S['rows']]))
print(f"  saved {time.time()-t0c:.0f}s")
