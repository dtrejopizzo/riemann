"""
FASE H1+H2+H3 — realizacion de Abboud sobre Z y ensamble local.
Logica de Hodge index hecha operativa: 𝒫 (polo) tiene rango 2 = plano AMPLE (1,1) (H0/H4).
En la PRIMITIVA = ker(𝒫) (dim 2N-1), A = 𝒫−ℛ−𝒬 = −ℛ−𝒬 = −Σ_v W_v   (𝒫=0 ahi).
Abboud (Thm Big.2, INCONDICIONAL): M̄²·L̄ ≤ 0 por lugar => cada W_v|primitiva ⪯ 0 (neg-semidef).
Si CADA termino local es ⪯0 => suma ⪯0 => A|primitiva ⪰0 => (con el budget ample) A⪰0 = RH.
TEST decisivo (H1): la firma de cada W_v restringido a ker(𝒫):
  W_∞ = ℛ (arquimediano, el lugar sospechoso),  W_p = 𝒬_p (cada primo).
  Abboud predice (0, *, neg) [neg-semidef] para cada uno.
 H2: el ∗ (E52) preserva ker(𝒫) y actua como operador de Weil (∗²=−1) ahi.
 H3: ensamble Σ_v y comparacion con A.  zeta vs DH (falsador).
"""
import mpmath as mp
mp.mp.dps = 30
exec(open('E53_noncircular_gate.py').read().split('def run')[0])  # polemat, archmat, vm_*, primemat-less

def primemat_p(L,N,Lam,p):
    dim=2*N+1; idx=list(range(-N,N+1)); Q=mp.zeros(dim); mx=int(mp.e**L)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0); pw=p
            while pw<=mx:
                if Lam[pw]!=0: s+=Lam[pw]*(mp.mpf(pw)**mp.mpf('-0.5'))*q(mp.log(pw))
                pw*=p
            Q[a,b]=s; Q[b,a]=s
    return Q

def kerP_basis(P,tol=mp.mpf('1e-9')):
    # base ortonormal de ker(P) (autovectores con |autovalor|<tol)
    E,V=mp.eigsy(P); dim=P.rows; cols=[]
    for i in range(dim):
        if abs(E[i])<tol:
            cols.append([V[r,i] for r in range(dim)])
    B=mp.zeros(dim,len(cols))
    for j,c in enumerate(cols):
        for r in range(dim): B[r,j]=c[r]
    return B  # dim x k

def sig_on(M,B):
    # firma de B^T M B (M simetrica real, B columnas ortonormales)
    Mr=B.T*M*B; E,_=mp.eigsy(Mr); ev=[E[i] for i in range(Mr.rows)]
    p=sum(1 for e in ev if e>1e-12); n=sum(1 for e in ev if e<-1e-12)
    return (p, Mr.rows-p-n, n)

def run(lam,N,kind):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2)
    even=(kind=='zeta'); C=LOG4PI+GAMMA+(0 if kind=='zeta' else LOG5)
    P=polemat(L,N) if kind=='zeta' else mp.zeros(2*N+1)
    R=archmat(L,N,even,C)
    Lam=vm_zeta(mx) if kind=='zeta' else vm_DH(mx)
    primes=[p for p in range(2,mx+1) if Lam[p]!=0 and all(p%d for d in range(2,int(p**0.5)+1))]
    Qps={p:primemat_p(L,N,Lam,p) for p in primes}
    Qall=mp.zeros(2*N+1)
    for p in primes: Qall=Qall+Qps[p]
    A=P-R-Qall
    print(f"\n=== {kind} lambda={lam} N={N} ===")
    if kind=='zeta':
        B=kerP_basis(P); k=B.cols
        print(f"  primitiva = ker(𝒫): dim {k} (de {2*N+1}); plano ample dim {2*N+1-k}")
    else:
        B=mp.eye(2*N+1); print(f"  DH sin polo: primitiva = todo el espacio (dim {2*N+1})")
    print(f"  H1 — firma de cada termino LOCAL W_v restringido a la primitiva (Abboud predice neg-semidef (0,*,neg)):")
    okall=True
    sR=sig_on(R,B); print(f"     W_∞ = ℛ (arquimediano): {sR}   {'⪯0 OK' if sR[0]==0 else '<-- TIENE DIRECCION + (residual!)'}")
    if sR[0]>0: okall=False
    for p in primes:
        sp=sig_on(Qps[p],B); flag='⪯0 OK' if sp[0]==0 else '<-- +'
        if sp[0]>0: okall=False
        print(f"     W_{p} = 𝒬_{p}: {sp}   {flag}")
    sA=sig_on(A,B)
    print(f"  H3 — A|primitiva = {sA}  (Abboud=>⪰0)  ;  A global firma = {sig(A)}")
    print(f"  VEREDICTO: cada W_v local ⪯0 sobre primitiva? {okall}")
    if okall:
        print(f"     => SUMA ⪯0 => A|primitiva ⪰0 INCONDICIONAL (Abboud por lugar). Cruce local cierra.")
    else:
        print(f"     => algun W_v tiene direccion + en primitiva: la positividad NO es puramente local;")
        print(f"        el residual vive ahi (sospechoso: ℛ, lugar ∞). = donde hace falta cancelacion global.")

run('7.0',9,'zeta')
run('7.0',9,'DH')
