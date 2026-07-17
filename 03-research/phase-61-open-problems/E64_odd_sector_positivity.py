"""
ATAQUE DIRECTO a A_impar ⪰ 0 (sector IMPAR, pole-free) — sobreviviente de Opcion B.
En el sector impar NO hay modo n=0/polo, asi que A_impar = -(R + Q)_impar (solo arq+primos).
Por tanto:  A_impar ⪰ 0  <=>  (R+Q)_impar ⪯ 0  = INDICE DE HODGE en el sector pole-free.
Tests (todos zero-independientes, falsador DH):
 (1) firma de R_impar, Q_impar, y (R+Q)_impar.  ¿(R+Q)_impar es EXACTO neg-semidef (como el
     global (0,7,10) de E56)?  Su nucleo = clase 'numericamente trivial' del sector impar.
 (2) ¿el termino ARQUIMEDIANO domina? R_impar ⪯ 0 por si solo y |Q_impar| acotado por |R_impar|
     => A_impar = -R_impar - Q_impar con -R_impar ⪰0 'cubriendo' a Q_impar.  Test: -R_impar ⪰ Q_impar ?
 (3) certificado limpio: Cholesky de A_impar (zeta) debe existir; DH debe fallarlo (1 pivote<0).
 (4) escala: μ_impar vs λ — ¿acotado lejos de 0 (positividad ESTRICTA, no marginal)?
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
def sig(M):
    n=M.rows; H=mp.zeros(n)
    for i in range(n):
        for j in range(n): H[i,j]=(M[i,j]+M[j,i])/2
    E,_=mp.eigsy(H); ev=[E[i] for i in range(n)]
    p=sum(1 for e in ev if e>1e-12); ng=sum(1 for e in ev if e<-1e-12)
    return (p,n-p-ng,ng), min(ev)
def chol_ok(M):
    # Cholesky por pivotes (LDL); devuelve (#pivotes<0, min pivote)
    n=M.rows; A=mp.matrix([[ (M[i,j]+M[j,i])/2 for j in range(n)] for i in range(n)])
    d=[]; L=mp.zeros(n)
    for i in range(n):
        s=A[i,i]-sum(L[i,k]**2*d[k] for k in range(i))
        d.append(s); L[i,i]=1
        if abs(s)<1e-25:
            for j in range(i+1,n): L[j,i]=0
            continue
        for j in range(i+1,n):
            L[j,i]=(A[j,i]-sum(L[j,k]*L[i,k]*d[k] for k in range(i)))/s
    nneg=sum(1 for x in d if x<-1e-14)
    return nneg, min(d)

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2)
    R=archmat(L,N,True,LOG4PI+GAMMA)
    Q=primemat_all(L,N,vm_zeta(mx))
    Bo=parity_proj(N,False)
    Ro=Bo.T*R*Bo; Qo=Bo.T*Q*Bo
    RQo=Ro+Qo                      # = -(A_impar)
    Aimp=-RQo                      # A_impar = -(R+Q)_impar
    print(f"\n=== A_impar (pole-free)  zeta lambda={lam} N={N}  dim_impar={Bo.cols} ===")
    sR,_=sig(Ro); sQ,_=sig(Qo); sRQ,mRQ=sig(RQo); sA,mA=sig(Aimp)
    print(f"  (1) firma  R_impar={sR}   Q_impar={sQ}   (R+Q)_impar={sRQ} (min={mp.nstr(mRQ,3)})")
    print(f"      => A_impar=-(R+Q)_impar firma {sA}  => {'NEG-SEMIDEF exacto (Hodge pole-free)' if sRQ[0]==0 else 'INDEFINIDO'}")
    # (2) domina el arquimediano? -R_impar - Q_impar, con -R_impar como 'capa' positiva
    sNR,mNR=sig(-Ro)
    dom,_=sig(-Ro-Qo)  # = A_impar (mismo); en su lugar test: -R_impar ⪰ Q_impar  <=> -R-Q ⪰0 ya visto
    # mejor: cuanto aporta cada uno al min de A_impar
    _,mNRo=sig(-Ro); _,mNQo=sig(-Qo)
    print(f"  (2) -R_impar firma {sNR} (min={mp.nstr(mNR,3)})  => arq solo {'⪰0' if sNR[2]==0 else 'indef'}; -Q_impar min={mp.nstr(mNQo,3)}")
    # (3) Cholesky limpio
    nneg,mp_=chol_ok(Aimp)
    print(f"  (3) Cholesky A_impar (zeta): #pivotes<0 = {nneg}, min pivote={mp.nstr(mp_,3)}  => {'PSD (certificado)' if nneg==0 else 'FALLA'}")
    return mA

def run_DH(lam,N):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2)
    R=archmat(L,N,False,LOG4PI+GAMMA+LOG5)
    Q=primemat_all(L,N,vm_DH(mx))
    Bo=parity_proj(N,False)
    Aimp=-(Bo.T*R*Bo+Bo.T*Q*Bo)
    sA,mA=sig(Aimp); nneg,mp_=chol_ok(Aimp)
    print(f"  (FALSADOR DH) A_impar firma {sA} min={mp.nstr(mA,3)}  Cholesky #pivotes<0={nneg}  => {'DH FALLA (correcto)' if nneg>0 else 'DH pasa (?!)'}")

print("="*70)
m7=run('7.0',12); run_DH('7.0',12)
m9=run('9.0',12); run_DH('9.0',12)
m12=run('12.0',14)
print(f"\n  (4) ESCALA μ_impar: λ=7→{mp.nstr(m7,3)}  λ=9→{mp.nstr(m9,3)}  λ=12→{mp.nstr(m12,3)}")
print(f"      (¿acotado lejos de 0 => positividad estricta del sector pole-free?)")
