import json,numpy as np
from numpy.polynomial import legendre as Lg
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
E=json.load(open('MORI15_EXTREMAL_001_data/p0_eig.json')); v=np.array([float(x) for x in E['vectors'][0]])
N=1664; a=0.5*np.log(15); I=np.arange(0,N,2)
coef=np.zeros(N); coef[I]=v*np.sqrt((2*I+1)/(2*a))
xg,wg=Lg.leggauss(2000); s=(xg+1)*a; w=wg*a
g=Lg.legval(s/a-1,coef)          # ǧ(s)=g(-a+s)
print('norm',np.sum(w*g*g),'int g',np.sum(w*g))
A=np.sum(w*g*np.exp(s/2)); B=np.sum(w*g*np.exp(-s/2))
Lj=[np.sum(w*g*np.exp(-(2*j+.5)*s)) for j in range(1,400)]
SL=sum(x*x for x in Lj)
def conv(t):
    # (ǧ*ǧ)(t)=∫ ǧ(r)ǧ(t-r) dr, r in (max(0,t-2a),min(t,2a))
    lo,hi=max(0,t-2*a),min(t,2*a)
    if hi<=lo: return 0.
    r=(xg+1)/2*(hi-lo)+lo; ww=wg*(hi-lo)/2
    return np.sum(ww*Lg.legval(r/a-1,coef)*Lg.legval((t-r)/a-1,coef))
from sympy import primerange
P=0.
for p in primerange(2,226):
    q=p
    while q<226:
        P+=np.log(p)*q**-.5*conv(np.log(q)); q*=p
print('A^2',A*A,'B',B,'SumLj2',SL,'P',P,'Wrefl[g]',SL+P-A*A, 'E_Lambda=P-A^2',P-A*A)
