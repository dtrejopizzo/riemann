"""
E26: verificar la identidad EXACTA  A_lambda(f,f) = Sum_rho |f_hat(gamma_rho)|^2
para f soportada en [0,L] (truncamiento de primos en lambda^2 es exacto).
Muestra que las autofunciones del radical tienen f_hat EXP-PEQUENA en los ceros,
y que Sum_rho |f_hat_k(gamma_rho)|^2 = eps_k.
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

lam = mp.mpf('7.0'); N = 14
L = 2*mp.log(lam); dim = 2*N+1; idx = list(range(-N, N+1))
M = mp.zeros(dim)
for a in range(dim):
    for b in range(a, dim):
        v = QW_entry(idx[a], idx[b], L, lam); M[a,b]=v; M[b,a]=v
E, V = mp.eigsy(M); order = sorted(range(dim), key=lambda j: E[j])
print(f"lambda=7 N={N} L={mp.nstr(L,5)}  eps_k:", [mp.nstr(E[order[k]],5) for k in range(4)])

# Mellin f_tilde(1/2+i g) = int_0^L f(y) e^{y/2} e^{i g y} dy  (peso e^{y/2}=x^{1/2} de E)
# int_0^L e^{(1/2 + i(k_n+g)) y} dy = (e^{(1/2+i(k_n+g))L}-1)/(1/2+i(k_n+g))
def fhat(c, g, half=True):
    s = mp.mpf(0)
    for i, n in enumerate(idx):
        kn = 2*mp.pi*n/L
        if half:
            al = mp.mpf(1)/2 + 1j*(kn+g)
        else:
            al = 1j*(kn+g)
        s += c[i]*(mp.e**(al*L)-1)/al
    return s

# ceros de zeta (positivos); sum_rho = 2 * sum_{j>0} |f_hat(gamma_j)|^2  (f real)
Mz = 300
print(f" calculando {Mz} ceros de zeta ...", flush=True)
gammas = [mp.im(mp.zetazero(j)) for j in range(1, Mz+1)]
print(" listo. Sum_rho |f_hat_k(g)|^2 vs eps_k:")
for k in range(4):
    c = [V[i, order[k]] for i in range(dim)]
    tot = mp.mpf(0); partial = []
    for j, g in enumerate(gammas):
        tot += 2*abs(fhat(c, g))**2
        if j+1 in (50, 150, 300): partial.append(mp.nstr(tot,5))
    ek = E[order[k]]
    print(f"  k={k}: eps_k={mp.nstr(ek,5)}  Sum(50,150,300)={partial}  ratio Sum/eps={mp.nstr(tot/ek,5)}")
    # tamano de f_hat en el primer cero
    print(f"        |f_hat({mp.nstr(gammas[0],4)})|={mp.nstr(abs(fhat(c,gammas[0])),3)} (exp-pequena)")
