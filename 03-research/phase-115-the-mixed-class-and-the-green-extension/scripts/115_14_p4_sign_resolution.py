"""
POINT 4, sign resolution.

115_13 wrote phi = -arg E.  That is calibrated wrong.  The archimedean case
fixes the convention: for S={infinity},
    E_inf(s) = L_inf(1/2+is) = pi^{-1/4-is/2} Gamma(1/4+is/2),
    arg E_inf(s) = -(s/2) log pi + arg Gamma(1/4+is/2) = theta(s),
the Riemann-Siegel theta function, and theta'(s) ~ (1/2)log(s/2pi) > 0.
A de Branges phase must be INCREASING, so phi = +arg E, not -arg E.

Consequences to check numerically:
  (1) phi_inf = theta  and theta' > 0
  (2) d/ds arg prod_{p<=P} L_p(1/2+is) = - sum_{n P-smooth} Lambda(n) n^{-1/2} cos(s log n)
      (MINUS: this is the standard Riemann-von Mangoldt density, N(T)=theta/pi+1+S(T))
  (3) phi_S' = theta' - sum ... > 0
"""
import mpmath as mp
mp.mp.dps = 30

def primes_upto(N):
    s=[True]*(N+1); s[0]=s[1]=False
    for i in range(2,int(N**.5)+1):
        if s[i]:
            for j in range(i*i,N+1,i): s[j]=False
    return [i for i,b in enumerate(s) if b]

def theta(s):   # arg E_inf
    return mp.im(mp.loggamma(mp.mpf('0.25')+mp.mpc(0,0.5)*s)) - s/2*mp.log(mp.pi)

def argL(s,P):  # arg prod_{p<=P} L_p(1/2+is),  L_p = (1-p^{-1/2-is})^{-1}
    t=mp.mpf(0)
    for p in primes_upto(P):
        t += -mp.arg(1 - mp.mpf(p)**(mp.mpf('-0.5')-mp.mpc(0,1)*s))
    return t

def d(fn, s, h=mp.mpf('1e-8')):
    return (fn(s+h)-fn(s-h))/(2*h)

def vm(s,P,KMAX=60):
    t=mp.mpf(0)
    for p in primes_upto(P):
        lp=mp.log(p)
        for k in range(1,KMAX+1):
            n=mp.mpf(p)**k
            if n>mp.mpf('1e18'): break
            t += lp/mp.sqrt(n)*mp.cos(s*k*lp)
    return t

print("(1)  theta' > 0  (de Branges phase must increase)")
for s in ['2','6','14','30','100']:
    s=mp.mpf(s)
    print("      s=%6s   theta(s)=%14s   theta'(s)=%12s   (1/2)log(s/2pi)=%12s"
          % (str(s), mp.nstr(theta(s),8), mp.nstr(d(theta,s),8),
             mp.nstr(mp.log(s/(2*mp.pi))/2,8)))

print("\n(2)  d/ds arg prod L_p   vs   MINUS von Mangoldt")
print("       P     s          d/ds arg prod L_p          -sum Lambda/sqrt(n) cos        diff")
print("     " + "-"*80)
for P in [3,7,19,53]:
    for s in ['0.4','1.7','5.0','13.9']:
        s=mp.mpf(s)
        L=d(lambda x: argL(x,P), s); R=-vm(s,P)
        print("     %4d  %6s   %24s  %24s   %.2e"
              % (P,str(s),mp.nstr(L,16),mp.nstr(R,16),float(abs(L-R))))

print("\n(3)  phi_S' = theta' - vonMangoldt  > 0 ?")
print("       P      s        theta'        -vM          phi_S'")
for P in [7,53,211]:
    for s in ['14','30','100','1000']:
        s=mp.mpf(s)
        a=d(theta,s); b=-vm(s,P)
        print("     %4d  %6s   %10s  %10s   %12s   %s"
              % (P,str(s),mp.nstr(a,7),mp.nstr(b,7),mp.nstr(a+b,8),
                 "OK" if a+b>0 else "NEGATIVE"))
