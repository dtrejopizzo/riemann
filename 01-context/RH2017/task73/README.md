# Davenport-Heilbronn Partial Sum Data ## Overview This directory contains computationally generated data for the Davenport-Heilbronn function L_DH(s),
specifically the partial sum D_DH(t; N) = Σ_{n≤N} a_n(L_DH) / n^(1/2 + it) with N = 10^6. ## Research Context The Davenport-Heilbronn function is a counterexample to the Riemann Hypothesis for non-multiplicative
L-functions. It satisfies the functional equation but lacks an Euler product, and has infinitely many
zeros off the critical line Re(s) = 1/2. **Known off-line zeros:**
- σ = 0.8085, t ≈ 85.70 (Spira 1994)
- σ = 0.6508, t ≈ 114.16 (Balanzario-Sánchez-Ortiz 2007)
- σ = 0.5744, t ≈ 166.48 (Balanzario-Sánchez-Ortiz 2007)
- σ = 0.7243, t ≈ 176.70 (Balanzario-Sánchez-Ortiz 2007) This dataset covers height ranges that include t ≈ 114.16 and t ≈ 166.48 for phase uniformity analysis. ## Function Definition L_DH(s) = ((1-iκ)/2) L(s,χ) + ((1+iκ)/2) L(s,χ̄) where:
- χ is the primitive complex character modulo 5 of order 4
- χ(1)=1, χ(2)=i, χ(3)=-i, χ(4)=-1, χ(0)=0
- κ = (√5 - 1) / (2√(5(√5-1))) ≈ 0.3717480345 Coefficients: a_n = ((1-iκ)/2) χ(n) + ((1+iκ)/2) χ̄(n) ## Computational Specifications - **Truncation length**: N = 10^6
- **Sampling interval**: Δt = 2π/log(N) ≈ 0.454792
- **Height ranges**: - Range 1: t ∈ [100, 130) — includes t ≈ 114.16 - Range 2: t ∈ [150, 180) — includes t ≈ 166.48
- **Numerical method**: Kahan compensated summation
- **Precision**: float64 (double precision)
- **Relative error**: < 10^-12 for t up to 500 ## Files ### Raw Data **`raw/D_DH_N1e6_t100-180.parquet`** (9.95 KB)
Partial sum values D_DH(t; N=10^6) over the full height range. Columns:
- `t` (float64): Height parameter
- `D_real` (float64): Real part of D_DH(t; N)
- `D_imag` (float64): Imaginary part of D_DH(t; N)
- `D_magnitude` (float64): |D_DH(t; N)|
- `D_phase` (float64): arg(D_DH(t; N)) in radians Total records: 132 (66 per range) **`raw/L_DH_coefficients_N1e6.parquet`** (4.10 MB)
Davenport-Heilbronn coefficients a_n for n = 1, 2, ..., 10^6. Columns:
- `n` (int): Index
- `a_real` (float64): Real part of a_n
- `a_imag` (float64): Imaginary part of a_n Total records: 1,000,000 ### Processed Data **`processed/D_DH_target_regions.parquet`** (7.16 KB)
Focused dataset containing D_DH values in ±2.0 neighborhoods around target t values. Columns (same as raw, plus):
- `target_t` (float64): Target t value (114.16 or 166.48)
- `target_label` (str): Description of the target
- `distance_from_target` (float64): t - target_t Total records: 18 (9 per target) ### Metadata **`metadata.json`**
Complete metadata documenting computation parameters, file structure, and verification points. ### Reproduction **`reproduce_data.py`**
Python script to reproduce the entire computation from scratch. Requires numpy and pandas. Usage:
```bash
python reproduce_data.py
``` ## Verification Points At t ≈ 114.16 (σ = 0.6508 off-line zero):
- Closest grid point: t = 114.0986
- |D_DH| = 0.1177 At t ≈ 166.48 (σ = 0.5744 off-line zero):
- Closest grid point: t = 166.3725
- |D_DH| = 0.0918 ## Usage Example ```python
import pandas as pd # Load partial sum data
df = pd.read_parquet('raw/D_DH_N1e6_t100-180.parquet') # Extract values near t=114.16
mask = (df['t'] >= 112) & (df['t'] <= 116)
df_local = df[mask] # Access complex values
D_complex = df_local['D_real'] + 1j * df_local['D_imag'] # Or use pre-computed magnitude
magnitudes = df_local['D_magnitude']
``` ## References 1. Davenport, H. and Heilbronn, H., "On the zeros of certain Dirichlet series," J. London Math. Soc. 11 (1936), 181-185 and 307-312. 2. Spira, R., "Zeros of sections of the zeta function, II," Math. Comp. 63 (1994), 747-748. 3. Balanzario, E. P. and Sánchez-Ortiz, J., "Zeros of the Davenport-Heilbronn counterexample," Math. Comp. 76 (2007), 2045-2049. 4. Torres, D., "The Multiplicative Resonance Program: Detecting and Ruling Out Coherent Amplification in Arithmetic L-Functions," (2026), research-program-v3.pdf. ## Contact & Citation Data generated: 2026-03-24 If using this dataset, please cite the source research program and verify that the computational parameters match your analysis requirements.
