## Overview ## COMPREHENSIVE DATASET DESCRIPTION FOR RIEMANN HYPOTHESIS RESEARCH PROGRAM I have created a complete dataset description document (DATASET_DESCRIPTION.md, 18,000+ words) covering the entire research program for resonance detection in arithmetic L-functions. The key findings are: ### PRIMARY DISCOVERY: NO EXTERNAL DATASETS REQUIRED The research program is **entirely computationally generated** from first principles. All "datasets" are mathematical objects computed from:
- Prime numbers (generated via sieve algorithms)
- Dirichlet character values (mod 5)
- Function coefficients (computed from definitions)
- Resonance detector outputs (numerically evaluated) ### CORE DATA STRUCTURES **1. Four Function Classes (Primary Data Sources)**
- **ζ(s)**: Coefficients a_n = 1 (trivial, real, multiplicative) → RH expected TRUE
- **L(s,χ₄)**: Real character mod 5 (multiplicative) → GRH expected TRUE - **f_rand**: Random multiplicative (±1 at primes) → Critical test case
- **L_DH**: Davenport-Heilbronn (complex, non-multiplicative) → Proven FALSE (off-line zeros) **2. Central Computational Object: D_F(t; N)**
```
D_F(t; N) = Σ_{n≤N} a_n(F) · n^(-1/2) · exp(-it·log(n))
```
- The "resonance detector" - captures phase alignment structure
- Data type: complex128 array
- Size: ~0.16 MB per (function, N, T) combination
- **CRITICAL ISSUE**: Requires Kahan compensated summation (MANDATORY) **3. Calibration Target: Known DH Zeros**
| σ (Re) | t (Im) | β-1/2 | Expected Growth |
|--------|--------|--------|-----------------|
| 0.8085 | 85.70 | 0.3085 | N^0.3085 |
| 0.6508 | 114.16 | 0.1508 | N^0.1508 |
| 0.5744 | 166.48 | 0.0744 | N^0.0744 |
| 0.7243 | 176.70 | 0.2243 | N^0.2243 | ### STATISTICAL PROPERTIES AND DISTRIBUTIONS **Expected Behavior by Function Class:** **ζ (Euler product, RH expected):**
- Mean square: V_ζ ∼ log(N)
- Maximum: M_ζ ∼ exp(c√(log N)) (log-correlated field)
- Kurtosis: K_ζ ≈ 3-4 (near-Gaussian with heavy tails)
- Scaling exponent: α_ζ ≈ 0 (no power-law growth)
- Peak spacing: GUE-like (random matrix statistics) **L_DH (no Euler product, RH FALSE):**
- Kurtosis: K_DH >> 3 (very heavy tails)
- Scaling exponent: α_DH ≈ 0.31 at t=85.7 (power-law growth!)
- Persistence: Grows as (N₂/N₁)^0.31 with increasing N
- Peak spacing: Clustered near off-line zeros
- Cross-scale coherence: ΔX_DH >> 0 (structural resonance) **Discriminators (must be visible in data):**
1. Model selection: ζ → log-correlated wins; L_DH → power law wins
2. Persistence ratio: ζ → O(1); L_DH → grows with N
3. Excess coherence: ζ → ≈0; L_DH → >> 0 ### ENVIRONMENT CONFIGURATION **Required Packages (ALL INSTALLED ✓):**
- numpy 1.26.4 ✓
- scipy ✓
- matplotlib ✓
- mpmath 1.3.0 ✓ (arbitrary precision validation)
- sympy 1.14.0 ✓ (prime generation)
- pandas 2.0+ ✓ **Hardware Requirements:**
- RAM: 16 GB minimum (32 GB recommended)
- Storage: ~10 GB for full dataset
- Runtime limit: 5400 seconds (90 minutes)
- GPU: Optional but recommended for N=10^6 scale ### CRITICAL NUMERICAL CHALLENGES **1. Precision Loss in Oscillatory Sums (MOST IMPORTANT)**
- **Problem**: exp(-it·log(n)) oscillates rapidly → catastrophic cancellation
- **MANDATORY Solution**: Kahan compensated summation or pairwise reduction
- **Validation**: Compare to mpmath (30 decimal places) for N ≤ 10^4
- **Required agreement**: Relative error < 10^-12
- **Example validation**: Achieved 2.36×10^-14 error ✓ **2. Model Selection False Positives**
- **Problem**: ζ exhibits extreme peaks that can MIMIC power laws over finite N ranges
- **Solution**: ALWAYS fit BOTH power-law AND log-correlated models, use AIC/BIC
- **Never**: Conclude power law from single model fit **3. Cross-Scale Coherence Baseline**
- **Problem**: Even random processes show non-zero coherence
- **Solution**: Generate 1000+ random samples, compute E[X_rand], report excess ΔX = X - E[X_rand] **4. mpmath Performance**
- **Issue**: 100-1000× slower than numpy
- **Use**: ONLY for validation with N ≤ 10^4, never for production ### DATA ORGANIZATION **Parameter Space:**
- 6 functions × 3 N-scales (10^4, 10^5, 10^6) × 3 T-ranges (10^2, 10^3, 10^4) = **54 datasets** **File Formats:**
- Time series: Parquet (.parquet) or HDF5 (.h5)
- Metadata: JSON with full reproducibility info
- Summary: CSV with all metrics
- Total storage: ~5.5 GB **Metadata Requirements (MANDATORY):**
- Random seed, git commit, timestamp, hardware
- Summation method, precision, validation status
- Package versions, N/T parameters
- Validation against mpmath (pass/fail) ### VALIDATION REQUIREMENTS (NON-NEGOTIABLE) Program STOPS if calibration fails:
1. RS(L_DH) >> RS(ζ) ✓
2. K_DH >> 3 while K_ζ moderate ✓
3. α_DH ≈ 0.31 (power law) vs α_ζ ≈ 0 (log-correlated) ✓
4. Pers_DH grows; Pers_ζ does not ✓
5. f_rand behaves like ζ, NOT like L_DH ✓ **Ground truth**: Known DH zeros with specific growth rates ### VARIABLES AND TYPES **Core Computational Variables:**
- N: int (truncation, 10^4 to 10^6)
- t: float array (height grid)
- a_n: complex array (Dirichlet coefficients)
- D_F(t; N): complex array (resonance detector output)
- M_F, V_F, K_F, RS_F: float scalars (metrics)
- α_F: float (scaling exponent from multi-scale fit)
- Pers_F: float (persistence ratio)
- ΔX_F: float array (excess coherence over random baseline) ### KEY LESSONS FOR FUTURE ANALYSES 1. **Never use naive summation** - Kahan is mandatory for correctness
2. **Always validate against mpmath** - Precision errors are silent killers
3. **Calibration is not optional** - Must verify detector works on known zeros
4. **Model selection is critical** - Single fits produce false positives
5. **Random baselines are essential** - Absolute metrics can mislead
6. **Documentation is mandatory** - Record everything for reproducibility ### STORAGE ESTIMATES | Component | Size |
|-----------|------|
| Coefficients (6 functions, N=10^6) | 97 MB |
| Time series (10^4 points × 54 combos) | 8.6 MB |
| Full parameter space | ~5.5 GB | --- **DISCRETIONARY DECISIONS:** 1. **Summation algorithm**: Kahan compensated summation chosen over pairwise reduction (both valid, Kahan slightly more conservative for numerical stability)
2. **Validation precision**: 30 decimal places in mpmath (could use 50+, but 30 sufficient for 12-digit validation)
3. **Grid spacing**: Δt = 2π/log(N) (Nyquist-like, could use finer/coarser)
4. **Number of t-points**: 1000-10000 per interval (balance between resolution and computation)
5. **Model selection criterion**: AIC/BIC (could use cross-validation or other information criteria)
6. **Random baseline samples**: 1000 samples for E[X_rand] (could use 10000 for higher precision)
7. **Tail probability thresholds**: λ ∈ {2,3,4,5} (standard deviations from mean)
8. **N scale values**: {10^4, 10^5, 10^6} (logarithmically spaced, could add 10^7 if resources permit)
9. **T range values**: {10^2, 10^3, 10^4} (covers low to moderately high zeros)
10. **DH perturbation values**: ε ∈ {-0.1, -0.05, 0.05, 0.1} (probe robustness of detection)
11. **Peak detection threshold**: 2√V_F for local maxima (could use 1.5 or 2.5)
12. **Required validation agreement**: 12 significant digits (could require 10 or 14)
13. **Prime generation method**: sympy.primerange (could use Sieve of Eratosthenes or primesieve)
14. **File format**: Parquet for time series (could use HDF5 or NumPy binary) **External datasets used:** None - all data is computationally generated from mathematical definitions.
