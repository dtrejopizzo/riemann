"""
E29: ¿el overlap |<k_lambda, xi_0>| -> 1 al crecer N (a lambda fijo)?
Si si, el 0.7 de E27/E28 era artefacto de truncacion (CCM usan N=120).
lambda=7 fijo, N = 14,20,28,36. Guess Hermite (=prolata, E28).
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
def h_riem(x):
    x2 = x*x
    return (mp.pi/2)*x2*(2*mp.pi*x2 - 3)*mp.exp(-mp.pi*x2)

lam = mp.mpf('7.0'); L = 2*mp.log(lam)
def kfun(y):
    u = mp.e**y / lam; s = mp.mpf(0); n = 1
    while True:
        t = h_riem(n*u); s += t; n += 1
        if n*u > 7 and abs(t) < mp.mpf('1e-45'): break
        if n > 100000: break
    return mp.sqrt(u)*s

# coeficientes de Fourier hasta Nmax (se reusan para cada N)
Nmax = 36; idxmax = list(range(-Nmax, Nmax+1))
print("precomputando coeficientes de Fourier de k_lambda ...", flush=True)
call = {}
for n in idxmax:
    kn = 2*mp.pi*n/L
    re = mp.quad(lambda y: kfun(y)*mp.cos(kn*y), [0, L])/L
    im = mp.quad(lambda y: -kfun(y)*mp.sin(kn*y), [0, L])/L
    call[n] = re + 1j*im
print("listo.\n", flush=True)

for N in (14, 20, 28, 36):
    dim = 2*N+1; idx = list(range(-N, N+1)); M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, lam); M[a,b]=v; M[b,a]=v
    E, V = mp.eigsy(M); order = sorted(range(dim), key=lambda j: E[j])
    c = [call[n] for n in idx]; nc = mp.sqrt(sum(abs(ci)**2 for ci in c))
    xi0 = [V[i, order[0]] for i in range(dim)]
    nx0 = mp.sqrt(sum(abs(xi0[i])**2 for i in range(dim)))
    ip0 = sum(mp.conj(c[i])*xi0[i] for i in range(dim))
    ov0 = abs(ip0)/(nc*nx0)
    # fraccion del guess capturada por los primeros 6 modos pares
    capt = mp.mpf(0)
    for k1 in range(0, min(8,dim)):
        xk = [V[i, order[k1]] for i in range(dim)]
        nk = mp.sqrt(sum(abs(xk[i])**2 for i in range(dim)))
        capt += (abs(sum(mp.conj(c[i])*xk[i] for i in range(dim)))/(nc*nk))**2
    print(f"N={N}: |<k,xi_0>|={mp.nstr(ov0,5)}  eps_0={mp.nstr(E[order[0]],4)}  captura 8 modos={mp.nstr(capt,5)}", flush=True)
