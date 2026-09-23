import math, numpy as np, core
T=math.log(2)
for K in (80,160,240,320,480):
    B=core.Body(T,K)
    un={n:-2*core.wgt(n) for n in B.contacts}
    lam=B.lmin(1.0,un)
    print(f"K={K:4d}  lmin(A_log2)={lam: .6e}   x0range_min={B.lmin(1.0,{}): .6f}  x2max={B.support(0.0,{2:1.0,3:0.0}): .8f}  x3max={B.support(0.0,{2:0.0,3:1.0}): .8f}")
