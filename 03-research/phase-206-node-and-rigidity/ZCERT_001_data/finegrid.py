# Malla fina T = 0.75..4.30 paso 0.01, bloque canonico N(T), K=500 ceros (truncar solo baja la cota): cert riguroso vs tau.
import sys; sys.argv=['x']; exec(open('zcert.py').read().split("if __name__")[0])
import json
res=[]; T=0.75
while T<4.305:
    N=NT(T); ks=list(range(1,N+1,2))
    if len(ks)>=2:
        prec=500; mp.mp.dps=150
        M,c,w=build(T,ks,500,prec); mu=lam_num(M,c); eps=certify(M,c,mu) if mu>0 else None; ta=tau(T,ks)
        res.append(dict(T=round(T,2),N=N,cert=(eps.mid().str(6,radius=False) if eps is not None else None),tau=ta,node=bool(eps is not None and eps>arb(ta))))
    T+=0.01
json.dump(res,open('finegrid.json','w'),indent=1)
bad=[r for r in res if not r['node']]; print(len(res),'puntos; fallan:',[(r['T'],r['N']) for r in bad][:10])
