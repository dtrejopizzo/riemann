import math, core
print("| T | a | L/a | m=ceil(L/a)+1 | cos(pi/m) | numeric max c_F(a)/||F||^2 (K=400, unconstrained) |")
for T,a in [(math.log(2),math.log(2)),(math.log(2),math.log(3)),(0.5*math.log(3),math.log(2)),
            (0.5*math.log(5),math.log(2)),(0.5*math.log(5),math.log(3)),(0.5*math.log(5),math.log(4)),
            (1.2,math.log(2)),(1.8,math.log(2)),(2.5,math.log(2))]:
    L=2*T; m=math.ceil(L/a)+1
    B=core.Body(T,400,contacts=[],constrained=False)
    import numpy as np, scipy.linalg as sla
    S=core.shift_matrix(T,400,a)
    ev=sla.eigh(S,np.eye(400)*T,eigvals_only=True)
    print(f"| {T:.6f} | {a:.6f} | {L/a:.4f} | {m} | {math.cos(math.pi/m):.10f} | {ev[-1]:.10f} / min {ev[0]:.10f} |")
