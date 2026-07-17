"""
E30: ceros de xi_hat_lambda (FT del ground state del engine) vs ceros de zeta.
xi_hat_0(z) = 2 sin(zL/2) g(z), g(z)=sum_n (ev)_n/(k_n+z), k_n=2pi n/L.
Los ceros espurios de la caja estan en z=k_m (sin). Los genuinos = ceros de g(z),
que deben converger a 14.1347, 21.022, 25.011, ... (ceros de zeta) [Outlook CCM].
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 40
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

ZZ = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]  # ceros de zeta

def run(lam_f, N):
    lam = mp.mpf(lam_f); L = 2*mp.log(lam); Lf=float(L); dim = 2*N+1; idx = list(range(-N, N+1))
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, lam); M[a,b]=v; M[b,a]=v
    E, V = mp.eigsy(M); order = sorted(range(dim), key=lambda j: E[j])
    ev = np.array([float(mp.re(V[i, order[0]])) for i in range(dim)])
    kn = np.array([2*np.pi*n/Lf for n in idx])
    def g(z): return np.sum(ev/(kn+z))
    # escanear z, hallar ceros (cambios de signo) de g
    zs = np.linspace(0.5, 35, 20000); gv = np.array([g(z) for z in zs])
    zeros = []
    for i in range(len(zs)-1):
        if gv[i]*gv[i+1] < 0:
            # refinar por biseccion
            a,b = zs[i],zs[i+1]
            for _ in range(60):
                m=(a+b)/2
                if g(a)*g(m)<=0: b=m
                else: a=m
            zeros.append((a+b)/2)
    print(f"\nlambda={lam_f} N={N} L={Lf:.3f}  k_N={kn.max():.2f}")
    print(f"  ceros de g(z) en [0.5,35]: {[round(z,3) for z in zeros]}")
    print(f"  ceros de zeta:             {ZZ}")
    # emparejar
    for zt in ZZ:
        if zeros:
            near = min(zeros, key=lambda z: abs(z-zt))
            print(f"    zeta {zt:.6f} <-> g-cero {near:.6f}  (dif {abs(near-zt):.2e})")

run('7.0', 28)
run('11.0', 34)
run('13.0', 40)
