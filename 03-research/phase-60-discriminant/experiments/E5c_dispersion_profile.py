#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E5c: PERFIL de dispersion vs altura (separa senal de ruido de truncacion).
#
# E5b mostro dispersion(L_DH) mayor en 85.7 que en control, pero el control no quedo plano.
# Test limpio: dispersion(H) = spread sobre N del autovalor mas cercano a H, como funcion
# de H en [20,120]. Ceros OFF-line de L_DH: 85.699, 114.163. Si dispersion(L_DH) tiene
# PICOS localizados en esas alturas sobre una linea base ~ dispersion(ζ), es la firma del
# cero off-line (convergencia <=> RH). Si crece suave con H, es resolucion, no concluyente.
# ======================================================================================
import numpy as np, importlib.util
spec=importlib.util.spec_from_file_location("e5","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E5_ldh_violator.py")
e5=importlib.util.module_from_spec(spec); spec.loader.exec_module(e5)

LAM=3.7
tgrid=np.arange(-300,300,0.01)+1e-6
coeffs_zeta=e5.vonmangoldt_upto(int(LAM*LAM))
coeffs_ldh =e5.ldh_b_upto(int(LAM*LAM))
Ns=[44,48,52,56,60]
OFFLINE=[85.699,114.163]

def all_roots(coeffs,a,cond,pole):
    """raices reales en (1,130) para cada N -> dict N->array."""
    out={}
    for N in Ns:
        QW,idx,L=e5.build_QW(LAM,N,a,cond,coeffs,pole,tgrid)
        xi,_=e5.lowest_xi(QW)
        d=2*np.pi*idx/L; order=np.argsort(d); d=d[order]; xi=xi[order]
        from scipy.optimize import brentq
        f=lambda s: np.sum(xi/(s-d))
        r=[]
        for i in range(len(d)-1):
            aa,bb=d[i]+1e-7,d[i+1]-1e-7
            if aa>=bb or bb<15 or aa>130: continue
            try:
                if f(aa)*f(bb)<0: r.append(brentq(f,aa,bb,xtol=1e-10))
            except Exception: pass
        out[N]=np.array(sorted(r))
    return out

def dispersion_profile(roots,Hs):
    prof=[]
    for H in Hs:
        vals=[]
        for N in Ns:
            r=roots[N]
            if len(r): vals.append(r[np.argmin(np.abs(r-H))])
        vals=np.array(vals)
        prof.append(vals.max()-vals.min())
    return np.array(prof)

print("="*78); print(" E5c: perfil de dispersion(H).  λ=3.7, N=",Ns); print("="*78)
Rz=all_roots(coeffs_zeta,0.25,1.0,True)
Rd=all_roots(coeffs_ldh ,0.75,5.0,False)
Hs=np.arange(20,121,2.0)
Pz=dispersion_profile(Rz,Hs)
Pd=dispersion_profile(Rd,Hs)
print(f"\n base ζ: mediana={np.median(Pz):.4f}  max={Pz.max():.4f}")
print(f" L_DH  : mediana={np.median(Pd):.4f}  max={Pd.max():.4f}\n")
print("   H     disp(ζ)   disp(L_DH)   ratio   marca")
mx=max(Pd.max(),1e-9)
for H,pz,pd in zip(Hs,Pz,Pd):
    near=min(abs(H-z) for z in OFFLINE)
    mark="  <== OFF-line zero" if near<2.0 else ""
    bar="#"*int(40*pd/mx)
    print(f"  {H:5.0f}  {pz:7.4f}   {pd:8.4f}   {pd/max(pz,1e-4):5.1f}  {bar}{mark}")
print("\n LECTURA: pico de disp(L_DH) localizado en 85.7 / 114 sobre base plana = firma")
print(" del cero off-line. Crecimiento suave con H = resolucion, no concluyente.")
