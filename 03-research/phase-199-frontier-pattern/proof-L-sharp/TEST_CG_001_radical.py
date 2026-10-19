# TEST_CG_001 radical diagnostics: (i) Q-form on the radical span (must vanish: numerical validation of the pipeline);
# (ii) -Q(G,G) on the radical span; (iii) Schur version: 𝔔 vs min over radical shifts of -Q(G,G).
import sys, os, numpy as np
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'TEST_CG_001_analysis.py')).read().split('print("mu",mu')[0]
exec(src)
T=2000; QQ,QGG,S,QF,C0=forms(T)
print("# mu=%g T=%d"%(mu,T))
for Ju in Juse:
    Rc=np.zeros((nb,Ju)); Rc[K:K+Ju,:]=np.eye(Ju); Rc=gorth(Rc@null_of(d['g0'][K:K+Ju]),G)
    eQ=ev(QQ,Rc); eG=ev(-QGG,Rc); eF=ev(QF,Rc)
    # Schur: for v in PW constrained space (no projection), m(v)=min_r -QGG(v+r); compare with QQ(v)
    Pc=np.zeros((nb,K)); Pc[:K,:]=np.eye(K); Pc=gorth(Pc@null_of(d['g0'][:K]),G)
    Wall=np.hstack([Pc,Rc]); H=sym(Wall.T@(-QGG)@Wall); p=Pc.shape[1]
    Hrr=H[p:,p:]; Hpr=H[:p,p:]; er=np.linalg.eigvalsh(Hrr)
    Sch=H[:p,:p]-Hpr@np.linalg.pinv(Hrr,rcond=1e-12)@Hpr.T
    # also Schur of QQ (should equal QQ restricted, since radical is QQ-null)
    Q2=sym(Wall.T@QQ@Wall); 
    # gen eig of QQ_pp vs Sch on Pc (orthonormal in L2 but distance not used here)
    e,v=np.linalg.eigh(sym(Sch)); 
    if e.min()>0:
        L=v/np.sqrt(e); r=np.linalg.eigvalsh(sym(L.T@Q2[:p,:p]@L)); thS=np.abs(1-r).max()
    else: r=[np.nan]; thS=np.nan
    print("J=%2d rad dim %2d | max|QQ| on rad %.2e (QF scale %.2e) | -QGG on rad [%.3g .. %.3g] | Schur(-QGG) min %.4f, QQ/Schur in [%.4f, %.4f], theta_Schur %.4f"%(
        Ju,Rc.shape[1],np.abs(eQ).max(),np.abs(eF).max(),eG[0],eG[-1],e.min(),np.min(r),np.max(r),thS))
