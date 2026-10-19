"""
P3 - real mechanism of 2.3.F-Loc, WITHOUT guessing tapers. Direct LOCALITY test of the
Doob-conjugated kernel: is the operator G_lambda = u0 (A-eps0) u0 LOCAL (decays fast away
from the diagonal)?  And crucially: does the locality come from ARCH-PRIME CANCELLATION?

Thesis: ARCH-only and PRIME-only have SLOW off-diagonal tails (non-local, large jumps);
in ARCH-PRIME they CANCEL -> fast decay = LOCAL. DH: they do NOT cancel -> remains non-local.

Method: position-space kernel K_M(x,y)=Sum_{mn} M_{mn} e^{2pi i m x/L} e^{-2pi i n y/L}/L.
Doob: G(x,y)=u0(x)u0(y) K_{A-eps0}(x,y) (off-diagonal part, x!=y, without the delta).
Non-locality measure: NL(d) = RMS_{|x-y|>d} |G| / RMS_{all} |G|.  Compare ARCH, PRIME,
ARCH-PRIME (zeta) and ARCH-PRIME (DH).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
exec(open('E70_doob_parter.py').read().split('# ---- run')[0])

def kernel_grid(Mmat, idx, L, Ny=240):
    dim=len(idx); ys=np.linspace(0,L,Ny)
    # phi_m(x)=exp(2pi i m x/L); K = E * M * E^H /L  with E[x,m]=phi_m(x)
    Ecos=np.zeros((Ny,dim)); Esin=np.zeros((Ny,dim))
    for j,n in enumerate(idx):
        ph=2*np.pi*n*ys/L; Ecos[:,j]=np.cos(ph); Esin[:,j]=np.sin(ph)
    Mr=np.array([[float(Mmat[a,b]) for b in range(dim)] for a in range(dim)])
    # K(x,y)=Sum_mn M_mn phi_m(x) conj(phi_n(y)); M real symmetric -> take the real part
    # phi_m(x)conj(phi_n(y)) real part = cos(m x)cos(n y)+sin(m x)sin(n y) (with sign in n)
    Kr = Ecos@Mr@Ecos.T + Esin@Mr@Esin.T
    return ys, Kr/L

def nonlocality(ys, G):
    Ny=len(ys); X=np.abs(ys[:,None]-ys[None,:])
    Gabs=np.abs(G); allrms=np.sqrt(np.mean(Gabs**2))
    ds=np.linspace(0,ys[-1]*0.6,7); out=[]
    for d in ds:
        mask=X>d
        out.append(np.sqrt(np.mean(Gabs[mask]**2))/allrms if mask.any() else 0)
    return ds,out

def run73(lam,N,kind='zeta'):
    A,Larch,Lpr,L,idx=build(lam,N,kind)
    dim=len(idx)
    E,V=mp.eigsy(A); order=sorted(range(dim),key=lambda j:E[j])
    eps0=E[order[0]]
    c0=np.array([float(V[i,order[0]]) for i in range(dim)])
    ys,u0=recon_grid(c0,idx,L,Ny=240)
    if u0[len(u0)//2]<0: u0=-u0
    W=np.outer(u0,u0)
    # A - eps0 I  (I in Fourier space is the identity)
    Ae=A.copy()
    for i in range(dim): Ae[i,i]=Ae[i,i]-eps0
    parts={'ARCH':Larch,'PRIME':Lpr,'ARCH-PRIME(=A-eps0)':Ae}
    print(f"\n{'='*60}\n{kind} lambda={lam} N={N} L={L:.3f}  eps0={float(eps0):+.3e}")
    print(f"  non-locality NL(d)=RMS_{{|x-y|>d}}|G|/RMS_all  (fast drop=LOCAL):")
    res={}
    for name,M in parts.items():
        _,K=kernel_grid(M,idx,L)
        G=W*K  # Doob (off-diagonal part; the diagonal/delta does not affect the decay)
        ds,nl=nonlocality(ys,G); res[name]=nl
    hdr="    d=" + " ".join(f"{d:5.2f}" for d in ds)
    print(hdr)
    for name in parts:
        print(f"  {name:>20}: " + " ".join(f"{x:5.2f}" for x in res[name]))
    # quantify: at half-box d=L/3, how much tail remains
    i3=np.argmin(np.abs(ds-L/3))
    print(f"  --> tail at d=L/3={L/3:.2f}:  ARCH={res['ARCH'][i3]:.2f}  PRIME={res['PRIME'][i3]:.2f}  ARCH-PRIME={res['ARCH-PRIME(=A-eps0)'][i3]:.2f}")
    print(f"      {'CANCELLATION -> LOCAL' if res['ARCH-PRIME(=A-eps0)'][i3] < 0.6*min(res['ARCH'][i3],res['PRIME'][i3]) else 'no locality gain from cancellation'}")
    return ds,res

for lam,N in [(7.0,14),(11.0,18)]:
    run73(lam,N,'zeta')
run73(7.0,14,'DH')
