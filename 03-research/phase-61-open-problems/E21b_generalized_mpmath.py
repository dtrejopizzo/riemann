"""
E21b: problema generalizado  A v = rho G v  TODO EN MPMATH (el radical ~e^{-cL}
esta por debajo de float64, hay que usar precision extendida como E11).

A = QW del engine (forma de Weil).   G = Gram E*E = int |zeta|^2 h_m h_n,
   h_n(t) = -2 sin(tL/2)/(k_n - t),  k_n = 2 pi n/L.  (singularidades removibles)

Generalizado via Cholesky G = R R^T,  B = R^{-1} A R^{-T},  eigsy(B).
Control: eigsy(A) ordinario debe dar (k+1)^2.
"""
import mpmath as mp
mp.mp.dps = 30
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

def run(lam_str, N, Tmax):
    lam = mp.mpf(lam_str); L = 2*mp.log(lam); dim = 2*N+1
    idx = list(range(-N, N+1)); k = [2*mp.pi*n/L for n in idx]
    print(f"lam={lam_str} N={N} dim={dim} L={mp.nstr(L,6)} Tmax={Tmax}", flush=True)

    # ---- A (engine QW) ----
    print(" construyendo A ...", flush=True)
    A = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, lam); A[a,b]=v; A[b,a]=v

    # control ordinario
    EA,_ = mp.eigsy(A); EA = sorted([EA[i] for i in range(dim)])
    print(" ORDINARIO eigsy(A):", flush=True)
    print("   eig[:6]:", [mp.nstr(EA[i],4) for i in range(6)])
    print("   ratios e_k/e_0:", [mp.nstr(EA[i]/EA[0],5) for i in range(8)])

    # ---- G (Gram E*E) ----
    print(" construyendo G (int |zeta|^2 h_m h_n) ...", flush=True)
    half = mp.mpf(1)/2
    def zeta2(t): return abs(mp.zeta(half + 1j*t))**2
    def make_integrand(km, kn):
        def f(t):
            s = mp.sin(t*L/2)
            dm = km - t; dn = kn - t
            # singularidades removibles
            if abs(dm) < mp.mpf('1e-9') and abs(dn) < mp.mpf('1e-9'):
                return zeta2(t) * L*L            # diagonal nodo
            if abs(dm) < mp.mpf('1e-9') or abs(dn) < mp.mpf('1e-9'):
                return mp.mpf(0)
            return zeta2(t) * 4*s*s/(dm*dn)
        return f
    # puntos de corte: nodos k_n dentro de [-Tmax,Tmax] + extremos
    nodes = sorted(set([float(x) for x in k if abs(x) < Tmax] + [-Tmax, Tmax, 0.0]))
    G = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            f = make_integrand(k[a], k[b])
            val = mp.quad(f, nodes)
            G[a,b]=val; G[b,a]=val
        print(f"   fila {a+1}/{dim} lista", flush=True)

    gev,_ = mp.eigsy(G); gev = sorted([gev[i] for i in range(dim)])
    print(" Gram eig min/max:", mp.nstr(gev[0],5), mp.nstr(gev[-1],5), flush=True)

    # ---- generalizado: G = R R^T (mp.cholesky lower), B = R^{-1} A R^{-T} ----
    R = mp.cholesky(G)          # lower-tri, G = R * R^T
    Rinv = R**-1
    B = Rinv * A * Rinv.T
    B = (B + B.T)/2
    EB,_ = mp.eigsy(B); EB = sorted([EB[i] for i in range(dim)])
    print(" GENERALIZADO eigsy(B):", flush=True)
    print("   eig[:6]:", [mp.nstr(EB[i],4) for i in range(6)])
    print("   ratios rho_k/rho_0:", [mp.nstr(EB[i]/EB[0],5) for i in range(8)])
    print("   objetivo (k+1)^2:", [(i+1)**2 for i in range(8)])

if __name__ == "__main__":
    run('5.0', 6, 80.0)
