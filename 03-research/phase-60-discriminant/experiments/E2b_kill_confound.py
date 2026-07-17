#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — Discriminante.  E2b: matar el confound de E2 antes de cantar GO.
#
# E2 dio ζ a +30..41σ de shuffle/random. SOSPECHA: shuffle/random rompen la correlacion
# posicion(log n)<->valor, asi que la separacion puede ser "suma COHERENTE (suave en log n)
# vs INCOHERENTE", NO multiplicatividad. Λ(n)=log p es trivialmente suave en log n.
#
# CONTROL DECISIVO (suave pero NO-multiplicativo, mismo soporte/magnitud):
#   flat   : c(n) = media(Λ)  (constante en potencias de primo) -- maximamente suave
#   loglin : c(n) = ajuste lineal de Λ vs log n -- suave, no-Euler
#   logn   : c(n) = log n     (suave monotono, no es von Mangoldt de ningun Euler)
# Si ζ NO se separa de estos => la firma es SUAVIDAD/COHERENCIA, no multiplicatividad => NO-GO.
# Si ζ SE separa tambien de estos => la multiplicatividad aporta algo mas que suavidad.
#
# Fix numerico: A es casi-singular sin 1/2pi; usamos pseudo-inversa con corte de rango.
# ======================================================================================
import numpy as np, mpmath as mp
mp.mp.dps = 20

J, SIGMA, T0, X = 12, 1.0, 46.13, 100000
NCTRL = 200

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
    P=np.zeros((J,J),complex)
    Wlist=[wvec(n,J,sigma,T0) for (n,p,lp) in terms]
    for c,w in zip(coeffs,Wlist):
        P+=c*np.outer(w,np.conj(w))
    return np.real((P+P.conj().T)/2)

# precompute W once for speed
print("setup ...", flush=True)
terms=pp_terms(X)
W=np.array([wvec(n,J,SIGMA,T0) for (n,p,lp) in terms])   # (Nterms, J)
def build_P_fast(coeffs):
    # P = sum_k c_k w_k w_k^*  = W^H diag(c) W (real part)
    M = (W.conj().T * coeffs) @ W
    return np.real((M+M.conj().T)/2)

A=build_A(J,SIGMA,T0)
wA,VA=np.linalg.eigh(A)
print(f"  A eigenvalues: {np.array2string(wA, precision=3, max_line_width=120)}")
# robust A^{-1/2} via rank cutoff (drop modes below tol*max)
tol=1e-8*wA.max()
keep = wA>tol
print(f"  A: keeping {keep.sum()}/{J} modes above tol={tol:.2e}  (min kept={wA[keep].min():.3e})")
Ainv2 = VA[:,keep] @ np.diag(wA[keep]**-0.5) @ VA[:,keep].T
def carleson_C(P):
    M=Ainv2@P@Ainv2; M=(M+M.T)/2
    return np.linalg.eigvalsh(M)[-1]

sqrtn=np.array([np.sqrt(n) for (n,p,lp) in terms])
logn =np.array([np.log(n) for (n,p,lp) in terms])
Lam  =np.array([lp for (n,p,lp) in terms])
base_zeta = Lam/sqrtn

Cz=carleson_C(build_P_fast(base_zeta))
print(f"\n[REAL] zeta (multiplicativo): C={Cz:.4f}")

# smooth non-multiplicative controls (same support, /sqrt n, magnitude-matched)
mean_target = base_zeta.mean()
flat   = np.full_like(base_zeta, Lam.mean())/sqrtn
# loglin: linear fit of Lam vs logn, then /sqrt n
b1,b0 = np.polyfit(logn, Lam, 1); loglin = (b0+b1*logn)/sqrtn
logn_c = (logn)/sqrtn
# scale smooth controls to same L2 norm as base_zeta (fair magnitude)
def rescale(v): return v*(np.linalg.norm(base_zeta)/np.linalg.norm(v))
flat_s, loglin_s, logn_s = rescale(flat), rescale(loglin), rescale(logn_c)

print("\n SMOOTH non-multiplicative controls (magnitude-matched):")
for name,v in [("flat (const Λ̄)",flat_s),("loglin fit",loglin_s),("logn",logn_s)]:
    C=carleson_C(build_P_fast(v))
    print(f"   {name:18s}: C={C:.4f}   (zeta/this = {Cz/C:.2f}x)")

# incoherent controls
Cs_shuf=[]; Cs_rand=[]
mu,sd=base_zeta.mean(),base_zeta.std()
for s in range(NCTRL):
    rng=np.random.default_rng(s)
    Cs_shuf.append(carleson_C(build_P_fast(base_zeta[rng.permutation(len(base_zeta))])))
    cr=np.clip(rng.normal(mu,sd,len(base_zeta)),0,None)
    Cs_rand.append(carleson_C(build_P_fast(cr)))
Cs_shuf=np.array(Cs_shuf); Cs_rand=np.array(Cs_rand)

print(f"\n incoherent: shuffle C={Cs_shuf.mean():.4f}±{Cs_shuf.std():.4f}   random C={Cs_rand.mean():.4f}±{Cs_rand.std():.4f}")

print("\n"+"="*78); print(" DIAGNOSTICO DEL CONFOUND"); print("="*78)
Cflat=carleson_C(build_P_fast(flat_s)); Cloglin=carleson_C(build_P_fast(loglin_s))
print(f"  zeta C ........... {Cz:.4f}")
print(f"  smooth-nonmult ... flat {Cflat:.4f} | loglin {Cloglin:.4f}   <- son SUAVES y NO multiplicativos")
print(f"  incoherent ....... shuffle {Cs_shuf.mean():.4f} | random {Cs_rand.mean():.4f}")
print()
if Cflat > 0.7*Cz or Cloglin > 0.7*Cz:
    print("  >>> CONFOUND CONFIRMADO: controles SUAVES no-multiplicativos alcanzan C")
    print("      comparable a ζ. La separacion de E2 era SUAVIDAD/COHERENCIA, no")
    print("      multiplicatividad. La firma 'Euler' de E2 es ESPURIA. -> NO-GO parcial.")
else:
    print("  >>> ζ se separa TAMBIEN de los controles suaves no-multiplicativos.")
    print("      La multiplicatividad aporta señal mas alla de la suavidad. -> sigue vivo.")
