# N_BUILD_017 — The ℤ-additive centre 𝒞(F) on the archimedean-negative cone: it equals +4T‖F‖² − O(1) — wrong sign, size T; no slack

Pen and paper. Notation of N_BUILD_016: comb(F) := Σ v_n Re c_F(log n) = 𝒞(F) + 2Re⟨a⊥, c⊥⟩, 𝒞(F) := −‖F‖²∂_s log‖U_sF‖²|_{s=½},
F ∈ P_T real. Target (N_loc): comb(F) ≤ 𝔞_∞(F) on P_T.

## Corpus check
grep "Montgomery–Vaughan|mean value theorem|Σ n^{−s}.*N^{1−s}|ζ_N|truncated zeta|integer Dirichlet polynomial": phase 137
(R137_001/002/007) uses the Montgomery–Vaughan mean value theorem for a different purpose (canonical coupling, large-sieve sizes); no
memo evaluates ‖U_sF‖² or its s-log-derivative. N_BUILD_016 (Gram identity), L2_BUILD_008 (clamped modes), N_BUILD_001 (A).
New: §1–§3.

## 1. Exact multiplier form (PROVED)
U_s is the Fourier multiplier with symbol ζ_N(s − iτ)-type (conjugation conventions immaterial for |·|), ζ_N(z) := Σ_{n<N}n^{−z}. Hence,
on all of L²(ℝ) (no truncation),
 ‖U_sF‖² = (1/2π)∫|ζ_N(s+iτ)|²|F̂(τ)|²dτ,  ∂_s‖U_sF‖² = (1/2π)∫2Re(ζ_N′ ζ̄_N)(s+iτ)|F̂|²dτ.

## 2. Asymptotics of the symbol (PROVED with a CITED Euler–Maclaurin formula)
For s = ½ + iτ (CITED: ζ(s) = Σ_{n<N}n^{−s} + N^{1−s}/(s−1) + ½N^{−s} + E, |E| ≤ |s(s+1)|N^{−3/2}/… for N ≥ 2):
 ζ_N(½+iτ) = N^{½−iτ}/(½−iτ) + ζ(½+iτ) − ½N^{−½−iτ} + E,
 ∂_sζ_N(½+iτ) = −Σ(log n)n^{−½−iτ} = N^{½−iτ}[−log N/(½−iτ) + 1/(½−iτ)²] + ζ′(½+iτ) + (smaller).
Write M(τ) := N^{½−iτ}/(½−iτ) (|M| = e^T/(¼+τ²)^{1/2}) and r(τ) := ζ_N − M = ζ(½+iτ) + O(e^{−T}(1+|τ|)²). Then
 2Re(ζ_N′ζ̄_N) = 2Re[M′M̄] + O(|M|·(|ζ′| + |ζ|·(2T+2))) + O(|ζ||ζ′|),  M′ := ∂_sM = M·(−2T + 1/(½−iτ)),
 2Re[M′M̄] = |M|²·(−4T + 2Re(1/(½−iτ))) = |M|²·(−4T + 1/(¼+τ²)).
For F with ∫(1+τ²)^2|F̂|²dτ < ∞ (true on P_T: F = (¼−∂²)G, and ‖G‖_{H²} finite; |ζ(½+iτ)|, |ζ′(½+iτ)| ≪ (1+|τ|)^{1/2} log(2+|τ|),
convexity bound CITED), the |M|²-terms dominate the integrals by a factor ≍ e^{T}/T² against the cross terms, uniformly for unit F with
bounded H¹-type moments. Hence, with the weight w_F(τ) := |F̂(τ)|²/(¼+τ²) and ⟨g⟩_w := ∫g w/∫w,
 **∂_s log‖U_sF‖²|_{½} = −4T + ⟨1/(¼+τ²)⟩_{w_F} + O_F(T e^{−T}),**
 **𝒞(F) = ‖F‖²·(4T − ⟨1/(¼+τ²)⟩_{w_F}) + O_F(T e^{−T}).**
Since 0 < 1/(¼+τ²) ≤ 4: 𝒞(F) ≥ (4T − 4)‖F‖² − o(1). The constant in O_F depends on ∫(1+τ²)^{3/2}|F̂|²/∫|F̂|²/(¼+τ²) — bounded on any
fixed finite-dimensional space such as the archimedean-negative space 𝒩_T at a given T, and on the low clamped modes (L2_BUILD_008:
ground mode φ₀ is low-frequency, F̂ concentrated at |τ| ≲ π/T after the factor (τ²+¼)) uniformly in T (ARGUED for uniformity).
On φ₀: w concentrates near τ = 0 where 1/(¼+τ²) ≈ 4, so 𝒞(φ₀) ≈ (4T − 4)‖φ₀‖².

## 3. Consequence: the centre carries the wrong sign (PROVED for T large on 𝒩_T)
(N_loc) on F requires comb(F) ≤ 𝔞_∞(F) < 0 on 𝒩_T, i.e. 2Re⟨a⊥, c⊥⟩ ≤ 𝔞_∞(F) − 𝒞(F) ≈ −(4T − 4 + |𝔞_∞(F)|/‖F‖²)‖F‖².
**There is no slack: the ℤ-additive centre is +4T‖F‖² (wrong sign, growing), and the Möbius⊥/log⊥ interaction must cancel it and
supply the full deficit on top.** The comb itself is O(1) on P_T (it equals −𝔭 + 𝓕_T with 𝔭 ≤ 4‖F‖²; on low modes 𝓕_T is the
fluctuation), so the Gram split of N_BUILD_016 represents an O(1) quantity as the difference of two O(T) quantities. NO-GO for using the
centre as slack.
Explanation: the centre is dominated by the integer comb's main term N^{1−s}/(1−s) — the PNT/polar density of ℤ — which the Tate
conditions annihilate in the comb (N_BUILD_001 (A)) but NOT in the Gram norm ‖U_sF‖² (a quadratic, not linear, functional of the
integer comb: its main term is the autocorrelation of e^{u/2}, not e^{u/2} itself).

## 4. Repair direction (PROVED identity; OPEN use)
Replace b = U_1F by the Tate-compatible fluctuation vector b♭ := (U_1 − 𝓜)F, 𝓜 the multiplier M(τ) = N^{½−iτ}/(½−iτ) (main term of
ζ_N). Then (G1) becomes Re⟨a, b♭⟩ = ‖F‖² − Re⟨U_μF, 𝓜F⟩, and Re⟨U_μF, 𝓜F⟩ = pairing of the Möbius comb with the Mellin main term —
a smoothed Mertens sum Σ μ(d)d^{−½}·(main-term kernel), O(e^{T}·smoothed M(x)/x) — no longer exact, losing exactly what (G1) gave.
So any Gram split either has an exact Möbius identity (G1) with a wrong-sign centre of size 4T, or a small centre with an inexact
Möbius term. The anti-alignment problem is invariant under this choice (the comb is fixed). Recorded; OPEN.

## Self-review
1. §1: multiplier form is exact on L²(ℝ) (U_sF is not compressed). Correct.
2. §2: Euler–Maclaurin form of ζ_N with explicit error is classical (CITED); the dominance argument needs ∫|ζ|·|M|·|F̂|² ≪ e^T∫(1+|τ|)^{½+ε}
|F̂|²/(¼+τ²)^{½} — finite for F ∈ P_T (F̂ = (τ²+¼)Ĝ, Ĝ ∈ H²-transform). Ratio to ∫|M|²|F̂|² ≍ e^{2T}∫w: relative O(e^{−T}·poly). Correct;
uniformity in T on 𝒩_T is ARGUED (needs uniform moment bounds of the negative eigenvectors).
3. §3 sign: 𝒞 = −‖F‖²∂_s log‖U_sF‖² = +‖F‖²(4T − ⟨·⟩) > 0. Checked against a sanity case: for F concentrated at τ ≈ 0,
‖U_sF‖² ≈ |ζ_N(s)|²‖F‖² with ζ_N(s) ≈ N^{1−s}/(1−s) decreasing in s at rate log N = 2T per unit s for |·|, so log|·|² decreases at
rate 4T − 2/(1−s)·… : −∂_s log = 4T − 4 at s = ½. Matches.
4. Consistency with the comb being O(1): comb = 𝒞 + 2Re⟨a⊥,c⊥⟩ forces 2Re⟨a⊥,c⊥⟩ ≈ −4T‖F‖²; not a contradiction.
No sign contact; no negative value certified.
