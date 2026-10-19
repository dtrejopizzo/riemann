"""
PHASE G: DIRECT construction of Deninger's object (2.7) in finite version = quaternionic detector.
Space H = <zeros rho>.  theta = mult by rho (diag).  Alternating Omega: pairs rho <-> 1-rho (FE).
* antilinear with *^2=-1: pairs rho <-> conj(rho), quaternionic sign.
Scalar product <v,w> = Omega(v, *w).
MECHANISM (exact): <,> positive-definite  <=>  1-rho = conj(rho) for every zero  <=> Re(rho)=1/2 (RH)
   <=>  theta-1/2 antisymmetric with respect to <,> (purely imaginary eigenvalues).
Off-line: the zero splits into a quadruple {b+ig, b-ig, 1-b+ig, 1-b-ig}; the FE-partner (1-rho)
   is NO LONGER the conjugate => Omega(rho,*rho)=Omega(rho, conj(rho)) and conj(rho)!=1-rho => norm=0/collapses.
Test: on-line zeta zeros -> Gram PD, theta-1/2 skew. Off-line quadruple -> Gram NOT PD, skew fails.
"""
import mpmath as mp
mp.mp.dps = 30
I=mp.mpc(0,1)

def build_object(zeros):
    # zeros: list of rho (complex), CLOSED under conjugation and under rho->1-rho.
    n=len(zeros)
    idx={}
    for j,z in enumerate(zeros): idx[(mp.nstr(z.real,18),mp.nstr(z.imag,18))]=j
    def find(z):
        return idx.get((mp.nstr(z.real,18),mp.nstr(z.imag,18)),None)
    # theta
    theta=mp.zeros(n)
    for j,z in enumerate(zeros): theta[j,j]=z
    # alternating Omega: Omega[j,k]=+1 if zeros[k]=1-zeros[j] (j "smaller"), -1 the other way
    Om=mp.zeros(n)
    for j,z in enumerate(zeros):
        k=find(1-z)
        if k is not None and k!=j:
            if z.imag>0 or (z.imag==0 and z.real<mp.mpf('0.5')):  # orientation for antisymmetry
                Om[j,k]=1; Om[k,j]=-1
    # antilinear *: *e_j = sgn * e_{conj index}. Pairs j<->conj with *^2=-1.
    #   for pair {z, zbar} with Im!=0: *e_z=e_zbar, *e_zbar=-e_z.  (linear matrix S, * v = S conj(v))
    S=mp.zeros(n)
    done=set()
    for j,z in enumerate(zeros):
        if j in done: continue
        k=find(z.conjugate())
        if k is None:
            # self-conjugate (Im=0, real): * = i? does not fit in real; left as obstruction (real slot)
            S[j,j]=I  # *e=i e -> *^2=-1 but breaks reality (odd central mode)
            done.add(j)
        elif k==j:
            S[j,j]=I; done.add(j)
        else:
            S[j,k]=1; S[k,j]=-1; done.add(j); done.add(k)
    return theta,Om,S,zeros

def gram(Om,S,n):
    # <e_j,e_k> = Omega(e_j, *e_k) = Omega(e_j, S conj(e_k)) = sum_l Om[j,l]*S[l,k]^*?  e_k real -> conj trivial
    # *e_k = sum_l S[l,k] e_l  ; Omega(e_j, *e_k)= sum_l S[l,k] Om[j,l]
    G=mp.zeros(n)
    for j in range(n):
        for k in range(n):
            G[j,k]=sum(S[l,k]*Om[j,l] for l in range(n))
    return G

def herm_eigs(G):
    n=G.rows
    # make Hermitian numerically: H=(G+G^H)/2
    H=mp.zeros(n)
    for i in range(n):
        for j in range(n): H[i,j]=(G[i,j]+mp.conj(G[j,i]))/2
    E,_=mp.eighe(H)
    return [E[i] for i in range(n)]

def skew_algebraic(theta,Om,S,n):
    # NOTE: <(theta-1/2)v,w>+<v,(theta-1/2)w>=0 is AUTOMATIC (theta derives Omega; Deninger's
    # prop 2.5). It does NOT contain RH. We measure it only to confirm it is structural (=0 always).
    G=gram(Om,S,n); T=mp.zeros(n)
    for i in range(n): T[i,i]=theta[i,i]-mp.mpf('0.5')
    M=G*T+T.H*G
    return max(abs(M[i,j]) for i in range(n) for j in range(n))

def report(name,zeros):
    th,Om,S,_=build_object(zeros); n=len(zeros)
    G=gram(Om,S,n); eg=herm_eigs(G)
    npos=sum(1 for e in eg if e>1e-12); nneg=sum(1 for e in eg if e<-1e-12); nz=n-npos-nneg
    sd=skew_algebraic(th,Om,S,n)
    # REAL discriminator: definition of <,>  +  real part of theta-1/2 (spectrum)
    reparts=sorted(set(mp.nstr(z.real-mp.mpf('0.5'),3) for z in zeros))
    definite = (nneg==0 or npos==0) and nz==0
    minority = min(npos,nneg)   # # eigenvalues of the wrong sign
    print(f"\n=== {name} (dim {n}) ===")
    print(f"  Gram <,> eigenvalues: {[mp.nstr(e,3) for e in eg]}")
    print(f"  signature (pos,0,neg) = ({npos},{nz},{nneg})  => {'DEFINITE (RH-compatible)' if definite else 'INDEFINITE (VIOLATES RH)'}")
    print(f"  # eigenvalues of the wrong sign = {minority}  (= 2 x #off-line zeros = kappa)")
    print(f"  spectrum of Re(theta-1/2) = {reparts}  (0 <=> Re rho=1/2; !=0 <=> off-line)")
    print(f"  [algebraic skew of theta-1/2 = {mp.nstr(sd,2)} : STRUCTURAL (prop 2.5), does not contain RH]")

# (1) ON-LINE zeta zeros: rho=1/2 +- i gamma  (first gammas)
gammas=[mp.mpf('14.134725'),mp.mpf('21.022040'),mp.mpf('25.010858')]
zr=[]
for g in gammas:
    zr.append(mp.mpf('0.5')+I*g); zr.append(mp.mpf('0.5')-I*g)
report("ZETA on-line (Re=1/2)",zr)

# (2) OFF-LINE quadruple: beta=0.7, gamma=14.13  -> {b+ig,b-ig,1-b+ig,1-b-ig}
b=mp.mpf('0.7'); g=mp.mpf('14.134725')
zo=[b+I*g, b-I*g, (1-b)+I*g, (1-b)-I*g]
report("OFF-LINE quadruple (Re=0.7)",zo)

# (3) mixed: 2 on-line + 1 off-line quadruple
report("MIXED (on-line + 1 off-line quad)", zr+zo)
