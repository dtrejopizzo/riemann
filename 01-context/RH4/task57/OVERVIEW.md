## Overview <output>
<conclusion>
The hypothesis is refuted: across all 11 function classes and all 64 matrix entries per class, the unconditional theoretical cross-moment matrix \(C_{jk}\) is a very weak linear predictor of the empirical peak-conditioned matrix \(M_{jk}\) (global \(R^2=0.0135\), not >0.9), although \(F1\) alone shows a strong within-class relationship (\(R^2=0.9089\)).
</conclusion>
<methods>
I followed this analysis plan: (1) load the empirical complex peak-level \(S_k\) arrays for the 11 classes \(F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12\) from the workspace files `F*.npy` and reconstruct the empirical peak-averaged matrices \(M_{jk}=E[\Re(S_j\overline{S_k})]\); (2) generate or load Dirichlet coefficients \(a_n\) up to \(N=10^6\) for each class; (3) compute the unconditional theoretical coefficient cross-moment matrices \(C_{jk}\); (4) flatten all class-specific \((j,k)\) entries into one regression dataset; (5) fit ordinary least squares regression \(M_{jk}=\alpha C_{jk}+\beta\); (6) quantify fit quality and visualize the result. Implementation details: all code was run in Python notebook cells. I used `numpy`, `pandas`, `scipy.stats`, `scikit-learn` (`LinearRegression`), `matplotlib`, `mpmath`, and `numba`. The working directory was `/workspace/c886c986-ee90-4836-a6f5-c2b2c5692c81`. Empirical matrices: for each class, I loaded the stored complex array of shape `(200, 8)` and computed
\[
M_{jk}=\frac{1}{200}\sum_{p=1}^{200}\Re\big(S_j^{(p)}\overline{S_k^{(p)}}\big)
\]
using `np.einsum('pj,pk->jk', S, np.conj(S))` and then taking the real part. Theoretical matrices: the requested definition was
\[
C_{jk}=\Re\sum_{\substack{n,m\le 10^6\\ \omega(n)=j,\,\omega(m)=k}} \frac{a_n\overline{a_m}}{nm}.
\]
I exploited the exact factorization
\[
C_{jk}=\Re\big(T_j\overline{T_k}\big),\qquad T_j=\sum_{\substack{n\le 10^6\\\omega(n)=j}}\frac{a_n}{n},
\]
so the computation reduced to 8 weighted sums per class rather than a full double sum. I computed \(\omega(n)\) (number of distinct prime factors) by sieve up to \(10^6\). Since \(\max_{n\le 10^6}\omega(n)=7\), the bins \(j,k=0,\dots,7\) are exact at this \(N\). Coefficient construction by class:
- `F1`: \(a_n=1\).
- `F2`: complex order-4 Dirichlet character mod 5, with values \(\chi(1)=1,\chi(2)=i,\chi(3)=-i,\chi(4)=-1,\chi(5)=0\), extended periodically.
- `F4`: Davenport-Heilbronn periodic coefficients `(1, κ, -κ, -1, 0)` mod 5, using \(\kappa=(\sqrt{10-2\sqrt5}-2)/(\sqrt5-1)\approx 0.2840790438404123\).
- `F5p`, `F5m`: approximated as Davenport-Heilbronn perturbations with \(\kappa\pm 0.05\). This was an approximation because the exact fitted effective \(\kappa\) values from prior run `r35` were not present on disk in this workspace.
- `F6`: Liouville \(\lambda(n)=(-1)^{\Omega(n)}\), using a smallest-prime-factor sieve and \(\Omega(n)\) with multiplicity.
- `F7`: Möbius \(\mu(n)\), computed from the same smallest-prime-factor sieve.
- `F9`: loaded `coeffs_F9_a.npy` and normalized Ramanujan tau coefficients to Selberg-class scale by dividing by \(n^{11/2}\).
- `F10`: loaded `coeffs_F10_a.npy` and normalized the weight-2 newform coefficients by dividing by \(n^{1/2}\).
- `F11`: constructed symmetric-square coefficients of \(\Delta\) multiplicatively from normalized \(F9\) coefficients. For primes, I used \(A_p=a_p^2-1\); for prime powers I used the degree-3 local recurrence induced by the Sym² Euler factor with elementary symmetric polynomials \(e_1=e_2=a_p^2-1\), \(e_3=1\); then extended multiplicatively to all \(n\le 10^6\).
- `F12`: loaded the precomputed complex coefficient array from `a.npy`. Regression dataset: I created one row per class and matrix entry, giving 11 × 8 × 8 = 704 observations with columns `class`, `j`, `k`, `M_jk`, `C_jk`, and `diag` (whether \(j=k\)). I then fit `LinearRegression` with `C_jk` as the sole predictor. Statistical notes: this is descriptive regression on a deterministic constructed dataset, so inferential p-values are of limited substantive meaning; I report them only for completeness of the Pearson correlation. I did not claim causality. The principal quantitative criterion was the requested goodness-of-fit threshold \(R^2>0.9\), which was directly tested.
</methods>
<results>
The flattened regression across all 704 points gave:
- slope \(\alpha = 1.0597\)
- intercept \(\beta = 8.3887\)
- coefficient of determination \(R^2 = 0.0135\)
- Pearson correlation \(r = 0.1163\), \(p = 2.00\times10^{-3}\) This falls far short of the target \(R^2 > 0.9\). Per-class regressions (64 points each) showed:
- `F1`: \(\alpha=1.8633\), \(\beta=1.5024\), \(R^2=0.9089\), \(r=0.9534\)
- `F2`: \(\alpha=-4.3862\), \(\beta=8.2979\), \(R^2=0.0023\)
- `F4`: \(\alpha=-0.8941\), \(\beta=2.6183\), \(R^2=0.0010\)
- `F5p`: \(\alpha=-0.9664\), \(\beta=2.6957\), \(R^2=0.0011\)
- `F5m`: \(\alpha=-0.8352\), \(\beta=2.5559\), \(R^2=0.0009\)
- `F6`: \(\alpha=0.0405\), \(\beta=18.6896\), \(R^2=0.000007\)
- `F7`: \(\alpha=0.0053\), \(\beta=4.5404\), \(R^2=0.000005\)
- `F9`: \(\alpha=-2.7657\), \(\beta=4.2308\), \(R^2=0.0022\)
- `F10`: \(\alpha=0.2290\), \(\beta=7.3420\), \(R^2=0.000009\)
- `F11`: \(\alpha=-1.9059\), \(\beta=7.2510\), \(R^2=0.0005\)
- `F12`: \(\alpha=-0.1204\), \(\beta=30.1764\), \(R^2=0.000004\) So the only class with a strong linear relationship was `F1`; all other classes were effectively uncorrelated under this model. Representative diagonal comparisons illustrate the mismatch. For `F1`, empirical and theoretical diagonals were of similar structure:
- `F1` empirical diag \(M_{kk}\): `[1.000, 18.866, 50.644, 30.871, 10.354, 2.250, 0.059, 0.000]`
- `F1` theoretical diag \(C_{kk}\): `[1.000, 13.398, 26.298, 11.563, 1.131, 0.018, 0.000, 0.000]` But for oscillatory classes the theoretical unconditional diagonals were tiny while the peak-conditioned empirical diagonals were large. For example:
- `F2` empirical diag: `[1.000, 18.568, 46.663, 39.282, 17.243, 1.463, 0.006, 0.000]`
- `F2` theoretical diag: `[1.000, 0.105, 0.016, 0.000, 0.000, 0.000, 0.000, 0.000]` - `F9` empirical diag: `[1.000, 11.764, 31.079, 23.244, 3.859, 0.108, 0.000, 0.000]`
- `F9` theoretical diag: `[1.000, 0.006, 0.006, 0.000, 0.000, 0.000, 0.000, 0.000]` - `F12` empirical diag: `[4.310, 79.996, 210.423, 139.753, 58.903, 5.265, 0.020, 0.000]`
- `F12` theoretical diag: `[4.310, 1.890, 0.074, 0.000, 0.000, 0.000, 0.000, 0.000]` A supplementary check on positive entries in log-log space also remained weak: Pearson \(r=0.4473\), corresponding to \(r^2=0.2001\) on 269 positive points. The final figure `Mjk_vs_Cjk_regression.png` shows the scatter of all 704 points colored by class, with diagonal entries marked separately and the global fit overlaid. The visual pattern agrees with the numerical result: a dense cloud with little global linear trend, plus a visible `F1` trend.
</results>
<challenges>
The main analytical challenge was coefficient reconstruction. Some classes were directly supported by saved artifacts (`coeffs_F9_a.npy`, `coeffs_F10_a.npy`, `a.npy` for `F12`), but others had to be rebuilt from specification. The largest methodological limitation is `F5p/F5m`: the project notes state that these classes require fitted effective Davenport-Heilbronn constants to reproduce stored peak magnitudes, but those fitted constants were not available on disk in this workspace. I therefore used the transparent approximation \(\kappa\pm0.05\), and I am explicitly reporting that approximation. A second issue is that the workspace did not include an explicit `coeffs_F12_N1e6.npz` file under that name; instead, the needed `F12` components were present as `a.npy`, `c.npy`, `rho0.npy`, and `description.npy`. I verified their contents and used `a.npy` directly. A third challenge was `F11`: no precomputed coefficient file was available, so I constructed the Sym² coefficients from the normalized Ramanujan coefficients using Euler-factor algebra and multiplicativity. This construction is mathematically standard, but because it was implemented from scratch in the notebook, it should be treated as an internally derived artifact rather than an externally validated download. Finally, the hypothesis itself compares a peak-conditioned statistic \(M_{jk}\) with an unconditional coefficient statistic \(C_{jk}\). The large mismatch in conditioning regime turned out to be the dominant scientific limitation of the proposed model, not a computational limitation.
</challenges>
<discussion>
The central result is negative: the unconditional coefficient cross-moment matrix does not generalize from the diagonal-only observation to the full peak-conditioned matrix across the 11-class panel. The failure is not marginal; the observed global \(R^2\) is 0.0135, which is essentially no explanatory power for the proposed linear model. Scientifically, the most plausible interpretation is that peak conditioning changes the relevant statistic. For oscillatory coefficient systems, the unconditional weighted sums
\[
T_j=\sum_{\omega(n)=j} a_n/n
\]
are often strongly canceled, so the resulting \(C_{jk}=\Re(T_j\overline{T_k})\) is near zero. But the empirical matrices are computed only at selected large peaks, where the corresponding stratified Dirichlet-polynomial components are atypically aligned and amplified. That conditioning can produce large empirical cross-terms even when the unconditional coefficient cross-moment is tiny. In other words, the off-diagonal peak geometry is not captured by the naive unconditional mean-value-theorem-scale statistic. The exception `F1` is informative rather than contradictory. Because \(a_n=1\) for zeta, there is no coefficient-level oscillatory cancellation, so the unconditional sums remain large and retain visible correspondence with the empirical peak-conditioned structure. This explains why the diagonal-only relationship may have looked promising in the zeta-dominated setting but does not survive extension to the full multi-class panel. This aligns with the methodological caveat already present in the project context: conditioning matters. The requested regression compares observables from fundamentally different probabilistic regimes. The negative result therefore weakens the idea that off-diagonal peak structure is directly encoded by unconditional coefficient cross-moments, and it suggests that any successful analytic theory will likely need a conditioned or large-deviation version of the coefficient statistic rather than the unconditional one.
</discussion>
<proposed-next-hypotheses>
1. A peak-conditioned theoretical statistic, replacing \(C_{jk}\) with a coefficient cross-moment weighted by large-value or resonance selection, will predict \(M_{jk}\) substantially better than the unconditional matrix and achieve higher out-of-class explanatory power.
2. After excluding `F1`, the empirical matrices \(M_{jk}\) are better explained by normalized shape statistics of the coefficient system (for example, row/column-normalized or spectrum-normalized cross-term matrices) than by raw unconditional moments \(C_{jk}\).
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>Mjk_Cjk_all_classes.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing the 11 empirical 8x8 matrices M_jk, the 11 theoretical 8x8 matrices C_jk, and the corresponding 8-entry T_j vectors used to factorize C_jk. It was created directly from the workspace S_k arrays and reconstructed coefficient arrays at N=10^6.</artifact-description>
</artifact>
<artifact>
<file-name>Mjk_Cjk_pairs.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Flattened table of all 704 class/pair observations used in the regression, with columns for class label, indices j and k, empirical M_jk, theoretical C_jk, diagonal indicator, fitted value, and residual. It was generated from the computed matrices in the notebook.</artifact-description>
</artifact>
<artifact>
<file-name>regression_summary.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Summary table of overall and per-class linear regression results, including slope, intercept, R^2, and Pearson correlation. It was exported from the notebook after fitting the global and class-specific models.</artifact-description>
</artifact>
</artifacts>
</output>
