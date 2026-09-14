#!/usr/bin/env python3
"""R146 round 2 / D.47 -- the single-prime Frobenius tower {Frob_{p^k}}_{k>=1}.

Half-density Gram (Paper 44 Thm 8bis.1 + K1, restricted to m,n in {p^k}):
    G_{jk} = c_p * (log p) * p^{-|j-k|/2}   (j != k),        G_{jj} = delta_p ,
with c_p = prod_{s in S_f \ {p}} vol(1+s^N Z_s) > 0 the SAME constant for all (j,k)
(because P(p^j) = P(p^k) = {p}), and delta_p the SAME number for all k
(Thm 8bis.1b: the diagonal depends on n only through P(n); Cor 8bis.1b' likewise).
Normalized:  G = c_p (log p) [ T(rho) + (tau - 1) I ],  rho = p^{-1/2},  T_{jk} = rho^{|j-k|},
             tau := delta_p / (c_p log p).
Xi_a version: weights Lambda_a(p^k) = Lambda(p^k)(p^{ka}+p^{-ka})/2  ==>  off-diagonal
             ghat_a(k) = (rho_+^k + rho_-^k)/2 with rho_pm = p^{-(1/2 -+ a)}.
Thresholds (bi-infinite tower, Toeplitz symbol):
    PSD          <==>  tau >= tau_+(a) := ghat-symbol minimum condition = 2*sum_pm rho/(1+rho) /2
    NEG.SEMIDEF  <==>  tau <= tau_-(a) := -(...)/... (symbol maximum at theta=0)
Usage: python3 tower_gram.py [--fast]
"""
import sys, math
import numpy as np

FAST = "--fast" in sys.argv

def thresholds(p, a=0.0):
    rho_p = p**(-(0.5 - a)); rho_m = p**(-(0.5 + a))
    if rho_p >= 1.0: return (float('inf'), float('-inf'), rho_p, rho_m)
    # symbol of the off-diagonal part: sum_{k!=0} ghat(|k|) e^{ik theta},
    # ghat(k) = (rho_p^k + rho_m^k)/2 ; extremes at theta = pi and 0.
    def P(r, th): return 2*r*(math.cos(th)-r)/(1-2*r*math.cos(th)+r*r)
    lo = 0.5*(P(rho_p, math.pi) + P(rho_m, math.pi))   # minimum of off-diag symbol
    hi = 0.5*(P(rho_p, 0.0)     + P(rho_m, 0.0))       # maximum
    return (-lo, -hi, rho_p, rho_m)                    # PSD iff tau >= -lo ; NSD iff tau <= -hi

print("=== [1] tau thresholds for the xi tower (a = 0):  PSD iff tau >= tau_+ ;  NSD iff tau <= tau_- ===")
print(f"{'p':>6} {'rho=p^-1/2':>12} {'tau_+ = 2/(sqrt p+1)':>22} {'tau_- = -2/(sqrt p-1)':>22}")
for p in [2,3,5,7,11,13,101]:
    tp, tm, _, _ = thresholds(p, 0.0)
    print(f"{p:>6} {p**-0.5:12.6f} {tp:22.6f} {tm:22.6f}   (closed form: {2/(math.sqrt(p)+1):.6f}, {-2/(math.sqrt(p)-1):.6f})")

print()
print("=== [2] finite sections T_K(rho): lambda_min <= 1 always, so tau < 0 can never be PSD ===")
print(f"{'p':>4} {'K':>4} {'lambda_min':>12} {'lambda_max':>12} {'1-lambda_min (=tau_+ at K)':>28}")
for p in [2,3,7]:
    rho = p**-0.5
    for K in ([4,8,16] if FAST else [4,8,16,64,256]):
        T = np.array([[rho**abs(i-j) for j in range(K)] for i in range(K)])
        ev = np.linalg.eigvalsh(T)
        print(f"{p:>4} {K:>4} {ev[0]:12.6f} {ev[-1]:12.6f} {1-ev[0]:28.6f}")

print()
print("=== [3] Xi_a: does the threshold move?  (A3 test on the tower) ===")
print(f"{'p':>4} {'a':>7} {'rho_+':>10} {'rho_-':>10} {'tau_+(a)':>12} {'tau_+(a)-tau_+(0)':>20}")
for p in [2,3,7]:
    t0, _, _, _ = thresholds(p, 0.0)
    for a in [0.0, 0.05, 0.1, 0.25, 0.4, 0.49]:
        tp, tm, rp, rm = thresholds(p, a)
        print(f"{p:>4} {a:7.2f} {rp:10.6f} {rm:10.6f} {tp:12.6f} {tp-t0:20.3e}")
    print(f"{p:>4}  a=0.50 : rho_+ = 1  -> the kernel is not summable, the symbol has a pole: the form is UNBOUNDED")

print()
print("=== [4] the model tower for comparison: kappa(k) = q^{-k/2} N_k, N_k = deg(1-pi^k) ===")
print("      (E/F_2 : y^2+xy = x^3+1, q=2, a=-1, alpha = (a +- sqrt(a^2-4q))/2)")
q, a_tr = 2, -1
al = complex(a_tr, math.sqrt(4*q - a_tr*a_tr))/2
print(f"{'k':>4} {'N_k':>12} {'kappa(k)=q^-k/2 N_k':>22} {'arithmetic (log p) p^-k/2':>26}")
for k in range(0, 9):
    S = 2*(al**k).real
    N = q**k + 1 - S if k > 0 else 2 - 2*1
    kap = (q**(-k/2))*N if k > 0 else 0.0
    print(f"{k:>4} {N:12.4f} {kap:22.6f} {math.log(2)*2**(-k/2):26.6f}")
print("   model kappa(k) ~ q^{k/2} GROWS;  arithmetic entry ~ (log p) p^{-k/2} DECAYS.")

print()
print("=== [5] M6: the rank-2 order is over-determined at a single prime ===")
print(f"{'l':>5} {'a_l = l+1-Lambda(l)':>22} {'N_2 predicted = l^2+1-(a^2-2l)':>32} {'dictionary N_2 = Lambda(l^2)':>30}")
for l in [2,3,5,7]:
    lam = math.log(l)
    A = l + 1 - lam
    N2 = l*l + 1 - (A*A - 2*l)
    print(f"{l:>5} {A:22.6f} {N2:32.6f} {lam:30.6f}")

print()
print("=== [6] M7: the Hasse test is an artifact of d_n = n ===")
print(f"{'l':>5} {'d=n: a_l':>12} {'a^2<=4l?':>10} {'d=log n (d_1=1): a_l':>22} {'a^2<=4l?':>10}")
for l in [2,3,5,7,11,101]:
    lam = math.log(l)
    A1 = l + 1 - lam
    A2 = 1 + math.log(l) - lam     # = 1 for l prime
    print(f"{l:>5} {A1:12.5f} {str(A1*A1<=4*l):>10} {A2:22.5f} {str(A2*A2<=4*l):>10}")

print()
print("=== [7] M13 / M8 robustness: the -10 witness under both degree normalizations ===")
for dn, nm in [((lambda n: n), "d_n = n"), ((lambda n: math.log(n)), "d_n = log n")]:
    A = 5 - 4
    B = 5*dn(6) - 4*dn(10)
    print(f"   {nm:>14}:  Q_0(5 Frob_6 - 4 Frob_10) = Phi(0)Phi(1) = {A*B:.6f}   (L(6,10) = 0, convention-free)")
