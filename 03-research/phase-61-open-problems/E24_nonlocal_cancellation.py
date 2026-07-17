"""
E24: la cuenta NO-LOCAL explicita.
Descomponer A_lambda(f_k,f_k) del radical en:
   ARCH_k = <f_k|(W02-WR)|f_k>   (masa Omega(0) + Levy E_theta, arquimediano)
   PRIME_k= <f_k|arith|f_k>       (E_prime, NO-LOCAL, saltos f(y)<->f(y+log n))
   eps_k  = ARCH_k - PRIME_k
Ver: (a) ARCH_k, PRIME_k son O(lambda) y se CANCELAN a eps_k~e^{-cL};
     (b) la estructura del residuo (k+1)^2.
"""
import mpmath as mp
mp.mp.dps = 40
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi)

def q_func(m, n, L):
    if m == n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def parts(m, n, L, lam):
    """devuelve (arch, prime) por separado; QW = arch - prime."""
    q = q_func(m, n, L); q0 = q(mp.mpf(0))
    W02 = mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
    def wr(y):
        if y < mp.mpf('1e-12'):
            h = mp.mpf('1e-8'); return ((q(h)-q0)/h+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WR = (LOG4PI+GAMMA)*q0/2 + mp.quad(wr, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    arch = W02 - WR
    prime = mp.mpf(0); mx = int(lam*lam); sv = [True]*(mx+1)
    for i in range(2, int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i, mx+1, i): sv[j] = False
    for p in range(2, mx+1):
        if sv[p]:
            lp = mp.log(p); pm = p; me = 1
            while pm <= mx:
                prime += lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp); pm *= p; me += 1
    return arch, prime

def run(lam, N):
    L = 2*mp.log(mp.mpf(lam)); dim = 2*N+1; idx = list(range(-N, N+1))
    ARCH = mp.zeros(dim); PRIME = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            ar, pr = parts(idx[a], idx[b], L, mp.mpf(lam))
            ARCH[a,b]=ar; ARCH[b,a]=ar; PRIME[a,b]=pr; PRIME[b,a]=pr
    M = ARCH - PRIME
    E, V = mp.eigsy(M); order = sorted(range(dim), key=lambda j: E[j])
    e0 = E[order[0]]
    print(f"\nlambda={lam} N={N} L={mp.nstr(L,5)}  (P_lambda~2lam={2*lam:.1f})")
    print(" k :    eps_k      eps_k/eps_0    ARCH_k       PRIME_k     ARCH-PRIME chk")
    for k in range(6):
        c = V[:, order[k]]
        arch_k = (c.T * ARCH * c)[0,0]
        prime_k = (c.T * PRIME * c)[0,0]
        nrm = (c.T*c)[0,0]
        ek = E[order[k]]
        print(f" {k} : {mp.nstr(ek,4):>10} {mp.nstr(ek/e0,5):>10}   {mp.nstr(arch_k,5):>10} {mp.nstr(prime_k,5):>10}  {mp.nstr(arch_k-prime_k,3)}")
    # mostrar magnitud de cancelacion para k=0
    c0 = V[:, order[0]]
    a0 = (c0.T*ARCH*c0)[0,0]; p0=(c0.T*PRIME*c0)[0,0]
    print(f"  cancelacion k=0: ARCH={mp.nstr(a0,6)} PRIME={mp.nstr(p0,6)} -> eps_0={mp.nstr(a0-p0,4)}  (ratio residuo/pieza ~ {mp.nstr((a0-p0)/a0,3)})")

    # ARCH definida positiva?
    EA,_ = mp.eigsy(ARCH); EA=sorted([EA[i] for i in range(dim)])
    print(f"  ARCH eig min/max: {mp.nstr(EA[0],4)} / {mp.nstr(EA[-1],4)}  (PD si min>0)")
    EP,_ = mp.eigsy(PRIME); EP=sorted([EP[i] for i in range(dim)])
    print(f"  PRIME eig min/max: {mp.nstr(EP[0],4)} / {mp.nstr(EP[-1],4)}")

    # GENERALIZADO (M, ARCH): eig de ARCH^{-1} M  via Cholesky si ARCH PD
    if EA[0] > 0:
        R = mp.cholesky(ARCH); Rinv = R**-1
        B = Rinv * M * Rinv.T; B=(B+B.T)/2
        EB,_ = mp.eigsy(B); EB=sorted([EB[i] for i in range(dim)])
        print(" GENERALIZADO (M, ARCH) ratios rho_k/rho_0:", [mp.nstr(EB[i]/EB[0],5) for i in range(8)])
        print("   objetivo (k+1)^2:", [(i+1)**2 for i in range(8)])

run(7.0, 14)
