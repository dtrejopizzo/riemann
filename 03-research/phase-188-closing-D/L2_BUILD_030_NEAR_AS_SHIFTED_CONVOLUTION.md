# L2_BUILD_030 — The near-coincidence part as a shifted-convolution operator; exact operator identities

Scope (coordinator): operator/matrix structure only; the arithmetic of the shifted sums Σ_{m−kn=h}Λ(n) is left to the track (N).

## Corpus check
028 (A_M = Arch − Div − Near), 029 (Near-free sets are trivial), N_BUILD_001 (A),(B) (polar elimination, m^♯ form), Paper 46 eq:Aform; R186_001 (Gram of
translates); phase 167 (shifted sums, Titchmarsh divisor problem mentions). grep "Ramanujan sum / c_q / shifted convolution / m − kn = h / Dirichlet
polynomial times": no row-D memo writes the integer-lattice form as W(Vs). New: §1–§4.

Notation: s = (s_m)_{m≤M} real; W_g := [ǧ_g(log m − log k)] where ǧ_g is the inverse Fourier transform of g·F̂₀² (so W_1 has entries c₀(log(m/k)));
P_s(τ) := Σ_m s_m m^{iτ}; V := Dirichlet-convolution matrix (Vs)_j = Σ_{n|j}v_n s_{j/n}, v_n = 2Λ(n)n^{−½}; F₀ the profile of 025, ‖F₀‖ = 1, width 2T₀.

## 1. Exact identities (PROVED)
(a) s^TA_Ms = s^T W_m s − s^T W_1 V s  (the second term symmetrized; W_1 couples m with j = kn only when |log(m/j)| ≤ 2T₀).
(b) Spectral form: s^TW_g s = (1/2π)∫g F̂₀²|P_s|²dτ, and P_{Vs} = P_s·V(τ) with V(τ) := Σ_n v_n n^{iτ} (Dirichlet polynomials multiply under Dirichlet
    convolution). Hence
      s^TA_Ms = (1/2π)∫F̂₀(τ)²|P_s(τ)|²[m(τ) − Re V(τ)]dτ   (n effectively < Me^{2T₀}).
(c) Splitting by the additive shift h := m − kn:
      s^T W_1 V s = Σ_h Σ_{m − kn = h} s_m s_k v_n c₀(log(m/(kn))),   c₀(log(m/(kn))) = c₀(−log(1 − h/m)),
    with h = 0 ↔ Div and h ≠ 0 ↔ Near; the support condition |log(m/(kn))| ≤ 2T₀ gives |h| ≤ (e^{2T₀} − 1)m ≈ 2T₀m. For 2T₀ = c/M this is |h| ≲ c·m/M ≤ c:
    **Near is a sum over boundedly many additive shifts h ∈ [−c, c] \ {0}, each a shifted convolution Σ_{m−kn=h} s_m s_k Λ(n)/√n weighted by c₀(h/m + O(h²/m²)).**
*Proof.* (a) is 028 §2 regrouped (c₀ even). (b): Σ_{m,k}s_ms_k ǧ_g(log(m/k)) = (1/2π)∫gF̂₀²|P_s|² by Fourier inversion; Dirichlet product rule. (c): expand. ∎

## 2. Sign structure (PROVED)
- W_1 = [c₀(log m − log k)] is positive semidefinite (sampling of the positive definite function c₀ at the points log m). W_m is not (symbol m < 0 near 0).
- V is lower triangular (not symmetric); W_1V has no sign: by (b) its symmetric part is the multiplier Re V(τ), which is indefinite.
- In the Bohr picture (028 §2(c)) Div is the Bohr-diagonal part of |P_s|²·V (exact resonances m = kn) and Near is the near-diagonal part (m ≈ kn): Near is
  not a separate operator with its own sign; it is the finite-resolution remainder of the same product, of relative size governed by the resolution 2T₀M.

## 3. What cancels and what remains (PROVED for the identities; the discrete main-term statement ARGUED)
Ramanujan expansion (CITED): 1_{n|j} = (1/n)Σ_{q|n}c_q(j). For Λ(n) ≠ 0, n = p^a, so the divisors q > 1 are prime powers p^b, b ≤ a:
  (Vs)_j = Σ_n (v_n/n) s̃_n(j) + Σ_{p,b≥1} c_{p^b}(j) Σ_{a≥b}(v_{p^a}/p^a) s̃_{p^a}(j),   s̃_n(j) := n·s_{j/n} if n | j, interpolated otherwise
(for s sampled from a smooth function S, s̃_n(j) = S(j/n)·n·1_{n|j}/… — the clean statement is in terms of S: Σ_{n|j}v_nS(j/n) = Σ_q c_q(j)Σ_{q|n}(v_n/n)S(j/n)).
- q = 1 term: Σ_n (v_n/n)S(j/n) = Σ 2Λ(n)n^{−3/2}S(j/n): the density (PNT) part plus its Chebyshev fluctuation. In the analytic pairing its PNT main term is
  exactly the polar density 2e^{u/2}, which on primitive tests gives +𝔭(F) ≥ 0 (N_BUILD_001 (A)) — so Arch + (q = 1 main term) = the m^♯-form (N_BUILD_001 (B)),
  and the q = 1 remainder is the Chebyshev fluctuation 𝓕_T in integer coordinates.
- q = p^b terms: additive characters c_{p^b}(j) = Σ_{(a,p^b)=1} e(aj/p^b), weighted by Σ_{a≥b}2 log p·p^{−3a/2}: these are the "local" (prime-power modulus)
  components of the shifted convolution; under the near-diagonal smoothing over |h| ≤ c they are NOT averaged out (bandwidth c is O(1), not ≫ p^b).
So: **Q = (m^♯-form) − ⟨Chebyshev fluctuation (q = 1)⟩ − Σ_{p,b}⟨additive-character components mod p^b⟩**, all three exact in the analytic pairing; the last
two are where the arithmetic of Σ_{m−kn=h}Λ(n) enters (the track (N)'s object). The h = 0 slice of the q = p^b components reproduces Div's local Euler-factor
symbols of 029.

## 4. Review
- §1 exact (Fourier inversion; Dirichlet product). §1(c) the bound |h| ≲ c m/M is exact up to e^{2T₀} − 1 ≈ 2T₀.
- §2 correct; the point "Near has no sign of its own; it is the finite-resolution remainder of |P_s|²V" is structural and PROVED via (b).
- §3: the Ramanujan expansion is exact; the passage from sequences s to a smooth S (interpolation) is ARGUED; in the analytic pairing (b) everything is exact,
  and the identification "Arch + q=1 main term = m^♯-form" is N_BUILD_001 (B) in different coordinates (corpus-known). New is only the operator bookkeeping
  (W_1V, shifted-convolution slices, prime-power-modulus components).
- No sign certified; no negative value of 𝔞_T for ζ.
