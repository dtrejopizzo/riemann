import math, numpy as np, scipy.linalg as sla
from track2_needle import blocks, lam_min, LOG3, W2, W3, autocorr
T=math.log(2); K=160
tau,ww,H,March,M2=blocks(T,K)
C_=None
from aud_spectral import moments
Z=sla.null_space(moments(T,K,[-0.5,0.5]))
G=np.eye(K)*T; B=Z.T@G@Z
def spec(b,n=3):
    M3=np.real((H*(ww*2*np.cos(tau*b)))@H.conj().T)
    M=2*(March-W2*M2-W3*M3)/(2*math.pi); M=0.5*(M+M.T)
    w,V=sla.eigh(Z.T@M@Z,B)
    return w[:n], Z@V[:,:n]
b0=1.0986265908
print("two lowest eigenvalues near b*:")
prev=None
for d in (-3e-5,-1e-5,-1e-6,-1e-7,-1e-8,0,1e-8,1e-7,1e-6,1e-5,3e-5):
    w,V=spec(b0+d)
    ov="" if prev is None else f" overlap_with_prev={abs(V[:,0]@ (G@prev))/math.sqrt((V[:,0]@G@V[:,0])*(prev@G@prev)):.6f}"
    print(f"  d={d:+.0e}  lam1={w[0]: .8e}  lam2={w[1]: .8e}  gap={w[1]-w[0]:.3e}{ov}")
    prev=V[:,0].copy()
w,V=spec(b0)
c=autocorr(T,V[:,0],K,[b0]); 
print("c_F1(b*) =",c[0])
# derivative of c for minimiser at b*-1e-5 and b*+1e-5
for d in (-1e-5,1e-5):
    w,V=spec(b0+d); b=b0+d; h=1e-4
    cm=autocorr(T,V[:,0],K,[b-h,b+h]); print(f"  minimiser at d={d:+.0e}: c'={(cm[1]-cm[0])/(2*h): .6f}  -> -2w3 c' = {-2*W3*(cm[1]-cm[0])/(2*h): .6f}")
