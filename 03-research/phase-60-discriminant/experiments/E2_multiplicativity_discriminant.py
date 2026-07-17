#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — Discriminante.  E2: ¿controla la MULTIPLICATIVIDAD el signo de Weil?
#
# E1 probo que el lado-cero es ciego a multiplicatividad (solo ve ubicacion de ceros).
# La tesis vive en el lado ARITMETICO P (bloque de primos del explicit formula).
#
# BLOQUEO previo (Phase3-results.md): comparar L-funciones reales (ζ vs L(χ4)) esta
# confundido porque tienen factores Γ distintos (a=1/4 vs 3/4) => baselines A distintos,
# y la calibracion absoluta de la normalizacion no esta cerrada (C(ζ)~1.98, factor-2).
#
# APORTE METODOLOGICO (desbloquea el discriminante):
#   Fijar el bloque arquimediano A (el de ζ, a=1/4) y variar SOLO la multiplicatividad
#   de los coeficientes c(n) en el bloque de primos P. La normalizacion desconocida
#   afecta a TODOS los P por igual => se cancela en la comparacion RELATIVA.
#
#   Controles (todos con el MISMO soporte {potencias de primo n<=X} y MISMA A):
#     P_zeta    : c(n)=Λ(n)            (multiplicativo, derivado de Euler)         <- real
#     P_shuffle : exactamente el multiset {Λ(n)} reasignado a posiciones log n
#                 permutadas  (preserva la DISTRIBUCION de valores, rompe la
#                 correlacion aritmetica posicion<->valor)                         <- control
#     P_random  : c(n) iid con misma media/var que Λ(n) en el soporte             <- control
#
# PRE-REGISTRO (00-PLAN §5):
#   GO   : P_zeta se separa de los controles de forma ESTABLE (X, semilla) =>
#          la multiplicatividad deja una firma operatorial. Conjetura + paper.
#   NO-GO: P_zeta cae dentro de la nube de controles => la multiplicatividad NO
#          controla el signo en este observable => registrar NG y cerrar la ruta.
#
# HONESTO: la calibracion ABSOLUTA (C<=1) sigue abierta; aqui se reporta el
# discriminante RELATIVO (ranking/separacion), que es invariante a la normalizacion.
# ======================================================================================
import numpy as np, mpmath as mp
mp.mp.dps = 20
rng_global = np.random.default_rng(12345)

J, SIGMA, T0, X = 12, 1.0, 46.13, 100000
NCTRL = 200   # numero de controles aleatorios/shuffle

def hermite(J,u):
    H=np.zeros((J,len(u))); H[0]=np.pi**-0.25*np.exp(-u**2/2)
    if J>1: H[1]=np.sqrt(2.0)*u*H[0]
    for k in range(2,J): H[k]=np.sqrt(2.0/k)*u*H[k-1]-np.sqrt((k-1.0)/k)*H[k-2]
    return H
def primes_upto(X):
    s=np.ones(X+1,bool); s[:2]=False
    for p in range(2,int(X**0.5)+1):
        if s[p]: s[p*p::p]=False
    return np.nonzero(s)[0]
def pp_terms(X):
    out=[]
    for p in primes_upto(X):
        pk=p; lp=np.log(p)
        while pk<=X: out.append((pk,p,lp)); pk*=p
    return out
def wvec(n,J,sigma,T0):
    x=np.log(n); hk=hermite(J,np.array([sigma*x]))[:,0]
    ik=np.array([(-1j)**k for k in range(J)])
    return ik*hk*np.exp(-1j*T0*x)

def build_A(J,sigma,T0):
    u=np.linspace(-10,10,5000); r=T0+sigma*u; h=hermite(J,u); du=u[1]-u[0]
    a=0.25
    Omega=np.array([float(mp.re(mp.digamma(a+1j*rr/2))) for rr in r])-np.log(np.pi)
    A=np.zeros((J,J))
    for i in range(J):
        for j in range(i,J):
            A[i,j]=np.sum(h[i]*h[j]*Omega)*du*sigma; A[j,i]=A[i,j]
    return A

def build_P(coeffs, terms, J, sigma, T0):
    """coeffs[k] es el c(n)/sqrt(n) para el k-esimo termino (n,p,lp). P = sum c_k w w*."""
    P=np.zeros((J,J),complex)
    for c,(n,p,lp) in zip(coeffs,terms):
        w=wvec(n,J,sigma,T0)
        P+=c*np.outer(w,np.conj(w))
    return np.real((P+P.conj().T)/2)

def carleson(A,P):
    w,V=np.linalg.eigh(A); w=np.maximum(w,1e-12)
    Ainv2=V@np.diag(w**-0.5)@V.T
    M=Ainv2@P@Ainv2; M=(M+M.T)/2
    return np.linalg.eigvalsh(M)[-1], np.linalg.eigvalsh(A-P)[0]

print("building archimedean block A (zeta, a=1/4) ...", flush=True)
A=build_A(J,SIGMA,T0)
terms=pp_terms(X)
sqrtn=np.array([np.sqrt(n) for (n,p,lp) in terms])
Lam=np.array([lp for (n,p,lp) in terms])          # Λ(n) real
base_zeta = Lam/sqrtn                               # c(n)/sqrt(n), multiplicativo

print(f"  J={J}, sigma={SIGMA}, T0={T0}, X={X}, #prime-power terms={len(terms)}")

Cz,lz = carleson(A, build_P(base_zeta, terms, J,SIGMA,T0))
print(f"\n[REAL] zeta (multiplicativo): C={Cz:.4f}   lambda_min(A-P)={lz:+.4e}")
print( "       (C absoluto NO calibrado, ~factor-2 conocido; usamos comparacion RELATIVA)")

# --- controles: misma A, mismo soporte, misma distribucion de |coeff|, sin multiplicatividad ---
mu, sd = base_zeta.mean(), base_zeta.std()
Cs_shuffle, ls_shuffle = [], []
Cs_random,  ls_random  = [], []
for s in range(NCTRL):
    rng = np.random.default_rng(s)
    # shuffle: MISMOS valores, posiciones (log n) permutadas
    perm = rng.permutation(len(base_zeta))
    Csh,lsh = carleson(A, build_P(base_zeta[perm], terms, J,SIGMA,T0))
    Cs_shuffle.append(Csh); ls_shuffle.append(lsh)
    # random: iid gaussiano misma media/var, recortado a >=0 (Λ>=0)
    cr = np.clip(rng.normal(mu,sd,len(base_zeta)),0,None)
    Crd,lrd = carleson(A, build_P(cr, terms, J,SIGMA,T0))
    Cs_random.append(Crd); ls_random.append(lrd)

Cs_shuffle=np.array(Cs_shuffle); Cs_random=np.array(Cs_random)
def z(val, arr): return (val-arr.mean())/arr.std() if arr.std()>0 else float('nan')

print("\n"+"="*78)
print(" DISCRIMINANTE RELATIVO  (C; cuanto sobresale ζ de la nube de controles)")
print("="*78)
print(f"  zeta C                         : {Cz:.4f}")
print(f"  shuffle  (n={NCTRL})  C        : media {Cs_shuffle.mean():.4f}  std {Cs_shuffle.std():.4f}  rango[{Cs_shuffle.min():.3f},{Cs_shuffle.max():.3f}]")
print(f"  random   (n={NCTRL})  C        : media {Cs_random.mean():.4f}  std {Cs_random.std():.4f}  rango[{Cs_random.min():.3f},{Cs_random.max():.3f}]")
print(f"\n  z-score zeta vs shuffle : {z(Cz,Cs_shuffle):+.2f} sigma")
print(f"  z-score zeta vs random  : {z(Cz,Cs_random):+.2f} sigma")
pct_sh = (Cs_shuffle < Cz).mean()*100
pct_rd = (Cs_random  < Cz).mean()*100
print(f"  percentil de zeta en shuffle: {pct_sh:.0f}%   en random: {pct_rd:.0f}%")

print("\n"+"="*78)
print(" VEREDICTO (pre-registrado)")
print("="*78)
zs = abs(z(Cz,Cs_shuffle)); zr = abs(z(Cz,Cs_random))
if zs>3 and zr>3:
    print(" GO: ζ se separa >3σ de AMBOS controles => la multiplicatividad deja firma")
    print("     operatorial estable. Siguiente: estabilidad en X y T0, e identificar el bloque.")
elif zs<1 and zr<1:
    print(" NO-GO: ζ cae DENTRO de la nube de controles (<1σ) => en este observable la")
    print("        multiplicatividad NO controla el signo. Registrar NG, cerrar ruta.")
else:
    print(" PARCIAL: separacion intermedia. Requiere estabilidad (X, T0, semilla) antes de")
    print("          concluir. No reportar como resultado todavia.")
