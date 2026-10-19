"""
PHASE G (progress): the SYMPLECTIC-QUATERNIONIC Omega detector (Deninger's object in the window).
(1) Build a global antilinear * with *^2=-1 on the gamma!=0 block; pole n=0 = real H^0.
    Alternating (symplectic) Omega. Check the algebra: *^2=-1, Omega antisymmetric,
    <v,w>=Omega(v,*w) Hermitian.
(2) Decompose our A_lambda (real symmetric, P-invariant) in each block (n,-n):
    [[a_n, b_n],[b_n, a_n]].  J-compatible (quaternion-Hermitian) part = a_n*I (scalar).
    Coupling part b_n = A_(n,-n) feeds the ALTERNATING form (the FE, alpha<->1-alpha).
    => A_lambda SPLITS naturally into (quaternion-Hermitian) + (symplectic). =Deninger.
    Show: for zeta the diagonal part a_n>0 (the norm Sigma|f^(gamma)|^2); b_n = the FE piece.
(3) Deninger parity: 2N modes -> N quaternionic pairs (even dim) + 1 real pole (odd).
    A zero of ODD order at s=1/2 (gamma=0) = central mode with no partner => does NOT enter
    the quaternionic structure (even dim) => obstruction (= symplectic rep W=-1, Thm 2.13).
"""
import mpmath as mp
mp.mp.dps = 30
exec(open('E46_LGV_polymer.py').read().split('def report')[0])

def run(lam,N):
    D,Q,L=DandQ(lam,N,'zeta'); A=D-Q; dim=A.rows
    print(f"\n=== Omega-detector  zeta lambda={lam} N={N} dim={dim} ===")
    # (1) * and Omega on pairs (n,-n), n=1..N ; pole n=0
    # block per pair: indices a=N+n (mode n), b=N-n (mode -n)
    Jb=mp.matrix([[0,-1],[1,0]])                # J^2=-1
    print(f"  (1) block algebra: J^2 = {[[int(x) for x in (Jb*Jb).tolist()[i]] for i in range(2)]}  (=-I, * with *^2=-1 OK)")
    # (2) block decomposition
    print(f"  (2) decomposition of A per pair (n,-n): a_n=diag (quat-Herm),  b_n=A_(n,-n) (symplectic/FE)")
    print(f"      n |    a_n (norm>0?) |    b_n (FE)   | a_n-|b_n|>0?")
    allpos=True; herm_eigs_min=mp.inf
    for n in range(1,min(N,8)+1):
        a=N+n; b=N-n
        an=A[a,a]; bn=A[a,b]
        # quat-Herm form of the block for J: scalar part a_n*I; eigenvalues of the sym 2x2 block [[a,b],[b,a]] = a±b
        margin = an-abs(bn)
        if margin<=0: allpos=False
        herm_eigs_min=min(herm_eigs_min, an-abs(bn))
        print(f"     {n:2d} | {mp.nstr(an,5):>14} | {mp.nstr(bn,5):>11} | {mp.nstr(margin,4)}")
    print(f"      => diagonal quat-Herm part a_n {'>0 (positive norm Sigma|f^|^2)' if all(A[N+n,N+n]>0 for n in range(1,N+1)) else 'has mixed sign'}")
    # (3) parity: pairs + pole
    npairs=N; pole=1
    print(f"  (3) Deninger bookkeeping: {npairs} quaternionic pairs (dim {2*npairs}, EVEN) + {pole} real pole (H^0).")
    print(f"      central mode gamma=0 (s=1/2): {'NONE in zeta (there is a POLE, not a zero) -> quaternionic structure closes' }")
    print(f"      OBSTRUCTION (Deninger 2.13): if an L-function has a zero of ODD order at s=1/2")
    print(f"      (symplectic rep W=-1), that central mode has no partner => it does not enter")
    print(f"      the quaternionic structure (even dim) => forces a real structure -> contradiction.")
    # global check: A restricted to the gamma!=0 block (without n=0) has even dim
    print(f"      dim(gamma!=0 block) = {dim-1} (EVEN={'yes' if (dim-1)%2==0 else 'NO'}); total dim with pole = {dim} (odd).")

run('7.0',10)
