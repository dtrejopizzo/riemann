import json,math,sys,time
import numpy as np
from core import *
t0=time.time(); out={}
for X in (240.0,48.0):
    G=Grid(X); r=FUN['rho']; key=f'X{int(X)}'; o={}
    r1=G.dil(r,1); X11=G.bil(r1,r1,0,0); o['X11']=X11
    # (1,n) entries of 𝒲 (=2 bil(ρ@1,ρ@n)), split arch/pole/comb, and pro/Δr blocks
    for n in range(2,8):
        rn=G.dil(r,n); ar,po,cb=G.bil(r1,rn,0,math.log(n),parts=True)
        e=dict(total=2*(ar+po+cb)/X11,arch=2*ar/X11,pole=2*po/X11,comb=2*cb/X11)
        for P,D in (('pro04','dr_out04'),('pro_all','dr_out')):
            p1=G.dil(FUN[P],1); pn=G.dil(FUN[P],n); d1=G.dil(FUN[D],1); dn=G.dil(FUN[D],n)
            e[f'{P}@1x{D}@n']=2*G.bil(p1,dn,0,math.log(n))/X11; e[f'{D}@1x{P}@n']=2*G.bil(d1,pn,0,math.log(n))/X11
            e[f'{P}x{P}']=2*G.bil(p1,pn,0,math.log(n))/X11; e[f'{D}x{D}']=2*G.bil(d1,dn,0,math.log(n))/X11
            # P3 cross-block cosine (L2(λ,∞) in w; D_n unitary: D_n b(w)=n^½ b(nw))
            e[f'cos<{P},D_n {D}>']=math.sqrt(n)*G.ip(p1,dn)/math.sqrt(G.ip(p1,p1)*G.ip(d1,d1))
            e[f'cos<{D},D_n {P}>']=math.sqrt(n)*G.ip(d1,pn)/math.sqrt(G.ip(p1,p1)*G.ip(d1,d1))
        e['cos<r,D_n r>']=math.sqrt(n)*G.ip(r1,rn)/G.ip(r1,r1)
        o[f'(1,{n})']=e; print(key,n,{k:round(v,4) for k,v in e.items()},flush=True)
    # P2 θ_n
    th={}
    for nm in ('rho','pro_all','pro04','dr_out'):
        f1=G.dil(FUN[nm],1); tot=G.ip(f1,f1); th[nm]={'norm2':tot}
        for n in (2,3,5): th[nm][n]=lam*np.sum(G.wq*f1*f1*(G.s<n))/tot
    o['theta']=th; print(th,flush=True)
    out[key]=o
json.dump(out,open('calib_r1b.json','w'),indent=1,default=float); print(time.time()-t0)
