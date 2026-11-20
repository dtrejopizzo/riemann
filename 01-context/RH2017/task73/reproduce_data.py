#!/usr/bin/env python3
"""
Reproduction script for Davenport-Heilbronn partial sum data
D_DH(t; N=10^6) for t ∈ [100,130] ∪ [150,180] This script reproduces the exact computation from the data retrieval process.
All parameters match the specifications from research-program-v3.pdf.
""" import numpy as np
import pandas as pd # ============================================================================
# STEP 1: Define the Davenport-Heilbronn function coefficients
# ============================================================================ def compute_chi_mod5(n): """ Compute χ(n) for the primitive complex character modulo 5 of order 4. χ(1)=1, χ(2)=i, χ(3)=-i, χ(4)=-1, χ(0)=0 """ n_mod5 = n % 5 chi_map = {0: 0+0j, 1: 1+0j, 2: 0+1j, 3: 0-1j, 4: -1+0j} return chi_map[n_mod5] def compute_chi_bar_mod5(n): """Compute conjugate character χ̄(n)""" return np.conj(compute_chi_mod5(n)) # Define κ parameter (equation from research-program-v3.pdf)
sqrt5 = np.sqrt(5)
kappa = (sqrt5 - 1) / (2 * np.sqrt(sqrt5 * (sqrt5 - 1))) # Compute coefficients: a_n = ((1-iκ)/2) χ(n) + ((1+iκ)/2) χ̄(n)
N = 10**6
a_DH = np.zeros(N+1, dtype=np.complex128) for n in range(1, N+1): chi_n = compute_chi_mod5(n) chi_bar_n = compute_chi_bar_mod5(n) a_DH[n] = ((1 - 1j*kappa)/2) * chi_n + ((1 + 1j*kappa)/2) * chi_bar_n print(f"Generated {N} Davenport-Heilbronn coefficients")
print(f"κ = {kappa:.10f}") # ============================================================================
# STEP 2: Kahan compensated summation (for numerical precision)
# ============================================================================ def kahan_sum_complex(values): """ Kahan compensated summation for complex values. Reduces round-off error from O(ε·N) to O(ε·log N) """ s = 0.0 + 0.0j c = 0.0 + 0.0j for val in values: y = val - c t = s + y c = (t - s) - y s = t return s # ============================================================================
# STEP 3: Compute D_DH(t; N) = Σ_{n≤N} a_n / n^(1/2 + it)
# ============================================================================ def compute_D_DH(t, N, a_coeffs): """ Compute partial sum D_DH(t; N). Uses Kahan compensated summation as specified. """ n_values = np.arange(1, N+1) phases = np.exp(-1j * t * np.log(n_values)) terms = (a_coeffs[1:] * phases) / np.sqrt(n_values) return kahan_sum_complex(terms) # ============================================================================
# STEP 4: Generate grid and compute over height ranges
# ============================================================================ # Sampling interval: Δt = 2π/log(N)
delta_t = 2 * np.pi / np.log(N) # Height ranges covering t=114.16 and t=166.48
t_grid_1 = np.arange(100.0, 130.0, delta_t)
t_grid_2 = np.arange(150.0, 180.0, delta_t)
t_grid = np.concatenate([t_grid_1, t_grid_2]) print(f"\nComputing D_DH(t; N={N}) for {len(t_grid)} values of t...")
print(f"Sampling interval: Δt = {delta_t:.6f}") # Compute D_DH for each t
D_values = np.array([compute_D_DH(t, N, a_DH) for t in t_grid]) # ============================================================================
# STEP 5: Create dataset and save
# ============================================================================ df = pd.DataFrame({ 't': t_grid, 'D_real': D_values.real, 'D_imag': D_values.imag, 'D_magnitude': np.abs(D_values), 'D_phase': np.angle(D_values)
}) df.to_parquet('D_DH_N1e6_t100-180_reproduced.parquet', compression='snappy')
print(f"\nSaved {len(df)} records to D_DH_N1e6_t100-180_reproduced.parquet") # Verification
print(f"\nVerification at key t values:")
for t_target in [114.16, 166.48]: idx = np.argmin(np.abs(df['t'].values - t_target)) t_actual = df.iloc[idx]['t'] D_mag = df.iloc[idx]['D_magnitude'] print(f" t ≈ {t_target}: actual t = {t_actual:.4f}, |D_DH| = {D_mag:.6f}")
