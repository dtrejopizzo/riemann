#!/usr/bin/env python3
"""BARRIER_Z_001 (NUMÉRICO, mpmath, not interval): parity-resolved bottoms of a_T on P_T (P47 eq:Aform).
Exact reflection R F(t)=F(-t) commutes with a_T and maps the Tate pair {∫F e^{t/2}, ∫F e^{-t/2}} to itself,
so P_T = P_T^+ ⊕ P_T^- with constraints ∫F cosh(t/2)=0 (even) / ∫F sinh(t/2)=0 (odd).
Basis: monomials (t/T)^j; c(u) matrices are exact polynomials in s=u/T (rational coefficients);
∫(G-C(u))K(u)du via moments ∫_0^{2T} s^r K. Usage: z001_parity_split.py M dps [comb]  comb in {Lam, aP, cLam}"""
import sys, mpmath as mp
from fractions import Fraction as Fr
from math import comb as binom
def pp(nmax):
    out=[]
    for n in range(2,nmax+1):
        p=next(q for q in range(2,n+1) if n%q==0); r=n
        while r%p==0: r//=p
        if r==1: out.append((n,p))
    return out
_cache={}
def Cpoly(j,k):
    # ∫_{-1+s}^{1} x^j (x-s)^k dx as dict power->Fraction
    key=(j,k)
    if key in _cache: return _cache[key]
    P={}
    for i in range(k+1):
        c=binom(k,i)*(-1)**(k-i); m=j+i+1   # c s^{k-i} (1-(s-1)^m)/m
        P[k-i]=P.get(k-i,0)+Fr(c,m)
        for l in range(m+1):   # (s-1)^m = sum binom(m,l) s^l (-1)^{m-l}
            P[k-i+l]=P.get(k-i+l,0)-Fr(c*binom(m,l)*(-1)**(m-l),m)
    _cache[key]=P; return P
def K(u): return 2*mp.e**(-u/2)/(1-mp.e**(-2*u))
def sector_bottoms(T, M, comb='Lam', alt=None):
    T=mp.mpf(T); N=mp.e**(2*T)
    cont=[(n,p) for n,p in pp(int(N)+1) if mp.log(n)<2*T]
    if comb=='Lam': a={n:mp.log(p) for n,p in cont}
    elif comb=='cLam': a={n:alt*mp.log(p) for n,p in cont}
    elif comb=='aP': a={n:(mp.log(p) if p!=alt else 0) for n,p in cont}
    mom=[mp.quad(lambda u:(u/T)**r*K(u),[0,T,2*T]) for r in range(2*M+2)]
    tail=mp.quad(K,[2*T,mp.inf]); C0=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
    res={}
    for par in (0,1):
        idx=[j for j in range(M) if j%2==par]; d=len(idx)
        G=mp.matrix(d,d); A=mp.matrix(d,d)
        for a_,j in enumerate(idx):
            for b_,k in enumerate(idx):
                P=Cpoly(j,k); Q=Cpoly(k,j)
                g0=P.get(0,0); g=T*mp.mpf(g0.numerator)/g0.denominator
                pol={r:(P.get(r,0)+Q.get(r,0))/2 for r in set(P)|set(Q)}
                ev=lambda s: T*mp.fsum(mp.mpf(c.numerator)/c.denominator*s**r for r,c in pol.items())
                E=-T*mp.fsum(mp.mpf(c.numerator)/c.denominator*mom[r] for r,c in pol.items() if r>0)
                cb=mp.fsum(2*a[n]/mp.sqrt(n)*ev(mp.log(n)/T) for n,_ in cont)
                G[a_,b_]=g; A[a_,b_]=(C0+tail)*g+E-cb
        # constraint vector
        w=(lambda t:mp.cosh(t/2)) if par==0 else (lambda t:mp.sinh(t/2))
        cvec=[mp.quad(lambda t:(t/T)**j*w(t),[-T,0,T]) for j in idx]
        # null basis of cvec: eliminate the first coordinate whose coefficient is nonzero
        piv=0; Z=mp.matrix(d,d-1)
        for c in range(1,d): Z[c,c-1]=1; Z[piv,c-1]=-cvec[c]/cvec[piv]
        Gz=Z.T*G*Z; Az=Z.T*A*Z
        L=mp.cholesky(Gz); Li=mp.inverse(L); S=Li*Az*Li.T; S=(S+S.T)/2
        e=mp.eigsy(S,eigvals_only=True); e=sorted([e[i] for i in range(len(e))])
        res['even' if par==0 else 'odd']=e[:2]
    return res
if __name__=='__main__':
    M=int(sys.argv[1]); mp.mp.dps=int(sys.argv[2]); comb=sys.argv[3] if len(sys.argv)>3 else 'Lam'
    alt=float(sys.argv[4]) if len(sys.argv)>4 else None
    if comb=='aP': alt=int(alt)
    Ts=[float(x) for x in sys.argv[5].split(',')] if len(sys.argv)>5 else [0.8,0.9,1.0,1.1,1.2,1.3]
    for T in Ts:
        r=sector_bottoms(T,M,comb,alt); e,o=r['even'][0],r['odd'][0]
        print(f"T={T} M={M} {comb}{'' if alt is None else alt}: mu_even={mp.nstr(e,15)} mu_odd={mp.nstr(o,15)} diff={mp.nstr(e-o,6)} | 2nd: {mp.nstr(r['even'][1],6)} {mp.nstr(r['odd'][1],6)}",flush=True)
