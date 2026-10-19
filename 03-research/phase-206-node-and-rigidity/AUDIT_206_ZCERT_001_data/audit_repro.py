# Independent reproduction: orthonormal basis of c^perp built in balls via Gram-Schmidt
# over integer vectors, compression P^T M P and ball Cholesky (arb_mat) of P^T M P - eps*G, G = P^T P.
# Also a rigorous UPPER bound for the value of the full form at the minimizing vector (tail K + off-line).
import flint, mpmath as mp, math, sys
from flint import arb, arb_mat, acb
def NT(T): return int(math.ceil(2*T*6.289836/math.pi))-1
def run(Tstr,K=2000,prec=900):
    flint.ctx.prec=prec; mp.mp.dps=int(prec*0.3)
    T=arb(Tstr); ks=list(range(1,NT(float(Tstr))+1,2)); n=len(ks)
    w=[arb.pi()*k/(2*T) for k in ks]; s=1/T.sqrt()
    g=[z.imag for z in acb.zeta_zeros(1,K)]
    M=arb_mat(n,n)
    for gg in g:
        v=[s*(gg*T).cos()*2*wk/(wk*wk-gg*gg) for wk in w]
        for i in range(n):
            for j in range(n): M[i,j]+=2*v[i]*v[j]
    c=[s*2*wk*(T/2).cosh()/(wk*wk+arb('0.25')) for wk in w]
    # basis of c^perp: b_j = c_0 e_j - c_j e_0 (j=1..n-1), exactly orthogonal to c (in balls)
    P=arb_mat(n,n-1)
    for j in range(1,n): P[0,j-1]=c[j]; P[j,j-1]=-c[0]
    PT=P.transpose(); A=PT*M*P; G=PT*P
    Am=mp.matrix([[mp.mpf(A[i,j].mid().str(mp.mp.dps,radius=False)) for j in range(n-1)] for i in range(n-1)])
    Gm=mp.matrix([[mp.mpf(G[i,j].mid().str(mp.mp.dps,radius=False)) for j in range(n-1)] for i in range(n-1)])
    Lg=mp.cholesky(Gm); Li=mp.inverse(Lg); E,V=mp.eigsy(Li*Am*Li.T); i0=min(range(n-1),key=lambda i:E[i]); mu=E[i0]
    eps=arb(mp.nstr(mu*mp.mpf('0.99'),25)); B=A-eps*G
    # ball Cholesky
    ok=True; L=[[arb(0)]*(n-1) for _ in range(n-1)]
    for j in range(n-1):
        d=B[j,j]-sum((L[j][k]**2 for k in range(j)),arb(0))
        if not d>0: ok=False;break
        L[j][j]=d.sqrt()
        for i in range(j+1,n-1): L[i][j]=(B[i,j]-sum((L[i][k]*L[j][k] for k in range(j)),arb(0)))/L[j][j]
    # minimizing vector and upper bound for Z_T(F)/||F||^2
    y=Li.T*V[:,i0]; x=[sum((P[i,j]*arb(mp.nstr(y[j],mp.mp.dps)) for j in range(n-1)),arb(0)) for i in range(n)]
    nx=sum((xi*xi for xi in x),arb(0)); Zon=arb(0)
    for gg in g:
        f=sum((x[i]*2*w[i]/(w[i]*w[i]-gg*gg) for i in range(n)),arb(0)); Zon+=2*s*s*((gg*T).cos()*f)**2
    # tail on the line gamma>gamma_K: |f(g)| <= sum_j 2|S_{2j+1}|/g^{2j+2}, S_m=sum x_k w_k^m (series, w_max<g)
    gK=g[-1].upper(); S=[abs(sum((x[i]*w[i]**(2*j+1) for i in range(n)),arb(0))) for j in range(12)]
    wm=max(w,key=lambda a:a.upper()); q=(wm/arb(gK))**2
    # bound |f(g)| <= (2/g^2)*[sum_{j<12} S_j' g^{-2j} + remainder], remainder via sum|x_k| w_k^{25}/g^{24}/(1-q)
    Rem=sum((abs(x[i])*w[i]**25 for i in range(n)),arb(0))
    # ∑_{g>gK} g^{-p} <= int_{gK}^inf t^{-p} dN, N(t)<=(t/2pi)log t ; dN<=... use p*int N t^{-p-1}: (p/2pi)(log gK/((p-1)gK^{p-1})+1/((p-1)^2 gK^{p-1}))
    def Sp(p): G=arb(gK); return arb(p)/(2*arb.pi())*(G.log()/((p-1)*G**(p-1))+1/((p-1)**2*G**(p-1)))
    # |f|^2 <= (sum a_j g^{-2j-2})^2 ; expand crudely with sup over g>=gK of inner sum times one factor
    inner=sum((2*S[j]/arb(gK)**(2*j) for j in range(12)),arb(0))+2*Rem/arb(gK)**24/(1-q)
    tail=2*s*s*((T).cosh()**0)*inner*inner*Sp(4)  # cos^2<=1 on the line; factor 2: ±gamma
    tau=math.exp(float(Tstr))/float(Tstr)*sum(4*float(wk.mid())**2 for wk in w)*2*4/(2*math.pi)*(math.log(3e12)/(3*(3e12)**3)+1/(9*(3e12)**3))*1.0000001
    up=(Zon+tail)/nx
    print(Tstr,'N',NT(float(Tstr)),'dim',n-1,'mu',mp.nstr(mu,8),'cholOK',ok,'eps',eps.mid().str(6,radius=False),
          'tau %.3e'%tau,'node',ok and float(eps.mid())>tau,'upper(Z_on+tail)/|x|^2',up.upper().str(6,radius=False),'+tau')
for t in sys.argv[1:]: run(t)
