import numpy as np
from scipy.special import digamma
from scipy.optimize import brentq
from scipy.integrate import quad
def Lam(n):
    m=n;p=2;ps=[]
    while p*p<=m:
        if m%p==0:
            while m%p==0: m//=p
            ps.append(p)
        p+=1
    if m>1: ps.append(m)
    return np.log(ps[0]) if len(ps)==1 else 0.0
def weights(T):
    N=int(np.floor(np.exp(2*T)))+1
    out=[]
    for n in range(2,N+1):
        if n>=np.exp(2*T): continue
        L=Lam(n)
        if L>0: out.append((n,L/np.sqrt(n)))
    return out
def gmm(t): return np.real(digamma(0.25+0.5j*np.asarray(t,dtype=float)))-np.log(np.pi)
def mk(T):
    W=weights(T); logs=np.array([np.log(n) for n,w in W]); ws=np.array([w for n,w in W])
    def sig(t):
        t=np.asarray(t,dtype=float)
        return gmm(t)-2*np.sum(ws[:,None]*np.cos(np.outer(logs,t)),axis=0).reshape(t.shape) if t.ndim else gmm(t)-2*np.sum(ws*np.cos(logs*t))
    return W,sig
def rho_f(sig): return lambda t:(np.asarray(t,float)**2+0.25)**2*sig(t)
def analyze(T,lab):
    W,sig=mk(T); rho=rho_f(sig)
    S=sum(w for n,w in W)
    print(f"\n=== T={lab} = {T:.10f}   terms {[(n,round(w,6)) for n,w in W]}  sum w={S:.8f}  2S={2*S:.8f}")
    print(f" sigma(0)={sig(0.0):.10f}   g-m0 at 0 = {gmm(0.0):.10f}")
    g=np.linspace(0,120,1200001); v=sig(g)
    idx=np.where(np.sign(v[:-1])*np.sign(v[1:])<0)[0]
    roots=[brentq(lambda x:sig(x),g[i],g[i+1],xtol=1e-14) for i in idx]
    print(" roots of sigma on [0,120]:",[f"{r:.8f}" for r in roots])
    negmask=v<0
    if negmask.any():
        taustar=g[negmask].max(); D=(-v[negmask]).max(); Dt=np.abs(rho(g[negmask])).max()
    else: taustar=0.0;D=0;Dt=0
    print(f" tau* = sup N_T = {taustar:.8f};  D_T = max|sigma|_N = {D:.8f};  max|rho|_N = {Dt:.8f}")
    # L1 of rho^-
    L1=2*quad(lambda t: max(0.0,-rho(t)),0,taustar+0.5,limit=400,points=[r for r in roots if r<taustar+0.5])[0]
    # also L1 of sigma^-
    L1s=2*quad(lambda t: max(0.0,-sig(t)),0,taustar+0.5,limit=400,points=[r for r in roots if r<taustar+0.5])[0]
    print(f" ||rho^-||_1 = {L1:.8f}   ||sigma^-||_1 = {L1s:.8f}")
    gg=np.linspace(taustar,300,3000001); rv=rho(gg); i=np.argmin(rv)
    eps=rv[i]
    print(f" eps_* = inf_{{|t|>=tau*}} rho = {eps:.8f} at tau={gg[i]:.5f}")
    th=2*T*taustar/np.pi
    print(f" theta_L1bound = 2T tau*/pi = {th:.8f}")
    lhs=eps*(1-th) if th<1 else float('-inf'); rhs=T/np.pi*L1
    print(f" CRITERION lhs={lhs:.8f} rhs={rhs:.8f} -> {'CLOSES margin '+str(lhs-rhs) if lhs>=rhs else 'FAILS shortfall '+str(rhs-lhs)}")
    return dict(T=T,taustar=taustar,eps=eps,L1=L1,th=th,roots=roots,D=D,Dt=Dt)
R={}
for T,lab in [(0.5*np.log(3),'0.5log3'),(np.log(2),'log2'),(0.5*np.log(5),'0.5log5'),(0.5*np.log(7),'0.5log7')]:
    R[lab]=analyze(T,lab)
