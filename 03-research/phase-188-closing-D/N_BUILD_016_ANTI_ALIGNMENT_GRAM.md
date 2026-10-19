# N_BUILD_016 — The anti-alignment inequality: (b) the s-derivative route is a commuting-multiplier tautology (NO-GO); (a) an exact three-vector Gram decomposition with a ℤ-additive centre

Pen and paper. F ∈ P_T real; N = e^{2T}; shifts (τ_aF)(t) = F(t−a) on L²(ℝ). Following L2_BUILD_017:
U_s := Σ_{n<N} n^{−s}τ_{−log n} (integer comb), U_1 := U_{½}, U_μ := Σ_{d<N} μ(d)d^{−½}τ_{log d}, U_log := Σ_{m<N}(log m)m^{−½}τ_{−log m}
= −∂_sU_s|_{½}. Comb pairing (L2_017 Lemma 1): Σ_{n<N} v_n Re c_F(log n) = 2Re⟨U_μF, U_logF⟩. Target on the archimedean-negative
space: 2Re⟨U_μF, U_logF⟩ ≤ 𝔞_∞(F) (= (N_loc), L2_006).

## Corpus check
L2_BUILD_017 (operator form; modulus-type splitting certificates: class empty for T ≥ 0.60; lesson "need a lower bound / anti-alignment"),
R162_903 (Gram of Möbius images ACROSS windows: Cauchy–Binet/Moore collapse; Perron + |μ| ≤ 1 gives only |Z^{−1}F| ≤ Z|F|), N_BUILD_005
(𝔄_T; comb = −∂_s log Z), N_BUILD_006 (Möbius-transported test). grep "U_1|log U_s|∂_s log‖|three-vector Gram|angle between U_μ":
none at a single window. New: §1 (NO-GO with explicit tests), §2 (Gram identity with ℤ-additive centre), §3.

## 1. Route (b): −∂_s log of the operator family — NO-GO (PROVED)
(i) All operators here are functions of the generator D = −i d/dt: τ_a = e^{−iaD}. So U_s, U_μ, U_log are Fourier multipliers with
symbols ζ_N(s + iτ) := Σ_{n<N}n^{−s−iτ}, M_N(½ + iτ) := Σ_{d<N} μ(d)d^{−½+iτ}... (conventions aside), −∂_sζ_N; they commute, and modulo
lags ≥ 2T (invisible to F ∈ L²(I_T)) U_μ^*U_1 ≡ I and U_μ^*U_log ≡ U_Λ (μ*1 = δ, μ*log = Λ; nm ≥ N gives shifts ≥ 2T).
So "−∂_s log U_s" is the multiplier −(ζ′/ζ)_N compressed to I_T — exactly the comb form; the operator-family route adds no structure.
(ii) Monotonicity/convexity in s fails. Q(s) := Re⟨F, (−∂_s log U_s)F⟩ = Σ_{n<N}Λ(n)n^{−s}Re c_F(log n) (exact mod high lags).
Q′(s) = −Σ Λ(n)(log n)n^{−s}Re c_F(log n), Q″(s) = Σ Λ(n)(log n)²n^{−s}Re c_F(log n). Two-bump tests F_± = φ ± τ_{log 2}φ (φ narrow,
φ̂(±i/2) = 0; N_BUILD_007 §1(iv)) have Re c_{F_±}(log 2) = ±1 and Re c_{F_±}(log n) = 0 for n ≠ 2 (bumps narrower than the gap to log 3):
Q, Q′, Q″ take both signs on P_T. No monotonicity or convexity in s holds as a form inequality. ∎

## 2. Route (a): the three-vector Gram decomposition (PROVED)
For F ≠ 0 put a := U_μF, b := U_1F, c := U_logF ∈ L²(ℝ). Exact facts:
 (G1) Re⟨a, b⟩ = ‖F‖² (μ*1 = δ: ⟨U_μF, U_1F⟩ = Σ_{dn<N}μ(d)(dn)^{−½}c_F(log dn)… = Σ_k (μ*1)(k)k^{−½}c_F(log k) = c_F(0) = ‖F‖²,
  terms with dn ≥ N vanish because c_F = 0 beyond 2T).
 (G2) Re⟨a, c⟩ = ½Σ v_n Re c_F(log n) (L2_017 Lemma 1; μ*log = Λ).
 (G3) Re⟨b, c⟩ = −½ ∂_s‖U_sF‖²|_{s=½} (c = −∂_sU_sF; real F).
Decompose a = αb + a⊥, c = βb + c⊥ (orthogonal to b in the real Hilbert space L²(ℝ;ℂ) with Re⟨·,·⟩). Then α = ‖F‖²/‖b‖² by (G1),
β = Re⟨b,c⟩/‖b‖², and
 **Σ_n v_n Re c_F(log n) = 2αβ‖b‖² + 2Re⟨a⊥, c⊥⟩ = −‖F‖²·∂_s log‖U_sF‖²|_{s=½} + 2Re⟨a⊥, c⊥⟩.**
The first term — the **ℤ-additive centre** — depends only on the integer comb U_s (coefficients 1), not on μ or Λ. The second is the
Möbius–log interaction orthogonal to the integer-comb direction. Cauchy–Schwarz: |Re⟨a⊥, c⊥⟩| ≤ ‖a⊥‖‖c⊥‖ with
‖a⊥‖² = ‖U_μF‖² − ‖F‖⁴/‖U_1F‖², ‖c⊥‖² = ‖U_logF‖² − (Re⟨b,c⟩)²/‖U_1F‖².
Hence (N_loc) holds for F if
 (A) −‖F‖²∂_s log‖U_sF‖² + 2‖a⊥‖‖c⊥‖ ≤ 𝔞_∞(F),
and (N_loc) is EQUIVALENT to the anti-alignment ρ(F) := Re⟨a⊥, c⊥⟩/(‖a⊥‖‖c⊥‖) ≤ [𝔞_∞(F) + ‖F‖²∂_s log‖U_sF‖²]/(2‖a⊥‖‖c⊥‖).

## 3. Size test of (A) — the Cauchy–Schwarz version loses (ARGUED, with PROVED diagonal parts)
Diagonal (n = m) parts of the multiplier norms: ‖U_μF‖² ≥? the diagonal is Σ_{d<N}μ(d)²/d·‖F‖² ≍ (6/π²)(2T)‖F‖², and
‖U_logF‖² diagonal Σ (log m)²/m·‖F‖² ≍ (2T)³/3·‖F‖² (PROVED for the diagonal; off-diagonal terms are c_F(log(n/m)) with |c_F| ≤ ‖F‖²,
not controlled in sign). If the off-diagonal parts do not cancel the diagonal (generic F, ARGUED), 2‖a⊥‖‖c⊥‖ ≍ T²‖F‖², while 𝔞_∞(F) and
the centre are O(T)‖F‖² at most on low-frequency F. So (A) fails by a factor ≍ T: **the needed anti-alignment is real and sharp —
ρ(F) must be ≈ −(centre − 𝔞_∞/2)/(‖a⊥‖‖c⊥‖) = O(1/T) away from orthogonality with a definite sign; Cauchy–Schwarz cannot supply it.**
NO-GO for (A) as a sufficient condition (ARGUED).

## 4. What is new and what it points to
- (G1)–(G3) and the centre formula are PROVED and new: the comb splits EXACTLY into a ℤ-additive part −‖F‖²∂_s log‖U_sF‖² (no primes,
  no Möbius; a statement about the integer comb's norm as a function of s) and an interaction orthogonal to U_1F.
- Discrimination (input map L2_011): the centre is unchanged by tail deletion/rescaling of Λ (it does not see Λ) — so falsifiers act only
  on Re⟨a⊥,c⊥⟩; the interaction carries all the arithmetic. Beurling systems change the centre (positions not ℤ).
- The required inequality is now: Re⟨a⊥, c⊥⟩ ≤ ½[𝔞_∞(F) + ‖F‖²∂_s log‖U_sF‖²] on P_T, with a⊥ = (U_μ − αU_1)F, c⊥ = (U_log − βU_1)F —
  an anti-alignment between the "Möbius part orthogonal to ℤ" and the "log part orthogonal to ℤ". OPEN.
- Sign of the centre: −∂_s log‖U_sF‖² = 2Re⟨U_1F,U_logF⟩/‖U_1F‖²; the multiplier is Re(−ζ_N′·conj ζ_N)(½+iτ)/… — no sign in general
  (two-bump tests as in §1(ii) give both signs). OPEN for F in the archimedean-negative cone.

## Self-review
1. §1(i): the "≡ mod high lags" statements: ⟨F, τ_aF⟩ = c_F(a) = 0 for |a| ≥ 2T — correct; composites of U_μ^* and U_log shift by
log d + log m in the same direction (L2_017 convention) — consistent with L2_017 Lemma 1. Correct.
2. §1(ii): the two-bump test needs φ̂(±i/2) = 0 and width < (log 3 − log 2)/2 so that only lag log 2 (and 0) is hit; then c_{F±}(log n) = 0
for n ≥ 3 and n = 2 gives ±‖φ‖². Correct.
3. (G1): Σ_{d,n} μ(d)(dn)^{−½}c_F(log d + log n) groups by k = dn: Σ_k k^{−½}c_F(log k)Σ_{d|k}μ(d) = c_F(0). Requires the shifts to add
(both in the same direction) — with U_μ shifting by +log d and U_1 by −log n, ⟨τ_{log d}F, τ_{−log n}F⟩ = c_F(log d + log n) (up to the
convention c_F(a) = ⟨F, τ_aF⟩ and evenness of Re c_F). Correct for real F.
4. §3 is ARGUED (off-diagonal cancellation not excluded); labelled.
5. No claim that the anti-alignment holds or fails.
No sign contact; no negative value certified.
