from mpmath import mp, mpf, quad, exp, log, sqrt, psi, pi, matrix, eig, findroot
import itertools
mp.dps=30
T=log(3)/2; L=2*T; u2=log(2); v2=2*log(2)/sqrt(2)
nu=lambda u: exp(-u/2)/(1-exp(-2*u))
m0=psi(0,mpf(1)/4)-log(pi)
N=lambda r: quad(nu,[r,mp.inf])
def W(s):
    w=m0-v2+N(T-s)+N(T+s)
    w+= v2/2*((1 if u2>=T-s else 0)+(1 if u2>=T+s else 0))
    return w
ss=[mpf(k)/1000*T for k in range(0,1000)]
Wm=min((W(s),s) for s in ss); print('m0',m0,'W(0)',W(0),'minW',Wm)
# Rayleigh for censored gap: basis of mean-zero polynomials Legendre P1..P5 scaled
from mpmath import legendre
B=[ (lambda k: (lambda t: legendre(k,t/T)))(k) for k in range(1,7)]
def E(f,g):
    inner=lambda u: quad(lambda t:(f(t+u)-f(t))*(g(t+u)-g(t)),[-T,T-u])
    a=quad(lambda u: nu(u)*inner(u),[0,L])
    return a+ v2/2*inner(u2)
n=len(B)
A=matrix(n,n); G=matrix(n,n)
for i in range(n):
  for j in range(i,n):
    A[i,j]=A[j,i]=E(B[i],B[j]); G[i,j]=G[j,i]=quad(lambda t:B[i](t)*B[j](t),[-T,T])
import mpmath
ev=mpmath.eigsy(mpmath.cholesky(G)**-1*A*(mpmath.cholesky(G)**-1).T)[0]
print('Rayleigh eigs',[mpmath.nstr(e,8) for e in ev])
print('g_upper+minW', ev[0]+Wm[0])
d2=L-(4*mpmath.sinh(T/2))**2/(T+mpmath.sinh(T)); print('delta^2',d2, d2/L)
f=lambda t:t
print('R(t)=',E(f,f)/quad(lambda t:t*t,[-T,T]))
print('W(0.1440)',W(mpf('0.1440')),'W(T-0.01)',W(T-mpf('0.01')))
