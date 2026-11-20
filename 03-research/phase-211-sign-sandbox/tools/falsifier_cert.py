"""Interval-arithmetic certificates lambda_A(T; w) < 0 for modified combs w (ROUND_007_C).
Usage: python3 falsifier_cert_run.py {a3|beur|1.1L} N delta   (memo values: a3 8 1e-6, beur 8 1e-6, 1.1L 12 1e-6).
The witness is rebuilt from the Galerkin minimiser; the printed rationals and solved coefficient are the certified F."""
import numpy as np, mpmath as mp, sys

from fractions import Fraction as Fr
from flint import arb, acb, ctx
ctx.prec=256
def combs(Tf):
    import math
    v=lambda p,n: 2*math.log(p)/math.sqrt(n)
    return {'a3':[(math.log(3),v(3,3)),(math.log(5),v(5,5))],
            'beur':[(math.log(2),v(2,2)),(math.log(3.2),v(3,3)),(math.log(4),v(2,4)),(math.log(5),v(5,5))],
            '1.1L':[(math.log(n),1.1*v(p,n)) for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]]}
# ---- generic closed forms, backend-agnostic (x = sin/cos/exp functions)
def cfun(a,L,u,sin,cos):
    # c(u)=int_u^L F(s)F(s-u)ds, F=sum a_k sin(w_k s), w_k=k pi/L
    N=len(a); tot=0
    for j in range(N):
        for k in range(N):
            if a[j]==0 or a[k]==0: continue
            wj=(j+1)*PI/L; wk=(k+1)*PI/L
            al=wj-wk; be=wk*u
            t1=(L-u)*cos(be) if j==k else (sin(al*L+be)-sin(al*u+be))/al
            al2=wj+wk; be2=-wk*u
            t2=(sin(al2*L+be2)-sin(al2*u+be2))/al2
            tot=tot+a[j]*a[k]*(t1-t2)/2
    return tot
def num_min(Tf,comb,N):
    global PI; PI=np.pi
    L=2*Tf; C0=float(mp.digamma(0.25)-mp.log(mp.pi))
    tail=-np.log(np.tanh(Tf/2))+np.pi-2*np.arctan(np.exp(Tf))
    K=lambda u:1/(2*np.sinh(u/2))+1/(2*np.cosh(u/2))
    def form(a):
        c0=cfun(a,L,0.0,np.sin,np.cos)
        x,wq=np.polynomial.legendre.leggauss(300); u=(x+1)*L/2
        I=np.sum(wq*L/2*(c0-cfun(a,L,u,np.sin,np.cos))*K(u))
        return (C0+tail)*c0+I-sum(w*cfun(a,L,x,np.sin,np.cos) for x,w in comb)
    E=np.eye(N); M=np.zeros((N,N))
    d=[form(E[i]) for i in range(N)]
    for i in range(N):
        M[i,i]=d[i]
        for j in range(i):
            M[i,j]=M[j,i]=(form(E[i]+E[j])-d[i]-d[j])/2
    # moments
    def mom(k,s):
        w=(k+1)*np.pi/L; z=complex(s,w); return np.exp(-s*Tf)*((np.exp(z*L)-1)/z).imag
    Cm=np.array([[mom(k,0.5) for k in range(N)],[mom(k,-0.5) for k in range(N)]])
    Q=np.linalg.svd(Cm)[2][2:].T
    G=(L/2)*np.eye(N)
    ev,V=np.linalg.eigh(Q.T@M@Q, Q.T@G@Q) if False else (None,None)
    from scipy.linalg import eigh
    ev,V=eigh(Q.T@M@Q,Q.T@G@Q)
    return ev[0], Q@V[:,0], Cm
def certify(Tstr,comb_exact,a_num,label):
    PI_=arb.pi(); global PI; PI=PI_
    T=Tstr
    L=2*T; N=len(a_num)
    # rational coefficients: normalize largest to 1, round to 1e-6, then solve last two exactly (ball) for A=B=0
    a=np.array(a_num)/np.max(np.abs(a_num))
    r=[Fr(round(x*10**6),10**6) for x in a]
    ev_=[i for i in range(N) if i%2==0]; od_=[i for i in range(N) if i%2==1]
    i1=max(ev_,key=lambda i:abs(a[i])); i2=max(od_,key=lambda i:abs(a[i]))
    def mom(k,s):
        w=(k+1)*PI_/L; z=acb(s,w); return ( (-arb(s)*T).exp()*(((z*L).exp()-1)/z).imag )
    A=[mom(k,arb(1)/2) for k in range(N)]; B=[mom(k,-arb(1)/2) for k in range(N)]
    free=[i for i in range(N) if i not in (i1,i2)]
    ra=sum(arb(r[i].numerator)/r[i].denominator*A[i] for i in free)
    rb=sum(arb(r[i].numerator)/r[i].denominator*B[i] for i in free)
    det=A[i1]*B[i2]-A[i2]*B[i1]
    x1=(-ra*B[i2]+rb*A[i2])/det; x2=(-A[i1]*rb+B[i1]*ra)/det
    co=[arb(r[i].numerator)/r[i].denominator for i in range(N)]; co[i1]=x1; co[i2]=x2
    # check moments
    Am=sum(co[i]*A[i] for i in range(N)); Bm=sum(co[i]*B[i] for i in range(N))
    C0=arb(1)/4; C0=acb(C0).digamma().real-PI_.log()
    tail=-(T/2).tanh().log()+PI_-2*(T.exp()).atan()
    nrm=L/2*sum(c*c for c in co)
    c0=cfun(co,L,arb(0),lambda x:x.sin(),lambda x:x.cos())
    cfa=[acb(c) for c in co]
    def g(u,analytic):
        cu=cfun(cfa,acb(L),u,lambda x:x.sin(),lambda x:x.cos())
        Ku=1/(2*(u/2).sinh())+1/(2*(u/2).cosh())
        return (acb(c0)-cu)*Ku
    delta=arb(sys.argv[3]) if len(sys.argv)>3 else arb('0.01')
    I=acb.integral(g,acb(delta),acb(L)).real
    # [0,delta]: 0<= integrand <= ||F'||^2 u^2/2 *(1/u+1/2)
    d2=L/2*sum((co[k]*(k+1)*PI_/L)*(co[k]*(k+1)*PI_/L) for k in range(N))
    I0=arb(0).union(d2*(delta**2/4+delta**3/12))
    comb=sum(w*cfun(co,L,x,lambda y:y.sin(),lambda y:y.cos()) for x,w in comb_exact)
    print(' parts: C0',C0.str(20),' tail',tail.str(20),' I[delta,2T]',I.str(20),' I0',I0.str(5),' |F_prime|^2',d2.str(10))
    val=(C0+tail)*c0+I+I0-comb
    print(label,'N=',N,'idx solved',i1+1,i2+1)
    print(' coeffs (k=1..N):',[str(r[i]) if i not in (i1,i2) else 'solved' for i in range(N)])
    print(' x_%d='%(i1+1),x1.str(20),' x_%d='%(i2+1),x2.str(20))
    print(' A=',Am.str(5),' B=',Bm.str(5))
    print(' ||F||^2=',nrm.str(15),' c0=',c0.str(15))
    print(' Arch=',((C0+tail)*c0+I+I0).str(15),' comb=',comb.str(15))
    print(' a_T(F)=',val.str(15),'  ratio=',(val/nrm).str(10), ' upper<0:', val.upper()<0)
    return val
