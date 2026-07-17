## Overview # ANALYSIS OF L_DH^(ε=-0.05) FINE-GRAINED RESONANCE SCAN ## Main Findings **Peak Locations:**
- |D(t)| peaks at t_D = 80.852 with magnitude 3.542
- R_comp peaks at t_R = 80.910 with value 0.003213
- Peak separation: |t_R - t_D| = 0.058 **Peak Characteristics:**
- |D(t)| exhibits a sharper, more localized peak (FWHM = 0.484, SNR = 1.45)
- R_comp shows a broader peak (FWHM = 0.622, SNR = 1.25)
- The two metrics are highly correlated (r = 0.936) but peak at distinct locations **Statistical Significance:**
- Rayleigh test at t_D: p = 0.350 (NOT significant, p > 0.05)
- Rayleigh test at t_R: p = 0.335 (NOT significant, p > 0.05)
- Both R_comp peak values (~0.003) are only ~1× the random expectation (1/√n_eff ≈ 0.0031) **Hypothesis Verification:**
The research hypothesis is PARTIALLY CONFIRMED:
✓ The two metrics DO locate the resonance at distinct t values (Δt = 0.058)
✓ |D(t)| DOES produce a sharper, more localized peak than R_comp
✗ R_comp does NOT show higher SNR than |D(t)| (contrary to expectation)
✗ Neither peak shows statistically significant phase coherence (p < 0.05) **Critical Interpretation:**
The resonance at ε=-0.05 is substantially weaker than at ε=0 or ε=0.01. The observed R_comp values are barely distinguishable from random phase expectations, indicating minimal coherent phase alignment. This suggests that the perturbation ε=-0.05 significantly disrupts the structural resonance mechanism that produces strong off-line zeros in the unperturbed Davenport-Heilbronn function. --- ## Discretionary Analytical Decisions - **Perturbation parameter**: Analyzed L_DH with ε=-0.05 as specified in the research objective (κ' = κ + ε = 0.1986)
- **Truncation length**: Used N=10^6 as specified in the research objective
- **Scan parameters**: Fine-grained scan over t ∈ [80.5, 81.5] with Δt=0.001 (1001 points) centered on coarse scan peak at t≈80.86
- **Numerical precision**: Implemented Kahan compensated summation for all partial sum computations to achieve relative errors < 10^-15
- **Squarefree constraint**: Enforced a_n = 0 for all non-squarefree n (where μ(n)=0) following the corrected L_DH implementation standard
- **R_comp definition**: Computed as weighted mean resultant length for composite squarefree terms (ω(n)≥2, μ(n)≠0)
- **Rayleigh test**: Used weighted version to account for amplitude weighting by |a_n|/√n, with effective sample size n_eff = (Σw)²/(Σw²)
- **Signal-to-noise ratio**: Defined as SNR = (peak - mean)/std for both metrics
- **Peak width (FWHM)**: Computed as the width of the main contiguous region where metric exceeds half-maximum value
- **Statistical significance threshold**: Set α = 0.05 for Rayleigh test as specified in research objective
- **Character χ mod 5**: Used primitive complex character with χ(1)=1, χ(2)=i, χ(3)=-i, χ(4)=-1, χ(0)=0
- **L_DH coefficient formula**: a_n = [(1-iκ')/2]·χ(n) + [(1+iκ')/2]·χ̄(n) for squarefree n only 