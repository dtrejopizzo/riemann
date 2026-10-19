# BB_001 step 2 (NUMÉRICO, double on the V_50^⊥ block; right-hand sides from step 1 in arb, rescaled before conversion).
# Tests: (a) exact Feshbach δ = −(QGQ−λ*)^{-1}QGp; (b) Strategy-BB leading order δ_BB = (QArQ−λ*)^{-1}QCp (and (QGQ)^{-1}QCp);
# (c) energies ⟨QGp,R QGp⟩ vs W(δ); BB "depression" ⟨QCp,(QArQ)^{-1}QCp⟩ in units W*; (d) spectra of QArQ, QGQ on V_50^⊥;
# (e) Legendre spectrum of QCp (kink vs smooth content); (f) c-family: QG_c p = QGp + (1−c)QCp.
import json,os,numpy as np
from pathlib import Path
SP=Path(os.environ['SP'])/'bb'; S=json.load(open(SP/'split.json'))
G=np.load(SP/'G.npy'); C=np.load(SP/'C.npy'); B=np.load(SP/'Bas.npy'); Ar=G+C
P=__import__('pickle').load(open(SP.parent/'rc'/'pvecs.pkl','rb'))['pvecs']
dl=np.array([float(x) for x in P['delta']]); p=np.array([float(x) for x in P['p']])
Wst=4.763466135565557e-70; lam=Wst
v=lambda k,s=1.0: np.array([float(x) for x in S[k]])*s
QGp=v('QGp',1e35); QCp=v('QCp'); QArp=v('QArp')
U,_=np.linalg.qr(B); d=len(p); Z=np.linalg.svd(np.eye(d)-U@U.T)[0][:,:d-B.shape[1]]  # orthonormal basis of V^⊥
QGQ=Z.T@G@Z; QArQ=Z.T@Ar@Z; QCQ=Z.T@C@Z
eG=np.linalg.eigvalsh(QGQ); eA=np.linalg.eigvalsh(QArQ); eC=np.linalg.eigvalsh(QCQ)
out={'|QGp|':float(np.linalg.norm(QGp))*1e-35,'|QCp|':float(np.linalg.norm(QCp)),'|QArp|':float(np.linalg.norm(QArp)),
     'cancellation digits':float(np.log10(np.linalg.norm(QCp)/(np.linalg.norm(QGp)*1e-35))),
     'spec QGQ min/max':[float(eG[0]),float(eG[-1])],'spec QArQ min/max':[float(eA[0]),float(eA[-1])],'#neg QArQ':int((eA<0).sum()),
     'spec QCQ min/max':[float(eC[0]),float(eC[-1])],'|δ|':float(np.linalg.norm(dl))}
dz=Z.T@dl*1e35
dF=-np.linalg.solve(QGQ,Z.T@QGp)          # exact Feshbach (λ* negligible against spec QGQ)
cos=lambda a,b: float(a@b/np.linalg.norm(a)/np.linalg.norm(b))
out['Feshbach: |dF-δ|/|δ|']=float(np.linalg.norm(dF-dz)/np.linalg.norm(dz))
out['Feshbach energy <QGp,(QGQ)^-1 QGp>/W*']=float(-(Z.T@QGp)@dF*1e-70/Wst)
dBB=np.linalg.solve(QArQ,Z.T@QCp); dBB2=np.linalg.solve(QGQ,Z.T@QCp)
out['BB: |(QArQ)^-1 QCp|/|δ|']=float(np.linalg.norm(dBB)/(np.linalg.norm(dz)*1e-35)); out['BB cos(δ_BB,δ)']=cos(dBB,dz)
out['BB2: |(QGQ)^-1 QCp|/|δ|']=float(np.linalg.norm(dBB2)/(np.linalg.norm(dz)*1e-35)); out['BB2 cos']=cos(dBB2,dz)
out['BB depression <QCp,(QArQ)^-1QCp>/W*']=float((Z.T@QCp)@dBB/Wst)
out['BB2 depression <QCp,(QGQ)^-1QCp>/W*']=float((Z.T@QCp)@dBB2/Wst)
# Legendre spectrum (degree bands) of QCp and of δ
I=np.arange(0,1664,2); bands=[(0,50),(50,100),(100,200),(200,400),(400,800),(800,1664)]
def band(x): return {f'{a}-{b}':float(np.sum(x[(I>=a)&(I<b)]**2)/np.sum(x**2)) for a,b in bands}
out['spectrum QCp']=band(QCp); out['spectrum δ']=band(dl); out['spectrum QGp']=band(QGp)
out['cos(QGp,Gδ-direction check)']=cos(QGp,Z@ (QGQ@dz))
# c-family at fixed p: |QG_c p| = |QGp + (1-c)QCp|
out['|QG_c p| for c=0.9,0.99,1,1.01']={c:float(np.linalg.norm(QGp*1e-35+(1-c)*QCp)) for c in (0.9,0.99,1.0,1.01)}
json.dump(out,open(SP/'feshbach.json','w'),indent=1); print(json.dumps(out,indent=1))
