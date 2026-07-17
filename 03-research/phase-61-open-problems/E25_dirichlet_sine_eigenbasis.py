"""
E25: TEST CRUCIAL para 2.3.F. ¿Son los senos Dirichlet s_k=sin((k+1)pi y/L)
los autovectores de la forma de Weil M con autovalor ∝ (k+1)^2?
  S_{jk} = <s_j | M | s_k>   (M = forma de Weil del engine, base Fourier e^{2pi i n y/L})
Si S es DIAGONAL con S_kk ∝ (k+1)^2  =>  M|radical = Laplaciano Dirichlet en [0,L]. Cerrado.
Cambio de base C (seno->Fourier) numerico; S = C^T M C en mpmath (radical ~ e^{-cL}).
"""
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

def cproj(k, n, L):
    # c^k_n = (1/L) int_0^L sin((k+1)pi y/L) e^{-2pi i n y/L} dy   (real)
    a = (k+1)*mp.pi/L; b = 2*mp.pi*n/L
    f = lambda y: mp.sin(a*y)*mp.cos(b*y)   # parte real (la imag se anula)
    return mp.quad(f, [0, L])/L

def run(lam, N, K=7):
    L = 2*mp.log(mp.mpf(lam)); dim = 2*N+1; idx = list(range(-N, N+1))
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, mp.mpf(lam)); M[a,b]=v; M[b,a]=v
    # C: dim x K, columnas = senos Dirichlet en base Fourier
    C = mp.zeros(dim, K)
    for k in range(K):
        for i, n in enumerate(idx):
            C[i, k] = cproj(k, n, L)
    # Gram de los senos truncados y S = C^T M C
    G = C.T * C
    S = C.T * M * C
    print(f"\nlambda={lam} N={N} L={mp.nstr(L,5)}")
    # diagonal normalizada S_kk / G_kk  = <s_k|M|s_k>/<s_k|s_k>
    diag = [S[k,k]/G[k,k] for k in range(K)]
    print(" S_kk/G_kk (Rayleigh de senos Dirichlet):", [mp.nstr(d,4) for d in diag])
    print("   ratios /[0]:", [mp.nstr(diag[k]/diag[0],5) for k in range(K)])
    print("   (k+1)^2:", [(k+1)**2 for k in range(K)])
    # diagonalidad: norma off-diag relativa (en metrica G^{-1/2})
    R = mp.cholesky(G); Rinv = R**-1
    B = Rinv * S * Rinv.T   # S en base ortonormalizada de senos
    offmax = max(abs(B[i,j]) for i in range(K) for j in range(K) if i!=j)
    dmin = min(abs(B[i,i]) for i in range(K))
    print(f"   diagonalidad de M en base seno: max|offdiag|={mp.nstr(offmax,3)}  min|diag|={mp.nstr(dmin,3)}  ratio={mp.nstr(offmax/dmin,3)}")
    EB,_ = mp.eigsy(B); EB=sorted([EB[i] for i in range(K)])
    print("   eig(B) ratios:", [mp.nstr(EB[k]/EB[0],5) for k in range(K)])

run(9.0, 16)
run(13.0, 21)
