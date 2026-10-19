# AUDIT_200_CERTDH_001: independent checks (mpmath, 30 digits) + zeta control via the same Galerkin template
from mpmath import mp, mpf, sqrt, log, pi, digamma, euler, gamma, zeta, mpc, findroot, dirichlet, exp, quad, inf
mp.dps=35
kap=(sqrt(10-2*sqrt(5))-2)/(sqrt(5)-1); print('kappa',kap)
chi={1:1,2:1j,3:-1j,4:-1,0:0}
a=[ (mpc(1,-kap)*chi[n%5]).real for n in range(1,6)]; print('a_n=Re((1-ik)chi(n))',a)
# Gauss sum root numbers
for c in (chi,{k:(v.conjugate() if isinstance(v,complex) else v) for k,v in chi.items()}):
    g=sum(c[r]*exp(2j*pi*r/5) for r in range(1,5)); print('eps(chi)=tau/(i sqrt5)=',g/(1j*sqrt(5)))
co=[1,kap,-kap,-1,0]
F=lambda s: 5**(-s)*sum(co[r-1]*zeta(s,mpf(r)/5) for r in range(1,5))
Lam=lambda s:(mpf(5)/pi)**(s/2)*gamma((s+1)/2)*F(s)
for s in (mpc(0.3,2),mpc(0.8,17.5),mpc(2,-5),mpc(0.1,40)): print('FE',s,abs(Lam(s)-Lam(1-s))/abs(Lam(s)))
r=findroot(F,mpc(0.8085,85.6993)); print('zero',r,abs(F(r)))
C0=log(5/pi)+digamma(mpf(3)/4); print('C0',C0, 'closed', log(5)-log(pi)-euler+pi/2-3*log(2))
# Levy check: Re psi(3/4+i t/2)+log(5/pi) - C0 == int (1-cos tu) K
t=mpf(7); K=lambda u:2*exp(-1.5*u)/(1-exp(-2*u))
print('Levy', (digamma(mpf(3)/4+0.5j*t)).real+log(5/pi)-C0, quad(lambda u:(1-mp.cos(t*u))*K(u),[0,1,5,inf]))
print('b2=kappa log2',kap*log(2))
