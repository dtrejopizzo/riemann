"""
LEMA DE PARIDAD (muro CCM: ξ_λ par). [A,P]=0 => A=A_par ⊕ A_impar. ξ_λ par <=> μ_par<μ_impar.
Pregunta honesta: con polo, μ_par y μ_impar AMBOS ->0 (Cor 2.17). La paridad es razor-thin?
O el RATIO μ_par/μ_impar esta acotado lejos de 1 (statement escala-invariante, mas tratable)?
Test: barrer λ, registrar μ_par, μ_impar, ratio, y la brecha. Si ratio<1 robusto => lema genuino.
Tambien: ¿μ_impar = primer autovalor del sector impar, relacionado al primer cero? estructura.
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
def two_lowest(M,B):
    Mr=B.T*M*B; E,_=mp.eigsy(Mr); ev=sorted(E[i] for i in range(Mr.rows))
    return ev[0],ev[1]

print("=== LEMA DE PARIDAD: μ_par vs μ_impar en rango de λ ===")
print(" λ    N |   μ_par      μ_impar    | ratio par/impar | par<impar? | μ_impar/μ_par")
for lam,N in [('5.0',12),('7.0',12),('9.0',12),('12.0',13),('16.0',14)]:
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2)
    P=polemat(L,N); R=archmat(L,N,True,LOG4PI+GAMMA); Q=primemat_all(L,N,vm_zeta(mx))
    A=P-R-Q
    Be=parity_proj(N,True); Bo=parity_proj(N,False)
    mp_e,_=two_lowest(A,Be); mp_o,mo2=two_lowest(A,Bo)
    ratio=mp_e/mp_o if mp_o!=0 else mp.nan
    inv= mp_o/mp_e if mp_e!=0 else mp.nan
    print(f" {lam:>4} {N:2d} | {mp.nstr(mp_e,4):>10} {mp.nstr(mp_o,4):>10} | {mp.nstr(ratio,4):>13} | {str(mp_e<mp_o):>9} | {mp.nstr(inv,4)}")
print("\n  Lectura: si μ_impar/μ_par ESTABLE >1 (lejos de 1) => paridad robusta escala-invariante (lema genuino).")
print("           si ->1 cuando λ crece => paridad tan delicada como positividad (no separable).")
