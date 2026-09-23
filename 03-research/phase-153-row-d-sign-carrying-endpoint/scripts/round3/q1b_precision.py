import math
from track2_needle import lam_min, LOG3
T=math.log(2)
print("quadrature sensitivity at b=log3, K=160:")
for taumax,npan,ng in [(2000,400,24),(4000,400,24),(8000,400,24),(4000,600,24),(4000,400,32)]:
    print(f"  taumax={taumax} npan={npan} ng={ng}: {lam_min(T,160,LOG3,taumax=float(taumax),npan=npan,ng=ng): .8e}")
print("basis refinement at b=log3:")
for K in (100,160,240,320):
    print(f"  K={K}: {lam_min(T,K,LOG3): .8e}")
print("argmax at T=log2 (golden section, K=160):")
lo,hi=LOG3-0.05,LOG3+0.05
for _ in range(60):
    m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
    if lam_min(T,160,m1)<lam_min(T,160,m2): lo=m1
    else: hi=m2
    if hi-lo<1e-10: break
b=0.5*(lo+hi)
print(f"  b*={b:.10f}  b*-log3={b-LOG3:+.3e}  lam={lam_min(T,160,b): .8e}  lam(log3)={lam_min(T,160,LOG3): .8e}")
