"""
EL SELECTOR ARITMETICO: la formula explicita de Riemann-Weil.

Esto es 'lo que GUE no tiene': la identidad EXACTA que ata los ceros a los
primos. Una matriz GUE no la satisface; los ceros de Riemann si.

Formula (Bombieri, RH Millennium), h par, g(u) = (1/2pi) int h(r) e^{-iur} dr:

  sum_gamma h(gamma)  =  h(i/2) + h(-i/2)             [polo de zeta en s=1]
                        - g(0) log(pi)                 [arquimediano cte]
                        + (1/2pi) int h(r) Re psi(1/4 + i r/2) dr   [arquimediano]
                        - 2 sum_n  Lambda(n)/sqrt(n) g(log n)       [PRIMOS]

Verificamos LHS (suma sobre TUS 10000 ceros) == RHS (primos + arquimediano).
Si coinciden, el selector queda EXHIBIDO: los ceros no son GUE generico,
estan encadenados a los primos por esta ecuacion.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 20
g_zeros = np.loadtxt("zeros_10000.txt")

# test function: gaussiana h(r) = exp(-r^2 / (2 sigma^2))
def run(sigma):
    h = lambda r: math.exp(-r*r/(2*sigma*sigma))
    # g(u) = (sigma/sqrt(2pi)) exp(-sigma^2 u^2 / 2)
    gfun = lambda u: (sigma/math.sqrt(2*math.pi))*math.exp(-sigma*sigma*u*u/2)

    # ----- LHS: suma sobre los ceros (todos: +gamma y -gamma) -----
    LHS = 2.0*np.sum(np.exp(-g_zeros**2/(2*sigma*sigma)))  # h par, zeros simetricos

    # ----- RHS -----
    # polo:  h(i/2)+h(-i/2) = 2 exp(+ (1/4)/(2 sigma^2))
    polo = 2.0*math.exp((0.25)/(2*sigma*sigma))
    # arquimediano cte:  -g(0) log pi
    g0 = sigma/math.sqrt(2*math.pi)
    arq_cte = -g0*math.log(math.pi)
    # arquimediano integral: (1/2pi) int h(r) Re psi(1/4 + i r/2) dr
    def integrand(r):
        return h(r)*float(mp.re(mp.digamma(mp.mpc(0.25, r/2))))
    R = 12*sigma
    xs = np.linspace(-R, R, 6000)
    vals = np.array([integrand(r) for r in xs])
    arq_int = np.trapezoid(vals, xs)/(2*math.pi)
    # primos: -2 sum Lambda(n)/sqrt(n) g(log n)
    def lambdas(Nmax):
        lam = np.zeros(Nmax+1)
        sieve = np.ones(Nmax+1, bool); sieve[:2]=False
        for i in range(2, Nmax+1):
            if sieve[i]:
                lp=math.log(i); pk=i
                while pk<=Nmax:
                    lam[pk]=lp; pk*=i
                sieve[i*i::i]=False
        return lam
    Nmax = int(math.exp(8.0/sigma)) + 50   # g(log n) decae rapido
    Nmax = max(Nmax, 200)
    lam = lambdas(Nmax)
    primos = 0.0
    for n in range(2, Nmax+1):
        if lam[n]>0:
            primos += lam[n]/math.sqrt(n)*gfun(math.log(n))
    primos *= -2.0

    RHS = polo + arq_cte + arq_int + primos
    return LHS, RHS, polo, arq_cte, arq_int, primos

print(f"{'sigma':>6} {'LHS (ceros)':>14} {'RHS (primos+arq)':>18} {'error rel':>12}")
for sigma in [2.0, 3.0, 4.0, 6.0]:
    LHS, RHS, polo, arqc, arqi, pr = run(sigma)
    err = abs(LHS-RHS)/abs(LHS)
    print(f"{sigma:6.1f} {LHS:14.6f} {RHS:18.6f} {err:12.2e}")

print()
LHS, RHS, polo, arqc, arqi, pr = run(4.0)
print("Descomposicion del RHS (sigma=4):")
print(f"  polo (zeta en s=1)     = {polo:+.5f}")
print(f"  arquimediano cte       = {arqc:+.5f}")
print(f"  arquimediano integral  = {arqi:+.5f}")
print(f"  PRIMOS                 = {pr:+.5f}   <-- lo que GUE no tiene")
print(f"  suma RHS               = {RHS:+.5f}")
print(f"  LHS (ceros)            = {LHS:+.5f}")
