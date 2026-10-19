import numpy as np
np.random.seed(0)
n=6
g=np.sort(np.random.uniform(5,40,n))
def moments(F,K=12):
    return np.array([sum(F[r,s]*g[s]**k for r in range(n) for s in range(n)) for k in range(K)])
F=np.random.randn(n,n)
# Delta with EXACTLY zero column sums (sum over axis 0): subtract column-mean from each entry
col_mean=F.mean(axis=0,keepdims=True)*0 + np.random.randn(1,n)*0  # placeholder
Delta=np.random.randn(n,n)
Delta=Delta-Delta.sum(axis=0,keepdims=True)/n          # now each column sums to 0
assert np.max(np.abs(Delta.sum(axis=0)))<1e-12, "column sums not zero"
Fp=F+Delta
M, Mp = moments(F), moments(Fp)
print("col-sum(Delta) max abs :", np.max(np.abs(Delta.sum(axis=0))))   # ~0
print("max |M_k - M'_k|       :", np.max(np.abs(M-Mp)))                 # ~0: SAME moments
print("max |F - F'| (kernel)  :", np.max(np.abs(F-Fp)))                 # >0: DIFFERENT kernel
D =np.array([[F [r,s]/(g[r]-g[s]) if r!=s else 0 for s in range(n)] for r in range(n)])
Dp=np.array([[Fp[r,s]/(g[r]-g[s]) if r!=s else 0 for s in range(n)] for r in range(n)])
print("max |D - D'| (operator):", np.max(np.abs(D-Dp)))                 # >0: D NOT determined
