"""Analytic polynomial upper bound for BUILD083 q at T=4/5.

All integrals are polynomial or explicit logarithmic moments. No quadrature.
With ctx=mpmath.iv, bounds include the positive tail of the cosh series.
"""
from math import comb, factorial
import mpmath as mm

def add(p,q):
    r = [0]*max(len(p),len(q))
    for i,x in enumerate(p): r[i] += x
    for i,x in enumerate(q): r[i] += x
    return r

def mul(p,q):
    r = [0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j] += x*y
    return r

def integral(p,a,b):
    return sum(x*(b**(i+1)-a**(i+1))/(i+1) for i,x in enumerate(p))

def shift(p,h):
    r = [0]*len(p)
    for i,x in enumerate(p):
        for j in range(i+1): r[j] += x*comb(i,j)*h**(i-j)
    return r

def polynomial(n):
    # P_n(2z-1), exactly integer coefficients.
    return [(-1)**(n-k)*comb(n,k)*comb(n+k,k) for k in range(n+1)]

def build(ctx, degree, interval=False):
    T = ctx.mpf(4)/5
    one = ctx.mpf(1)
    zero = ctx.mpf(0)
    def harmonic(n): return sum(one/k for k in range(1,n+1))
    def cosh_moment(k):
        a = T/2
        M = 32
        value = sum(a**(2*m)/(factorial(2*m)*(k+2*m+1)) for m in range(M))
        next_term = a**(2*M)/(factorial(2*M)*(k+2*M+1))
        tail = next_term/(1-a*a/((2*M+1)*(2*M+2)))
        return value + (ctx.mpf([0,1])*tail if interval else tail/2)
    denominator = cosh_moment(0)
    basis = []
    for n in range(1,degree+1):
        p = [ctx.mpf(c) for c in polynomial(n)]
        correction = sum(c*cosh_moment(k) for k,c in enumerate(p))/denominator
        p[0] -= correction
        basis.append(p)
    def log_moment(k):
        # integral_0^1 z^k log(1-z^2) dz.
        if k%2:
            return -harmonic((k+1)//2)/(k+1)
        m = k//2
        return (2*ctx.log(2)-2*harmonic(2*m+2)+harmonic(m+1))/(k+1)
    def divided(p):
        return [(i-1-k,k,c) for i,c in enumerate(p) if i for k in range(i)]
    def difference_integral(p,q):
        value = zero
        for i,j,c in divided(p):
            for k,l,d in divided(q):
                u,v = i+k,j+l
                factor = (one/((v+1)*(v+2))+one/((u+1)*(u+2)))/(u+v+3)
                value += c*d*factor
        return value
    alternating = [ctx.log(2)]
    for k in range(1,2*degree+1):
        alternating.append(one/k-alternating[-1])
    def cauchy_monomial(u,v):
        return (alternating[u]+alternating[v])/(u+v+1)
    def reflected_integral(p,q):
        value = zero
        for i,j,c in divided(p):
            for k,l,d in divided(q):
                u,v = i+k,j+l
                value += c*d*(cauchy_monomial(u+2,v)-2*cauchy_monomial(u+1,v+1)+cauchy_monomial(u,v+2))
        return value
    cbar = -ctx.euler-ctx.log(2*ctx.pi)+T/4-ctx.log(T)
    def upper(p,q):
        pq = mul(p,q)
        gram = integral(pq,zero,one)
        val = cbar*T*gram - T/2*sum(c*log_moment(k) for k,c in enumerate(pq))
        val += T/4*(difference_integral(p,q)+reflected_integral(p,q))
        val += T*T/2*(gram-integral(p,zero,one)*integral(q,zero,one))
        for n,prime in [(2,2),(3,3),(4,2)]:
            length = ctx.log(n)
            weight = ctx.log(prime)/ctx.sqrt(n)
            if n==2:  # log2 < 4/5 < log3, log4.
                d = length/T
                cross = integral(mul(p,shift(q,-d)),d,one)
                cross += integral(mul(q,shift(p,-d)),d,one)
                val -= weight*T*cross
                val -= weight*T*integral(pq,zero,d)
            else:
                val -= weight*T*gram
        return val
    matrix = [[zero for _ in basis] for _ in basis]
    for i,p in enumerate(basis):
        for j in range(i+1):
            matrix[i][j] = matrix[j][i] = upper(p,basis[j])
    return matrix,basis

if __name__=='__main__':
    import numpy as np
    mm.mp.dps = 60
    matrix,basis = build(mm.mp,8)
    values,vectors = np.linalg.eigh(np.array(matrix,dtype=float))
    print('Exploratory upper-matrix eigenvalues:',values.tolist())
    print('First two eigenvectors (columns):',vectors[:,:2].tolist())
