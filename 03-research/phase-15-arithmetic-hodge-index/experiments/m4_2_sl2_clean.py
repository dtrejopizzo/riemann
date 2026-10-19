import numpy as np
# Continuum sl2 on L^2(R,dr):  L=T_c, H=(2/c)*mult_r, Lambda=T_{-c}*m(r), m=-r^2/c^2+r/c
N=6000; h=0.01; c=1.0                 # shift by c/h=100 grid points (exact translation)
shift=int(round(c/h))
r=(np.arange(N)-N//2)*h
Tcont=np.diag(r)
Tc =np.zeros((N,N)); Tc[shift:,:-shift]=np.eye(N-shift)    # (T_c f)_j=f_{j-shift}
Tmc=np.zeros((N,N)); Tmc[:-shift,shift:]=np.eye(N-shift)   # (T_-c f)_j=f_{j+shift}
m=-(r**2)/c**2+r/c
H=(2.0/c)*Tcont; L=Tc; Lam=Tmc@np.diag(m)
comm=lambda A,B:A@B-B@A
s=slice(shift+20,N-shift-20)
e=lambda M:float(np.max(np.abs(M[s,s])))
print("max abs error on interior block:")
print(f"  [T_cont,L]-cL   : {e(comm(Tcont,L)-c*L):.2e}")
print(f"  [H,L]-2L        : {e(comm(H,L)-2*L):.2e}")
print(f"  [H,Lam]+2Lam    : {e(comm(H,Lam)+2*Lam):.2e}")
print(f"  [L,Lam]-H       : {e(comm(L,Lam)-H):.2e}")
print(f"  L off-diagonal (not in W*(T_cont)): {float(np.max(np.abs(L-np.diag(np.diag(L))))):.1f}")
