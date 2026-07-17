"""
OPCION C — Hodge-Riemann via ∗. Para H¹ (peso 1) la 2da relacion bilineal de Riemann:
  h(v,w) = −A(v,∗w)  debe ser Hermitiana POSITIVA-definida en la primitiva (∗=operador de Weil).
TEST DE NO-CIRCULARIDAD decisivo: ¿la positividad de h es ALGEBRAICA (se sigue de ∗²=−1 + Ω,
para CUALQUIER forma) o necesita que A sea aritmetica especial (=positividad disfrazada)?
 (1) construir h(v,w)=−A(v,∗w) para zeta; firma en primitiva. ¿Definida?
 (2) CONTROL: M aleatoria real-simetrica; h_M(v,w)=−M(v,∗w). ¿h_M definida?
     Si h_M aleatoria es indefinida => HR positividad NO algebraica => necesita A => circular.
     Si h_M aleatoria siempre definida => HR positividad algebraica (de ∗) => CRUCE.
 (3) falsador DH.
"""
import mpmath as mp, random
mp.mp.dps = 30
exec(open('E53_noncircular_gate.py').read().split('def run')[0])
I=mp.mpc(0,1)

def primemat_all(L,N,Lam):
    dim=2*N+1; idx=list(range(-N,N+1)); Q=mp.zeros(dim); mx=int(mp.e**L)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0)
            for k in range(2,mx+1):
                if Lam[k]!=0: s+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
            Q[a,b]=s; Q[b,a]=s
    return Q
def star_matrix(N):
    dim=2*N+1; idx=list(range(-N,N+1)); Sst=mp.zeros(dim)
    for a in range(dim):
        n=idx[a]; sg=mp.mpf(0 if n==0 else (1 if n>0 else -1)); Sst[idx.index(-n),a]=I*sg
    return Sst
def sig_herm(M):
    n=M.rows; H=mp.zeros(n)
    for i in range(n):
        for j in range(n): H[i,j]=(M[i,j]+mp.conj(M[j,i]))/2
    E,_=mp.eighe(H); ev=[E[i] for i in range(n)]
    p=sum(1 for e in ev if e>1e-12); ng=sum(1 for e in ev if e<-1e-12)
    return (p,n-p-ng,ng)

def hform(M,Sst):
    # h(v,w) = -A(v,∗w) = -(M Sst conj)?  En coords: ∗w = Sst conj(w). h_{ab}= -(M Sst)_{ab} (con conj implicito en sesquilinealidad)
    # Construimos la matriz Hermitiana H = -(M @ Sst) y la simetrizamos Herm.
    return -(M*Sst)

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2); dim=2*N+1
    A=polemat(L,N)-archmat(L,N,True,LOG4PI+GAMMA)-primemat_all(L,N,vm_zeta(mx))
    Sst=star_matrix(N)
    print(f"\n=== OPCION C Hodge-Riemann via ∗  zeta lambda={lam} N={N} ===")
    h=hform(A,Sst); print(f"  (1) h=−A∗ (zeta): firma Herm {sig_herm(h)}   A firma {sig_herm(A)}")
    # control aleatorio
    print(f"  (2) CONTROL no-circularidad: M aleatoria real-sim, h_M=−M∗, firma:")
    inds=0
    for seed in range(5):
        random.seed(seed); M=mp.zeros(dim)
        for i in range(dim):
            for j in range(i,dim):
                v=mp.mpf(random.gauss(0,1)); M[i,j]=v; M[j,i]=v
        s=sig_herm(hform(M,Sst))
        if s[0]>0 and s[2]>0: inds+=1
        print(f"      seed {seed}: {s}")
    print(f"      => {inds}/5 aleatorias INDEFINIDAS. {'HR positividad NO algebraica (necesita A) => circular' if inds>=3 else 'h_M tiende a definida => HR algebraica?? revisar'}")

run('7.0',12)
