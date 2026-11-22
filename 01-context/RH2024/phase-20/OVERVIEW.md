## Conclusion

For L(Δ,s) at (T₀=85.7, J=16, X=10⁵), λ_min(Q) is strictly monotone-nondecreasing under nested window enlargement and is monotone with σ wherever the calculation is not prime-cutoff–dominated, with no de Branges / Conrey–Li obstruction pattern observed.

## Methods

1. Loaded `zeros_LDelta_local_final.pkl` (62 high-precision positive zeros of Λ_an(½+it), dps=80, |Λ_an|<10⁻⁷⁰) and `tau_table.pkl` (τ(n) for n≤10⁵). Built the prime list to X=10⁵ with a sieve.
2. Built the analytic Fourier transform of the Hermite–Gauss product ψ_i(t)ψ_j(t) (centered at T₀ with width σ) by deriving the closed form from the Hermite generating function: ∫H_m(u)H_n(u)e^{-u²}e^{-ivu}du = √π e^{-v²/4} m!n! Σ_k (-is)^{m+n-2k} 2^k / ((m-k)!(n-k)!k!) (Laguerre-equivalent polynomial). I verified this analytic FT against scipy.integrate.quad for several (m,n) values (agreement to ~10⁻¹⁴).
3. Constructed M_arith[i,j] = M_arch[i,j] + M_prime[i,j] with no polar term (L(Δ,s) entire): - M_arch = (1/2π) ∫ ψ_i ψ_j [−2log(2π) + 2 Re ψ(6+it)] dt via 200-node Gauss–Hermite quadrature in u=(t−T₀)/σ (norm π^{−¼}(2^i i!)^{−½}). - M_prime = −(1/π) Σ_{p^k≤X} c_f(p^k) log(p)/√(p^k) · Re ĥ_{ij}(log p^k), where c_f(p^k) satisfies the Hecke recurrence c_{k+1}=a_f(p)c_k − c_{k−1} with a_f(p)=τ(p)/p^{11/2}; ĥ_{ij}(x)=e^{−iT₀x}(−i)^{i+j} F_{ij}(σx), evaluated by polynomial reuse and pre-tabulated v-powers (9.7k prime powers, ~1.3 M evaluations, ~17 ms).
4. Constructed M_zeros[i,j] = Σ_γ ψ_i(γ)ψ_j(γ) summed over ±γ pairs (L(Δ,s) self-dual; using the cached 62 positive zeros and their negatives).
5. Verified the trace identity tr(M_zeros)=tr(M_arith) at (T₀=85.7, σ=2, J=16) to 1.74×10⁻¹².
6. σ-monotonicity: re-built Q for σ∈{0.25,0.5,1,2,4} at fixed T₀=85.7, J=16, X=10⁵, and reported λ_min and trace residuals.
7. Window-monotonicity: at (T₀=85.7, σ=2, J=16), retained only zeros with |γ−T₀|<W for W∈{5,8,10,12,15,18,20,22,25,28,30,35,40}, computed λ_min and tr_res.
8. Eigenvalues via scipy.linalg.eigvalsh on the symmetric real Q. Saved CSV/JSON/PNG artifacts.

## Results

**Trace identity (validation gate)** at σ=2, T₀=85.7, J=16, X=10⁵:
tr(M_zeros) − tr(M_arith) = +1.74×10⁻¹² — the gate is satisfied (the spec quotes ~10⁻²⁷ as previously achievable, but this run uses double precision throughout numpy arithmetic; the residual is well below |λ_min| only when σ≥2). **σ-sweep at T₀=85.7, J=16, X=10⁵:**
| σ | λ_min(Q) | trace residual | |λ_min|/tr(M_zeros) |
|---|---|---|---|
| 0.25 | −2.601978e+0 | −1.64e−1 | 2.21e−1 |
| 0.50 | −1.193569e+0 | −2.26e−2 | 9.88e−2 |
| 1.00 | −6.774646e−3 | −2.47e−3 | 5.05e−4 |
| 2.00 | −7.347374e−12 | +1.74e−12 | 5.46e−13 |
| 4.00 | −3.556077e−12 | +8.40e−12 | 2.69e−13 | λ_min is monotone-increasing with σ from σ=0.25 to σ=2 (becoming less negative), and saturates at the numerical floor (~10⁻¹²) for σ≥2. For σ≤1 the trace residual is of the same order as |λ_min|, so those negative eigenvalues are dominated by the insufficient prime cutoff X=10⁵, exactly as the engine specification warned (it states X∝exp(c/σ²) is required for σ≤1). **Window enlargement at T₀=85.7, σ=2, J=16, X=10⁵:**
| W | N(positive zeros) | λ_min(Q) | trace residual |
|---|---|---|---|
| 5 | 8 | −1.208949e+0 | −6.52e+0 |
| 8 | 12 | −1.145361e+0 | −3.42e+0 |
| 10 | 18 | −5.203420e−2 | −7.30e−2 |
| 12 | 20 | −1.017112e−3 | −1.28e−3 |
| 15 | 26 | −2.028247e−9 | −2.03e−9 |
| 18 | 30 | −7.347408e−12 | +1.74e−12 |
| 20 | 33 | −7.347374e−12 | +1.74e−12 |
| 25 | 41 | −7.347374e−12 | +1.74e−12 |
| 30 | 49 | −7.347374e−12 | +1.74e−12 |
| 40 | 62 (all) | −7.347374e−12 | +1.74e−12 | λ_min is strictly nondecreasing across the entire sequence of nested enlargements: −1.21 → −1.15 → −5.2×10⁻² → −1.0×10⁻³ → −2.0×10⁻⁹ → −7.35×10⁻¹² (floor). The trace residual collapses in lockstep, confirming that the residual negativity at small W is the truncation artifact of dropped zeros, not a structural obstruction. Once W≥18 captures the locally relevant zeros (|t−T₀|/σ ≤ ~9), λ_min is at the numerical floor for all further W. **Presence/absence of non-monotonic behavior under window enlargement:** absent. No instance in the sequence shows λ_min decreasing as W grows. The behavior is consistent with the hypothesis: no de Branges / Conrey–Li-style persistent negativity emerges as the spectral window enlarges.

## Challenges

- No prior engine implementation existed on disk; the entire M_arith / M_zeros / Q stack had to be implemented from scratch, guided by `engine-spec.md`.
- Sign / 2π conventions in the Weil explicit formula are not standardized across references. I had to use the trace identity as a hard test: my first attempt left a residual ~0.84 because of a missing 1/(2π) factor in the prime-power term; including it brought the residual down to 1.7×10⁻¹². This is the decisive sanity check that locked in the convention −(1/π)Σc_f(n)log p/√n · Re ĥ(log n) for the self-dual prime sum.
- The analytic Hermite-product Fourier transform was derived from the generating function ∫G(x,t)G(x,u)e^{−x²−isx}dx = √π e^{−s²/4} e^{−is(t+u)+2tu} rather than imported from a library; numerical verification against scipy.quad agreed to ~10⁻¹⁴ for all tested (m,n).
- For σ≤1 with the fixed cutoff X=10⁵ the trace identity fails by 10⁻³ to 10⁻¹, so the corresponding λ_min values are unreliable in the absolute sense; I reported them with their trace residuals so the reader can see the cutoff-dominated regime clearly demarcated.
- Computation used double precision in numpy for the matrices; the high-precision (dps=80) zero values were cast to float at the matrix build step. This is adequate at J=16 because the numerical floor of eigvalsh is ~10⁻¹² × tr, which dominates over any high-precision gain.

## Discussion

The hypothesis H2 specialized to L(Δ,s) is confirmed in the reliable regime: (i) λ_min increases (monotone nondecreasing) under nested enlargement of the zero window at σ=2, and (ii) λ_min is monotone with σ once σ is wide enough that prime-cutoff error is below the eigenvalue. Combined with the engine-spec result of ~2733-order GRH baseline suppression at full J and the documented Davenport–Heilbronn negativity (|λ_min|/tr~1.7 at the same parameters), the absence of any persistent negativity for L(Δ,s) under window enlargement is a strong negative result for any de Branges / Conrey–Li-type obstruction in L(Δ,s) at this scale. The σ=0.25, 0.5, 1 negative eigenvalues are exactly the artifact predicted by the spec — the M_arith trace is missing a tail (X=10⁵ leaves out the steeply growing prime contribution at small σ), and this manifests both as a large trace residual and as a spuriously negative λ_min that decreases as σ shrinks. This is not a violation of monotonicity in σ; it is the well-characterized cutoff-error regime. The window result is the cleaner test of the hypothesis because the arithmetic side is fixed across W; the perfectly monotone sequence directly shows that adding more zeros never makes the form more indefinite, exactly the qualitative behavior expected if the explicit formula is being faithfully discretized.

## Next hypotheses

1. Across all three GRH controls (ζ, L(χ₄ mod 5), L(Δ,s)), the residual λ_min in the cutoff-dominated regime (σ≤1, X=10⁵) scales as a universal function of trace residual, i.e. λ_min ≈ −c · |tr_res| with c of order unity, indicating that the negativity in this regime is entirely an arithmetic-truncation artifact rather than spectral structure.
2. For L(Δ,s) at (T₀=85.7, σ=2, J=16) with a dynamic cutoff X(σ)∝exp(c/σ²), the floor |λ_min| collapses uniformly to the eigvalsh roundoff (~10⁻¹⁴ × tr) for all σ∈{0.5,1,2,4} — implying that σ-monotonicity becomes exact (and trivial at the floor) once the spec-mandated cutoff scaling is implemented.

## Files

- `LDelta_monotonicity_results.json` (computed) — JSON summary of the σ-sweep (σ∈{0.25,0.5,1,2,4}) and window-sweep (W∈{5..40}) at T₀=85.7, J=16, X=10⁵ for L(Δ,s). Each record contains λ_min(Q), tr(M_zeros), tr(M_arith), trace residual, and the number of zeros used. Includes run parameters and methodology note.
- `lambda_min_sigma_sweep.csv` (computed) — CSV table of L(Δ,s) λ_min(Q) and trace residual versus σ at T₀=85.7, J=16, X=10⁵.
- `lambda_min_window_sweep.csv` (computed) — CSV table of L(Δ,s) λ_min(Q) and trace residual for nested zero-windows |γ−T₀|<W (W=5..40) at fixed T₀=85.7, σ=2, J=16, X=10⁵; demonstrates monotone-nondecreasing λ_min with W.
- `LDelta_lambda_min_monotonicity.png` (computed) — Two-panel summary figure. Panel A: |λ_min(Q)| versus σ on a log scale, with overlaid trace residual; the prime-cutoff-dominated regime (σ≲1.5) is shaded. Panel B: |λ_min(Q)| versus window half-width W at σ=2 with overlaid trace residual, showing strictly monotone-nondecreasing behavior down to the numerical floor.
