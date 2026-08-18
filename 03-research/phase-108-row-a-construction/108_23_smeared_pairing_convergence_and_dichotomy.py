#!/usr/bin/env python3
"""Verifier for 108.23 - the smeared object converges as a formal sum but is
   a zero-sourced definition, not a forced extension.  numpy only.

   IMPORTANT: no actual zeta zero locations are used anywhere below. The
   convergence test uses a SYNTHETIC ordinate sequence built purely from the
   classical, unconditional Riemann-von Mangoldt counting-function asymptotic
   N(T) ~ (T/2pi) log(T/2pi e) + 7/8, inverted by bisection. This is a
   statement about growth rate, not about any zero's actual position, and
   does not touch RH."""
import numpy as np, sys
FAIL = []
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# --- synthetic zero-ordinate sequence from the classical counting bound ---
def N_of_T(T):
    return (T/(2*np.pi))*np.log(T/(2*np.pi*np.e)) + 7.0/8.0

def bisect_increasing(target, lo, hi, f, iters=80):
    flo = f(lo)
    for _ in range(iters):
        mid = 0.5*(lo+hi)
        if f(mid) < target: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)

def synthetic_ordinates(n_terms, T_lo=15.0, T_hi_start=1e6):
    # N(T) is increasing for T > 2*pi*e ~ 17.08; start search comfortably
    # above that, and grow the search window until it brackets each target.
    out = []
    hi = T_hi_start
    for n in range(1, n_terms+1):
        while N_of_T(hi) < n: hi *= 2
        t = bisect_increasing(n, T_lo, hi, N_of_T)
        out.append(t)
    return np.array(out)

n_terms = 3000
t_n = synthetic_ordinates(n_terms)
ok = np.all(np.diff(t_n) > 0)
check("synthetic ordinates strictly increasing (sanity)", ok,
      f"t_1={t_n[0]:.2f} t_{n_terms}={t_n[-1]:.2f}")
# cross-check: the synthetic sequence really does reproduce N(T)~n
resid = np.max(np.abs(N_of_T(t_n) - np.arange(1, n_terms+1)))
check("synthetic ordinates invert N(T) to high precision", resid < 1e-6,
      f"max residual {resid:.2e}")

# --- (A)+(B) convergence of sum_rho phi(Re rho) ghat(rho') --------------
# phi: bump on [0.2,0.8], bounded, compact support in [0,1].
def phi(a):
    a = np.asarray(a, dtype=float)
    out = np.zeros_like(a)
    m = (a > 0.2) & (a < 0.8)
    out[m] = np.exp(-1.0/(1-((a[m]-0.5)/0.3)**2))  # smooth bump, |.|<1 on support
    return out

# ghat with Gaussian decay along verticals: s0*sqrt(2pi)*exp(s0^2 s^2/2)
def ghat_gaussian(s, s0=0.15):
    return s0*np.sqrt(2*np.pi)*np.exp(s0**2*(s**2)/2.0)

# ghat with insufficient decay (control): power-law decay only
def ghat_slow(s):
    return 1.0/(1.0+np.abs(s)**1.2)

# use Re(rho) = 0.5 as a representative value: Theorem 2.1's proof only uses
# boundedness of phi on (0,1), not the actual real parts (classical fact
# 0 < Re(rho) < 1 is all that's needed) -- so any fixed representative in
# (0,1) exercises the SAME convergence mechanism the proof relies on.
re_rho = 0.5
rho_prime = np.array([ (1-re_rho) + 1j*t for t in t_n ])  # rho' = 1-conj(rho)

def partial_sums(ghat_fn):
    terms = phi(re_rho*np.ones(n_terms)) * np.conj(ghat_fn(rho_prime))
    return np.cumsum(terms)

ps_fast = partial_sums(ghat_gaussian)
ps_slow = partial_sums(ghat_slow)

# Cauchy criterion on the tail: fast case should stabilize
tail_fast = np.abs(ps_fast[-1] - ps_fast[n_terms//2])
check("Gaussian-decay ghat: partial sums stabilize (Cauchy tail -> 0)",
      tail_fast < 1e-8, f"tail(N/2..N)={tail_fast:.3e}")

# slow-decay control: tail should NOT be negligible / sums keep growing
tail_slow = np.abs(ps_slow[-1] - ps_slow[n_terms//2])
growth_ratio = np.abs(ps_slow[-1])/max(np.abs(ps_slow[n_terms//4]), 1e-300)
check("power-law-decay ghat: partial sums do NOT stabilize (decay hypothesis "
      "is load-bearing)", tail_slow > 1e-3, f"tail(N/2..N)={tail_slow:.3e}")

# --- (C) the exact D(T)*int(phi) + int(phi*L_g) identity -----------------
# Illustrative model only: D(T) stands in for the unevaluated, a-independent
# divergent part; L_g(a,T) stands in for 108_11's closed a-dependent object
# -- a bounded function of a that itself CONVERGES pointwise as T->inf
# (mirroring 108_11's cited closure), but need not be T-independent at
# finite T.
GRID = np.linspace(1e-6, 1-1e-6, 40001)
def D(T): return np.log(T)                       # unbounded, monotone
def L_g(a, T): return np.sin(2*np.pi*a) * (1 - 1.0/T)  # -> sin(2 pi a)

def integral(fn_of_a):
    return np.trapz(fn_of_a(GRID), GRID)

def Sigma(phi_fn, T):
    return np.trapz(phi_fn(GRID)*(D(T) + L_g(GRID, T)), GRID)

def phi_generic(a):
    # smooth bump on (0.1,0.9), strictly positive integral; smooth (not a
    # hard step) so trapz quadrature is grid-insensitive.
    a = np.asarray(a, dtype=float)
    z = np.clip((a-0.1)/0.8, 1e-9, 1-1e-9)
    return np.exp(-1.0/(z*(1-z)))

def phi_meanzero(a):
    a = np.asarray(a, dtype=float)
    return np.sin(2*np.pi*a)  # int_0^1 sin(2 pi a) da = 0 exactly

int_phi_generic = integral(phi_generic)
int_phi_meanzero = integral(phi_meanzero)
check("int(phi_meanzero) = 0 to quadrature precision", abs(int_phi_meanzero) < 1e-10,
      f"{int_phi_meanzero:.2e}")
check("int(phi_generic) != 0", abs(int_phi_generic) > 1e-3, f"{int_phi_generic:.4f}")

Ts = np.array([10.0, 1e2, 1e4, 1e6, 1e8, 1e10])
Sigma_generic = np.array([Sigma(phi_generic, T) for T in Ts])
Sigma_meanzero = np.array([Sigma(phi_meanzero, T) for T in Ts])

# generic phi: Sigma = D(T)*int(phi) + int(phi*L_g(.,T)) EXACTLY, and since
# D(T)=log(T) is unbounded and int(phi) != 0, Sigma diverges (fit slope vs
# log T should match int_phi_generic).
predicted_generic = D(Ts)*int_phi_generic + np.array(
    [np.trapz(phi_generic(GRID)*L_g(GRID, T), GRID) for T in Ts])
slope = np.polyfit(np.log(Ts), Sigma_generic, 1)[0]
check("generic phi: Sigma_g(phi,T) diverges as T->infty, slope vs log T "
      "matches int(phi) (Theorem 1.1-style rate)",
      abs(slope-int_phi_generic) < 1e-6,
      f"fitted slope={slope:.6f} int(phi)={int_phi_generic:.6f}")
check("generic phi: Sigma matches D(T)*int(phi) + int(phi*L_g) exactly",
      np.allclose(Sigma_generic, predicted_generic, rtol=1e-6),
      f"max rel diff {np.max(np.abs((Sigma_generic-predicted_generic)/predicted_generic)):.2e}")

# mean-zero phi: the D(T)-term contributes EXACTLY zero at every finite T
# (not asymptotically) -- verified by comparing Sigma against int(phi*L_g)
# alone, with the divergent D(T) term dropped.
L_g_part = np.array([np.trapz(phi_meanzero(GRID)*L_g(GRID, T), GRID) for T in Ts])
check("mean-zero phi: Sigma_g(phi,T) = int(phi*L_g(.,T)) EXACTLY at every T "
      "(the unbounded D(T) term cancels identically, not asymptotically)",
      np.allclose(Sigma_meanzero, L_g_part, atol=1e-9),
      f"max abs diff {np.max(np.abs(Sigma_meanzero-L_g_part)):.2e}")
# ... and THAT (bounded) quantity converges as T -> infty, per the cited
# closure of 108_11's a-dependent object -- unlike the generic-phi case,
# which diverges outright.
expected_limit = integral(lambda a: phi_meanzero(a)*np.sin(2*np.pi*a))  # = 0.5
check("mean-zero phi: Sigma_g(phi,T) converges (stays bounded, -> 0.5) as "
      "T->infty, in contrast to the generic-phi divergence above",
      abs(Sigma_meanzero[-1]-expected_limit) < 1e-3 and
      np.max(np.abs(Sigma_meanzero)) < 1.0,
      f"Sigma(T=1e10)={Sigma_meanzero[-1]:.6f} expected_limit={expected_limit:.6f}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
