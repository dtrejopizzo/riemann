"""Eigenvalues of the sinc kernel sin(c(x-y))/(pi(x-y)) on [-1,1] (Gauss-Legendre Nystrom, 400 nodes); zero of Phi."""
import numpy as np, mpmath as mp
from numpy.polynomial.legendre import leggauss
x,w=leggauss(400); D=x[:,None]-x[None,:]; s=np.sqrt(w)
for c in [5,10,20,40]:
    K=np.where(D==0,c/np.pi,np.sin(c*D)/(np.pi*np.where(D==0,1,D)))
    e=np.sort(np.linalg.eigvalsh(s[:,None]*K*s[None,:]))[::-1]
    print("c=%d  1-lambda_max=%.3e  #{lambda>0.999}=%d"%(c,1-e[0],(e>0.999).sum()))
print("Phi(r)=0 at r =",mp.findroot(lambda r: mp.re(mp.digamma(0.25+0.5j*r))-mp.log(mp.pi),6))
