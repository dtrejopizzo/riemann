import math, pickle, sys, time, numpy as np
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-154-row-d-law-of-the-body/scripts/round3')
from cert3 import base,g0h,g1h,vdict,fval,m,lip
from close3 import lp
from close4 import resonance_grid

def rigorous_bb(T,us,a,b0,b1,v,taumax,target,w0=0.02,wmin=5e-8):
    """Returns (certified_lower_bound_on_inf_f_over_[0,taumax], min_sampled, L, capped_flag, nsurv)."""
    L=lip(T,us,a,b0,b1,v)
    n0=int(math.ceil(taumax/w0)); w=taumax/n0
    cur=np.arange(n0)*w; best=np.inf; capped=False
    while True:
        mid=cur+w/2; vals=np.empty(len(mid))
        for i in range(0,len(mid),200000):
            sl=slice(i,i+200000); vals[sl]=fval(mid[sl],T,us,a,b0,b1,v)
        best=min(best,float(vals.min()))
        keep=vals-L*w/2<target; nk=int(keep.sum())
        if nk==0: return target,best,L,capped,0
        if w/2<wmin:
            lb=float(vals[keep].min())-L*w/2
            return min(target,lb),best,L,capped,nk
        idx=np.where(keep)[0]
        if len(idx)>400000:
            capped=True; idx=idx[np.argsort(vals[idx])][:400000]
        cur=np.repeat(cur[idx],2)+np.tile(np.array([0.0,w/2]),len(idx)); w=w/2

T=0.5*math.log(3); M=16; U=20.0; taumax=100.0; dtau=0.002; rhomax=1.5
v=vdict(T); d=2*T/M; J=int((2*T+U)/d); us=np.arange(M,J+1)*d; P=2*math.pi/d
tau=np.unique(np.concatenate([np.arange(1e-7,taumax,dtau),resonance_grid(P,taumax,10,0.01,1e-3)]))
tp=np.unique(np.concatenate([np.arange(0.0,P,0.02),resonance_grid(P,P,10,0.01,1e-3)]))
print('atoms',len(us),'P',P,'rows',len(tau),len(tp),flush=True)
t0=time.time(); sol=lp(T,us,tau,tp,P,taumax,v,rhomax=rhomax); print('LP',sol['c'],time.time()-t0,flush=True)
a,b0,b1=sol['a'],sol['b0'],sol['b1']
pickle.dump(dict(T=T,M=M,U=U,us=us,a=a,b0=b0,b1=b1,lp=sol['c'],taumax=taumax,P=P,v=v),
            open('cert.pkl','wb'))
# rho on one period, rigorous
Ln=2*float(np.sum(np.abs(a)*us)); h=2e-5; tpf=np.arange(0.0,P,h)
nuf=np.empty(len(tpf))
for i in range(0,len(tpf),20000):
    sl=slice(i,i+20000); nuf[sl]=2*(np.cos(np.outer(tpf[sl],us))@a)
rho=-(float(nuf.min())-Ln*h/2)
print('Ln',Ln,'period residual',Ln*h/2,'rho',rho,flush=True)
k0=2*math.cosh(T)/taumax+math.sinh(T)/taumax**2; k1=8*T*math.sinh(T)/taumax
tail=m(np.array([taumax]))[0]-sum(v.values())-rho-abs(b0)*k0-abs(b1)*k1
print('tail',tail,'b0',b0,'b1',b1,'|a|1',np.abs(a).sum(),flush=True)
t0=time.time()
lb,best,L,capped,ns=rigorous_bb(T,us,a,b0,b1,v,taumax,sol['c']-1e-10)
print('L',L,'BB rigorous lb',lb,'min sampled',best,'capped',capped,'nsurv',ns,'t',time.time()-t0,flush=True)
print('CERTIFIED c =',min(tail,lb),flush=True)
