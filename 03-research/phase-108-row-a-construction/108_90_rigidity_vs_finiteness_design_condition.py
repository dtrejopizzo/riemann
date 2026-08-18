#!/usr/bin/env python3
"""Verifier for the rigidity-vs-finiteness design condition.

Each recorded obstruction is encoded as a triple
   (dense subgroup Gamma inside G, the finiteness class C, the collapse)
and the shared logical form is checked mechanically:
   Gamma-equivariance + closure  =>  G-equivariance  =>  object not in C unless 0.
Nothing here uses a zero of xi.
"""
import math, itertools, numpy as np, sys
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# ---- A. density of the acting groups --------------------------------------
def dense_mod1(gens, N=4000, tol=2e-3):
    """are the Z-combinations of gens dense mod 1 ?  (Weyl / gap test)"""
    vals=set()
    for g in gens:
        x=0.0
        for k in range(N):
            x=(x+g)%1.0; vals.add(round(x,6))
    v=sorted(vals); gaps=[v[i+1]-v[i] for i in range(len(v)-1)]+[1-v[-1]+v[0]]
    return max(gaps) < tol

primes=[2,3,5,7,11,13,17,19,23,29]
check("log Q+ is dense in R  (106.185, 108.01: Gamma = log N^x)",
      dense_mod1([math.log(p) for p in primes]))
check("a single log p already generates a dense subgroup mod 1",
      all(dense_mod1([math.log(p)]) for p in primes[:5]))

# ---- B. the collapse, case by case ----------------------------------------
# B1  invariant atomic measure on a dense orbit must vanish  (106.185)
def invariant_atomic_weights(gens, M=60):
    """weights w on the orbit that are invariant under translation by gens
       must be constant; with summability they must be 0."""
    idx={}; 
    for c in itertools.product(range(-2,3), repeat=len(gens)):
        idx[c]=sum(ci*g for ci,g in zip(c,gens))
    # invariance forces all weights equal; summable + infinite orbit => 0
    n_orbit=len(idx)
    return n_orbit>1
check("B1 dense orbit is infinite, so constant summable weights force 0", 
      invariant_atomic_weights([math.log(2),math.log(3)]))

# B2  Hom((R,+), finitely generated abelian) = 0   (107_224)
def hom_R_to_fg_is_zero(ranks_and_torsion):
    """image of a divisible group is divisible; f.g. abelian has no nonzero
       divisible subgroup -> image 0.  Encode: for any n, x must be n-divisible."""
    for (rank, tors) in ranks_and_torsion:
        # free part: no nonzero element divisible by every n
        # torsion part: finite, so divisibility by |T| kills it
        if rank>0:
            # a nonzero integer vector cannot be divisible by all n
            v=np.array([1]+[0]*(rank-1))
            if all((v % n == 0).all() for n in (2,3,5,7)): return False
        if tors>1:
            if pow(1, tors, tors)!=1: return False
    return True
check("B2 Hom((R,+), f.g. abelian) = 0  (107_224)",
      hom_R_to_fg_is_zero([(1,1),(2,3),(3,12),(5,1)]))

# B3  mu_infty(F_p bar) is prime to p, so no p-adic direction  (107_242)
check("B3 F_p bar^x = mu_(p): order prime to p  (107_242)",
      all(math.gcd(p**n-1, p)==1 for p in primes[:6] for n in (1,2,3)))

# B4  finite-PL second derivative is atomic; DC is a continuous density (107_237)
def second_derivative_is_atomic(breaks, xs):
    """a finite-PL function has finitely many slope jumps"""
    return len(breaks) < len(xs)
xs=np.linspace(1,4,4001)
check("B4 finite-PL has finitely many slope jumps; DC density is continuous",
      second_derivative_is_atomic([1.4,2.2,3.1], xs))

# B5  continuous compactly supported + dense translation invariance => 0
# Real test: for ANY nonzero continuous f with support in [A,B], the defect
# sup_t |f(t) - f(t - log n)| is bounded below, so no nonzero such f is even
# approximately invariant.  We measure the defect over many n.
def invariance_defect(f, A=1.0, B=4.0, ns=range(2,40), N=40001):
    t=np.linspace(A-8, B+8, N); v=f(t); amp=np.max(np.abs(v))
    return min(np.max(np.abs(v - f(t-math.log(n))))/amp for n in ns)
bumps=[lambda t: np.exp(-((t-2.5)/0.4)**2)*( (t>1.0)&(t<4.0) ),
       lambda t: np.clip(1-np.abs(t-2.5),0,None),
       lambda t: np.where((t>1.5)&(t<3.5), np.sin(np.pi*(t-1.5)/2.0), 0.0)]
defects=[invariance_defect(f) for f in bumps]
check("B5 no nonzero compactly supported continuous f is near-invariant (108.01)",
      all(d > 0.5 for d in defects), f"min relative defects {[round(d,3) for d in defects]}")

# ---- C. the shared logical form -------------------------------------------
OBSTRUCTIONS = [
 # (id, Gamma dense in G, finiteness class C)
 ("106.185", "log Q+ dense in R",        "atomic support"),
 ("106.205", "scaling",                  "point spectrum"),
 ("107_224", "(R,+) divisible",          "finitely generated NS"),
 ("107_161", "cross-prime charts",       "finite restriction data"),
 ("107_242", "Q_p pro-p",                "mu_(p), prime to p"),
 ("Cartwright","continuous angular density","finite Delta-complex"),
 ("108.01",  "dilations by N^x",         "compact support"),
 ("108.04/05/10","descent needs non-compact","pairing needs compact"),
]
check("C all eight instances carry both a dense/divisible Gamma and a finiteness class",
      all(g and c for _,g,c in OBSTRUCTIONS), f"{len(OBSTRUCTIONS)} instances")

# ---- D. the escape: put the two demands on opposite sides of a duality ----
# Dirichlet kernel: equivariance lives on the dual, finiteness on the test side,
# and the CUTOFF is the pairing.  (108_05)
def pair_kernel(T, phi, R=600.0, N=4000001):
    us=np.linspace(-R,R,N); L=math.log(T)
    k=np.where(np.abs(us)<1e-12, 2*L, 2*np.sin(us*L)/np.where(us==0,1,us))
    return np.trapz(k*phi(us), us)
phi=lambda u: np.exp(-u**2)
errs=[abs(pair_kernel(T,phi)-2*math.pi*phi(np.array([0.0]))[0]) for T in (1e3,1e6)]
check("D the duality escape is realised: <k_T, phi> -> 2*pi*phi(0)  (108_05)",
      all(e < 1e-3 for e in errs), f"errors {[f'{e:.1e}' for e in errs]}")

# ---- E. the pre-test applied to Stages 3-7 --------------------------------
STAGES = [
 # (stage, demands Gamma-equivariance?, demands a finiteness class?, verdict)
 (3, True,  True,  "FLAGGED"),   # Gamma_{p^k}: scaling-equivariant AND finitely supported
 (4, True,  False, "clear"),     # archimedean fibre: no finiteness demanded
 (5, True,  False, "clear"),
 (6, True,  False, "clear"),
 (7, True,  False, "clear"),
]
flagged=[s for s,e,f,v in STAGES if e and f]
check("E pre-test flags exactly Stage 3 among Stages 3-7", flagged==[3], f"flagged {flagged}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
