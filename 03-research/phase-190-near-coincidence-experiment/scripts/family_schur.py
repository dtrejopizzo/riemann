"""CA_C_007: scalar Schur complement s_M = Q(u) - b^T Qt^{-1} b of the eta-family (tail block positive), Z vs jit."""
import sys, numpy as np, scipy.linalg as sl
from family_split import system, P
from am import AM
eta=float(sys.argv[1])
for lat in sys.argv[2].split(','):
  for M in [int(t) for t in sys.argv[3].split(',')]:
    ints,pos,w=system(lat,M); x=np.log(ints); n=len(ints); A=AM(P,x,pos,w).A; G=P.c0(np.abs(x[:,None]-x[None,:]))
    k=np.searchsorted(ints,eta*M,side='right'); u=np.zeros(n); u[:k]=ints[:k]**-0.5
    Qu=u@A@u; b=(A@u)[k:]; At=A[k:,k:]; Gu=u@G@u
    lam_t=np.linalg.eigvalsh(At)[0]
    sM=Qu-b@np.linalg.solve(At,b)
    print(f"{lat:4s} M={M} Q(u)/M={Qu/M:.4f} |F_u|^2/M={Gu/M:.4f} s_M={sM:.4e} s_M/Q(u)={sM/Qu:.4e} tail l2-min={lam_t:.2e}",flush=True)
