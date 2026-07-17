## Overview <output>
<conclusion>
Peak-level phase coherence P(t)=|Σ_{k=1..4}S_k(t)|²/Σ_{k=1..4}|S_k(t)|² does not support the hypothesis as stated: across all 2200 peaks, GRH-false classes had a slightly higher distribution than GRH-true classes, so P(t) is not a viable standalone feature for GRH/non-GRH discrimination in the proposed direction.
</conclusion>
<methods>
I followed this plan: (1) load the 2200 peak locations from peaks_features_F1_F12_normalized_full.csv; (2) reconstruct complex ω-stratified sums S_k(t), k=0..7, at N=10^6 for all 11 classes; (3) compute the phase coherence score P(t)=|Σ_{k=1..4}S_k(t)|²/Σ_{k=1..4}|S_k(t)|² for each peak; (4) summarize class-wise distributions; (5) test GRH-true versus GRH-false differences with a Mann-Whitney U test; and (6) generate a final summary figure. Implementation details: I used Python with numpy, pandas, scipy, scikit-learn, matplotlib, numba, and cypari2/PARI. I first computed ω(n), Ω(n), μ(n), and the SPF sieve up to N=10^6. I then implemented a Numba-accelerated function with Kahan compensated summation to evaluate S_k(t)=Σ_{ω(n)=k} a_n n^(-1/2-it) simultaneously for k=0..7. This implementation was validated exactly against the existing complex S_k arrays for F1, F2, F6, and F7 at their saved peak locations. Coefficient construction:
- F1: a_n=1.
- F2: primitive order-4 Dirichlet character mod 5, with χ(2)=i.
- F4: Davenport-Heilbronn coefficients a_n=Re(χ(n))+κ Im(χ(n)); κ was numerically refined to 0.28407904 to reproduce existing S_k values.
- F5p/F5m: effective DH-family perturbations were fit directly to reproduce the stored |S_k| magnitudes, giving κ=0.2982840142 and κ=0.2698759855 respectively.
- F6: Liouville λ(n)=(-1)^Ω(n).
- F7: Möbius μ(n).
- F9: Ramanujan Δ coefficients via cypari2/PARI mfDelta() and mfcoefs, normalized as τ(n)/n^(11/2).
- F10: level-11 weight-2 newform via PARI mfinit/mfbasis/mfcoefs, normalized as a_n/√n.
- F11: Sym²(Δ) normalized coefficients constructed from F9 prime coefficients using the degree-3 Euler-factor recurrence.
- F12: loaded directly from local a.npy. Validation against the CSV magnitudes abs_S0…abs_S7 was performed for every class. F1/F2/F6/F7/F9/F10/F11/F12 matched to machine precision; F4/F5 variants matched after κ fitting. After obtaining complex S_k, I computed P(t) for all 2200 peaks, aggregated by class and by GRH label, ran Mann-Whitney U tests, calculated Cliff’s delta and ROC AUC, saved the per-peak table to phase_coherence_per_peak.csv, saved the complex arrays to Sk_complex_csv_peaks_all_classes.npz, and produced a boxplot figure phase_coherence_boxplot.png.
</methods>
<results>
Data reconstruction and validation:
- 2200 peaks analyzed: 11 classes × 200 peaks/class.
- Validation of reconstructed |S_k| versus CSV abs_Sk: - F1: max relative error 2.92×10^-10 - F2: 1.72×10^-10 - F4: 2.85×10^-6 before final κ refinement - F5p: 4.44×10^-8 after κ fitting - F5m: 4.29×10^-8 after κ fitting - F6: 3.15×10^-10 - F7: 1.72×10^-10 - F9: 5.36×10^-10 - F10: 3.03×10^-10 - F11: 4.60×10^-11 - F12: 1.75×10^-10 Class-level phase coherence summaries (median P(t), IQR):
- F10 (GRH-true): 3.3560, [3.233, 3.450]
- F9 (GRH-true): 3.3692, [3.255, 3.460]
- F12 (GRH-false): 3.4272, [3.169, 3.669]
- F11 (GRH-true): 3.4316, [3.212, 3.573]
- F6 (GRH-true): 3.4362, [3.281, 3.589]
- F7 (GRH-true): 3.5415, [3.299, 3.637]
- F5p (GRH-false): 3.5675, [3.342, 3.725]
- F5m (GRH-false): 3.5679, [3.341, 3.723]
- F4 (GRH-false): 3.5693, [3.322, 3.723]
- F1 (GRH-true): 3.5720, [3.426, 3.703]
- F2 (GRH-true): 3.6807, [3.568, 3.778] Grouped GRH summaries:
- GRH-true peaks: n=1400, mean=3.4042, median=3.4649
- GRH-false peaks: n=800, mean=3.4493, median=3.5383 Statistical tests:
- Mann-Whitney U, alternative “GRH-true > GRH-false”: U=497345, p≈1.0000
- Mann-Whitney U, two-sided: U=497345, p=1.23×10^-5
- Cliff’s delta: -0.1119
- ROC AUC using P(t) alone to classify GRH-true: 0.4441
- ROC AUC using P(t) alone to classify GRH-false: 0.5559 Thus, the observed shift was statistically detectable but opposite to the hypothesis direction and small in effect size.
</results>
<challenges>
The primary challenge was that the available workspace did not contain a ready-made Sk_complex_arrays.npz for all 11 classes at the CSV peak locations. The pre-existing complex arrays for F1/F2/F4/F5p/F5m/F6/F7 corresponded to different peak sets, so they could not be used directly for the requested 2200-peak analysis. I therefore rebuilt the full complex S_k dataset from scratch. A second challenge was missing cypari2 initially; I installed it and increased the PARI stack to 4 GB before generating F9 and F10 modular-form coefficients. F10 coefficient generation was comparatively slow (~193 s). A third challenge was that the F5p/F5m perturbation convention in the provided narrative was not numerically consistent with a naive κ±0.05 parameterization; I resolved this by fitting the effective κ values directly against the stored abs_Sk magnitudes and then validating the reconstruction. This preserves data fidelity because the target magnitudes were part of the provided dataset and the fitted coefficients were only used to recover the missing complex phases required for this analysis. Methodological limitations: the Mann-Whitney U test treats peaks as independent observations, whereas peaks within a class may be correlated because they come from the same underlying L-function family. Therefore the p-value should be interpreted as a peak-level distributional comparison, not as a fully class-independent causal statement. Also, I tested one predefined feature P(t); failure of this feature does not rule out other peak-level phase descriptors.
</challenges>
<discussion>
The hypothesis predicted that systematic phase alignment at the peak level would be stronger for GRH-true functions than for GRH-false ones. The data did not support that prediction. Instead, P(t) was slightly higher for the GRH-false group overall, and its discriminative performance as a standalone GRH feature was poor (AUC 0.444 for GRH-true, equivalently 0.556 for GRH-false). This is not just a non-significant null result; the direction of the observed effect contradicts the original expectation. The class-wise pattern suggests that P(t) captures family-specific arithmetic structure rather than GRH status. In particular, F1 and F2 had high coherence, the DH-family violators F4/F5p/F5m were also high, while the modular-form families F9 and F10 were lower. F12, another GRH-violator, sat in the middle. That pattern is more compatible with dependence on coefficient family, degree, conductor, or mod-5/DH-style arithmetic than on RH truth value per se. This also helps reconcile the earlier success of class-level spectral features from M_jk: those features average cross-terms over peaks and may encode richer second-order phase geometry than the scalar peak-level compression P(t). In other words, the class-level spectral separation does not collapse cleanly to this simple one-number phase-coherence score at individual peaks. So peak-level phase information may still be useful, but P(t) as defined here is too coarse to inherit the full discriminative structure seen in the M_jk spectrum.
</discussion>
<proposed-next-hypotheses>
1. A peak-level feature based on the full 4×4 normalized Gram matrix G_jk(t)=Re(S_j(t)conj(S_k(t)))/( |S_j(t)||S_k(t)| ) for j,k=1..4 will discriminate function families better than the scalar coherence score P(t), and may recover part of the class-level M_jk spectral signal.
2. The distribution of P(t) is driven primarily by arithmetic family characteristics (e.g., mod-5/DH-style coefficients versus modular-form coefficients) rather than GRH status, so a multi-class classifier using phase features will separate families but not cleanly separate GRH-true from GRH-false labels.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>Sk_complex_csv_peaks_all_classes.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing reconstructed complex S_k arrays (k=0..7) and aligned peak t-values for all 11 function classes at the 2200 CSV peak locations. It was generated from locally reconstructed coefficient sequences using a Numba-accelerated Kahan-summation engine and validated against the provided abs_Sk columns.</artifact-description>
</artifact>
<artifact>
<file-name>phase_coherence_per_peak.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Per-peak results table with 2200 rows containing function label, GRH label, peak t, phase coherence score P_t, and the real and imaginary parts of S_0 through S_7. It was derived from the reconstructed complex S_k arrays and saved for reuse in downstream analyses.</artifact-description>
</artifact>
</artifacts>
</output>
