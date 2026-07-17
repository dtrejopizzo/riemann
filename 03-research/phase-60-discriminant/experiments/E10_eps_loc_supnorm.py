#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — N5c (v2): el objeto del Teorema 2, observable correcto y libre de escala.
#
# sup|ξ̂-Ξ|: cerca de una raiz ρ̂_n del aproximante, ξ̂≈0, asi que |ξ̂-Ξ| ≈ |Ξ(ρ̂_n)|.
# Normalizado por la escala local de Ξ:
#     eta_n = |Ξ(ρ̂_n)| / max_{|t-ρ̂_n|<Δ} |Ξ(t)|        (Δ ~ medio espaciado local)
# Mide cuanto FALLA el target exacto en anularse donde el aproximante SI se anula.
#   ζ (RH-true): ρ̂_n≈γ_n (cero) => eta_n≈0 en todo n.
#   L_DH: en la raiz ~85.70 (proyeccion del par off-line) Ξ_DH NO se anula => eta ~ O(1),
#         localizado. Si persiste/crece con λ => firma real-axis de beta (A). Si ->0 => B.
#
# Esto es exactamente eps_loc relativo (Teorema 2), separado interior/borde, sin los polos
# del ratio de Hadamard ni el desajuste de escala producto-vs-Gamma.
# ======================================================================================
import numpy as np, importlib.util, mpmath as mp
mp.mp.dps=25
spec=importlib.util.spec_from_file_location("e5","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E5_ldh_violator.py")
e5=importlib.util.module_from_spec(spec); spec.loader.exec_module(e5)

def xi_zeta(t):
    s=mp.mpf('0.5')+1j*mp.mpf(t)
    return abs(mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))
KAPPA=mp.mpf((np.sqrt(10-2*np.sqrt(5))-2)/(np.sqrt(5)-1))
Adh=[mp.mpf(0),mp.mpf(1),KAPPA,-KAPPA,mp.mpf(-1)]
def f_dh(s): return mp.mpf(5)**(-s)*mp.fsum([Adh[r%5]*mp.zeta(s,mp.mpf(r)/5) for r in range(1,6)])
def xi_dh(t):
    s=mp.mpf('0.5')+1j*mp.mpf(t); G=(mp.mpf(5)/mp.pi)**((s+1)/2)*mp.gamma((s+1)/2)
    return abs(G*f_dh(s))

def ccm_roots(which,lam,hmax):
    N=int(hmax*np.log(lam)/np.pi)+18
    tgrid=np.arange(-3.5*hmax,3.5*hmax,0.01)+1e-6
    if which=='zeta':
        coeffs=e5.vonmangoldt_upto(int(lam*lam)); QW,idx,L=e5.build_QW(lam,N,0.25,1.0,coeffs,True,tgrid)
    else:
        coeffs=e5.ldh_b_upto(int(lam*lam));       QW,idx,L=e5.build_QW(lam,N,0.75,5.0,coeffs,False,tgrid)
    w,V=np.linalg.eigh(QW); xi=V[:,0]
    d=2*np.pi*idx/L; o=np.argsort(d); d=d[o]; xi=xi[o]
    from scipy.optimize import brentq
    f=lambda s: np.sum(xi/(s-d)); r=[]
    for i in range(len(d)-1):
        a,b=d[i]+1e-7,d[i+1]-1e-7
        if a>=b or b<2 or a>hmax: continue
        try:
            if f(a)*f(b)<0: r.append(brentq(f,a,b,xtol=1e-11))
        except Exception: pass
    return np.array(sorted([x for x in r if 2<x<hmax]))

def eta(absfun, root, spacing):
    Δ=0.5*spacing
    ts=np.linspace(root-Δ, root+Δ, 25)
    vals=[float(absfun(float(t))) for t in ts]
    here=float(absfun(float(root)))
    mx=max(vals)
    return here/mx if mx>0 else np.nan

print("="*88)
print(" N5c (v2): eta_n = |Ξ(ρ̂_n)|/escala_local  (cuanto falla Ξ en anularse en la raiz de ξ̂)")
print("="*88,flush=True)
print(f"{'λ':>4} {'T*':>6} | {'ζ: max eta_int':>16} {'eta_edge':>10} | {'DH: max eta_int':>16} {'eta_edge':>10} | {'DH eta@85.7':>12}",flush=True)

for lam in [4.0,5.0,6.0,7.0,8.0]:
    Tstar=2*np.pi*lam*lam; edge=0.92*Tstar
    rz=ccm_roots('zeta',lam,edge); rd=ccm_roots('ldh',lam,edge)
    def spac(roots,i):
        if 0<i<len(roots)-1: return min(roots[i+1]-roots[i],roots[i]-roots[i-1])
        return 2*np.pi/np.log(max(roots[i],3))
    def etas(roots,absfun):
        out=[]
        for i,r in enumerate(roots):
            out.append((r, eta(absfun,r,spac(roots,i))))
        return out
    ez=etas(rz,xi_zeta); ed=etas(rd,xi_dh)
    def split(es):
        intr=[e for (t,e) in es if t<0.7*Tstar and not np.isnan(e)]
        edg =[e for (t,e) in es if t>=0.7*Tstar and not np.isnan(e)]
        return (max(intr) if intr else np.nan, max(edg) if edg else np.nan)
    ziz,zed=split(ez); diz,ded=split(ed)
    # eta en la raiz DH mas cercana a 85.7 (si interior)
    if len(rd):
        j=int(np.argmin(np.abs(rd-85.70)))
        e85 = eta(xi_dh, rd[j], spac(rd,j)) if rd[j]<0.85*Tstar else np.nan
    else: e85=np.nan
    print(f"{lam:4.1f} {Tstar:6.0f} | {ziz:16.3e} {zed:10.3e} | {diz:16.3e} {ded:10.3e} | {e85:12.3e}",flush=True)

print("\n LECTURA:")
print("  B (ciega): max eta_int^DH ~ eta_int^ζ (ambos ~0); eta@85.7 -> 0 con λ.")
print("  A (residual real-axis): eta_int^DH NO->0, dominado por eta@85.7 que PERSISTE/crece = firma de β.")
