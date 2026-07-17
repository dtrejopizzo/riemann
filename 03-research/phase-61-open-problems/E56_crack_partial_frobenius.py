"""
GRIETA de H1-H3: ¿factorizacion Gram PARCIAL (Frobenius aproximado) sobre p<λ, y el ∗ (E52)
regulariza hacia positividad? = puente a opcion 2 (Hodge-Riemann via ∗).
Tests sobre la primitiva ker(𝒫):
 (1) Split: firma de Σ_{p<λ}W_p (interior), Σ_{p>λ}W_p (exterior), ℛ (∞). ¿Cual esta cerca de ⪯0?
 (2) ∗-simetrizacion (Hodge-Riemann): A es real-simetrica. Su parte ∗-cuaternionico-Hermitiana
     A_H = (A + S† A S)/2 con S=∗ (E52). ¿A_H es DEFINIDA aun cuando A no lo es localmente?
     Y la forma g(v,w)=Ω(v,∗w): ¿g|primitiva es definida (=2da relacion bilineal de Riemann)?
 (3) Frobenius aproximado: reconstruir el bloque de bajas frecuencias desde p<λ y ver si es Gram (PSD).
"""
import mpmath as mp
mp.mp.dps = 30
exec(open('E53_noncircular_gate.py').read().split('def run')[0])  # polemat, archmat, vm_*, q_kernel
I=mp.mpc(0,1)

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

def star_matrix(N):
    # ∗ V_n = i sgn(n) V_{-n}  (E52). Sst e_n = i sgn(n) e_{-n}; ∗v = Sst conj(v).
    dim=2*N+1; idx=list(range(-N,N+1)); Sst=mp.zeros(dim)
    for a in range(dim):
        n=idx[a]; sg=mp.mpf(0 if n==0 else (1 if n>0 else -1))
        b=idx.index(-n); Sst[b,a]=I*sg
    return Sst

def kerP_basis(P,tol=mp.mpf('1e-9')):
    E,V=mp.eigsy(P); dim=P.rows; cols=[]
    for i in range(dim):
        if abs(E[i])<tol: cols.append([V[r,i] for r in range(dim)])
    B=mp.zeros(dim,len(cols))
    for j,c in enumerate(cols):
        for r in range(dim): B[r,j]=c[r]
    return B

def sig_real(M):
    Mr=(M+M.T)/2; E,_=mp.eigsy(Mr); ev=[E[i] for i in range(Mr.rows)]
    p=sum(1 for e in ev if e>1e-12); n=sum(1 for e in ev if e<-1e-12)
    return (p,Mr.rows-p-n,n)
def sig_on(M,B):
    Mr=B.T*M*B; return sig_real(Mr)
def sig_herm(M,B):
    # M puede ser compleja Hermitiana: B^H M B
    Mr=B.H*M*B; n=Mr.rows
    H=mp.zeros(n)
    for i in range(n):
        for j in range(n): H[i,j]=(Mr[i,j]+mp.conj(Mr[j,i]))/2
    E,_=mp.eighe(H); ev=[E[i] for i in range(n)]
    p=sum(1 for e in ev if e>1e-12); ng=sum(1 for e in ev if e<-1e-12)
    return (p,n-p-ng,ng)

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2); lamf=float(lam)
    P=polemat(L,N); R=archmat(L,N,True,LOG4PI+GAMMA); Lam=vm_zeta(mx)
    primes=[p for p in range(2,mx+1) if Lam[p]!=0 and all(p%d for d in range(2,int(p**0.5)+1))]
    Qin=mp.zeros(2*N+1); Qout=mp.zeros(2*N+1)
    for p in primes:
        Qp=primemat_p(L,N,Lam,p)
        if p<lamf: Qin=Qin+Qp
        else: Qout=Qout+Qp
    A=P-R-Qin-Qout
    B=kerP_basis(P)  # primitiva
    Sst=star_matrix(N)
    print(f"\n=== GRIETA zeta lambda={lam} N={N}; primitiva dim {B.cols} ===")
    print(f"  (1) SPLIT sobre primitiva (Abboud quiere ⪯0):")
    print(f"      W_∞=ℛ        : {sig_on(R,B)}")
    print(f"      Σ_{{p<λ}} W_p  : {sig_on(Qin,B)}   (interior, log p<L/2)")
    print(f"      Σ_{{p>λ}} W_p  : {sig_on(Qout,B)}   (exterior)")
    print(f"      ℛ+Σ_in       : {sig_on(R+Qin,B)}   (∞ + interior)")
    print(f"      ℛ+Σ_all      : {sig_on(R+Qin+Qout,B)}   (= −A|prim, Abboud quiere ⪯0)")
    # (2) ∗-simetrizacion / Hodge-Riemann
    AH=(A+Sst.H*A*Sst)/2   # parte ∗-Hermitiana (cuaternionica)
    print(f"  (2) Hodge-Riemann via ∗:")
    print(f"      A|prim (real)             : {sig_on(A,B)}")
    print(f"      A_H=(A+S†AS)/2 |prim      : {sig_herm(AH,B)}   (parte ∗-cuaternionico-Hermitiana)")
    # g(v,w)=Omega(v,∗w). Tomamos Omega = la parte alternante natural del acoplamiento de paridad.
    # Aqui probamos directamente si ∗ 'endereza': cuantas direcciones negativas de A sobreviven en A_H.
    nA=sig_on(A,B)[2]; nAH=sig_herm(AH,B)[2]
    print(f"      => negativas: A|prim={nA}, A_H|prim={nAH}  {'∗ REGULARIZA (menos neg)' if nAH<nA else ('igual' if nAH==nA else '∗ empeora')}")

run('7.0',9)
run('9.0',9)
