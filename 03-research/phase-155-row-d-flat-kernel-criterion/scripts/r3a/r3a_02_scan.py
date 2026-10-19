"""lambda^inf_min(T) (archimedean only: pole+gamma), lambda^{inf,P}_min(T) (restricted to P_T),
number of negative eigenvalues, ||P_T||, and lambda_min of the full forms. Usage: r3a_02_scan.py T1 T2 ..."""
import sys, os, time; sys.path.insert(0, os.path.dirname(__file__))
import numpy as np, arch_core as ac
t0 = time.time(); N = 18; ac.Cmat.__defaults__ = (100,)
print('   T     lam^inf_min   lam^{inf,P}_min  n_neg(A_inf) n_neg(A_inf|P)   ||P_T||    A_T    lam_min(a_T|P_T)  lam_min(W_T)')
for T in [float(s) for s in sys.argv[1:]]:
    G = ac.gamma_matrix(T, N, nu=120); P, a, b = ac.pole_matrix(T, N)
    Pi, A_T, ct = ac.prime_matrix(T, N)
    eA = np.linalg.eigvalsh(G+P); eAP = np.linalg.eigvalsh(ac.restrict(G, a, b))
    print('%6.3f %+13.6e %+13.6e %8d %10d %12.5f %8.4f %+13.6e %+13.6e'
          % (T, eA[0], eAP[0], int((eA < 0).sum()), int((eAP < 0).sum()),
             np.linalg.norm(Pi, 2), A_T,
             np.linalg.eigvalsh(ac.restrict(G+Pi, a, b))[0], np.linalg.eigvalsh(G+P+Pi)[0]))
print('runtime %.1fs (N=%d)' % (time.time()-t0, N))
