#!/usr/bin/env python3
"""R147 D.51 -- the Epstein falsifier, run as a CONE-MEMBERSHIP test.

Frame cone:  E_cone = { E in D^W : E >= 0 pointwise },  deg E = int E(t) 2cosh(t/2) dt.
Canonical class of an admissible Z:  Phi_{K_Z} = Xi_Z.

For K = Q(sqrt(-D)) imaginary quadratic, every class-group character is
UNRAMIFIED, so all h Hecke L-functions share the SAME completion factor
(sqrt(D)/2pi)^s Gamma(s).  Hence, from phase 139 (D.19.1),
     Lambda_{Q_0} = (1/h) sum_chi Lambda(s,chi)   and   K_{Q_0} = (1/h) sum_chi K_chi ,
a combination with ALL coefficients 1/h > 0.  Question (blueprint D.51):
is K_{Q_0} in the effective cone?

Formulas (phase 139 Theorem D.19.2, D.19.3):
  K_Q(t) = (1/4) e^{t/2} sum'_{v in Z^2} (y^2 - 2y) e^{-y},  y = c e^t Q(v), c = 2pi/sqrt(D)
  2 Lambda_Q(s) = 1/(s-1) - 1/s + int_1^inf A(u)(u^{s-1}+u^{-s}) du,  A = Theta - 1
  Xi_Q(s) = (1/2) s(s-1) Lambda_Q(s)
Riemann control (same derivation with Theta_R(u) = sum_{n in Z} e^{-pi n^2 u}):
  K(t) = e^{t/2} sum_{n>=1} (4y^2 - 6y) e^{-y},  y = pi n^2 e^{2t},  deg K = 1.

NO positivity of any trace form is asserted anywhere; these are membership tests
for a pointwise-nonnegativity cone and evaluations of Xi on the real axis.
"""
import sys, math

FAST = "--fast" in sys.argv
YMAX = 70.0 if FAST else 90.0
STEP = 0.05 if FAST else 0.02
TMAX = 4.5
NQ   = 400 if FAST else 1600

# (D, h, principal form, a non-principal form or None)
CASES = [(3,1,(1,1,1),None),(4,1,(1,0,1),None),(7,1,(1,1,2),None),(8,1,(1,0,2),None),
         (11,1,(1,1,3),None),(19,1,(1,1,5),None),(43,1,(1,1,11),None),(163,1,(1,1,41),None),
         (15,2,(1,1,4),(2,1,2)),(23,3,(1,1,6),(2,1,3)),(47,5,(1,1,12),(2,1,6))]

def lam_min(abc):
    a,b,c = abc; return 0.5*((a+c) - math.sqrt((a-c)**2 + b*b))

def K_Q(t, abc, cc):
    """Adaptive radius: the box must contain EVERY v with y_v <= YMAX.  A fixed
    truncation destroys the (y^2-2y) cancellation and produces a spurious sign."""
    a,b,c = abc; u = cc*math.exp(t)
    R = int(math.ceil(math.sqrt(YMAX/(u*lam_min(abc))))) + 2
    s = 0.0
    for x in range(-R, R+1):
        for yv in range(-R, R+1):
            if x == 0 and yv == 0: continue
            y = u*(a*x*x + b*x*yv + c*yv*yv)
            if y <= YMAX: s += (y*y - 2.0*y)*math.exp(-y)
    return 0.25*math.exp(0.5*t)*s

def K_riemann(t):
    u = math.pi*math.exp(2*t); N = int(math.ceil(math.sqrt(YMAX/u))) + 2; s = 0.0
    for n in range(1, N+1):
        y = u*n*n
        if y > YMAX: break
        s += (4*y*y - 6*y)*math.exp(-y)
    return math.exp(0.5*t)*s

def Theta_m1(u, abc, cc):
    a,b,c = abc
    R = int(math.ceil(math.sqrt(YMAX/(cc*u*lam_min(abc))))) + 2; s = 0.0
    for x in range(-R, R+1):
        for yv in range(-R, R+1):
            if x == 0 and yv == 0: continue
            z = cc*u*(a*x*x + b*x*yv + c*yv*yv)
            if z <= YMAX: s += math.exp(-z)
    return s

def Lambda_Q(s, abc, cc, U=8.0, n=None):
    n = n or NQ; h = (U-1.0)/n; tot = 0.0
    for k in range(n+1):
        u = 1.0 + k*h; w = (0.5 if k in (0,n) else 1.0)*h
        tot += w*Theta_m1(u, abc, cc)*(u**(s-1.0) + u**(-s))
    return 0.5*(1.0/(s-1.0) - 1.0/s + tot)

def Xi_Q(s, abc, cc): return 0.5*s*(s-1.0)*Lambda_Q(s, abc, cc)

ts = [k*STEP for k in range(-int(TMAX/STEP), int(TMAX/STEP)+1)]

print("=== [A] Riemann control: is Paper 46's K effective?")
vs = [K_riemann(t) for t in ts]
degK = sum(v*2*math.cosh(t/2)*STEP for t,v in zip(ts,vs))
ev = max(abs(vs[k]-vs[len(vs)-1-k]) for k in range(len(vs)))
print(f"    min K = {min(vs):.6e}   max K = {max(vs):.6f}   deg K = {degK:.9f} (must be 1)")
print(f"    evenness residual = {ev:.2e}   ->  K >= 0 : K IS IN THE EFFECTIVE CONE"
      if min(vs) > -1e-12 else "    K < 0 somewhere")

print()
print("=== [B] K_Q membership, Epstein (Q_0 = principal form)")
print(f"{'D':>4s} {'h':>2s} {'form':>10s} {'min K_Q':>14s} {'argmin':>7s} {'max K_Q':>10s}  verdict")
memb = {}
for D,h,P,NP in CASES:
    cc = 2*math.pi/math.sqrt(D)
    for lab,abc in (("principal",P),("non-princ",NP)):
        if abc is None: continue
        vs = [K_Q(t,abc,cc) for t in ts]
        mn, mx = min(vs), max(vs); am = ts[vs.index(mn)]
        ok = mn > -1e-12*max(1.0,mx)
        if lab == "principal": memb[D] = ok
        print(f"{D:4d} {h:2d} {str(abc):>10s} {mn: 14.6e} {am:+7.2f} {mx:10.6f}  "
              + ("IN the cone" if ok else "NOT in the cone  (|min|/max = %.3f)" % (abs(mn)/mx)))

print()
print("=== [C] Xi_Q on the real axis  (E >= 0 forces Phi_E(s) > 0 for every real s)")
print(f"{'D':>4s} {'Xi(0)':>9s} {'Xi(1/4)':>10s} {'Xi(1/2)':>10s} {'Xi(3/4)':>10s} {'Xi(1)':>9s}   "
      "Lemma D.31.4 check: |Xi(1/2)| <= (1/2)deg = 1/4")
for D,h,P,NP in CASES:
    cc = 2*math.pi/math.sqrt(D)
    row = [Xi_Q(s,P,cc) for s in (1e-9,0.25,0.5,0.75,1-1e-9)]
    print(f"{D:4d} " + " ".join(f"{v:10.7f}" for v in row) +
          f"    margin 1/4 - Xi(1/2) = {0.25-row[2]:.7f}")

print()
print("=== [D] quadrature margins")
for D,h,P,NP in CASES[:4] + CASES[-3:]:
    cc = 2*math.pi/math.sqrt(D)
    a1 = Lambda_Q(0.5,P,cc,n=NQ); a2 = Lambda_Q(0.5,P,cc,n=2*NQ)
    print(f"    D={D:4d}  Lambda_Q(1/2) = {a1:.9f}   |n vs 2n| = {abs(a1-a2):.3e}")

print()
print("=== [E] SUMMARY: membership of the PRINCIPAL K_Q in the cone, vs h")
for D,h,P,NP in CASES:
    print(f"    D={D:4d}  h={h}  K_Q0 in cone: {str(memb[D]):5s}"
          + ("   <-- h>1, so Z_Q0 has infinitely many zeros in Re s>1 (Davenport-Heilbronn)" if h>1 and memb[D] else ""))
print("    => membership is UNCORRELATED with h and with zero location.")
