import numpy as np, mpmath as mp, sys, pickle
from cache import get; from wext import Combo
import wext
mu=10; D=get(mu)
for name,coef in [('psi4',{4:mp.mpf(1)}),('core-ish',None)]:
    if coef is None:
        sys.argv=['x','10','core4','20']; 
        import importlib; 
        exec(open('run.py').read().split('res={}')[0].split('D=get(mu)')[1].replace('lam=mp.sqrt(mu)','lam=mp.sqrt(mu)'),globals())
        coef,_=core_coef((0,4,8,12))
    C=Combo(D,coef)
    o,(s,phi,phil)=wext.evaluate(C,V=20,verbose=False)
    idx=[10,len(s)//7,len(s)//3,len(s)//2,len(s)-5]
    for j in idx:
        v=np.exp(s[j]); N=4_000_000; n=np.arange(1,N+1)
        r=C.rho(n*v); b=np.sum(r); bl=np.sum(np.log(n)*r)
        z=np.exp(1j*C.c*v); Nn=N+1; q=N/(N+1)
        tail=np.real(C.b[0]*z**Nn/Nn/(1-z*q))/v; tl=np.real(C.b[0]*z**Nn*np.log(Nn)/Nn/(1-z*q*np.log(Nn+1)/np.log(Nn)))/v
        print(name,'v=%.4f'%v,'pipeline',phi[j]*np.exp(-s[j]/2),'brute',b+tail,' log: ',phil[j]*np.exp(-s[j]/2),bl+tl)
