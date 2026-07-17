#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E5b: el DISCRIMINANTE de convergencia (el experimento decisivo).
#
# Mapa a RH, Eslabon 2 + Thm 1.1(iii): ξ̂_{λ,N} tiene SOLO raices reales a todo N finito.
# Si Ξ_f tiene un cero COMPLEJO (off-line), ξ̂ no puede converger a el (Hurwitz) => la
# convergencia en N del autovalor cercano DEBE romperse.
#
# Test: para ζ (control, ceros on-line) y L_DH (violador, cero off-line en 85.699+0.3085i),
# seguir el autovalor real mas cercano a una altura H al crecer N=[36..56], y medir su
# DISPERSION (max-min). Convergido => dispersion->0 ; roto => dispersion grande/estancada.
#
# CONTROL ANTI-AUTOENGANO: medir tambien a una altura H_on donde L_DH tiene ceros ON-line.
# Si L_DH converge bien en H_on y SOLO se rompe en H_off=85.7 => firma especifica del cero
# off-line (no "L_DH converge peor en todos lados"). Si se rompe en ambas => no concluyente.
# ======================================================================================
import numpy as np, importlib.util
spec=importlib.util.spec_from_file_location("e5","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E5_ldh_violator.py")
e5=importlib.util.module_from_spec(spec); spec.loader.exec_module(e5)

LAM=3.7
tgrid=np.arange(-300,300,0.01)+1e-6
coeffs_zeta=e5.vonmangoldt_upto(int(LAM*LAM))
coeffs_ldh =e5.ldh_b_upto(int(LAM*LAM))
Ns=[36,40,44,48,52,56]

def track(coeffs,a_arch,cond,use_pole,H):
    vals=[]
    for N in Ns:
        QW,idx,L=e5.build_QW(LAM,N,a_arch,cond,coeffs,use_pole,tgrid)
        xi,_=e5.lowest_xi(QW)
        r=e5.roots_near(xi,idx,L,H,3.0)
        if len(r):
            vals.append(r[np.argmin(np.abs(r-H))])
        else:
            vals.append(np.nan)
    return np.array(vals)

def disp(v):
    v=v[~np.isnan(v)]
    return (v.max()-v.min()) if len(v)>=2 else np.nan

print("="*78)
print(" E5b: convergencia-en-N del autovalor (decisivo).  λ=3.7")
print("="*78)
print(f" N = {Ns}\n")

for H,label in [(48.0,"H=48  (control)"),(85.7,"H=85.7 (L_DH OFF-line: 85.699+0.3085i)")]:
    print(f"--- altura {label} ---")
    vz=track(coeffs_zeta,0.25,1.0,True,H)
    vd=track(coeffs_ldh ,0.75,5.0,False,H)
    print(f"  ζ   autovalor(N): {np.round(vz,4)}   dispersion={disp(vz):.4f}")
    print(f"  L_DH autovalor(N): {np.round(vd,4)}   dispersion={disp(vd):.4f}")
    print()

print("="*78)
print(" LECTURA")
print("="*78)
print(" Si disp(ζ) pequena en ambas alturas, y disp(L_DH) pequena en H=48 pero GRANDE en")
print(" H=85.7 => firma especifica del cero off-line = testigo de 'convergencia <=> RH'.")
print(" Si disp(L_DH) grande en ambas => operador peor condicionado, NO concluyente.")
