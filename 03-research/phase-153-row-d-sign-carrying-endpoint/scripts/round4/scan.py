import math, sys, numpy as np, core
Ts=[0.30,0.32,0.3466,0.36,0.40,0.44,0.48,0.52,0.5493,0.56,0.58,0.60,0.62,0.64,0.66,0.68,math.log(2)]
Ks=[int(x) for x in (sys.argv[1:] or ['160'])]
print("T        "+"".join(f"  lam(K={K})        par" for K in Ks))
for T in Ts:
    row=[]
    for K in Ks:
        l,p,_=core.lam_min(T,K); row.append((l,p))
    print(f"{T:.4f}  "+"  ".join(f"{l: .8e} {p[:2]}" for l,p in row)); sys.stdout.flush()
