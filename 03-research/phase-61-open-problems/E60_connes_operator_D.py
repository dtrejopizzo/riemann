"""
CONSTRUIR el operador de escala de Connes D_{λ,N} (CCM Prop 3.21) en el modelo finito.
  D_log = generador de escala, diagonal: D_log V_n = k_n V_n, k_n = 2 pi n / L (frecuencia).
  ξ = ground state de QW_λ=A (E57).  δ_N = (1/√L) Σ_n V_n (Dirichlet kernel) = coef 1/√L.
  D_{λ,N} = D_log − |D_log ξ⟩⟨δ_N|   (perturbacion rango 1).
Verificar (Thm 1.1):
  (i) D_{λ,N} ξ = 0 (constraint).  (ii) self-adjoint respecto de ⟨,⟩_A = A − μ_0 I.
  (iii) autovalores REALES (= ceros on-line), comparar con γ_1=14.13, γ_2=21.02, γ_3=25.01.
Es el 'Frobenius para Z': self-adjoint /QW_λ <=> autovalores reales <=> RH a nivel λ.
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

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2); dim=2*N+1; idx=list(range(-N,N+1))
    A=polemat(L,N)-archmat(L,N,True,LOG4PI+GAMMA)-primemat_all(L,N,vm_zeta(mx))
    E,V=mp.eigsy(A); g0=min(range(dim),key=lambda i:E[i]); mu0=E[g0]
    xi=mp.matrix([V[r,g0] for r in range(dim)])
    # D_log diagonal k_n=2 pi n/L
    kn=[2*mp.pi*idx[a]/L for a in range(dim)]
    Dlog=mp.zeros(dim)
    for a in range(dim): Dlog[a,a]=kn[a]
    # delta_N = (1/sqrt L) sum V_n => coef vector all 1/sqrt(L)
    dN=mp.matrix([1/mp.sqrt(L) for _ in range(dim)])
    Dxi=Dlog*xi
    # normalizar para constraint <dN|xi>=1: D = Dlog - |Dxi><dN| / <dN|xi>
    ip=sum(dN[a]*xi[a] for a in range(dim))
    D=Dlog.copy()
    for a in range(dim):
        for b in range(dim):
            D[a,b]-=Dxi[a]*dN[b]/ip
    print(f"\n=== Connes D_{{λ,N}}  zeta lambda={lam} N={N} dim={dim} ===")
    print(f"  μ_0(ground)={mp.nstr(mu0,3)}  <δ_N|ξ>={mp.nstr(ip,4)}")
    # (i) D xi = 0 ?
    Dxi_check=D*xi; nrm=max(abs(Dxi_check[a]) for a in range(dim))
    print(f"  (i)  D ξ = 0 ? max|Dξ| = {mp.nstr(nrm,3)}  => {'OK' if nrm<1e-10 else 'no'}")
    # (ii) self-adjoint /<,>_A con A_form=A-mu0 I:  D^H A_form == A_form D ?
    Af=A.copy()
    for a in range(dim): Af[a,a]-=mu0
    M=D.T*Af-Af*D
    sa=max(abs(M[a,b]) for a in range(dim) for b in range(dim))
    print(f"  (ii) self-adjoint /⟨,⟩_A ? max|D^T A_f − A_f D| = {mp.nstr(sa,3)}")
    # (iii) autovalores de D (reales?), comparar con gammas
    ev=mp.eig(D,left=False,right=False)
    evs=sorted([e for e in ev], key=lambda z: abs(z))
    maximag=max(abs(mp.im(e)) for e in ev)
    pos=sorted(set(round(float(mp.re(e)),3) for e in ev if mp.re(e)>0.5))
    print(f"  (iii) autovalores de D: max|Im|={mp.nstr(maximag,3)} (=>{'REALES' if maximag<1e-6 else 'complejos'})")
    print(f"       Re>0 (deberian ~ γ_1=14.13, γ_2=21.02, γ_3=25.01): {pos[:6]}")

run('7.0',12)
run('9.0',14)
