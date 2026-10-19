"""
THE ARITHMETIC SELECTOR: the Riemann-Weil explicit formula.

This is 'what GUE lacks': the EXACT identity tying the zeros to the
primes. A GUE matrix does not satisfy it; the Riemann zeros do.

Formula (Bombieri, RH Millennium problem description), h even, g(u) = (1/2pi) int h(r) e^{-iur} dr:

  sum_gamma h(gamma)  =  h(i/2) + h(-i/2)             [pole of zeta at s=1]
                        - g(0) log(pi)                 [archimedean constant]
                        + (1/2pi) int h(r) Re psi(1/4 + i r/2) dr   [archimedean]
                        - 2 sum_n  Lambda(n)/sqrt(n) g(log n)       [PRIMES]

We check LHS (sum over the 10000 zeros) == RHS (primes + archimedean).
If they agree, the selector is EXHIBITED: the zeros are not generic GUE,
they are chained to the primes by this equation.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 20
g_zeros = np.loadtxt("zeros_10000.txt")

# test function: Gaussian h(r) = exp(-r^2 / (2 sigma^2))
def run(sigma):
    h = lambda r: math.exp(-r*r/(2*sigma*sigma))
    # g(u) = (sigma/sqrt(2pi)) exp(-sigma^2 u^2 / 2)
    gfun = lambda u: (sigma/math.sqrt(2*math.pi))*math.exp(-sigma*sigma*u*u/2)

    # ----- LHS: sum over the zeros (all: +gamma and -gamma) -----
    LHS = 2.0*np.sum(np.exp(-g_zeros**2/(2*sigma*sigma)))  # h even, symmetric zeros

    # ----- RHS -----
    # pole:  h(i/2)+h(-i/2) = 2 exp(+ (1/4)/(2 sigma^2))
    polo = 2.0*math.exp((0.25)/(2*sigma*sigma))
    # archimedean constant:  -g(0) log pi
    g0 = sigma/math.sqrt(2*math.pi)
    arq_cte = -g0*math.log(math.pi)
    # archimedean integral: (1/2pi) int h(r) Re psi(1/4 + i r/2) dr
    def integrand(r):
        return h(r)*float(mp.re(mp.digamma(mp.mpc(0.25, r/2))))
    R = 12*sigma
    xs = np.linspace(-R, R, 6000)
    vals = np.array([integrand(r) for r in xs])
    arq_int = np.trapezoid(vals, xs)/(2*math.pi)
    # primes: -2 sum Lambda(n)/sqrt(n) g(log n)
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
    Nmax = int(math.exp(8.0/sigma)) + 50   # g(log n) decays fast
    Nmax = max(Nmax, 200)
    lam = lambdas(Nmax)
    primos = 0.0
    for n in range(2, Nmax+1):
        if lam[n]>0:
            primos += lam[n]/math.sqrt(n)*gfun(math.log(n))
    primos *= -2.0

    RHS = polo + arq_cte + arq_int + primos
    return LHS, RHS, polo, arq_cte, arq_int, primos

print(f"{'sigma':>6} {'LHS (zeros)':>14} {'RHS (primes+arch)':>18} {'rel error':>12}")
for sigma in [2.0, 3.0, 4.0, 6.0]:
    LHS, RHS, polo, arqc, arqi, pr = run(sigma)
    err = abs(LHS-RHS)/abs(LHS)
    print(f"{sigma:6.1f} {LHS:14.6f} {RHS:18.6f} {err:12.2e}")

print()
LHS, RHS, polo, arqc, arqi, pr = run(4.0)
print("Decomposition of the RHS (sigma=4):")
print(f"  pole (zeta at s=1)     = {polo:+.5f}")
print(f"  archimedean constant  = {arqc:+.5f}")
print(f"  archimedean integral  = {arqi:+.5f}")
print(f"  PRIMES                = {pr:+.5f}   <-- what GUE lacks")
print(f"  RHS total             = {RHS:+.5f}")
print(f"  LHS (zeros)           = {LHS:+.5f}")
