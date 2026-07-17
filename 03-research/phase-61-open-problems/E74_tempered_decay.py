"""
P3 paso 1+2 - DERIVACION honesta del multiplicador C_lambda via Lema 1.1 + Doob ground-state.
Kernel = D_zeta(|x-y|), singularidades-primo delta en u=log n peso Lambda(n)/√n.
Doob por u0 da forma de saltos POSITIVA; multiplicador local:
   C(x) ∝ (1/u0(x)) Sum_n Lambda(n)/√n (log n)^2 * ½(u0e(x+log n)+u0e(x-log n))
con u0e = u0 extendido por CERO fuera de [0,L] (band-limit; f soportada en [0,L]).
El tempering REAL es u0(x±log n)/u0(x) (no (1-s/L) de E72).
Test: comparar perfil C(x)/mean con el C(y) REAL medido en E70:
   E70: bump central centro/borde~1.51, std/mean 0.222(λ7)->0.146(λ9)->0.137(λ11) DECRECE.
Si reproduce perfil Y tendencia con λ => C derivado (pasos 1+2 cerrados, falta solo λ-unif=paso3).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
exec(open('E70_doob_parter.py').read().split('# ---- ejecutar')[0])

def primes_jumps(mx):
    sv=[True]*(mx+1); out=[]
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pm=p; me=1
            while pm<=mx:
                out.append((float(me*lp), float(lp*(mp.mpf(pm)**mp.mpf('-0.5')))))
                pm*=p; me+=1
    return out

def run74(lam,N):
    A,Larch,Lpr,L,idx=build(lam,N,'zeta'); dim=len(idx)
    E,V=mp.eigsy(A); order=sorted(range(dim),key=lambda j:E[j])
    c0=np.array([float(V[i,order[0]]) for i in range(dim)])
    Ny=1000; ys,u0=recon_grid(c0,idx,L,Ny=Ny)
    if u0[Ny//2]<0: u0=-u0
    dy=ys[1]-ys[0]
    def u0e(xq):  # u0 extendido por cero fuera de [0,L], interp lineal
        out=np.zeros_like(xq); m=(xq>=0)&(xq<=L)
        out[m]=np.interp(xq[m],ys,u0)
        return out
    mx=int(lam*lam); pj=primes_jumps(mx)
    a0=np.max(np.abs(u0)); bulk=(np.abs(u0)>0.20*a0)
    # C(x) derivado
    num=np.zeros(Ny)
    for s,w in pj:
        num += w*s*s*0.5*(u0e(ys+s)+u0e(ys-s))
    C=np.where(np.abs(u0)>1e-9*a0, num/np.where(np.abs(u0)>1e-12,u0,1e-12), np.nan)
    Cb=C[bulk]; Cb=Cb[np.isfinite(Cb)]
    inner=(np.abs(u0)>0.45*a0); Ci=C[inner]; Ci=Ci[np.isfinite(Ci)]
    flat=np.std(Ci)/(abs(np.mean(Ci))+1e-300)
    cen=np.nanmean(C[(ys>L/2-0.4)&(ys<L/2+0.4)])
    yb=ys[bulk]; edg=np.nanmean(C[(ys>yb.min())&(ys<yb.min()+0.4)])
    # perfil 5 puntos
    yin=ys[inner]; prof=C[inner]/np.mean(Ci); sel=np.linspace(0,len(yin)-1,5).astype(int)
    print(f"\nlambda={lam} N={N} L={L:.3f}")
    print(f"  C(x) DERIVADO: perfil/mean bulk = {[f'{yin[s]:.2f}:{prof[s]:+.2f}' for s in sel]}")
    print(f"  std/|mean|={flat:.3f}   centro/borde={cen/edg:.3f}  (E70 real: bump 1.51, std 0.22/0.15/0.14)")
    return L,flat,cen/edg

print("E74: C_lambda DERIVADO (Lema1.1+Doob, tempering u0(x±logn)/u0(x)) vs C real E70")
res=[run74(l,N) for l,N in [(7.0,14),(9.0,16),(11.0,18),(13.0,21)]]
print(f"\nRESUMEN  (debe: std DECRECER ~0.22->0.14, centro/borde ~1.5 BUMP central):")
print(f"  L:            {[f'{r[0]:.2f}' for r in res]}")
print(f"  std/|mean|:   {[f'{r[1]:.3f}' for r in res]}")
print(f"  centro/borde: {[f'{r[2]:.3f}' for r in res]}")
