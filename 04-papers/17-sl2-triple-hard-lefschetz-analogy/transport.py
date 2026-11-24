# Transport identity check: Q = A_inf - P for hhat(r)=(r^2+1/4)^2 exp(-r^2/sigma^2).
import time, mpmath as mp, sympy as sp
t0=time.time(); mp.mp.dps=30
logpi=mp.log(mp.pi)
Psi=lambda r: mp.re(mp.digamma(mp.mpf(1)/4+1j*r/2))-logpi
u,S=sp.symbols('u S',positive=True)
G=S*sp.sqrt(sp.pi)*sp.exp(-S**2*u**2/4)          # int exp(-r^2/S^2)cos(ur)dr
gexpr=(sp.diff(G,u,4)-sp.Rational(1,2)*sp.diff(G,u,2)+sp.Rational(1,16)*G)/(2*sp.pi)
gfun=sp.lambdify((u,S),gexpr,'mpmath')
Z=[mp.im(mp.zetazero(k)) for k in range(1,301)]
NMAX=20000
sieve=[True]*(NMAX+1); pp=[]
for p in range(2,NMAX+1):
    if sieve[p]:
        for j in range(p*p,NMAX+1,p): sieve[j]=False
        q=p
        while q<=NMAX: pp.append((q,mp.log(p))); q*=p
for s in [2,3,4]:
    sig=mp.mpf(s); h=lambda r:(r**2+mp.mpf(1)/4)**2*mp.exp(-r**2/sig**2)
    Q=mp.fsum(2*h(z) for z in Z)
    A=mp.quad(lambda r:h(r)*Psi(r),[0,mp.mpf('6.2898'),20,60,mp.inf])/mp.pi
    gI=mp.quad(lambda r:h(r)*abs(Psi(r)),[0,mp.mpf('6.2898'),20,60,mp.inf])/mp.pi
    P=mp.fsum(2*L/mp.sqrt(n)*gfun(mp.log(n),sig) for n,L in pp)
    print(s,'Q',mp.nstr(Q,8),'A',mp.nstr(A,10),'P',mp.nstr(P,10),'res',mp.nstr(Q-(A-P),3),'gI/Q',mp.nstr(gI/Q,3))
print('time %.1fs'%(time.time()-t0))
