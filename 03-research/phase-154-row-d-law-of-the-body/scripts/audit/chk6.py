import math,time,numpy as np
from scipy.special import psi as dg
from scipy.optimize import linprog
v={2:2*math.log(2)/math.sqrt(2),3:2*math.log(3)/math.sqrt(3)}
def run(T,contacts,U,cap,du=0.05,dtau=0.01,taumax=80.0,ref=10,two=False):
    t0=time.time();L=2*T
    tau=np.arange(0,taumax,dtau)
    base=np.real(dg(0.25+0.5j*tau))-math.log(math.pi)-sum(v[n]*np.cos(tau*math.log(n)) for n in contacts)
    us=np.arange(2*T,2*T+U+1e-12,du);nu=len(us)
    def h(t): return 2*(0.5*math.sinh(T)*np.cos(L*t)+t*math.cosh(T)*np.sin(L*t))/(t**2+0.25)
    def h1(t):
        # int_{-L}^{L} s sinh(s/2) cos(t s) ds  = d/da [2*(a sinh(aL)cos(tL)+t cosh(aL) sin(tL))/(a^2+t^2)] at a=1/2
        a=0.5;e=1e-5
        f=lambda a: 2*(a*np.sinh(a*L)*np.cos(t*L)+t*np.cosh(a*L)*np.sin(t*L))/(a**2+t**2)
        return (f(a+e)-f(a-e))/(2*e)
    cols=[2*np.cos(np.outer(tau,us)),h(tau)[:,None],-h(tau)[:,None]]
    if two: cols+= [h1(tau)[:,None],-h1(tau)[:,None]]
    A=np.hstack([np.ones((len(tau),1))]+[-c for c in cols])
    nvar=A.shape[1];c=np.zeros(nvar);c[0]=-1
    bnds=[(None,None)]+[(-cap,cap)]*nu+[(0,None)]*(nvar-1-nu)
    r=linprog(c,A_ub=A,b_ub=base,bounds=bnds,method='highs')
    x=r.x;cc=x[1:1+nu];bb=x[1+nu]-x[2+nu];b1=(x[3+nu]-x[4+nu]) if two else 0.0
    best=1e9
    for k in range(ref):
        tf=np.arange(k*taumax/ref,(k+1)*taumax/ref,dtau/20)
        bf=np.real(dg(0.25+0.5j*tf))-math.log(math.pi)-sum(v[n]*np.cos(tf*math.log(n)) for n in contacts)
        best=min(best,(bf+2*np.cos(np.outer(tf,us))@cc+bb*h(tf)+b1*h1(tf)).min())
    print(f"T={T:.5f} {contacts} U={U} cap={cap} two={two}: LP={x[0]:.5e} fine={best:.5e} |c|1={abs(cc).sum():.4g} ({time.time()-t0:.0f}s)",flush=True)
for U,cap,two in [(6,3,False),(14,3,False),(14,3,True),(25,3,True),(25,10,True),(40,10,True)]:
    run(0.5*math.log(3),[2],U,cap,two=two)
run(math.log(2),[2,3],25,10,two=True)
