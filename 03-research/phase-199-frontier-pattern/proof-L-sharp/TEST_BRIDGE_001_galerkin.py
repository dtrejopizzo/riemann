# TEST_BRIDGE_001 step 2 (Legendre/Galerkin side, Mori's even form G = sym(A+J) at μ=15, 832 modes):
#  task 2: R_J = W(g_J)/W(g*), g_J = L²(I)-projection of g* on V_J = span{P_N E e_j : j ≤ J}, e_j = ψ_{4j} − (ψ_{4j}(0)/ψ_0(0))ψ_0
#          (f(0) = 0 re-imposed); Ritz minimum of W on V_J; truncation variant with the MORI15 prolate coefficients a_{4j}.
#  task 1: edge/bulk split with p_λ = canonical Schur complement (W-orthogonal to the core of V_J; and of the full space),
#          f(λ) = g(T)/√λ;  b*, e₂, C* = W(v*), identity C* + 2f b* + f² e₂ = W*.
import json,sys,os,time,pickle
from pathlib import Path
from flint import arb,arb_mat,ctx
import mpmath as mp
SP=Path(os.environ['SP']); OUT=SP/'tb'; DATA=Path(__file__).parent/'MORI15_EXTREMAL_001_data'
ctx.prec=int(os.environ.get('PREC','400')); mp.mp.prec=ctx.prec
RF=os.environ.get('RUNGS','rungs_QF1.0.pkl')
t0=time.time()
mu=15; L=arb(mu).log()/2; lam=arb(mu).sqrt(); N=1664; I=list(range(0,N,2)); d=len(I)
E=json.load(open(DATA/'p0_eig.json')); g=arb_mat([[arb(x)] for x in E['vectors'][0]])
lamstar=arb(E['rayleigh_bottom'].split('+/-')[0].strip('[ '))
R=pickle.load(open(OUT/RF,'rb')); ks=R['ks']; nk=len(ks)
Bk=arb_mat([[arb(x) for x in row] for row in R['coef']])
psi0={k:arb(R['info'][k]['psi0']) for k in ks}; psi1={k:arb(R['info'][k]['psi1']) for k in ks}
J_all=nk-1
# basis e_j, j=1..J_all
Bas=arb_mat(d,J_all)
for j in range(1,nk):
    r=psi0[ks[j]]/psi0[0]
    for i in range(d): Bas[i,j-1]=Bk[i,j]-r*Bk[i,0]
evT=arb_mat([[ (arb(2*I[t]+1)/(2*L)).sqrt() for t in range(d)]])   # row: g ↦ g(T)
edge=lambda M: evT*M/lam.sqrt()          # f(λ) = g(T)/√λ
# check edge of the Legendre-projected rungs vs exact λ^{-1/2}ψ_k(1)
ek=edge(Bk); edge_check={k:[ek[0,q].str(10),(psi1[k]/lam.sqrt()).str(10)] for q,k in enumerate(ks) if k<=48}
print('edge check',edge_check,flush=True)
# G
cache=OUT/'G_even.pkl'
if cache.exists(): Gs=pickle.load(open(cache,'rb'))
else:
    A=json.load(open(SP/'mori15'/'p0_A_mid.json')); Jm=json.load(open(SP/'mori15'/'p0_J_mid.json'))
    Gs=[[None]*d for _ in range(d)]
    for i in range(d):
        for j in range(i,d):
            s=(mp.mpf(A[i][j])+mp.mpf(Jm[i][j])+mp.mpf(A[j][i])+mp.mpf(Jm[j][i]))/2
            Gs[i][j]=Gs[j][i]=mp.nstr(s,140,strip_zeros=False)
    del A,Jm; pickle.dump(Gs,open(cache,'wb'))
G=arb_mat([[arb(x) for x in row] for row in Gs]); del Gs
print('G loaded',time.time()-t0,flush=True)
Wst=(g.transpose()*G*g)[0,0]; print('W(g*)',Wst.str(25),' lambda*',lamstar.str(25),flush=True)
GB=G*Bas; K=Bas.transpose()*GB; M=Bas.transpose()*Bas; bg=Bas.transpose()*g
ed=edge(Bas); fst=edge(g)[0,0]
def sub(Mx,J): return arb_mat([[Mx[i,j] for j in range(J)] for i in range(J)])
def subv(v,J): return arb_mat([[v[i,0]] for i in range(J)])
out={'W*':Wst.str(25),'f*(λ)':fst.str(20),'g*(T)':(fst*lam.sqrt()).str(20),'edge_check':edge_check,'task2':{},'task1':{}}
# MORI15 prolate coefficients (min gauge, 20 digits)
P28=json.load(open(DATA/'p0_prolate_M28.json')); ak=[arb(x) for x in P28['a_k_mingauge']]   # index = k/2
def mpm(Mx): return mp.matrix([[mp.mpf(Mx[i,j].mid().str(130,radius=False)) for j in range(Mx.ncols())] for i in range(Mx.nrows())])
for J in [1,2,3,4,5,6,8,10,11,12,15,20,30,40,50]:
    if J>J_all: continue
    MJ=sub(M,J); KJ=sub(K,J); bJ=subv(bg,J)
    y=MJ.solve(bJ); gJ=Bas*arb_mat([[y[i,0]] for i in range(J)]+[[arb(0)]]*(J_all-J))
    dl=g-gJ; nd2=(dl.transpose()*dl)[0,0]; ng2=(gJ.transpose()*gJ)[0,0]
    WJ=(y.transpose()*KJ*y)[0,0]; Wd=(dl.transpose()*G*dl)[0,0]
    # Ritz minimum on V_J: generalized eigen (K,M)
    Km=mpm(KJ); Mm=mpm(MJ); Lc=mp.cholesky(Mm); Li=mp.inverse(Lc); Ar=Li*Km*Li.T; Ar=(Ar+Ar.T)/2
    ev=mp.eigsy(Ar,eigvals_only=True); rmin=min(ev)
    row={'R_J=W(g_J)/W*':(WJ/Wst).str(12),'Rayleigh(g_J)/W*':(WJ/ng2/Wst).str(12),'||g*-g_J||^2':nd2.str(8),
         'W(g*-g_J)/W*':(Wd/Wst).str(12),'Ritz_min/W*':mp.nstr(rmin/mp.mpf(Wst.mid().str(60,radius=False)),12),
         'f_J(λ)/f*(λ)':(edge(gJ)[0,0]/fst).str(10)}
    # truncation variant: f_J^tr = Σ_{j≤J} a_{4j} e_j  (a_0 replaced by the f(0)=0 repair)
    if 2*J<len(ak):
        ytr=arb_mat([[ak[2*j]] for j in range(1,J+1)])
        gtr=Bas*arb_mat([[ytr[i,0]] for i in range(J)]+[[arb(0)]]*(J_all-J))
        Wtr=(ytr.transpose()*KJ*ytr)[0,0]; dtr=g-gtr
        row['trunc: W/W*']=(Wtr/Wst).str(12); row['trunc: ||g*-g_tr||^2']=(dtr.transpose()*dtr)[0,0].str(8)
    out['task2'][J]=row; print('J',J,row,time.time()-t0,flush=True)
# ---- task 1: edge/bulk split (all in basis coordinates: p = Bas·yp has coefficients ~1e34, so avoid forming G·p)
pvecs={}
Gg_bas=Bas.transpose()*(G*g)     # = λ*·Basᵀg up to the eigen-residual
for J in [1,2,3,4,5,6,8,10,11,12]:
    if J>J_all: continue
    KJ=sub(K,J); eJ=arb_mat([[ed[0,j]] for j in range(J)])
    z=KJ.solve(eJ); e2=1/((eJ.transpose()*z)[0,0]); yp=z*e2      # p_J = Bas·yp, ε(p_J)=1, W-orthogonal to the core of V_J
    Wp=(yp.transpose()*KJ*yp)[0,0]; gp=(yp.transpose()*subv(bg,J))[0,0]; Wpg=(yp.transpose()*subv(Gg_bas,J))[0,0]
    MJ=sub(M,J); np2=(yp.transpose()*MJ*yp)[0,0]
    b=Wpg-fst*Wp                       # b* = W(v*,p), v* = g* − f*p
    Cst=Wst-2*fst*Wpg+fst*fst*Wp       # C* = W(v*)
    v2=1-2*fst*gp+fst*fst*np2          # ‖v*‖²
    row={'e2':Wp.str(15),'e2(Schur formula)':e2.str(15),'b*':b.str(12),'f*':fst.str(15),'C*=W(v*)':Cst.str(12),
         'C*/W*':(Cst/Wst).str(10),'2f b/W*':(2*fst*b/Wst).str(10),'f^2 e2/W*':(fst*fst*Wp/Wst).str(10),
         'identity (C+2fb+f²e2)/W*':((Cst+2*fst*b+fst*fst*Wp)/Wst).str(15),'theta_C = 1-b^2/(e2 C*)':(1-b*b/(Wp*Cst)).str(10),
         'W*/C*':(Wst/Cst).str(10),'<p,g*>':gp.str(12),'||p||':np2.sqrt().str(12),'cos(p,g*)':(gp/np2.sqrt()).str(15),
         '||v*||^2':v2.str(10),'W(p,g*)/(λ*<p,g*>)':(Wpg/(lamstar*gp)).str(15),'Rayleigh(v*)/W*':(Cst/v2/Wst).str(10)}
    out['task1'][J]=row; print('T1 J',J,row,flush=True)
    pJ=Bas*arb_mat([[yp[i,0]] for i in range(J)]+[[arb(0)]]*(J_all-J)); vJ=g-fst*pJ
    pvecs[J]=[vJ[i,0].mid().str(90,radius=False) for i in range(d)]   # stores v*_J = g* − f*(λ) p_J (core)
    # core part of the low-block projection g_J (L² projection of g* on V_J): u_J = g_J − f_J(λ) p_J ∈ V_J ∩ core
    yJ=sub(M,J).solve(subv(bg,J)); fJ=(arb_mat([[ed[0,j] for j in range(J)]])*yJ)[0,0]; yu=yJ-fJ*yp
    Wu=(yu.transpose()*KJ*yu)[0,0]; nu2=(yu.transpose()*sub(M,J)*yu)[0,0]
    uJ=Bas*arb_mat([[yu[i,0]] for i in range(J)]+[[arb(0)]]*(J_all-J))
    pvecs[f'low{J}']=[uJ[i,0].mid().str(90,radius=False) for i in range(d)]
    Dk={k:arb(R['info'][k]['one_minus'].strip('[]').split('+/-')[0]) for k in ks}
    r_=[psi0[ks[j]]/psi0[0] for j in range(1,J+1)]
    leakP=sum(yu[j,0]**2*Dk[ks[j+1]] for j in range(J))+(sum(yu[j,0]*r_[j] for j in range(J)))**2*Dk[0]
    row['low-block core u_J: prolate leak Σy²(1-λ)']=leakP.str(8); row['low-block core u_J: ||f||^2 prolate']=(sum(yu[j,0]**2 for j in range(J))+(sum(yu[j,0]*r_[j] for j in range(J)))**2).str(8)
    row['low-block core u_J: W/W*']=(Wu/Wst).str(12); row['low-block core u_J: ||u||^2']=nu2.str(12); row['f_J(λ)/f*']=(fJ/fst).str(10)
# global Schur in the whole Galerkin space: p = G⁻¹ε/(εᵀG⁻¹ε); b ≡ 0; C* = W* − f*²e2
evc=arb_mat([[(arb(2*I[t]+1)/(2*L)).sqrt()/lam.sqrt()] for t in range(d)])
z=G.solve(evc); e2g=1/((evc.transpose()*z)[0,0]); zz=(z.transpose()*z)[0,0]; zg=(z.transpose()*g)[0,0]
out['task1']['global']={'e2':e2g.str(15),'f^2 e2/W*':(fst*fst*e2g/Wst).str(15),'cos(p_glob,g*)':(zg/zz.sqrt()).str(20),
    'C*/W*':((Wst-fst*fst*e2g)/Wst).str(15),'zg vs f*/λ*':(zg*lamstar/fst).str(15)}
print('global',out['task1']['global'],flush=True)
zm=arb_mat([[z[i,0].mid()] for i in range(d)]); vg=g-(fst*e2g).mid()*zm; vg=arb_mat([[vg[i,0].mid()] for i in range(d)]); pvecs['glob']=[vg[i,0].mid().str(90,radius=False) for i in range(d)]
out['task1']['global']['edge(v_glob)']=edge(vg)[0,0].str(5); out['task1']['global']['W(v_glob)/W*']=((vg.transpose()*G*vg)[0,0]/Wst).str(15)
pickle.dump({'pvecs':pvecs,'note':'v*_J vectors','fst':fst.str(60)},open(OUT/'pvecs.pkl','wb'))
json.dump(out,open(OUT/f'galerkin_{RF}.json','w'),indent=1)
print('done',time.time()-t0)
