# N_BUILD_004 — Route (b): the reflection u ↦ 2T − u, from scratch; route (c): Selberg's symmetry formula

## Corpus check
- Paper 47 thm:nyq-sectors (ii): Δ_T(F) = ∫K(u)Re c_F(2T−u) + Σ v_n Re c_F(2T−log n); s^per = 𝔞_T − Δ_T, s^anti = 𝔞_T + Δ_T.
- R186_052 §5.2 "99.4 % antiperiodic" — **RETRACTED** (R186_118 MAJOR-3: basis artefact; every F has 100 % energy in each
  sector). Not used.
- Selberg symmetry: phase-104 104_13, phase-103 103_63, phase-5 M5, phase-159 G2_B3_R3 (A1 closure / M5 gates; none on the
  row-D window form at Nyquist points).

## 1. The reflection is a property of the window, not of Λ (PROVED)
From lem:nyq-sampling(ii): (1/4T)Σ_k(−1)^k a_k cos(ω_k u) = Re c_F(2T − u), 0 ≤ u ≤ 2T. Pairing with the comb:
  Σ_k (−1)^k a_k P(ω_k) = 4T Σ_{n∈N_T} v_n Re c_F(log(e^{2T}/n)).
So the reflection n ↦ e^{2T}/n is exactly the alternating part of the sampled comb. For F ∈ P_T, (D0) of N_BUILD_001
gives Σ(−1)^k a_k = 0; hence only the oscillating part of P on the mesh enters, and with (D1) the polar part also drops
out. *No sign*: for any F, replacing F by F·e^{iπt/2T} (which maps the periodic basis to the antiperiodic one) exchanges
the two sector forms up to the half-step conjugation (R186_053 L1.1(iv)), so a sector-wise sign statement cannot be
specific to either sector. NO-GO for "localize the sign in one spin sector" (PROVED by this exchange; consistent with
the retraction).

## 2. Contact windows: divisor pairing (PROVED, elementary)
At T = ½log q (q a prime power, first-contact windows) the reflected atoms log(q/n) are comb atoms iff n | q:
Σ_n v_n c_F(log(q/n)) = Σ_{n m = q} v_n c_F(log m)·[v_m-free] + (non-integer lags). For q = p^k the divisor pairs are
(p^i, p^{k−i}): the reflection couples only the powers of the entering prime. So the reflection carries no information
on the other primes at contact windows. NO-GO as a source of cross-prime cancellation.

## 3. Route (c): Selberg's symmetry formula
Σ_{n≤x}Λ(n)log n + Σ_{nm≤x}Λ(n)Λ(m) = 2x log x + O(x) (CITED, elementary). It is a signed identity coupling Λ with Λ*Λ.
In the window, Λ*Λ appears as the comb of the comb: c_F against Σ v_n v_m δ_{log nm} = the square of the comb operator
𝒱 = Σv_n(τ_{log n}+τ_{−log n})/2 restricted to products — i.e. ⟨𝒱F,𝒱F⟩-type terms (since τ_aτ_b = τ_{a+b}).
Obstruction (PROVED): the error O(x) is exponent 1; in the window it contributes O(e^{T})·‖F‖² after weighting by
n^{−1/2} — the same loss as rem:wit-cheb. The formula holds for every a in 𝒞_PNT-type classes with the same O(x)
error and finite modifications change it by O(x^{1/2+o(1)}) only, so any argument using it alone applies to the members of thm:finmod (ARGUED, not a formal class theorem). NO-GO (ARGUED).
Residual idea kept (OPEN, not a theorem): the second-moment operator inequality 𝒱² ≤ ? — the window form contains 𝒱
linearly; a Cauchy–Schwarz ⟨F,𝒱F⟩ ≤ ‖F‖‖𝒱F‖ loses the sign; no signed use found.

## Self-review
§1: the exchange claim — multiplication by e^{iπt/2T} is unitary on L²(I_T) but does NOT preserve P_T (it moves the
Tate points ±i/2 by π/2T). So the exchange is exact only on L²(I_T); on P_T it holds modulo a 2-dim correction. The
NO-GO is therefore downgraded to ARGUED on P_T (exact on L²(I_T)). §2 correct and trivial. §3 correct; the residual
is a question, not progress. No sign contact; no negative value.
