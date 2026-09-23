import math, numpy as np
from track2_needle import lam_min, LOG3
T=math.log(2)
def tip(T,K,c,half=0.05,tol=1e-11):
    lo,hi=c-half,c+half
    for _ in range(80):
        m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
        if lam_min(T,K,m1)<lam_min(T,K,m2): lo=m1
        else: hi=m2
        if hi-lo<tol: break
    b=0.5*(lo+hi); return b,lam_min(T,K,b)
for K in (100,160,240,320):
    b,l=tip(T,K,LOG3)
    print(f"K={K:4d}  b*={b:.10f}  b*-log3={b-LOG3:+.4e}  lam_max={l: .6e}  lam(log3)={lam_min(T,K,LOG3): .6e}")
print()
print("fine profile around b* (K=160):")
b0,_=tip(T,160,LOG3)
for d in [0]+[s*10**e for e in (-7,-6.5,-6,-5.5,-5,-4.5,-4,-3.5,-3,-2.5,-2) for s in (1,-1)]:
    b=b0+d
    print(f"  b-b*={d:+.3e}  b-log3={b-LOG3:+.3e}  lam={lam_min(T,160,b): .6e}")
