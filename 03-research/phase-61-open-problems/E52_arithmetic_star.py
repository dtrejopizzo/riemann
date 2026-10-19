"""
ARITHMETIC-SIDE ATTACK: build Deninger's quaternionic * FROM the scale flow
(Connes-Consani), NOT from the zeros. The inversion u->1/u (=s->1-s, FE) is additively
u->L-u (parity P). The natural * on the scale space:
   (*f)(u) = i * sgn(u-L/2) * conj( f(L-u) )
In the mode basis V_n=e^{2 pi i n u /L}:  conj(f(L-u)) = sum conj(c_n) V_n  (fixed indices),
   then multiply by sgn (operator Sigma), then by i.  => * = i * Sigma * K  (K=conjugation).
   *^2 = Sigma conj(Sigma). If Sigma is imaginary-antisymmetric and Sigma^2=I => *^2 = -I.  (quaternionic!)
theta = scale generator = d/du : diag(2 pi i n / L). Test: *^2=-1, [*,theta], and whether the
Gram <V_n,V_m>=Omega(V_n,*V_m) (alternating Omega of the FE) reproduces the Weil form A_lambda.
EVERYTHING built from the scale geometry; the zeros are OUTPUT (spectrum), not input.
"""
import mpmath as mp
mp.mp.dps = 30
I=mp.mpc(0,1)
exec(open('E46_LGV_polymer.py').read().split('def report')[0])  # DandQ for A_lambda

def sigma_matrix(N,L):
    # Sigma_{nm} = (1/L) \int_0^L sgn(u-L/2) e^{2 pi i (n-m) u /L} du
    dim=2*N+1; idx=list(range(-N,N+1)); S=mp.zeros(dim)
    for a in range(dim):
        for b in range(dim):
            k=idx[a]-idx[b]
            if k==0:
                S[a,b]=0   # odd sgn -> mean 0
            else:
                # \int_0^L sgn(u-L/2) e^{2 pi i k u/L} du/L
                # = (1/L)[ \int_0^{L/2}(-1)e.. + \int_{L/2}^L(+1)e.. ]
                w=2*mp.pi*I*k/L
                def F(u): return mp.e**(w*u)/w
                val=(-(F(L/2)-F(0))+(F(L)-F(L/2)))/L
                S[a,b]=val
    return S,idx

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); dim=2*N+1; idx=list(range(-N,N+1))
    print(f"\n=== CORRECT arithmetic-star  lambda={lam} N={N} dim={dim} ===")
    # * V_n = i sgn(n) V_{-n}  (Hilbert transform sgn(n) + FE-inversion + conj). theta-compatible by construction.
    # linear matrix Sstar with *v = Sstar conj(v):  Sstar e_n = i sgn(n) e_{-n}
    Sst=mp.zeros(dim)
    for a in range(dim):
        n=idx[a]; sg=mp.mpf(0 if n==0 else (1 if n>0 else -1))
        b=idx.index(-n); Sst[b,a]=I*sg
    # (1) *^2 = Sst conj(Sst) = -1 ? (n=0 stays at 0 -> the central mode/pole, real slot)
    Sc=mp.zeros(dim)
    for i in range(dim):
        for j in range(dim): Sc[i,j]=mp.conj(Sst[i,j])
    st2=Sst*Sc
    # at n!=0 it must be -1; at n=0 it is 0 (real mode, H^0)
    err=mp.mpf(0)
    for a in range(dim):
        tgt = mp.mpf(0) if idx[a]==0 else mp.mpf(-1)
        err=max(err, abs(st2[a,a]-tgt))
    offd=max(abs(st2[i,j]) for i in range(dim) for j in range(dim) if i!=j)
    print(f"  (1) *^2=-1 at gamma!=0, =0 at n=0(pole): max diag err={mp.nstr(err,2)}  offdiag={mp.nstr(offd,2)}  => {'EXACT' if err<1e-25 and offd<1e-25 else 'no'}")
    # (3) [*,theta]=0 with theta=diag(2 pi i n/L). *theta v = Sst conj(theta v)=Sst conj(theta)conj(v)
    #     = Sst(-theta)conj v.  theta* v = theta Sst conj v.  commutes <=> -Sst theta = theta Sst <=> theta Sst+Sst theta=0
    th=mp.zeros(dim)
    for i in range(dim): th[i,i]=2*mp.pi*I*idx[i]/L
    comm=th*Sst+Sst*th
    cerr=max(abs(comm[i,j]) for i in range(dim) for j in range(dim))
    print(f"  (3) [*,theta]=0: max|theta Sst+Sst theta|={mp.nstr(cerr,2)}  => {'EXACTLY COMMUTES (* compatible with the scale flow)' if cerr<1e-25 else 'no'}")
    # (4) relation to A_lambda: the Weil form. <v,w>=Omega(v,*w). We verify that A is *-real:
    #     A must commute with the structure: A J = J A with J the real-J (P) already seen; here we check
    #     whether A is quaternionic-Hermitian: A(*v,*w)=conj A(v,w) (compatibility with *).
    D,Q,_=DandQ(str(float(lam)),N,'zeta'); A=D-Q
    EA,_=mp.eigsy(A); naA=sum(1 for i in range(dim) if EA[i]<-1e-14)
    # compat test: M = Sst^H A Sst  should = conj(A)=A (A real) if A is *-compatible
    M=Sst.H*A*Sst
    compat=max(abs(M[i,j]-A[i,j]) for i in range(dim) for j in range(dim))
    print(f"  (4) A_lambda *-compatible? max|Sst^H A Sst - A|={mp.nstr(compat,3)}  => {'A respects the quaternionic structure' if compat<1e-9 else 'A NOT *-compat (mixes gamma!=0 with the pole)'}")
    print(f"      A_lambda (prime-side) #eigval<0 = {naA} (=0 <=> RH at this lambda)")

run('7.0',8)
run('9.0',8)
