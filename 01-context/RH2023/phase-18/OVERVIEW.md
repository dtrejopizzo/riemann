## Conclusion

The Front A signal model (c_pred·δ²) and Front B noise model (η_theory(X)) successfully integrate into a Detector Feasibility Table that quantitatively guides the Weil-quadratic-form off-critical-zero detector across (T₀,σ,J,m,δ).

## Methods

1. Loaded `c_pred_vs_c_emp_grid.csv` (60 rows, R²=1.0000) and `frontC_theory_vs_empirical.json` (T₀=46.13, σ=1, J=10 noise data).
2. Resolved a J-convention mismatch: the c_pred grid is tabulated only at J∈{4,8,12,16,20}, but the canonical parameter points use J=10. Estimated c_pred(σ,J=10,m=20) by linear interpolation between J=8 and J=12: c_pred(σ=1)=−16.872, c_pred(σ=2)=−3.633.
3. Re-implemented the closed-form Hermite–Gauss/PNT noise bound from the JSON's `formula` field using `scipy.special.eval_genlaguerre`, building g_ij(u)=(−i)^(i+j)·exp(−ω²/4)·√(min!/max!)·(ω/√2)^|i−j|·L_min^|i−j|(ω²/2) with ω=σu, and integrating (2/π)∫_{logX}^∞ exp(u/2)·‖g(u)‖₂ du. Operator norm computed by SVD via numpy. Verified against frontC values: e.g. at X=10³,10⁴,10⁵,10⁶, computed η=32.90, 2.71, 4.31e−3, 1.85e−7 vs. stored 32.83, 2.70, 4.30e−3, 1.77e−7 (agreement to <5%, within quadrature tolerance). T₀ enters only as an overall phase and does not change the spectral norm of g(u); the model is therefore extensible to T₀=85.7 by simply changing σ.
4. For each of (δ=10⁻³,10⁻⁴,10⁻⁵) and m=20, computed Signal=|c_pred|·δ² and Noise η_theory at X=10⁶. Solved η_theory(X)=Signal by `scipy.optimize.brentq` on log X.
5. Saved the seven-column table as `detector_feasibility_summary.csv` and produced a 2-panel summary figure (`detector_feasibility_summary.png`) showing (A) noise η(X) curves with signal thresholds for both parameter points, and (B) X_min bars.

## Results

Detector Feasibility Table (m=20, J=10 via interpolation between J=8 and J=12 from the c_pred grid): | T₀ | σ | J | m | δ | c_pred | Signal \|λ_min\| | Noise η(X=10⁶) | X_min for Detection | SNR @ X=10⁶ |
|---|---|---|---|---|---|---|---|---|---|
| 46.13 | 1 | 10 | 20 | 10⁻³ | −16.87 | 1.69e−5 | 1.85e−7 | 3.91e+05 | 91.0 |
| 46.13 | 1 | 10 | 20 | 10⁻⁴ | −16.87 | 1.69e−7 | 1.85e−7 | 1.02e+06 | 0.91 |
| 46.13 | 1 | 10 | 20 | 10⁻⁵ | −16.87 | 1.69e−9 | 1.85e−7 | 2.41e+06 | 9.1e−3 |
| 85.70 | 2 | 10 | 20 | 10⁻³ | −3.633 | 3.63e−6 | 1.24e−64 | 4.80e+02 | 2.9e+58 |
| 85.70 | 2 | 10 | 20 | 10⁻⁴ | −3.633 | 3.63e−8 | 1.24e−64 | 7.81e+02 | 2.9e+56 |
| 85.70 | 2 | 10 | 20 | 10⁻⁵ | −3.633 | 3.63e−10 | 1.24e−64 | 1.21e+03 | 2.9e+54 | Key observations: (i) For T₀=46.13 (σ=1), δ=10⁻³ is detectable already at X≈4×10⁵; δ=10⁻⁴ requires the full X≈10⁶ benchmark (SNR≈1 at X=10⁶, consistent with the documented δ²-vs-noise crossover); δ=10⁻⁵ needs X≈2.4×10⁶. (ii) For T₀=85.7 with σ=2 the noise floor decays super-rapidly with X (η(10⁶)≈10⁻⁶⁴), so even δ=10⁻⁵ is detected by X≈1.2×10³ primes — the σ=2 basis essentially eliminates truncation noise within the practical range. (iii) The two parameter points illustrate a strong σ-dependence: doubling σ trades a factor ~4–5 in |c_pred| (signal) for many orders of magnitude in η (noise), making P2 far easier to detect at small δ.

## Challenges

1. J-convention mismatch: c_pred_vs_c_emp_grid.csv only tabulates J∈{4,8,12,16,20}; canonical parameter points use J=10. Resolved via linear interpolation in J between J=8 and J=12 at m=20; c_pred is approximately linear in J in this range. This introduces interpolation uncertainty (∼5–10%) that is small compared to the orders-of-magnitude signal/noise differences in the table.
2. The σ=2 noise floor at X=10⁶ is numerically near-zero (∼10⁻⁶⁴); the brentq search must use a wide log-X bracket. The Gaussian factor exp(−ω²/4)=exp(−σ²u²/4) drives the integrand to underflow rapidly, producing only minor quadrature warnings handled by scipy.
3. The c_pred grid uses m∈{1,5,20}; we used m=20 per the objective. For m=1, c_pred=0 in nearly all rows (the rank-2 operator is degenerate), so the table is meaningful only at m=20.
4. The frontC JSON only directly provides noise data for P1; for P2 we relied on the validated closed-form formula. The T₀-independence of ‖g(u)‖₂ was used to justify this extrapolation.

## Discussion

The table operationalizes the project's two key theoretical advances: (1) Front A's prediction that the off-critical-zero signature in the Weil quadratic form scales as |λ_min|≈c·δ² with c given by the minimum eigenvalue of a sum of rank-2 localized operators, and (2) Front B's closed-form PNT/Hermite-Gauss noise bound η_theory(X). The intersection of these two curves yields a practical X_min, and the SNR column tells an experimenter immediately whether a candidate (T₀,σ,δ) combination is above the noise floor at the standard X=10⁶ benchmark. The σ=1 point at δ=10⁻⁴ sits right at the SNR=1 boundary (consistent with the project's stated δ²-vs-η crossover analysis), while σ=2 confers a massive noise advantage at the cost of some signal. The table thus provides quantitative guidance for choosing basis width σ when targeting a specific minimum δ.

## Next hypotheses

1. There exists an optimal σ*(δ,T₀) that minimizes X_min for detection, defined by the balance ∂_σ[|c_pred(σ)|·δ²/η_theory(X,σ)]=0; for the canonical δ∼10⁻⁵ regime this optimum is hypothesized to lie in σ∈[1.3, 1.8].
2. The empirical noise floor's geometric undershoot (factor ∼108×) below η_theory is structural rather than random, and applying the empirical-fit free-p parameters (A=−0.049, c=0.00119, p=3.689) instead of the theoretical bound would reduce X_min for σ=1,δ=10⁻⁴ by roughly 1.5–2× without compromising detection guarantees.

## Files

- `detector_feasibility_summary.csv` (computed) — Final Detector Feasibility Table integrating Front A signal model (c_pred·δ², with c_pred at J=10 interpolated between J=8 and J=12 from c_pred_vs_c_emp_grid.csv) with Front B noise model (η_theory(X) computed from the closed-form Hermite-Gauss/PNT bound in frontC_theory_vs_empirical.json). Six rows covering (T₀=46.13,σ=1) and (T₀=85.7,σ=2) at J=10, m=20, and δ∈{10⁻³,10⁻⁴,10⁻⁵}, with columns: T0, sigma, J, m, delta, c_pred, Signal_abs_lambda_min, Noise_eta_X1e6, X_min_for_Detection, SNR_at_X1e6. X_min computed by brentq root-finding on η_theory(X)=Signal.
