#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E9b: clasificacion LIMPIA. Ceros reales de L_DH (mpmath) vs raices de ξ̂_DH.
#
# E9 mostro: ξ̂_DH pone una raiz real en 85.7306 (cerca de Re del cero off-line 85.699),
# que CONVERGE. ¿Es eso "ve un cero on-line que existe ahi" (sin senal) o "rellena la
# proyeccion real del par off-line" (Escenario B, ciego a posicion)? Decide saber donde
# estan los ceros VERDADEROS de L_DH.
#
# f_DH(s) = 5^{-s} Σ_{r=1}^{5} a(r) ζ(s, r/5)   (Hurwitz), a=(1,κ,-κ,-1,0), κ=0.284079.
# Buscamos ceros on-line (s=1/2+it) por cambio de signo de f en la linea, y confirmamos
# el par off-line 0.8085±... +85.699i. Luego overlay con las raices reales de ξ̂_DH.
# ======================================================================================
import numpy as np, importlib.util, mpmath as mp
mp.mp.dps=30
spec=importlib.util.spec_from_file_location("e5","/Users/dt/riemann/riemann-program/phase-60-discriminante/experiments/E5_ldh_violator.py")
e5=importlib.util.module_from_spec(spec); spec.loader.exec_module(e5)

KAPPA=mp.mpf((np.sqrt(10-2*np.sqrt(5))-2)/(np.sqrt(5)-1))
A=[mp.mpf(0),mp.mpf(1),KAPPA,-KAPPA,mp.mpf(-1)]   # a[r], r=1..4, a[5]=a[0]=0  -> index r%5

def f_dh(s):
    return mp.mpf(5)**(-s)*mp.fsum([A[r%5]*mp.zeta(s, mp.mpf(r)/5) for r in range(1,6)])

print("="*80)
print(" E9b: ceros reales de L_DH (mpmath) vs raices de ξ̂_DH (CCM, lambda=6)")
print("="*80,flush=True)

# 1) confirmar el cero off-line conocido
z_off=mp.mpf('0.5')+mp.mpf('0.3085')+1j*mp.mpf('85.699')
print(f"\n confirmando cero off-line: f_DH(0.8085+85.699i) = {mp.nstr(f_dh(z_off),4)}",flush=True)
try:
    zo=mp.findroot(f_dh, mp.mpf('0.8085')+1j*mp.mpf('85.699'))
    print(f"   refinado: s={mp.nstr(zo,10)}   (Re-1/2={mp.nstr(mp.re(zo)-0.5,4)}, Im={mp.nstr(mp.im(zo),8)})",flush=True)
except Exception as ex:
    print("   findroot off-line fallo:",ex,flush=True)

# 2) ceros ON-line (s=1/2+it): cambios de signo de g(t)=f_dh(1/2+it) (real en la linea? no necesariamente)
#    f_DH NO es autodual real; usamos Z-funcion: rotamos por la fase del factor gamma. Simplest:
#    buscar minimos de |f_dh(1/2+it)| como proxy de ceros on-line.
print("\n ceros on-line de L_DH (minimos de |f_DH(1/2+it)|) en ventanas de interes:",flush=True)
def find_online_zeros(t0,t1,step=mp.mpf('0.05')):
    ts=[]; t=t0; prev=abs(f_dh(mp.mpf('0.5')+1j*t)); pt=t
    vals=[]
    tt=t0
    while tt<=t1:
        v=abs(f_dh(mp.mpf('0.5')+1j*tt)); vals.append((tt,v)); tt+=step
    # minimos locales bajo umbral
    out=[]
    for i in range(1,len(vals)-1):
        if vals[i][1]<vals[i-1][1] and vals[i][1]<vals[i+1][1] and vals[i][1]<0.05:
            # refinar
            try:
                zr=mp.findroot(lambda t: f_dh(mp.mpf('0.5')+1j*t), vals[i][0])
                if abs(mp.im(zr))>0 and abs(mp.re(zr))<1e-6: pass
                out.append(complex(vals[i][0], float(vals[i][1])))
            except Exception: out.append(complex(vals[i][0], float(vals[i][1])))
    return out

for (lo,hi,lab) in [(44,54,"interior on-line ~49"),(80,92,"alrededor off-line 85.7"),(110,118,"alrededor off-line 114.2")]:
    zs=find_online_zeros(mp.mpf(lo),mp.mpf(hi))
    print(f"  [{lo},{hi}] {lab}: minimos |f| on-line en t≈ {[round(z.real,3) for z in zs]}  (|f|={[round(z.imag,4) for z in zs]})",flush=True)

# 3) raices reales de ξ̂_DH (CCM) en las mismas ventanas
print("\n raices reales de ξ̂_DH (CCM lambda=6, N=80):",flush=True)
LAM=6.0; tgrid=np.arange(-600,600,0.01)+1e-6
coeffs_ldh=e5.ldh_b_upto(int(LAM*LAM))
QW,idx,L=e5.build_QW(LAM,80,0.75,5.0,coeffs_ldh,False,tgrid)
w,V=np.linalg.eigh(QW); xi=V[:,0]
d=2*np.pi*idx/L; o=np.argsort(d); d=d[o]; xi=xi[o]
from scipy.optimize import brentq
f=lambda s: np.sum(xi/(s-d)); roots=[]
for i in range(len(d)-1):
    aa,bb=d[i]+1e-7,d[i+1]-1e-7
    if aa>=bb or bb<40 or aa>120: continue
    try:
        if f(aa)*f(bb)<0: roots.append(brentq(f,aa,bb,xtol=1e-11))
    except Exception: pass
roots=np.array(sorted(roots))
for (lo,hi) in [(44,54),(80,92),(110,118)]:
    print(f"  [{lo},{hi}]: {np.round(roots[(roots>=lo)&(roots<=hi)],4)}",flush=True)

print("\n"+"="*80)
print(" LECTURA: si ξ̂_DH tiene raiz real en ~85.73 PERO L_DH NO tiene cero on-line ahi")
print("   (solo el par off-line) => ξ̂ RELLENA la proyeccion real = Escenario B (ciego).")
print("   Si L_DH tiene un cero on-line en ~85.73 => ξ̂ solo lo reproduce, sin senal.")
print("   Si ξ̂ tiene un GAP donde deberia haber cero => detecta off-line = Escenario A.")
