#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — N5c (v4, DECISIVO): PERFIL de eta sobre el interior. Localizacion (referee §4).
#
# eta(raiz) = |Ξ(raiz)|/escala_local. Perfil sobre TODAS las raices interiores de ξ̂.
#   ζ  (RH-true): perfil PLANO ~0 (Ξ_ζ se anula en cada raiz).
#   DH: si el perfil es plano ~0 EXCEPTO picos en 85.7 y 114.2 (los DOS ceros off-line)
#       => firma LOCALIZADA de β en sup-norma (Escenario A, Teorema 2 con dientes).
#       si degradado en todos lados => no concluyente. si plano sin picos => B.
#
# lambda=7: T*=308, interior hasta ~154 contiene AMBOS ceros off-line (85.699, 114.163).
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

def eta(absfun, roots, i):
    r=roots[i]
    sp=min(roots[i+1]-r, r-roots[i-1]) if 0<i<len(roots)-1 else 2*np.pi/np.log(max(r,3))
    Δ=0.5*sp; ts=np.linspace(r-Δ, r+Δ, 13)
    vals=[float(absfun(float(t))) for t in ts]; mx=max(vals)
    return float(absfun(float(r)))/mx if mx>0 else np.nan

LAM=7.0; Tstar=2*np.pi*LAM*LAM; HI=0.52*Tstar
print("="*74)
print(f" N5c (v4) PERFIL de eta.  lambda={LAM}  T*={Tstar:.0f}  ceros off-line: 85.699, 114.163")
print("="*74,flush=True)
rz=ccm_roots('zeta',LAM,HI); rd=ccm_roots('ldh',LAM,HI)

print("\n  raiz_ζ    eta_ζ    |   raiz_DH   eta_DH   marca",flush=True)
OFF=[85.699,114.163]
nmax=max(len(rz),len(rd))
for i in range(nmax):
    sz=f"{rz[i]:8.3f} {eta(axi_zeta,rz,i):9.2e}" if 0<i<len(rz)-1 and rz[i]>25 else " "*18
    if 0<i<len(rd)-1 and rd[i]>25:
        ed=eta(axi_dh,rd,i); mk=""
        if min(abs(rd[i]-o) for o in OFF)<1.5: mk="  <== OFF-line"
        sd=f"{rd[i]:8.3f} {ed:9.2e}{mk}"
    else: sd=""
    if sz.strip() or sd.strip(): print(f"  {sz}   | {sd}",flush=True)

# resumen: baseline vs picos
def prof(absfun,roots):
    es=[(roots[i],eta(absfun,roots,i)) for i in range(1,len(roots)-1) if roots[i]>30]
    base=np.median([e for (t,e) in es if min(abs(t-o) for o in OFF)>=2])
    pk=[(t,e) for (t,e) in es if min(abs(t-o) for o in OFF)<1.5]
    return base,pk
bz,_=prof(axi_zeta,rz); bd,pkd=prof(axi_dh,rd)
print("\n RESUMEN:",flush=True)
print(f"  ζ  baseline eta (mediana) = {bz:.2e}",flush=True)
print(f"  DH baseline eta (mediana, lejos de off-line) = {bd:.2e}",flush=True)
print(f"  DH eta en ceros off-line: {[(round(t,2),float(f'{e:.2e}')) for t,e in pkd]}",flush=True)
print("\n A: DH baseline bajo + picos claros en 85.7 y 114.2 = firma localizada de β (sup-norma).")
print(" B/no-concluyente: sin contraste pico/baseline.")
