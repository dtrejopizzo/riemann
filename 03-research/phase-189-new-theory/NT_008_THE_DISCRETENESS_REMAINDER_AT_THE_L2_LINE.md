# NT_008 — The integer-discreteness remainder ℛ₁ explicitly: ℛ₁(τ₀) = a₀ − 2Re(−ζ′/ζ)(3/2 + iτ₀) + O(√T₀ log(1/T₀)) on the
# spectral range |τ₀| ≤ C/T₀

Phase 189, construction step 8 (P189.1(a)). Notation of NT_005–007 (with errata). Labels as before.

## Corpus check
grep "Euler–Maclaurin" + "remainder", "discreteness", "sparse", "(−ζ′/ζ)(3/2", "ζ′/ζ(3/2)": hits — NT_004 Thm 4.2 (EM with Tate
zero integral), N_006 (integer-comb discrepancy O(1 + ‖F′‖²)), L2_028 §3 (resolution buys archimedean energy log(1/θ)), L2_029
(Near-free sets: local Euler symbols; the 3/2 abscissa does not appear). **New:** the evaluation of ℛ₁ on the curve; the identification of
its leading arithmetic term as the Div symbol shifted to abscissa 3/2 (height damping at σ = 1 gives n^{−1}·n^{−½}); the scale split
(sparse L ≲ 1/T₀ / Euler–Maclaurin L ≫ 1/T₀).

## 1. Statement
**Thm 8.1.** Fix C ≥ 1. There are T(C) > 0 and an absolute K such that for every admissible profile with T₀ ≤ T(C) and every |τ₀| ≤ C/T₀:
  ℛ₁(τ₀) = a₀ − 2Re(−ζ′/ζ)(3/2 + iτ₀) + E(τ₀),   |E(τ₀)| ≤ K C²√T₀ log(1/T₀).
More generally, for |σ − 1| ≤ ¼: ℛ_σ(τ₀) = a₀ − 2Re(−ζ′/ζ)(σ + ½ + iτ₀) + O(C²√T₀ log(1/T₀)) uniformly.
Consequently ℛ₁ ≥ a₀ − 2(−ζ′/ζ)(3/2) − o(1) ≥ a₀ − 3.02 (−ζ′/ζ(3/2) = 1.5052…, CITED value), which tends to +∞ as T₀ → 0 (NT_002 Lemma 2.6).

## 2. Proof (PROVED; bookkeeping routine)
By definition (NT_005 Thm 5.2), ζ(2σ)ℛ_σ = Σ_k k^{−s̄}[E^A_k(s) − Σ_nv_nE^c_{kn}(s)], s = σ + iτ₀. Split by the scale L (= k or kn) against
1/T₀; the c₀-window in x around L is [Le^{−2T₀}, Le^{2T₀}], of length ≤ 5T₀L.
(i) **Sparse scales L ≤ 1/(10T₀)**: the window contains no integer except possibly L itself. Hence
  E^c_L(s) = L^{−s}c₀(0) − L^{1−s}Ĉ(s) (L an integer, c₀(0) = 1),  |L^{1−s}Ĉ(s)| ≤ L^{1−σ}|F̂₀(z)|² ≤ L^{1−σ}·e^{2T₀|σ−1|}‖F₀‖₁² ≤ 3T₀L^{1−σ}.
  For A: Σ_m m^{−s}A(log m − log k) = k^{−s}a₀ + Σ_{m≠k}m^{−s}A(log(m/k)); for m ≠ k, d = |log(m/k)| ≥ log(1 + 1/k) ≥ 1/(2k) ≥ 5T₀, and
  (NT_002 Thm 2.5 Arch paragraph, now with 1 − e^{−2(d−2T₀)} ≥ d) |A(d)| ≤ 2T₀·2e^{−5(d−2T₀)/2}/d ≤ 8T₀k·e^{−5d/2}·e^{5T₀}; the m-sum is
  ≤ 8e T₀k·k^{−σ}Σ_{j≥1}(1 + j/k)^{−5/2−σ}… ≤ C₀T₀k^{2−σ}·(k^{−1}) = C₀T₀k^{1−σ}; and |k^{1−s}Â(s)| ≤ k^{1−σ}|m(z)||F̂₀(z)|² ≤ C T₀log(1/T₀)k^{1−σ}.
  Summing against k^{−σ}: diagonal Σ_{k≤1/(10T₀)}k^{−2σ}a₀ = ζ(2σ)a₀ − O(a₀T₀^{2σ−1}); comb diagonal
  Σ_{kn≤1/(10T₀)}k^{−2σ}v_nn^{−s} = ζ(2σ)·2Σ_nΛ(n)n^{−σ−½−iτ₀} − O(√T₀ log(1/T₀)) (tails Σ_{n>N}Λ(n)n^{−3/2} ≪ N^{−½}, Σ_{k>K}k^{−2σ} ≪ K^{1−2σ});
  the corrections Σ_{L≤1/(10T₀)}(k^{−σ}·T₀L^{1−σ}·log) with the divisor-weighted count Σ_{kn=L}k^{−σ}v_n ≤ L^{−σ}·2Σ_{n|L}Λ(n)n^{σ−½} ≪ L^{−½}log L
  give O(T₀·Σ_{L≤1/T₀}L^{1−σ−½}log L) = O(√T₀ log(1/T₀)) at σ = 1 (and uniformly for |σ − 1| ≤ ¼ up to a T₀^{¼}-loss absorbed in K… stated
  with √T₀ at σ = 1).
(ii) **Euler–Maclaurin scales L ≥ 10/T₀**: f(x) = x^{−s}c₀(log x − log L) has |f″| ≤ K L^{−σ−2}(|τ₀| + 1/T₀)² on a support of length ≤ 5T₀L,
  so |E^c_L| ≤ K L^{−σ−1}T₀(C/T₀ + 1/T₀)² ≤ K C²L^{−σ−1}/T₀. Weighted sum: Σ_{L≥10/T₀}(KC²/T₀)L^{−σ−1}·L^{−½}log L ≤ KC²√T₀log(1/T₀) at σ = 1.
  The A-defects at k ≥ 10/T₀ satisfy the same bound (A has the scale T₀ in log, decays like e^{−5|d|/2}).
(iii) **Transition 1/(10T₀) < L < 10/T₀**: both the sum and the integral are O(L^{−σ}(1 + T₀L)) per scale; weighted sum O(√T₀ log(1/T₀)).
Divide by ζ(2σ) and take real parts. ∎

## 3. Reading
At the ℓ² line, after the main term has absorbed the near-coincidences at all scales where ℕ looks continuous (L ≫ 1/T₀), the remainder is
**the archimedean energy a₀ minus the exact-coincidence (Div) symbol moved to abscissa 3/2** — the height damping H(n)^{−1} = n^{−1} has shifted
the local Euler factors from ½ to 3/2 — plus a small sparse-scale error. ℤ-integrality enters exactly here: the scales L ≲ 1/T₀ where the
c₀-window sees at most one integer. Note −2Re(−ζ′/ζ)(3/2 + iτ₀) ∈ [−3.02, 3.02]: bounded, Euler-product-exact, no near-coincidences.

## 4. Review
- (i): "no integer other than L in the window" needs 5T₀L < 1 ✓ for L ≤ 1/(10T₀). The A off-diagonal bound uses d ≥ 1/(2k) ≫ T₀, so the
  denominator 1 − e^{−2(d−2T₀)} ≥ d is valid for small T₀ ✓.
- (ii): the second-derivative bound uses |s| ≤ 1 + C/T₀ — this is why the theorem is restricted to |τ₀| ≤ C/T₀ (the range where F̂₀ has its mass).
  Outside that range the sparse/EM split must be replaced by a stationary-phase (Poisson-dual) analysis: NOT done here.
- The uniformity claim for |σ − 1| ≤ ¼ is stated with a weaker error; only σ = 1 is used below.
- No numerics beyond the CITED constant −ζ′/ζ(3/2) = 1.5052…. **No sign contact.**

## Erratum note (after NT_008_010_REVIEW)
§2(i): the A off-diagonal m-sum bound is O(T₀k^{1−σ}log k) (not T₀k^{1−σ}); totals unchanged up to a log. The uniform-in-σ clause
(|σ − 1| ≤ ¼) is restated with error O(C²T₀^{1/4}log(1/T₀)); only σ = 1 is used downstream.
