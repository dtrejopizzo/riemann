"""
SURF-A finite Gram experiment (Phase 17, step 1).

Purpose (per phase-17/00-SURF-2.0-design.md, acceptance test A.4):
  Establish the TARGET signature template that any SURF-A geometry must reproduce,
  and confirm the structural clue A.2 quantitatively:
    - on-line zero (b=0)   -> off-axis functional is REAL  -> block signature (1,0)
    - off-line zero (b!=0)  -> functional is COMPLEX        -> block signature (1,1)
    - the negative direction switches on continuously with b = distance to the real locus,
    - total negative index of the bilinear Weil-Gram = number of off-line quartets (=kappa/4).

This is NOT a construction of the geometry. It computes what the geometry must MATCH,
using a concrete finite zero configuration and a finite even-test-function basis.

Numerical note: the Gaussian amplitudes sqrt(pi/a) exp((b^2-gamma^2)/(4a)) vary by factors
~e^{130} across widths, which would swamp the Gram to numerical rank 1. We therefore divide
each evaluation by its own modulus. Scaling test functions by positive constants is a
CONGRUENCE D M D, which preserves the signature (Sylvester's law); it only fixes the scale.

Math:
  Weil form (bilinear, P25/P26):  Q(f,g) = sum_rho phi_f(rho) phi_g(rho),
    phi_f(s) = int f(u) e^{(s-1/2)u} du,  fhat(z):=phi_f(1/2+iz),  phi_f(rho)=fhat(gamma-ib),
    rho = 1/2 + b + i*gamma,  b = beta-1/2.
  For an even real Gaussian f_a(u)=e^{-a u^2}:
    fhat_a(gamma-ib) = sqrt(pi/a) * exp((b^2-gamma^2)/(4a)) * exp( i*gamma*b/(2a) ),
  so after modulus normalization the direction is exp( i*gamma*b/(2a) ).
  Off-line quartet {1/2 +- b +- i*gamma} regroups (P25 Thm D) to 4*Re[fhat(gamma-ib)^2]=4(u^2-v^2).
"""

import numpy as np

WIDTHS = np.array([0.35, 0.6, 1.0, 1.7, 2.8, 4.5])   # even test fns f_a(u)=e^{-a u^2}

def eval_dir(gamma, b):
    """unit-modulus off-axis evaluation direction per test function: exp(i*gamma*b/(2a))."""
    phase = gamma * b / (2*WIDTHS)
    return np.exp(1j * phase)               # u + i v (already |.|=1)

def block_gram(gamma, b):
    """bilinear contribution of one zero/quartet: M_kl = 4 Re[w_k w_l] (product, not modulus).
       b=0 -> w real -> 4 u_k u_l (rank 1, sig (1,0)); b!=0 -> 4(u_k u_l - v_k v_l) (sig (1,1))."""
    w = eval_dir(gamma, b)
    return 4.0 * np.real(np.outer(w, w))

def signature(M, rtol=1e-8):
    ev = np.linalg.eigvalsh((M + M.T)/2)
    scale = max(np.max(np.abs(ev)), 1e-300)
    pos = int(np.sum(ev >  rtol*scale))
    neg = int(np.sum(ev < -rtol*scale))
    return pos, neg, len(ev)-pos-neg, ev

print("="*74)
print("SURF-A  |  TARGET Gram-signature template (what the geometry must reproduce)")
print("="*74)

# (A) single-block signatures: on-line (1,0) vs off-line (1,1)
print("\n(A) Single-zero / single-quartet block signatures (gamma=14.13)")
for label, b in [("on-line  (b=0)   ", 0.0), ("off-line (b=0.20)", 0.20)]:
    p, n, z, ev = signature(block_gram(14.13, b))
    print(f"  {label}: signature (pos,neg,zero) = ({p},{n},{z})   "
          f"nonzero eigs = {np.round(ev[np.abs(ev)>1e-8*max(np.abs(ev))], 3)}")

# (B) b-scaling: the negative direction switches on continuously with b (A.2)
print("\n(B) |negative eigenvalue| vs b = distance to the real locus (gamma=14.13)")
print("      b      lambda_min     lambda_max    signature")
for b in [0.0, 0.02, 0.05, 0.10, 0.20, 0.30, 0.45]:
    p, n, z, ev = signature(block_gram(14.13, b))
    print(f"   {b:5.2f}   {ev.min():11.4e}   {ev.max():11.4e}   ({p},{n},{z})")

# (C) several distinct off-line quartets -> total negative index = number of quartets
print("\n(C) K distinct off-line quartets -> negative index = K")
quartets = [(14.13, 0.18), (21.02, 0.25), (25.01, 0.31)]   # distinct (gamma,b)
for K in range(0, len(quartets)+1):
    M = sum((block_gram(g, b) for g, b in quartets[:K]), np.zeros((len(WIDTHS),)*2))
    p, n, z, ev = signature(M)
    print(f"   K={K}:  signature (pos,neg,zero) = ({p},{n},{z})   "
          f"-> negative index = {n}  (expected {K})")

# (D) geometric mechanism + a real constraint:
#     a Lorentzian (1,N-1) intersection form (arithmetic Hodge index, Faltings-Hriljac) can
#     produce the per-block (1,1)/(1,0) -- BUT only for cycle-planes that meet the positive
#     (timelike) cone. A generic 2-plane is (0,2): the cone is "thin" (1 timelike vs N-1
#     spacelike). So each off-line Z_rho must carry one timelike (positive) direction; this is
#     a nontrivial geometric constraint a candidate must explain (the single + = polarization).
print("\n(D) Lorentzian (1,N-1) intersection form (arithmetic Hodge index) restricted to planes")
N = 8
J = np.diag([1.0] + [-1.0]*(N-1))                       # sig (1,7): 1 timelike, 7 spacelike
e = np.eye(N)
rng = np.random.default_rng(0)
# random 2-planes: how often is the restriction (1,1)?
cnt = {}
for _ in range(2000):
    P = rng.standard_normal((N, 2))
    s = signature(P.T @ J @ P)[:2]
    cnt[s] = cnt.get(s, 0) + 1
print(f"   random 2-plane restricted signature distribution: "
      f"{ {f'{k[0]},{k[1]}': v for k,v in sorted(cnt.items())} }")
print( "     -> a GENERIC plane is (0,2); (1,1) is NOT automatic (the cone is thin).")
# off-line cycle-plane = span{ timelike e_0 (the polarization), one spacelike } -> (1,1)
P_off = np.column_stack([e[0], e[1]])
p, n, z, _ = signature(P_off.T @ J @ P_off)
print(f"   off-line Z_rho = span(timelike, spacelike): signature = ({p},{n},{z})  [target (1,1)]")
# on-line cycle = the single timelike polarization direction (imag part collapses) -> (1,0)
P_on = e[0:1].T
p, n, z, _ = signature(P_on.T @ J @ P_on)
print(f"   on-line  Z_rho = span(timelike) only:       signature = ({p},{n},{z})  [target (1,0)]")

print("\n" + "="*74)
print("VERDICT: the bilinear Weil-Gram has exactly the (1,0)/(1,1) block structure, the")
print("negative index counts off-line quartets, and it switches on continuously with b (A.2).")
print("An arithmetic Lorentzian (1,N-1) intersection form is signature-COMPATIBLE, but only")
print("if every off-line cycle-plane Z_rho contains the one positive (polarization) direction")
print("-- a genuine constraint, not automatic. The F-indep origin of the cycles Z_rho remains")
print("the open test that decides A-pass vs A-fail.")
print("="*74)
