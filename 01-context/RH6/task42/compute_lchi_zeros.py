
"""
Compute the first 5000 zeros of L(s, chi_4 mod 5) to dps=50.
The character chi is the order-4 primitive character mod 5 with chi(2)=i.
Saves results as lchi_zeros_5000_dps50.npy.
"""
import time
import math
import numpy as np
import mpmath as mpm
from mpmath import mp, mpf, mpc as MPC, pi as mp_pi, exp as mp_exp, gamma as mp_gamma, sqrt as mp_sqrt, arg as mp_arg, log as mp_log mp.dps = 50 # --- Character definition ---
# Order-4 primitive Dirichlet character mod 5:
# chi(0)=0, chi(1)=1, chi(2)=i, chi(3)=-i, chi(4)=-1
# This is the choice with chi(2)=i. It is an ODD character: chi(-1)=chi(4)=-1.
q = 5
a = 1 # odd character (gamma factor index)
chi_list = [0, 1, 1j, -1j, -1] # Verify multiplicativity
for x in range(1, 20): for y in range(1, 20): v1 = chi_list[(x*y) % q] if (x*y) % q != 0 else 0 v2 = chi_list[x % q] * chi_list[y % q] assert abs(v1 - v2) < 1e-12 # --- Compute Gauss sum and epsilon factor ---
tau_chi = MPC(0)
for n in range(1, q): tau_chi += chi_list[n] * mp_exp(MPC(0, 2)*mp_pi*n/q)
epsilon = tau_chi / (MPC(0,1)**a * mp_sqrt(q))
assert abs(abs(epsilon) - 1) < 1e-45, f"|epsilon|={abs(epsilon)}"
eps_sqrt = mpm.sqrt(epsilon) # --- Hardy-style real-valued Z function ---
# Lambda(s, chi) = (q/pi)^((s+a)/2) * Gamma((s+a)/2) * L(s, chi)
# FE: Lambda(s, chi) = eps * conj(Lambda(s, chi)) on Re(s)=1/2
# => Z(t) := eps^{-1/2} * (q/pi)^((1/2+it+a)/2) * Gamma((1/2+it+a)/2) * L(1/2+it, chi) is REAL
# But this magnitudes decays super-exponentially. So divide out the magnitude (keep argument):
# Z_Hardy(t) = exp(i * theta(t)) * L(1/2+it, chi)
# where theta(t) = arg[ (q/pi)^((1/2+it+a)/2) * Gamma((1/2+it+a)/2) / eps^{1/2} ] def theta_chi(t): s = MPC(mpf("0.5"), t) half = (s + a) / 2 return mp_arg((mpf(q)/mp_pi)**half * mp_gamma(half) / eps_sqrt) def Z_hardy(t): s = MPC(mpf("0.5"), t) L = mpm.dirichlet(s, chi_list) return (mp_exp(MPC(0, theta_chi(t))) * L).real # Approximate zero density (mean gap)
def mean_gap(t): return 2*math.pi / math.log(max(q*t/(2*math.pi), 2.0)) # --- Adaptive sign-change scan with secant root-find ---
target = int(__import__("os").environ.get("N_ZEROS", "5000"))
output_path = __import__("os").environ.get("OUTPUT", "lchi_zeros_5000_dps50.npy")
checkpoint_every = 100 zeros = []
t_curr = mpf("0.1")
prev_z = Z_hardy(t_curr)
prev_sign = 1 if prev_z > 0 else -1
n_evals = 1
t0_all = time.time()
ckpt_path = output_path + ".ckpt.npy" # load checkpoint if exists
try: saved = np.load(ckpt_path, allow_pickle=True) if len(saved) > 0: zeros = [mpf(str(x)) for x in saved] t_curr = zeros[-1] + mpf(str(mean_gap(float(zeros[-1])) * 0.1)) prev_z = Z_hardy(t_curr) prev_sign = 1 if prev_z > 0 else -1 n_evals += 1 print(f"Resumed from checkpoint with {len(zeros)} zeros, t={float(t_curr):.3f}")
except FileNotFoundError: pass while len(zeros) < target: gap = mean_gap(float(t_curr)) step = mpf(gap/4) # 4 samples per mean gap t_next = t_curr + step z_next = Z_hardy(t_next) n_evals += 1 s_next = 1 if z_next > 0 else -1 if s_next != prev_sign: # Found sign change; secant-style root finding try: root = mpm.findroot(lambda x: Z_hardy(x), (t_curr, t_next), solver="anderson", tol=mpf(10)**(-45)) n_evals += 10 except Exception: lo_t, hi_t = t_curr, t_next lo_z, hi_z = prev_z, z_next for _ in range(200): mid = (lo_t + hi_t) / 2 mz = Z_hardy(mid) n_evals += 1 if (mz > 0) == (lo_z > 0): lo_t, lo_z = mid, mz else: hi_t, hi_z = mid, mz if abs(hi_t - lo_t) < mpf(10)**(-48): break root = (lo_t + hi_t) / 2 zeros.append(root) if len(zeros) % checkpoint_every == 0: elapsed = time.time() - t0_all rate = len(zeros) / elapsed est_remaining = (target - len(zeros)) / rate if rate > 0 else 0 print(f" {len(zeros)} zeros, t={float(root):.2f}, elapsed={elapsed:.0f}s, evals={n_evals}, rate={rate:.2f} zeros/s, est_remaining={est_remaining:.0f}s") # save checkpoint np.save(ckpt_path, np.array([mpm.nstr(z, 55) for z in zeros])) prev_z = z_next prev_sign = s_next t_curr = t_next # Save final result as strings to preserve precision; also save as float64 array for convenience
zeros_str = np.array([mpm.nstr(z, 55) for z in zeros])
np.save(output_path, zeros_str)
print(f"Saved {len(zeros)} zeros to {output_path}")
print(f"Total time: {time.time()-t0_all:.0f}s, total evals: {n_evals}")
print(f"First zero: {zeros[0]}")
print(f"Last zero: {zeros[-1]}")
