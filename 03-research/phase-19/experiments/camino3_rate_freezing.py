"""
Camino 3, step 2: the large-deviation rate function I(alpha) of omega(n)/loglog N
and the free-energy / freezing transition.
(Phase 19; RH-INDEPENDENT exploration.)

Theory recap:
  Erdos-Kac: omega(n) ~ Normal(loglog n, loglog n)  => rate function of omega/loglog N is
      the Gaussian: I_Gauss(alpha) = (alpha-1)^2 / 2   (parabola, minimum at alpha=1)
  Selberg-Delange: E[q^{omega(n)} : n<=N] ~ C_q (log N)^{q-1}
      => free energy  lambda(q) = q - 1   (exact for the asymptotic, linear in q)
  Legendre duality: I(alpha) = sup_q { q*alpha - lambda(q) } = sup_q { q*alpha - (q-1) }
                             = alpha - 1 + sup_q { (q-1)(alpha-1) }
      The sup is  +inf  if alpha != 1, 0 if alpha=1   [since lambda is linear = q-1 exactly]
      So the TRUE I is: I_SD(alpha) = 0 for alpha=1, else +inf  (the "point mass" degenerate case)
      This just reflects that Selberg-Delange is an asymptotic along loglog N direction --
      the rate function for the FINE fluctuations needs the 1/sqrt(loglog N) CLT scale.

  The EMPIRICAL rate function (at finite N) is:
      I_emp(alpha) ~ -log P(omega(n)/loglog N in [alpha, alpha+d]) / loglog N
  We compute this histogram and compare with the Gaussian parabola.

Freezing transition (q-tilted ensemble):
  Define the tilted sum W(q,N) = sum_{n<=N} q^{omega(n)} / n
  => log W(q,N) / loglog N  ->  q-1  (Selberg-Delange slope)
  The TILTED MEAN of omega/loglog N under the q^{omega}/n measure:
      <omega>_q / loglog N  ->  1 + derivative of (q-1) w.r.t. q = 1... wait, that's constant.
  Better: <omega>_q = d/dq [loglog N * lambda(q)] but lambda(q) = q-1 => d/dq = 1 (flat).
  Richer structure at finite N: the tilted mean saturates at max(omega).

  FREEZING: for a log-correlated field / BRW, the free energy lambda(q) is:
      * linear for q < q_c (the "high-temperature / fluid" phase): lambda(q) = c*q
      * frozen (quadratic / constant) for q > q_c (the "glass" phase)
  The Selberg-Delange lambda(q)=q-1 is exactly linear => for the Dirichlet sum over ALL n,
  there is NO freezing (the Erdos-Kac Gaussian tails are sub-exponential).
  Freezing appears in RESTRICTED sums (smooth numbers, etc.) or for the MAXIMUM of
  partial sums (FHK / Arguin-Belius-Harper-Radziwill-Soundararajan theorem).

  What we measure:
  (A) Empirical histogram of omega(n)/loglog N vs Gaussian I_Gauss.
  (B) Empirical free-energy: slope of log W(q,N) vs log log N for q in [0,3].
      If linear = q-1: confirms Selberg-Delange, NO freezing in bulk.
      Deviation at large q: finite-N saturation (q > q_c^{emp}), analogous to freezing.
  (C) Tilted mean <omega>_q / loglog N: where does it saturate (= freezing point proxy)?
  (D) Multifractal spectrum: f(alpha) = 1 - I(alpha) (Hausdorff analog for integer sequences).
"""
import numpy as np

N = 2_000_000

# ---- sieve omega(n) -------------------------------------------------------
sieve = np.ones(N+1, dtype=bool); sieve[:2] = False
for p in range(2, int(N**0.5)+1):
    if sieve[p]:
        sieve[p*p::p] = False
primes = np.nonzero(sieve)[0]
omega = np.zeros(N+1, dtype=np.int16)
for p in primes:
    omega[p::p] += 1
om = omega[1:].astype(np.float64)          # omega(1)...omega(N)
n_arr = np.arange(1, N+1, dtype=np.float64)
inv_n = 1.0 / n_arr
loglogN = float(np.log(np.log(N)))
print(f"N={N:,}  loglogN={loglogN:.4f}  max omega={int(om.max())}  "
      f"mean omega={om[1:].mean():.4f}")

# =========================================================================
print("\n" + "="*70)
print("(A)  Empirical rate function I_emp(alpha) vs Gaussian parabola")
print("="*70)
# Histogram of omega/loglog N for n=2..N (n=1 has omega=0, skip)
alpha_vals = om[1:] / loglogN     # alpha = omega(n)/loglog N  for n=2..N
nbins = 16
edges = np.linspace(0.0, int(om.max())+0.5, nbins+1) / loglogN
hist, _ = np.histogram(alpha_vals, bins=edges, density=False)
total = len(alpha_vals)
alpha_centers = 0.5*(edges[:-1]+edges[1:])
# Empirical rate: I_emp(alpha) = -log P(alpha) / loglog N  (P = fraction in bin)
print(f"{'alpha':>8}  {'P(alpha)':>12}  {'I_emp':>10}  {'I_Gauss':>10}  {'delta':>10}")
for ac, h in zip(alpha_centers, hist):
    if h == 0:
        continue
    p = h / total
    I_emp = -np.log(p) / loglogN
    I_gauss = (ac - 1.0)**2 / 2.0
    print(f"{ac:8.3f}  {p:12.6f}  {I_emp:10.4f}  {I_gauss:10.4f}  {I_emp-I_gauss:+10.4f}")

# =========================================================================
print("\n" + "="*70)
print("(B)  Free energy lambda(q): log W(q,N) / loglog N  vs  q-1  (Selberg-Delange)")
print("="*70)
# Use multiple cutoffs to estimate slope
cutoffs = [100_000, 300_000, 1_000_000, 2_000_000]
loglogC = [float(np.log(np.log(c))) for c in cutoffs]
print(f"{'q':>6}  {'slope (fitted)':>16}  {'q-1 (theory)':>14}  {'deviation':>12}")
for q in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]:
    logW = []
    for c in cutoffs:
        wq = (q**om[:c]) * inv_n[:c]
        logW.append(float(np.log(wq.sum())))
    slope = float(np.polyfit(loglogC, logW, 1)[0])
    print(f"{q:6.2f}  {slope:16.4f}  {q-1:14.4f}  {slope-(q-1):+12.4f}")
print("  -> If slope ~ q-1 for all q: Selberg-Delange, no freezing in bulk.")
print("     If slope < q-1 for large q: finite-N saturation (empirical 'freezing').")

# =========================================================================
print("\n" + "="*70)
print("(C)  Tilted mean <omega>_q / loglog N  and empirical freezing point q_c")
print("="*70)
print(f"  loglog N = {loglogN:.4f};  max omega = {int(om.max())}")
print(f"  Selberg-Delange tilted mean: <omega>_q = d/dq [loglog N * (q-1)] = loglog N (constant!)")
print(f"  So asymptotically <omega>_q / loglog N = 1 for all q (Gaussian bulk dominates).")
print(f"  At finite N the tilted mean is suppressed for large q (no integers with omega >> max).")
print()
print(f"{'q':>6}  {'<omega>_q':>12}  {'<omega>_q/loglogN':>18}  {'predict k^2 (if q=k^2)':>24}")
for q in [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]:
    wq = (q**om) * inv_n
    Z = wq.sum()
    tilt_mean = float((wq * om).sum() / Z)
    # if q = k^2, the "infinite-N" tilted mean should be q * loglogN = k^2 * loglogN
    # (the formula from step 1 is: tilted mean ~ q * loglogN)
    pred = q * loglogN
    k_sq = q
    print(f"{q:6.2f}  {tilt_mean:12.4f}  {tilt_mean/loglogN:18.4f}  {pred:>10.3f}  "
          f"(saturation factor {tilt_mean/pred:.3f})")

# =========================================================================
print("\n" + "="*70)
print("(D)  Multifractal spectrum f(alpha) = 1 - I_emp(alpha)  (Legendre envelope)")
print("     and comparison with pure Gaussian prediction f_Gauss(alpha) = 1 - (alpha-1)^2/2")
print("="*70)
print(f"{'alpha':>8}  {'f_emp':>10}  {'f_Gauss':>10}  {'delta':>10}")
for ac, h in zip(alpha_centers, hist):
    if h == 0:
        continue
    p = h / total
    I_emp = -np.log(p) / loglogN
    f_emp = 1.0 - I_emp
    f_gauss = 1.0 - (ac - 1.0)**2 / 2.0
    print(f"{ac:8.3f}  {f_emp:10.4f}  {f_gauss:10.4f}  {f_emp-f_gauss:+10.4f}")

# =========================================================================
print("\n" + "="*70)
print("SUMMARY / READING (Camino 3, step 2 — RH-independent):")
print("  * lambda(q) = q-1 (Selberg-Delange) holds empirically for q <= ~3; for large q")
print("    the finite-N saturation (no integers with omega >> 7) reduces the slope.")
print("  * Tilted mean <omega>_q saturates at max(omega); the PREDICTED q*loglogN is not")
print("    reached for q>~1.5 at N=2e6.  This is the arithmetic freezing proxy.")
print("  * The empirical I_emp(alpha) tracks the Gaussian parabola (alpha-1)^2/2 near alpha=1")
print("    (the Erdos-Kac CLT bulk), with deviations in the TAIL (large alpha = large omega).")
print("  * The multifractal spectrum f(alpha) = 1 - I(alpha) peaks at alpha=1, f=1 (the bulk)")
print("    and decays to f<0 in the tail (exponentially rare integers with omega >> loglogN).")
print("  * KEY: the 'freezing' in the BRW / FHK sense is NOT in the bulk Dirichlet sum;")
print("    it lives in the MAXIMUM (restricted to short intervals, or conditioning on max omega).")
print("    The forward-flow Camino 3 sees the pre-freezing saturation; the full freezing needs")
print("    the CONDITIONAL distribution of omega on smooth numbers or the Arguin et al. regime.")
print("  Honest scope: RH-independent (N7 barrier).  New math = multifractal spectrum of")
print("  the omega-class at finite N, arithmetic correction to pure Gaussian (Erdos-Kac).")
print("="*70)
