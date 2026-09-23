"""R155.026 round 3c: parity split of V and the even-sector crude condition, N=18."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3a'))
import numpy as np, arch_core as ac
t0=time.time(); N=18; ac.Cmat.__defaults__=(100,); res={}
par=np.array([(-1)**k for k in range(N)])
for T in [0.58, 0.62, 0.65, float(np.log(2))]:
    G=ac.gamma_matrix(T,N,nu=120); Pl,a,b=ac.pole_matrix(T,N); Pi,A_T,ct=ac.prime_matrix(T,N)
    Q=np.column_stack([a,b]); U,s,_=np.linalg.svd(Q,full_matrices=True); Z=U[:,2:]
    Ainf=Z.T@G@Z; PiP=Z.T@Pi@Z; W=Ainf+PiP
    ev,V=np.linalg.eigh(Ainf); f=V[:,0]
    pv=[float(np.sum(par*(Z@V[:,j])*(Z@V[:,j]))) for j in range(V.shape[1])]
    p0=pv[0]
    same=[j for j in range(1,V.shape[1]) if pv[j]*p0>0]    # same parity as F* => coupled sector
    lam_even2=float(ev[same[0]])
    Y=V[:,1:]; w11=float(f@W@f); bv=Y.T@(W@f); c=float(np.linalg.norm(bv))
    Ys=V[:,same]; PiS=Ys.T@PiP@Ys
    crude_even=lam_even2-np.linalg.norm(PiS,2)-c*c/w11
    res['%.4f'%T]=dict(lam1=float(ev[0]),lam2=float(ev[1]),lam3=float(ev[2]),
        parity_F=p0, coupled_lam=lam_even2, w11=w11, c=c, c2_over_w11=c*c/w11,
        normPi_coupled=float(np.linalg.norm(PiS,2)), crude_even=float(crude_even),
        crude_even_nofaults=float(lam_even2-c*c/w11))
    print('T=%.4f lam2=%+.5f lam3=%+.5f coupled_lam=%+.5f c^2/w11=%.4f |Pi_even|=%.4f '
          'crude_even=%+.4f (without |Pi|: %+.4f)'%(T,ev[1],ev[2],lam_even2,c*c/w11,
          np.linalg.norm(PiS,2),crude_even,lam_even2-c*c/w11))
json.dump(res,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'r3c_04.json'),'w'),indent=1)
print('runtime %.1fs'%(time.time()-t0))
