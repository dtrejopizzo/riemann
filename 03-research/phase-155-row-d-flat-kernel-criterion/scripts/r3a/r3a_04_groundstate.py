"""Prime term evaluated on the archimedean ground states; deficits; trivial bound."""
import sys, os, time; sys.path.insert(0, os.path.dirname(__file__))
import numpy as np, arch_core as ac
t0 = time.time(); N = 18; ac.Cmat.__defaults__ = (100,)
print('T        lam^inf   lam^infP   P_T(F*_inf)  W_T(F*_inf)  P_T(F*_P)  a_T(F*_P)   ||P_T||   triv=lam^inf-||P||   lam_min(W_T)  lam_min(a_T|P_T)')
for T in [0.5*np.log(3), 0.58, np.log(2)]:
    G = ac.gamma_matrix(T, N, nu=120); P, a, b = ac.pole_matrix(T, N)
    Pi, A_T, ct = ac.prime_matrix(T, N)
    w, V = np.linalg.eigh(G+P); x = V[:, 0]
    Q = np.column_stack([a, b]); U, s, _ = np.linalg.svd(Q, full_matrices=True); Z = U[:, 2:]
    wp, Vp = np.linalg.eigh(Z.T @ G @ Z); y = Z @ Vp[:, 0]
    print('%.4f %+9.5f %+9.5f  %+10.5f  %+10.5f  %+9.5f  %+9.5f  %8.5f  %+12.5f  %+11.4e  %+11.4e'
          % (T, w[0], wp[0], x@Pi@x, x@(G+P+Pi)@x, y@Pi@y, y@(G+Pi)@y, np.linalg.norm(Pi,2),
             w[0]-np.linalg.norm(Pi,2), np.linalg.eigvalsh(G+P+Pi)[0],
             np.linalg.eigvalsh(ac.restrict(G+Pi,a,b))[0]))
print('runtime %.1fs' % (time.time()-t0))
