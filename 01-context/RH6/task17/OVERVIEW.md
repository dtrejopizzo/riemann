## Overview <output>
<conclusion>
The hypothesis is confirmed: a from-scratch `cypari2` computation with periodic checkpointing successfully produced a complete, contiguous, strictly monotonic list of the first 5,000 non-trivial zeros of L(s, χ) for the primitive odd Dirichlet character mod 5 with χ(2)=i (LMFDB 5.c.a), saved as `lchi_zeros_5000_dps50.npy`.
</conclusion> <methods>
1. Installed `cypari2` (v2.2.4 wrapping PARI/GP 2.17.2) and set PARI real precision to 50 decimal places (`pari.set_real_precision(50)`).
2. Constructed the target character in PARI: `G = znstar(5,1)` (generator g=2, order 4) and `chi = [G, [1]]`, corresponding to χ(2) = exp(2πi/4) = i. Built the L-function with `L = lfuncreate(chi)`. Validated against the partial file: the first three zeros (6.18357…, 8.45722…, 12.67494…) match exactly.
3. Iterated `lfunzeros(L, [T_lo, T_hi])` in chunks (length 200 at low T, automatically subdivided when the PARI stack overflowed, and reduced to length 100 for T≥3700 where evaluation slows). After the initial 8 MB stack overflow at T≈1400, allocated up to 1 GB (`pari.allocatemem(0, 1<<30)`).
4. Since `lfunzeros` **includes the lower endpoint**, deduplicated chunk boundaries by tracking the last accepted zero in `mpmath.mpf` (60 dps) and skipping any new value ≤ last + 1e-30.
5. Wrote checkpoint `lchi_zeros_checkpoint.npy` whenever the count crossed a multiple of 500.
6. Verification: confirmed length = 5000, all 5,000 values unique, strictly monotonic (`diff > 0` for all 4,999 consecutive pairs), and cross-validated against the legacy partial file in the overlap region T∈[2500, 4391.58] (2,380/2,380 string-identical matches) and the low-T region T∈(0, 212] (139/139 zeros agree to ≥45 decimals; only the last 1–3 digits drift, max difference 1.2×10⁻⁴⁵).
7. Saved as `lchi_zeros_5000_dps50.npy` (`numpy` array of decimal strings, dtype='<U51', shape=(5000,)). Generated a 2-panel summary figure (counting function vs. Riemann–von Mangoldt prediction; normalized nearest-neighbor gap distribution).
</methods> <results>
- Number of zeros: 5000 (exactly).
- Range: T₁ = 6.1835781954508539143775173097086925259215005792280, T₅₀₀₀ = 4391.5822107025899588087809855969874623992084609392.
- Strictly monotonic: True (all 4,999 consecutive differences positive); all 5,000 values distinct.
- Smallest gap: 0.0727; largest gap: 4.2177.
- Counting function tracks the Riemann–von Mangoldt prediction N(T) ≈ (T/2π) log(qT/(2πe)) with q=5 essentially indistinguishably on the plot (Panel A).
- Mean normalized nearest-neighbor spacing ⟨(t_{n+1}−t_n)·ρ(t_n)⟩ = 1.001, consistent with the expected unfolded mean of 1.
- Cross-validation against legacy `lchi_zeros_partial_dps50.npy`: 2,380/2,380 exact string matches in T∈[2500, 4391.58]; 139 low-T zeros agree to ≥45 decimal places (max |Δ| = 1.2×10⁻⁴⁵, within last-digit rounding noise of the 50-dp computation).
- Generation wall-clock: roughly 25–30 min effective CPU; chunk speed scaled with T (≈0.4 s/200T at T≈0, ≈53 s/100T at T≈3700).
</results> <challenges>
- **PARI stack overflow**: The default 8 MB PARI stack overflowed during `lfunzeros` around T=1400. Resolved with `pari.allocatemem(0, 1<<30)` (1 GB cap). Also added an automatic subdivision-on-error fallback for robustness.
- **Notebook cell 900 s timeout**: Long single-cell loops were truncated by the kernel's 900-second cell timeout. Resolved by splitting the computation across cells and continuing from the in-memory `zeros_list` / `T` state, plus on-disk checkpoints every 500 zeros.
- **Boundary duplicates**: `lfunzeros([T_lo, T_hi])` is inclusive at the lower endpoint, so naively concatenating chunks would double-count zeros at chunk boundaries. Handled by tracking the last accepted zero in mpmath and rejecting any new value within 10⁻³⁰ of it.
- **Variable naming**: PARI rejects identifiers beginning with underscore; used `zlist` instead of `_zs`.
- **Precision noise vs. partial file**: The two computations differ by ≤10⁻⁴⁵ in the last few digits of some low-T zeros. This is sub-precision rounding noise, not an analytical disagreement, but it means the new file is not byte-identical to the partial file's overlap region — it should be considered the canonical, clean 50-dps list going forward.
</challenges> <discussion>
The clean, contiguous list of the first 5,000 zeros of the Dirichlet L-function L(s, χ₅.c.a) eliminates the data-integrity gap identified in report r5 and brings this L-function to parity with the ζ (5000 zeros) and L(Δ) (2000 zeros) datasets. All 5,000 zeros lie on the critical line at the working precision of 50 dps, consistent with the Riemann Hypothesis for this Dirichlet L-function in the range T ∈ (0, 4392]. The empirical counting function matches the Riemann–von Mangoldt main term to within plotting resolution, and the normalized nearest-neighbor spacing distribution has mean 1.001 with a shape qualitatively consistent with GUE (Montgomery–Dyson) statistics — though a formal pair-correlation comparison is left for follow-up. With this file in place, downstream analyses (Weil quadratic form, ω-class moment decompositions, cross-L-function spectral comparisons) that previously had to work around the gap in (212, 2500) can now use the canonical first-5000-zeros truncation for L(χ₅.c.a).
</discussion> <proposed-next-hypotheses>
1. The normalized pair-correlation function R₂(x) of the first 5,000 zeros of L(χ₅.c.a), computed in the range T ∈ [200, 4000] to avoid edge effects, agrees with the GUE prediction 1 − (sin πx / πx)² to within Kolmogorov–Smirnov statistical fluctuations expected from a sample of ~4000 unfolded zeros.
2. Substituting the new contiguous 5,000-zero list into the Weil explicit-formula quadratic form centered at heights T ∈ {500, 1500, 2500, 3500} yields strictly positive values for every smooth, compactly-supported test function in a Gaussian/Hermite test bank, providing additional numerical evidence consistent with RH for L(χ₅.c.a).
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>lchi_zeros_5000_dps50.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Numpy array (shape (5000,), dtype '&lt;U51') of 50-decimal-place string representations of the imaginary parts of the first 5,000 non-trivial zeros of the Dirichlet L-function L(s, χ) where χ is the primitive odd character mod 5 with χ(2)=i (LMFDB 5.c.a). Generated from scratch with cypari2 / PARI-GP 2.17.2 at real precision 50, using lfunzeros over chunks of length 100–200, with boundary-duplicate removal via mpmath. Verified to contain exactly 5,000 distinct, strictly increasing values spanning T∈(0, 4391.58]; cross-validated against the legacy partial file (2,380/2,380 string-identical matches in the overlap region).</artifact-description>
</artifact>
<artifact>
<file-name>lchi_zeros_checkpoint.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Intermediate checkpoint file written every 500 zeros during the from-scratch generation; final checkpoint state matches the canonical 5,000-zero list. Same dtype/format as the final file. Kept as a recovery artifact.</artifact-description>
</artifact>
</artifacts>
</output>
