"""R153 Q2/Q3 -- is the certified endpoint prime-blind?  And the near-null direction.

Run: python3 r153_q2_mechanism.py
All numbers DIAGNOSTIC-NUMERIC (float64 Galerkin, piecewise-constant basis).
"""
import math, sys, os
import numpy as np, scipy.linalg as sla
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    "../../phase-118-the-exact-threshold-inequality/scripts")))
import rowd_assembly as RA
from r153_q1_xi_a import moments, constrained_min, cell_avg_exp

def build(T, refine, extra=()):
    D = RA.assemble(T, refine=refine, extra_points=extra)
    return D

def report(T, refine):
    D = build(T, refine)
    c,d,Gram = D['c'],D['d'],D['Gram']
    G = D['G']; A = D['A']
    Arch = G - RA.M0*Gram
    lam = RA.von_mangoldt(max(D['N'],2))
    prim = [n for n in RA.prime_powers_upto(max(D['N'],2)) if n < math.exp(2*T)-1e-13]
    C2 = moments(c,d,[-0.5,0.5])
    w,V = constrained_min(A,Gram,C2)
    print(f"T={T:.6f} refine={refine} cells={len(c)} contacts={prim}")
    print(f"  lambda_min(A_T|P_T)          = {w[0]: .6e}")
    wa,_ = constrained_min(Arch,Gram,C2)
    absnorm = 2*sum(lam[n]/math.sqrt(n) for n in prim)
    print(f"  lambda_min(G-m0|P_T)         = {wa[0]: .6e}   2*sum w_n = {absnorm:.6f}")
    print(f"  Q2(i)  lambda_min(A^abs|P_T) = {wa[0]-absnorm: .6e}  -> "
          f"{'POSITIVE (Outcome A)' if wa[0]-absnorm>0 else 'NEGATIVE (no archimedean domination in the crude sense)'}")
    # Q2(ii) sign flips
    def with_weights(wts):
        M = Arch.copy()
        for n,wn in wts.items():
            S = RA.shift_form(c,d,math.log(n)); M -= wn*(S+S.T)
        return M
    base = {n: lam[n]/math.sqrt(n) for n in prim}
    for name,wts in [("Lambda(3) -> -Lambda(3)", {**base, **({3:-base[3]} if 3 in base else {})}),
                     ("drop n=3",               {n:v for n,v in base.items() if n!=3}),
                     ("drop n=2",               {n:v for n,v in base.items() if n!=2}),
                     ("Lambda(2) -> -Lambda(2)", {**base, **({2:-base[2]} if 2 in base else {})})]:
        ww,_ = constrained_min(with_weights(wts),Gram,C2)
        print(f"  Q2(ii) {name:26s} lambda_min = {ww[0]: .6e}")
    # generic shift b replacing log 3, same weight
    if 3 in base:
        for b in (0.8,0.9,1.0,1.0986,1.2,1.3):
            M = Arch.copy()
            S = RA.shift_form(c,d,math.log(2)); M -= base[2]*(S+S.T)
            S = RA.shift_form(c,d,b);           M -= base[3]*(S+S.T)
            ww,_ = constrained_min(M,Gram,C2)
            print(f"  Q2(ii) generic shift b={b:.4f} (weight w_3)      lambda_min = {ww[0]: .6e}")
    # Q2(iii) decomposition of the minimiser v1
    v = V[:,0]; v = v/math.sqrt(v@Gram@v)
    print(f"  Q2(iii) <(G-m0)v1,v1> = {v@Arch@v: .6e}")
    for n in prim:
        S = RA.shift_form(c,d,math.log(n)); sym = S+S.T
        print(f"          <w_{n}(S_+ + S_-)v1,v1> = {base[n]*(v@sym@v): .6e}  (w_{n}={base[n]:.6f})")
    print(f"          sum check = {v@A@v: .6e}")
    return D,v,Gram,Arch

if __name__=="__main__":
    for T in (math.log(2), 0.5*math.log(3)):
        for ref in (64,128,256):
            report(T,ref)
        print()
