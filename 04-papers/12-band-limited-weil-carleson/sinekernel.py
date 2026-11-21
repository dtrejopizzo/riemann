"""Subdominant spectrum at d=1.3, T0=80 and comparison with the sine kernel (Section 4)."""
import numpy as np, mpmath as mp
from scipy.linalg import eigh
from carleson_engine import engine
d,T0,N=1.3,80.0,29
A,P=engine(d,T0,N=N,R=79.0,M=200001)
rj=T0+(np.arange(N)-(N-1)/2)*np.pi/d
lo,hi=rj[0],rj[-1]
g=[];k=1
while True:
    z=float(mp.zetazero(k).imag); k+=1
    if z>hi+20: break
    g.append(z)
g=np.array(g); win=g[(g>=lo)&(g<=hi)]; K=len(win)
M=A-P
ev=np.sort(np.linalg.eigvalsh(M))[::-1]
print("window",lo,hi,"K",K); print("eig",np.round(ev,4))
ew=np.sort(eigh(M,A,eigvals_only=True))[::-1]; print("gen eig of (A-P,A)",np.round(ew,4))
S=lambda x: np.sinc(d*(x-rj)/np.pi)
V=np.array([S(x) for x in win])
G=V@np.linalg.solve(A,V.T); Dn=np.sqrt(np.diag(G)); Gn=G/np.outer(Dn,Dn)
D=win[:,None]-win[None,:]
Ks=np.where(D==0,1.0,np.sin(d*D)/(d*np.where(D==0,1,D)))
print("sine-kernel max dev",np.abs(Gn-Ks).max())
print("lambda_min(A_Phi)",np.linalg.eigvalsh(A).min())
