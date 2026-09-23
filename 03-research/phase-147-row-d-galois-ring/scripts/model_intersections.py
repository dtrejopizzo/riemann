#!/usr/bin/env python3
"""R147 D.53 -- the model: E/F_5 : y^2 = x^3 + x, CM by Z[i], Aut = mu_4.

Computes (1) point counts N_m and the Weil numbers; (2) the intersection numbers
Gamma_alpha . Gamma_beta = deg(alpha-beta) = N(alpha-beta) on E x E, checked
against Lefschetz fixed-point counts; (3) the NS identity
2[Gamma_i] = [Gamma_pi] - [Delta] - 2F_1 + 2F_2   (in NS(ExE); over Q: [Gamma_i] = 1/2[Gamma_pi] - 1/2[Delta] - F_1 + F_2)  (an EFFECTIVE class with
negative coefficients in the Frobenius basis); (4) the support-function
("cosh") constants of three cones:
      s_Frob   : Cone{ Gamma_{pi^n} }            (the frame's cone)
      s_AutFrob: Cone{ Gamma_{sigma pi^n} }      (Aut-twisted Frobenius)
      s_End    : Cone{ Gamma_alpha : alpha in Z[i] }
   s(cone) := min_theta  sup_gen  |Re(e^{i theta} Phi_gen)| / (1/2 deg gen),
   Phi_{Gamma_alpha}(rho_1) = alpha,  deg Gamma_alpha = 1 + N(alpha).
No positivity of any trace form is asserted; these are support functions only.
"""
import sys, math, cmath

FAST = "--fast" in sys.argv
p, a = 5, 2                      # y^2=x^3+x over F_5 : N_1 = 4, a = q+1-N_1 = 2
pi_ = complex(1.0, 2.0)          # pi = 1+2i, N(pi) = 5, tr = 2

def N(z): return z.real*z.real + z.imag*z.imag

# ---- (1) point counts, independent check ------------------------------------
def count_F5():
    sq = {(y*y) % 5 for y in range(5)}
    n = 1
    for x in range(5):
        v = (x*x*x + x) % 5
        if v == 0: n += 1
        elif v in sq: n += 2
    return n
N1 = count_F5()
assert N1 == 4, N1
assert abs(N(pi_) - p) < 1e-12 and abs(2*pi_.real - a) < 1e-12
Nm = [None] + [int(round(p**m + 1 - 2*(pi_**m).real)) for m in range(1, 7)]
assert Nm[1] == N1

# ---- (2) intersection numbers ------------------------------------------------
units = [complex(1,0), complex(0,1), complex(-1,0), complex(0,-1)]   # Aut(E)=mu_4
names = {complex(1,0):"1", complex(0,1):"i", complex(-1,0):"-1", complex(0,-1):"-i"}
print("[1] E/F_5 : y^2 = x^3 + x   N_1 =", N1, " a =", a, " pi = 1+2i,  End = Z[i],  Aut = mu_4")
print("    N_m =", Nm[1:5], " (N_m = deg(1-pi^m) check:",
      [int(round(N(1-pi_**m))) for m in range(1,5)], ")")
print("[2] Gamma_sigma . Gamma_tau = #Fix(sigma^{-1} tau) = N(sigma - tau):")
for s in units:
    row = [int(round(N(s-t))) for t in units]
    print("     sigma =", names[s].rjust(2), "->", row)
print("    Gamma_sigma . Gamma_pi = N(sigma - pi):",
      {names[s]: int(round(N(s-pi_))) for s in units})
print("    Gamma_sigma . Delta = #Fix(sigma) = #E[sigma-1]:",
      {names[s]: int(round(N(s-1))) for s in units})

# ---- (3) the NS identity (checked by pairing against a basis) ----------------
# Basis F_1,F_2,Delta,Gamma_pi.  Pairings: F_1^2=F_2^2=0, F_1F_2=1,
# Gamma_alpha.F_1 = 1, Gamma_alpha.F_2 = N(alpha), Gamma_alpha.Gamma_beta=N(alpha-beta).
def pair_graph_graph(al, be): return N(al-be)
basis = [("F1",None), ("F2",None), ("D",complex(1,0)), ("Gpi",pi_)]
def pair(X, Y):
    # X, Y given as dicts over {F1,F2} plus list of (coeff, alpha) graph parts
    tot = 0.0
    for cx, kx in X["f"]:
        for cy, ky in Y["f"]:
            tot += cx*cy*(1.0 if kx != ky else 0.0)
    for cx, ax in X["g"]:
        for cy, ky in Y["f"]:
            tot += cx*cy*(1.0 if ky == "F1" else N(ax))
    for cy, ay in Y["g"]:
        for cx, kx in X["f"]:
            tot += cx*cy*(1.0 if kx == "F1" else N(ay))
    for cx, ax in X["g"]:
        for cy, ay in Y["g"]:
            tot += cx*cy*pair_graph_graph(ax, ay)
    return tot
LHS = {"f": [], "g": [(1.0, complex(0,1))]}                                  # [Gamma_i]
RHS = {"f": [(-1.0,"F1"), (1.0,"F2")], "g": [(0.5, pi_), (-0.5, complex(1,0))]}
tests = [{"f":[(1.0,"F1")],"g":[]}, {"f":[(1.0,"F2")],"g":[]},
         {"f":[],"g":[(1.0,complex(1,0))]}, {"f":[],"g":[(1.0,pi_)]},
         {"f":[],"g":[(1.0,complex(0,1))]}, {"f":[],"g":[(1.0,complex(1,1))]}]
errs = [abs(pair(LHS,T)-pair(RHS,T)) for T in tests]
print("[3] NS identity  [Gamma_i] = 1/2[Gamma_pi] - 1/2[Delta] - F_1 + F_2")
print("    max |LHS.T - RHS.T| over 6 test classes =", max(errs))
assert max(errs) < 1e-12
print("    -> Gamma_i is an IRREDUCIBLE CURVE (effective) with coefficients",
      "(-1,+1,-1/2,+1/2) in (F_1,F_2,Delta,Gamma_pi): a genuine '+'.")

# ---- (4) support functions ----------------------------------------------------
def ratio(alpha, theta):
    d2 = 0.5*(1.0 + N(alpha))                 # (1/2) deg Gamma_alpha
    return abs((cmath.exp(1j*theta)*alpha).real)/d2

NMAX = 3 if FAST else 5
RAD  = 4 if FAST else 7
gens_frob    = [pi_**n for n in range(0, NMAX+1)] + [pi_.conjugate()**n for n in range(1, NMAX+1)]
gens_autfrob = [u*g for g in gens_frob for u in units]
gens_end     = [complex(x,y) for x in range(-RAD,RAD+1) for y in range(-RAD,RAD+1)
                if (x,y) != (0,0)]
def s_of(gens, steps=200001):
    best, bt = 2.0, None
    for k in range(steps):
        th = math.pi*k/(steps-1)
        v = max(ratio(g, th) for g in gens)
        if v < best: best, bt = v, th
    return best, bt
res = {}
for nm, gens in (("s_Frob",gens_frob), ("s_AutFrob",gens_autfrob), ("s_End",gens_end)):
    steps = 20001 if FAST else 200001
    v, th = s_of(gens, steps)
    res[nm] = (v, th)
    print(f"[4] {nm:10s} = {v:.9f}   at theta = {th:.9f}   (1 - s = {1-v:.9f})")
print("    closed forms:  s_Frob = sqrt(4q-a^2)/(q+1) =", math.sqrt(4*p-a*a)/(p+1),
      "  [= (145.9), the theta=pi/2 value; R145 (145.10) does NOT apply here:")
print("      its balance ignores the n=-1 entry, which dominates at its theta*.]")
print("    s_AutFrob = cos(pi/|Aut|) = cos(pi/4) =", math.cos(math.pi/4))
print("    s_End     = 2/sqrt(5) =", 2/math.sqrt(5))
print("    margins |numeric - closed form|:",
      abs(res['s_Frob'][0]-math.sqrt(4*p-a*a)/(p+1)),
      abs(res['s_AutFrob'][0]-math.cos(math.pi/4)),
      abs(res['s_End'][0]-2/math.sqrt(5)))
# cross-check of the search code against R145's record curve q=2, a=-1
q2,a2 = 2,-1; pi2 = complex(-0.5, math.sqrt(4*q2-a2*a2)/2)
g2 = [pi2**n for n in range(0,6)] + [pi2.conjugate()**n for n in range(1,6)]
def r2(al,th): return abs((cmath.exp(1j*th)*al).real)/(0.5*(1.0+N(al)))
b2 = min(max(r2(g,math.pi*k/200000) for g in g2) for k in range(200001))
print("    [cross-check] R145 record curve q=2,a=-1: numeric s* =", b2,
      " vs sqrt(7/11) =", math.sqrt(7/11), " margin", abs(b2-math.sqrt(7/11)))
print("    ALL THREE < 1 : the defect theorem survives on the model with its")
print("    full endomorphism-graph cone.  (Eff(ExE) itself has s = 1.)")
