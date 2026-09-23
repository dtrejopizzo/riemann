import math, numpy as np, scipy.linalg as sla, core
T=0.5*math.log(5); L=2*T
w={n:core.wgt(n) for n in (2,3,4)}
print("T=0.5log5 =",T," contacts 2,3,4  w=",w)
for K in (240,320,480):
    B=core.Body(T,K,contacts=[2,3,4])
    un={n:-2*w[n] for n in (2,3,4)}
    M=B.op(1.0,un); ev,V=sla.eigh(M,B.G)
    print(f"K={K:4d} lmin(A)={ev[0]: .6e}  next={ev[1]: .5e},{ev[2]: .5e}")
    print(f"      axis: x2 in [{B.lmin(0.,{2:1.,3:0.,4:0.}):.8f},{B.support(0.,{2:1.,3:0.,4:0.}):.8f}]"
          f" x3 in [{B.lmin(0.,{2:0.,3:1.,4:0.}):.8f},{B.support(0.,{2:0.,3:1.,4:0.}):.8f}]"
          f" x4 in [{B.lmin(0.,{2:0.,3:0.,4:1.}):.8f},{B.support(0.,{2:0.,3:0.,4:1.}):.8f}]  x0min={B.lmin(1.,{}):.8f}")
    c=V[:,0]; c=c/math.sqrt(c@B.G@c)
    print(f"      x(Fmin)=({c@B.M0@c: .6f},{c@B.Mn[2]@c: .6f},{c@B.Mn[3]@c: .6f},{c@B.Mn[4]@c: .6f})")
print("cos(pi/m) prediction: a=log2 L/a=%.4f m=%d -> %.8f"%(L/math.log(2),math.ceil(L/math.log(2))+1,math.cos(math.pi/(math.ceil(L/math.log(2))+1))))
print("                      a=log3 L/a=%.4f m=%d -> %.8f"%(L/math.log(3),math.ceil(L/math.log(3))+1,math.cos(math.pi/(math.ceil(L/math.log(3))+1))))
print("                      a=log4 L/a=%.4f m=%d -> %.8f"%(L/math.log(4),math.ceil(L/math.log(4))+1,math.cos(math.pi/(math.ceil(L/math.log(4))+1))))
B=core.Body(T,480,contacts=[2,3,4])
print("BOX bound:",B.lmin(1.,{})-sum(2*w[n]*0.5 for n in (2,3,4)) )
print("band in w4 (w2,w3 fixed): ", end="")
from scipy.optimize import minimize_scalar
r=minimize_scalar(lambda v:-B.lmin(1.,{2:-2*w[2],3:-2*w[3],4:-2*v}),bounds=(0.0,1.0),method='bounded',options={'xatol':1e-11})
print(f"max lmin={-r.fun:.5e} at v4={r.x:.6f}; w4={w[4]:.6f}; lmin at w4={B.lmin(1.,{2:-2*w[2],3:-2*w[3],4:-2*w[4]}):.5e}")
