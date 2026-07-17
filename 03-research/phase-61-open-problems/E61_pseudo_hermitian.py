"""
OPCION A — pseudo-Hermiticity / Herglotz. D_{λ,N}=D_log−|D_log ξ><δ_N| es perturbacion RANGO 1
de D_log (real, diagonal, k_n=2πn/L). Autovalores = raices de la ecuacion secular
   1 = Σ_n r_n/(z − k_n),   r_n = (D_log ξ)_n (δ_N)_n   (residuos).
TEOREMA (Herglotz/Pick): si todos los r_n tienen el MISMO signo, Σ r_n/(z−k_n) es monotona
entre polos consecutivos => exactamente una raiz real por hueco => TODO EL ESPECTRO REAL.
=> reality (ceros on-line) <= residuos mismo signo. Mecanismo Hilbert-Polya CONCRETO.
Tests:
 (1) patron de signo de ξ_n (¿estado base de signo definido / Perron?).
 (2) patron de signo de los residuos r_n. ¿Mismo signo (=> real)? Si no, ¿que estructura?
 (3) ¿la condicion 'r_n mismo signo' se sigue de ξ par + algo, SIN usar A⪰0? (no-circularidad)
 (4) falsador DH: residuos de signo mezclado => espectro complejo (off-line).
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

def run(lam,N,kind):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2); dim=2*N+1; idx=list(range(-N,N+1))
    even=(kind=='zeta'); C=LOG4PI+GAMMA+(0 if kind=='zeta' else LOG5)
    Pp=polemat(L,N) if kind=='zeta' else mp.zeros(dim)
    Lam=vm_zeta(mx) if kind=='zeta' else vm_DH(mx)
    A=Pp-archmat(L,N,even,C)-primemat_all(L,N,Lam)
    E,V=mp.eigsy(A); g0=min(range(dim),key=lambda i:E[i])
    xi=[V[r,g0] for r in range(dim)]
    kn=[2*mp.pi*idx[a]/L for a in range(dim)]
    dN=[1/mp.sqrt(L) for _ in range(dim)]
    # residuos r_n = (D_log xi)_n (delta_N)_n = k_n xi_n / sqrt(L)
    r=[kn[a]*xi[a]*dN[a] for a in range(dim)]
    # signos
    sx=[ (1 if xi[a]>1e-15 else (-1 if xi[a]<-1e-15 else 0)) for a in range(dim)]
    sr=[ (1 if r[a]>1e-18 else (-1 if r[a]<-1e-18 else 0)) for a in range(dim)]
    npos=sum(1 for s in sr if s>0); nneg=sum(1 for s in sr if s<0); nz=sum(1 for s in sr if s==0)
    print(f"\n=== OPCION A pseudo-Herm  {kind} lambda={lam} N={N} ===")
    print(f"  (1) ξ_n signo (n=-N..N): {''.join('+' if s>0 else ('-' if s<0 else '0') for s in sx)}")
    # ξ par => xi_n=xi_{-n}; con k_n=2πn/L (impar en n), r_n=k_n xi_n es IMPAR => r_n=-r_{-n}.
    print(f"  (2) r_n signo:           {''.join('+' if s>0 else ('-' if s<0 else '0') for s in sr)}")
    print(f"      residuos: {npos}+ {nneg}- {nz}0   => {'MISMO signo (Herglotz=>REAL)' if npos==0 or nneg==0 else 'signo MEZCLADO'}")
    # como r es impar (r_n=-r_{-n}) por ξ par, nunca puede ser 'mismo signo' globalmente.
    # PERO el problema se desdobla: para n>0 todos + y n<0 todos - ? eso es la estructura correcta.
    rpos=[sr[a] for a in range(dim) if idx[a]>0]; rneg=[sr[a] for a in range(dim) if idx[a]<0]
    half_consistent = (all(s>=0 for s in rpos) and all(s<=0 for s in rneg)) or (all(s<=0 for s in rpos) and all(s>=0 for s in rneg))
    print(f"      n>0: {''.join('+' if s>0 else('-' if s<0 else '0') for s in rpos)}   n<0: {''.join('+' if s>0 else('-' if s<0 else '0') for s in rneg)}")
    print(f"      => residuos de signo DEFINIDO en cada mitad (r_n=k_n ξ_n, ξ par)? {half_consistent}")
    print(f"         {'=> Herglotz por mitades: ξ_n>0 ∀n (estado base Perron) => espectro REAL' if half_consistent else '=> signo mezclado dentro de una mitad => raices complejas posibles'}")
    # (3) la condicion se reduce a: ξ_n > 0 para todo n (estado base de signo unico).
    xi_single = (all(x>=-1e-15 for x in xi) or all(x<=1e-15 for x in xi))
    print(f"  (3) ξ_n de signo UNICO (Perron, => r mismo signo por mitad => REAL)? {xi_single}")
    print(f"      NO-CIRCULARIDAD: reality <= 'ξ_n signo unico'. ¿Se prueba ξ_n>0 sin asumir A⪰0?")
    print(f"      (ground state de signo unico = Perron-Frobenius si A-cI tiene off-diag <=0; a verificar)")

run('7.0',12,'zeta')
run('7.0',12,'DH')
