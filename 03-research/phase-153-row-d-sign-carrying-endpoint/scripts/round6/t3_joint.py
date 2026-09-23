import math, numpy as np, core
from scipy.optimize import brentq
T=math.log(2); w2,w3=core.wgt(2),core.wgt(3); B=core.Body(T,320)
def f(v2,v3): return B.lmin(1.0,{2:-2*v2,3:-2*v3})
print("joint admissible region {(v2,v3): A>=0} at T=log2, K=320")
print("| v2 | v3^- | v3^+ | width |")
for v2 in [0.0,0.1,0.2,0.3,0.4,0.45,0.48,0.49,w2,0.4902,0.495,0.50,0.52]:
    g=lambda v: f(v2,v)
    from scipy.optimize import minimize_scalar
    r=minimize_scalar(lambda v:-g(v),bounds=(0.0,1.6),method='bounded',options={'xatol':1e-11})
    if -r.fun<0: print(f"| {v2:.6f} | EMPTY (max lmin={-r.fun:.3e} at v3={r.x:.5f}) |"); continue
    a=brentq(g,0.0,r.x,xtol=1e-13) if g(0.0)<0 else 0.0
    b=brentq(g,r.x,1.6,xtol=1e-13) if g(1.6)<0 else 1.6
    print(f"| {v2:.6f} | {a:.8f} | {b:.8f} | {b-a:.3e} |")
print("\nGamma coercivity: min x0 =",B.lmin(1.0,{}) , " max x0 over grid dir: +inf (unbounded multiplier)")
print("axis: max x2=",B.support(0.0,{2:1.0,3:0.0})," min x2=",B.lmin(0.0,{2:1.0,3:0.0}))
print("axis: max x3=",B.support(0.0,{2:0.0,3:1.0})," min x3=",B.lmin(0.0,{2:0.0,3:1.0}))
print("\nBOX bound in direction w_zeta: ",B.lmin(1.0,{})-2*w2*0.5-2*w3*0.5, " true:",f(w2,w3))
# 2-body (pair) bounds: relax one coordinate only
print("pair bound (x0,x2 joint; x3 free at 0.5):", B.lmin(1.0,{2:-2*w2}) - 2*w3*0.5)
print("pair bound (x0,x3 joint; x2 free at 0.5):", B.lmin(1.0,{3:-2*w3}) - 2*w2*0.5)
print("pair bound (x2,x3 joint; x0 free at min):", B.lmin(1.0,{})+B.lmin(0.0,{2:-2*w2,3:-2*w3}))
