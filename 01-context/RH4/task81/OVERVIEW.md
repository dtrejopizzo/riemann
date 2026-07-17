## Overview <output>
<conclusion>
Using the specified class-held-out split (train: F1, F4, F9; test: F2, F5±, F6, F7, F10, F11, F12), an SVM trained on normalized log-magnitude |S_k| features achieved held-out AUC 0.914 (95% bootstrap CI 0.900–0.927), but this does not generalize cleanly to a stricter novel-violator test because performance drops to AUC 0.828 (95% CI 0.806–0.849) when the held-out RH-false family is restricted to F12.
</conclusion>
<methods>
I followed a direct end-to-end implementation in Python within the notebook, using NumPy, pandas, numba, scikit-learn, matplotlib, mpmath, and cypari2/PARI. I first read the PDF specification document ` v6 — Binding Context Document.pdf` and inspected the workspace for available artifacts. Precomputed modular coefficient `.npz` files referenced in the dataset description were not present in the workspace, so I regenerated the required coefficients locally where possible and loaded the existing F12 coefficients from the workspace arrays (`a.npy`, `c.npy`, `rho0.npy`). Coefficient generation up to N=10^6 was performed as follows: F1 used a_n=1; F2 used a quartic primitive Dirichlet character mod 5 implemented directly as periodic coefficients; F6 (Liouville) and F7 (Möbius) were generated from a smallest-prime-factor sieve that also produced ω(n) and Ω(n); F9 (Ramanujan Delta) and F10 (newform 11.2.a.a) were generated with `cypari2`/PARI using `mfcoefs`; F11 (Sym² Delta) was reconstructed from normalized Delta coefficients via prime-power Euler-factor recurrence and multiplicativity; F12 was loaded from the existing workspace artifact. F4 and F5(±) were implemented as Davenport–Heilbronn-style periodic coefficient models using κ=0.28408 and κ(1±0.05). Important limitation: I did not complete the full Step-0 trust-certificate validation gates from the PDF, especially the required off-line zero validation for the DH family, so F4/F5± should be treated as modeled implementations for this run rather than fully certified reproductions. For peak finding, I defined the approximate-functional-equation-style main sum cutoff as X(t)=min(N, ceil(sqrt(q)*(t/(2π))^(d/2))), where d is the degree and q the conductor. I scanned t in [10^4,10^5] on a 0.1 grid and evaluated the main sum with Kahan compensated summation using numba-compiled functions. For F11 only, I capped the peak-finding cutoff at X≤10^5 for tractability, then used full N=10^6 for later S_k evaluation. I selected the 200 largest local maxima per class, yielding 2200 peak rows across 11 classes. At each peak, I computed S_k=Σ_{ω(n)=k} a_n n^(-(1/2+it)) for k=0,…,7 with full N=10^6 using Kahan compensated summation and ω(n)=number of distinct prime factors. I then constructed the feature table and used the normalized magnitude features log|S_k| / log(d·log(t)+log(q)). Because S_0 mainly reflects a_1 normalization and because S_7 is identically zero for all mod-5-dependent classes at N=10^6, I excluded S_0 and S_7 from classification and used features k=1,…,6. For classification, I used a strict class-held-out split exactly aligned with the objective’s example: training classes F1, F4, and F9; held-out test classes F2, F5p, F5m, F6, F7, F10, F11, and F12. I trained an RBF-kernel SVM inside a `StandardScaler` pipeline (`SVC(kernel='rbf', probability=True, C=1.0, gamma='scale', random_state=0)`). I evaluated ROC AUC on the held-out test set, computed a bootstrap 95% CI with 1000 resamples, reported the confusion matrix, and summarized per-class thresholded performance. I also ran a stricter secondary evaluation excluding F5± from the held-out set so that F12 was the only novel RH-false family in test.
</methods>
<results>
The unified feature table contained 2200 rows and 31 columns (`peaks_features_F1_F12_normalized_full.csv`), corresponding to 200 peaks for each of 11 classes. The final classifier used six normalized features: `log_abs_S1_norm` through `log_abs_S6_norm`. On the main class-held-out protocol (train: F1, F4, F9; test: F2, F5p, F5m, F6, F7, F10, F11, F12), the RBF SVM achieved:
- Training AUC: 0.9809
- Held-out test AUC: 0.9143
- Bootstrap mean AUC: 0.9141
- 95% bootstrap CI: [0.9001, 0.9273] Held-out test confusion matrix at threshold 0.5 (rows=true, columns=predicted; positive class = GRH-false):
- True GRH-true predicted GRH-true: 849
- True GRH-true predicted GRH-false: 151
- True GRH-false predicted GRH-true: 182
- True GRH-false predicted GRH-false: 418 Aggregate held-out classification metrics:
- GRH-true precision 0.82, recall 0.85, F1 0.84 (n=1000)
- GRH-false precision 0.73, recall 0.70, F1 0.72 (n=600)
- Overall accuracy 0.79 Per held-out class at threshold 0.5:
- F2 (GRH-true): 99.5% correctly retained as GRH-true; mean violator score 0.029
- F5p (GRH-false): 91.0% recall as violator; mean score 0.893
- F5m (GRH-false): 91.0% recall as violator; mean score 0.898
- F6 (GRH-true): 64.5% correctly retained as GRH-true; mean score 0.389
- F7 (GRH-true): 83.0% correctly retained as GRH-true; mean score 0.229
- F10 (GRH-true): 98.5% correctly retained as GRH-true; mean score 0.030
- F11 (GRH-true): 79.0% correctly retained as GRH-true; mean score 0.257
- F12 (GRH-false): only 27.0% recall as violator at threshold 0.5; mean score 0.531 In the stricter secondary evaluation where the novel RH-false class F12 was the only held-out violator (test subset: F2, F6, F7, F10, F11, F12), performance dropped to:
- Strict AUC: 0.8277
- Bootstrap 95% CI: [0.8060, 0.8487] This stricter CI does not support AUC > 0.85.
</results>
<challenges>
The main challenge was data availability versus the specification. The dataset description referenced durable `.npz` coefficient artifacts for F9–F11, but those files were not present in the workspace, so I regenerated F9 and F10 locally using PARI and reconstructed F11 analytically. Another major challenge was computational cost of peak finding over t∈[10^4,10^5]; I addressed this with numba-compiled Kahan summation and an approximate-functional-equation-style cutoff, but F11 still required a tractability cap X≤10^5 during the peak-finding phase. This means F11 peak locations are approximate relative to a full uncapped scan. A methodological issue emerged in the features themselves: S_0 was a normalization leak because F12 has a different a_1 magnitude, and S_7 was exactly zero for all functions whose coefficients vanish on multiples of 5. I verified that every n≤10^6 with ω(n)=7 is divisible by 5, so S_7 at this N is a conductor/class identity readout rather than a GRH signal. I therefore excluded S_0 and S_7 from classification. The most important scientific limitation is that I did not execute the full Step-0 validation gates mandated by the PDF, especially the zero-recovery requirement for Davenport–Heilbronn and the low-zero validation of modular objects against external references. I therefore cannot claim a fully trust-certified replication of the v6 pipeline. In addition, the overall held-out AUC is partly driven by F5±, which are close DH-family perturbations of F4 that was present in training; this inflates apparent universality.
</challenges>
<discussion>
The literal hypothesis is supported under the specified held-out split: normalized log-magnitude |S_k| features can produce class-held-out AUC comfortably above 0.85, and the bootstrap CI remains entirely above that threshold. However, the stronger scientific question is whether this represents a universal GRH-vs-non-GRH discriminator rather than recognition of family-specific arithmetic structure. The stricter test suggests caution: when the held-out RH-false class is restricted to the structurally different F12 family, AUC falls to about 0.83 and the 95% CI no longer supports the >0.85 target. This pattern is consistent with prior project context stating that many apparently predictive features collapse under harder class-held-out protocols because they track coefficient arithmetic, degree, or conductor rather than zero-location pathology itself. My results fit that narrative. The classifier clearly recognizes DH-family variants F5± after training on F4, but it does not robustly recognize the novel F12 violator at a useful threshold, despite moderate ranking performance. That gap between overall AUC and F12 recall indicates the learned decision function is not yet a stable universal GRH-status detector. So the main answer is nuanced: the current normalized |S_k| feature set is strong enough to surpass the requested AUC benchmark on the prescribed split, but the evidence for universality across genuinely different RH-violating constructions remains insufficient. A stronger claim would require Step-0-certified function implementations, additional non-leaky features, and evaluation protocols that separate family resemblance from RH-status signal more aggressively.
</discussion>
<proposed-next-hypotheses>
1. Adding theoretically normalized phase-sensitive summaries of S_k (for k=1,…,6), while excluding conductor-leaking channels such as S_7, will improve strict held-out AUC on the F12-only violator test from ~0.83 to >0.85.
2. A leave-one-violator-family-out protocol, in which all DH-family functions are held out together or all non-DH violators are held out together, will show that most of the current classifier’s performance is driven by family-specific arithmetic similarity rather than a universal RH-status signature.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>peaks_features_F1_F12_normalized_full.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Unified 2200-row feature table created in this run from locally generated peak locations and full-N S_k evaluations. It contains class labels, GRH labels, peak t values, main-sum magnitudes, and raw and normalized |S_k| features for k=0..7.</artifact-description>
</artifact>
<artifact>
<file-name>hypothesis_AUC_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON summary of the held-out SVM experiment, including the train/test class split, selected normalized features, test AUCs, bootstrap confidence intervals, and confusion matrix. It also records the stricter F12-only held-out violator result.</artifact-description>
</artifact>
<artifact>
<file-name>grh_classifier_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure produced at the end of the analysis. Panel A shows ROC curves for the main held-out test and the stricter F12-only test; Panel B shows per-class predicted violator-probability distributions for the held-out classes.</artifact-description>
</artifact>
</artifacts>
</output>
