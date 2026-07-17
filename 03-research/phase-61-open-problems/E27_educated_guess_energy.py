"""
E27: cota superior explicita de mu_lambda via el educated guess de CCM.
  k_lambda(u) = E(h)(u) = u^{1/2} sum_{n>=1} h(nu),  u in [lambda^{-1}, lambda]
  h(x) = (pi/2) x^2 (2 pi x^2 - 3) e^{-pi x^2}   (Hermite, integral nula; FT(E(h))=Xi exacto)
Proyecto k_lambda en la base V_n=e^{2pi i n y/L} del engine (y=log u + log lambda in [0,L]),
calculo QW_lambda(k,k)=c^dag M c y la comparo con mu_lambda = eps_0 (menor autovalor).
Si QW(k,k)/||k||^2 ~ mu_lambda -> el guess casi alcanza el minimo (missing step 2).
Si >> mu_lambda -> cuantifica el hueco del guess. Todo en mpmath (mu_lambda ~ e^{-cL}).
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
    # h(x) = (pi/2) x^2 (2 pi x^2 - 3) e^{-pi x^2}
    x2 = x*x
    return (mp.pi/2)*x2*(2*mp.pi*x2 - 3)*mp.exp(-mp.pi*x2)

def run(lam, N):
    lam = mp.mpf(lam); L = 2*mp.log(lam); dim = 2*N+1; idx = list(range(-N, N+1))
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, lam); M[a,b]=v; M[b,a]=v
    E, V = mp.eigsy(M); order = sorted(range(dim), key=lambda j: E[j]); mu = E[order[0]]
    print(f"\nlambda={mp.nstr(lam,4)} N={N} L={mp.nstr(L,5)}  mu_lambda=eps_0={mp.nstr(mu,5)}", flush=True)

    # k_lambda(y): u = e^y / lambda  (y in [0,L] <-> u in [1/lam, lam]); k=u^{1/2} sum_n h(n u)
    def kfun(y):
        u = mp.e**y / lam
        s = mp.mpf(0); n = 1
        while True:
            t = h_riem(n*u)
            s += t; n += 1
            if n*u > 7 and abs(t) < mp.mpf('1e-45'): break
            if n > 100000: break
        return mp.sqrt(u)*s

    # coeficientes de Fourier c_n = (1/L) int_0^L k(y) e^{-2pi i n y/L} dy
    c = []
    for n in idx:
        kn = 2*mp.pi*n/L
        re = mp.quad(lambda y: kfun(y)*mp.cos(kn*y), [0, L])/L
        im = mp.quad(lambda y: -kfun(y)*mp.sin(kn*y), [0, L])/L
        c.append(re + 1j*im)
    cv = mp.matrix(c)
    # ||k||^2 (proyectado) = L * sum |c_n|^2 ; QW(k,k) = c^dag M c
    nrm2 = L*sum(abs(ci)**2 for ci in c)
    Mc = M*cv
    qw = sum(mp.conj(cv[i])*Mc[i] for i in range(dim))
    qw = mp.re(qw)
    rayl = qw/nrm2
    print(f"  ||k||^2={mp.nstr(nrm2,5)}  QW(k,k)={mp.nstr(qw,5)}  Rayleigh={mp.nstr(rayl,5)}", flush=True)
    print(f"  Rayleigh/mu = {mp.nstr(rayl/mu,5)}   (=1 si k alcanza el minimo; >>1 = hueco del guess)", flush=True)
    print(f"  signo QW(k,k): {'+' if qw>0 else '-'}", flush=True)
    # OVERLAP con el autovector verdadero xi_lambda (= missing step 2, O(1) sin piso)
    xi = V[:, order[0]]
    ip = sum(mp.conj(cv[i])*xi[i] for i in range(dim))
    nxi = mp.sqrt(sum(abs(xi[i])**2 for i in range(dim)))
    nc = mp.sqrt(sum(abs(ci)**2 for ci in c))
    ov = abs(ip)/(nxi*nc)
    print(f"  OVERLAP |<k,xi_0>| = {mp.nstr(ov,6)}   (=1 si el guess ES el autovector)", flush=True)
    # overlap con xi_1, xi_2 (indicio 3: extiende a superiores)
    for k1 in (1,2):
        xk = V[:, order[k1]]
        ipk = sum(mp.conj(cv[i])*xk[i] for i in range(dim))
        nk = mp.sqrt(sum(abs(xk[i])**2 for i in range(dim)))
        print(f"     |<k,xi_{k1}>| = {mp.nstr(abs(ipk)/(nk*nc),5)}", flush=True)

for lm, NN in [('5.0',12), ('7.0',14), ('9.0',16)]:
    run(lm, NN)
