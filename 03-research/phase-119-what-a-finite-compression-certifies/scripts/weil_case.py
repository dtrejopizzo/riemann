import numpy as np, math
from math import log

def hankel(a, K):
    return np.array([[a[i+j] for j in range(1,K+1)] for i in range(1,K+1)], dtype=float)

def inert(M, tol=1e-9):
    w = np.linalg.eigvalsh(M); s = max(1.0, abs(w).max())
    return int((w>tol*s).sum()), int((w<-tol*s).sum()), w[0]

K = 6; NK = 2*K+2

print("Norm-pushforward Hankel for curves over F_q (not the place-indexed contact Gram).")
print("Lambda(q^m) = #C(F_{q^m}) * log q ;  P2_norm tests [Lambda(q^{i+j})]")
print("-"*74)

# P^1 / F_2 :  a_k = q^k + 1   (Frobenius eigenvalues q and 1, both positive real)
q = 2
a = [0.0]+[ (q**k + 1)*log(q) for k in range(1, NK) ]
p_,n_,lm = inert(hankel(a,K)); print(f"{'P^1 / F_2  (g=0)':34s} (+,-)=({p_},{n_})  lam_min={lm:+12.4f}")

# elliptic curves over F_q: a_k = q^k + 1 - (w^k + wbar^k), |w|=sqrt(q)
for q, t, lbl in ((2,0,'E/F_2, trace 0'), (2,1,'E/F_2, trace 1'), (2,-2,'E/F_2, trace -2'),
                  (3,2,'E/F_3, trace 2'), (5,3,'E/F_5, trace 3')):
    disc = complex(t*t - 4*q)
    w = (t + np.sqrt(disc))/2
    wb = (t - np.sqrt(disc))/2
    a = [0.0]+[ (q**k + 1 - (w**k + wb**k)).real*log(q) for k in range(1, NK) ]
    if min(a[1:]) < -1e-9:   # sanity: point counts must be >= 0
        lbl += "  [!]"
    p_,n_,lm = inert(hankel(a,K)); print(f"{lbl:34s} (+,-)=({p_},{n_})  lam_min={lm:+12.4f}")

# Formal genus-2 Weil spectrum over F_2.  The chosen angles satisfy the Weil
# absolute-value constraint but are not asserted to come from an actual curve.
q=2; ws=[np.sqrt(q)*np.exp(1j*th) for th in (0.9, 2.1)]
ws = ws + [np.conj(x) for x in ws]
a=[0.0]+[ (q**k+1-sum(x**k for x in ws)).real*log(q) for k in range(1,NK)]
p_,n_,lm = inert(hankel(a,K)); print(f"{'formal genus-2 Weil spectrum':34s} (+,-)=({p_},{n_})  lam_min={lm:+12.4f}")

print()
print("Cyclic cubic field of conductor 7 (K = Q(zeta_7)^+), full Gram [Lambda_K(mn)]:")
# Lambda_K(n) = 3*Lambda(n) if chi(n)=1 else 0, chi cubic mod 7 (3 is a primitive root mod 7)
def chi_is_one(n):
    if n % 7 == 0: return False
    # index of n base primitive root 3 mod 7 ; chi(n)=1 iff 3 | ind(n)
    g, ind, x = 3, 0, 1
    for e in range(6):
        if x == n % 7: ind = e; break
        x = (x*g) % 7
    return ind % 3 == 0
NMAX = 4900
Lam = np.zeros(NMAX+1)
sieve = np.zeros(NMAX+1, dtype=bool); sieve[2:]=True
for i in range(2,int(math.isqrt(NMAX))+1):
    if sieve[i]: sieve[i*i::i]=False
for p in np.nonzero(sieve)[0]:
    pk = int(p)
    while pk <= NMAX:
        Lam[pk] = 3*log(p) if chi_is_one(pk) else 0.0
        pk *= int(p)
# The conductor prime 7 is totally ramified and has residue degree one.
pk = 7
while pk <= NMAX:
    Lam[pk] = log(7)
    pk *= 7
assert Lam.min() >= 0, "P0 must hold"
for Ncap in (400, 1600, 4900):
    S = list(range(2, int(math.isqrt(Ncap))+1))
    M = np.array([[Lam[m*n] if m*n<=Ncap else 0.0 for n in S] for m in S])
    p_,n_,lm = inert(M)
    print(f"  N={Ncap:5d} |S|={len(S):3d}  P0(Lam>=0)=True  (+,-)=({p_},{n_})  lam_min={lm:+10.4f}")
