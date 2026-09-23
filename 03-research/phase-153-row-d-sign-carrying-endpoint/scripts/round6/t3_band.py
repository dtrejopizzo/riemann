import math, numpy as np, core
from scipy.optimize import brentq

def band(B, fixed, var, lo, hi, u0=1.0):
    """interval of `var`-weight v (as coefficient -2v on S_var) with lmin>=0."""
    def f(v):
        un={n:-2*c for n,c in fixed.items()}; un[var]=-2*v
        return B.lmin(u0, un)
    # find interior point = argmax
    from scipy.optimize import minimize_scalar
    r=minimize_scalar(lambda v:-f(v), bounds=(lo,hi), method='bounded',
                      options={'xatol':1e-10})
    vstar=r.x; fmax=-r.fun
    if fmax<0: return None,None,vstar,fmax
    a=brentq(f,lo,vstar,xtol=1e-12) if f(lo)<0 else lo
    b=brentq(f,vstar,hi,xtol=1e-12) if f(hi)<0 else hi
    return a,b,vstar,fmax

T=math.log(2); w2,w3=core.wgt(2),core.wgt(3)
print("== T = log 2, band in w_3 (w_2 fixed at Lambda(2)/sqrt2) ==")
for K in (240,320,480):
    B=core.Body(T,K)
    a,b,vs,fm=band(B,{2:w2},3,0.0,1.5)
    print(f"K={K:4d} band=[{a:.10f},{b:.10f}] width={b-a:.3e}  argmax={vs:.8f} lmax={fm:.5e}"
          f"  w3-a={w3-a:.3e} b-w3={b-w3:.3e}")
print("\n== T = log 2, band in w_2 (w_3 fixed) ==")
B=core.Body(T,480)
a,b,vs,fm=band(B,{3:w3},2,0.0,1.5)
print(f" band=[{a:.10f},{b:.10f}] width={b-a:.3e} argmax={vs:.8f}  w2={w2:.8f} w2-a={w2-a:.3e} b-w2={b-w2:.3e}")

print("\n== T = 0.5 log 3, band in w_2 (only contact) ==")
T2=0.5*math.log(3)
for K in (240,480):
    B2=core.Body(T2,K)
    a,b,vs,fm=band(B2,{},2,0.0,3.0)
    print(f"K={K:4d} band=[{a:.8f},{b:.8f}] argmax={vs:.6f} lmax={fm:.5e}  w2={w2:.6f} margin_to_upper={b-w2:.5f}")
