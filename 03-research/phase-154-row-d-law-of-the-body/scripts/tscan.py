"""R154 script 4: (B2) is there a kink of lambda(T) at the interior 3-smooth breakpoints
   T = 1/2 log(27/8) = 0.6082, 1/2 log(32/9) = 0.6343, between 1/2log3 and log2?
   Contacts held fixed at {2,3}. Also dlambda/dT vs the proved bound R'(T) = -(1/sinh T + 1/cosh T).
"""
import math, sys, numpy as np
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core
Kd=200
h=0.002
base=[0.6082,0.6343,0.5900]  # two 3-smooth breakpoints and a control point
print("central second differences of lambda(T), h=%.4f, K=%d"%(h,Kd))
for T0 in base:
    vals=[]
    for j in (-2,-1,0,1,2):
        T=T0+j*h
        B=core.Body(T,Kd,contacts=[2,3],npan=300)
        vals.append(B.lmin(1.0,{2:-2*core.wgt(2),3:-2*core.wgt(3)}))
    v=np.array(vals)
    d1=(v[3]-v[1])/(2*h); d2=(v[3]-2*v[2]+v[1])/h**2
    d2w=(v[4]-2*v[2]+v[0])/(2*h)**2
    print(f" T0={T0:.4f} lam={v[2]: .6e} dlam/dT={d1: .5f} d2(h)={d2: .4f} d2(2h)={d2w: .4f}  R'(T)={-(1/math.sinh(T0)+1/math.cosh(T0)): .5f}")
