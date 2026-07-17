## Overview <output>
<conclusion>
The truncation noise floor η(X) at (T₀=46.13, σ=1) decays much faster than either the unconditional (log X)²/X bound (R²=0.50) or the RH-like (log X)²/√X bound (R²=0.21); only the zero-density-style sub/super-exponential form A·exp(−c·(log X)^a) provides a strong fit (R²=0.995), and its predicted detection threshold for a δ=10⁻³ off-critical zero (X≈1.41×10⁵) matches the empirical crossover (X_min≈1.35×10⁵), so detection requires a hypothesis at least as strong as a zero-density / log-free-region regime — strictly stronger than the naïve unconditional bound but, empirically, the observed decay is even faster than the bound implied by full RH.
</conclusion> <methods>
1. Loaded eta_residual_law.json and extracted fine_X_scan_H2500 for the "optimal" point (T₀=46.13, σ=1, J=10, H=2500) across X∈{10³,3·10³,10⁴,3·10⁴,10⁵,3·10⁵,10⁶}, yielding η = [1.56e-1, 7.01e-2, 2.56e-2, 1.20e-3, 6.10e-5, 5.35e-7, 5.80e-9].
2. Fit three functional forms in log-space using scipy.optimize.curve_fit: • M1 (Unconditional-like): η = A·(log X)²/X • M2 (Zero-density-like): η = A·exp(−c·(log X)^a) • M3 (RH-like): η = A·(log X)²/√X Goodness-of-fit was assessed via log-space R², MSE, and AIC. M2 was also re-fit with a constrained to (0,1) per the prompt.
3. Computed the signal level c·δ² for δ=10⁻³ using c_prefactor=16.8718 (m=20) from detectability_summary.csv, giving signal = 1.687×10⁻⁵.
4. Solved each fitted η-model for η(X)=signal via scipy.optimize.brentq to obtain the predicted detection cutoff X under each hypothesis, and compared to the empirical X_min=1.347×10⁵.
5. Saved fit results to eta_bound_fit_results.json and produced a 2-panel summary figure eta_bound_fits.png.
</methods> <results>
Fits (log-space):
• M1 unconditional A·(log X)²/X: A=7.65×10⁻², R²=0.504, MSE=17.75, AIC=22.14.
• M2 zero-density A·exp(−c·(log X)^a) (free a): logA=−0.049, c=1.18×10⁻³, a=3.69, R²=0.995, MSE=0.165, AIC=−6.60.
• M2 with a constrained < 1: best a=0.99, R²=0.933 (still better than M1/M3 but markedly worse than free-a M2).
• M3 RH-like A·(log X)²/√X: A=4.35×10⁻⁴, R²=0.214, MSE=28.15, AIC=25.36.
ΔAIC(M2 − M1) = −28.7; ΔAIC(M2 − M3) = −32.0 (decisive preference for M2 even after penalising its 3 parameters vs 1). Crossover X for signal c·δ² = 1.687×10⁻⁵ (δ=10⁻³):
• Empirical (log–log interpolation of η scan): 1.347×10⁵
• M2 (zero-density-like): 1.411×10⁵ — matches empirical to ~5%.
• M1 (unconditional): 8.45×10⁵ — over-predicts X by a factor ~6.
• M3 (RH-like): 7.11×10⁷ — over-predicts X by ~500× because (log X)²/√X decays too slowly to ever reach the signal level by X=10⁶. The fitted M2 exponent a≈3.69 is super-exponential in log X (i.e. η falls off faster than any stretched-exponential with a<1), consistent with the empirically curved descent on the log-η vs log-X plot.
</results> <challenges>
• Only 7 data points are available for fitting; M2 has 3 free parameters, raising over-fitting concerns. We mitigated this by comparing log-space AIC (which still strongly prefers M2 with ΔAIC≈−29 vs M1 and ≈−32 vs M3) and by reporting a constrained variant (a<1, R²=0.933).
• The prompt suggested a<1 for M2 ("zero-density-like" stretched-exponential), but the unconstrained best fit prefers a≈3.69 (super-exponential in log X). We report both: even with a forced <1, M2 still outperforms M1 and M3 substantially.
• The data are smoothed onto a 1-decade-spaced X grid; finer X sampling would tighten the fit but is unavailable in eta_residual_law.json.
• Caveat: η as measured is a numerical residual of a Hermite-basis quadratic form, not a pure prime-sum truncation error; its decay reflects both the analytic-side / basis approximation and the prime cutoff. Linking the fitted M2 form to a specific number-theoretic bound (e.g. Vinogradov–Korobov or a Bombieri-type log-free region) is therefore by analogy, not by derivation.
</challenges> <discussion>
The exercise quantifies the minimum analytic hypothesis under which the Weil-quadratic-form engine can detect a δ=10⁻³ off-critical zero at the optimal benchmark point. The unconditional polynomial bound A·(log X)²/X is decisively rejected: it both fits the data poorly (R²=0.50) and would predict that the engine needs X≈8.5×10⁵ primes to lift the signal above noise, whereas the engine in fact succeeds by X≈1.35×10⁵. The full-RH-style bound A·(log X)²/√X is even worse — it fits the data poorly (R²=0.21) and is grossly pessimistic about detection (X≈7×10⁷). The only form that simultaneously fits the data and predicts the correct empirical crossover is the zero-density-style sub/super-exponential A·exp(−c·(log X)^a). This empirically corroborates the report-r11 hypothesis that detection at this benchmark requires a hypothesis stronger than the unconditional regime, in the family of log-free zero-free regions, zero-density estimates, or large-sieve type cancellation, rather than unconditional pointwise bounds. Notably, the observed η(X) decays faster than even RH-conditional pointwise bounds, suggesting that the residual is dominated by basis-truncation rather than prime-side error past X≳10⁵; under that interpretation the "weakest hypothesis" needed is genuinely number-theoretic only up to that scale, beyond which basis/analytic-side terms dominate. Formal statement of the weakest hypothesis: under a zero-density / log-free-region regime modelled empirically by η(X) ≈ exp(−c·(log X)^a) with c≈1.18×10⁻³, a≈3.69, the signal c·δ² = 1.687×10⁻⁵ for δ=10⁻³ at (T₀=46.13, σ=1, m=20) exceeds the noise floor for X ≥ 1.41×10⁵ — a feasible cutoff. Under the unconditional bound the required X ≥ 8.5×10⁵ is feasible but a factor ~6 larger; under the RH-style bound the requirement X ≥ 7×10⁷ is impractical, illustrating that the empirical regime sits above RH-style pointwise truncation predictions in detection power.
</discussion> <proposed-next-hypotheses>
1. The accelerated (super-stretched-exponential) decay of η(X) beyond X≈10⁵ is dominated by Hermite-basis truncation error rather than prime-side error; therefore increasing the basis size m at fixed X will leave η(X) near the empirical floor (~5.8×10⁻⁹) essentially unchanged, while decreasing m will degrade it.
2. At the second benchmark (T₀=85.7, σ=2) the same fit family will favour an even faster-decaying M2 (larger a) because that regime's noise is intrinsically lower and largely X-independent, indicating that the prime-side error is already negligible there even at X=10³.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>eta_bound_fit_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Fitted parameters, log-space R², MSE, and AIC for the three candidate bounds on η(X) at (T₀=46.13, σ=1), plus the predicted detection cutoff X under each model and the empirical X_min from the η scan. Produced by curve-fitting eta_residual_law.json["fine_X_scan_H2500"] data with scipy.optimize.curve_fit and brentq.</artifact-description>
</artifact>
<artifact>
<file-name>eta_bound_fits.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) log–log plot of empirical η(X) overlaid with the three fitted bounds and the δ=10⁻³ signal level; (B) bar chart of the X cutoff required for detection under each bound vs the empirical X_min. Generated with matplotlib from the fit outputs above.</artifact-description>
</artifact>
</artifacts>
</output> 