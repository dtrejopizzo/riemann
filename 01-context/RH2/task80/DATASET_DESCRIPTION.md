
# Research Dataset Description ## Overview
This dataset consists of results from previous research investigating resonance suppression in arithmetic L-functions and the Riemann Hypothesis, along with three published papers derived from that research. The research focuses on a computational and statistical approach to understanding whether the Riemann Hypothesis can be understood through resonance suppression in multiplicative arithmetic structures. ## Files ### 1. paper1.pdf (1,339,199 bytes)
**Title:** "Absence of Power-Law Growth in Partial Sums of the Davenport–Heilbronn Function at Off-Line Zeros" **Key Content:**
- Tests the prediction that off-line zeros produce power-law growth |D_DH(γ₀;N)| ~ N^(β₀-1/2)
- Uses Kahan-compensated partial sums over five decades of N (10⁴ to 10⁹)
- **Main finding:** Fitted growth exponent α = 0.000440 ± 0.000453 (statistically ~zero), vs predicted α = 0.3085
- Tests 4 known off-line zeros: (0.8085, 85.7), (0.6508, 114.16), (0.5744, 166.48), (0.7243, 176.70)
- **Phase analysis:** DH resonances are composite-driven with uniform prime phases (not prime-driven like ζ)
- 19 pages, 8 sections + 2 appendices **Key Numerical Results:**
- N range: 10⁴ to 10⁹
- Median relative error: 2.95×10⁻¹⁴
- Coefficient of variation at first zero: 0.52%
- Destructive interference: 78.4% magnitude reduction **Computational Notebooks Referenced:** task1, task4, task5, task6, task8, task10, task11, task14, task15, task20, task25, task26 ### 2. paper2.pdf (2,660,154 bytes)
**Title:** "Metric-Space Classification of L-Functions by Resonance Phenotype and Coefficient Organization" **Key Content:**
- Introduces metric-space approach using three features: composite coherence (R_comp), coherence magnitude (M_coh), CAS
- Tests 7 function classes: ζ, L(χ₄) mod5, L(χ₄) mod4, f_rand, L_DH, L(s,λ), f_fully_rand
- **Perfect classification:** Linear SVM achieves 100% accuracy on 350 peaks across 7 classes
- Shannon entropy uniquely identifies ζ (H = 0.000 bits)
- 20 pages, 8 sections + 2 appendices **Key Metrics Defined:**
- **R_comp (Composite coherence):** Mean resultant length of ω-class phases (k≥2)
- **M_coh (Coherence magnitude):** Ratio of Pythagorean norm to vector sum magnitude
- **CAS (Coefficient Autocorrelation Score):** log₁₀(max FFT power / mean FFT power)
- **Shannon entropy (H):** -Σ p_a log₂(p_a) over coefficient values **Key Findings:**
- ζ: R_comp = 0.0020±0.0013, M_coh = 0.5269±0.0417, H = 0.000
- L_DH: R_comp = 0.0132±0.0031, M_coh = 0.5464±0.0523, H = 0.999936
- L(s,λ) (Liouville): R_comp = 0.822 at peak (highest coherence), fully multiplicative but anomalous
- Effect sizes d > 4 for R_comp separation (ζ vs L_DH)
- p-values < 10⁻¹⁸ for cluster separation **Computational Parameters:**
- N = 10⁵ terms
- t ∈ [1000, 10000]
- Top 50 resonance peaks per function
- FFT on first N₀ = 10000 nonzero coefficients **Computational Notebooks Referenced:** task51, task55, task60, task64, task68, task73, task75, task80, task82, task85, task88 ### 3. paper3.pdf (1,313,561 bytes)
**Title:** "Not a Proof of the Riemann Hypothesis: A Physical Approach to Resonance Suppression in Arithmetic L-Functions" **Key Content:**
- Physical/experimental framework treating Dirichlet series as oscillatory signals
- Uses Generalized Extreme Value (GEV) distribution for extreme-value statistics
- Tests "multiplicativity illusion" - shows that multiplicativity ≠ resonance suppression
- Liouville function L(s,λ) demonstrates constructive interference despite full multiplicativity
- 25 pages (first 10 pages extracted) **Key Statistical Framework:**
- **GEV shape parameter ξ:** - ξ > 0 (Fréchet): heavy-tailed - ξ = 0 (Gumbel): exponentially decaying - ξ < 0 (Weibull): bounded upper tail
- ζ exhibits ξ ≈ -0.17 (Weibull, strongest suppression)
- Non-stationarity: ξ evolves with height t **Function Classes (7 total):**
- F1: ζ(s) - fully multiplicative, a_n = 1
- F2: L(s,χ₄) - real Dirichlet L-function
- F3: f_rand - random multiplicative
- F4: L_DH - Davenport-Heilbronn (non-multiplicative, off-line zeros)
- F5: L_DH^(ε) - perturbed DH family
- F6: L(s,λ) - Liouville (fully multiplicative, λ(n) = (-1)^Ω(n))
- F7: L(s,μ) - Möbius (multiplicative) **Davenport-Heilbronn Definition:**
- Character χ mod 5: χ(1)=1, χ(2)=i, χ(3)=-i, χ(4)=-1, χ(0)=0
- κ = (√5-1)/(2√(5√(5-1)))
- L_DH(s) = ((1-iκ)/2)·L(s,χ) + ((1+iκ)/2)·L(s,χ̄)
- Coefficients are complex and NOT multiplicative ### 4. resultado_Resonance_Detection_and_Class_Separation_in_Arithm.pdf (7,108,871 bytes)
**Title:** Discovery report for Resonance Detection and Class Separation in Arithmetic L-Functions **Structure:**
- Research Objective (detailed prompt)
- Dataset Description
- Summary of Discoveries (4 major discoveries)
- Detailed discovery reports with figures
- task sources (references to computational runs) **Four Main Discoveries:** **Discovery 1:** "Calibration of a Compensated-Sum Resonance Detector Refutes Power-Law Growth at Davenport-Heilbronn Zeros"
- Validates Kahan compensated summation
- Tests N ∈ {10⁴, 10⁵, 10⁶, 10⁷, 10⁸, 10⁹}
- Fitted α = 0.000440 ± 0.000453 vs predicted α = 0.3085
- Random multiplicative model shows strongest heavy tails (K ≈ 9.4, RS ≈ 4.9) **Discovery 2:** "Phase-Resolved Mechanisms of Resonance: Composite-Driven Coherence and Universal Inter-Class Destructive Interference"
- ζ: prime-driven resonance, 65% of peaks show p < 0.05 for prime-phase non-uniformity
- L_DH: composite-driven, 0/20 peaks significant for prime phases
- Universal M < 1 across all functions (destructive interference)
- At L_DH zero: 78.4% magnitude reduction from inter-class cancellation **Discovery 3:** "Metric-Space Classification of L-Functions by Resonance Phenotype and Coefficient Organization"
- 2D (M_coh, R_comp) separation with p < 10⁻¹⁸
- 3D perfect separability with CAS
- Shannon entropy provides unique ζ fingerprint **Discovery 4:** "Intrinsic Constructive Interference in Multiplicative Anomalies Challenges Suppression-by-Multiplicativity"
- L(s,λ) and L(s,μ) show intrinsic constructive interference
- Alignment ratio R = 0.822 for L(s,λ) at t* = 7563.5
- Sign pattern creates coherence, not destroys it **Referenced Trajectories:**
- r1: Numerical validation
- r3: Resonance detection analysis
- r4: Peak magnitude scaling
- r6: Prime phase analysis
- r8: Cross-scale coherence
- r11: DH growth analysis at zeros
- r14, r25, r26, r51, r54: Various phase and coherence analyses ## Key Computational Framework ### Resonance Detector
**Definition:** D_F(t;N) = Σ_{n≤N} a_n(F) / n^(1/2+it) **Numerical Implementation:**
- **Method:** Kahan compensated summation (essential, not optional)
- **Validation:** Against 30-digit arbitrary precision (mpmath)
- **Precision:** Median relative error 2.95×10⁻¹⁴
- **Test suite:** 360 test cases across 6 N values × 12 t values × 5 functions ### Parameter Ranges
- **N (truncation):** 10⁴, 10⁵, 10⁶, 10⁷, 10⁸, 10⁹
- **t (ordinate):** [100, 20000] typical, finer ranges for specific tests
- **Δt (spacing):** 2π/log(N) for peak resolution
- **Blocks for GEV:** 500 blocks typical
- **Number of peaks:** Top 20-50 per function ### Function Coefficient Structures | Function | Multiplicative | Periodicity | Entropy H (bits) | Key Property |
|----------|---------------|-------------|-----------------|--------------|
| ζ | Yes (fully) | None | 0.000000 | a_n = 1 ∀n |
| L(χ₄) mod5 | Yes | Period 5 | 1.521928 | Dirichlet character |
| L(χ₄) mod4 | Yes | Period 4 | 1.521928 | Dirichlet character |
| f_rand | Yes | None | 0.999995 | Random on primes |
| L_DH | NO | Period 5 | 0.999936 | Complex coefficients |
| L(s,λ) | Yes (fully) | None | 0.999936 | λ(n) = (-1)^Ω(n) |
| L(s,μ) | Yes | None | 1.574182 | Möbius function |
| f_fully_rand | NO | None | 0.999995 | i.i.d. random | ### Known Off-Line Zeros (DH function)
Validation threshold: |L_DH(ρ)| < 10⁻⁶ | Zero | σ (real part) | t (imaginary) | Predicted α |
|------|--------------|---------------|-------------|
| ρ₁ | 0.8085 | 85.70 | 0.3085 |
| ρ₂ | 0.6508 | 114.16 | 0.1508 |
| ρ₃ | 0.5744 | 166.48 | 0.0744 |
| ρ₄ | 0.7243 | 176.70 | 0.2243 | ## Statistical Metrics Dictionary ### Single-Scale Metrics
1. **Maximum magnitude M_F:** max_t |D_F(t;N)|
2. **Mean square V_F:** (1/T) ∫ |D_F(t;N)|² dt
3. **Kurtosis K_F:** E[|D_F|⁴] / (E[|D_F|²])²
4. **Resonance Score RS(F):** M_F / √V_F
5. **Tail probabilities:** P_F(λ) for λ = 2,3,4,5 ### Multi-Scale Metrics
1. **Scaling exponent α:** From M_F(N) ~ C·N^α
2. **Model selection:** AIC/BIC for power-law vs log-correlated
3. **Persistence:** Pers(t*; N₁, N₂) = |D_F(t*;N₂)| / |D_F(t*;N₁)|
4. **Cross-scale coherence:** X_F(t; N₁, N₂) ### Phase-Resolved Metrics
1. **Prime-phase Rayleigh statistic:** R(t) = (1/π(N))|Σ_p exp(iθ_p(t))| - θ_p(t) = -t·log(p) + arg(a_p)
2. **Composite coherence R_comp:** Mean resultant length of ω-class phases (k≥2)
3. **Cancellation metric M_coh:** Reciprocal of vector alignment
4. **ω-class decomposition:** S_k(t;N) = Σ_{ω(n)=k} a_n / n^(1/2+it) ### Coefficient Metrics
1. **CAS (Coefficient Autocorrelation Score):** log₁₀(max FFT power / mean power)
2. **Shannon entropy H:** -Σ p_a log₂(p_a)
3. **Sum squared ACF:** Σ_d (autocorrelation at lag d)² ### GEV Statistics
1. **Shape parameter ξ:** Determines tail behavior - ξ < 0: Weibull (bounded) - ξ = 0: Gumbel (exponential decay) - ξ > 0: Fréchet (heavy-tailed)
2. **Location μ, Scale σ**
3. **Confidence intervals:** Via 5000 bootstrap replicates ## Key Empirical Findings ### Cluster Centers (2D Classification)
From paper 2, N=10⁵, top 50 peaks: | Function | M_coh | R_comp | Separation |
|----------|-------|--------|------------|
| ζ | 0.5269±0.0417 | 0.0020±0.0013 | p < 10⁻¹⁸ vs L_DH |
| L(χ₄) | 0.5901±0.0851 | 0.0030±0.0015 | Effect size d=4.18 |
| f_rand | 0.6002±0.1195 | 0.0119±0.0078 | High variance |
| L_DH | 0.5464±0.0523 | 0.0132±0.0031 | Anomalous cluster | ### CAS Values
| Function | CAS | Interpretation |
|----------|-----|----------------|
| L(χ₄) mod5 | 3.47 | Strong periodicity |
| L_DH | 3.57 | Inherited period-5 |
| L(χ₄) mod4 | 2.75 | Period-4 structure |
| f_rand | 1.01 | No structure |
| f_fully_rand | 0.96 | No structure |
| ζ | ≈ 0 | DC only | ### Phase Coherence at Peaks
**ζ at t=57.50 (N=10⁶):**
- Prime R = 0.0150, p = 2.19×10⁻⁸
- 65% of top 20 peaks: p < 0.05
- 50% of top 20 peaks: p < 0.001 **L_DH at t=84.2 (near first zero, N=10⁶):**
- Prime R = 0.0021, p = 0.70 (uniform)
- 0/20 peaks significant
- All-terms R = 0.099, p < 10⁻¹⁵
- Composite k=2: R = 0.0426, p < 0.001
- Composite k=3: R = 0.1015, p < 0.001
- Composite k=4: R = 0.1762, p < 0.001 **L(s,λ) at t*=7563.5 (N=10⁵):**
- |D_λ(t*;N)| = 46.88
- Signed vectors R = 0.822 (82.2% alignment)
- Unsigned vectors R = 0.070 (random)
- Phase std of signed vectors: 40.4° ### Universal Features
1. **All functions:** M_coh < 1 (universal destructive interference)
2. **Multiplicative functions:** Prefer log-correlated growth model
3. **DH zero cancellation:** 78.4% magnitude reduction from inter-class interference ## Environment Configuration ### Required Packages
**Core:**
- numpy (array operations, FFT)
- scipy (stats, GEV fitting, statistical tests)
- mpmath (arbitrary precision validation)
- matplotlib (visualization)
- sklearn (SVM classification) **Specific methods:**
- scipy.stats.genextreme (GEV fitting)
- scipy.stats.rayleigh (Rayleigh test)
- sklearn.svm.LinearSVC (classification)
- Kahan summation (custom implementation required) ### Known Numerical Challenges
1. **Catastrophic cancellation:** D_F sums involve ~N oscillatory terms - **Solution:** MUST use Kahan compensated summation - **Impact:** Without compensation, errors ~10⁻⁴ to 10⁻² at N=10⁵ 2. **Precision requirements:** - Float64 with Kahan: sufficient for t ≤ 500 - Errors increase for t > 500 (rapid oscillation) - Validation threshold: ε_rel < 10⁻¹⁰ 3. **Peak resolution:** - Grid spacing: Δt ≈ 2π/log(N) - Minimum peak separation: ≥ 5 in t 4. **GEV fitting:** - Requires ≥ 100 blocks for stable estimation - Bootstrap: 5000 replicates for 95% CI - Sensitive to block size choice 5. **FFT for CAS:** - Remove DC component before FFT - N₀ = 10000 coefficients typical - Periodic functions: clear spectral peaks ## Data Provenance Issues ### DH Implementation Crisis
**Problem:** At least 3 incompatible L_DH implementations exist
- Different κ definitions
- Different character branches
- Different normalization conventions **Validation Protocol (from paper2):**
1. Compute |L_DH(ρ)| at all 4 known zeros
2. ALL must satisfy |L_DH(ρ)| < 10⁻⁶
3. Only "historical reconstruction" passes
4. Canonical failed: residuals ≈ 24×10⁻² **Robust metric:** CAS remains consistent across implementations (~3.5-3.6) ## Reproducibility Notes ### Computational Notebooks Structure
Papers reference numbered tasks (e.g., task1, task4, task11, etc.) **Paper 1 notebooks:**
- task1, task4, task5, task6, task8, task10, task11, task14, task15, task20, task25, task26 **Paper 2 notebooks:**
- task51, task55, task60, task64, task68, task73, task75, task80, task82, task85, task88 **Critical tasks:**
- task1: Numerical validation
- task11: Killer signature test at DH zeros
- task68: DH data-provenance crisis
- task73: Historical DH reconstruction
- task75: SVM classification ### Deterministic Requirements
1. **Random seed:** seed=42 for f_rand construction
2. **Prime generation:** Sieve of Eratosthenes up to N
3. **Character values:** Lookup table (period 5 or 4)
4. **Peak detection:** Minimum separation = 5, top 20-50 ### Validation Checklist
✓ Kahan summation implemented
✓ 360-test validation suite passes (ε_rel < 10⁻¹⁰)
✓ L_DH at 4 zeros: all |L_DH| < 10⁻⁶
✓ λ(n) multiplicativity: 1000 random pairs
✓ μ(n) on squarefree integers ## Key Conceptual Insights ### What the Research Shows
1. **Power-law prediction fails:** No evidence for N^(β₀-1/2) growth at DH zeros up to N=10⁹
2. **Multiplicativity illusion:** L(s,λ) is fully multiplicative yet shows HIGHEST resonance coherence
3. **Operative discriminant:** Coefficient architecture (entropy, periodicity, sign complexity), not Euler product
4. **Universal destructive interference:** All functions show M_coh < 1
5. **Mechanism separation:** - ζ: prime-driven peaks with prime-phase bias - L_DH: composite-driven with uniform primes, location-dependent composite coherence - L(s,λ): sign-organized constructive interference ### What This Enables
1. **Perfect classification:** 100% accuracy on 350 peaks, 7 function classes
2. **Robust to data issues:** Classification works despite DH implementation differences
3. **Phase-resolved understanding:** Separates prime vs composite contributions
4. **Statistical rigor:** p < 10⁻¹⁸ separations, effect sizes d > 4 ### Limitations
1. **Pre-asymptotic regime:** Results hold for N ≤ 10⁹, asymptotic onset may be beyond
2. **Height dependence:** ξ(t) is non-stationary, classification may degrade at very large t
3. **Function diversity:** Only 7-9 classes tested, exotic L-functions may challenge framework
4. **Not a proof:** Computational results, not analytical theorems ## Future Analysis Guidance ### What to Avoid
1. ❌ Naive summation (always use Kahan)
2. ❌ Single-N metrics without N-dependence
3. ❌ Trusting DH implementation without zero-validation
4. ❌ Assuming multiplicativity implies suppression
5. ❌ Continuing after validation failure
6. ❌ Confusing computation with proof ### What to Do
1. ✓ Validate all implementations against mpmath
2. ✓ Check DH at all 4 zeros before proceeding
3. ✓ Report metrics across multiple N
4. ✓ Use model selection (AIC/BIC) for growth patterns
5. ✓ Phase-resolved analysis in addition to amplitudes
6. ✓ Test both multiplicative and non-multiplicative functions ### Analytical Targets
If extending this work analytically:
1. Prove: R_comp ≤ 1-ε ∀t, N≥N₀ ⟹ ξ ≤ 0
2. Prove: For a_n=1, R_comp ≤ 1-c/log N via class-vector non-alignment
3. Establish: Relationship δ→ε in Rayleigh bound ⟹ composite coherence bound
4. Quantify: N-dependence of GEV shape parameter ξ(N) ## Summary Statistics **Computational scale:**
- 360+ validation test cases
- 350-450 peaks analyzed across studies
- 7-9 function classes
- N up to 10⁹ (5 decades)
- t ranges [100, 20000]
- ~1000s of individual D_F evaluations **Key p-values:**
- Cluster separation: p < 10⁻¹⁸
- Prime-phase tests: 65% with p < 0.05 (ζ), 0% (L_DH)
- Composite coherence: p < 0.001 for k≥2 classes at DH zeros **Effect sizes:**
- Cohen's d > 4 for R_comp (ζ vs L_DH)
- Spearman ρ = -0.310 (M_coh vs R_comp in L_DH) **Classification accuracy:**
- 2D SVM: separates clusters with p < 10⁻¹⁸
- 3D SVM: 100% accuracy, perfect LOOCV
- Entropy-based: 100% accuracy for ζ identification
