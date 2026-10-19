# W^ev = A^ev + 2 phi phi^* spectrum. UNCERTIFIED float.
import sys,numpy as np, scipy.special as sp
import t2001_typeI_search as S
K=int(sys.argv[1])
for a in sys.argv[2:]:
    T,s2,s3=map(float,a.split(','))
    (A0,A2,A3),ph,P0=S.pieces(T,K); A=A0-s2*A2-s3*A3
    l=np.arange(0,K,2); phi=np.sqrt((2*l+1)/(2*T))*2*T*sp.spherical_in(l,0.5*T)
    print('check |phi|^2',phi@phi, np.sinh(T)+T)
    W=A+2*np.outer(phi,phi); nu,V=np.linalg.eigh(W); mu=np.linalg.eigvalsh(A)
    print(T,s2,s3,'W:',' '.join('%.2e'%v for v in nu[:4]),'| <v_j,phi^>:',' '.join('%+.1e'%(V[:,j]@ph) for j in range(3)),'| A:',' '.join('%.2e'%v for v in mu[:3]))
