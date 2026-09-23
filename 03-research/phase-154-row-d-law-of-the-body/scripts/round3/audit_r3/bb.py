import math,pickle,sys,time,numpy as np
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-154-row-d-law-of-the-body/scripts/round3')
from cert3 import vdict,fval,m,lip
pk=sys.argv[1]; r=pickle.load(open(pk,'rb'))
T,us,a,b0,b1,v,taumax=r['T'],r['us'],r['a'],r['b0'],r['b1'],r['v'],r['taumax']
target=float(sys.argv[2]) if len(sys.argv)>2 else r['lp']-1e-10
wmin=5e-8
L=lip(T,us,a,b0,b1,v)
n0=int(math.ceil(taumax/0.02)); w0=taumax/n0
stack=[(np.arange(n0)*w0,w0)]
lb=np.inf; best=np.inf; nfinal=0; meas=0.0; t0=time.time(); nev=0
while stack:
    cur,w=stack.pop()
    if len(cur)>200000:
        stack.append((cur[200000:],w)); cur=cur[:200000]
    mid=cur+w/2; vals=fval(mid,T,us,a,b0,b1,v); nev+=len(mid)
    best=min(best,float(vals.min()))
    keep=vals-L*w/2<target; nk=int(keep.sum())
    if nk==0: continue
    if w/2<wmin:
        lb=min(lb,float(vals[keep].min())-L*w/2); nfinal+=nk; meas+=nk*w; continue
    c2=cur[keep]
    stack.append((np.repeat(c2,2)+np.tile(np.array([0.0,w/2]),nk),w/2))
print(f"L={L:.2f} target={target:.6e} evals={nev} best_sampled={best:.8e} "
      f"final_intervals={nfinal} surviving_measure={meas:.3e} lb_on_survivors={lb:.8e}")
print(f"RIGOROUS inf_[0,{taumax}] f >= {min(target,lb):.8e}   ({time.time()-t0:.0f}s)")
