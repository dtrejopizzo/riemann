import math,numpy as np,core,rate
Ts=[0.30,0.34,0.3466,0.38,0.42,0.46,0.50,0.54,0.5493,0.58,0.62,0.65,0.68,math.log(2)]
print("| T | lam K=160 | lam K=240 | lam K=320 | Richardson | parity | c_HF |")
for T in Ts:
    v=[core.lam_min(T,K)[0] for K in (160,240,320)]
    rich=v[2]+3*(v[2]-v[1])
    lam,par,tm=rate.rate(T,320); c=-sum(tm.values())/lam
    print(f"| {T:.4f} | {v[0]:.5e} | {v[1]:.5e} | {v[2]:.5e} | {rich:.5e} | {par} | {c:.2f} |")
