
# ω-CLASS GEOMETRY OF DIRICHLET POLYNOMIALS - DATASET DOCUMENTATION ## Overview
This dataset contains computationally generated data for mathematical research on the internal ω-class structure of Dirichlet partial sums. The data supports investigation of three research fronts:
- F1: Conditional anti-correlation at peaks
- F2: Moment decomposition by ω-classes - F3: Semiprime fragility mechanism ## Generated Files ### 1. dirichlet_polynomials_N10000_T10000-20000.pkl
**Description:** Dirichlet polynomial evaluations D_F(t; N) for multiple function classes
**Format:** Python pickle file (dictionary)
**Size:** ~0.38 MB
**Structure:**
```
{ 'metadata': { 'description': str, 'T_min': 10000, 'T_max': 20000, 'num_points': 2000, 'N': 10000, 'function_classes': ['zeta', 'L_DH', 'liouville', 'f_rand', 'f_fully_rand'], 'generation_date': str, 'seed': 42 }, 'data': { 'function_class_name': { 't_values': ndarray (2000,), # t values in [10000, 20000] 'D_F': ndarray (2000, complex), # D_F(t; N) evaluations 'modulus': ndarray (2000,), # |D_F(t; N)| 'argument': ndarray (2000,), # arg(D_F(t; N)) 'N': 10000 }, ... (5 function classes total) }
}
``` ### 2. dirichlet_summary_N10000.csv
**Description:** Summary statistics for each function class
**Format:** CSV
**Columns:**
- function_class: str - Name of the Dirichlet function
- num_points: int - Number of t values evaluated (2000)
- N: int - Truncation parameter (10000)
- mean_modulus: float - Mean of |D_F(t; N)|
- std_modulus: float - Standard deviation of |D_F(t; N)|
- max_modulus: float - Maximum of |D_F(t; N)|
- min_modulus: float - Minimum of |D_F(t; N)| **Key Statistics:**
- zeta: mean |ζ| = 1.88, max = 17.83
- L_DH: mean = 1.68, max = 9.99
- liouville: mean = 2.00, max = 30.68 (ANOMALOUS - note high peak)
- f_rand: mean = 2.33, max = 17.47
- f_fully_rand: mean = 2.74, max = 8.57 ### 3. zeta_peaks_N10000.pkl
**Description:** Peak locations and heights for ζ(1/2 + it)
**Format:** Python pickle file (dictionary)
**Size:** ~0.01 MB
**Structure:**
```
{ 't_values': ndarray (200,), # t values at top 200 peaks 'heights': ndarray (200,), # Peak heights (|ζ| values) 'indices': ndarray (200,), # Indices in original t array 'N': 10000
}
```
**Peak Characteristics:**
- 200 highest peaks selected from 241 total peaks with prominence > 1.0
- t range: [10025.01, 19914.96]
- Height range: [3.06, 17.83] ### 4. omega_decomposition_peaks_N10000.pkl
**Description:** ω-class decompositions at peak locations
**Format:** Python pickle file (dictionary)
**Size:** ~0.13 MB
**Structure:**
```
{ 'function_class_name': [ { 't': float, # Peak location 'peak_height': float, # |D_F(t; N)| at peak 'S_k': {k: complex, ...}, # ω-class sums S_k(t; N) 'r': float # Inter-class energy ratio }, ... (200 peaks) ], ... (3 function classes: zeta, L_DH, liouville)
}
``` **Inter-class Ratio Statistics:**
- zeta: mean r = 1.28, 12.5% of peaks have r < 0
- L_DH: mean r = -0.29, 77.5% of peaks have r < 0 - liouville: mean r = -0.90, 100% of peaks have r < 0 (STRONGLY anti-correlated) ## Function Classes (8 Total) ### F1: zeta (ζ function)
- **Definition:** a_n = 1 for all n
- **Type:** Multiplicative, satisfies RH (assumed)
- **Coefficients:** Real, dtype=float64
- **Key property:** Reference function for classical results ### F2: chi4 (L-function with character mod 5)
- **Definition:** χ(n) where χ is primitive character mod 5
- **Character values:** χ(1)=1, χ(2)=i, χ(3)=-i, χ(4)=-1, χ(0)=0
- **Type:** Multiplicative
- **Coefficients:** Complex, dtype=complex128 ### F3: f_rand (Multiplicative random)
- **Definition:** Random phases on primes, extended multiplicatively
- **Type:** Multiplicative with random Euler product
- **Coefficients:** Complex on unit circle, dtype=complex128
- **Seed:** 42 (fixed for reproducibility) ### F4: L_DH (Davenport-Heilbronn function) ⚠️
- **Definition:** L_DH(s) = ((1-iκ)/2)·L(s,χ) + ((1+iκ)/2)·L(s,χ̄)
- **κ value:** κ ≈ 0.28408
- **Type:** NOT MULTIPLICATIVE (linear combination)
- **Coefficients:** Complex, dtype=complex128
- **Special:** Has off-line zeros (zeros with Re(s) > 1/2)
- **Known zeros:** - (0.808517, 85.699348) - (0.650786, 114.163343) - (0.574355, 166.479306) - (0.724258, 176.702461) ### F5: L_DH_eps (Perturbed Davenport-Heilbronn)
- **Definition:** Same as L_DH but with κ → κ + ε
- **Perturbations:** ε ∈ {±0.1, ±0.05}
- **Type:** NOT multiplicative ### F6: liouville (Liouville function) ⚠️ CRITICAL RULE R3
- **Definition:** λ(n) = (-1)^Ω(n) where Ω(n) = number of prime factors with multiplicity
- **Type:** COMPLETELY MULTIPLICATIVE (λ(mn) = λ(m)λ(n) ALWAYS)
- **Coefficients:** {-1, +1}, dtype=float64
- **Euler product:** ∏_p (1 + p^(-s))^(-1)
- **ANOMALOUS PROPERTY:** Shows strong resonance (mean r = -0.90 at peaks)
- **IMPORTANT:** Do NOT classify as non-multiplicative! ### F7: mobius (Möbius function)
- **Definition:** μ(n) = (-1)^k if n is product of k distinct primes, 0 if not square-free
- **Type:** Multiplicative
- **Coefficients:** {-1, 0, 1}, dtype=float64 ### F8: f_fully_rand (Fully random)
- **Definition:** i.i.d. random phases on unit circle for all n
- **Type:** NOT multiplicative
- **Coefficients:** Complex on unit circle, dtype=complex128
- **Seed:** 42 + N (varies with N for reproducibility) ## Mathematical Definitions ### Dirichlet Polynomial
D_F(t; N) = Σ_{n=1}^N a_n / n^{1/2 + it} Computed using Kahan compensated summation for numerical stability (RULE R5). ### ω-class Decomposition
S_k(t; N) = Σ_{ω(n)=k} a_n / n^{1/2 + it} where ω(n) = number of distinct prime divisors of n. Key identity: D_F(t; N) = Σ_{k=0}^{K_max} S_k(t; N) Note: k=0 corresponds to n=1 only (ω(1) = 0). ### Inter-class Energy Ratio
r(t; N) = Σ_{j≠k} Re[S_j S̄_k] / Σ_k |S_k|² **Central observable for F1 (conditional anti-correlation).**
- r < 0 indicates anti-phase relationship between ω-classes
- r > 0 indicates constructive interference
- MVT predicts ⟨r⟩ ≈ 0 unconditionally (RULE R6)
- Interesting behavior appears when conditioning on peaks ## Computational Details ### Parameters
- **t range:** [10,000, 20,000]
- **Sampling:** 2,000 uniformly spaced points, Δt ≈ 5.0
- **Truncation:** N = 10,000 (will extend to 10^5, 10^6, 10^7 in full program)
- **Precision:** - Standard computation: float64/complex128 - Validation: mpmath with 50 decimal places
- **Random seed:** 42 (for reproducibility) ### Numerical Methods
- **Summation:** Kahan compensated summation (required by R5)
- **Peak finding:** scipy.signal.find_peaks with prominence > 1.0, distance ≥ 5
- **ω-function:** Sieve-based computation, pre-computed for all n ≤ N ### Pre-computed Arrays
The DirichletCoefficients class pre-computes:
- Primes up to N_max (9,592 primes for N=10^5)
- ω(n) for all n ≤ N_max (distinct prime factors)
- Ω(n) for all n ≤ N_max (prime factors with multiplicity) ## Data Quality and Validation ### Tests Performed
1. **Kahan summation:** Verified against pathological examples ✓
2. **ω-class decomposition:** Verified Σ_k S_k = D_F to machine precision ✓
3. **Liouville multiplicativity:** Verified λ(mn) = λ(m)λ(n) for sample pairs ✓
4. **Coefficient generation:** Tested all 8 function classes ✓ ### Known Properties Verified
- ζ: All coefficients = 1 ✓
- Liouville: All coefficients ∈ {-1, +1} ✓
- Möbius: All coefficients ∈ {-1, 0, +1} ✓
- Random functions: All on unit circle ✓ ### Anomalous Observations (Preliminary)
1. **Liouville anti-correlation:** 100% of peaks show r < 0 (mean = -0.90) - Dramatically stronger than ζ (only 12.5% have r < 0) - Suggests unique parity-driven cancellation mechanism 2. **L_DH behavior:** 77.5% of peaks show r < 0 (mean = -0.29) - Intermediate between ζ and Liouville - Non-multiplicative structure affects ω-class interactions 3. **ζ peaks:** Only 12.5% show r < 0, mean r = 1.28 is POSITIVE - This appears inconsistent with conditional anti-correlation hypothesis - May require larger peaks or higher N to observe - WARNING: Current data does NOT show strong anti-correlation for ζ at peaks ## Environment Configuration ### Python Packages Required
- numpy (standard installation)
- scipy (standard installation)
- matplotlib (standard installation)
- mpmath (standard installation)
- pandas (standard installation)
- sympy (available but not yet used)
- sklearn (available but not yet used) ### Package Installation
All packages were pre-installed in the environment. No additional installations required. ### Known Issues
None encountered during dataset generation. ## Usage Notes for Future Analyses ### Loading the Data
```python
import pickle
import numpy as np # Load main Dirichlet polynomial data
with open('dirichlet_polynomials_N10000_T10000-20000.pkl', 'rb') as f: data = pickle.load(f) t_values = data['data']['zeta']['t_values']
zeta_values = data['data']['zeta']['D_F']
zeta_modulus = data['data']['zeta']['modulus'] # Load omega decomposition data
with open('omega_decomposition_peaks_N10000.pkl', 'rb') as f: omega_data = pickle.load(f) # Access zeta omega-class data at peaks
zeta_omega = omega_data['zeta']
first_peak = zeta_omega[0]
t_peak = first_peak['t']
S_k = first_peak['S_k'] # Dictionary {k: S_k_value}
r_value = first_peak['r']
``` ### Computing Additional Metrics
The core computational engine is available via the DirichletCoefficients class:
```python
# Initialize for desired N_max
coeff_gen = DirichletCoefficients(N_max=100000) # Get coefficients for any function class
coeffs = coeff_gen.get_coefficients('zeta', N=10000) # Compute Dirichlet sum at specific t
D_F = compute_dirichlet_partial_sum(coeffs, t=15000.0, N=10000) # Compute omega-class decomposition
S_k = omega_class_decomposition(coeffs, t=15000.0, N=10000, omega_vals=coeff_gen.omega)
``` ### Validation Requirements (RULE R2)
Before ANY analysis, must validate L_DH at known zeros:
```python
# Off-line zeros of L_DH: (sigma, t)
zeros = [(0.808517, 85.699348), (0.650786, 114.163343), (0.574355, 166.479306), (0.724258, 176.702461)] # Compute with mpmath at high precision
# ALL must satisfy |L_DH(ρ)| < 10^-6
# If any fail → STOP analysis
``` ### Critical Analytical Rules
- **R1:** Use ONLY the functions defined in this dataset. Do not re-implement.
- **R4:** ALL metrics must be tracked across N ∈ {10^4, 10^5, 10^6, 10^7}
- **R5:** ALL Dirichlet sums must use Kahan summation
- **R6:** Specify conditioning for ALL correlation claims (never claim unconditional negative covariance)
- **R7:** Report observations, do not overclaim theoretical results ## Next Steps (Not Yet Implemented) ### Immediate Priorities
1. Extend to N ∈ {10^5, 10^6, 10^7} to verify N-dependence
2. Implement Validation Gate (R2): test L_DH at known zeros
3. Quartile analysis: bin peaks by magnitude, compute ⟨r⟩ per quartile
4. Full moment decomposition (k=1,2,3)
5. Phase offset analysis: Δφ(j,k) between ω-classes ### Research Questions to Address
- Q1: Is conditional anti-correlation r<0 specific to ζ or general?
- Q2: What fraction of moments comes from ω-class cross-terms?
- Q3: Is Δφ(1,2) ≈ π at peaks (anti-phase between primes and semiprimes)?
- Q4: Does liouville's strong anti-correlation generalize to higher N? ### Data Expansion Needed
- More function classes: chi4, mobius, f_rand (currently only computed for 3)
- Finer t sampling near peaks for phase analysis
- Moment integrals: ∫|D_F|^{2k} dt for k=1,2,3,4
- Continuous perturbation data: ξ(θ) for θ ∈ [0,π] ## File Manifest ```
./dirichlet_polynomials_N10000_T10000-20000.pkl 0.38 MB
./dirichlet_summary_N10000.csv ~0.001 MB ./zeta_peaks_N10000.pkl ~0.01 MB
./omega_decomposition_peaks_N10000.pkl 0.13 MB
./DATASET_README.txt (this file)
``` Total dataset size: ~0.52 MB ## Citation and Provenance This dataset was computationally generated as part of a mathematical research program investigating the ω-class geometry of Dirichlet polynomials. All code is deterministic and reproducible with seed=42. Generated: 2024
Mathematical framework: Dirichlet L-functions, analytic number theory
Research fronts: Conditional anti-correlation, moment decomposition, semiprime fragility ## Contact and Issues For questions about:
- Mathematical definitions: See research program documentation
- Data structure: See "Structure" sections above - Computational methods: See "Computational Details" and source code
- Anomalies: Note that some preliminary findings contradict expectations (see "Anomalous Observations")
