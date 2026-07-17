## Overview <output>
<conclusion>
At the truncated scale N=999 with ω-strata k=0..4, the spectral features (pc1_complex, H_complex) retain the same qualitative clustering seen previously at larger scale: the GRH-true classes form a compact low-entropy/high-pc1 cluster that is statistically separated from the GRH-false classes, and F13 lies decisively with the GRH-true cluster.
</conclusion>
<methods>
I worked in `/workspace/ee08b1fd-ca9c-480e-8f77-ad5fc9845ddf` using Python with NumPy, pandas, SciPy, scikit-learn, matplotlib, and SymPy. I first inspected the workspace and found that several derived artifacts described in the prompt were not present as `.npz` bundles, but key contents had been unpacked into `.npy` files. I validated this by directly loading the available arrays and matching them to the prompt descriptions. I defined the analysis plan as follows: (1) assemble or reconstruct coefficient arrays up to N=999 for all target classes; (2) compute the Dirichlet polynomial D(t;999)=Σ_{n≤999} a_n n^(-1/2-it) on t∈[10^4,2·10^4]; (3) identify the top 200 local maxima of |D(t)|; (4) compute the ω-stratified sums S_k(t)=Σ_{ω(n)=k} a_n n^(-1/2-it) for k=0,1,2,3,4 at those peak locations; (5) compute the 5×5 class-level matrix M_jk=E_t[Re(S_j(t)·conj(S_k(t)))]; (6) extract `pc1_complex` as the leading nonnegative eigenvalue fraction of M and `H_complex` as the natural-log spectral entropy of the eigenvalue distribution; (7) compare GRH-true and GRH-false clusters and quantify F13’s proximity to both centroids. Coefficient provenance and preprocessing were as follows. F1 used a_n=1. F6 and F7 were generated directly from the Liouville λ(n) and Möbius μ(n) functions using SymPy. F9 used `coeffs_F9_a.npy` and was normalized by n^(11/2). F10 used `coeffs_F10_a.npy` and was normalized by n^(1/2). F11 used `lambda_n.npy` directly, which already stores the normalized Sym²(Δ) coefficients. F12 used `a.npy` truncated to n≤999. F14 used `a_n_real.npy + i*a_n_imag.npy`, truncated to n≤999. F13 used `a_F13.npy`; because that file had an indexing ambiguity (it appeared to include a placeholder at index 0 and lacked an explicit nth=999 term), I aligned it to n=1..998 via entries 1:999 and left the n=999 coefficient at 0. I then verified that this reproduced the saved F13 spectral features closely. F2, F4, F5p, and F5m were reconstructed from the PDF specification and standard mod-5 / Davenport–Heilbronn conventions: F2 as the order-4 character mod 5 with values {1,i,-i,-1,0} by residue class; F4 as the real Davenport–Heilbronn pattern {1,κ,-κ,-1,0} with κ=0.28408; F5p and F5m as ±5% perturbations of κ. The ω-stratification used `omega_array.npy`. Inspection showed the stored indexing corresponded to ω(n) via array indices 1:1000 for n=1..999, so I used that mapping. Since max ω(n) for n<1000 is 4, all analyses were restricted to k≤4, matching the stated small-N protocol. For the peak search, I evaluated D(t) on a dense regular grid from 10000 to 20000 with step 0.05 and used `scipy.signal.find_peaks` to locate local maxima of |D(t)|. I retained the 200 highest peaks per class. At those 200 t-values I computed S_k(t) exactly by direct vectorized summation. I then formed M_jk=mean_t Re(S_j·conj(S_k)) and computed eigenvalues with `numpy.linalg.eigvalsh`, clipping tiny negative values to zero to stabilize the entropy calculation against numerical roundoff. I validated the pipeline against existing saved small-N outputs. For F13 I reproduced `pc1_complex=0.9491` vs saved `0.9496` and `H_complex=0.2312` vs saved `0.2295`. For F14 I reproduced `pc1_complex=0.9239` vs saved `0.9242` and `H_complex=0.3305` vs saved `0.3297`. These close matches support that the reconstruction and implementation are faithful. For quantitative separation, I computed GRH-true and GRH-false centroids in the 2D feature space, excluding F13 from the GRH-true centroid when assessing F13. I measured Euclidean distances in both raw and z-scored feature space. I also compared GRH-true vs GRH-false feature distributions using two-sided Mann–Whitney U tests and Welch t-tests. As a simple generalization check, I ran leave-one-out nearest-centroid and logistic regression classifiers on GRH status using only the 2D spectral features. I saved the main tabular output to `spectral_features_N999_all13.csv`, the matrices and peak data to `spectral_features_N999_all13.npz`, and the summary plot to `F13_consistency_N999.png`.
</methods>
<results>
The computed spectral features for the 13 classes were:
- F1: pc1_complex=0.9563, H_complex=0.2066
- F2: 0.9554, 0.2105
- F4: 0.9286, 0.3220
- F5p: 0.9278, 0.3244
- F5m: 0.9291, 0.3197
- F6: 0.9405, 0.2595
- F7: 0.9449, 0.2476
- F9: 0.9559, 0.2070
- F10: 0.9480, 0.2396
- F11: 0.9513, 0.2281
- F12: 0.9401, 0.2728
- F13: 0.9491, 0.2312
- F14: 0.9239, 0.3305 The GRH-true classes occupied the expected high-pc1 / low-entropy region, while the GRH-false classes occupied a lower-pc1 / higher-entropy region. The strongest GRH-false cluster consisted of F4, F5p, F5m, and F14 around pc1≈0.924–0.929 and H≈0.320–0.331. F12 was intermediate but still on the GRH-false side (pc1=0.9401, H=0.2728). F13 fell squarely inside the GRH-true cloud, nearest to F11 and F10. Centroid analysis:
- GRH-true centroid (excluding F13): approximately (0.9504, 0.2284)
- GRH-false centroid: approximately (0.9300, 0.3139)
- Distance from F13 to GRH-true centroid: 0.0030
- Distance from F13 to GRH-false centroid: 0.0849
- Distance ratio (false / true): 28.4 Using z-scored features gave the same conclusion:
- |F13 − GRH-true centroid| = 0.125
- |F13 − GRH-false centroid| = 2.490
- Ratio = 19.85 Distributional tests showed statistically significant separation between GRH-true and GRH-false classes despite the small class count:
- Mann–Whitney U for pc1_complex: U=40.0, p=0.0016
- Mann–Whitney U for H_complex: U=0.0, p=0.0016
- Welch t-test for pc1_complex: t=6.120, p=0.0001
- Welch t-test for H_complex: t=-7.077, p<0.0001 Nearest-neighbor structure around F13 was entirely GRH-true:
- nearest neighbors to F13 were F11, F10, F7, F2, and F9, all GRH-true. Leave-one-out classification on GRH status using only these two features gave:
- nearest-centroid accuracy: 12/13 = 0.923
- only F12 was misclassified by nearest-centroid; F13 was correctly assigned GRH-true. Validation against saved small-N artifacts:
- F13 recomputed vs saved: pc1 0.9491 vs 0.9496; H 0.2312 vs 0.2295
- F14 recomputed vs saved: pc1 0.9239 vs 0.9242; H 0.3305 vs 0.3297
These discrepancies are small and consistent with peak-grid or indexing details.
</results>
<challenges>
The main challenge was that several files named in the prompt (`F13_smallN_data.npz`, `coeffs_F12_N1e6.npz`, `F14_data.npz`, `coeffs_F11_N1e6.npz`) were not present in the workspace as described. I could not use those exact bundles because they were absent. Instead, I found that much of their content had been unpacked into individual `.npy` files and used those directly. A second challenge was that the exact code used in prior runs to define F2, F4, F5p, and F5m was not present in the workspace. I therefore reconstructed these classes from the PDF specification and standard Davenport–Heilbronn / Dirichlet character conventions. This reconstruction is well supported by the document and by the resulting geometry, but exact bit-for-bit equivalence to prior hidden code cannot be guaranteed without the original generator. A third challenge was an indexing ambiguity in `a_F13.npy`: the array appeared to contain a placeholder at index 0 and no explicit coefficient for n=999. I resolved this conservatively by using entries 1:999 for n=1..998 and setting the n=999 coefficient to zero. Because the recomputed F13 features matched the saved F13 features closely, this approximation appears acceptable for the current objective, but exact reproducibility would require the original F13 generation code or the missing `F13_smallN_data.npz` bundle. Methodologically, the sample size for class-level inference is small (8 GRH-true vs 5 GRH-false classes including F13/F14), so p-values should be interpreted cautiously. I therefore reported both nonparametric and parametric tests and emphasized effect geometry (centroid distances and nearest neighbors) rather than relying on a single inferential method.
</challenges>
<discussion>
These results support the hypothesis. At N=999 and k≤4, the spectral signature does not collapse; instead, it preserves the same broad organization reported at larger scale. The GRH-true families remain concentrated in a low-entropy, high-leading-eigenvalue region, whereas the GRH-false families shift toward higher entropy and reduced dominant-eigenvalue concentration. F13, the Maass-form class whose small-N result motivated this consistency check, sits very near the GRH-true centroid and very far from the GRH-false centroid. That is exactly the pattern needed to argue that the F13 signal is not an artifact of truncation to N=999. The structure is not perfectly binary at the family level: F12 is visibly intermediate and is the only failure in leave-one-out nearest-centroid classification. This is scientifically important, because it is consistent with the broader project memory that different RH-violator constructions need not occupy identical regions of feature space and that generalization across violator families can be asymmetric. Even so, F12 still lies on the GRH-false side of the centroid geometry, and the overall GRH-true/false split remains strong. Taken together, the evidence indicates that the small-N, k≤4 protocol used for the Maass-form study is comparable to the large-N methodology in the specific sense relevant here: it preserves the core spectral clustering pattern across the available families. Therefore, the Maass-form result in r47 should be regarded as methodologically credible rather than inconclusive due to truncation alone.
</discussion>
<proposed-next-hypotheses>
1. The borderline position of F12 reflects construction-specific heterogeneity among RH-violators: if additional DH-style linear-combination violators are generated at N=999, their (pc1_complex, H_complex) features will span a broader subcluster than the tighter F4/F5p/F5m/F14 group.
2. Recomputing the same 13-class panel with Hermitian M_jk = E[S_j conj(S_k)]-based spectral features, rather than Re(M_jk) alone, will preserve F13’s proximity to the GRH-true centroid and may improve the separation of F12 from the GRH-true classes.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>spectral_features_N999_all13.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>CSV table containing the final N=999, k≤4 spectral features for all 13 classes, including GRH-status labels and each class's Euclidean distances to the GRH-true and GRH-false centroids. Created from direct computation of top-200-peak S_k(t) spectra in the notebook.</artifact-description>
</artifact>
<artifact>
<file-name>spectral_features_N999_all13.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing per-class 5×5 M_jk matrices, top-200 peak locations and heights, S_k(t) arrays, class labels, and final pc1_complex/H_complex values for the 13-class N=999 analysis. Generated directly from the reconstructed coefficient sets and the peak-based spectral pipeline.</artifact-description>
</artifact>
</artifacts>
</output>
