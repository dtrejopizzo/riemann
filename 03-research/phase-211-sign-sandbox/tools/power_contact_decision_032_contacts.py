"""One fixed atom N211 k1 u31.5. Exact prime/polar intervals, no quadrature."""
from fractions import Fraction as F
from math import factorial,comb,isqrt
import power_fixed_grid_003 as C
N=211;u=F(63,2);M=512
K=F(N*2**(N-1),factorial(N)*comb(2*N-2,N-1))
# Divided-power coefficients: polynomial r(x)=sum a_j x^j/j!.
a=[K*F(factorial(2*N-j),2**(N-j)*factorial(N-j))*F(j*(j+1)-2*N,(2*N-j)*(2*N-j-1)) for j in range(N+1)]
def contact(q,p):
 x=u*C.logq(q)
 v=C.I(a[N])
 for j in range(N-1,-1,-1):v=C.I(a[j])+x*v/F(j+1)
 return 2*C.logq(p)*C.I(v.lo/q**32,v.hi/q**32)
contacts=[]
for p in range(2,M+1):
 if all(p%d for d in range(2,isqrt(p)+1)):
  q=p
  while q<=M:contacts.append((q,p));q*=p
contacts.sort()
prime=sum((contact(q,p) for q,p in contacts),C.I(0))
norm=F(comb(2*N-2,N-1),N*2**(2*N))/u**(2*N-1)
polar=-F(1,2)/(u*u-F(1,4))**(N+1)/norm
# Entire omitted tail, retaining positivity proved in ARITHMETIC_DIFFERENCES019.
# x^-32 (log x)^ell is unimodal; sum_(n>M) <= (1+32/M) integral_M^infty.
L=C.logq(M).hi
iv=F(1,31*M**31);total=F()
for ell in range(1,N+2):
 iv=L**ell/F(31*M**31)+F(ell,31)*iv
 total+=abs(a[ell-1])*u**(ell-1)*iv/factorial(ell-1)
tail=2*(1+F(32,M))*total
assert prime.hi-prime.lo<F(1,10**40)
assert 0<tail<F(11,10**16)
if __name__=='__main__':
 def out(label,z):
  S=10**35
  if isinstance(z,C.I):print(label,'[',int(z.lo*S//1),',',int(-((-z.hi*S)//1)),']/10^35')
  else:print(label,float(z))
 out('prime<=512',prime);out('polar',C.I(polar));out('complete omitted tail upper',tail)
 print('PASS contacts/polar/full-tail for ONE atom; full W requires independent ARCH interval.')
