import mpmath as mp
mp.mp.dps=30
def Lam(n):
    # von Mangoldt
    m=n; p=2; ps=[]
    while p*p<=m:
        if m%p==0:
            k=0
            while m%p==0: m//=p; k+=1
            ps.append(p)
        p+=1
    if m>1: ps.append(m)
    return mp.log(ps[0]) if len(ps)==1 else mp.mpf(0)
def weights(T):
    N=int(mp.floor(mp.e**(2*T)))
    out=[]
    for n in range(2,N+1):
        if mp.e**(2*T)<=n: continue
        L=Lam(n)
        if L>0: out.append((n,L/mp.sqrt(n)))
    return out
def gmm(tau):  # g_Gamma - m_0 = Re psi(1/4+i tau/2) - log pi
    return mp.re(mp.digamma(mp.mpf(1)/4+1j*tau/2))-mp.log(mp.pi)
def sigma(tau,W):
    return gmm(tau)-2*sum(w*mp.cos(tau*mp.log(n)) for n,w in W)
def rho(tau,W):
    return (tau**2+mp.mpf(1)/4)**2*sigma(tau,W)
import sys
def analyze(T,label):
    W=weights(T); S=sum(w for n,w in W)
    print(f"\n=== T={label} = {mp.nstr(T,8)}  primes/powers: {[(n,mp.nstr(w,6)) for n,w in W]}  sum w={mp.nstr(S,8)}")
    print(f" sigma(0) = {mp.nstr(sigma(0,W),10)}")
    # find sign changes on [0, 80]
    xs=[mp.mpf(i)/200 for i in range(0,16001)]
    vals=[sigma(x,W) for x in xs]
    roots=[]
    for i in range(len(xs)-1):
        if vals[i]*vals[i+1]<0:
            r=mp.findroot(lambda t: sigma(t,W), (xs[i],xs[i+1]), solver='bisect')
            roots.append(r)
    print(" sign changes of sigma on [0,80]:",[mp.nstr(r,8) for r in roots])
    # negative set
    neg=[(xs[i],vals[i]) for i in range(len(xs)) if vals[i]<0]
    if neg:
        taustar=max(t for t,v in neg)
        D=max(-v for t,v in neg)
        print(f" sup N_T ~ {mp.nstr(taustar,8)}   D_T=max|sigma| on N = {mp.nstr(D,8)}")
    else:
        taustar=mp.mpf(0); D=0
    # L1 norm of rho^-
    f=lambda t: max(mp.mpf(0),-rho(t,W))
    L1=2*mp.quad(f,[0]+[float(r) for r in roots if r<=taustar+1]+[float(taustar)+1])
    print(f" ||rho^-||_1 = {mp.nstr(L1,8)}")
    # eps_* = inf rho on |tau|>=taustar   (scan to 200, then analytic tail)
    ts=[taustar+mp.mpf(i)/200 for i in range(0,int(200*(200-float(taustar)))+1)]
    rv=[(t,rho(t,W)) for t in ts]
    tm,em=min(rv,key=lambda z:z[1])
    print(f" eps_* = inf_{{|t|>=tau*}} rho = {mp.nstr(em,8)} at tau={mp.nstr(tm,8)}")
    th=2*T*taustar/mp.pi
    print(f" theta = 2 T tau*/pi = {mp.nstr(th,8)}   (needs <1)")
    lhs=em*(1-th); rhs=T/mp.pi*L1
    print(f" CRITERION: eps_*(1-theta) = {mp.nstr(lhs,8)}  vs  (T/pi)||rho^-||_1 = {mp.nstr(rhs,8)}  -> {'CLOSES' if lhs>=rhs else 'FAILS by '+mp.nstr(rhs-lhs,6)}")
    return W,roots,taustar,D,L1,em,th
for T,lab in [(mp.log(3)/2,'0.5log3'),(mp.log(2),'log2'),(mp.log(5)/2,'0.5log5'),(mp.log(7)/2,'0.5log7')]:
    analyze(T,lab)
