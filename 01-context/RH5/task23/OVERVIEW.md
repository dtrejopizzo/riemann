## Overview <output>
<conclusion>
The hypothesis is confirmed: refining only the remaining 295 Odlyzko seeds (indices 4705–4999) at dps=50 was computationally trivial (~229 s on a single core) and successfully produced the complete N=5000, dps=50 zero list for ζ, from which the ζ_δ control was generated.
</conclusion> <methods>
1. Loaded the partial cache `zeta_refined_partial.npy` (4705 high-precision string-encoded imaginary parts) and the Odlyzko seed table `zeta_zeros_N100000_dps9.npy`.
2. Set `mpmath.mp.dps = 50`.
3. For each i ∈ [4705, 5000), used `mpmath.findroot(mpmath.siegelz, mpf(str(seeds[i])))` to refine the seed to 50 decimal digits. Stored the root as a string to preserve full precision.
4. Concatenated the 4705 cached refined zeros with the 295 newly refined zeros (5000 total), verified strict monotonicity (all consecutive gaps > 0; min gap = 0.0433, max gap = 6.887), sorted defensively, and saved the result to `zeta_zeros_N5000_dps50.npy` (dtype `<U51`).
5. R2 gate verification: differences between the first three saved entries and the spec values (14.134725141, 21.022039639, 25.010857580) were all ≤ 1e-9, well within the gate. Additionally evaluated |Z(γ)| via `mpmath.siegelz` at indices 0, 4704, 4705, 4706, 4999 — all in the 1e-49 to 5e-46 range, confirming true zeros at dps=50.
6. Generated the ζ_δ control as an `(re, im)` structured array of strings: real part = '0.5' for all indices except 1000..1019 inclusive (20 zeros), which were set to '0.6' (δ=0.1, one-sided perturbation per r3/r10). Saved as `zeta_delta_zeros_N5000_dps50.npy`.
7. Produced a two-panel summary figure: (A) histogram of consecutive ζ-zero gaps for the completed N=5000 list; (B) scatter of Re(ρ_n) vs n highlighting the 20 perturbed zeros in ζ_δ.
</methods> <results>
- New refinement step: 295 zeros at dps=50 in 228.7 s wall-clock on a single core (~0.77 s/zero), consistent with prior r14 cost estimates and indeed "computationally trivial" relative to the original 4705-zero job.
- Combined list: 5000 entries, strictly increasing, min consecutive gap = 0.0433, max = 6.887, median ≈ 1.013; first γ = 14.13472514173469…, last γ = 5447.86199830130…
- R2 validation passed: |γ_i^saved − γ_i^spec| < 1e-9 for i = 1, 2, 3.
- Independent zero check: |Z(γ_i)| at sampled indices (including boundary 4704↔4705 between old and new refinements) is in [2×10⁻⁴⁹, 5×10⁻⁴⁶], confirming all entries are bona fide ζ zeros at dps=50 precision.
- ζ_δ control: 5000 ρ-tuples; 4980 entries with Re = 0.5; 20 entries (indices 1000–1019) with Re = 0.6 (δ = 0.1), imaginary parts unchanged from the ζ list.
- Outputs: `zeta_zeros_N5000_dps50.npy`, `zeta_delta_zeros_N5000_dps50.npy`, `zeta_zd_summary.png`.
</results> <challenges>
- The partial cache was stored as fixed-width Unicode strings (`<U51`) rather than as `mpmath.mpf` objects; care was needed to preserve full 50-digit precision by keeping the new entries as strings and converting only via `mpf(str(...))` when needed.
- `siegelz` evaluation cost increases with γ; the 295 new zeros sit at γ ≈ 5173–5448, where each `findroot` call takes ~0.77 s. No issues encountered, but extrapolating to N=20k would be substantially more expensive and would warrant parallelization.
- The ζ_δ structure had to be encoded carefully to retain 50-digit imaginary parts; we used a structured `dtype=[('re','<U10'),('im','<U51')]` to keep precision in plain NumPy without an mpmath dependency at load time.
</challenges> <discussion>
This closes a small but blocking step for downstream Front analyses: the canonical ζ zero list at dps=50, N=5000, is now available and gate-validated, and a matching ζ_δ control with a deliberate δ=0.1 off-line perturbation on 20 zeros (a sparse, localized contamination model) is ready. The localized perturbation pattern is the one prescribed in r3/r10 and is well-suited for testing detection power of any subsequent statistical or spectral diagnostic — e.g., persistence diagrams, Jacobi coefficient anomalies (within the n < 0.1·N_zeros reliable range), or pair-correlation deviations. Because only 20/5000 zeros are perturbed and only on the real axis, ζ_δ remains "close" to ζ on most aggregate statistics; any successful diagnostic must therefore be locally sensitive rather than purely global.
</discussion> <proposed-next-hypotheses>
1. The 20 off-line perturbations in ζ_δ (Re shifted 0.5→0.6 at indices 1000–1019) will be detectable as a localized bump in the persistent H_1 diagram of the embedded zero point cloud at a filtration scale set by the local mean gap (~1.0) but invisible in the global pair-correlation R(s) statistic averaged over all 5000 zeros.
2. Reconstructed Front-I Jacobi coefficients (a_n, b_n) for ζ_δ will diverge from those of ζ only for n in a narrow window around n ≈ 1000–1019 (within the n < 0.1·N_zeros = 500 reliability bound this localized signal is partially aliased and the bulk Jacobi spectrum will appear unchanged), implying that Front-I Jacobi fits are insensitive to localized off-line contamination at this scale.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>zeta_zeros_N5000_dps50.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Complete list of the first 5000 nontrivial Riemann ζ-zero imaginary parts at 50-decimal precision, stored as a NumPy array of fixed-width Unicode strings (dtype `<U51`). Produced by concatenating the 4705-entry cache `zeta_refined_partial.npy` with 295 newly refined zeros obtained by applying `mpmath.findroot(mpmath.siegelz, seed)` at `mp.dps=50` to Odlyzko seeds at indices 4705–4999, then sorting. R2 gate passes (first three zeros match spec to <1e-9) and `|Z(γ)|` at sampled indices is ≤ 5×10⁻⁴⁶.</artifact-description>
</artifact>
<artifact>
<file-name>zeta_delta_zeros_N5000_dps50.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>ζ_δ control zero list with 5000 entries stored as a NumPy structured array (`re` as `<U10`, `im` as `<U51`). Imaginary parts are identical to those in `zeta_zeros_N5000_dps50.npy`; real parts are '0.5' for all zeros except indices 1000–1019, which are set to '0.6' (δ=0.1 one-sided perturbation per the r3/r10 protocol).</artifact-description>
</artifact>
<artifact>
<file-name>zeta_zd_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) histogram of consecutive ζ-zero gaps for the completed N=5000, dps=50 list (median gap ≈ 1.013); (B) scatter of Re(ρ_n) vs n for the ζ_δ control showing the 20 perturbed zeros (indices 1000–1019) at Re=0.6 against the unperturbed Re=0.5 baseline.</artifact-description>
</artifact>
</artifacts>
</output>
