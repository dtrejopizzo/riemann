"""NUMERICAL diagnostic for ONE atom only. No sign certificate for full W."""
import sys
from math import factorial,comb
import mpmath as m
m.mp.dps=int(sys.argv[1]) if len(sys.argv)>1 else 60
N=211;u=m.mpf(63)/2
norm=m.mpf(comb(2*N-2,N-1))/(N*2**(2*N)*u**(2*N-1))
beta=m.beta(m.mpf('1.5'),N-m.mpf('.5'))
def integr(t):
    tau=u*t
    return 2*t*t/(1+t*t)**(N+1)/beta*(m.re(m.digamma(m.mpf('.25')+1j*tau/2))-m.log(m.pi))
arch=m.quad(integr,[0,m.mpf('.025'),m.mpf('.05'),m.mpf('.1'),m.mpf('.2'),m.mpf('.4'),1,m.inf])
polar=-1/(2*(u*u-m.mpf('.25'))**(N+1))/norm
K=m.mpf(N)*2**(N-1)/(factorial(N)*comb(2*N-2,N-1))
r=[]
for j in range(N+1):
    a=m.mpf(factorial(2*N-j))/(2**(N-j)*factorial(N-j)*factorial(j))
    r.append(K*a*(j*(j+1)-2*N)/((2*N-j)*(2*N-j-1)))
contacts=[]
for p in range(2,301):
    if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
    q=p
    while q<=300:
        contacts.append((q,p));q*=p
partial=arch+polar
print('NUMERICAL, digits=',m.mp.dps,'ARCH=',m.nstr(arch,35),'POLAR=',m.nstr(polar,35))
for q,p in sorted(contacts):
    val=2*m.log(p)*m.polyval(list(reversed(r)),u*m.log(q))/m.mpf(q)**32
    partial+=val
    if q in (2,4,5,13,31,97,293):
        print('NUMERICAL partial q<=',q,':',m.nstr(partial,30))
print('This is NOT full W: positive contacts q>300 remain. No quadrature error certificate.')
