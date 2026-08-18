"""
Fit the coefficients of the Riemann-Weil explicit formula empirically.
No sign convention is assumed anywhere; the linear solve recovers them.

F(t)=exp(-t^2/(2 s^2)),  g=F*F,  h(r)=|F^(r)|^2 = 2 pi s^2 exp(-s^2 r^2) >= 0
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 25

NZEROS = 120
print("zeta zeros ...", flush=True)
gam = [mp.im(mp.zetazero(k)) for k in range(1, NZEROS+1)]
print("  gamma_1 = %s ,  gamma_%d = %s" % (mp.nstr(gam[0],10), NZEROS, mp.nstr(gam[-1],10)), flush=True)

NMAX = 200000
is_comp = np.zeros(NMAX+1, dtype=bool)
for p in range(2, int(NMAX**0.5)+1):
    if not is_comp[p]:
        is_comp[p*p::p] = True
Lam = np.zeros(NMAX+1)
for p in range(2, NMAX+1):
    if not is_comp[p]:
        q = p
        while q <= NMAX:
            Lam[q] = np.log(p); q *= p
nn  = np.arange(2, NMAX+1)
ww  = Lam[2:NMAX+1]
sel = ww > 0
nn, ww = nn[sel], ww[sel]
logn = np.log(nn)
pref = ww/np.sqrt(nn)

def terms(s):
    s = mp.mpf(s)
    h = lambda r: 2*mp.pi*s**2 * mp.e**(-s**2 * r**2)
    sf = float(s)

    Z  = 2*mp.fsum([h(gm) for gm in gam])                       # zeros, both signs
    P0 = 2 * (2*mp.pi*s**2 * mp.e**(s**2/4))                    # h(i/2)+h(-i/2)
    gv = sf*np.sqrt(np.pi)*np.exp(-logn**2/(4*sf**2))
    PR = mp.mpf(2*float(np.sum(pref*gv)))                       # prime term
    R  = 16/s
    A  = mp.quad(lambda r: h(r)*mp.re(mp.digamma(mp.mpf('0.25')+mp.mpc(0,0.5)*r)), [-R,0,R])/(2*mp.pi)
    L  = mp.log(mp.pi)*mp.quad(h, [-R,0,R])/(2*mp.pi)
    return [P0, PR, A, L], Z

S = [mp.mpf('0.10'), mp.mpf('0.15'), mp.mpf('0.22'), mp.mpf('0.30'), mp.mpf('0.45')]
rows, zs = [], []
for s in S:
    v, Z = terms(s); rows.append(v); zs.append(Z)
    print("s=%.2f  Z=% .12e  P0=% .8e  PR=% .8e  A=% .8e  L=% .8e"
          % (float(s), float(Z), float(v[0]), float(v[1]), float(v[2]), float(v[3])), flush=True)

Mfit = mp.matrix([[rows[i][j] for j in range(4)] for i in range(4)])
zfit = mp.matrix([zs[i] for i in range(4)])
c = mp.lu_solve(Mfit, zfit)
names = ["c1 (pole h(+-i/2))", "c2 (prime sum)", "c3 (Re psi)", "c4 (log pi)"]
print("\n  Z = c1*P0 + c2*PR + c3*A + c4*L")
for nme, ci in zip(names, c):
    print("   %-22s = %s" % (nme, mp.nstr(ci, 12)))
pred = mp.fsum([rows[4][j]*c[j] for j in range(4)])
print("\nheld-out s=%.2f :  predicted Z = %s" % (float(S[4]), mp.nstr(pred,12)))
print("                   actual    Z = %s" % mp.nstr(zs[4],12))
print("                   residual    = %s" % mp.nstr(pred-zs[4],6))
