# P2_GAUGE_RADICAL_001: window bottoms λ_A^{(a)}, λ_W^{(a)} in Legendre block (mpmath). NUMÉRICO (Galerkin).
# 𝔞_T(F)=C0 c(0)+∫0^{2T}(c(0)-c(u))K(u)du+c(0)∫_{2T}^∞K - Σ_{log n<2T} v_n c(log n), v_n=2a(n)/√n (CERT_FALSIFIERS_001)
import mpmath as mp, sys, json
mp.mp.dps=int(sys.argv[2]) if len(sys.argv)>2 else 60
mu=int(sys.argv[1]); M=int(sys.argv[3]) if len(sys.argv)>3 else 20
T=mp.log(mu)/2
def vm(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return (p, m==1)
    return (None,False)
def Lam(n):
    p,ok=vm(n); return mp.log(p) if ok else mp.mpf(0)
ns=[n for n in range(2,mu) if Lam(n)>0]   # log n<2T  <=> n<mu
C0=-mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi)
K=lambda u: mp.mpf(1)/(2*mp.sinh(u/2))+mp.mpf(1)/(2*mp.cosh(u/2))
Ktail=mp.log(mp.coth(T/2))+2*mp.atan(mp.exp(-T))
xg,wg=zip(*[(x,w) for x,w in zip(*mp.gauss_legendre_nodes(M+4))]) if False else (None,None)
# Gauss-Legendre nodes
def gl(n):
    xs=[];ws=[]
    for k in range(1,n+1):
        x=mp.cos(mp.pi*(k-mp.mpf(1)/4)/(n+mp.mpf(1)/2))
        for _ in range(100):
            p0,p1=mp.mpf(1),x
            for j in range(2,n+1): p0,p1=p1,((2*j-1)*x*p1-(j-1)*p0)/j
            dp=n*(x*p1-p0)/(x*x-1); dx=p1/dp; x-=dx
            if abs(dx)<mp.mpf(10)**(-mp.mp.dps+5): break
        p0,p1=mp.mpf(1),x
        for j in range(2,n+1): p0,p1=p1,((2*j-1)*x*p1-(j-1)*p0)/j
        dp=n*(x*p1-p0)/(x*x-1); xs.append(x); ws.append(2/((1-x*x)*dp*dp))
    return xs,ws
def leg(x):
    P=[mp.mpf(1),x]
    for j in range(2,M): P.append(((2*j-1)*x*P[-1]-(j-1)*P[-2])/j)
    return P[:M]
tx,tw=gl(M+2)
def cmat(u):  # c_jk(u)=∫_{-T+u}^{T} P_j(t/T)P_k((t-u)/T)dt, symmetrised
    a,b=-T+u,T; C=mp.zeros(M,M)
    for x,w in zip(tx,tw):
        t=(a+b)/2+(b-a)/2*x; Pj=leg(t/T); Pk=leg((t-u)/T); ww=w*(b-a)/2
        for j in range(M):
            for k in range(M): C[j,k]+=ww*Pj[j]*Pk[k]
    return (C+C.T)/2
C0m=cmat(mp.mpf(0))
NU=int(sys.argv[4]) if len(sys.argv)>4 else 80
ux,uw=gl(NU)
arch=C0m*(C0+Ktail)
for x,w in zip(ux,uw):
    u=T*(1+x); arch+= (C0m-cmat(u))*(K(u)*w*T)
comb_atoms={n:cmat(mp.log(n)) for n in ns}
A=mp.matrix([ [sum(w*leg(x)[j]*mp.exp(T*x/2) for x,w in zip(tx,tw))*T for j in range(M)] ]) 
B=mp.matrix([ [sum(w*leg(x)[j]*mp.exp(-T*x/2) for x,w in zip(tx,tw))*T for j in range(M)] ])
Mass=mp.diag([T*2/mp.mpf(2*j+1) for j in range(M)])
def form(coef):
    G=arch.copy()
    for n in ns: G-= comb_atoms[n]*(2*coef(n)/mp.sqrt(n))
    return G
def bottom(G,prim):
    if prim:
        # basis of nullspace of [A;B]
        Q2=mp.matrix([[A[0,0],A[0,1]],[B[0,0],B[0,1]]]); Qi=Q2**-1; Z=mp.zeros(M,M-2)
        for j in range(2,M):
            Z[j,j-2]=1; sol=Qi*mp.matrix([-A[0,j],-B[0,j]]); Z[0,j-2]=sol[0]; Z[1,j-2]=sol[1]
    else: Z=mp.eye(M)
    Gz=Z.T*G*Z; Mz=Z.T*Mass*Z
    L=mp.cholesky(Mz); Li=L**-1; H=Li*Gz*Li.T; H=(H+H.T)/2
    E=mp.eigsy(H)[0]; return min(E)
def p_of(n): return vm(n)[0]
falsif={'Lambda':lambda n:Lam(n),
 '0.9Lambda':lambda n:0.9*Lam(n),'1.1Lambda':lambda n:1.1*Lam(n),'2Lambda':lambda n:2*Lam(n),
 'a_{2}':lambda n:Lam(n)*(p_of(n)!=2),'a_{2,3}':lambda n:Lam(n)*(p_of(n) not in (2,3)),
 'zero comb':lambda n:0,'Lambda-delta_3':lambda n:Lam(n)*(n!=3)}
out={}
for k,f in falsif.items():
    G=form(f); WW=G+ (A.T*B+B.T*A)
    out[k]={'lamA':mp.nstr(bottom(G,True),12),'lamW':mp.nstr(bottom(WW,False),12)}
    print(mu,k,out[k],flush=True)
json.dump(out,open(f'window_bottoms_mu{mu}_M{M}.json','w'),indent=1)
