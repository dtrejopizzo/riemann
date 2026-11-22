# DATASET DESCRIPTION: Riemann Hypothesis Research Program
## Resonance Detection and Class Separation in Arithmetic L-Functions **Version:** 3.0 **Date:** March 2026 **Status:** No external datasets required - all data is computationally generated --- ## 1. OVERVIEW ### Research Objective
This research program tests whether the Riemann Hypothesis can be understood as a consequence of multiplicative arithmetic structure. The central hypothesis is: > **Functions with multiplicative Dirichlet coefficients (Euler products) cannot exhibit the coherent phase alignment ("resonance") needed to produce zeros off the critical line Re(s) = 1/2. Functions without multiplicative structure can and do.** ### Primary Files
- **main.pdf**: State-of-the-art survey paper on the Riemann Hypothesis (29 pages) - Covers analytic, spectral, and algebro-geometric approaches - Details 2024 Guth-Maynard breakthrough on zero density - Extensive references and current status - **research-program-v3.pdf**: Complete research program specification (12 pages) - Detailed computational protocol - Definition of resonance detector and metrics - Six research tracks (A-F) with specific projects - Validation requirements ### Data Generation Nature
**NO EXTERNAL DATASETS ARE USED.** All data is generated computationally from first principles:
- Prime numbers (generated via sieve)
- Dirichlet character values (mod 5)
- Function coefficients (computed)
- Resonance detector outputs (evaluated numerically) --- ## 2. FUNCTION CLASSES (Primary Data Sources) The analysis compares **four core function classes** and two perturbations: ### 2.1 Riemann Zeta Function ζ(s)
- **Coefficients:** a_n = 1 for all n (real, multiplicative)
- **Euler product:** YES (ζ(s) = ∏_p (1 - p^(-s))^(-1))
- **RH status:** Expected TRUE (unproven)
- **Storage:** N × float64 (trivial)
- **Expected behavior:** - Mean square V_ζ ∼ log(N) - Maximum M_ζ ∼ exp(c√(log N)) (log-correlated field) - Kurtosis K_ζ ≈ 3-4 - Scaling exponent α_ζ ≈ 0 - GUE-like peak spacing ### 2.2 Dirichlet L-function L(s, χ₄)
- **Character:** Real non-principal character mod 5
- **Values:** χ₄(1)=1, χ₄(2)=-1, χ₄(3)=-1, χ₄(4)=1, χ₄(0)=0
- **Coefficients:** a_n = χ₄(n mod 5) (real, multiplicative)
- **Euler product:** YES
- **GRH status:** Expected TRUE (unproven)
- **Storage:** N × int8 (values in {-1, 0, 1})
- **Expected behavior:** Similar to ζ (different constants, same structure) ### 2.3 Random Multiplicative Function f_rand
- **Construction:** - At each prime p: a_p = ±1 with probability 1/2 each (independent) - Extend multiplicatively: a_{p₁^e₁ · ... · p_k^e_k} = a_{p₁}^{e₁} · ... · a_{p_k}^{e_k}
- **Euler product:** No (random, not standard L-function)
- **Purpose:** Test whether multiplicativity alone suppresses resonance
- **Storage:** π(N) × int8 for prime values + factorization cache
- **CRITICAL TEST:** Should behave like ζ, NOT like L_DH - If f_rand shows DH-like resonance → multiplicativity insufficient - If f_rand matches ζ → multiplicativity is key mechanism ### 2.4 Davenport-Heilbronn Function L_DH (CALIBRATION TARGET)
- **Definition:** L_DH(s) = ((1-iκ)/2)·L(s,χ) + ((1+iκ)/2)·L(s,χ̄) - χ: primitive complex character mod 5 of order 4 - χ(1)=1, χ(2)=i, χ(3)=-i, χ(4)=-1, χ(0)=0 - κ = (√5 - 1) / (2√(5(√5 - 1))) ≈ 0.2486
- **Coefficients:** a_n = ((1-iκ)/2)χ(n) + ((1+iκ)/2)χ̄(n) (complex, NOT multiplicative)
- **Euler product:** NO
- **RH status:** FALSE (proven - has zeros off critical line)
- **Known off-line zeros:** | σ (real part) | t (imaginary part) | β - 1/2 | Expected growth |
|---------------|-------------------|---------|-----------------|
| 0.8085 | 85.70 | 0.3085 | N^0.3085 |
| 0.6508 | 114.16 | 0.1508 | N^0.1508 |
| 0.5744 | 166.48 | 0.0744 | N^0.0744 |
| 0.7243 | 176.70 | 0.2243 | N^0.2243 | - **Storage:** N × complex128
- **Expected behavior:** - Anomalous peaks at t ≈ 85.7, 114.2, 166.5, 176.7 - Kurtosis K_DH >> 3 (very heavy tails) - Scaling exponent α_DH ≈ 0.31 (power-law growth!) - Persistence: Pers_DH(85.7; N₁, N₂) ∼ (N₂/N₁)^0.31 - Clustered peak spacing ### 2.5 Perturbed DH Family L_DH^(ε)
- **Definition:** Same as L_DH but with κ' = κ + ε
- **Perturbations tested:** ε ∈ {-0.1, -0.05, 0.05, 0.1}
- **Purpose:** Verify detector tracks zero migration, not DH-specific artifacts
- **Expected behavior:** Off-line zeros at different locations, similar qualitative features --- ## 3. CENTRAL COMPUTATIONAL OBJECT: D_F(t; N) ### 3.1 Definition
The **resonance detector** for function F at height t with truncation N: ```
D_F(t; N) = Σ_{n≤N} a_n(F) / n^(1/2 + it) = Σ_{n≤N} a_n(F) · n^(-1/2) · exp(-it·log(n))
``` ### 3.2 Computational Properties
- **Input:** Coefficient array a_n (length N) and height t
- **Output:** Complex number
- **Challenges:** - ~N highly oscillatory terms (n^(-it) = exp(-it·log n)) - Massive cancellation → catastrophic round-off if naive - **MANDATORY:** Use Kahan compensated summation or pairwise reduction
- **Data type:** complex128 (16 bytes per value)
- **Typical parameters:** - N ∈ {10^4, 10^5, 10^6} - t ∈ [T, 2T] for T ∈ {10^2, 10^3, 10^4} - Grid spacing: Δt ≈ 2π/log(N) (Nyquist-like resolution) - Number of t points: 1000-10000 ### 3.3 Numerical Precision Requirements
- **Default precision:** float64 (53-bit mantissa, ~15 decimal digits)
- **Summation algorithm:** Kahan compensated or pairwise (NOT naive)
- **Validation:** For N ≤ 10^4, compare against mpmath with 30+ decimal places
- **Required agreement:** Relative error < 10^-12
- **Documentation:** Must record summation method in metadata **Example validation:**
```
N=100, t=50.0: float64 (Kahan): -0.269137043469080 + 0.253932479941561i mpmath (30 dec): -0.269137043469077 + 0.253932479941569i Relative error: 2.36e-14 ✓ PASS (< 10^-12)
``` --- ## 4. METRICS (Computed from D_F Time Series) ### 4.1 Single-Scale Metrics For each function F and parameter pair (N, T): **(A) Maximum magnitude**
```
M_F = max_{t∈[T,2T]} |D_F(t; N)|
``` **(B) Mean square**
```
V_F = (1/T) ∫_T^(2T) |D_F(t; N)|² dt
``` **(C) Kurtosis** (critical for heavy tail detection)
```
K_F = E[|D_F|⁴] / (E[|D_F|²])² = [(1/T) ∫ |D_F|⁴ dt] / [(1/T) ∫ |D_F|² dt]²
```
- Near-Gaussian: K ≈ 3
- Heavy tails: K >> 3
- Expected: K_ζ ≈ 3-4, K_DH >> 3 **(D) Resonance Score**
```
RS(F) = M_F / √V_F
```
- Dimensionless measure of peak-to-RMS ratio
- Expected: RS(L_DH) >> RS(ζ) **(E) Tail probability**
```
P_F(λ) = (1/T) · measure{t ∈ [T,2T] : |D_F(t)| > λ√V_F}
```
Computed for λ ∈ {2, 3, 4, 5} **(F) Peak spacing distribution**
- Extract local maxima exceeding threshold (e.g., 2√V_F)
- Compute gaps between consecutive peaks
- Compare to: - GUE spacing (expected for ζ): level repulsion - Clustered spacing (expected for L_DH near zeros) ### 4.2 Multi-Scale Metrics **CRITICAL:** Single-scale metrics alone can produce false positives because ζ exhibits extreme peaks via log-correlated fields that can mimic power laws over finite ranges. **(G) Scaling exponent with model selection** For each function F, compute M_F(N) at multiple N values and fit TWO competing models: 1. **Power law (structural resonance):** ``` M_F(N) ∼ C · N^α_F ``` 2. **Log-correlated (extreme fluctuation):** ``` M_F(N) ∼ C · exp(c√(log N)) ``` Use AIC/BIC to select best-fitting model. **Expected outcomes:**
- ζ: log-correlated model wins (α ≈ 0)
- L_DH: power-law model wins (α ≈ 0.31 at t=85.7) **Key discriminator:** Model selection, not just exponent fit. **(H) Persistence** For a peak at height t*, define:
```
Pers_F(t*; N₁, N₂) = |D_F(t*; N₂)| / |D_F(t*; N₁)|, N₂ > N₁
``` Test pairs: (N₁, N₂) = (10^4, 10^5), (10^5, 10^6) **Expected behavior:**
- L_DH at t* ≈ 85.7: Pers ∼ (N₂/N₁)^0.31 (growing)
- ζ at any peak: Pers ≈ O(1) (no systematic growth) **(I) Cross-scale coherence (with baseline)** ```
X_F(t; N₁, N₂) = D_F(t; N₁) · conj(D_F(t; N₂)) / √(V_F(N₁)·V_F(N₂))
``` **CRITICAL:** Must compare to random baseline! Generate 1000+ samples of:
```
D_rand(N) = Σ_{p≤N} (a_p/√p) · X_p, X_p ~ Uniform(S¹) i.i.d.
``` Compute E[|X_rand|] and report **excess coherence:**
```
ΔX_F(t) = |X_F(t; N₁, N₂)| - E[|X_rand(N₁, N₂)|]
``` **Expected behavior:**
- L_DH near off-line zeros: ΔX_DH >> 0 (structural coherence)
- ζ: ΔX_ζ ≈ 0 (matches random baseline) --- ## 5. DATA STRUCTURES AND STORAGE ### 5.1 Coefficient Arrays | Function | Data Type | Size (N=10^6) | Description |
|----------|-------------|---------------|-------------|
| ζ | float64 | 8 MB | All ones (can skip storage) |
| χ₄ | int8 | 1 MB | Values in {-1, 0, 1} |
| L_DH | complex128 | 16 MB | Complex coefficients |
| f_rand | int8 (dict) | ~0.1 MB | Prime values only + factorization | ### 5.2 Prime Lists | Bound | Count | Storage | Usage |
|-------|--------|---------|-------|
| 10^4 | 1,229 | ~10 KB | Small-scale tests |
| 10^5 | 9,592 | ~77 KB | Medium-scale |
| 10^6 | 78,498 | ~0.6 MB | Production | Generated via sympy.primerange() or Sieve of Eratosthenes. ### 5.3 Time Series Output For each (Function, N, T) combination: ```python
{ 'metadata': { 'function': 'zeta' | 'chi4' | 'frand' | 'DH' | 'DHeps', 'N': int, 'T_min': float, 'T_max': float, 'num_t': int, 'summation_method': 'kahan' | 'pairwise', 'precision': 'float64', 'random_seed': int (for f_rand only), 'git_commit': str, 'timestamp': ISO8601, 'validation_status': 'pass' | 'fail', }, 'time_series': { 't_values': ndarray[num_t, float64], 'D_F_values': ndarray[num_t, complex128], }, 'metrics': { 'M_F': float, 'V_F': float, 'K_F': float, 'RS_F': float, 'tail_probs': {2: float, 3: float, 4: float, 5: float}, }, 'peaks': { 'peak_locations': list[float], 'peak_magnitudes': list[float], }
}
``` ### 5.4 File Formats and Naming **Time series:**
- Format: Parquet (.parquet) or HDF5 (.h5)
- Naming: `{function}_N{N}_T{Tmin}_{Tmax}_n{num_t}.parquet`
- Example: `zeta_N100000_T1000_2000_n5000.parquet` **Metadata:**
- Format: JSON (.json)
- Naming: Same as time series with `.json` extension **Summary tables:**
- Format: CSV or Parquet
- Content: All metrics for all (F, N, T) combinations
- Columns: function, N, T_min, T_max, M_F, V_F, K_F, RS_F, alpha_F, ... ### 5.5 Storage Estimates | Component | Size |
|-----------|------|
| Coefficients (6 functions, N=10^6) | ~97 MB |
| Time series (10^4 t-points) | ~0.16 MB per dataset |
| Full parameter space (54 combinations) | ~5.4 GB |
| Metadata and summaries | ~10 MB |
| **Total** | **~5.5 GB** | --- ## 6. PARAMETER SPACE ### 6.1 Function Classes
1. ζ (Riemann zeta)
2. L(s, χ₄) (real character mod 5)
3. f_rand (random multiplicative)
4. L_DH (Davenport-Heilbronn)
5. L_DH^(-0.1) (perturbed)
6. L_DH^(0.1) (perturbed) **Total: 6 functions** ### 6.2 Truncation Lengths
- N ∈ {10^4, 10^5, 10^6} **Total: 3 scales** ### 6.3 Height Ranges
- T ∈ {10^2, 10^3, 10^4}
- Analysis window: [T, 2T] **Total: 3 ranges** ### 6.4 Total Combinations
6 functions × 3 N-scales × 3 T-ranges = **54 datasets** Plus multi-scale analyses (computing across N for fixed T) and coherence baselines (1000 random samples). --- ## 7. VALIDATION REQUIREMENTS (NON-NEGOTIABLE) ### 7.1 Mandatory Calibration (Track 0) The program **STOPS** if this validation fails: **Conditions:**
1. **Single-scale separation:** RS(L_DH) >> RS(ζ) and RS(L_DH) >> RS(χ₄)
2. **Heavy tails:** K_DH >> 3, while K_ζ and K_χ₄ are moderate
3. **Spacing:** Peak spacing of D_DH clusters near t ≈ 85.7, 114.2, 166.5, 176.7; D_ζ shows GUE-like spacing
4. **Multi-scale:** Scaling exponent α_DH > 0 (power law), while α_ζ ≈ 0 (log-correlated)
5. **Persistence:** Pers_DH(85.7; N₁, N₂) grows as (N₂/N₁)^0.31
6. **Multiplicativity test:** f_rand behaves like ζ, NOT like L_DH **Ground truth:** Known DH zeros with β - 1/2 ∈ {0.0744, 0.1508, 0.2243, 0.3085} ### 7.2 Numerical Precision Validation For N ≤ 10^4:
- Compute D_F(t; N) with float64 + Kahan summation
- Recompute same with mpmath at 30+ decimal places
- Require: Relative error < 10^-12 **Must pass before using results.** ### 7.3 Model Selection Validation For each function F:
- Fit both power-law and log-correlated models
- Compute AIC and BIC for each
- Report winning model **Expected outcomes:**
- ζ, χ₄, f_rand: log-correlated wins
- L_DH, L_DH^(ε): power-law wins **If pattern doesn't hold → something is wrong.** --- ## 8. ENVIRONMENT CONFIGURATION ### 8.1 Required Packages (MUST be installed) | Package | Version | Purpose |
|---------|---------|---------|
| numpy | ≥ 1.26 | Array operations, core numerics |
| scipy | ≥ 1.11 | Special functions |
| matplotlib | ≥ 3.7 | Visualization |
| mpmath | ≥ 1.3 | Arbitrary precision validation |
| sympy | ≥ 1.12 | Prime generation |
| pandas | ≥ 2.0 | Data organization | **Installation:**
```bash
pip install numpy scipy matplotlib mpmath sympy pandas
``` **All packages available in current environment:** ✓ VERIFIED ### 8.2 Optional Packages (For production) - **numba:** JIT compilation for speed
- **pyarrow:** Parquet file format support
- **h5py:** HDF5 file format support
- **cupy:** GPU acceleration (if CUDA available)
- **finufft:** Non-uniform FFT (if using FFT approach) ### 8.3 Hardware Requirements | Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 4 cores | 16+ cores |
| RAM | 16 GB | 32 GB |
| GPU | None | CUDA-capable with float64 |
| Storage | 10 GB | 20 GB (with safety margin) | **Runtime limit:** 5400 seconds (90 minutes) ### 8.4 Computational Complexity For one (F, N, T) combination:
- Operations: ~N × num_t × 10 FLOPS ≈ 10^11 FLOPS (N=10^6, num_t=10^4)
- Single CPU core (100 GFLOPS): ~1 second
- GPU (1 TFLOPS): ~0.1 second **Scaling:**
- N ≤ 10^5: CPU sufficient
- N = 10^6: GPU recommended --- ## 9. KNOWN ISSUES AND CHALLENGES ### 9.1 Numerical Precision (CRITICAL) **Problem:** Oscillatory sum with ~10^6 terms → catastrophic cancellation **Symptoms:**
- Naive float64 summation produces garbage for large N and t
- Results depend on summation order
- Spurious "resonances" that aren't real **Solution:**
- **MANDATORY:** Use Kahan compensated summation or pairwise reduction
- Never use naive sequential `sum()` or `+=` accumulation
- Validate against mpmath for small N **Detection:** If validation fails (error > 10^-12), summation is broken. ### 9.2 mpmath Performance **Problem:** mpmath is ~100-1000× slower than numpy **Solution:**
- Use mpmath ONLY for validation (N ≤ 10^4)
- Production runs use float64 + Kahan **DON'T:** Try to run N=10^6 with mpmath (will timeout) ### 9.3 GPU Float32 Precision **Problem:** Many GPUs have slow float64, fast float32 **Issue:** float32 has insufficient precision (24-bit mantissa ≈ 7 digits) **Solutions:**
1. Use GPU with good float64 support (Tesla, A100, etc.)
2. Implement mixed-precision: accumulate partial sums in float64 blocks
3. Use CPU if GPU doesn't support float64 **DON'T:** Use naive float32 - results will be wrong ### 9.4 Prime Factorization for f_rand **Problem:** Extending multiplicatively requires factorization of all n ≤ N **Naive approach:** Factor each n individually → O(N√N) operations **Optimized approach:**
1. Sieve to find primes p ≤ N
2. For each n, extract prime factorization via trial division
3. Cache factorizations
4. a_n = ∏_{p^e || n} a_p^e **For N=10^6:** Requires ~1 second preprocessing, saves hours in computation ### 9.5 Model Selection False Positives **Problem:** ζ has extreme peaks (log-correlated field) that can APPEAR to follow power law over finite N ranges **Example:** Fitting M_ζ(N) for N ∈ {10^4, 10^5} might give α ≈ 0.05 (spurious) **Solution:**
1. Always fit BOTH models (power law AND log-correlated)
2. Use AIC/BIC to select
3. Extend N range to 10^6 to disambiguate
4. Check residuals, not just R² **DON'T:** Conclude power law from single model fit ### 9.6 Cross-Scale Coherence Baseline **Problem:** Even random processes show X_rand ≠ 0 due to shared coefficients **Wrong conclusion:** "X_F = 0.3 is significant" (might not be!) **Solution:**
- Generate random baseline: D_rand(N) = Σ (a_p/√p) X_p, X_p ~ Uniform(S¹)
- Compute 1000 samples, estimate E[|X_rand|]
- Report excess: ΔX_F = |X_F| - E[|X_rand|] **Interpretation:**
- ΔX_F ≈ 0: matches random (no structure)
- ΔX_F >> 0: structural coherence --- ## 10. EXPECTED STATISTICAL PROPERTIES ### 10.1 Riemann Zeta ζ(s) **Theory basis:** Selberg CLT, GMC, GUE conjecture | Metric | Expected Value | Source |
|--------|---------------|--------|
| V_ζ | ~log(N) | Probabilistic number theory |
| M_ζ | ~exp(c√(log N)) | Log-correlated field / GMC |
| K_ζ | 3-4 | Near-Gaussian with heavy tails |
| RS_ζ | ~exp(c'/√(log log N)) | Soundararajan resonance method |
| α_ζ | 0 (model: log-corr.) | No power-law growth |
| Spacing| GUE | Montgomery pair correlation | **Key property:** Multiplicative structure → phase decorrelation → no systematic resonance ### 10.2 L(s, χ₄) (Real Character) **Similar to ζ but with modifications:**
- Same qualitative behavior (GRH expected)
- Different constants due to character oscillations
- RS(χ₄) ≈ RS(ζ), K(χ₄) ≈ K(ζ) ### 10.3 Random Multiplicative f_rand **CRITICAL TEST:**
- **If behaves like ζ:** Multiplicativity suppresses resonance (supports hypothesis)
- **If behaves like L_DH:** Multiplicativity insufficient (refutes hypothesis) **Expected (hypothesis):** Matches ζ in all metrics **Reason:** Multiplicative extension forces coefficient correlations that prevent phase alignment, even without specific arithmetic of primes ### 10.4 Davenport-Heilbronn L_DH **Known behavior (proven zeros off critical line):** | Metric | Expected Value | Evidence |
|--------|---------------|----------|
| V_DH | Anomalies at t ≈ 85.7, 114.2, ... | Off-line zeros |
| M_DH | >> M_ζ at specific t | Proven zeros |
| K_DH | >> 3 | Very heavy tails |
| RS_DH | >> RS_ζ | Strong resonance |
| α_DH | 0.31 at t=85.7 | β - 1/2 = 0.3085 |
| Persistence | Grows as (N₂/N₁)^0.31 | Power law from zero |
| Spacing | Clustered near zeros | Structural correlation |
| ΔX_DH | >> 0 at t ≈ 85.7 | Coherent phase alignment | **Mechanism:** Non-multiplicative coefficients allow hidden correlations → phase alignment → peaks → off-line zeros --- ## 11. DATA ORGANIZATION AND REPRODUCIBILITY ### 11.1 Directory Structure (Recommended) ```
project/
├── data/
│ ├── coefficients/
│ │ ├── zeta_N1000000.npy
│ │ ├── chi4_N1000000.npy
│ │ ├── DH_N1000000.npy
│ │ └── frand_seed42_N1000000.pkl
│ ├── time_series/
│ │ ├── zeta_N100000_T1000_2000_n5000.parquet
│ │ ├── DH_N100000_T1000_2000_n5000.parquet
│ │ └── ...
│ ├── metrics/
│ │ └── summary_all.csv
│ └── validation/
│ ├── mpmath_validation_N10000.json
│ └── model_selection.csv
├── code/
│ ├── generate_coefficients.py
│ ├── compute_D_F.py
│ ├── extract_metrics.py
│ └── validate.py
├── results/
│ ├── figures/
│ └── tables/
└── docs/ ├── DATASET_DESCRIPTION.md (this file) └── metadata_schema.json
``` ### 11.2 Metadata Schema (REQUIRED for each dataset) Every output file MUST include: ```json
{ "function_name": "zeta|chi4|frand|DH|DHeps", "N": 100000, "T_min": 1000.0, "T_max": 2000.0, "num_t": 5000, "delta_t": 0.4548, "summation_method": "kahan", "precision": "float64", "random_seed": 42, "git_commit": "abc123def456", "timestamp": "2026-03-15T10:30:00Z", "hardware": "Intel i9-12900K / NVIDIA A100", "validation": { "method": "mpmath_30digits", "N_validated": 10000, "max_relative_error": 2.36e-14, "status": "PASS" }, "dependencies": { "numpy": "1.26.4", "scipy": "1.11.0", "mpmath": "1.3.0", "sympy": "1.12.0" }
}
``` ### 11.3 Reproducibility Checklist For every computation, record: - [ ] Function name and parameters (N, T, num_t)
- [ ] Random seed (for f_rand)
- [ ] Summation method (kahan/pairwise/naive)
- [ ] Precision (float32/float64/float128)
- [ ] Git commit hash
- [ ] Timestamp
- [ ] Hardware specification
- [ ] Package versions
- [ ] Validation status (pass/fail)
- [ ] Maximum observed error vs. mpmath **If any missing → results not reproducible** --- ## 12. QUICK START FOR FUTURE ANALYSES ### 12.1 Generate Coefficients
```python
import numpy as np
import sympy # Primes up to N
N = 100000
primes = list(sympy.primerange(1, N)) # ζ: trivial
a_zeta = np.ones(N+1, dtype=float) # χ₄: real character mod 5
chi4_table = {0: 0, 1: 1, 2: -1, 3: -1, 4: 1}
a_chi4 = np.array([chi4_table[n % 5] for n in range(N+1)], dtype=int) # L_DH: complex coefficients
kappa = (np.sqrt(5) - 1) / (2 * np.sqrt(5 * (np.sqrt(5) - 1)))
chi_table = {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}
a_DH = np.array([ ((1 - 1j*kappa)/2) * chi_table[n % 5] + ((1 + 1j*kappa)/2) * np.conj(chi_table[n % 5]) for n in range(N+1)
], dtype=complex) # f_rand: random multiplicative (need factorization)
# [See full implementation in code]
``` ### 12.2 Compute D_F(t; N) with Kahan Summation
```python
def kahan_sum_complex(values): s = 0.0 + 0.0j c = 0.0 + 0.0j for val in values: y = val - c t = s + y c = (t - s) - y s = t return s def compute_D_F(a_coeffs, t, N): terms = [ a_coeffs[n] * n**(-0.5) * np.exp(-1j * t * np.log(n)) for n in range(1, N+1) ] return kahan_sum_complex(terms)
``` ### 12.3 Extract Metrics
```python
# Compute D_F on grid
t_grid = np.linspace(T_min, T_max, num_t)
D_F_values = np.array([compute_D_F(a_coeffs, t, N) for t in t_grid]) # Metrics
M_F = np.max(np.abs(D_F_values))
V_F = np.mean(np.abs(D_F_values)**2)
K_F = np.mean(np.abs(D_F_values)**4) / V_F**2
RS_F = M_F / np.sqrt(V_F) # Tail probabilities
for lam in [2, 3, 4, 5]: P_F = np.mean(np.abs(D_F_values) > lam * np.sqrt(V_F)) print(f"P_F({lam}) = {P_F:.4f}")
``` ### 12.4 Validate Against mpmath
```python
import mpmath
mpmath.mp.dps = 30 def compute_D_F_mpmath(a_coeffs, t, N): result = mpmath.mpc(0, 0) for n in range(1, N+1): result += a_coeffs[n] * mpmath.power(n, mpmath.mpc(-0.5, -t)) return complex(result) # Compare
D_float = compute_D_F(a_coeffs, t, N)
D_mpmath = compute_D_F_mpmath(a_coeffs, t, N)
rel_error = abs(D_float - D_mpmath) / abs(D_mpmath) assert rel_error < 1e-12, f"Validation failed: {rel_error:.2e}"
print("✓ Validation passed")
``` ### 12.5 Mandatory Calibration Test
```python
# Compute D_DH at known zero location
t_zero = 85.7
N_scales = [10**3, 10**4, 10**5, 10**6]
magnitudes = [ abs(compute_D_F(a_DH, t_zero, N)) for N in N_scales
] # Fit log-log slope
coeffs = np.polyfit(np.log(N_scales), np.log(magnitudes), 1)
alpha_measured = coeffs[0] print(f"Expected α ≈ 0.31, measured α = {alpha_measured:.3f}")
assert abs(alpha_measured - 0.31) < 0.05, "Calibration failed!"
print("✓ Calibration passed")
``` --- ## 13. REFERENCES AND SOURCES ### 13.1 Primary Literature **Davenport-Heilbronn Function:**
- H. Davenport & H. Heilbronn (1936): "On the zeros of certain Dirichlet series, I and II", J. London Math. Soc. 11, 181-185 and 307-312
- R. Spira (1994): "Zeros of sections of the zeta function, II", Math. Comp. 63, 747-748
- E.P. Balanzario & J. Sánchez-Ortiz (2007): "Zeros of the Davenport–Heilbronn counterexample", Math. Comp. 76, 2045-2049 **Analytic Theory:**
- L. Guth & J. Maynard (2024): "New large value estimates for Dirichlet polynomials", arXiv:2405.20552
- K. Soundararajan (2008): "Extreme values of zeta and L-functions", Math. Ann. 342, 467-486 **Random Matrix Theory:**
- H.L. Montgomery (1973): "The pair correlation of zeros of the zeta function", Analytic Number Theory (Proc. Sympos. Pure Math., Vol. XXIV)
- J.P. Keating & N.C. Snaith (2000): "Random matrix theory and ζ(1/2+it)", Comm. Math. Phys. 214, 57-89 **Log-Correlated Fields:**
- Y.V. Fyodorov, G.A. Hiary, & J.P. Keating (2012): "Freezing transition, characteristic polynomials of random matrices, and the Riemann zeta function", Phys. Rev. Lett. 108, 170601 ### 13.2 Data Sources **All data is GENERATED, not external:**
- Primes: sympy.primerange() (deterministic)
- Characters: Mathematical definition (mod 5)
- DH zeros: Literature values (Spira 1994, Balanzario-Sánchez-Ortiz 2007)
- Random functions: Pseudorandom with recorded seed **No datasets to download. Everything is computed from first principles.** --- ## SUMMARY **Dataset nature:** Entirely computationally generated **No external data:** All constructed from mathematical definitions **Size:** ~5.5 GB for full parameter space **Key challenge:** Numerical precision in oscillatory sums **Critical requirement:** Kahan summation (mandatory) **Validation target:** Davenport-Heilbronn (non-negotiable) **Research question:** Does multiplicativity suppress resonance? **Primary output:** Metrics distinguishing 4 function classes:
1. ζ (multiplicative, Euler product) → RH expected
2. χ₄ (multiplicative, Euler product) → GRH expected
3. f_rand (multiplicative, no Euler product) → Test case
4. L_DH (non-multiplicative) → Proven off-line zeros **Success criterion:** Clear separation between (1-3) and (4) in multi-scale metrics --- **End of Dataset Description**
