import numpy as np, math
from math import log, sqrt

# ---------- Dirichlet machinery ----------
def dirichlet_inverse(a, N):
    """a[1..N] with a[1]=1 -> b with (a*b)(n)=[n==1]"""
    b = np.zeros(N+1)
    b[1] = 1.0/a[1]
    for n in range(2, N+1):
        s = 0.0
        d = 1
        while d*d <= n:
            if n % d == 0:
                e = n//d
                if d != n: s += a[e]*b[d]
                if e != n and e != d: s += a[d]*b[e]
            d += 1
        b[n] = -s/a[1]
    return b

def dirichlet_conv(a, b, N):
    c = np.zeros(N+1)
    for d in range(1, N+1):
        if a[d] == 0: continue
        for e in range(1, N//d + 1):
            c[d*e] += a[d]*b[e]
    return c

def lambda_of(a, N):
    """coefficients of -f'/f  where f = sum a_n n^-s"""
    alog = np.zeros(N+1)
    for n in range(1, N+1):
        alog[n] = a[n]*log(n)
    b = dirichlet_inverse(a, N)
    return dirichlet_conv(alog, b, N)

# ---------- zeta ----------
def a_zeta(N):
    a = np.ones(N+1); a[0]=0; return a

# ---------- Davenport-Heilbronn ----------
def a_dh(N):
    xi = (sqrt(10-2*sqrt(5)) - 2)/(sqrt(5)-1)
    per = [0.0, 1.0, xi, -xi, -1.0, 0.0]   # a_1..a_5, index by n mod 5
    a = np.zeros(N+1)
    for n in range(1, N+1):
        r = n % 5
        a[n] = per[5] if r == 0 else per[r]
    return a

def contact_gram(Lam, S, N):
    k = len(S)
    M = np.zeros((k,k))
    for i,m in enumerate(S):
        for j,n in enumerate(S):
            p = m*n
            M[i,j] = Lam[p] if p <= N else 0.0
    return M

def inertia(M, tol=1e-9):
    w = np.linalg.eigvalsh(M)
    sc = max(1.0, np.abs(w).max())
    pos = int((w >  tol*sc).sum()); neg = int((w < -tol*sc).sum())
    return pos, neg, len(w)-pos-neg, w

NMAX = 400
for name, af in (("zeta", a_zeta), ("DH", a_dh)):
    a = af(NMAX)
    Lam = lambda_of(a, NMAX)
    print("="*66)
    print(name, " first Lambda coefficients n=1..14:")
    print("  ", np.round(Lam[1:15], 6))
    for Ncap in (60, 120, 200, 400):
        # index set: all integers 2..sqrt(Ncap) so that m*n <= Ncap is attainable
        S = list(range(2, int(math.isqrt(Ncap))+1))
        M = contact_gram(Lam, S, Ncap)
        pos, neg, zer, w = inertia(M)
        print(f"  N={Ncap:4d}  |S|={len(S):3d}   inertia (+,-,0) = ({pos},{neg},{zer})   lam_min={w[0]:+.6f}")

# Exact-formula audit for the first coefficients used in paper 42.
kappa = (sqrt(10-2*sqrt(5)) - 2)/(sqrt(5)-1)
Lam_DH = lambda_of(a_dh(NMAX), NMAX)
assert abs(Lam_DH[3] + kappa*log(3)) < 1e-12
assert abs(Lam_DH[4] + (2+kappa*kappa)*log(2)) < 1e-12
assert abs(Lam_DH[6] - (1+kappa*kappa)*log(6)) < 1e-12
assert abs(Lam_DH[5]) < 1e-12 and abs(Lam_DH[10]) < 1e-12

print()
print("### escala mayor + conteo de primos ###")
from sympy import primepi
for Ncap in (900, 1600, 2500, 4900):
    S = list(range(2, int(math.isqrt(Ncap))+1))
    for name, af in (("zeta", a_zeta), ("DH", a_dh)):
        Lam = lambda_of(af(Ncap), Ncap)
        M = contact_gram(Lam, S, Ncap)
        pos, neg, zer, w = inertia(M)
        tag = f"pi(sqrt N)={int(primepi(int(math.isqrt(Ncap))))}" if name=="zeta" else ""
        print(f"  N={Ncap:5d} |S|={len(S):3d} {name:5s} (+,-,0)=({pos:2d},{neg:2d},{zer:2d}) lam_min={w[0]:+12.4f}  {tag}")
