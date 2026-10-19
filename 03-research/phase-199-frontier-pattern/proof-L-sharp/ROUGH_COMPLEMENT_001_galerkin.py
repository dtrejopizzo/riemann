# ROUGH_COMPLEMENT_001 step 1 (NUMÉRICO, arb 400 bits, existing data only): split g* = p + δ, p = g*_J (L²(I)-projection on
# V_J, J=50 rungs, as TEST_BRIDGE_001 task 2). Outputs: W(p), W(p,δ), W(δ) (and W(g*,δ) = λ*‖δ‖² check); Legendre spectrum of δ;
# values/derivatives of δ, p, g* near the window edge x = ±T; odd-sector comparison of the Legendre tail; vectors for the exterior.
import json,os,time,pickle
from pathlib import Path
from flint import arb,arb_mat,ctx
import numpy as np
SP=Path(os.environ['SP']); TB=SP/'tb'; OUT=SP/'rc'; DATA=Path(__file__).parent/'MORI15_EXTREMAL_001_data'
ctx.prec=400; J=int(os.environ.get('J','50')); t0=time.time()
mu=15; L=arb(mu).log()/2; lam=arb(mu).sqrt(); N=1664; I=list(range(0,N,2)); d=len(I)
E=json.load(open(DATA/'p0_eig.json')); g=arb_mat([[arb(x)] for x in E['vectors'][0]])
R=pickle.load(open(TB/'rungs_QF1.5.pkl','rb')); ks=R['ks']; nk=len(ks)
Bk=arb_mat([[arb(x) for x in row] for row in R['coef']]); psi0={k:arb(R['info'][k]['psi0']) for k in ks}
Bas=arb_mat(d,J)
for j in range(1,J+1):
    r=psi0[ks[j]]/psi0[0]
    for i in range(d): Bas[i,j-1]=Bk[i,j]-r*Bk[i,0]
G=arb_mat([[arb(x) for x in row] for row in pickle.load(open(TB/'G_even.pkl','rb'))]); print('G',time.time()-t0,flush=True)
M=Bas.transpose()*Bas; y=M.solve(Bas.transpose()*g); p=Bas*y; dl=g-p
Gp=G*p; Gd=G*dl
Wst=(g.transpose()*G*g)[0,0]; Wp=(p.transpose()*Gp)[0,0]; Wpd=(p.transpose()*Gd)[0,0]; Wd=(dl.transpose()*Gd)[0,0]
nd2=(dl.transpose()*dl)[0,0]; Wgd=(g.transpose()*Gd)[0,0]
res={'J':J,'W*':Wst.str(20),'W(p)/W*':(Wp/Wst).str(12),'W(p,δ)/W*':(Wpd/Wst).str(12),'2W(p,δ)/W*':(2*Wpd/Wst).str(12),
     'W(δ)/W*':(Wd/Wst).str(12),'sum/W*':((Wp+2*Wpd+Wd)/Wst).str(15),'||δ||^2':nd2.str(10),'W(g*,δ)/(λ*||δ||^2)':(Wgd/(Wst*nd2)).str(10),
     'Rayleigh(δ)':(Wd/nd2).str(10),'cos_W(p,δ)=W(p,δ)/sqrt(W(p)W(δ))':(Wpd/(Wp*Wd).sqrt()).str(10)}
print(res,flush=True)
dv=np.array([float(dl[i,0].mid().str(30,radius=False)) for i in range(d)])
gv=np.array([float(x) for x in E['vectors'][0]]); pv=gv-dv
# Legendre spectrum (coefficient energy by band of degree j)
bands=[(0,50),(50,100),(100,200),(200,400),(400,800),(800,1200),(1200,1664)]
def band(v): return {f'{a}-{b}':float(np.sum(v[(np.array(I)>=a)&(np.array(I)<b)]**2)/np.sum(v**2)) for a,b in bands}
res['spectrum_delta']=band(dv); res['spectrum_p']=band(pv); res['spectrum_g*']=band(gv)
res['delta_top_mode_|coef|_max_over_rms']=float(np.max(np.abs(dv))/np.sqrt(np.mean(dv**2)))
res['delta_degree_of_max']=int(I[int(np.argmax(np.abs(dv)))])
# G-eigenbasis content of δ in double (scaled; large eigenvalues only resolved)
Gd_np=np.array([[float(G[i,j].mid().str(20,radius=False)) for j in range(d)] for i in range(d)])
ev,U=np.linalg.eigh(Gd_np); cc=(U.T@dv)**2; cc/=cc.sum()
edges=[-1,1e-12,1e-6,1e-3,1e-2,1e-1,1,10,1e3]
res['delta_G_eig_content']={f'[{edges[i]:.0e},{edges[i+1]:.0e})':float(cc[(ev>=edges[i])&(ev<edges[i+1])].sum()) for i in range(len(edges)-1)}
res['delta_rayleigh_double']=float((cc*ev).sum())
# pointwise profiles near x = T (even, so x = -T identical): values, derivatives, sup norms
Lf=float(L.mid().str(30,radius=False))
from numpy.polynomial import legendre as Lg
def coefs(v):
    c=np.zeros(N); c[I]=v*np.sqrt((2*np.array(I)+1)/(2*Lf)); return c
def ev_(v,x,der=0):
    c=coefs(v)
    if der: c=Lg.legder(c)/Lf
    return Lg.legval(np.asarray(x)/Lf,c)
xs=Lf*np.array([0,0.5,0.8,0.9,0.95,0.98,0.99,0.995,0.999,1.0])
prof={}
for nm,v in (('g*',gv),('p',pv),('δ',dv)):
    prof[nm]={'x/T':list(xs/Lf),'val':list(ev_(v,xs)),'der':list(ev_(v,xs,1)),'||v||':float(np.linalg.norm(v)),
              'sup|v| on grid':float(np.max(np.abs(ev_(v,np.linspace(0,Lf,40001)))))}
res['profiles']=prof
xx=np.linspace(0,Lf,40001); dd=ev_(dv,xx)
qs=[0.5,0.9,0.99,0.999]
res['delta_L2_mass_in_x_window']={f'|x|>{q}T':float(np.trapezoid(dd[xx>q*Lf]**2,xx[xx>q*Lf])/np.trapezoid(dd**2,xx)) for q in qs}
res['delta_L2_mass_check(2∫_0^T δ²=||δ||²)']=float(2*np.trapezoid(dd**2,xx)/np.sum(dv**2))
# odd sector comparison: Legendre tail energy above degree 400 of g*_odd vs even, relative to sqrt(W)
E1=json.load(open(DATA/'p1_eig.json')); go=np.array([float(x) for x in E1['vectors'][0]])
Wo=float(E1['rayleigh_bottom'].split('+/-')[0].strip('[ ')); We=float(Wst.mid().str(20,radius=False))
for nm,v,W in (('even',gv,We),('odd',go,Wo)):
    res[f'tail_{nm}']={'||coef_{j>=400}||':float(np.sqrt(np.sum(v[np.array(I if nm=="even" else range(1,N,2))>=400]**2))),'sqrt(W)':W**0.5,
                       'energy by band':band(v) if nm=='even' else {f'{a}-{b}':float(np.sum(v[(np.arange(1,N,2)>=a)&(np.arange(1,N,2)<b)]**2)) for a,b in bands}}
json.dump(res,open(OUT/f'galerkin_J{J}.json','w'),indent=1,default=float)
pickle.dump({'pvecs':{'delta':[dl[i,0].mid().str(90,radius=False) for i in range(d)],'p':[p[i,0].mid().str(90,radius=False) for i in range(d)]}},open(OUT/'pvecs.pkl','wb'))
print(json.dumps(res,indent=1,default=float)); print('done',time.time()-t0)
