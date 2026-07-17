## Overview <output>
<conclusion>
The hypothesis is not supported by the available data: a One-Class SVM on leak-controlled log|S_k| features detects F4/F5±/F12/F14 well against the in-sample GRH-true baseline (all bootstrap mean AUCs >0.95 when trained on F1,F2,F9,F10,F11), but it fails the stated universality criterion because performance drops sharply against held-out GRH-true families F6/F7 and because a fully range-matched F1–F16 peak dataset could not be constructed from the available workspace artifacts.
</conclusion>
<methods>
I followed a constrained but reproducible analysis using only data present in the workspace plus one directly derivable reconstruction. First, I audited the available files and found per-peak complex ω-stratified sums S_k(t) for F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, and F12 as local .npy arrays of shape (200, 8), together with peak locations t. I also found S_F13.npy with 200 peaks for F13, and class-level spectral summaries for F14–F16, but not the definitive .npz archives described in the prompt. Because F14 had full coefficient arrays (a_n_real.npy and a_n_imag.npy) and selected peak locations, I regenerated its per-peak S_k(t) values from scratch. The reconstruction used Python, NumPy, pandas, matplotlib, scikit-learn, and Numba. I generated ω(n), the number of distinct prime factors, for n≤10^6 by sieve. I then implemented a Numba-compiled Kahan-compensated summation routine for
S_k(t) = Σ_{n≤N, ω(n)=k} a_n n^{-1/2-it}, k=0,…,7,
with complex coefficients a_n. I validated this implementation by exactly reproducing the stored F1.npy values from first principles at a known peak t, confirming that the workspace S_k arrays are indeed these ω-stratified Dirichlet partial sums. I then applied the same routine to F14’s coefficients at its 200 stored peaks, obtaining F14_Sk_recomputed.npy. The class-level spectral features were computed from the peak-averaged complex Gram matrix M_jk = E_p[S_j(t_p) overline{S_k(t_p)}]. From the eigenvalues λ_i of the Hermitian symmetrization of M, I computed pc1_complex = λ_1 / Σ_i λ_i and H_complex = -Σ_i p_i log p_i with p_i = λ_i / Σ_i λ_i. This matched the stored F13 and F14 class summaries closely. For peak-level classification, I built a consolidated table with one row per peak and features log10|S_k|. I excluded log|S_0| because it is a class-constant leak equal to log|a_1|, and I excluded log|S_7| because of the known N=10^6 mod-5 zero/degeneracy leak affecting F2/F4/F5± and observed degeneracies in additional classes. Thus the classifier used only log|S_1|,…,log|S_6|. Features were standardized using StandardScaler fit on the training set. I trained an RBF One-Class SVM (scikit-learn OneClassSVM with gamma='scale', nu=0.05). I evaluated two protocols: (1) training on GRH-true F1, F2, F9, F10, F11 and using those same families as the negative class for family-wise AUC against each violator; and (2) using held-out GRH-true F6 and F7 as the negative class to test generalization across GRH-true construction families. AUCs were computed from -decision_function scores, where larger values indicate stronger anomaly evidence. I estimated 95% bootstrap confidence intervals with 200 resamples for each family-wise AUC. Finally, I assembled a master class-level table of pc1_complex and H_complex across all available classes, including F15 and the F16(c) perturbation sweep from F16_perturbation_results.csv, and created a final two-panel figure summarizing the spectral geometry and the One-Class SVM results.
</methods>
<results>
Data availability and protocol feasibility:
- Available per-peak S_k arrays: F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12, F13.
- F14 per-peak S_k was successfully regenerated from coefficients and stored peaks.
- F15/F16 had only class-level summaries; no per-peak S_k arrays were available, so they could not be included in the OC-SVM test.
- The requested fully range-matched protocol could not be executed because the workspace lacked the definitive multi-class .npz archives and most F1–F12 peaks are in t≈[1.0×10^4, 1.0×10^5], whereas F13/F14/F15/F16 lie in t≈[1.0×10^4, 2.0×10^4]. Validation of the reconstructed S_k engine:
- Exact numerical reproduction of stored F1.npy at a tested peak confirmed the summation formula and implementation.
- Recomputed F14 class features closely matched stored values: pc1_complex = 0.8954 vs stored 0.8909; H_complex = 0.4543 vs stored 0.4733. Class-level spectral geometry (selected values):
- GRH-true core families: F1 pc1=0.9589, H=0.2117; F2 pc1=0.9537, H=0.2221; F9 pc1=0.9564, H=0.2120; F10 pc1=0.9530, H=0.2189; F11 pc1=0.9543, H=0.2150; F13 pc1=0.9496, H=0.2294.
- Violators: F4 pc1=0.9227, H=0.3642; F5p pc1=0.9222, H=0.3670; F5m pc1=0.9237, H=0.3598; F12 pc1=0.9318, H=0.3120; F14 pc1=0.8954, H=0.4543.
- Held-out GRH-true but constructionally distinct families: F6 pc1=0.9363, H=0.2808; F7 pc1=0.9398, H=0.2669.
- F16(c) class-level task showed monotone movement toward the violator region with increasing c over most of the sweep: for example c=0.20 gave pc1=0.9350, H=0.2902; c=0.40 gave pc1=0.9206, H=0.3526; c=0.60 gave pc1=0.9094, H=0.4013; c=0.80 gave pc1=0.8998, H=0.4421. One-Class SVM results, training on GRH-true F1/F2/F9/F10/F11 (full-N families, leak-controlled features log|S_1|…log|S_6|):
Using the in-sample GRH-true baseline as negatives:
- F4: mean AUC 0.9960, 95% CI [0.9938, 0.9982], anomaly flag rate 0.990.
- F5p: mean AUC 0.9948, 95% CI [0.9915, 0.9978], anomaly flag rate 0.985.
- F5m: mean AUC 0.9968, 95% CI [0.9946, 0.9987], anomaly flag rate 0.990.
- F12: mean AUC 1.0000, 95% CI [1.0000, 1.0000], anomaly flag rate 1.000.
- F14: mean AUC 0.9552, 95% CI [0.9371, 0.9718], anomaly flag rate 0.865.
All five tested violator families exceeded the target AUC > 0.9 under this in-sample reference. Using held-out GRH-true families F6/F7 as negatives:
- F4: mean AUC 0.6518, 95% CI [0.6040, 0.6912].
- F5p: mean AUC 0.6250, 95% CI [0.5799, 0.6633].
- F5m: mean AUC 0.6651, 95% CI [0.6208, 0.7045].
- F12: mean AUC 0.8813, 95% CI [0.8522, 0.9033].
- F14: mean AUC 0.4978, 95% CI [0.4555, 0.5460].
Under this stricter generalization test, no family reached a bootstrap mean AUC > 0.9, and only F12 approached the threshold. Sensitivity to including F13 in training:
- When F13 was added to the training set despite its N≈999 limitation, F14 AUC versus the in-sample baseline dropped from 0.955 to 0.898, showing that mixed-resolution training degrades stability. Feature leak controls:
- log|S_0| was constant within each class and therefore a direct class-identity leak.
- |S_7| was exactly zero for F2/F4/F5p/F5m/F12 in the available data, consistent with the known mod-5 leak, and was therefore removed.
</results>
<challenges>
The main challenge was data incompleteness relative to the requested protocol. I cannot execute the exact fully range-matched F1–F16 analysis because the workspace does not contain the definitive archives (e.g., Sk_complex_all_2200peaks.npz and the coefficient .npz files for all full-N classes), and F15/F16 lack per-peak S_k arrays entirely. The existing peak sets are also not range matched: F1–F12 peak locations mostly lie well above 2×10^4, while F13/F14/F15/F16 are confined to [10^4, 2×10^4]. This violates the intended comparison design and is a likely confounder. A second challenge is heterogeneous resolution. F13 is available only in a small-N form (N≈999), whereas the other reconstructed classes are effectively N=10^6. Including F13 in the training set materially changed F14 performance, indicating that mixed-N training can distort anomaly boundaries. A third challenge is feature leakage: log|S_0| and log|S_7| contain construction-specific artifacts rather than meaningful anomaly signal, so they had to be removed. Finally, the held-out GRH-true families F6 and F7 are themselves structurally distinct from the modular/zeta-based training families, which exposed a major family-generalization failure of the OC-SVM.
</challenges>
<discussion>
The available evidence supports a narrower statement than the original hypothesis. If the baseline GRH-true class is defined by the specific families used for training (F1, F2, F9, F10, F11), then leak-controlled log|S_k| features are highly effective at flagging the constructed violators F4, F5±, F12, and F14. However, this success is not universal across GRH-true constructions: when the negative class is shifted to held-out GRH-true families F6 and F7, performance collapses. That is exactly the type of construction-sensitivity highlighted in the project memory and is consistent with the broader finding that these peak-conditioned spectral/statistical features encode how a function is built, not simply whether it violates GRH. The class-level spectral map reinforces this interpretation. Violators occupy a distinct low-pc1/high-H region relative to the core GRH-true training families, and the F16(c) perturbation path moves smoothly from the GRH-true region toward the violator region as c increases. This suggests that the spectral features are sensitive to perturbation strength and family geometry, but not universally calibrated across all legitimate GRH-true baselines. In practical terms, the OC-SVM is a strong family-conditional anomaly detector, not a definitive universal GRH-violation detector under the present data conditions. Because the requested fully range-matched dataset could not be built from the workspace, the present analysis should be treated as a partial validation. A definitive test would require regenerating top-200 peaks in t∈[10^4,2×10^4] for all classes with the same N and the same peak-finding rule, then recomputing the entire peak-level feature matrix before refitting the OC-SVM.
</discussion>
<proposed-next-hypotheses>
1. After regenerating a truly range-matched t∈[10^4,2×10^4], N=10^6 peak dataset for all classes, a One-Class SVM trained on a broader GRH-true set that includes F6 and F7 will retain AUC > 0.9 for F12 and F14 but will show reduced separation for F4/F5±, indicating that their current detectability is partly construction-family specific.
2. The F16(c) family has a monotone transition in class-level spectral geometry, and a threshold near c≈0.4–0.5 marks entry into the empirical violator region in (pc1_complex, H_complex) space; with per-peak S_k data, peak-level anomaly scores will increase monotonically with c.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>master_class_features.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Table of class-level spectral features pc1_complex and H_complex for all classes that could be computed from available data, plus F15 and the F16(c) sweep loaded from the provided CSV. Created from local .npy peak-level S_k arrays and reconstructed F14 S_k values.</artifact-description>
</artifact>
<artifact>
<file-name>peak_level_logSk_features.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Peak-level feature table containing one row per peak and log10|S_k| values for all classes with available or reconstructed peak-level S_k arrays. Used as the main input table for One-Class SVM fitting and evaluation.</artifact-description>
</artifact>
<artifact>
<file-name>peak_logSk_OCSVM_dataset.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing the leak-controlled OC-SVM feature matrix, feature names, class labels, and peak locations. Generated from the consolidated peak-level table to provide a compact reusable modeling dataset.</artifact-description>
</artifact>
<artifact>
<artifact>
<file-name>F14_Sk_recomputed.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Recomputed complex ω-stratified sums S_k(t) for F14 across its 200 stored peaks, generated from a_n_real.npy and a_n_imag.npy using a Numba-accelerated Kahan summation engine validated against the stored F1 arrays. This enabled direct inclusion of F14 in the peak-level anomaly analysis.</artifact-description>
</artifact>
<artifact>
<file-name>OCSVM_AUC_summary.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>CSV summary of family-wise One-Class SVM AUCs and bootstrap 95% confidence intervals under both in-sample and held-out GRH-true evaluation protocols. Created from scikit-learn decision scores and 200 bootstrap resamples per family.</artifact-description>
</artifact>
</artifacts>
</output>
