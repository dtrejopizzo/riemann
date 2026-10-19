# TEST_CG_001 analysis: constrained space (ghat(0)=0, L2(1,inf)-orthogonal to the radical span), spectra, theta, rank.
# Usage: python3 TEST_CG_001_analysis.py OUT.npz [Jused ...]
import sys, numpy as np
np.set_printoptions(precision=5,linewidth=160)
d=np.load(sys.argv[1]); K=int(d['K']); J=int(d['J']); mu=float(d['mu']); nb=K+J
Juse=[int(x) for x in sys.argv[2:]] or [J]
G=d['Gram']; A,B=d['A'],d['B']; AB=np.outer(A,B)+np.outer(B,A)
sym=lambda M:(M+M.T)/2
def null_of(c):  # orthonormal basis of {x: c.x=0}
    u,s,vt=np.linalg.svd(c[None,:]); return vt[1:].T
import os
CUT=float(os.environ.get("CG_CUT","1e-11"))
def gorth(W,G,cut=None):
    cut=CUT if cut is None else cut
    g=W.T@G@W; e,v=np.linalg.eigh(sym(g)); k=e>cut*e.max(); return W@v[:,k]/np.sqrt(e[k])
def basis(Ju,proj=True):
    Pc=np.zeros((nb,K)); Pc[:K,:]=np.eye(K); Pc=Pc@null_of(d['g0'][:K])
    if Ju==0 or not proj: return gorth(Pc,G)
    Rc=np.zeros((nb,Ju)); Rc[K:K+Ju,:]=np.eye(Ju); Rc=Rc@null_of(d['g0'][K:K+Ju]); Rc=gorth(Rc,G)
    W=Pc-Rc@(Rc.T@G@Pc); return gorth(W,G)
def forms(T,which='c'):
    QF=sym(d['QFt_%d'%T]); C0=d['C0%st_%d'%(which,T)]
    QGG=QF-C0-C0.T; S=2*QF-(C0+C0.T)+AB; QQ=QF+AB
    return QQ,QGG,S,QF,C0
def ev(M,U): return np.linalg.eigvalsh(sym(U.T@M@U))
print("mu",mu,"K",K,"J",J)
for T in (500,1000,2000):
    a,b,c=[forms(T,w)[4] for w in 'clo']
    print("T",T,"C0 contour vs line |diff|/|C0|: %.2e  vs old-style %.2e"%(np.abs(a-b).max()/np.abs(a).max(),np.abs(a-c).max()/np.abs(a).max()))
for Ju in Juse:
  for proj in ([True,False] if Ju==Juse[0] else [True]):
    U=basis(Ju,proj); print("\n=== radical span J=%d proj=%s  dim=%d"%(Ju,proj,U.shape[1]))
    for T in (500,1000,2000):
        QQ,QGG,S,QF,C0=forms(T)
        eQ=ev(QQ,U); eG=ev(-QGG,U); eS=ev(S,U)
        print("T=%d"%T); print(" eig QQ   ",eQ); print(" eig -QGG ",eG); print(" eig 2QFG+2AB",eS)
        g=sym(U.T@(-QGG)@U); e,v=np.linalg.eigh(g)
        if e.min()>0:
            L=v/np.sqrt(e); th=np.linalg.eigvalsh(sym(L.T@U.T@S@U@L)); print(" theta spectrum",th," theta=%.4g"%np.abs(th).max())
        else: print(" -QGG not PD: min",e.min())
        # rank / pole-range of sym Q(F,G)
        QFG=sym(QF-C0.T); M=U.T@QFG@U; sv=np.linalg.svd(M,compute_uv=False); print(" sv symQ(F,G)",sv[:8])
        Pf=np.array([A,B,d['R1'],d['FL1']])@U
        for k in (2,4):
            uu,ss,vt=np.linalg.svd(Pf[:k]); Pp=np.eye(U.shape[1])-vt[:k].T@vt[:k]
            print("  |P⊥ QFG P⊥|/|QFG| with %d pole functionals: %.3e"%(k,np.linalg.norm(Pp@M@Pp,2)/np.linalg.norm(M,2)))
