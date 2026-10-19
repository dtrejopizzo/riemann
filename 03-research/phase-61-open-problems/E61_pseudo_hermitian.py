"""
OPTION A — pseudo-Hermiticity / Herglotz. D_{λ,N}=D_log−|D_log ξ><δ_N| is a RANK-1 perturbation
of D_log (real, diagonal, k_n=2πn/L). Eigenvalues = roots of the secular equation
   1 = Σ_n r_n/(z − k_n),   r_n = (D_log ξ)_n (δ_N)_n   (residues).
THEOREM (Herglotz/Pick): if all the r_n have the SAME sign, Σ r_n/(z−k_n) is monotone
between consecutive poles => exactly one real root per gap => THE WHOLE SPECTRUM IS REAL.
=> reality (on-line zeros) <= residues of the same sign. CONCRETE Hilbert-Polya mechanism.
Tests:
 (1) sign pattern of ξ_n (is the ground state of definite sign / Perron?).
 (2) sign pattern of the residues r_n. Same sign (=> real)? If not, what structure?
 (3) does the condition 'r_n same sign' follow from ξ even + something, WITHOUT using A⪰0? (non-circularity)
 (4) DH falsifier: mixed-sign residues => complex spectrum (off-line).
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
    # residues r_n = (D_log xi)_n (delta_N)_n = k_n xi_n / sqrt(L)
    r=[kn[a]*xi[a]*dN[a] for a in range(dim)]
    # signs
    sx=[ (1 if xi[a]>1e-15 else (-1 if xi[a]<-1e-15 else 0)) for a in range(dim)]
    sr=[ (1 if r[a]>1e-18 else (-1 if r[a]<-1e-18 else 0)) for a in range(dim)]
    npos=sum(1 for s in sr if s>0); nneg=sum(1 for s in sr if s<0); nz=sum(1 for s in sr if s==0)
    print(f"\n=== OPTION A pseudo-Herm  {kind} lambda={lam} N={N} ===")
    print(f"  (1) ξ_n sign (n=-N..N): {''.join('+' if s>0 else ('-' if s<0 else '0') for s in sx)}")
    # ξ even => xi_n=xi_{-n}; with k_n=2πn/L (odd in n), r_n=k_n xi_n is ODD => r_n=-r_{-n}.
    print(f"  (2) r_n sign:           {''.join('+' if s>0 else ('-' if s<0 else '0') for s in sr)}")
    print(f"      residues: {npos}+ {nneg}- {nz}0   => {'SAME sign (Herglotz=>REAL)' if npos==0 or nneg==0 else 'MIXED sign'}")
    # since r is odd (r_n=-r_{-n}) because ξ is even, it can never be 'same sign' globally.
    # BUT the problem splits: for n>0 all + and n<0 all - ? that is the correct structure.
    rpos=[sr[a] for a in range(dim) if idx[a]>0]; rneg=[sr[a] for a in range(dim) if idx[a]<0]
    half_consistent = (all(s>=0 for s in rpos) and all(s<=0 for s in rneg)) or (all(s<=0 for s in rpos) and all(s>=0 for s in rneg))
    print(f"      n>0: {''.join('+' if s>0 else('-' if s<0 else '0') for s in rpos)}   n<0: {''.join('+' if s>0 else('-' if s<0 else '0') for s in rneg)}")
    print(f"      => residues of DEFINITE sign on each half (r_n=k_n ξ_n, ξ even)? {half_consistent}")
    print(f"         {'=> Herglotz by halves: ξ_n>0 ∀n (Perron ground state) => REAL spectrum' if half_consistent else '=> mixed sign within a half => complex roots possible'}")
    # (3) the condition reduces to: ξ_n > 0 for all n (single-sign ground state).
    xi_single = (all(x>=-1e-15 for x in xi) or all(x<=1e-15 for x in xi))
    print(f"  (3) ξ_n of SINGLE sign (Perron, => r same sign per half => REAL)? {xi_single}")
    print(f"      NON-CIRCULARITY: reality <= 'ξ_n single sign'. Is ξ_n>0 proved without assuming A⪰0?")
    print(f"      (single-sign ground state = Perron-Frobenius if A-cI has off-diag <=0; to be verified)")

run('7.0',12,'zeta')
run('7.0',12,'DH')
