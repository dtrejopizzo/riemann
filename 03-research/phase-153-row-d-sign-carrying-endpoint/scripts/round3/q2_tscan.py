"""T-scan: does the needle tip b*(T) follow log 3 (arithmetic) or f(T) (analytic)?
Parity-resolved: the form commutes with t -> -t, so lam_min = min(lam_even, lam_odd)."""
import math, sys, numpy as np, scipy.linalg as sla
from track2_needle import blocks, LOG3, W2, W3
from aud_spectral import moments
def parity_spec(T,K,b):
    tau,ww,H,March,M2=blocks(T,K)
    M3=np.real((H*(ww*2*np.cos(tau*b)))@H.conj().T)
    M=2*(March-W2*M2-W3*M3)/(2*math.pi); M=0.5*(M+M.T)
    Z=sla.null_space(moments(T,K,[-0.5,0.5])); G=np.eye(K)*T
    # sine basis sin(k pi (t+T)/2T): parity (-1)^(k+1) -> k odd = even function
    ie=[k-1 for k in range(1,K+1) if k%2==1]; io=[k-1 for k in range(1,K+1) if k%2==0]
    out=[]
    for idx in (ie,io):
        Ms=M[np.ix_(idx,idx)]; Gs=G[np.ix_(idx,idx)]
        Cs=moments(T,K,[-0.5,0.5])[:,idx]
        # only one independent constraint per parity block
        Zs=sla.null_space(Cs)
        out.append(sla.eigh(Zs.T@Ms@Zs,Zs.T@Gs@Zs,eigvals_only=True)[0])
    return out  # [even, odd]
def lmin(T,K,b): 
    e,o=parity_spec(T,K,b); return min(e,o)
def tip(T,K,lo,hi):
    for _ in range(90):
        m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
        if lmin(T,K,m1)<lmin(T,K,m2): lo=m1
        else: hi=m2
        if hi-lo<1e-11: break
    b=0.5*(lo+hi); return b,lmin(T,K,b)
if __name__=="__main__":
    K=int(sys.argv[1]) if len(sys.argv)>1 else 160
    for T in (0.66,0.68,math.log(2),0.70,0.72):
        bs=np.linspace(math.log(2)+2e-3,2*T-2e-3,30)
        ev=np.array([parity_spec(T,K,b) for b in bs])
        vals=ev.min(axis=1); i=int(np.argmax(vals))
        b1,b2=bs[max(i-1,0)],bs[min(i+1,len(bs)-1)]
        bst,lst=tip(T,K,b1,b2)
        e,o=parity_spec(T,K,LOG3)
        print(f"T={T:.6f} (2T={2*T:.4f}) K={K}")
        print(f"   tip b*={bst:.9f}  b*-log3={bst-LOG3:+.4e}  lam(b*)={lst: .6e}")
        print(f"   at b=log3: even={e: .6e} odd={o: .6e} min={min(e,o): .6e}")
        print("   coarse (even,odd):", " ".join(f"{b:.3f}:[{x[0]:+.1e},{x[1]:+.1e}]" for b,x in list(zip(bs,ev))[::4]))
