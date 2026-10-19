# TOOLS_204U_001 (phase 204u), PRED-aP: copy of phase-202 CALIB_001_data/WT_scan.py with family a_P (Lambda*1{p>=P}, prop:shape-eulerdel). aP3 = erases {2}; aP5 = erases {2,3}. NUMERICAL.
# Phase 204n / prop:WT (P47 l.4358): inertia and polar resolvent per sector of the full form in a Legendre block. NUMERICAL (Galerkin, mpmath).
# 𝔄 = C0 c(0)+∫_0^{2T}(c(0)-c(u))K(u)du + c(0)∫_{2T}^∞K − Σ_{log n<2T} v_n c(log n)   (window_bottoms.py / cert_*), without the Tate condition.
# χ_ev = cosh(t/2)1_{I_T}, χ_odd = sinh(t/2)1_{I_T} (P47 subsec:conv); W^par = 𝔄 + 2ε_par ℓ_par², ε_ev=+1, ε_odd=−1.
import mpmath as mp, sys, json, math
from fractions import Fraction as Fr
from multiprocessing import Pool
LQ=json.load(open('/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/LEMMA_E_EPSTEIN_001_data/lambdaQ_exact.json'))
def fam(name):
    if name.startswith('aP'):
        Pthr=int(name[2:])
        def c(n):
            from sympy import factorint
            f=factorint(n); p=list(f)[0]
            return mp.log(p) if (len(f)==1 and p>=Pthr) else mp.mpf(0)
        C0=-mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi); K=lambda u: 1/(2*mp.sinh(u/2))+1/(2*mp.cosh(u/2))
        tail=lambda T: mp.log(mp.coth(T/2))+2*mp.atan(mp.exp(-T)); polar=True
    elif name=='zeta':
        def c(n):
            from sympy import factorint
            f=factorint(n); return mp.log(list(f)[0]) if len(f)==1 else mp.mpf(0)
        C0=-mp.euler-mp.pi/2-3*mp.log(2)-mp.log(mp.pi); K=lambda u: 1/(2*mp.sinh(u/2))+1/(2*mp.cosh(u/2))
        tail=lambda T: mp.log(mp.coth(T/2))+2*mp.atan(mp.exp(-T)); polar=True
    elif name=='epstein':
        def c(n):
            d=LQ.get(str(n)); return mp.fsum(mp.mpf(Fr(q).numerator)/Fr(q).denominator*mp.log(int(p)) for p,q in d.items()) if d else mp.mpf(0)
        C0=mp.log(20)-2*mp.euler-6*mp.log(2)-2*mp.log(mp.pi); K=lambda u: 1/mp.sinh(u/2); tail=lambda T: 2*mp.log(mp.coth(T/2)); polar=True
    else:
        s5=mp.sqrt(5); kap=(mp.sqrt(10-2*s5)-2)/(s5-1); CH={1:(1,0),2:(0,1),3:(0,-1),4:(-1,0),0:(0,0)}
        a=lambda n: CH[n%5][0]+kap*CH[n%5][1]; B={}
        def c(n):
            for m in range(2,n+1):
                if m not in B: B[m]=a(m)*mp.log(m)-mp.fsum(a(d)*B[m//d] for d in range(2,m) if m%d==0)
            return B[n]
        C0=mp.log(5/mp.pi)+mp.digamma(mp.mpf(3)/4); K=lambda u: 1/(2*mp.sinh(u/2))-1/(2*mp.cosh(u/2))
        tail=lambda T: mp.log(mp.coth(T/2))-2*mp.atan(mp.exp(-T)); polar=False
    return c,C0,K,tail,polar
def run(args):
    name,Ts,T,M=args; mp.mp.dps=40; c,C0,K,tail,polar=fam(name)
    tx,tw=mp.gauss_quadrature(M+2,'legendre') if hasattr(mp,'gauss_quadrature') else (None,None)
    import numpy as np
    xs,ws=np.polynomial.legendre.leggauss(M+2)  # nodes in double are enough? use mp refinement below
    def gl(n):
        X=[];Wt=[]
        for k in range(1,n+1):
            x=mp.cos(mp.pi*(k-mp.mpf(1)/4)/(n+mp.mpf(1)/2))
            for _ in range(60):
                p0,p1=mp.mpf(1),x
                for j in range(2,n+1): p0,p1=p1,((2*j-1)*x*p1-(j-1)*p0)/j
                dp=n*(x*p1-p0)/(x*x-1); dx=p1/dp; x-=dx
                if abs(dx)<mp.mpf(10)**(-35): break
            p0,p1=mp.mpf(1),x
            for j in range(2,n+1): p0,p1=p1,((2*j-1)*x*p1-(j-1)*p0)/j
            dp=n*(x*p1-p0)/(x*x-1); X.append(x); Wt.append(2/((1-x*x)*dp*dp))
        return X,Wt
    tx,tw=gl(M+2); ux,uw=gl(80)
    def leg(x):
        P=[mp.mpf(1),x]
        for j in range(2,M): P.append(((2*j-1)*x*P[-1]-(j-1)*P[-2])/j)
        return P[:M]
    def cmat(u):
        a,b=-T+u,T; C=mp.zeros(M,M)
        for x,w in zip(tx,tw):
            t=(a+b)/2+(b-a)/2*x; Pj=leg(t/T); Pk=leg((t-u)/T); ww=w*(b-a)/2
            for j in range(M):
                if (j%2)!=0 and False: pass
                for k in range(M): C[j,k]+=ww*Pj[j]*Pk[k]
        return (C+C.T)/2
    C0m=cmat(mp.mpf(0)); G=C0m*(C0+tail(T))
    for x,w in zip(ux,uw):
        u=T*(1+x); G+=(C0m-cmat(u))*(K(u)*w*T)
    n=2
    while mp.log(n)<2*T:
        cn=c(n)
        if cn!=0: G-=cmat(mp.log(n))*(2*cn/mp.sqrt(n))
        n+=1
    lev=mp.matrix([sum(w*leg(x)[j]*mp.cosh(T*x/2) for x,w in zip(tx,tw))*T for j in range(M)])
    lod=mp.matrix([sum(w*leg(x)[j]*mp.sinh(T*x/2) for x,w in zip(tx,tw))*T for j in range(M)])
    res={'family':name,'T':Ts,'M':M,'polar':polar}
    for par,idx,chi,eps in (('ev',[j for j in range(M) if j%2==0],lev,1),('odd',[j for j in range(M) if j%2==1],lod,-1)):
        k=len(idx); A=mp.matrix(k,k); Ms=mp.matrix(k,k); ch=mp.matrix(k,1)
        for i,a_ in enumerate(idx):
            ch[i]=chi[a_]; Ms[i,i]=2*T/(2*a_+1)
            for j,b_ in enumerate(idx): A[i,j]=G[a_,b_]
        L=mp.cholesky(Ms); Li=L**-1; H=Li*A*Li.T; H=(H+H.T)/2; E=mp.eigsy(H)[0]
        np_=sum(1 for e in E if e>0); nm=sum(1 for e in E if e<0)
        q=(ch.T*(mp.lu_solve(A,ch)))[0]
        Wm=A+2*eps*(ch*ch.T); HW=Li*Wm*Li.T; HW=(HW+HW.T)/2; EW=mp.eigsy(HW)[0]
        d={'n+':np_,'n-':nm,'eig_min_A':mp.nstr(min(E),12),'eig_max_A':mp.nstr(max(E),12),'q':mp.nstr(q,20),
           'q+1/2' if par=='ev' else '1/2-q':mp.nstr(q+mp.mpf(1)/2 if par=='ev' else mp.mpf(1)/2-q,12),
           'lamW_par':mp.nstr(min(EW),12),'eigA_low':[mp.nstr(e,8) for e in sorted(E)[:6]],'nW-':sum(1 for e in EW if e<0)}
        res[par]=d
    print(json.dumps(res),flush=True); return res
if __name__=='__main__':
    import sys
    Ms=[int(x) for x in sys.argv[1].split(',')]
    jobs=[]
    for M in Ms:
        for Ts in ['1/2log3','1','1/2log5','2','2.5','3']:
            T=mp.log(int(Ts.split('log')[1]))/2 if 'log' in Ts else mp.mpf(Ts)
            for nm in ('aP3','aP5','zeta'): jobs.append((nm,Ts,T,M))
    with Pool(min(len(jobs),36)) as P: R=P.map(run,jobs)
    json.dump(R,open('aP_scan_M'+sys.argv[1].replace(',','_')+'.json','w'),indent=1)
