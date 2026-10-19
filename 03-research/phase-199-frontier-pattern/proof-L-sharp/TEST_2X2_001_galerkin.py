# TEST_2X2_001 step 1 (NUMÉRICO, arb 800 bits + mpmath 800 bits on J×J blocks; existing Mori VIII μ=15 even data only).
# 2×2 block structure "prolate span V_J vs complement" of G = sym(A+J) = Ar − C:
#  a_J = λ_min(PGP|V_J) (Ritz), b_J = λ_min(QGQ|V_J^⊥), c_J = ‖QGP‖ (op norm, L²), θ_J = sup ‖QGv‖²/(b_J⟨v,Gv⟩) (v∈V_J),
#  θ'_J = sup ⟨QGv,(QGQ)^{-1}QGv⟩/⟨v,Gv⟩ (exact Schur ratio), Feshbach check λ_min(S_J(λ*), M) = λ*,
#  split ‖QCP‖, ‖QArP‖ (comb / archimedean+pole) and cancellation depth.
import json,os,pickle,time
from pathlib import Path
from flint import arb,arb_mat,ctx
import mpmath as mp
SP=Path(os.environ['SP']); OUT=Path(__file__).parent/'TEST_2X2_001_data'; ctx.prec=800; mp.mp.prec=800; t0=time.time()
DATA=Path(__file__).parent/'MORI15_EXTREMAL_001_data'
N=1664; d=832; gam=arb(74)/16
G=arb_mat([[arb(x) for x in row] for row in pickle.load(open(SP/'tb'/'G_even.pkl','rb'))]); print('G',time.time()-t0,flush=True)
A=json.load(open(SP/'mori15'/'p0_A_mid.json')); C=arb_mat(d,d)
for i in range(d):
    for j in range(i,d):
        s=-(arb(A[i][j])+arb(A[j][i]))/2; C[i,j]=s; C[j,i]=s
    C[i,i]+=gam
del A; print('C',time.time()-t0,flush=True)
R=pickle.load(open(SP/'tb'/'rungs_QF1.5.pkl','rb')); ks=R['ks']; JM=50
Bk=arb_mat([[arb(x) for x in row] for row in R['coef']]); psi0={k:arb(R['info'][k]['psi0']) for k in ks}
Bas=arb_mat(d,JM)
for j in range(1,JM+1):
    r=psi0[ks[j]]/psi0[0]
    for i in range(d): Bas[i,j-1]=Bk[i,j]-r*Bk[i,0]
E=json.load(open(DATA/'p0_eig.json')); lst=arb(E['eigs'][0]); gs=arb_mat([[arb(x)] for x in E['vectors'][0]])
om4=arb(R['info'][4]['one_minus'].strip('[]').split('+/-')[0])
GB=G*Bas; CB=C*Bas; ArB=GB+CB
def M2mp(X): return mp.matrix([[mp.mpf(X[i,j].mid().str(230,radius=False)) for j in range(X.ncols())] for i in range(X.nrows())])
def geig(Amp,Bmp):  # generalized symmetric eigenvalues of (A,B), B ≻ 0
    L=mp.cholesky(Bmp); Li=mp.inverse(L); S=Li*Amp*Li.T; S=(S+S.T)/2
    E,U=mp.eigsy(S); return sorted([E[i] for i in range(S.rows)]), (Li.T*U, E)
def sub(X,J): return X[:, :J] if False else arb_mat([[X[i,j] for j in range(J)] for i in range(X.nrows())])
res={'lambda*':lst.str(30),'1-chi_4':om4.str(20),'J':{}}
import numpy as np
Gd=np.load(SP/'bb'/'G.npy')
for J in (1,2,3,5,10,20,50):
    B=sub(Bas,J); GBJ=sub(GB,J); CBJ=sub(CB,J); ABJ=sub(ArB,J)
    M=B.transpose()*B; Mi=M.inv()
    Q=lambda X: X-B*(Mi*(B.transpose()*X))
    QG=Q(GBJ); QC=Q(CBJ); QA=Q(ABJ)
    PGP=B.transpose()*GBJ; PGP=(PGP+PGP.transpose())/2
    Mm=M2mp(M); Pm=M2mp(PGP)
    ev,(V,_)=geig(Pm,Mm); aJ=ev[0]
    K=M2mp(QG.transpose()*QG); KC=M2mp(QC.transpose()*QC); KA=M2mp(QA.transpose()*QA)
    cJ=mp.sqrt(geig(K,Mm)[0][-1]); cC=mp.sqrt(geig(KC,Mm)[0][-1]); cA=mp.sqrt(geig(KA,Mm)[0][-1])
    # b_J and (QGQ)^{-1}: deflated matrix K = QGQ + σP (σ = 10) has spec = spec(QGQ|V^⊥) ∪ {σ}; K^{-1} = (QGQ|V^⊥)^{-1} ⊕ σ^{-1}P.
    # (The route via G^{-1} − G^{-1}B(B^TG^{-1}B)^{-1}B^TG^{-1} loses the O(1) block under the 1/λ* ≈ 2·10⁶⁹ component for J ≥ 10.)
    PG=B*(Mi*(B.transpose()*G)); Pr=B*(Mi*B.transpose())
    Kd=G-PG-PG.transpose()+B*(Mi*(PGP*(Mi*B.transpose())))+10*Pr
    Ki=Kd.inv(); print(' Ki',J,time.time()-t0,flush=True)
    x=Q(arb_mat([[arb(np.sin(1.3*i+0.7))] for i in range(d)])); rq_hist=[]
    for it in range(200):
        y=Q(Ki*x); rq=(x.transpose()*y)[0,0]/(x.transpose()*x)[0,0]; rq_hist.append(rq)
        nr=(y.transpose()*y)[0,0].sqrt(); x=arb_mat([[(y[i,0]/nr).mid()] for i in range(d)])
        if it>8 and abs(rq_hist[-1]-rq_hist[-2])<abs(rq_hist[-1])*arb(10)**-25: break
    b_arb=1/rq_hist[-1]
    # double cross-check of b_J (adequate when b_J = O(1))
    Bd=np.array([[float(B[i,j].mid().str(20,radius=False)) for j in range(J)] for i in range(d)])
    U_,_=np.linalg.qr(Bd); Z=np.linalg.svd(np.eye(d)-U_@U_.T)[0][:,:d-J]; eZ=np.linalg.eigvalsh(Z.T@Gd@Z)
    bJ=mp.mpf(b_arb.mid().str(40,radius=False))
    thJ=geig(K,Pm)[0][-1]/bJ
    # exact Schur ratio θ'_J = λ_max(T,PGP), T = (QGP)^T H0 (QGP), explicit
    def H0(X): return Q(Ki*X)
    H0QG=H0(QG); T=M2mp(QG.transpose()*H0QG); T=(T+T.T)/2
    thp=geig(T,Pm)[0][-1]
    Ys=[H0QG]
    for k in range(3): Ys.append(H0(Ys[-1]))          # Ys[k] = H0^{k+1} QGP
    Sl=Pm-T; lk=arb(1)
    for k in range(1,5):                                 # term λ^k ⟨QGP, H0^{k+1} QGP⟩ = λ^k Ys[i]^T Ys[j], i+j+2 = k+1
        lk=lk*lst; i=(k-1)//2; j=k-1-i; Sl=Sl-M2mp(lk*(Ys[i].transpose()*Ys[j]))
    Sl=(Sl+Sl.T)/2
    sl=geig(Sl,Mm)[0]; lstm=mp.mpf(lst.mid().str(60,radius=False))
    # closed form check: S(0) = M N^{-1} M  → bottom 1/λ_max(N,M)
    s0=geig(Pm-T,Mm)[0][0]
    # bottom Ritz vector v_J: leakage-scale split of its coupling
    v=V[:,0]; vv=arb_mat([[arb(mp.nstr(v[i],130))] for i in range(J)])
    nG=(lambda X:((X*vv).transpose()*(X*vv))[0,0].sqrt())(QG); nC=((QC*vv).transpose()*(QC*vv))[0,0].sqrt(); nA=((QA*vv).transpose()*(QA*vv))[0,0].sqrt()
    nv=((B*vv).transpose()*(B*vv))[0,0].sqrt()
    f=lambda z: mp.nstr(z,22)
    r={'a_J':f(aJ),'a_J/W*':f(aJ/lstm),'a_J/(1-chi_4)':f(aJ/mp.mpf(om4.str(30,radius=False))),'ritz_2nd/W*':f(ev[1]/lstm) if J>1 else None,
       'b_J (arb power it.)':f(bJ),'b_J iterations':len(rq_hist),'b_J double':float(eZ[0]),'QGQ spec double max':float(eZ[-1]),
       'c_J=|QGP| op':f(cJ),'|QCP| op':f(cC),'|QArP| op':f(cA),'depth_op log10(|QCP|/|QGP|)':f(mp.log10(cC/cJ)),
       'theta_J (RC: |QGv|^2/(b_J<v,Gv>))':f(thJ),"theta'_J (exact Schur)":f(thp),'1-theta\'_J':f(1-thp),
       'Feshbach bottom S_J(λ*)/λ*':f(sl[0]/lstm),'Feshbach rel err':f(abs(sl[0]-lstm)/lstm),'S_J(0) bottom/λ*':f(s0/lstm),
       'Ritz v_J: |QGv|/|v|':f(mp.mpf(nG.mid().str(40,radius=False))/mp.mpf(nv.mid().str(40,radius=False))),
       'Ritz v_J: |QCv|/|v|':f(mp.mpf(nC.mid().str(40,radius=False))/mp.mpf(nv.mid().str(40,radius=False))),
       'Ritz v_J: |QArv|/|v|':f(mp.mpf(nA.mid().str(40,radius=False))/mp.mpf(nv.mid().str(40,radius=False))),
       'Ritz v_J: |QGv|^2/(b_J W(v))':f((mp.mpf(nG.mid().str(40,radius=False))**2/mp.mpf(nv.mid().str(40,radius=False))**2)/(bJ*aJ))}
    # coupling singular values on V_J (L² metric) for G, C, Ar
    r['sv QGP']=[mp.nstr(mp.sqrt(abs(z)),6) for z in geig(K,Mm)[0][::-1]][:8]
    res['J'][J]=r; print(J,json.dumps(r),time.time()-t0,flush=True)
    json.dump(res,open(OUT/'galerkin_2x2.json','w'),indent=1)
# projections of g* on V_J for the exterior step
pv={}
for J in (1,2,3,5,10,20,50):
    B=sub(Bas,J); M=B.transpose()*B; pJ=B*M.solve(B.transpose()*gs)
    pv[f'p{J}']=[pJ[i,0].mid().str(120,radius=False) for i in range(d)]
    pv[f'd{J}']=[(gs[i,0]-pJ[i,0]).mid().str(120,radius=False) for i in range(d)]
    W=lambda u,w:(u.transpose()*G*w)[0,0]
    dl=gs-pJ; res['J'][J]['W(p_J)/W*']=(W(pJ,pJ)/lst).str(15); res['J'][J]['W(p_J,δ_J)/W*']=(W(pJ,dl)/lst).str(15); res['J'][J]['W(δ_J)/W*']=(W(dl,dl)/lst).str(15)
pickle.dump({'pvecs':pv},open(SP/'t2x2_pvecs.pkl','wb'))
json.dump(res,open(OUT/'galerkin_2x2.json','w'),indent=1); print('done',time.time()-t0)
