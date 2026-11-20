import sys, numpy as np, scipy.linalg as sl
exec(open('cellRg.py').read().split('Vn=sl.null_space')[0].replace("R=int(sys.argv[1]); Nb=int(sys.argv[2]); T=float(sys.argv[3]); J=int(sys.argv[4])","R=2; Nb=int(sys.argv[1]); T=float(sys.argv[2]); J=0"))
beta=2.3784
Qa=Tm.T@Ar@Tm   # first cell: comb-free Levy form (Q of 17C)
Cn=C/np.linalg.norm(C,axis=0)   # coefficient vectors of weights (|w| approx)
U,_=np.linalg.qr(Cn)
print(T,Nb,"q_W = lam_max (Q+beta) on span W:",np.linalg.eigvalsh(U.T@(Qa+beta*np.eye(Nb))@U).max(), "captured norm of weights",np.linalg.norm(C,axis=0)**2/np.array([np.trapz(xi*fun[k]**2,z) for k in fun]))
