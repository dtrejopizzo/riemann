"""
OPCION B — reduccion por paridad. E59: μ_par/μ_impar≈0.26>0 estable (mismo signo).
Si signo(μ_par)=signo(μ_impar) es ROBUSTO, entonces A⪰0 ⟺ μ_impar≥0, y atacamos solo el
sector impar (sin el modo n=0/polo/marginal). Tests:
 (1) robustez del mismo-signo: agregar un cero OFF-LINE (Q_off, fuerza μ<0). ¿μ_par y μ_impar
     cruzan 0 JUNTOS al subir la intensidad t? Si si => mismo-signo robusto => reduccion valida.
 (2) razon del ratio≈3.8: contribucion del modo n=0 (presente solo en par).
 (3) ¿A_impar tiene certificado mas limpio? Cholesky/rango.
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
def Qoff(L,N,b,g0):
    # contribucion de un cero off-line a altura g0, desviacion b: ∫ q · 4cosh(bu)cos(g0 u) du
    dim=2*N+1; idx=list(range(-N,N+1)); Q=mp.zeros(dim)
    for a in range(dim):
        for c in range(a,dim):
            q=q_kernel(idx[a],idx[c],L)
            v=mp.quad(lambda u:q(u)*4*mp.cosh(b*u)*mp.cos(g0*u),[0,L]); Q[a,c]=v; Q[c,a]=v
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

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2)
    A0=polemat(L,N)-archmat(L,N,True,LOG4PI+GAMMA)-primemat_all(L,N,vm_zeta(mx))
    Be=parity_proj(N,True); Bo=parity_proj(N,False)
    print(f"\n=== OPCION B reduccion paridad  zeta lambda={lam} N={N} ===")
    print(f"  (1) robustez mismo-signo bajo cero OFF-LINE (g0=14, b=0.4), intensidad t:")
    Qo=Qoff(L,N,mp.mpf('0.4'),mp.mpf('14.0'))
    print(f"      t     μ_par        μ_impar      signo(par)=signo(impar)?")
    for t in [mp.mpf(x)/10 for x in [0,5,10,20,40]]:
        A=A0 - t*Qo
        me=mins(A,Be); mo=mins(A,Bo)
        same = (me>0)==(mo>0)
        print(f"     {float(t):.1f}  {mp.nstr(me,4):>11} {mp.nstr(mo,4):>11}   {same}")
    print(f"      => si cruzan 0 JUNTOS, mismo-signo robusto => A⪰0 ⟺ μ_impar≥0 (reduccion vale)")
    # (3) certificado del sector impar
    Aoo=Bo.T*A0*Bo
    E,_=mp.eigsy(Aoo); neg=sum(1 for i in range(Aoo.rows) if E[i]<-1e-14)
    print(f"  (3) A_impar (zeta): dim {Aoo.rows}, #neg={neg}, μ_impar_min={mp.nstr(min(E[i] for i in range(Aoo.rows)),4)}")
    print(f"      A_par incluye modo n=0; A_impar NO. El ratio≈3.8 = exceso de marginalidad del modo n=0.")

run('7.0',12)
run('9.0',12)
