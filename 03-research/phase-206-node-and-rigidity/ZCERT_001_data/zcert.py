# ZCERT_001: zero-side certificate of the node. Zeros: arb (python-flint acb.zeta_zeros, certified).
# Z_T(F) = sum_rho Phi_F(rho)^2,  Phi_k(1/2+i g) = T^{-1/2} cos(gT) 2w_k/(w_k^2-g^2)  (closed form, k odd).
# Rigorous lower bound: ball Cholesky of  M_on + L c c^T - eps I  (=> lambda_min(M_on | c^perp) >= eps).
import flint, mpmath as mp, json, sys, math
from flint import arb, arb_mat, acb
T0=arb('6.289836')
def NT(T): return int(math.ceil(2*T*6.289836/math.pi))-1
_Z={}
def zeros(K,prec):
    if (K,prec) not in _Z:
        flint.ctx.prec=prec; _Z[(K,prec)]=[z.imag for z in acb.zeta_zeros(1,K)]
    return _Z[(K,prec)]
def build(T,ks,K,prec):
    flint.ctx.prec=prec; T=arb(T); w=[arb.pi()*k/(2*T) for k in ks]; s=1/T.sqrt()
    n=len(ks); M=arb_mat(n,n); g=zeros(K,prec)
    for gg in g:
        cg=(gg*T).cos(); v=[s*cg*2*wk/(wk*wk-gg*gg) for wk in w]
        for i in range(n):
            for j in range(i,n): M[i,j]+=2*v[i]*v[j]          # factor 2: rho and rho-bar
    for i in range(n):
        for j in range(i): M[i,j]=M[j,i]
    c=[s*2*wk*(T/2).cosh()/(wk*wk+arb(0.25)) for wk in w]
    return M,c,w
def to_mp(a): return mp.mpf(a.mid().str(mp.mp.dps+5,radius=False))
def lam_num(M,c):
    n=len(c); A=mp.matrix(n,n)
    for i in range(n):
        for j in range(n): A[i,j]=to_mp(M[i,j])
    cv=mp.matrix([to_mp(x) for x in c]); cv=cv/mp.norm(cv)
    # orthonormal basis of c^perp via Householder
    e=mp.matrix(n,1); e[0]=1; u=cv-e if cv[0]<0 else cv+e; u=u/mp.norm(u)
    H=mp.eye(n)-2*u*u.T; B=H[:,1:n] if n>1 else None
    P=B.T*A*B; return min(mp.eigsy(P)[0])
def chol_ok(A):
    n=A.nrows(); L=[[arb(0)]*n for _ in range(n)]
    for j in range(n):
        d=A[j,j]-sum((L[j][k]*L[j][k] for k in range(j)),arb(0))
        if not d>0: return False
        L[j][j]=d.sqrt()
        for i in range(j+1,n): L[i][j]=(A[i,j]-sum((L[i][k]*L[j][k] for k in range(j)),arb(0)))/L[j][j]
    return True
def certify(M,c,mu):
    n=len(c); cc=sum((x*x for x in c),arb(0)); tr=sum((M[i,i] for i in range(n)),arb(0))
    for Lf in [1e2,1e6,1e12,1e24,1e48]:
        eps=arb(mp.nstr(mu*mp.mpf('0.999'),30))
        A=arb_mat(n,n)
        for i in range(n):
            for j in range(n): A[i,j]=M[i,j]+arb(Lf)*tr/cc*c[i]*c[j]-(eps if i==j else 0)
        if chol_ok(A): return eps
    return None
def tau(T,ks,H=3e12):
    # sum_{|g|>H} |Phi_F|^2 <= |x|^2 e^T/T sum_k 4w_k^2 /(H^2-1/4-wmax^2)^2-scaled; int dN/t^4 <= 4(logH/(3H^3)+1/(9H^3)), N(t)<=(t/2pi) log t for t>=H (Trudgian 2014, CITED)
    w=[math.pi*k/(2*T) for k in ks]; wm=max(w)
    S=2*4/(2*math.pi)*(math.log(H)/(3*H**3)+1/(9*H**3))*(H*H/(H*H-0.25-wm*wm))**2
    return math.exp(T)/T*sum(4*x*x for x in w)*S
if __name__=='__main__':
    out={}
    Ts=[('½log5',math.log(5)/2),('1',1.0),('½log15',math.log(15)/2),('2',2.),('2.5',2.5),('3',3.),('4',4.),('5',5.),('6',6.),('8',8.)]
    mult=[1,2,4] if len(sys.argv)<2 else [int(a) for a in sys.argv[1:]]
    for name,T in Ts:
        N=NT(T)
        for m in mult:
            ks=list(range(1,m*N+1,2))
            if len(ks)<2: continue
            prec=max(300,int(60*T*m)+300); mp.mp.dps=int(prec*0.30)
            row={}
            for K in [500,1000,2000]:
                M,c,w=build(T,ks,K,prec); row[K]=lam_num(M,c)
            mu=row[2000]; eps=certify(M,c,mu) if mu>0 else None
            ta=tau(T,ks)
            r=dict(T=T,N=N,mult=m,dim=len(ks)-1,mu={K:mp.nstr(v,12) for K,v in row.items()},
                   cert=(eps.mid().str(8,radius=False) if eps is not None else None),tau=ta,
                   node=(eps is not None and eps>arb(ta)))
            print(name,r,flush=True); out[f'{name}|{m}N']=r
    json.dump(out,open('zcert_results%s.json'%('' if len(sys.argv)<2 else '_'+'_'.join(sys.argv[1:])),'w'),indent=1,ensure_ascii=False)
