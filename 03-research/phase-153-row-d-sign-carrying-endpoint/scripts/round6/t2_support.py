import math, numpy as np, core
T=math.log(2); B=core.Body(T,320); w2,w3=core.wgt(2),core.wgt(3)
x0m=B.lmin(1.,{})
print("Support function h_W(u), u=(-1,v2,v3):  h = -lmin(M0 - v2 S2 - v3 S3)")
print("| v2 | v3 | h_W(u) | box bound -x0min+.5(|v2|+|v3|) | coupling gap |")
rows=[(0,0),(0.5,0),(0,0.5),(0.5,0.5),(1,0),(0,1),(1,1),(-1,1),(1,-1),(-1,-1),
      (2*w2,0),(0,2*w3),(2*w2,2*w3),(-2*w2,-2*w3),(2,2),(5,5)]
for v2,v3 in rows:
    h=-B.lmin(1.,{2:-v2,3:-v3})
    box=-x0m+0.5*(abs(v2)+abs(v3))
    print(f"| {v2:+.5f} | {v3:+.5f} | {h:+.8f} | {box:+.8f} | {box-h:.8f} |")
print("\nx0 min (Gamma coercivity) =",x0m,"  h_W(0,+-e_n)=0.5 exactly (cos(pi/3))")
print("recession: h_W(u0>0,.)=+inf since Re psi(1/4+i tau/2) ~ log|tau| unbounded")
