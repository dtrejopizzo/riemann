#!/usr/bin/env python3
"""CC_001 (NUMÉRICO, mpmath, not interval): λ(κ)=bottom of a_T(F;a_κ) on P_T, a_κ(p^k)=κ_p log p at positions k·u_p
(u_p=log p for ℤ; perturbed for Beurling-type tests). a_T(F;κ)=Arch_T(F) − Σ_p κ_p L_p(F), L_p linear in κ.
Gradient (Hellmann–Feynman) and Hessian (2nd-order perturbation) per parity sector; c_{h*} at log2,log3,log6,log(3/2).
Usage: cc001_cross_hessian.py M dps T k2,k3,k5,k7 [d3]   (d3 = shift of the generator position of 3)."""
import sys, mpmath as mp
sys.path.insert(0,__file__.rsplit('/',1)[0])
from z001_parity_split import Cpoly, K
def run(T,M,kap,d3=0):
    T=mp.mpf(T); P=[2,3,5,7]; up={2:mp.log(2),3:mp.log(3)+d3,5:mp.log(5),7:mp.log(7)}
    pos={p:[(k*up[p]) for k in range(1,6) if k*up[p]<2*T] for p in P}
    mom=[mp.quad(lambda u:(u/T)**r*K(u),[0,T,2*T]) for r in range(2*M+2)]
    tail=mp.quad(K,[2*T,mp.inf]); C0=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
    out={}
    for par in (0,1):
        idx=[j for j in range(M) if j%2==par]; d=len(idx)
        G=mp.matrix(d,d); A0=mp.matrix(d,d); Bp={p:mp.matrix(d,d) for p in P}
        cf=lambda s,pol: T*mp.fsum(mp.mpf(c.numerator)/c.denominator*s**r for r,c in pol.items())
        pols={}
        for a_,j in enumerate(idx):
            for b_,k in enumerate(idx):
                Pp=Cpoly(j,k); Q=Cpoly(k,j); pol={r:(Pp.get(r,0)+Q.get(r,0))/2 for r in set(Pp)|set(Q)}; pols[a_,b_]=pol
                g0=Pp.get(0,0); G[a_,b_]=T*mp.mpf(g0.numerator)/g0.denominator
                A0[a_,b_]=(C0+tail)*G[a_,b_]-T*mp.fsum(mp.mpf(c.numerator)/c.denominator*mom[r] for r,c in pol.items() if r>0)
                for p in P: Bp[p][a_,b_]=mp.fsum(2*mp.log(p)*mp.e**(-u/2)*cf(u/T,pol) for u in pos[p])
        w=(lambda t:mp.cosh(t/2)) if par==0 else (lambda t:mp.sinh(t/2))
        cv=[mp.quad(lambda t:(t/T)**j*w(t),[-T,0,T]) for j in idx]
        Z=mp.matrix(d,d-1)
        for c in range(1,d): Z[c,c-1]=1; Z[0,c-1]=-cv[c]/cv[0]
        L=mp.cholesky(Z.T*G*Z); Li=mp.inverse(L); tr=lambda X:(lambda S:(S+S.T)/2)(Li*(Z.T*X*Z)*Li.T)
        S=tr(A0); Sp={p:tr(Bp[p]) for p in P}
        for i,p in enumerate(P): S=S-kap[i]*Sp[p]
        E,Q=mp.eigsy(S); n=len(E); o=sorted(range(n),key=lambda i:E[i]); E=[E[i] for i in o]
        V=[Q[:,i] for i in o]; v0=V[0]
        grad={p:-(v0.T*Sp[p]*v0)[0] for p in P}
        H={(p,q):-2*mp.fsum((v0.T*Sp[p]*V[j])[0]*(v0.T*Sp[q]*V[j])[0]/(E[j]-E[0]) for j in range(1,n)) for p in P for q in P}
        x=Z*(Li.T*v0)   # coefficients of h* in monomials
        def c(u):
            s=u/T; return mp.fsum(x[a]*x[b]*cf(s,pols[a,b]) for a in range(d) for b in range(d)) if s<2 else 0
        out['even' if par==0 else 'odd']=dict(lam=E[0],gap=E[1]-E[0],grad=grad,H=H,
            c={k:c(u) for k,u in [('0',0),('2',mp.log(2)),('3',mp.log(3)),('3/2',mp.log(1.5)),('6',mp.log(6))]})
    return out
if __name__=='__main__':
    M=int(sys.argv[1]); mp.mp.dps=int(sys.argv[2]); T=float(sys.argv[3]); kap=[float(x) for x in sys.argv[4].split(',')]
    d3=float(sys.argv[5]) if len(sys.argv)>5 else 0
    r=run(T,M,kap,d3)
    for s in ('even','odd'):
        R=r[s]; f=lambda z:mp.nstr(z,8)
        print(f"T={T} κ={kap} d3={d3} {s}: λ={f(R['lam'])} gap={f(R['gap'])} grad={{{', '.join(f'{p}:{f(v)}' for p,v in R['grad'].items())}}}")
        print("   H22,H33,H23,H25,H35 =",f(R['H'][2,2]),f(R['H'][3,3]),f(R['H'][2,3]),f(R['H'][2,5]),f(R['H'][3,5]),
              " corr23=",f(R['H'][2,3]/mp.sqrt(R['H'][2,2]*R['H'][3,3])))
        print("   c(0),c(l2),c(l3),c(l3/2),c(l6) =",', '.join(f(v) for v in R['c'].values()))
