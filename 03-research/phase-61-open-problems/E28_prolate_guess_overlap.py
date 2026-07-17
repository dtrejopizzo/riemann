"""
E28: el educated guess REAL de CCM (prolata h_lambda) vs el autovector verdadero xi_0.
PW_lambda = -d((lambda^2-x^2)d) + (2 pi lambda x)^2 en [-lambda,lambda] (FD).
h_lambda = combinacion de h_{0,lambda}, h_{4,lambda} (pares) con integral nula.
k_lambda(u)=u^{1/2} sum_n h_lambda(n u). Overlap |<k_lambda, xi_0>| (engine, mpmath).
Compara Hermite (E27, ~0.7) vs prolata: ¿la prolata da overlap -> 1? (= CCM step 2 ok)
"""
import numpy as np
import mpmath as mp
from scipy.linalg import eigh_tridiagonal
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

def prolate_hlambda(lam, Ng=4000):
    """h_{0,lambda}, h_{4,lambda} de PW_lambda por FD en [-lam,lam]; combo integral nula."""
    x = np.linspace(-lam, lam, Ng+2)[1:-1]   # interior (evita endpoints singulares)
    dx = x[1]-x[0]
    p = lam**2 - x**2                          # p(x)=lambda^2-x^2 >0 interior
    phalf = lam**2 - (x+dx/2)**2               # p en x_{i+1/2}
    pm = lam**2 - (x-dx/2)**2
    diag = (phalf+pm)/dx**2 + (2*np.pi*lam*x)**2
    off = -phalf[:-1]/dx**2
    w, V = eigh_tridiagonal(diag, off)
    # autofunciones pares: indices 0,2,4,... ; queremos n=0 y n=4 (3a par)
    def even_idx(j):  # j-esima par
        cnt=-1
        for i in range(len(w)):
            v=V[:,i]
            # paridad: v(-x)=+-v(x); aprox v[0] vs v[-1]
            if np.sign(v[0])==np.sign(v[-1]) and abs(abs(v[0])-abs(v[-1]))<0.3*np.max(np.abs(v)):
                cnt+=1
                if cnt==j: return i
        return None
    i0 = 0
    i4 = None
    # contar pares por nodos: tomar los autovectores 0 y 4 en orden (espectro PW ~ Hermite)
    h0 = V[:,0]; h4 = V[:,4]
    # normalizar signo +
    if h0[Ng//2]<0: h0=-h0
    if h4[Ng//2]<0: h4=-h4
    I0 = np.sum(h0)*dx; I4 = np.sum(h4)*dx
    # combo integral nula: h = h4 - (I4/I0) h0
    h = h4 - (I4/I0)*h0
    return x, h, dx

def run(lam_f, N, Ng=4000):
    lam = mp.mpf(lam_f); L = 2*mp.log(lam); dim = 2*N+1; idx = list(range(-N, N+1))
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, lam); M[a,b]=v; M[b,a]=v
    E, Vm = mp.eigsy(M); order = sorted(range(dim), key=lambda j: E[j])
    xi0 = np.array([float(mp.re(Vm[i, order[0]])) for i in range(dim)])  # autovector ground (O(1))
    xi2 = np.array([float(mp.re(Vm[i, order[2]])) for i in range(dim)])

    lamf = float(lam); Lf = float(L)
    x, hgrid, dx = prolate_hlambda(lamf, Ng)
    def h_interp(t):  # h_lambda(t) por interp lineal, 0 fuera de [-lam,lam]
        return np.interp(t, x, hgrid, left=0.0, right=0.0)
    # k_lambda(y) en grilla y, u=e^y/lam
    Ny = 2000; ys = np.linspace(0, Lf, Ny)
    kvals = np.empty(Ny)
    for i, y in enumerate(ys):
        u = np.exp(y)/lamf
        nmax = int(lamf/u)+1
        ns = np.arange(1, nmax+1)
        kvals[i] = np.sqrt(u)*np.sum(h_interp(ns*u))
    # coeficientes Fourier c_n (float64)
    c = np.empty(dim, dtype=complex)
    for j, n in enumerate(idx):
        kn = 2*np.pi*n/Lf
        integ = kvals*np.exp(-1j*kn*ys)
        c[j] = np.trapz(integ, ys)/Lf
    nc = np.linalg.norm(c)
    ov0 = abs(np.vdot(c, xi0))/(nc*np.linalg.norm(xi0))
    ov2 = abs(np.vdot(c, xi2))/(nc*np.linalg.norm(xi2))
    print(f"lambda={lam_f} N={N} Ng={Ng}: PROLATA  |<k,xi_0>|={ov0:.4f}  |<k,xi_2>|={ov2:.4f}", flush=True)

for lm, NN in [('5.0',12), ('7.0',14), ('9.0',16)]:
    run(lm, NN)
