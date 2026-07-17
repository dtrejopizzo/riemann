"""
FASE G: construccion DIRECTA del objeto de Deninger (2.7) en version finita = detector cuaternionico.
Espacio H = <ceros rho>.  theta = mult por rho (diag).  Omega alternante: empareja rho <-> 1-rho (EF).
* antilineal con *^2=-1: empareja rho <-> conj(rho), signo cuaternionico.
Producto escalar <v,w> = Omega(v, *w).
MECANISMO (exacto): <,> positivo-definido  <=>  1-rho = conj(rho) para todo cero  <=> Re(rho)=1/2 (RH)
   <=>  theta-1/2 antisimetrico respecto de <,> (autovalores imaginarios puros).
Off-line: el cero se desdobla en cuadruple {b+ig, b-ig, 1-b+ig, 1-b-ig}; el companero-EF (1-rho)
   ya NO es el conjugado => Omega(rho,*rho)=Omega(rho, conj(rho)) y conj(rho)!=1-rho => norma=0/colapsa.
Test: ceros de zeta on-line -> Gram PD, theta-1/2 skew. Cuadruple off-line -> Gram NO PD, skew falla.
"""
import mpmath as mp
mp.mp.dps = 30
I=mp.mpc(0,1)

def build_object(zeros):
    # zeros: lista de rho (complejos), CERRADA bajo conjugacion y bajo rho->1-rho.
    n=len(zeros)
    idx={}
    for j,z in enumerate(zeros): idx[(mp.nstr(z.real,18),mp.nstr(z.imag,18))]=j
    def find(z):
        return idx.get((mp.nstr(z.real,18),mp.nstr(z.imag,18)),None)
    # theta
    theta=mp.zeros(n)
    for j,z in enumerate(zeros): theta[j,j]=z
    # Omega alternante: Omega[j,k]=+1 si zeros[k]=1-zeros[j] (j "menor"), -1 al reves
    Om=mp.zeros(n)
    for j,z in enumerate(zeros):
        k=find(1-z)
        if k is not None and k!=j:
            if z.imag>0 or (z.imag==0 and z.real<mp.mpf('0.5')):  # orientacion para antisimetria
                Om[j,k]=1; Om[k,j]=-1
    # * antilineal: *e_j = sgn * e_{conj index}. Empareja j<->conj con *^2=-1.
    #   para par {z, zbar} con Im!=0: *e_z=e_zbar, *e_zbar=-e_z.  (matriz lineal S, * v = S conj(v))
    S=mp.zeros(n)
    done=set()
    for j,z in enumerate(zeros):
        if j in done: continue
        k=find(z.conjugate())
        if k is None:
            # auto-conjugado (Im=0, real): * = i? no cabe en real; lo dejamos como obstruccion (slot real)
            S[j,j]=I  # *e=i e -> *^2=-1 pero rompe realidad (modo central impar)
            done.add(j)
        elif k==j:
            S[j,j]=I; done.add(j)
        else:
            S[j,k]=1; S[k,j]=-1; done.add(j); done.add(k)
    return theta,Om,S,zeros

def gram(Om,S,n):
    # <e_j,e_k> = Omega(e_j, *e_k) = Omega(e_j, S conj(e_k)) = sum_l Om[j,l]*S[l,k]^*?  e_k real -> conj triv
    # *e_k = sum_l S[l,k] e_l  ; Omega(e_j, *e_k)= sum_l S[l,k] Om[j,l]
    G=mp.zeros(n)
    for j in range(n):
        for k in range(n):
            G[j,k]=sum(S[l,k]*Om[j,l] for l in range(n))
    return G

def herm_eigs(G):
    n=G.rows
    # hacer Hermitiana numericamente: H=(G+G^H)/2
    H=mp.zeros(n)
    for i in range(n):
        for j in range(n): H[i,j]=(G[i,j]+mp.conj(G[j,i]))/2
    E,_=mp.eighe(H)
    return [E[i] for i in range(n)]

def skew_algebraic(theta,Om,S,n):
    # NOTA: <(theta-1/2)v,w>+<v,(theta-1/2)w>=0 es AUTOMATICO (theta deriva Omega; prop 2.5
    # de Deninger). NO contiene RH. Lo medimos solo para confirmar que es estructural (=0 siempre).
    G=gram(Om,S,n); T=mp.zeros(n)
    for i in range(n): T[i,i]=theta[i,i]-mp.mpf('0.5')
    M=G*T+T.H*G
    return max(abs(M[i,j]) for i in range(n) for j in range(n))

def report(name,zeros):
    th,Om,S,_=build_object(zeros); n=len(zeros)
    G=gram(Om,S,n); eg=herm_eigs(G)
    npos=sum(1 for e in eg if e>1e-12); nneg=sum(1 for e in eg if e<-1e-12); nz=n-npos-nneg
    sd=skew_algebraic(th,Om,S,n)
    # discriminador REAL: definicion de <,>  +  parte real de theta-1/2 (espectro)
    reparts=sorted(set(mp.nstr(z.real-mp.mpf('0.5'),3) for z in zeros))
    definite = (nneg==0 or npos==0) and nz==0
    minority = min(npos,nneg)   # # autovalores de signo equivocado
    print(f"\n=== {name} (dim {n}) ===")
    print(f"  autovalores de Gram <,>: {[mp.nstr(e,3) for e in eg]}")
    print(f"  firma (pos,0,neg) = ({npos},{nz},{nneg})  => {'DEFINIDA (RH-compatible)' if definite else 'INDEFINIDA (VIOLA RH)'}")
    print(f"  # autovalores de signo equivocado = {minority}  (= 2 x #ceros off-line = kappa)")
    print(f"  espectro de Re(theta-1/2) = {reparts}  (0 <=> Re rho=1/2; !=0 <=> off-line)")
    print(f"  [skew algebraico de theta-1/2 = {mp.nstr(sd,2)} : ESTRUCTURAL (prop 2.5), no contiene RH]")

# (1) ceros de zeta ON-LINE: rho=1/2 +- i gamma  (primeros gammas)
gammas=[mp.mpf('14.134725'),mp.mpf('21.022040'),mp.mpf('25.010858')]
zr=[]
for g in gammas:
    zr.append(mp.mpf('0.5')+I*g); zr.append(mp.mpf('0.5')-I*g)
report("ZETA on-line (Re=1/2)",zr)

# (2) cuadruple OFF-LINE: beta=0.7, gamma=14.13  -> {b+ig,b-ig,1-b+ig,1-b-ig}
b=mp.mpf('0.7'); g=mp.mpf('14.134725')
zo=[b+I*g, b-I*g, (1-b)+I*g, (1-b)-I*g]
report("OFF-LINE quadruple (Re=0.7)",zo)

# (3) mezcla: 2 on-line + 1 cuadruple off-line
report("MIXTA (on-line + 1 off-line quad)", zr+zo)
