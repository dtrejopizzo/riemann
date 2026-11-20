"""Enclose optimal binomial coefficient costs; HiGHS only proposes witnesses."""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, vstack
from flint import arb, ctx

ctx.prec = 128
scale = 10**9

def prime_power(m):
    d = next((d for d in range(2, m + 1) if m % d == 0), m)
    while m % d == 0:
        m //= d
    return m == 1

def bounds(x, atomic):
    N = 2*x
    coords = [m for m in range(2, N+1) if not atomic or prime_power(m)]
    pairs = [(n,k) for n in range(2,N+1) for k in range(1,n//2+1)]
    carry = np.array([[n//m - k//m - (n-k)//m for m in coords]
                      for n,k in pairs], dtype=np.int64)
    def weight(m):
        if m <= x or m >= N:
            return arb(0)
        ratio = arb(m)/x
        return (1 - (2*arb.pi()*ratio.log()/arb(2).log()).cos())/ratio.sqrt()
    g = [weight(m) for m in coords]
    D = csr_matrix(carry)
    cons = vstack([D,-D],format='csr')
    opt = linprog(-np.array([float(v) for v in g]), A_ub=cons,
                  b_ub=np.ones(cons.shape[0]), bounds=(None,None),method='highs')
    if not opt.success:
        raise RuntimeError(opt.message)
    z = [round(float(v)*scale) for v in opt.x]
    # Integer products are done in Python; no fixed-width overflow.
    denom = max(scale, max(abs(sum(z[i] for i in row.nonzero()[0]))
                            for row in carry))
    lower = sum(v*t for v,t in zip(g,z))/denom
    marg = opt.ineqlin.marginals
    coeff = [round(float(marg[i+len(pairs)]-marg[i])*scale)
             for i in range(len(pairs))]
    values = [0]*len(coords)
    for a,row in zip(coeff,carry):
        if a:
            for i in row.nonzero()[0]:
                values[i] += a
    upper = arb(sum(abs(a) for a in coeff))/scale
    for m,v,num in zip(coords,g,values):
        divisor_count = sum(m % d == 0 for d in range(1,m+1))
        upper += (2 if atomic else divisor_count)*abs(v-arb(num)/scale)
    lo = int((1000*lower).floor().unique_fmpz())
    hi = int((1000*upper).ceil().unique_fmpz())
    assert upper - lower < arb('0.0001')
    return f'[{lo}/1000, {hi}/1000]'

if __name__ == '__main__':
    for x in (16,32,64):
        print(x, 'prime powers', bounds(x,True), 'all integers', bounds(x,False),
              flush=True)
