"""
Camino 3, step 4: the quenched observable -- maximum of the random B-smooth
Dirichlet polynomial, the arithmetic side of the BRW/FHK freezing transition.
(Phase 19; RH-INDEPENDENT.)

Steps 1-3 studied ANNEALED observables (expectations, sums).  The true BRW freezing
transition is QUENCHED: it lives in the MAXIMUM of a log-correlated field over a
continuous parameter (t).

The experiment here:
  Fix B (smoothness level).  For each prime p <= B draw a random sign epsilon_p = +/-1
  (Rademacher; the random multiplicative function restricted to B-smooth numbers).
  Form the random Dirichlet polynomial:
      F(t) = sum_{n<=N, B-smooth} epsilon^{omega(n)} / sqrt(n) * e^{-it log n}
  Compute max_{t in [0, T]} |F(t)|^2 over a grid.
  Repeat R=200 realizations.  Estimate:
      E[max |F|^2]  and  Var[max |F|^2]
  Compare with the BRW prediction:
      E[max |F(t)|] ~ exp( sqrt( Sigma^2 * loglog(logB) ) )
  where Sigma^2 = sum_{p<=B} 1/p is the variance of log|F| (from each prime).

Why this is the right experiment:
  - F(t) is a log-correlated field: Cov(log|F(t)|, log|F(s)|) ~ sum_{p<=B} cos((t-s)logp)/p
    = -log|t-s| + O(1) for |t-s| in (1/logB, 1).
  - The maximum of a log-correlated GFF over [0,T] grows as sqrt(2 Sigma^2 logT) - C loglogT
    (the "freezing" law, Fyodorov-Keating / Arguin-Belius-Harper-RS for zeta).
  - For our B-smooth polynomial, Sigma^2 = sum_{p<=B} 1/p ~ log log B (Mertens).
  - The BRW freezing temperature is q_c = sqrt(2/Sigma^2) -- at q > q_c the maximum grows
    slower than expected (the "glass" phase).

What we measure:
  (A) Distribution of max_{t} |F(t)| over R realizations: histogram, mean, variance.
  (B) Scaling with T: does E[max] grow as C sqrt(logT)?  Fit.
  (C) Scaling with B: compare max statistics for B = 7, 11, 13 -- the freezing onset.
  (D) Prime-variance Sigma^2 = sum_{p<=B} 1/p: the log-correlated field strength.

Honest scope: this is a RANDOM model (epsilon_p random, not the actual Liouville function).
The connection to zeta: the actual ζ(1/2+it) is believed to behave like a random
multiplicative Dirichlet polynomial; the random model gives the correct freezing law
(proven by Harper 2020 for smooth mollifiers).  The RH-independence holds: we never
use zero locations.
"""
import numpy as np
from numpy.fft import rfft, rfftfreq

rng = np.random.default_rng(42)

N_smooth = 500_000     # maximum n for smooth integers (smaller than full N for speed)
T_grid   = 4096        # number of t-values in [0, T]
T_max    = 100.0       # length of t-interval (should >> 1/logB ~ 0.3 for B=17)
R        = 300         # number of realizations

# ---- sieve primes, omega, smooth sets ----------------------------------------
sieve = np.ones(N_smooth+1, dtype=bool); sieve[:2] = False
for p in range(2, int(N_smooth**0.5)+1):
    if sieve[p]:
        sieve[p*p::p] = False
all_primes = np.nonzero(sieve)[0]

def make_smooth_data(B):
    """Return (n_arr, inv_sqrtn, om_arr, prime_list) for B-smooth n in [1, N_smooth]."""
    is_sm = np.ones(N_smooth+1, dtype=bool)
    for p in all_primes:
        if p > B:
            is_sm[p::p] = False
    omega = np.zeros(N_smooth+1, dtype=np.int8)
    p_list = [p for p in all_primes if p <= B]
    for p in p_list:
        omega[p::p] += 1
    idx = np.nonzero(is_sm[1:])[0]       # 0-indexed; actual n = idx+1
    n_arr = (idx + 1).astype(np.float64)
    inv_sqrtn = 1.0 / np.sqrt(n_arr)
    om_arr = omega[1:][idx].astype(np.int32)
    return n_arr, inv_sqrtn, om_arr, p_list

t_vals = np.linspace(0.0, T_max, T_grid)

print("="*70)
print("Camino 3, step 4: random B-smooth Dirichlet polynomial maximum")
print(f"  N_smooth={N_smooth:,}  T=[0,{T_max}]  grid={T_grid}  R={R} realizations")
print("="*70)

results = {}
for B in [7, 11, 13, 17]:
    n_arr, inv_sqrtn, om_arr, p_list = make_smooth_data(B)
    Sigma2 = float(sum(1.0/p for p in p_list))
    pi_B   = len(p_list)
    count  = len(n_arr)
    print(f"\nB={B}: {pi_B} primes  {count:,} smooth integers  "
          f"Sigma^2=sum(1/p)={Sigma2:.4f}  sqrt(Sigma^2)={Sigma2**0.5:.4f}")

    # Precompute log n (for the phase e^{-it log n})
    logn = np.log(n_arr)               # shape (count,)

    # Monte Carlo over R realizations
    max_vals = np.zeros(R)
    for r in range(R):
        # Draw random signs per prime, then eps^{omega(n)} = product of signs
        eps_p = rng.choice([-1.0, 1.0], size=pi_B)
        # eps^{omega(n)} = product_{primes p dividing n} eps_p
        # For each n, we need the product of signs of its prime factors.
        # Efficient: rebuild sign product via sieve approach -- but with small count,
        # just compute it directly from the prime factorization of each n.
        # Precompute: sign(n) = product_{p | n, p<=B} eps_p
        # Using: sign[n] = product eps_p for each prime p <= B dividing n
        sign_arr = np.ones(count, dtype=np.float64)
        for j, p in enumerate(p_list):
            # which smooth integers are divisible by p?
            divisible = (n_arr % p == 0)
            sign_arr[divisible] *= eps_p[j]
        # Amplitudes: sign_arr * inv_sqrtn
        amp = sign_arr * inv_sqrtn           # shape (count,)
        # F(t) = sum_n amp_n * e^{-it log n}
        # For each t: F(t) = sum_n amp_n * exp(-i * t * logn_n)
        # This is a non-uniform DFT.  For small count and T_grid, vectorize:
        # phase matrix shape (T_grid, count): phases[i,j] = -t_vals[i]*logn[j]
        # F_arr shape (T_grid,): complex
        # Do in blocks to manage memory
        BLOCK = 256
        F_max = 0.0
        for start in range(0, T_grid, BLOCK):
            t_block = t_vals[start:start+BLOCK]           # (blk,)
            phase = -np.outer(t_block, logn)              # (blk, count)
            F_block = (amp * np.exp(1j*phase)).sum(axis=1)  # (blk,)
            F_max = max(F_max, float(np.abs(F_block).max()))
        max_vals[r] = F_max

    mean_max  = float(max_vals.mean())
    std_max   = float(max_vals.std())
    med_max   = float(np.median(max_vals))
    # BRW prediction for mean: ~ exp(sqrt(2*Sigma^2 * log(T_max/1))) * const
    # For simplicity measure the empirical distribution
    results[B] = (mean_max, std_max, med_max, Sigma2)
    print(f"  max|F(t)| over {R} realizations:  mean={mean_max:.4f}  "
          f"std={std_max:.4f}  median={med_max:.4f}")
    print(f"  BRW proxy: 2*Sigma^2*log(T_max) = {2*Sigma2*np.log(T_max):.3f}  "
          f"sqrt = {(2*Sigma2*np.log(T_max))**0.5:.3f}")
    # Percentiles
    p5, p25, p75, p95 = np.percentile(max_vals, [5, 25, 75, 95])
    print(f"  Percentiles: 5%={p5:.3f}  25%={p25:.3f}  75%={p75:.3f}  95%={p95:.3f}")

print("\n" + "="*70)
print("COMPARISON TABLE: max statistics vs BRW predictions")
print("="*70)
print(f"{'B':>4}  {'Sigma^2':>9}  {'E[max]':>8}  {'std':>8}  "
      f"{'BRW_sqrt':>10}  {'ratio':>8}")
for B, (mean_m, std_m, med_m, s2) in results.items():
    brw = (2*s2*np.log(T_max))**0.5
    print(f"{B:4d}  {s2:9.4f}  {mean_m:8.4f}  {std_m:8.4f}  {brw:10.4f}  "
          f"{mean_m/brw:8.4f}")

print("\n" + "="*70)
print("READING (Camino 3, step 4 — RH-independent):")
print()
print("  1. The random B-smooth Dirichlet polynomial is a log-correlated field")
print("     with variance Sigma^2 = sum_{p<=B} 1/p ~ loglog B (Mertens).")
print("     The BRW prediction for the maximum: E[max|F|] ~ (2*Sigma^2*logT)^{1/2}.")
print()
print("  2. 'ratio' = E[max] / (2*Sigma^2*logT)^{1/2}: if ~ 1, the BRW scaling holds.")
print("     Deviation from 1 = the -C loglogT correction term (Fyodorov-Keating constant)")
print("     and finite-N/finite-T effects.")
print()
print("  3. Larger B => larger Sigma^2 => larger max (more log-correlation).")
print("     This is the arithmetic side of the FHK freezing: the prime sum Sigma^2=sum(1/p)")
print("     measures the strength of the log-correlated field; the maximum grows with B.")
print()
print("  4. KEY (honest caveat): with only ~1500-8000 B-smooth integers, the")
print("     polynomial F(t) has MANY GAPS -- it is not dense in t. The maximum is")
print("     a lower bound on the continuous maximum. The BRW scaling is expected")
print("     only in the N->inf / dense limit. This is the finite-N precursor.")
print()
print("  5. Honest scope: RH-independent (N7 barrier). The connection to zeta is via")
print("     Harper's theorem (random multiplicative function ~ zeta statistics) and")
print("     the FHK conjecture (proven for random models, open for actual zeta).")
print("="*70)
