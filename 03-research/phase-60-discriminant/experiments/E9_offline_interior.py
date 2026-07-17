#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E9: el discriminante DECISIVO, corregido. Violador L_DH INTERIOR + off-axis.
#
# Por que E5 fallo (inconcluso): (1) lambda=3.7 pone el cero off-line de L_DH (85.699+0.3085i)
# JUSTO en el horizonte T*=86 -> no-resolucion ambigua (Nyquist vs off-line). (2) metrica
# de dispersion en eje real, cuando Thm 1.1(iii) dice que un cero off-line es un autovalor
# FALTANTE (gap), no uno disperso.
#
# E9 corrige AMBOS:
#  - lambda=6 -> T*=2*pi*36=226 -> el cero 85.7 esta a x=0.38 (interior profundo).
#  - metrica de RAIZ FALTANTE + off-axis:
#       (A) ¿ξ̂_DH pone una raiz real cerca de 85.699?  (vecino mas cercano y su gap)
#       (B) convergencia en N de esa raiz vs control interior on-line (H=49) de la MISMA L_DH
#       (C) off-axis: |f_DH(85.699+0.3085i)| (no puede anularse) — ¿converge a un minimo local?
#
# Discriminante:
#   Escenario A (CCM ve posicion): anomalia LOCALIZADA en 85.7 (gap/no-convergencia/min off-axis)
#       ausente en el control on-line y ausente en zeta. -> Teorema 2 cobra dientes.
#   Escenario B (CCM ciego a posicion): ξ̂_DH coloca raiz en ~85.699 como si fuera on-line,
#       converge igual que el control. -> el puente a RH es ilusion.
# ======================================================================================
import numpy as np, importlib.util, mpmath as mp
spec=importlib.util.spec_from_file_location("e5","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E5_ldh_violator.py")
e5=importlib.util.module_from_spec(spec); spec.loader.exec_module(e5)

LAM=6.0
TSTAR=2*np.pi*LAM*LAM
RHO0_IM=85.699; RHO0_RE_DEPTH=0.3085      # cero off-line DH: 1/2+0.3085 + 85.699 i  (en t: 85.699 - 0.3085 i)
print("="*80)
print(f" E9: violador L_DH INTERIOR.  lambda={LAM}  T*={TSTAR:.1f}  (cero off-line 85.7 a x={RHO0_IM/TSTAR:.3f})")
print("="*80,flush=True)

coeffs_zeta=e5.vonmangoldt_upto(int(LAM*LAM))
coeffs_ldh =e5.ldh_b_upto(int(LAM*LAM))
tgrid=np.arange(-600,600,0.01)+1e-6

def full_real_roots(coeffs,a,cond,pole,N,hmax=130):
    QW,idx,L=e5.build_QW(LAM,N,a,cond,coeffs,pole,tgrid)
    w,V=np.linalg.eigh(QW); xi=V[:,0]
    d=2*np.pi*idx/L; order=np.argsort(d); d=d[order]; xi=xi[order]
    from scipy.optimize import brentq
    f=lambda s: np.sum(xi/(s-d))
    r=[]
    for i in range(len(d)-1):
        aa,bb=d[i]+1e-7,d[i+1]-1e-7
        if aa>=bb or bb<10 or aa>hmax: continue
        try:
            if f(aa)*f(bb)<0: r.append(brentq(f,aa,bb,xtol=1e-11))
        except Exception: pass
    return np.array(sorted([x for x in r if 10<x<hmax])), (xi,d)

def f_complex(xidata, s):
    xi,d=xidata
    return np.sum(xi/(s-d))

def nearest(roots,H):
    if len(roots)==0: return np.nan
    return roots[np.argmin(np.abs(roots-H))]

Ns=[50,60,70,80]
print(f" N escalados: {Ns}   (dim hasta {2*max(Ns)+1})\n",flush=True)

# ---------- GATE zeta a lambda=6 ----------
print("--- GATE: zeta a lambda=6 (debe reproducir ceros on-line) ---",flush=True)
rz,zdat=full_real_roots(coeffs_zeta,0.25,1.0,True,max(Ns))
g1=float(mp.im(mp.zetazero(1))); g_near85=84.73549
print(f"  raiz cerca 14.1347 : {nearest(rz,14.1347):.5f}   (err {abs(nearest(rz,14.1347)-g1):.2e})")
print(f"  raiz cerca 84.7355 : {nearest(rz,84.7355):.5f}   (cero on-line zeta 84.73549)",flush=True)

# ---------- L_DH: patron de raices alrededor del cero off-line ----------
print("\n--- L_DH: raices reales en [78,94] (max N) ---",flush=True)
rd,ddat=full_real_roots(coeffs_ldh,0.75,5.0,False,max(Ns))
band=rd[(rd>=78)&(rd<=94)]
print(f"  raices L_DH: {np.round(band,4)}")
near_off=nearest(rd,RHO0_IM)
print(f"  raiz mas cercana a 85.699 (Re del cero off-line): {near_off:.5f}   gap={abs(near_off-RHO0_IM):.4f}",flush=True)

# ---------- convergencia en N: off-line (85.7) vs control interior on-line (49) ----------
print("\n--- convergencia en N de la raiz mas cercana (L_DH) ---",flush=True)
print("    N |  raiz~49 (control on-line) | raiz~85.699 (target off-line) | |f_DH(rho0)| off-axis",flush=True)
rho0 = RHO0_IM - 1j*RHO0_RE_DEPTH    # punto off-axis en variable t
v49=[]; v85=[]
for N in Ns:
    rr,dat=full_real_roots(coeffs_ldh,0.75,5.0,False,N)
    a49=nearest(rr,49.0); a85=nearest(rr,RHO0_IM)
    foff=abs(f_complex(dat,rho0))
    v49.append(a49); v85.append(a85)
    print(f"   {N:3d} |        {a49:10.5f}        |        {a85:10.5f}          |   {foff:.4e}",flush=True)
v49=np.array(v49); v85=np.array(v85)
disp49=np.nanmax(v49)-np.nanmin(v49); disp85=np.nanmax(v85)-np.nanmin(v85)

# ---------- control zeta: convergencia en N en 84.7355 (on-line) ----------
print("\n--- convergencia en N de la raiz zeta cerca 84.7355 (control RH-true) ---",flush=True)
vz=[]
for N in Ns:
    rr,_=full_real_roots(coeffs_zeta,0.25,1.0,True,N)
    az=nearest(rr,84.7355); vz.append(az)
    print(f"   N={N:3d}: raiz={az:.6f}",flush=True)
vz=np.array(vz); dispz=np.nanmax(vz)-np.nanmin(vz)

print("\n"+"="*80)
print(" LECTURA")
print("="*80)
print(f"  dispersion(N) L_DH control on-line H=49      = {disp49:.5f}")
print(f"  dispersion(N) L_DH target off-line H=85.7    = {disp85:.5f}")
print(f"  dispersion(N) zeta  on-line H=84.7355        = {dispz:.5f}")
print(f"  gap |raiz_DH - 85.699|                       = {abs(near_off-RHO0_IM):.5f}")
print()
print("  Escenario A (CCM ve posicion): disp85 >> disp49 y >> dispz, anomalia LOCALIZADA")
print("     en 85.7; o gap claro; o |f_DH(rho0)| con minimo que NO baja. -> Teorema 2 con dientes.")
print("  Escenario B (CCM ciego): disp85 ~ disp49 ~ dispz, raiz en ~85.699 limpia. -> ilusion.")
