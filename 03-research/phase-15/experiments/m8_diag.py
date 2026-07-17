import numpy as np
np.random.seed(0)
n=6
g=np.sort(np.random.uniform(5,40,n))
Delta=np.random.randn(n,n)
Delta=Delta-Delta.sum(axis=0,keepdims=True)/n
print("col sums:", np.round(Delta.sum(axis=0),12))
# direct: moments(Delta)[k] = sum_{r,s} Delta[r,s] g[s]^k  == sum_s (col_sum_s) g[s]^k == 0
for k in range(4):
    direct=sum(Delta[r,s]*g[s]**k for r in range(n) for s in range(n))
    viamarg=sum(Delta[:,s].sum()*g[s]**k for s in range(n))
    print(f"k={k}: moments(Delta)={direct:.6e}  via-marginal={viamarg:.6e}")
