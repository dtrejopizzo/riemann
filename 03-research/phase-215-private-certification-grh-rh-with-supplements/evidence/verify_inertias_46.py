"""Arb verification of the four bordered forms, conditional on quadrature remainder.
Reads independently reconstructed matrices. No claimed certificate unless every
predicate succeeds AND the analytic quadrature remainder has been established.
"""
import json, time
from pathlib import Path
from flint import arb, arb_mat, ctx
ctx.prec=640
BASE=Path(__file__).resolve().parent

def ballerr(bound):
    return arb(0,bound.upper())

def positive_ldl(M):
    # Symmetric LDL, each positive pivot is a rigorous ball predicate.
    n=M.nrows(); L=[[arb(0) for j in range(n)] for i in range(n)]; D=[]
    for i in range(n):
        d=M[i,i]-sum((L[i][k]**2*D[k] for k in range(i)),arb(0))
        if not d>0:
            return dict(ok=False,index=i,pivot=d.str(30))
        D.append(d)
        for j in range(i+1,n):
            L[j][i]=(M[j,i]-sum((L[j][k]*L[i][k]*D[k] for k in range(i)),arb(0)))/d
    return dict(ok=True,min_pivot=min(d.lower() for d in D).str(30),size=n)

def preconditioned_positive(M):
    n=M.nrows(); L=[[arb(0) for _ in range(n)] for _ in range(n)]; D=[]
    for i in range(n):
        d=(M[i,i].mid()-sum((L[i][k]**2*D[k] for k in range(i)),arb(0))).mid()
        if not d>0: return dict(ok=False,reason='midpoint factorization',index=i)
        D.append(d); L[i][i]=arb(1)
        for j in range(i+1,n):
            L[j][i]=((M[j,i].mid()-sum((L[j][k]*L[i][k]*D[k] for k in range(i)),arb(0)))/d).mid()
    # L has exact entries and diagonal 1. Its inverse is certified by Arb.
    P=arb_mat(L).inv()
    for i in range(n):
        scale=D[i].sqrt()
        for j in range(n): P[i,j]/=scale
    S=P*M*P.transpose()
    margins=[S[i,i]-sum((abs(S[i,j]) for j in range(n) if j!=i),arb(0)) for i in range(n)]
    return dict(ok=all(v>0 for v in margins),method='certified congruence and Gershgorin',min_margin=min(v.lower() for v in margins).str(30),midpoint_min_pivot=min(D).str(30),size=n)

def run():
    raw=json.loads((BASE/'matrices_46_arb.json').read_text())
    T=arb(5).log()/2; A=2*arb(2).log()/arb(2).sqrt()+2*arb(3).log()/arb(3).sqrt()+arb(2).log()
    si=arb(raw['s_infty']); c0=arb(1)/4
    C0=c0.digamma()-arb.pi().log()
    op=si-C0+A; om=2*A
    lam1=arb('4.5e-20'); lam2=arb('3.9e-70')
    tail=(op+om)*lam2.sqrt()
    x=T/2
    chi=[(arb(2*n+1)/(2*T)).sqrt()*2*T*(arb.pi()/(2*x)).sqrt()*x.bessel_i(arb(n)+arb('0.5')) for n in range(330)]
    results=[]
    for parity,mu,c in [(0,'2.5e-12','0'),(1,'3e-10','0'),(0,'1e-18','-0.5'),(1,'1e-16','0.5')]:
        G=arb_mat([[arb(v) for v in row] for row in raw['matrices'][parity]])
        ch=[chi[n] for n in range(parity,330,2)]
        total=T.sinh()+(T if parity==0 else -T)
        chi_tail=max(arb(0),(total-sum((v*v for v in ch),arb(0))).upper()).sqrt()
        q=si-arb(mu)-op*lam1
        assert q>0
        R=arb_mat(141,141)
        for i in range(140):
            for j in range(i+1):
                gram=sum((G[k,i]*G[k,j] for k in range(140,165)),arb(0))+ballerr(tail**2)
                v=(si-arb(mu) if i==j else arb(0))-G[i,j]-gram/q
                R[i,j]=v; R[j,i]=v
            cross=sum((G[k,i]*ch[k] for k in range(140,165)),arb(0))+ballerr(tail*chi_tail)
            R[i,140]=ch[i]+cross/q; R[140,i]=R[i,140]
        # Replacing only this diagonal by a lower bound gives R' <= R.
        chi_y=max(arb(0),(total-sum((v*v for v in ch[:140]),arb(0))).upper())
        R[140,140]=arb(c)-(chi_y/q.lower()).upper()
        entry=dict(parity=parity,mu=mu,c=c,q_Y=q.str(30),tail=tail.str(30))
        if c=='0.5':
            entry['inertia']=positive_ldl(R)
            entry['expected_negative']=0
        else:
            if c=='-0.5':
                v=[R[i,140].mid() for i in range(140)]
                norm=sum((a*a for a in v),arb(0)).sqrt()
                v[0]+=norm if v[0]>0 else -norm
                vn=sum((a*a for a in v),arb(0))
                H=arb_mat([[(arb(1) if i==j else arb(0))-2*v[i]*v[j]/vn for j in range(140)] for i in range(140)])
                E=H.transpose()*H
                assert all(sum((abs(E[i,j]-(1 if i==j else 0)) for j in range(140)),arb(0))<1 for i in range(140))
                HH=arb_mat(141,141)
                for i in range(140):
                    for j in range(140): HH[i,j]=H[i,j]
                HH[140,140]=1
                R=HH.transpose()*R*HH
                entry['householder_invertibility_verified']=True
            # A fixed principal two-by-two block; no numerical Householder needed.
            B=arb_mat([[R[0,0],R[0,140]],[R[140,0],R[140,140]]])
            entry['border_det']=B.det().str(30)
            if not B.det()<0:
                entry['inertia']=dict(ok=False,reason='border determinant not negative')
            else:
                C=arb_mat([[R[i,0],R[i,140]] for i in range(1,140)])
                D=arb_mat([[R[i,j] for j in range(1,140)] for i in range(1,140)])
                S=D-C*B.inv()*C.transpose()
                entry['inertia']=positive_ldl(S)
                if not entry['inertia']['ok']:
                    entry['direct_ldl_failure']=entry['inertia']
                    entry['inertia']=preconditioned_positive(S)
            entry['expected_negative']=1
        results.append(entry)
        print(json.dumps(entry),flush=True)
    report=dict(status='conditional on analytic remainder and tail bounds',precision=640,results=results)
    (BASE/'inertias_46_arb.json').write_text(json.dumps(report,indent=2))
if __name__=='__main__':
    run()
