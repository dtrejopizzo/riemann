import math, numpy as np, scipy.linalg as sla, core
T=math.log(2)
for K in (240,320,480):
    B=core.Body(T,K)
    w2,w3=core.wgt(2),core.wgt(3)
    un={2:-2*w2,3:-2*w3}
    M=B.op(1.0,un)
    ev,V=sla.eigh(M,B.G)
    print("K=",K,"lowest 6 eigs of A_T:",np.array2string(ev[:6],precision=8))
    # coordinates of the minimiser
    for i in range(3):
        c=V[:,i]; c=c/math.sqrt(c@B.G@c)
        x0=c@B.M0@c; x2=c@B.Mn[2]@c; x3=c@B.Mn[3]@c
        F=B.Z@c
        # parity: phi_k(-t) = (-1)^{k+1} phi_k(t)
        sg=np.array([(-1)**(k+1) for k in range(1,K+1)])
        par = 'even' if abs(np.linalg.norm(F-sg*F))<abs(np.linalg.norm(F+sg*F)) else 'odd'
        print(f"   eig{i} {ev[i]: .6e} {par:4s} x=({x0: .8f},{x2: .8f},{x3: .8f})  check={x0-2*w2*x2-2*w3*x3: .6e}")
print("w2=",core.wgt(2),"w3=",core.wgt(3))
