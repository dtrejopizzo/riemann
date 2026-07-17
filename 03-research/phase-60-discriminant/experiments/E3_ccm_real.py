#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — CCM REAL.  Implementacion honesta del spectral triple H_x (CAND-1).
#
# Todas las versiones connes_hx_*.py de nemotron CALCULAN la von Mangoldt y la DESCARTAN
# (QW = Q_arch*0.5), dando la escalera pelada de D_log, NO los ceros. Aqui implementamos
# la forma documentada (CCM arXiv:2511.22755, Prop 1) que nunca se ejecuto:
#
#   L = 2 log λ ;  base V_n, n=-N..N
#   b_n = (1/L) Σ_{k>=2} Λ(k)/√k · sin(2π k n / L)         [cutoff k <= K]
#   QW_{n,n} = log(λ)/2 ;  QW_{n,m} = (b_n - b_m)/(n-m)    (Cauchy-Toeplitz)
#   minimizador RESTRINGIDO  ξ = QW^{-1} δ / (δ^T QW^{-1} δ)   (Lagrange; el stub usaba
#       el min-eigvector, que es INCORRECTO bajo la restriccion δ_N(ξ)=1)
#   H_x = D_log - |D_log ξ⟩⟨δ_N|   ;  D_log = diag(2π n / L)
#
# GATE (falsable, duro): ¿el espectro de H_x se aproxima a los ceros γ_ρ = 14.13, 21.02,...?
# Si NO para ningun (λ,N,K) razonable -> la forma documentada NO es suficiente / mal leida,
# y hay que traer el paper. Lo reportamos honestamente; no fabricamos coincidencia.
# ======================================================================================
import numpy as np

ZEROS = [14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,43.327073]

def von_mangoldt(K):
    Lam=np.zeros(K+1); s=np.ones(K+1,bool); s[:2]=False
    for p in range(2,int(K**0.5)+1):
        if s[p]: s[p*p::p]=False
    for p in np.nonzero(s)[0]:
        pk=p; lp=np.log(p)
        while pk<=K: Lam[pk]=lp; pk*=p
    return Lam

def build_QW(lam, N, K):
    L=2.0*np.log(lam); n=np.arange(-N,N+1); dim=2*N+1
    Lam=von_mangoldt(K); ks=np.arange(1,K+1); coef=Lam[1:K+1]/np.sqrt(ks)
    # b_n = (1/L) Σ_k coef_k sin(2π k n / L)
    b=np.array([(1.0/L)*np.sum(coef*np.sin(2*np.pi*ks*nn/L)) for nn in n])
    QW=np.zeros((dim,dim))
    for i in range(dim):
        for j in range(dim):
            if i==j: QW[i,j]=np.log(lam)*0.5
            else:    QW[i,j]=(b[i]-b[j])/(n[i]-n[j])
    return (QW+QW.T)/2, L, n

def Hx_spectrum(lam,N,K):
    QW,L,n=build_QW(lam,N,K)
    delta=np.ones(2*N+1)/np.sqrt(L)
    # constrained minimizer xi = QW^{-1} delta / (delta^T QW^{-1} delta)
    try:
        y=np.linalg.solve(QW,delta)
    except np.linalg.LinAlgError:
        y=np.linalg.lstsq(QW,delta,rcond=None)[0]
    denom=delta@y
    if abs(denom)<1e-300: return None
    xi=y/denom
    Dlog=np.diag(2*np.pi*n/L)
    Dxi=Dlog@xi
    Hx=Dlog-np.outer(Dxi,delta)            # rank-1 perturbation
    ev=np.linalg.eigvals(Hx)               # NOT hermitian in general -> eigvals
    return ev

print("="*78)
print(" E3: CCM H_x REAL (forma documentada Cauchy-Toeplitz) vs ceros de zeta")
print("="*78)
print(f" ceros objetivo: {ZEROS[:6]}\n")

best=None
for lam in [2.0,3.0,5.0,7.0,11.0,20.0,50.0]:
    for N in [20,40,80]:
        for K in [int(lam**2), max(50,int(lam**2)), 500, 2000]:
            ev=Hx_spectrum(lam,N,K)
            if ev is None: continue
            # buscar autovalores reales positivos cercanos a ceros
            re=np.sort(ev.real[np.abs(ev.imag)<1e-6])
            pos=re[(re>5)&(re<50)]
            if len(pos)==0: continue
            # distancia del primer "candidato" al primer cero
            d1=np.min(np.abs(pos-ZEROS[0])) if len(pos) else 1e9
            if best is None or d1<best[0]:
                best=(d1,lam,N,K,pos[:6].copy())

print(" Mejor aproximacion encontrada al primer cero (14.1347):")
if best:
    d1,lam,N,K,pos=best
    print(f"   lam={lam}, N={N}, K={K}")
    print(f"   autovalores reales de H_x en (5,50): {np.round(pos,3)}")
    print(f"   |primer candidato - 14.1347| = {d1:.4f}")
else:
    print("   NINGUN autovalor real de H_x cayo en (5,50). La construccion documentada")
    print("   NO reproduce los ceros tal como esta. Hace falta el paper (prolate/scaling).")

print("\n" + "="*78)
print(" Diagnostico adicional: estructura del espectro para lam=5,N=40,K=25")
print("="*78)
ev=Hx_spectrum(5.0,40,25)
re=np.sort(ev.real)
print(f"   #autovalores reales (|im|<1e-6): {np.sum(np.abs(ev.imag)<1e-6)}/{len(ev)}")
print(f"   rango parte real: [{re.min():.2f}, {re.max():.2f}]")
print(f"   espaciado D_log puro 2pi/L = {2*np.pi/(2*np.log(5.0)):.3f}")
print(f"   primeros reales >0: {np.round(re[re>0][:8],3)}")
