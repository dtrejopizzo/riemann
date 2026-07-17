"""
E21d: problema generalizado A v = rho G v, METRICA COMPLETADA |xi|^2.

La Gram |zeta|^2 desnuda tiene cola de fluctuacion O(1/T) -> no se puede fijar a
la profundidad del radical e^{-cL}. La metrica fiel es la COMPLETADA (el lugar
arquimediano ya esta en QW via Omega-tilde):
   xi(s) = 1/2 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s),  s=1/2+it
   chi(t) = |xi(1/2+it)|^2  ~ e^{-pi|t|/2}  (cola muerta a T~40).
   ceros de xi = gamma_rho.

G_{mn} = int chi(t) h_m(t) h_n(t) dt,  h_n(t) = 2 sin(tL/2)/(k_n - t),  k_n=2pi n/L.
Todo en mpmath (radical ~ e^{-cL}).  Control: eigsy(A) ordinario -> (k+1)^2.
"""
import mpmath as mp
mp.mp.dps = 45
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi)

def q_func(m, n, L):
    if m == n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def QW_entry(m, n, L, lam):
    q = q_func(m, n, L); q0 = q(mp.mpf(0))
    W02 = mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
    def wr(y):
        if y < mp.mpf('1e-12'):
            h = mp.mpf('1e-8'); return ((q(h)-q0)/h+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WR = (LOG4PI+GAMMA)*q0/2 + mp.quad(wr, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    arith = mp.mpf(0); mx = int(lam*lam); sv = [True]*(mx+1)
    for i in range(2, int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i, mx+1, i): sv[j] = False
    for p in range(2, mx+1):
        if sv[p]:
            lp = mp.log(p); pm = p; me = 1
            while pm <= mx:
                arith += lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp); pm *= p; me += 1
    return W02 - WR - arith

def xi(s):
    return mp.mpf(1)/2 * s*(s-1) * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)

def run(lam_str, N, Tmax):
    lam = mp.mpf(lam_str); L = 2*mp.log(lam); dim = 2*N+1
    idx = list(range(-N, N+1)); k = [2*mp.pi*n/L for n in idx]
    print(f"lam={lam_str} N={N} dim={dim} L={mp.nstr(L,6)} Tmax={Tmax} dps={mp.mp.dps}", flush=True)

    A = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, lam); A[a,b]=v; A[b,a]=v
    EA,_ = mp.eigsy(A); EA = sorted([EA[i] for i in range(dim)])
    print(" ORDINARIO eigsy(A) eig[0]=", mp.nstr(EA[0],4), flush=True)
    print("   ratios e_k/e_0:", [mp.nstr(EA[i]/EA[0],5) for i in range(8)], flush=True)

    half = mp.mpf(1)/2
    def chi(t): return abs(xi(half + 1j*t))**2
    def hfac(kk, t):
        d = kk - t
        if abs(d) < mp.mpf('1e-10'):
            return -L*mp.cos(t*L/2)       # lim_{t->k} 2sin(tL/2)/(k-t) = -L cos(kL/2)
        return 2*mp.sin(t*L/2)/d
    # nodos para quad
    nodes = sorted(set([float(x) for x in k if abs(x) < Tmax] + [-Tmax, Tmax, 0.0]))
    print(" construyendo G (metrica |xi|^2) ...", flush=True)
    G = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            f = lambda t, ka=k[a], kb=k[b]: chi(t)*hfac(ka,t)*hfac(kb,t)
            v = mp.quad(f, nodes); G[a,b]=v; G[b,a]=v
        print(f"   fila {a+1}/{dim}", flush=True)
    gev,_ = mp.eigsy(G); gev = sorted([gev[i] for i in range(dim)])
    print(" Gram |xi|^2 eig min/max:", mp.nstr(gev[0],5), mp.nstr(gev[-1],5), flush=True)

    R = mp.cholesky(G); Rinv = R**-1
    B = Rinv * A * Rinv.T; B = (B+B.T)/2
    EB,_ = mp.eigsy(B); EB = sorted([EB[i] for i in range(dim)])
    print(" GENERALIZADO eig[0]=", mp.nstr(EB[0],4), flush=True)
    print("   ratios rho_k/rho_0:", [mp.nstr(EB[i]/EB[0],5) for i in range(8)], flush=True)
    print("   objetivo (k+1)^2:", [(i+1)**2 for i in range(8)], flush=True)

if __name__ == "__main__":
    run('5.0', 14, 40.0)
