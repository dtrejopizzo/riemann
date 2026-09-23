"""Boundary exponent of the minimiser: |F_T(-T+h)| ~ h^alpha, and the jump test
c_k * k * pi/4 -> F(+-T) for the even block."""
import math,numpy as np,core
for K in (160,240,320):
  for T in (0.60,math.log(2)):
    lam,par,vec=core.lam_min(T,K,want_vec=True); vec/=math.sqrt(T*np.dot(vec,vec))
    if vec[0]<0: vec=-vec
    L=2*T
    F=lambda t: sum(vec[k-1]*np.sin(k*math.pi*(np.asarray(t)+T)/L) for k in range(1,K+1))
    hs=np.array([0.20,0.15,0.12,0.10,0.08,0.06,0.05,0.04]); v=np.abs(F(-T+hs))
    a=np.polyfit(np.log(hs),np.log(v),1)[0]
    loc=[round(math.log(v[i]/v[i+1])/math.log(hs[i]/hs[i+1]),3) for i in range(len(hs)-1)]
    jump=[round(vec[k-1]*k*math.pi/4,5) for k in range(K//3|1,K,50)]
    print(f'K={K} T={T:.4f} alpha={a:.3f} local={loc} F(0)={F(0.0):.4f} jump est={jump}')
