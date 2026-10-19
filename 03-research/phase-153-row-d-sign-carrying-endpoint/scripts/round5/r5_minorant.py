import numpy as np
from scipy.special import digamma
from scipy.optimize import brentq, linprog
from scipy.integrate import quad
LOGP=np.log(np.pi)
def Lam(n):
    m=n;p=2;ps=[]
    while p*p<=m:
        if m%p==0:
            while m%p==0: m//=p
            ps.append(p)
        p+=1
    if m>1: ps.append(m)
    return np.log(ps[0]) if len(ps)==1 else 0.0
def weights(T,a=0.0):
    out=[]
    for n in range(2,int(np.exp(2*T))+2):
        if np.log(n)>=2*T-1e-12: continue
        L=Lam(n)
        if L>0: out.append((n,L/np.sqrt(n)*(n**a+n**(-a) if a>0 else 1.0)))
    return out
def make(T,a=0.0):
    W=weights(T,a); logs=np.array([np.log(n) for n,w in W]); ws=np.array([w for n,w in W])
    if a>0:
        arch=lambda t:(np.real(digamma(0.25+a/2+0.5j*np.asarray(t,float)))+np.real(digamma(0.25-a/2+0.5j*np.asarray(t,float)))-2*LOGP)
        wt=lambda t:((np.asarray(t,float)**2+(0.5+a)**2)*(np.asarray(t,float)**2+(0.5-a)**2))
        deg=4
    else:
        arch=lambda t: np.real(digamma(0.25+0.5j*np.asarray(t,float)))-LOGP
        wt=lambda t:(np.asarray(t,float)**2+0.25)**2
        deg=4
    def sig(t):
        t=np.asarray(t,float)
        s=arch(t)
        for l,w in zip(logs,ws): s=s-2*w*np.cos(l*t)
        return s
    rho=lambda t: wt(t)*sig(t)
    return W,sig,rho,sum(ws)
def report(T,lab,a=0.0):
    W,sig,rho,S=make(T,a)
    mu=(np.pi/(2*T))**2
    print(f"\n=== T={lab}={T:.8f}  a={a}  terms={[(n,round(w,6)) for n,w in W]}  2S={2*S:.6f}  mu=(pi/2T)^2={mu:.6f}")
    print(f" sigma(0)={sig(0.0):.8f}")
    g=np.linspace(0,200,2000001); v=sig(g)
    idx=np.where(np.sign(v[:-1])*np.sign(v[1:])<0)[0]
    roots=[brentq(sig,g[i],g[i+1],xtol=1e-13) for i in idx]
    neg=v<0; taustar=g[neg].max() if neg.any() else 0.0
    print(f" #roots={len(roots)} first={roots[0]:.6f} last={roots[-1]:.6f}  tau*=supN={taustar:.5f}  D_T={(-v[neg]).max():.6f}")
    print(f"  roots: {[round(r,4) for r in roots][:14]}")
    # LP: maximize a2 mu^2 + a1 mu + a0 s.t. a2 x^2+a1 x+a0 <= rho(sqrt x), a2>=0, a1+a2 mu>=0
    X=np.concatenate([np.linspace(0,60,6001),np.linspace(60,400,3401)])
    x=X**2; r=rho(X)
    A=np.column_stack([x**2,x,np.ones_like(x)])
    Aub=np.vstack([A, [-1,0,0], [-mu,-1,0]]); bub=np.concatenate([r,[0,0]])
    res=linprog(c=[-mu**2,-mu,-1],A_ub=Aub,b_ub=bub,bounds=[(None,None)]*3,method='highs')
    if not res.success: print(" LP failed",res.message); return None
    a2,a1,a0=res.x; s1=a1+a2*mu; s0=a0+mu*s1
    # tail check: need a2 x^2+a1 x+a0 <= rho for tau>400
    tail_ok = a2 <= (np.log(400/2)-LOGP-2*S)
    print(f" minorant P(tau)={a2:.6f} tau^4 + {a1:.6f} tau^2 + {a0:.6f}   (P<=rho on [0,400], tail-ok={tail_ok})")
    print(f" Horner: s2={a2:.6f}>=0, s1={s1:.6f}>=0, s0 = {s0:.8f}  -> {'CLOSES' if s0>=0 else 'FAILS, shortfall '+format(-s0,'.6f')}")
    print(f"   (relative shortfall s0/|a0| = {s0/abs(a0):.4f})")
    return s0
for T,lab in [(0.5*np.log(2),'0.5log2'),(0.5*np.log(3),'0.5log3'),(np.log(2),'log2'),(0.5*np.log(5),'0.5log5'),(0.5*np.log(7),'0.5log7')]:
    report(T,lab)
for a in [0.10,0.30,0.45]:
    report(np.log(2),'log2',a)
    report(0.5*np.log(3),'0.5log3',a)
