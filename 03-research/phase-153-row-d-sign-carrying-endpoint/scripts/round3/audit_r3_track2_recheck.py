import math,sys,numpy as np,scipy.linalg as sla
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round3')
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/audit')
from track2_needle import blocks,LOG3,W2,W3
from aud_spectral import moments
def spec(T,K,b,n=3,**kw):
    tau,ww,H,March,M2=blocks(T,K,**kw)
    M3=np.real((H*(ww*2*np.cos(tau*b)))@H.conj().T)
    M=2*(March-W2*M2-W3*M3)/(2*math.pi); M=0.5*(M+M.T)
    Z=sla.null_space(moments(T,K,[-0.5,0.5])); G=np.eye(K)*T
    w,V=sla.eigh(Z.T@M@Z,Z.T@G@Z)
    return w[:n]
def tip(T,K,lo,hi,**kw):
    for _ in range(100):
        m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
        if spec(T,K,m1,1,**kw)[0]<spec(T,K,m2,1,**kw)[0]: lo=m1
        else: hi=m2
        if hi-lo<1e-12: break
    b=0.5*(lo+hi); return b,spec(T,K,b,1,**kw)[0]
T=math.log(2)
print("=== (f) tip and crossing, independent golden section")
for K in (160,240):
    b,l=tip(T,K,LOG3-0.02,LOG3+0.02)
    w=spec(T,K,b,3)
    print("  K=%d  b*-log3=%+.4e  lam(b*)=%.6e  gap12=%.3e  lam3=%.3e  lam(log3)=%.6e"%(
        K,b-LOG3,l,w[1]-w[0],w[2],spec(T,K,LOG3,1)[0]))
    # quadrature sensitivity of the displacement
    b2,_=tip(T,K,LOG3-0.02,LOG3+0.02,taumax=8000.,npan=600,ng=32)
    print("     quad-varied: b*-log3=%+.4e  (shift %.2e)"%(b2-LOG3,b2-b))
print("=== (g) T-scan, independent")
for Tv in (0.68,0.70,0.704,0.706):
    b,l=tip(Tv,240,LOG3-3e-3,LOG3+3e-3)
    print("  T=%.4f  b*-log3=%+.4e  lam(b*)=%+.6e"%(Tv,b-LOG3,l))
