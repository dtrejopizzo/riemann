# P2_GAUGE_RADICAL_001 analysis: gauge restriction of 𝒲_a, D_a = 𝒲_a|_𝒢 = Σ_n 2(Λ(n)-a(n))/√n c_Φ(log n)  (exact given Guo L4.4)
import numpy as np, json, sys
out={}
for mu in (5,10,15):
    d=np.load(f'gauge_mu{mu}.npz'); ns=d['atoms_n']; At=d['atoms']; arch=d['arch']; AB=d['AB']; combL=d['combL']
    def p_of(n):
        for p in range(2,n+1):
            if n%p==0: return p
    P=np.array([p_of(int(n)) for n in ns]); L=np.log(P); w=2*L/np.sqrt(ns)
    fals={'0.9Λ':w*0.1,'1.1Λ':w*(-0.1),'2Λ':w*(-1.0),'a_{2}':w*(P==2),'a_{2,3}':w*np.isin(P,[2,3]),
          'zero comb':w,'Λ−δ_3':w*(ns==3),'Λ−δ_7':w*(ns==7),'Λ−δ_2':w*(ns==2)}
    WL=arch-combL+AB; eWL=np.linalg.eigvalsh(WL)
    r={'Mg':int(arch.shape[0]),'W_Λ|G eig range':[float(eWL.min()),float(eWL.max())],
       'arch|G eig':np.linalg.eigvalsh(arch).round(5).tolist(),'(arch+2AB)|G eig':np.linalg.eigvalsh(arch+AB).round(5).tolist(),
       'combΛ|G eig':np.linalg.eigvalsh(combL).round(5).tolist()}
    for k,coef in fals.items():
        D=np.tensordot(coef,At,1); e=np.linalg.eigvalsh(D)
        r[k]={'min':float(e.min()),'max':float(e.max()),'n-':int((e<-1e-9).sum()),'n+':int((e>1e-9).sum()),
              'sigma_min':float(np.abs(e).min()),'d_a(defect)':float(max(0,-e.min())),'eig':e.tolist()}
    out[mu]=r
json.dump(out,open('analysis.json','w'),indent=1)
for mu,r in out.items():
    print('mu',mu,'Mg',r['Mg'],'WΛ|G',r['W_Λ|G eig range']); print(' arch',r['arch|G eig']); print(' comb',r['combΛ|G eig'])
    for k,v in r.items():
        if isinstance(v,dict): print(f"  {k:10s} min {v['min']:.4e} max {v['max']:.4e} n-/n+ {v['n-']}/{v['n+']} σmin {v['sigma_min']:.3e}")
