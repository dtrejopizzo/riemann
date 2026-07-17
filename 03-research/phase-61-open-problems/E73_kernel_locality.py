"""
P3 - mecanismo real de 2.3.F-Loc, SIN adivinar tapers. Test directo de LOCALIDAD del kernel
Doob-conjugado: ¿el operador G_lambda = u0 (A-eps0) u0 es LOCAL (decae rapido fuera de la
diagonal)?  Y crucialmente: ¿la localidad viene de la CANCELACION ARCH-PRIME?

Tesis: ARCH-solo y PRIME-solo tienen colas off-diagonal LENTAS (no-locales, saltos grandes);
en ARCH-PRIME se CANCELAN -> decaimiento rapido = LOCAL. DH: NO cancelan -> sigue no-local.

Metodo: kernel en posicion K_M(x,y)=Sum_{mn} M_{mn} e^{2pi i m x/L} e^{-2pi i n y/L}/L.
Doob: G(x,y)=u0(x)u0(y) K_{A-eps0}(x,y) (parte off-diagonal, x!=y, sin la delta).
Medida de no-localidad: NL(d) = RMS_{|x-y|>d} |G| / RMS_{all} |G|.  Comparar ARCH, PRIME,
ARCH-PRIME (zeta) y ARCH-PRIME (DH).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
exec(open('E70_doob_parter.py').read().split('# ---- ejecutar')[0])

def kernel_grid(Mmat, idx, L, Ny=240):
    dim=len(idx); ys=np.linspace(0,L,Ny)
    # phi_m(x)=exp(2pi i m x/L); K = E * M * E^H /L  con E[x,m]=phi_m(x)
    Ecos=np.zeros((Ny,dim)); Esin=np.zeros((Ny,dim))
    for j,n in enumerate(idx):
        ph=2*np.pi*n*ys/L; Ecos[:,j]=np.cos(ph); Esin[:,j]=np.sin(ph)
    Mr=np.array([[float(Mmat[a,b]) for b in range(dim)] for a in range(dim)])
    # K(x,y)=Sum_mn M_mn phi_m(x) conj(phi_n(y)); M real simetrica -> tomar parte real
    # phi_m(x)conj(phi_n(y)) real part = cos(m x)cos(n y)+sin(m x)sin(n y) (con signo en n)
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
    # A - eps0 I  (la I en Fourier es identidad)
    Ae=A.copy()
    for i in range(dim): Ae[i,i]=Ae[i,i]-eps0
    parts={'ARCH':Larch,'PRIME':Lpr,'ARCH-PRIME(=A-eps0)':Ae}
    print(f"\n{'='*60}\n{kind} lambda={lam} N={N} L={L:.3f}  eps0={float(eps0):+.3e}")
    print(f"  no-localidad NL(d)=RMS_{{|x-y|>d}}|G|/RMS_all  (cae rapido=LOCAL):")
    res={}
    for name,M in parts.items():
        _,K=kernel_grid(M,idx,L)
        G=W*K  # Doob (off-diagonal; la diagonal/delta no afecta el decaimiento)
        ds,nl=nonlocality(ys,G); res[name]=nl
    hdr="    d=" + " ".join(f"{d:5.2f}" for d in ds)
    print(hdr)
    for name in parts:
        print(f"  {name:>20}: " + " ".join(f"{x:5.2f}" for x in res[name]))
    # cuantificar: a media-caja d=L/3, cuanta cola queda
    i3=np.argmin(np.abs(ds-L/3))
    print(f"  --> cola a d=L/3={L/3:.2f}:  ARCH={res['ARCH'][i3]:.2f}  PRIME={res['PRIME'][i3]:.2f}  ARCH-PRIME={res['ARCH-PRIME(=A-eps0)'][i3]:.2f}")
    print(f"      {'CANCELACION -> LOCAL' if res['ARCH-PRIME(=A-eps0)'][i3] < 0.6*min(res['ARCH'][i3],res['PRIME'][i3]) else 'sin ganancia de localidad por cancelacion'}")
    return ds,res

for lam,N in [(7.0,14),(11.0,18)]:
    run73(lam,N,'zeta')
run73(7.0,14,'DH')
