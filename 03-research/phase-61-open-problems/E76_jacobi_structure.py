"""
Objeto correcto, sin atajos: estructura de MATRIZ de la forma Doob G en la base Dirichlet ideal.
s_k(y) = sin((k+1) pi (y-y0)/W) en el bulk [y0,y0+W] (y0=margen, W=L-2*margen).
Calcular:
  Wm_kj = <s_k, s_j>_{u0^2}   (masa, peso u0^2)
  Gm_kj = G(u0 s_k, u0 s_j) = <u0 s_k, (A-eps0) u0 s_j>   (forma Doob)
Generalizado (Gm, Wm) -> ratios; comparar con (k+1)^2-1.
CLAVE: ¿la matriz normalizada Wm^{-1/2} Gm Wm^{-1/2} es TRIDIAGONAL (Jacobi)?
  Si si: la deformacion Dirichlet->QW es una correccion de Jacobi (nearest-neighbor),
  conectable con Connes Prop 3.5. Medir diagonal d_k vs (k+1)^2-1 y off-diag e_k, y su escala con lambda.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
exec(open('E70_doob_parter.py').read().split('# ---- ejecutar')[0])

def project_fourier(g, ys, idx, L):
    # coef c_n = (1/L) int g e^{-2pi i n y/L}; base real -> guardamos como vector complejo->real,imag
    dim=len(idx); cr=np.zeros(dim); ci=np.zeros(dim)
    for j,n in enumerate(idx):
        ph=2*np.pi*n*ys/L
        cr[j]=np.trapezoid(g*np.cos(ph),ys)/L
        ci[j]=np.trapezoid(g*np.sin(ph),ys)/L
    return cr,ci

def run76(lam,N,nmode=5):
    A,Larch,Lpr,L,idx=build(lam,N,'zeta'); dim=len(idx)
    E,V=mp.eigsy(A); order=sorted(range(dim),key=lambda j:E[j])
    eps0=float(E[order[0]])
    c0=np.array([float(V[i,order[0]]) for i in range(dim)])
    Ny=1400; ys,u0=recon_grid(c0,idx,L,Ny=Ny)
    if u0[Ny//2]<0: u0=-u0
    a0=np.max(np.abs(u0)); bulk=np.abs(u0)>0.20*a0; yb=ys[bulk]
    y0=yb.min(); W=yb.max()-yb.min()
    # A en numpy
    Anp=np.array([[float(A[a,b]) for b in range(dim)] for a in range(dim)])
    # modos ideales s_k * u0 -> proyectar a Fourier, formar Gm,Wm
    coefs=[]
    for k in range(nmode):
        sk=np.zeros(Ny); m=(ys>=y0)&(ys<=y0+W)
        sk[m]=np.sin((k+1)*np.pi*(ys[m]-y0)/W)
        g=u0*sk
        cr,ci=project_fourier(g,ys,idx,L)
        coefs.append((cr,ci))
    Gm=np.zeros((nmode,nmode)); Wm=np.zeros((nmode,nmode))
    for k in range(nmode):
        crk,cik=coefs[k]
        for j in range(nmode):
            crj,cij=coefs[j]
            # <g_k|A|g_j> real = crk^T A crj + cik^T A cij  (A real sym, base e^{2pi i n y/L})
            gAg=crk@Anp@crj + cik@Anp@cij
            ov = crk@crj + cik@cij   # <g_k|g_j> = L * sum c_k conj(c_j) -> real part
            Gm[k,j]=gAg - eps0*ov*L   # (A-eps0) ; ov*L = <g_k|g_j>_{L2}
            Wm[k,j]=ov*L
    # normalizar: H = Wm^{-1/2} Gm Wm^{-1/2}
    wval,wvec=np.linalg.eigh(Wm)
    Wm_ih=wvec@np.diag(1/np.sqrt(np.abs(wval)))@wvec.T
    H=Wm_ih@Gm@Wm_ih
    H=(H+H.T)/2
    ev=np.sort(np.linalg.eigvalsh(H))
    ratios=[ev[k]/ev[0] for k in range(nmode)]
    # estructura: diagonal vs off-diagonal de H (en base ideal, tras blanquear masa)
    diag=np.diag(H); off=H-np.diag(diag)
    # tridiagonalidad: masa fuera de la 1a sub/super-diagonal
    triband=np.zeros_like(H)
    for k in range(nmode):
        for j in range(nmode):
            if abs(k-j)<=1: triband[k,j]=H[k,j]
    nontri=np.linalg.norm(H-triband)/np.linalg.norm(H)
    print(f"\nlambda={lam} N={N} L={L:.3f} bulk W={W:.3f} margen={(L-W)/2:.3f}")
    print(f"  ratios (Gm,Wm)/ev0 = {[round(r,3) for r in ratios]}  (target (k+1)^2=1,4,9,16,25)")
    print(f"  H diag normaliz/d0 = {[round(float(diag[k]/diag[0]),3) for k in range(nmode)]}")
    print(f"  off-diag vecinas e_k=H[k,k+1]/d0 = {[round(float(H[k,k+1]/diag[0]),4) for k in range(nmode-1)]}")
    print(f"  NO-tridiagonal (masa fuera banda)/||H|| = {nontri:.4f}  => {'JACOBI (tridiag)' if nontri<0.15 else 'no tridiag'}")
    return L,ratios,nontri

print("E76: estructura de matriz de la forma Weil exacta en base Dirichlet ideal")
res=[run76(l,N) for l,N in [(7.0,14),(9.0,16),(11.0,18),(13.0,21)]]
print(f"\nRESUMEN escala lambda:")
print(f"  L:           {[f'{r[0]:.2f}' for r in res]}")
print(f"  ratio_2 (->4): {[f'{r[1][1]:.3f}' for r in res]}   ratio_3(->9): {[f'{r[1][2]:.3f}' for r in res]}")
print(f"  no-tridiag:  {[f'{r[2]:.3f}' for r in res]}")
