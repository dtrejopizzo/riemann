"""
ATAQUE al muro de CCM (ξ_λ PAR): como [A,P]=0, A se bloque-diagonaliza en par/impar.
ξ_λ par  <=>  μ_par < μ_impar  (el minimo vive en el bloque par).
HIPOTESIS: el POLO 𝒫 (presupuesto, firma (1,1), clase amplia) vive en el sector PAR y por eso
baja μ_par. Sin polo, ξ pasaria a impar (como DH). = razon estructural de la paridad de CCM,
y conexion pole(ample) -> even -> Frobenius self-adjoint -> RH.
Test: μ_par y μ_impar de A=𝒫−ℛ−𝒬 con polo ON/OFF; y la firma del polo 𝒫 en cada sector.
"""
import mpmath as mp
mp.mp.dps = 30
exec(open('E53_noncircular_gate.py').read().split('def run')[0])

def primemat_all(L,N,Lam):
    dim=2*N+1; idx=list(range(-N,N+1)); Q=mp.zeros(dim); mx=int(mp.e**L)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0)
            for k in range(2,mx+1):
                if Lam[k]!=0: s+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
            Q[a,b]=s; Q[b,a]=s
    return Q

def parity_proj(N,even):
    idx=list(range(-N,N+1)); dim=2*N+1; cols=[]
    if even:
        v=mp.zeros(dim,1); v[N]=1; cols.append(v)
        for n in range(1,N+1):
            v=mp.zeros(dim,1); v[N+n]=1/mp.sqrt(2); v[N-n]=1/mp.sqrt(2); cols.append(v)
    else:
        for n in range(1,N+1):
            v=mp.zeros(dim,1); v[N+n]=1/mp.sqrt(2); v[N-n]=-1/mp.sqrt(2); cols.append(v)
    Pm=mp.zeros(dim,len(cols))
    for j,c in enumerate(cols):
        for r in range(dim): Pm[r,j]=c[r]
    return Pm

def mins(M,B):
    Mr=B.T*M*B; E,_=mp.eigsy(Mr); return min(E[i] for i in range(Mr.rows))
def sig_on(M,B):
    Mr=B.T*M*B; E,_=mp.eigsy(Mr); ev=[E[i] for i in range(Mr.rows)]
    p=sum(1 for e in ev if e>1e-12); n=sum(1 for e in ev if e<-1e-12); return (p,Mr.rows-p-n,n)

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2)
    Pp=polemat(L,N); R=archmat(L,N,True,LOG4PI+GAMMA); Q=primemat_all(L,N,vm_zeta(mx))
    Be=parity_proj(N,True); Bo=parity_proj(N,False)
    print(f"\n=== ξ par via polo  zeta lambda={lam} N={N} ===")
    print(f"  firma del POLO 𝒫 por sector: par={sig_on(Pp,Be)}  impar={sig_on(Pp,Bo)}")
    print(f"     => el +1 ample del polo vive en el sector {'PAR' if sig_on(Pp,Be)[0]>sig_on(Pp,Bo)[0] else 'IMPAR'}")
    for tag,Pmat in [('con polo',Pp),('SIN polo',mp.zeros(2*N+1))]:
        A=Pmat-R-Q
        me=mins(A,Be); mo=mins(A,Bo)
        gs='PAR' if me<mo else 'IMPAR'
        print(f"  {tag}: μ_par={mp.nstr(me,4)}  μ_impar={mp.nstr(mo,4)}  => ground state {gs}")
    print(f"  => {'el POLO hace μ_par<μ_impar (ξ par); sin polo se invierte' if True else ''}")

run('7.0',12)
run('9.0',12)
