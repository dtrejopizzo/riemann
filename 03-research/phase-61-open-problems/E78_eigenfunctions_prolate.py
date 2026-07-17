"""
8vo angulo (usa solo autoFUNCIONES O(1), inmune al knife-edge e^{-cL}).
Hipotesis: las autofunciones de QW = prolato-esferoidales (mismas que el prolato desnudo);
SOLO los autovalores se deforman (8n+1 lineal -> (k+1)^2 cuadr) = cambio de ORDEN del operador.
Si OVERLAP(f_k^QW, psi_k^prolate) ~ 1 => 2.3.F se parte: (a) autofunc prolatas => portadora afin
por WKB prolato (citable), (b) aritmetico cambia orden 1->2.

Prolatas = autofunciones del operador de concentracion sinc en [0,L] con time-bandwidth c:
   (S f)(x) = int_0^L sin(W(x-y))/(pi(x-y)) f(y) dy,  c = W*L/2.
Escaneo c (CCM usa c=2pi lam^2) y reporto overlap de f_0,f_1,f_2,f_3 con psi_0,psi_1,psi_2,psi_3.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
exec(open('E70_doob_parter.py').read().split('# ---- ejecutar')[0])

def prolate_funcs(L, W, Ny, nmode):
    ys=np.linspace(0,L,Ny); dy=ys[1]-ys[0]
    X=ys[:,None]-ys[None,:]
    with np.errstate(divide='ignore',invalid='ignore'):
        K=np.where(np.abs(X)<1e-12, W/np.pi, np.sin(W*X)/(np.pi*X))
    K=K*dy  # cuadratura
    ev,evec=np.linalg.eigh(K)
    order=np.argsort(-ev)  # mayor concentracion primero
    out=[evec[:,order[k]]/np.sqrt(np.sum(evec[:,order[k]]**2)) for k in range(nmode)]
    return ys,out,[ev[order[k]] for k in range(nmode)]

def qw_funcs(lam,N,nmode):
    A,La,Lp,L,idx=build(lam,N,'zeta'); dim=len(idx)
    E,V=mp.eigsy(A); order=sorted(range(dim),key=lambda j:E[j])
    fs=[]
    Ny=900
    for k in range(nmode):
        c=np.array([float(V[i,order[k]]) for i in range(dim)])
        ys,f=recon_grid(c,idx,L,Ny=Ny)
        f=f/np.sqrt(np.sum(f**2)); fs.append(f)
    return ys,fs,L

def overlap(a,b):
    return abs(np.dot(a,b))/(np.linalg.norm(a)*np.linalg.norm(b))

def run78(lam,N,nmode=4):
    ys,fs,L=qw_funcs(lam,N,nmode); Ny=len(ys)
    print(f"\n{'='*60}\nlambda={lam} N={N} L={L:.3f}")
    # escanear bandwidth W via c
    best=None
    for c in [mp.pi*lam**2*f for f in [0.5,1.0,2.0]]:
        W=float(2*c/L)
        yp,ps,conc=prolate_funcs(L,W,Ny,nmode)
        ov=[overlap(fs[k],ps[k]) for k in range(nmode)]
        score=np.mean(ov)
        if best is None or score>best[0]: best=(score,float(c),ov,conc)
    # refinar alrededor del mejor c
    c0=best[1]
    for c in [c0*f for f in [0.6,0.8,1.0,1.25,1.6]]:
        W=float(2*c/L)
        yp,ps,conc=prolate_funcs(L,W,Ny,nmode)
        ov=[overlap(fs[k],ps[k]) for k in range(nmode)]
        if np.mean(ov)>best[0]: best=(np.mean(ov),c,ov,conc)
    print(f"  mejor c={best[1]:.2f} (CCM c=2pi lam^2={float(2*mp.pi*lam**2):.1f})")
    print(f"  OVERLAP(f_k^QW, psi_k^prolate) k=0..{nmode-1}: {[round(x,4) for x in best[2]]}")
    print(f"  concentracion prolata (autoval sinc, ~1=concentrado): {[round(x,4) for x in best[3]]}")
    print(f"  => {'AUTOFUNCIONES PROLATAS (hip. confirmada)' if min(best[2])>0.9 else 'overlap parcial' if min(best[2])>0.7 else 'NO prolatas'}")
    return best[2]

for lam,N in [(7.0,14),(9.0,16),(11.0,18)]:
    run78(lam,N)
