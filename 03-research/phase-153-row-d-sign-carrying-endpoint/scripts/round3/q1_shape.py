import math, numpy as np
from track2_needle import lam_min, LOG3
T=math.log(2)
for K in (100,160,240):
    print("K=",K)
    for d in (-1e-2,-1e-3,-1e-4,-1e-5,-1e-6,-1e-7,0.0,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2):
        print(f"   delta={d:+.0e}  lam={lam_min(T,K,LOG3+d): .10e}")
