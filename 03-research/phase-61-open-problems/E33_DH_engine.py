"""
E33: engine-DH (Weil form de Davenport-Heilbronn) — el control del muro.
QW^DH = -WR_DH - arith_DH  (sin W02: DH entera, sin polo)
  arith_DH = sum_{k<=lam^2} Lambda_DH(k) k^{-1/2} q(log k)   [Lambda_DH exacto, E31]
  WR_DH    = C_DH*q0/2 + int (e^{-y/2}q(y)-q0)/(2 sinh y) dy + q0 log(tanh(L/2))/2
             [peso e^{-y/2} (impar, a=1) -> da psi(3/4); C_DH=(gamma+log4pi)/2+log5 (conductor)]
VALIDACION (C-independiente): ceros de xi_hat_0^DH vs ceros on-line DH (E32): 5.094,14.404,19.309,26.095,33.700,35.891
TEST DEL MURO: signo de eps_0 (¿detecta la NO-RH de DH, o es ciego? NG-E1).
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 40
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi); LOG5 = mp.log(5)

# Lambda_DH(n) exacto
kappa = (mp.sqrt(10-2*mp.sqrt(5)) - 2)/(mp.sqrt(5)-1)
def a_dh(n):
    return [mp.mpf(0), mp.mpf(1), kappa, -kappa, mp.mpf(-1)][n % 5]
def build_LambdaDH(NMAX):
    c = [mp.mpf(0)]*(NMAX+1)
    for n in range(1, NMAX+1):
        s = mp.log(n)*a_dh(n); d = 2
        while d <= n:
            if n % d == 0: s -= a_dh(d)*c[n//d]
            d += 1
        c[n] = s
    return c

def q_func(m, n, L):
    if m == n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def QW_DH_entry(m, n, L, lam, LamDH, Cdh):
    q = q_func(m, n, L); q0 = q(mp.mpf(0))
    # WR_DH con peso e^{-y/2}
    def wr(y):
        if y < mp.mpf('1e-12'):
            h = mp.mpf('1e-8'); return ((q(h)*mp.e**(-h/2)-q0)/h + q0*(-mp.mpf('0.5')))/2  # approx
        return (mp.e**(-y/2)*q(y)-q0)/(2*mp.sinh(y))
    WR = Cdh*q0/2 + mp.quad(wr, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    arith = mp.mpf(0); mx = int(lam*lam)
    for kk in range(2, mx+1):
        arith += LamDH[kk]*(mp.mpf(kk)**mp.mpf('-0.5'))*q(mp.log(kk))
    return -WR - arith

ZZ_DH = [5.094, 14.404, 19.309, 26.095, 33.700, 35.891]

def run(lam_f, N, Cdh):
    lam = mp.mpf(lam_f); L = 2*mp.log(lam); Lf=float(L); dim = 2*N+1; idx = list(range(-N, N+1))
    LamDH = build_LambdaDH(int(lam*lam)+1)
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_DH_entry(idx[a], idx[b], L, lam, LamDH, Cdh); M[a,b]=v; M[b,a]=v
    E, V = mp.eigsy(M); order = sorted(range(dim), key=lambda j: E[j])
    eps = [E[order[k]] for k in range(min(6,dim))]
    print(f"\nlambda={lam_f} N={N} L={Lf:.3f}  Cdh={mp.nstr(Cdh,5)}")
    print(f"  espectro bajo: {[mp.nstr(e,4) for e in eps]}")
    print(f"  eps_0 = {mp.nstr(eps[0],5)}  signo: {'NEGATIVO (detecta!)' if eps[0]<0 else 'positivo'}")
    # validacion: ceros de xi_hat_0^DH (C-independiente)
    ev = np.array([float(mp.re(V[i, order[0]])) for i in range(dim)])
    kn = np.array([2*np.pi*nn/Lf for nn in idx])
    def g(z): return np.sum(ev/(kn+z))
    zs = np.linspace(0.5, 40, 24000); gv = np.array([g(z) for z in zs]); zeros=[]
    for i in range(len(zs)-1):
        if gv[i]*gv[i+1]<0:
            a2,b2=zs[i],zs[i+1]
            for _ in range(50):
                mm=(a2+b2)/2
                if g(a2)*g(mm)<=0: b2=mm
                else: a2=mm
            zeros.append((a2+b2)/2)
    print(f"  ceros xi_hat_0^DH: {[round(z,3) for z in zeros if z<40]}")
    for zt in ZZ_DH:
        if zeros:
            near=min(zeros,key=lambda z:abs(z-zt))
            print(f"    DH-zero {zt} <-> xi_hat-cero {near:.3f} (dif {abs(near-zt):.3f})")

Cdh = (GAMMA+LOG4PI)/2 + LOG5  # conductor 5; parity via e^{-y/2} kernel
run('7.0', 14, Cdh)
