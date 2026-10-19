import numpy as np
np.random.seed(1)
n=6
g=np.sort(np.random.uniform(0,1,n))   # normalize to [0,1] so g^k doesn't amplify roundoff
mom=lambda F,K=10: np.array([sum(F[r,s]*g[s]**k for r in range(n) for s in range(n)) for k in range(K)])
F=np.random.randn(n,n)
Delta=np.random.randn(n,n); Delta-=Delta.sum(axis=0,keepdims=True)/n   # zero column sums
Fp=F+Delta
M,Mp=mom(F),mom(Fp)
relM=np.max(np.abs(M-Mp))/np.max(np.abs(M))
D =np.array([[F [r,s]/(g[r]-g[s]) if r!=s else 0 for s in range(n)] for r in range(n)])
Dp=np.array([[Fp[r,s]/(g[r]-g[s]) if r!=s else 0 for s in range(n)] for r in range(n)])
print(f"relative moment difference |M-M'|/|M| : {relM:.2e}   (= same moments)")
print(f"kernel difference        |F-F'|       : {np.max(np.abs(F-Fp)):.3f}   (= different kernel)")
print(f"OPERATOR difference      |D-D'|       : {np.max(np.abs(D-Dp)):.3f}   (= D NOT determined)")
print("\n=> Theorem 3.1 FALSE: {M_k} fixes only the marginal sum_rho F(.,sigma);")
print("   the off-diagonal D_{rho sigma} needed by Sections 4-8 is underdetermined.")
