import json,math,numpy as np
from sigma_g import p,lam
xs,ws=np.polynomial.legendre.leggauss(4000)
# split [1/λ,λ] in 12 panels × 4000 GL
edges=np.linspace(1/lam,lam,13); V=[];W=[]
for a,b in zip(edges[:-1],edges[1:]): V.append((a+b)/2+(b-a)/2*xs); W.append((b-a)/2*ws)
V=np.concatenate(V); W=np.concatenate(W); PW=2*W*p(V)
def sig(om):
    out=np.empty(len(om))
    for i in range(0,len(om),500): out[i:i+500]=np.cos(2*math.pi*lam*np.outer(om[i:i+500],V))@PW
    return out
om=np.round(np.arange(1/15,240+1e-9,0.002),6); S=sig(om)
np.save('sigma_tilde.npy',np.vstack([om,S]))
print('max|p|',np.abs(p(V)).max(),'sigma(0)',sig(np.array([0.0]))[0])
for w in [0.1,0.3,0.5,0.9,1.0,1.5,2,5,10,48,100,240]: print(w,sig(np.array([w]))[0])
