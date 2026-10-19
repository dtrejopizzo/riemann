# Barrido de T* (bloque N): certificado riguroso eps(T) vs tau(T).
import sys; sys.argv=['x']; exec(open('zcert.py').read().split("if __name__")[0])
import json
res=[]
for T in [4.0,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5.0]:
    N=NT(T); ks=list(range(1,N+1,2)); prec=600; mp.mp.dps=180
    M,c,w=build(T,ks,2000,prec); mu=lam_num(M,c); eps=certify(M,c,mu); ta=tau(T,ks)
    ok=eps is not None and eps>arb(ta); res.append(dict(T=T,N=N,mu=mp.nstr(mu,8),cert=eps.mid().str(6,radius=False),tau=ta,node=ok)); print(res[-1],flush=True)
json.dump(res,open('tstar.json','w'),indent=1)
