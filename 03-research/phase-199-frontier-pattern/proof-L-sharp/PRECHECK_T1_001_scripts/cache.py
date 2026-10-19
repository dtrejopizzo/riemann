# build & cache prolate data + exterior continuations for given mu
import numpy as np, mpmath as mp, pickle, os, sys
from prol import prolates; from ext import Ext
def get(mu, ks=(0,4,8,12), OmF=4, ppw=48):
    fn=f'cache_mu{mu}.pkl'
    if os.path.exists(fn): return pickle.load(open(fn,'rb'))
    o,c=prolates(mu,ks=ks); cf=float(c); lam=mp.sqrt(mu)
    D={'mu':mu,'c':cf,'k':{}}
    for k in ks:
        v=o[k]; E=Ext(float(v['chi']),cf,OmF*cf,ppw)
        Y=E.spl(E.t); Yp=E.spl(E.t,1)
        S=lam**0.5*v['muk']*v['psi1']            # ρ_k(t)=S*y_k(t), ρ = r(λt), f=λ^{-1/2}ψ_k(x/λ) normalised
        D['k'][k]=dict(chi=float(v['chi']),one_minus=v['one_minus'],lam=v['lam'],psi0=v['psi0'],psi1=v['psi1'],muk=v['muk'],
                      S=S,B=E.B,beta=E.beta,Y=Y,Yp=Yp,Bspread=E.Bspread)
        D['t']=E.t; D['Om']=E.Om
        print('mu',mu,'k',k,'done',mp.nstr(v['one_minus'],8),flush=True)
    pickle.dump(D,open(fn,'wb')); return D
if __name__=='__main__': get(int(sys.argv[1]))
