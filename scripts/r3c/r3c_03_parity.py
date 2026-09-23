"""R155.026 round 3c: parity structure of the Schur complement at T = log 2 (N=18)."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3a'))
import numpy as np, arch_core as ac
t0=time.time(); T=float(np.log(2)); N=18; ac.Cmat.__defaults__=(100,)
G=ac.gamma_matrix(T,N,nu=120); Pl,a,b=ac.pole_matrix(T,N); Pi,A_T,ct=ac.prime_matrix(T,N)
Q=np.column_stack([a,b]); U,s,_=np.linalg.svd(Q,full_matrices=True); Z=U[:,2:]
Ainf=Z.T@G@Z; W=Ainf+Z.T@Pi@Z
ev,V=np.linalg.eigh(Ainf); f=V[:,0]
par=np.array([(-1)**k for k in range(N)])            # parity of Legendre basis
def parity(v):
    w=Z@v; return float(np.sum((par*w)*w))           # +1 even, -1 odd
print('lam_1..5(A_inf|P_T):', np.round(ev[:5],6))
print('parity of F* and of the next four archimedean eigenvectors:',
      [round(parity(V[:,j]),4) for j in range(5)])
Y=V[:,1:]; WV=Y.T@W@Y; bv=Y.T@(W@f); w11=float(f@W@f)
S=WV-np.outer(bv,bv)/w11
evS,VS=np.linalg.eigh(S)
g=VS[:,0]
print('w11=%.6f  lam_min(S)=%.4e  parity of S ground state=%.4f'%(w11,evS[0],parity(Y@g)))
print('|b| components on archimedean eigvecs 2..6:', np.round(bv[:5],5))
# odd sector decouples?
odd=[j for j in range(1,V.shape[1]) if parity(V[:,j])<0]
print('cross terms W(F*, odd eigvecs) max abs: %.2e'%max(abs(float(f@W@V[:,j])) for j in odd))
json.dump(dict(ev=list(map(float,ev[:6])), w11=w11, lamS=float(evS[0]),
               parity_F=parity(f), parity_Sgs=parity(Y@g)),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'r3c_03.json'),'w'),indent=1)
print('runtime %.1fs'%(time.time()-t0))
