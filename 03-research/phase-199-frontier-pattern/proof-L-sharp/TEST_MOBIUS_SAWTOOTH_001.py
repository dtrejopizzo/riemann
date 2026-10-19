# TEST_MOBIUS_SAWTOOTH_001: re-normalize Mori V Table 1 ratios; compare increments with mu(m) and Lambda(m). NUMERICO.
from mpmath import mp, mpf, pi, sqrt, exp, log, factorial
from sympy import mobius, factorint
mp.dps=30
R={7:4.21,11:4.72,12:4.11,13:4.94,14:4.55,15:4.63,16:4.49,17:4.70,18:4.38,19:5.34,20:4.90}
N={7:240,11:320,12:300,13:330,14:370,15:370,16:440,17:420,18:440,19:470,20:570}
def fuchs(n,c): return 4*sqrt(pi)*mpf(8)**n/factorial(n)*c**(n+mpf(1)/2)*exp(-2*c)
# Mori V: (1-l4)/fuchs4 rises smoothly 0.89 (mu=11) -> 0.94 (mu=20); linear interp used for reconstruction only
def corr(mu): return 0.89+(0.94-0.89)*(mu-11)/9
print("mu N N/(ac) kappa4 lam_rec kappa_l2 kappa_scale")
K2={};KS={}
for mu in sorted(R):
    c=2*pi*mu; d4=fuchs(4,c)*corr(mu); lam=R[mu]*d4
    K2[mu]=lam/fuchs(2,c); KS[mu]=lam/(mu**4.5*exp(-4*pi*mu))
    print(mu,N[mu],float(N[mu]/(log(mu)/2*c)),R[mu],mp.nstr(lam,4),mp.nstr(K2[mu],4),mp.nstr(KS[mu],4))
def Lam(m): f=factorint(m); return len(f)==1
print("m mu(m) primepower dk4 dlogk4 dlogk2 dlogkS")
for m in range(11,20):
    a,b=m,m+1
    print(m,mobius(m),Lam(m),round(R[b]-R[a],2),mp.nstr(log(R[b]/R[a]),3),mp.nstr(log(K2[b]/K2[a]),3),mp.nstr(log(KS[b]/KS[a]),3))
