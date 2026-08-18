"""
POINT 4 -- the mechanism that closes the gap measured in 115_12.

Claim:   d/ds [ arg prod_{p<=P} (1 - p^{-1/2-is}) ]
       = sum_{n P-smooth} Lambda(n)/sqrt(n) * cos(s log n)

i.e. differentiating the PHASE of the finite Euler factor turns the
multiplicative Moebius-type weight into the additive von Mangoldt sum.
The 1/k of the log-expansion cancels against the k from d/ds.

LHS computed by complex arithmetic + central differences (no series).
RHS computed as an explicit von Mangoldt sum.
"""
import mpmath as mp
mp.mp.dps = 30

def primes_upto(N):
    s = [True]*(N+1); s[0]=s[1]=False
    for i in range(2,int(N**.5)+1):
        if s[i]:
            for j in range(i*i,N+1,i): s[j]=False
    return [i for i,b in enumerate(s) if b]

def argprod(s, P):
    """arg of prod_{p<=P} (1 - p^{-1/2-is}), continuous branch via summing args"""
    tot = mp.mpf(0)
    for p in primes_upto(P):
        z = 1 - mp.mpf(p)**(mp.mpf('-0.5') - mp.mpc(0,1)*s)
        tot += mp.arg(z)
    return tot

def lhs(s, P, h=mp.mpf('1e-8')):
    return (argprod(s+h,P) - argprod(s-h,P))/(2*h)

def rhs(s, P, KMAX=60):
    tot = mp.mpf(0)
    for p in primes_upto(P):
        lp = mp.log(p)
        for k in range(1, KMAX+1):
            n = mp.mpf(p)**k
            if n > mp.mpf('1e18'): break
            tot += lp / mp.sqrt(n) * mp.cos(s*k*lp)
    return tot

print("  d/ds arg prod_{p<=P}(1-p^{-1/2-is})   vs   sum_n Lambda(n) n^{-1/2} cos(s log n)\n")
print("     P     s        LHS (numeric derivative)      RHS (von Mangoldt)         diff")
print("  " + "-"*82)
for P in [3, 7, 19, 53]:
    for s in ['0.4', '1.7', '5.0', '13.9']:
        s = mp.mpf(s)
        L = lhs(s,P); R = rhs(s,P)
        print("  %4d  %6s   %24s  %24s   %.2e"
              % (P, str(s), mp.nstr(L,16), mp.nstr(R,16), float(abs(L-R))))
