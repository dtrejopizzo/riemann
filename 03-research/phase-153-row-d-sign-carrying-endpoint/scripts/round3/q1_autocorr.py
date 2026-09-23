import math, numpy as np
from track2_needle import lam_min, autocorr, LOG3, W3
T=math.log(2)
for K in (100,160,240):
    l,v=lam_min(T,K,LOG3,vec=True)
    bs=np.linspace(0.70,2*T-1e-6,60)
    c=autocorr(T,v,K,bs)
    i=int(np.argmin(c))
    # local min of c near log3
    print(f"K={K} lam(log3)={l: .6e}  argmin_b c_F(b) = {bs[i]:.6f} (log3={LOG3:.6f}) c={c[i]: .6e}")
    print("   c_F at log3 =", f"{autocorr(T,v,K,[LOG3])[0]: .6e}", " c_F at log2 =", f"{autocorr(T,v,K,[math.log(2)])[0]: .6e}")
    # slope of lam at log3 (one sided)
    h=1e-5
    lm=lam_min(T,K,LOG3-h); lp=lam_min(T,K,LOG3+h)
    print(f"   one-sided slopes: left {(l-lm)/h: .4f}  right {(lp-l)/h: .4f}")
    print("   c profile:", " ".join(f"{b:.3f}:{x:+.3f}" for b,x in zip(bs[::6],c[::6])))
