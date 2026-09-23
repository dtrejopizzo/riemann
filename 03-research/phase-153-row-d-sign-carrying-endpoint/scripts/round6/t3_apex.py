import math, numpy as np, core
from scipy.optimize import minimize_scalar
T=math.log(2); w2,w3=core.wgt(2),core.wgt(3)
for K in (240,320,480):
  B=core.Body(T,K)
  def M(v2):
    r=minimize_scalar(lambda v:-B.lmin(1.0,{2:-2*v2,3:-2*v}),bounds=(0.55,0.72),
                      method='bounded',options={'xatol':1e-12})
    return -r.fun, r.x
  from scipy.optimize import brentq
  va=brentq(lambda v2:M(v2)[0],w2,0.4903,xtol=1e-12)
  fm,v3a=M(va)
  print(f"K={K} apex v2*={va:.9f} (w2={w2:.9f}, v2*-w2={va-w2:.3e}, rel {(va-w2)/w2:.3e})  v3 at apex={v3a:.8f} (w3={w3:.8f}, diff={v3a-w3:.3e})")
