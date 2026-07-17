"""
Phase 20, Step 1: Fluctuation analysis of M_k(N) / (logN)^{k^2}.
(Ruta C: does the ω forward flow encode zero information in its fluctuations?)

KNOWN (Phase 19): M_k(N) ~ C_k (logN)^{k^2}.  The MEAN is insensitive to zeros.

QUESTION: Do the FLUCTUATIONS of M_k(N) around C_k(logN)^{k^2} encode zero info?

MECHANISM (if κ>0):
  M_k(N) = (1/2πi) ∫ F(s) N^s/s ds   [Perron formula, F(s)=zeta(s)^{k^2}*G(s)]
  The residue at s=1 gives C_k(logN)^{k^2}.
  Each zero rho of zeta gives a term N^rho/rho * d^{k^2-1}/ds^{k^2-1}[...].
  For on-line zeros rho=1/2+i*gamma: term ~ N^{1/2+i*gamma} (amplitude N^{1/2}).
  For off-line zero rho=sigma+i*gamma, sigma>1/2: term ~ N^{sigma} (amplitude > N^{1/2}).

  PREDICTION:
    kappa=0 -> R_k(N) := M_k(N)/(logN)^{k^2} oscillates with amplitude ~ N^{1/2-1} = N^{-1/2}
              (the N^{1/2} zero contribution divided by (logN)^{k^2} ~ N * sub-poly)
    kappa>0 -> ADDITIONAL term ~ N^{sigma-1} with sigma > 1/2 -> decays SLOWER than N^{-1/2}

  OBSERVABLE: Compute R_k(N) for many N; estimate amplitude via range or std; check decay rate.

MEASUREMENT STRATEGY:
  Instead of computing R_k directly (needs precise C_k), use the RATIO:
     Q_k(N) := M_k(N) / M_k(N/e)  - e^{k^2}
  This cancels C_k and isolates the sub-leading oscillation.
  If M_k(N) ~ C_k (logN)^{k^2}: M_k(N)/M_k(N/e) ~ (logN)^{k^2}/(logN-1)^{k^2} ~ e^{k^2}
  The RESIDUAL Q_k(N) = oscillatory term ~ amplitude * N^{-1/2} (if kappa=0).

  Check: does std(Q_k) decrease as N grows at rate N^{-1/2}?
"""
import numpy as np

N_MAX = 2_000_000

# ---- sieve omega(n) ----------------------------------------------------------
sieve = np.ones(N_MAX+1, dtype=bool); sieve[:2] = False
for p in range(2, int(N_MAX**0.5)+1):
    if sieve[p]:
        sieve[p*p::p] = False
primes = np.nonzero(sieve)[0]
omega = np.zeros(N_MAX+1, dtype=np.int16)
for p in primes:
    omega[p::p] += 1
om = omega[1:].astype(np.float64)
inv_n = 1.0 / np.arange(1, N_MAX+1, dtype=np.float64)
print(f"Sieved omega(n) for n<={N_MAX:,}")

# Build cumulative M_k(N) for many N values
# We evaluate at a fine grid to see oscillations
N_vals = np.arange(10_000, N_MAX+1, 500)   # step 500

print("\n" + "="*70)
print("Step 1: Computing M_k(N) at fine grid (step=500)...")
print("="*70)

def compute_Mk_series(k, N_vals):
    """Return M_k(N) for each N in N_vals (cumulative sum)."""
    q = k*k
    w = (q**om) * inv_n         # contribution of each n: q^{omega(n)}/n
    Mk = np.cumsum(w)            # Mk[j] = M_k(j+1)
    # subsample at N_vals
    return Mk[N_vals - 1]        # index N-1 gives sum up to N

for k in [1.0, 1.5, 2.0]:
    q = k*k
    Mk_series = compute_Mk_series(k, N_vals)
    logN_series = np.log(N_vals.astype(float))

    # Ratio Q_k(N) = M_k(N) / M_k(N/e) - e^{k^2}
    # For N/e: find closest index
    e_val = np.e
    N_over_e = (N_vals / e_val).astype(int)
    N_over_e = np.clip(N_over_e, 1, N_MAX)
    Mk_Ne = np.array([compute_Mk_series(k, np.array([n]))[0] for n in N_over_e[:20]])
    # Too slow for full series; use a faster approach

    # Alternative: estimate oscillation amplitude directly from the normalized residual
    # R_k(N) = M_k(N) / (logN)^{k^2}
    Rk = Mk_series / logN_series**q
    # R_k should converge to C_k as N grows.  Estimate C_k ~ mean over last 20%
    n_last = len(Rk) // 5
    C_k_est = float(Rk[-n_last:].mean())

    # Oscillation amplitude: std of R_k - C_k, measured in windows
    residual = Rk - C_k_est
    # Divide into 4 quartiles of N
    q1 = len(N_vals)//4
    std_q1 = float(residual[:q1].std())
    std_q2 = float(residual[q1:2*q1].std())
    std_q3 = float(residual[2*q1:3*q1].std())
    std_q4 = float(residual[3*q1:].std())
    N_q1 = float(N_vals[q1//2])
    N_q2 = float(N_vals[q1+q1//2])
    N_q3 = float(N_vals[2*q1+q1//2])
    N_q4 = float(N_vals[3*q1+q1//2])

    print(f"\nk={k:.1f} (q=k^2={q:.2f})  C_k_est={C_k_est:.6f}")
    print(f"  Oscillation amplitude std(R_k - C_k) in N quartiles:")
    print(f"    Q1 (N~{N_q1:.0f}): std={std_q1:.6f}")
    print(f"    Q2 (N~{N_q2:.0f}): std={std_q2:.6f}")
    print(f"    Q3 (N~{N_q3:.0f}): std={std_q3:.6f}")
    print(f"    Q4 (N~{N_q4:.0f}): std={std_q4:.6f}")
    # Check decay: if std ~ A * N^{alpha}, estimate alpha from Q1/Q4 ratio
    alpha_est = np.log(std_q4/std_q1) / np.log(N_q4/N_q1) if std_q1 > 0 else float('nan')
    print(f"  Estimated decay exponent alpha (std ~ N^alpha): {alpha_est:.4f}")
    print(f"  (kappa=0 prediction: alpha ~ -1/2 = -0.5000; kappa>0: alpha > -0.5)")

print("\n" + "="*70)
print("Step 2: Q_k(N) = R_k(N)/R_k(N-step) - (logN/log(N-step))^{k^2}")
print("  This isolates incremental oscillations (cancels C_k more precisely).")
print("="*70)
STEP = 10_000   # step size for ratio
N_ratio_vals = np.arange(50_000, N_MAX+1, STEP)

for k in [1.0, 1.5, 2.0]:
    q = k*k
    Mk_series = compute_Mk_series(k, N_ratio_vals)
    Mk_prev = compute_Mk_series(k, N_ratio_vals - STEP)
    logN = np.log(N_ratio_vals.astype(float))
    logN_prev = np.log((N_ratio_vals - STEP).astype(float))
    # incremental ratio minus predicted factor
    ratio = Mk_series / Mk_prev
    expected_ratio = (logN / logN_prev)**q
    Qk = ratio / expected_ratio - 1.0    # should be 0 + oscillation

    n_last = len(Qk)//5
    print(f"\nk={k:.1f}: Q_k oscillation (ratio method):")
    print(f"  Mean(Q_k) = {Qk.mean():.6f}  (should be ~0)")
    print(f"  Std(Q_k) overall = {Qk.std():.6f}")
    # Quartile stds to measure decay
    q1 = len(Qk)//4
    std_q4 = Qk[3*q1:].std()
    std_q1 = Qk[:q1].std()
    N_q1 = float(N_ratio_vals[q1//2])
    N_q4 = float(N_ratio_vals[3*q1+q1//2])
    alpha_est = np.log(std_q4/std_q1) / np.log(N_q4/N_q1) if std_q1 > 0 else float('nan')
    print(f"  Decay exponent alpha: {alpha_est:.4f}  (kappa=0 predicts alpha ~ -1/2)")

print("\n" + "="*70)
print("READING:")
print()
print("  IF alpha ~ -0.5: the fluctuations of M_k decay as N^{-1/2}, consistent with")
print("  ONLY on-line zeros driving the oscillation (kappa=0 picture).")
print()
print("  IF alpha > -0.5 (slower decay): potential signal of off-line zero terms.")
print("  NOTE: finite-N effects and the approach to C_k can mimic slower decay;")
print("  a careful sub-leading analysis would be needed before claiming a signal.")
print()
print("  IF alpha < -0.5 (faster decay): unexpected; would suggest cancellation between")
print("  zero contributions (e.g. Montgomery pair correlation).")
print()
print("  HONEST CAVEAT: at N=2e6 the zero oscillations are very small (N^{-1/2} ~ 0.0007)")
print("  relative to C_k ~ 0.01-1.0. The signal-to-noise ratio is extremely low.")
print("  This experiment is a qualitative probe, not a precision measurement.")
print("="*70)
