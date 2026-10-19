# L2_BUILD_029 — A_M on separated multiplicative sets: Kronecker sums of local Euler-factor Toeplitz forms

## Corpus check
028 (A_M ⟺ D; Arch − Div − Near), 023 Lemma C (archimedean cross terms O(e^{−5d/2})), phase-146 R146_003 §D.47 (single-prime tower: PSD iff τ_p ≥
2/(√p+1) — the MINIMUM of the local symbol), R184_004 (inertia of B_p blocks), Paper 47 finmod(ii). New: the restriction to Near-free sets, its exact
Kronecker-sum structure, the explicit eigenvalue bound, and the separation–resolution trade-off that makes it trivial.

## 1. Near-free supports (PROVED)
Let P = {p_1, …, p_r} and K_i ≥ 1, S := {m = Π p_i^{k_i} : 0 ≤ k_i ≤ K_i}, L := Σ_i K_i log p_i (so all m ≤ e^L). For m, k ∈ S and n ≥ 2 put
x = log m − log k − log n. If x ≠ 0 then |x| ≥ 1/(2 max(m, kn, …)) ≥ e^{−2L}/2 (ratio of integers ≤ e^{2L} when |x| ≤ log 2). Choose the profile width
2T₀ < e^{−2L}/2: then Near vanishes on S, and the exact coincidences m = kn with Λ(n) ≠ 0 occur iff m/k is a single prime power p_i^h (h ≥ 1) —
a ratio with two different primes is not in the support of Λ. ∎

## 2. Exact structure (PROVED, up to the archimedean cross terms of 023 Lemma C)
On S (indexed by k = (k_1, …, k_r)), with ‖F₀‖ = 1 and a₀ := 𝔞_∞(F₀) (no prime in the central window):
  s^T A s = a₀Σ_k s_k² − Σ_i Σ_{k, h≥1} log p_i·p_i^{−h/2}·2 s_k s_{k + h e_i} + E,  |E| ≤ C Σ_{k≠l}|s_ks_l|e^{−5|log(m_k/m_l)|/2} = O(e^{−5 log 2/2})‖s‖²·(…)
So A|_S = a₀ I − Σ_i (D_i ⊗ I_{others}) + E: a KRONECKER SUM of one-prime Toeplitz matrices D_i = [log p_i·p_i^{−|j−k|/2}]_{j≠k} (zero diagonal),
plus exponentially small archimedean couplings.
Local symbol (exact): the Toeplitz symbol of D_i is δ_i(θ) := Σ_{h≥1}2 log p_i p_i^{−h/2}cos(hθ) = 2 log p_i Re[x/(1 − x)], x = p_i^{−½}e^{iθ}, i.e. minus
twice the real part of the log-derivative of the local Euler factor (1 − p_i^{−½−iθ})^{−1} (times log p_i normalization). Exact range:
  max_θ δ_i = 2 log p_i/(√p_i − 1)  (θ = 0),   min_θ δ_i = −2 log p_i/(√p_i + 1)  (θ = π)   [the latter is the phase-146 threshold].
Eigenvalues: the finite Toeplitz sections of δ_i have spectrum inside [min δ_i, max δ_i] and fill it as K_i → ∞ (Szegő, CITED); the Kronecker sum has
spectrum {Σ_i μ_i}. Hence
  λ_min(A|_S) = a₀ − Σ_i μ_max(D_i) + O(E),  μ_max(D_i) ↑ 2 log p_i/(√p_i − 1) as K_i → ∞.

## 3. The test and its verdict (PROVED as stated)
Necessary condition (from D, since A|_S is a principal submatrix of A_M): a₀ ≥ Σ_i μ_max(D_i) − O(E).
Separation forces resolution: §1 requires 2T₀ < e^{−2L}/2, and for a primitive profile of width 2T₀ the archimedean energy is a₀ = log(1/T₀) + C_χ + o(1)
(ARGUED, 028 §3), so a₀ ≥ 2L + C_χ + log 4 = 2Σ_iK_i log p_i + O(1). Since 2 log p/(√p − 1) ≤ 2 log p·(1/(√2−1)) ≈ 4.83 log p and K_i ≥ 1, the condition
reads Σ_i 2 log p_i/(√p_i − 1) ≤ 2Σ_iK_i log p_i + O(1) — true for all P, K once K_i ≥ 3 (for p ≥ 11 already K_i ≥ 1: 2/(√p−1) < 1). So:
- ζ passes this test trivially, for a cheap reason: the separation needed to kill Near costs resolution, which buys archimedean energy ≈ 2L that dominates
  the Euler-factor maxima Σ 2 log p/(√p − 1). The local Euler-factor identity that makes it pass is the exact range of δ_p (above), i.e. the bound
  |Re(log-derivative of the local factor at ½)| ≤ log p/(√p − 1) — a property of each local factor separately.
- a_P (deletion): the Div blocks of deleted primes vanish — passes trivially.
- Amplification finmod(ii) (a(2) = log 2 + c): δ_2 scales with the weight at 2; fails once the amplified maximum exceeds a₀ — only for c ≳ a₀, i.e.
  gross amplification. Epstein/DH: no local Euler factors; the construction does not apply.
**Verdict: on Near-free multiplicative sets the test is a Kronecker sum of local Euler-factor Toeplitz forms; it is satisfied for local reasons, carries no
global (FE) input, and gives no certificate.** The sign of D cannot live on Near-free sets: it must involve the near-coincidences (Near), i.e. the
interaction of the real-lag archimedean kernel with integers that are close but not equal in log scale — consistent with 019/020 (resolution scale e^{2T})
and 028 §2.

## 4. Review
- §1: the separation bound is crude but correct; it is exactly the resolution trade-off. §2: Kronecker-sum structure exact given Λ supported on prime
  powers (cross ratios with two primes have Λ = 0); Szegő for Toeplitz sections CITED; max/min of δ_p computed from Re[x/(1−x)] = (Re x − |x|²)/|1−x|²,
  extremal at θ = 0, π. Correct.
- §3: the archimedean energy asymptotic a₀ ≈ log(1/T₀) + C_χ is ARGUED (as in 028). The comparison is robust (L-linear vs constants).
- No sign certified; no negative value of 𝔞_T for ζ.
