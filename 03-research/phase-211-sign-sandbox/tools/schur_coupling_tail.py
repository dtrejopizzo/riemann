"""Poisson tail Psi of the survivor and its pairings with the window sines (ROUND_017_A).  NUMERICAL tool.
  Psi(x) = e^{-x/2} rho(e^{-x}), rho(w) = sum_m u(m w), u = F(f_* 1_[-lam,lam]) off the band (x < -T).
  u from the prolate ODE (Frobenius start at t = 1, DOP853), asymptotic edge series + Bernoulli closed forms for m w > Xi.
  Outputs per sine e_k (k = 1..Nb):
    Y_k[n]  = (Lambda(n)/sqrt n) <Psi, e_k(. + log n)>       (comb part, every prime power n <= nmax)
    Ar_k    = 1/2 int_0^inf K(u) <Psi, e_k(. + u)> du          (archimedean part, = -Arch(Psi, e_k))
usage: python3 schur_coupling_tail.py T Nb [nmax] [Lx]   -> cache/tail_T{T}_N{Nb}.npz"""
import sys, os, pickle, math, time, numpy as np, mpmath as mp
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
T = float(sys.argv[1]); Nb = int(sys.argv[2]); nmax = int(sys.argv[3]) if len(sys.argv) > 3 else 3000
Lx = float(sys.argv[4]) if len(sys.argv) > 4 else 9.0
S = pickle.load(open(f'cache/surv_T{T}_N{Nb}.pkl', 'rb'))
mp.mp.dps = 50
a = [mp.mpf(x) for x in S['a']]; lam_m = mp.mpf(S['lam']); c_m = mp.mpf(S['c'])
lam = float(lam_m); c = float(c_m); NN = lam*lam
FR = [[mp.mpf(x) for x in r] for r in S['FR']]; chis = [float(mp.mpf(x)) for x in S['chis']]; sc = [mp.mpf(x) for x in S['scale']]
Fn = np.array([float(mp.mpf(x)) for x in S['F']]); Fnorm = float(np.sqrt(Fn @ Fn))
t0c = time.time()
Xi = 8*math.pi*lam**3                  # asymptotic edge series used for xi > Xi
tmax = Xi/lam*1.0001; s0 = 0.02
# r-grid: t = sqrt(1 + r^2), r in [0, rmax]
rmax = math.sqrt(tmax**2 - 1); hr = 2*math.pi/(c*48); rg = np.arange(0, rmax + hr, hr); tg = np.sqrt(1 + rg**2)
U = np.zeros_like(rg)
for i in range(5):
    if abs(a[i]*FR[i][0]) < mp.mpf(10)**-45: continue
    q0 = FR[i][0]; qn = [float(x/q0) for x in FR[i]]
    def frob(s, der=0):
        if der == 0: return sum(qn[j]*s**j for j in range(len(qn)))
        return sum(j*qn[j]*s**(j-1) for j in range(1, len(qn)))
    chi = chis[i]
    def rhs(t, y): return [y[1], (2*t*y[1] - (chi - c*c*t*t)*y[0])/(1 - t*t)]
    near = tg <= 1 + s0; far = ~near
    vals = np.zeros_like(rg)
    vals[near] = [frob(t - 1) for t in tg[near]]
    sol = solve_ivp(rhs, (1 + s0, tg[-1]), [frob(s0), frob(s0, 1)], method='DOP853', rtol=1e-12, atol=1e-14, t_eval=tg[far])
    vals[far] = sol.y[0]
    U += float(a[i]*sc[i]*q0)*vals
    print(f"  prolate {2*i}: ODE ok={sol.success}, coeff {float(a[i]*sc[i]*q0):.3e}", flush=True)
Usp = CubicSpline(rg, U)
def u_tab(xi):
    t = xi/lam; return Usp(np.sqrt(np.maximum(t*t - 1, 0)))
# edge derivatives f^(p)(lam) = sum_i a_i lam^{-1/2-p} p! q_{i,p}
PA = 14
fder = [float(mp.fsum(a[i]*lam_m**(-mp.mpf(1)/2 - p)*mp.factorial(p)*FR[i][p] for i in range(5))) for p in range(2*PA + 2)]
def u_asym(xi):
    A = 2*np.pi*xi; s = np.sin(2*np.pi*lam*xi); co = np.cos(2*np.pi*lam*xi); out = 0
    for j in range(PA):
        out = out + 2*(-1)**j*(fder[2*j]*s/A**(2*j+1) + fder[2*j+1]*co/A**(2*j+2))
    return out
for xi in [Xi/4, Xi/2, Xi*0.999]:
    print(f"  check u at xi={xi:.1f}: table {u_tab(np.array([xi]))[0]:.6e}, asym {u_asym(np.array([xi]))[0]:.6e}")
# Bernoulli closed forms: Ssin_{2p+1}(x) = sum sin(2 pi k x)/k^{2p+1}, Scos_{2p}(x) = sum cos(2 pi k x)/k^{2p}
Bp = [np.array([float(mp.bernpoly(n, 0)) for n in range(0)])]
def bern(n, x):   # Bernoulli polynomial via mpmath coefficients
    co = [float(mp.binomial(n, k)*mp.bernoulli(k)) for k in range(n+1)]
    return sum(co[k]*x**(n-k) for k in range(n+1))
def Ssin(p, x): return (-1)**(p+1)*(2*np.pi)**(2*p+1)*bern(2*p+1, x)/(2*float(math.factorial(2*p+1)))
def Scos(p, x): return (-1)**(p+1)*(2*np.pi)**(2*p)*bern(2*p, x)/(2*float(math.factorial(2*p)))
xx = 0.3; print("  Bernoulli check", Ssin(0, xx) - sum(math.sin(2*math.pi*k*xx)/k for k in range(1, 200000)), Scos(1, xx) - sum(math.cos(2*math.pi*k*xx)/k**2 for k in range(1, 200000)))
def rho(w):
    w = np.asarray(w, float); x0 = np.mod(lam*w, 1.0); M = np.floor(Xi/w).astype(int); Mmax = int(M.max()) if M.size else 0
    out = np.zeros_like(w); part_s = [np.zeros_like(w) for _ in range(PA)]; part_c = [np.zeros_like(w) for _ in range(PA)]
    for mi in range(1, Mmax + 1):
        m = mi
        msk = M >= m
        if not msk.any(): break
        wm = w[msk]*m; m = float(m)
        out[msk] += u_tab(wm)
        th = 2*np.pi*m*x0[msk]; sn = np.sin(th); cs = np.cos(th)
        for j in range(PA):
            part_s[j][msk] += sn/m**(2*j+1); part_c[j][msk] += cs/m**(2*j+2)
    A = 2*np.pi*w
    for j in range(PA):
        out += 2*(-1)**j*(fder[2*j]*(Ssin(j, x0) - part_s[j])/A**(2*j+1) + fder[2*j+1]*(Scos(j+1, x0) - part_c[j])/A**(2*j+2))
    return out
def Psi(x): return np.exp(-x/2)*rho(np.exp(-x))
# validation of Psi against the finite Poisson sum Phi(x) = e^{x/2} sum_n f(n e^x) in multiprecision
from prolate_defect import prolate
ks, De = prolate(c_m, dps=70, parity=0, nfun=5)
def fval(xx):
    t = xx/lam_m
    if abs(t) >= 1: return mp.mpf(0)
    v = [mp.mpf(1), t]; A0, B0 = v
    for k in range(2, ks[-1]+1): A0, B0 = B0, ((2*k-1)*t*B0-(k-1)*A0)/k; v.append(B0)
    return mp.fsum(a[i]*mp.fsum(d*mp.sqrt(k+mp.mpf(1)/2)*v[k] for d, k in zip(De[i], ks)) for i in range(5))/mp.sqrt(lam_m)
with mp.workdps(70):
    for xv in [-T-0.05, -T-0.4, -T-1.3]:
        X = mp.mpf(xv); e = mp.exp(X); s = mp.fsum(fval(n*e) for n in range(1, int(lam_m/e)+2))
        print(f"  Psi({xv:.3f}): Poisson-sum {mp.nstr(mp.exp(X/2)*s,8)}  tail formula {Psi(np.array([xv]))[0]:.8e}", flush=True)
print(f"  setup {time.time()-t0c:.0f}s", flush=True)
# master x-grid on (-T-Lx, -T): breakpoints at jumps x = T - log j (j > N) and cut points -T - log n
jmax = int(lam*math.exp(T + Lx)) + 1
bp = set([-T - Lx, -T])
for j in range(int(NN) + 1, jmax + 1):
    x = T - math.log(j)
    if -T - Lx < x < -T: bp.add(x)
def Lam(n):
    for p in range(2, int(math.isqrt(n)) + 1):
        if n % p == 0:
            m = n
            while m % p == 0: m //= p
            return p if m == 1 else 0
    return n
pps = [(n, Lam(n)) for n in range(2, nmax + 1) if Lam(n)]
pps = [(n, p) for n, p in pps if math.log(n) < Lx]
for n, p in pps: bp.add(-T - math.log(n))
bp = np.array(sorted(bp))
print(f"  {len(bp)} breakpoints, {len(pps)} prime powers (n <= {pps[-1][0]})", flush=True)
gx, gw = np.polynomial.legendre.leggauss(40)
xs = []; ws = []; seg = []
for lo, hi in zip(bp[:-1], bp[1:]):
    w = math.exp(-0.5*(lo + hi)); nq = int(min(40, 6 + 3*c*lam/w/max(1, lam*w*(hi-lo)*0 + 1)))
    nq = 6 if w > Xi else max(6, min(40, int(6 + 2*c*lam/w)))
    xg, wg = np.polynomial.legendre.leggauss(nq)
    xs.append(0.5*(hi - lo)*xg + 0.5*(hi + lo)); ws.append(0.5*(hi - lo)*wg); seg.append(len(xg))
segstart = np.concatenate([[0], np.cumsum(seg)]); xs = np.concatenate(xs); ws = np.concatenate(ws)
print(f"  {len(xs)} nodes; evaluating Psi ...", flush=True)
Pv = np.concatenate([Psi(xs[i:i+20000]) for i in range(0, len(xs), 20000)])/(Fnorm/math.sqrt(lam))   # unit Ef_* (eproj vectors carry a factor lam^{1/2})
print(f"  Psi done {time.time()-t0c:.0f}s; |Psi|^2 on grid = {np.sum(ws*Pv**2):.4e}", flush=True)
ak = np.arange(1, Nb + 1)*np.pi/(2*T); sT = 1/math.sqrt(T)
# cumulative integrals from the top (x = -T) downwards, at breakpoints: Sk(X) = int_X^{-T} Psi sin(a_k (x+T)) dx
segS = np.zeros((len(bp)-1, Nb)); segC = np.zeros((len(bp)-1, Nb))
for s in range(len(bp) - 1):
    sl = slice(segstart[s], segstart[s+1]); arg = np.outer(xs[sl] + T, ak); wv = ws[sl]*Pv[sl]
    segS[s] = wv @ np.sin(arg); segC[s] = wv @ np.cos(arg)
cumS = np.vstack([np.cumsum(segS[::-1], axis=0)[::-1], np.zeros(Nb)]); cumC = np.vstack([np.cumsum(segC[::-1], axis=0)[::-1], np.zeros(Nb)])
idx = {round(x, 12): i for i, x in enumerate(bp)}
def h(ell):   # <Psi, e_k(. + ell)> for all k; window x in (-T-ell, min(-T, T-ell))
    lo = -T - ell; hi = min(-T, T - ell)
    il = idx[round(lo, 12)]; ih = idx[round(hi, 12)]
    dS = cumS[il] - cumS[ih]; dC = cumC[il] - cumC[ih]
    return sT*(np.cos(ak*ell)*dS + np.sin(ak*ell)*dC)
Y = np.zeros((len(pps), Nb))
for r, (n, p) in enumerate(pps): Y[r] = math.log(p)/math.sqrt(n)*h(math.log(n))
print(f"  comb pairings done {time.time()-t0c:.0f}s", flush=True)
# archimedean: Ar_k = 1/2 int K(u) <Psi, e_k(.+u)> du = int_{x<-T} Psi(x) g_k(x) dx,
# g_k(x) = 1/2 int e_k(y) K(y - x) dy = sum_j e^{s_j (x+T)} a_k (1 - (-1)^k e^{-2 s_j T}) / ((s_j^2 + a_k^2) sqrt T), s_j = 2j + 1/2
sg = (-1.0)**np.arange(1, Nb + 1)
delta = -T - xs; Ar = np.zeros(Nb); Kerr = 0.0
for (dlo, dhi, J) in [(0.5, 1e9, 60), (0.05, 0.5, 600), (0.005, 0.05, 6000), (0.0, 0.005, 60000)]:
    msk = (delta >= dlo) & (delta < dhi)
    if not msk.any(): continue
    sj = 2*np.arange(J) + 0.5
    I = (ak[None, :]*(1 - sg[None, :]*np.exp(-2*sj[:, None]*T))/(sj[:, None]**2 + ak[None, :]**2))*sT   # J x Nb
    E = np.exp(-np.outer(delta[msk], sj))                                                            # pts x J
    Ar += (ws[msk]*Pv[msk]) @ (E @ I)
    Kerr += np.sum(np.abs(ws[msk]*Pv[msk])*np.exp(-(2*J+0.5)*delta[msk])/np.maximum(1-np.exp(-2*delta[msk]), 1e-300))
print(f"  arch pairings done {time.time()-t0c:.0f}s; crude truncation bound of K-series {Kerr*sT:.2e}", flush=True)
# Tate functionals of Psi on the grid (for reference): A(Psi) = int Psi e^{x/2}, B(Psi) = int Psi e^{-x/2}
APsi = np.sum(ws*Pv*np.exp(xs/2)); BPsi = np.sum(ws*Pv*np.exp(-xs/2))
np.savez(f'cache/tail_T{T}_N{Nb}.npz', Y=Y, n=np.array([n for n, p in pps]), p=np.array([p for n, p in pps]), Ar=Ar, APsi=APsi, BPsi=BPsi,
         Fnorm=Fnorm, fder=np.array(fder[:6]), Lx=Lx)
print(f"  saved; A(Psi) {APsi:.4e}, B(Psi) {BPsi:.4e}; f(lam) {fder[0]:.4e}")
