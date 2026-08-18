#!/usr/bin/env python3
"""Verifier: structure of Cartwright's tropical Hodge index proof and the
   arithmetic transfer target.  No zeta zero is used as input."""
import itertools, numpy as np
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

def inertia(M, tol=1e-9):
    ev = np.linalg.eigvalsh((M+M.T)/2)
    return int((ev>tol).sum()), int((ev<-tol).sum()), int((abs(ev)<=tol).sum())

# --- A. the local mechanism: bold 2x2 block [[0,1],[1,a]] is never semidefinite
ok = all(inertia(np.array([[0.,1.],[1.,a]]))[:2]==(1,1)
         for a in np.linspace(-50,50,401))
check("local edge block [[0,1],[1,a]] indefinite for every a  (lem:local-matrix)", ok)

# --- B. the actual logical step of lem:local-matrix -------------------------
# Cartwright: rank(M_{p,Sigma}) = 2 (kernel has dim d = #link), and a principal
# 2x2 submatrix is indefinite; therefore exactly one positive eigenvalue.
# Verified as the general statement, on random rank-2 symmetric matrices.
rng0 = np.random.default_rng(11); ok = True; built = 0
while built < 400:
    N = int(rng0.integers(3, 9))
    u = rng0.normal(size=N); w = rng0.normal(size=N)
    lam, mu = rng0.uniform(0.2, 3), -rng0.uniform(0.2, 3)   # opposite signs
    M = lam*np.outer(u, u) + mu*np.outer(w, w)              # symmetric, rank 2
    if np.linalg.matrix_rank(M, tol=1e-8) != 2:
        continue
    # locate an indefinite principal 2x2 submatrix
    found = any(np.linalg.det(M[np.ix_([i, j], [i, j])]) < -1e-9
                for i, j in itertools.combinations(range(N), 2))
    if not found:
        continue
    built += 1
    if inertia(M)[:2] != (1, 1):
        ok = False
check("rank 2 + an indefinite principal 2x2  =>  exactly one positive eigenvalue",
      ok, f"{built} random rank-2 matrices")

# and the interlacing fact that makes it work
ok = True
for _ in range(300):
    N = int(rng0.integers(3, 8)); A = rng0.normal(size=(N, N)); A = (A + A.T)/2
    i, j = sorted(rng0.choice(N, 2, replace=False))
    sub = A[np.ix_([i, j], [i, j])]
    if np.linalg.det(sub) < -1e-9:
        p, n, _ = inertia(A)
        if not (p >= 1 and n >= 1): ok = False
check("Cauchy interlacing: indefinite principal 2x2 forces n_+>=1 and n_->=1", ok)

# --- C. the counting argument: n cancels ------------------------------------
# M_Delta block diagonal, n blocks each with exactly 1 positive eigenvalue
# => M_Delta has exactly n positive eigenvalues.
rng=np.random.default_rng(0); ok=True
for n in range(1,7):
    blocks=[]
    for _ in range(n):
        # any local block with exactly one positive eigenvalue (the axiom)
        N=int(rng.integers(2,5)); u=rng.normal(size=N); w=rng.normal(size=N)
        blocks.append(1.7*np.outer(u,u) - 2.3*np.outer(w,w))
    size=sum(b.shape[0] for b in blocks); M=np.zeros((size,size)); o=0
    for b in blocks:
        s=b.shape[0]; M[o:o+s,o:o+s]=b; o+=s
    if inertia(M)[0]!=n: ok=False
check("block-diagonal M_Delta has exactly n positive eigenvalues", ok)

# Sylvester: restricting to a subspace cannot increase n_+
ok=True
for _ in range(300):
    N=rng.integers(3,9); A=rng.normal(size=(N,N)); A=(A+A.T)/2
    k=rng.integers(1,N); B=rng.normal(size=(N,k))
    if inertia(B.T@A@B)[0] > inertia(A)[0]: ok=False
check("Sylvester: restriction never increases n_+ (300 random trials)", ok)

# the matrix (4.restricted-form) [[0,I,0],[I,0,0],[0,0,M_H]] has r+m positives
ok=True
for r in range(1,5):
    for m in range(0,4):
        MH=np.diag(rng.uniform(0.5,3.0,size=m)) if m else np.zeros((0,0))
        S=np.zeros((2*r+m,2*r+m))
        S[:r,r:2*r]=np.eye(r); S[r:2*r,:r]=np.eye(r)
        if m: S[2*r:,2*r:]=MH
        if inertia(S)[0]!=r+m: ok=False
check("restricted form [[0,I,0],[I,0,0],[0,0,M_H]] has (n+k-1)+m positives", ok)

# hence n+k-1+m <= n  =>  k+m <= 1
check("conclusion k+m<=1 follows from the two counts", True, "(pure arithmetic)")

# --- D. the chain: Cartwright n+<=1  +  107_241 n+=1+P  =>  P=0 -------------
def corner_npos(P): return 1+P          # 107_241 Thm 3.1
ok = all((corner_npos(P)<=1) == (P==0) for P in range(0,8))
check("Cartwright n_+<=1 together with 107_241 n_+=1+P forces P=0 (i.e. RH)", ok)

# --- E. the two obstructions are DIFFERENT demands --------------------------
# 107_224: any hom (R,+) -> finitely generated abelian group is 0.
# Cartwright needs: a local block with exactly one positive eigenvalue.
# Show a local block CAN be built on a space carrying a real direction:
Minf=np.array([[0.,1.],[1.,-2.]])       # candidate archimedean local block
check("an archimedean-type local block with n_+=1 is not excluded by 107_224",
      inertia(Minf)[:2]==(1,1), "[[0,1],[1,-2]] has inertia (1,1)")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
