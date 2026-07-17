#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — N5c (v3, robusto): el discriminante de sup-norma en 3 numeros, sin raices
# espurias. Solo en raices emparejadas a ceros verdaderos. lambda interior (6,7,8).
#
#   eta(root) = |Ξ(root)| / max_{|t-root|<=0.5*spacing} |Ξ(t)|
#     = cuanto FALLA el target exacto Ξ en anularse donde el aproximante ξ̂ SI se anula.
#     (proxy escalado de |ξ̂-Ξ| cerca de la raiz; eps_loc relativo local del Teorema 2.)
#
#   eta_off  : raiz DH ~85.70 (proyeccion real del cero OFF-line 85.699+0.3085i) -> Ξ_DH NO se anula
#   eta_onDH : raiz DH ~49    (cero ON-line de control)                          -> Ξ_DH se anula
#   eta_onZ  : raiz ζ  ~84.74 (cero ON-line de ζ)                                -> Ξ_ζ se anula
#
# Escenario A (firma real-axis de β): eta_off ~ O(1) >> eta_onDH ~ eta_onZ ~ 0, y eta_off PERSISTE con λ.
# Escenario B (ciega):                eta_off ~ eta_onDH ~ eta_onZ ~ 0, eta_off -> 0 con λ.
# ======================================================================================
import numpy as np, importlib.util, mpmath as mp
mp.mp.dps=22
spec=importlib.util.spec_from_file_location("e5","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E5_ldh_violator.py")
e5=importlib.util.module_from_spec(spec); spec.loader.exec_module(e5)

def axi_zeta(t):
    s=mp.mpf('0.5')+1j*mp.mpf(t)
    return abs(mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))
KAPPA=mp.mpf((np.sqrt(10-2*np.sqrt(5))-2)/(np.sqrt(5)-1))
Adh=[mp.mpf(0),mp.mpf(1),KAPPA,-KAPPA,mp.mpf(-1)]
def f_dh(s): return mp.mpf(5)**(-s)*mp.fsum([Adh[r%5]*mp.zeta(s,mp.mpf(r)/5) for r in range(1,6)])
def axi_dh(t):
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
    ts=np.linspace(root-Δ, root+Δ, 13)
    vals=[float(absfun(float(t))) for t in ts]
    mx=max(vals); here=float(absfun(float(root)))
    return here/mx if mx>0 else np.nan

def local_spacing(roots, r):
    i=int(np.argmin(np.abs(roots-r)))
    if 0<i<len(roots)-1: return min(roots[i+1]-roots[i], roots[i]-roots[i-1])
    return 2*np.pi/np.log(max(r,3))

print("="*78)
print(" N5c (v3): eta = |Ξ(raiz)|/escala_local.  off-line(85.7) vs on-line controls")
print("="*78)
print(f"{'λ':>4} {'T*':>6} {'x=85.7/T*':>9} | {'DH eta_off(85.7)':>16} {'DH eta_on(49)':>14} {'ζ eta_on(84.7)':>15}",flush=True)

for lam in [6.0,7.0,8.0]:
    Tstar=2*np.pi*lam*lam
    rd=ccm_roots('ldh',lam,0.6*Tstar)
    rz=ccm_roots('zeta',lam,0.6*Tstar)
    roff=rd[np.argmin(np.abs(rd-85.70))]
    ron =rd[np.argmin(np.abs(rd-49.0))]
    ronz=rz[np.argmin(np.abs(rz-84.7355))]
    eoff=eta(axi_dh, roff, local_spacing(rd,roff))
    eon =eta(axi_dh, ron,  local_spacing(rd,ron))
    eonz=eta(axi_zeta:=axi_zeta, ronz, local_spacing(rz,ronz)) if False else eta(axi_zeta, ronz, local_spacing(rz,ronz))
    print(f"{lam:4.1f} {Tstar:6.0f} {85.7/Tstar:9.3f} | {eoff:16.4e} {eon:14.4e} {eonz:15.4e}   (roff={roff:.3f})",flush=True)

print("\n LECTURA:")
print("  A: eta_off ~ O(1) >> eta_on, y PERSISTE/crece con λ  => firma real-axis de β (Teorema 2 con dientes).")
print("  B: eta_off ~ eta_on ~ 0, eta_off -> 0 con λ          => CCM ciega a posicion tambien en sup-norma.")
