# PROOF_L_SHARP_Y_001 — Theorem B′: multi-cell Langer chirps, overlapping dilates and the (1,n) resonances (plank P2)

Phase 199, Pen and paper. Two scratch checks of elementary constants (not stored) are labelled NUMÉRICO
and only check the proof. , no zero is
used, and

**Outcome.**
- Theorem B (X_001, single cell) is extended to **multi-cell Langer chirps** ρ = a e^{iφ_c}, φ_c(t) = c√(t²−1), c = 2πμ,
  with a ∈ C²_c((1+η, X)) vanishing to first order at every integer (no truncation jumps), f(λ) = 0 (no edge), gauge ignored:
  **𝔔[ρ] = ∫_1^∞ 𝔴_μ(t)|a(t)|²dt + 𝓡_res + E,  |𝓡_res| ≤ C_res·c^{−½},  |E| ≤ C_E·c^{−1}**, explicit constants (Thm Y.5).
  Hence **𝔔[ρ] ≥ (log 2μ − R(c))‖a‖², R(c) = O(c^{−½}log c)** for a fixed profile (Cor Y.6). PROVED.
- The three new effects, exactly: (a) truncation at t = n reproduces H(t) = H_N on cell N exactly (the E.1′ harmonic cut on the
  diagonal); the sawtooth is inside the weight, not an error; truncation *jumps* are O(log c/c) (ARGUED, Prop Y.7);
  (b) overlapping dilates m ≠ n: the relative Mellin phase ψ_{mn} is **strictly concave** for m = 1 and has a unique stationary
  point s_n = √(1+n^{−2}) (sampled points t = s_n and t = √(n²+1), common frequency c(n²+1)/n, Hessian
  −c(n⁴−1)(n²+1)/n³); **no stationary point for 2 ≤ m < n** (gap ≥ 0.77cs(n−m)). PROVED. (c) The comb is no longer scalar:
  its diagonal is the phase-blind −2∫H₁|a|² (Λ∗1 = log, cell by cell); its off-diagonal is phase-dependent and is absorbed
  into the same oscillatory pairs.
- **Resonances are O(c^{−½}) only under amplitude regularity on the Fresnel scale.** For Fresnel-scale amplitudes a (1,n)
  resonance is O(1) relative, but at leading order it never exceeds 1/√(nH_n) ≤ 0.58 of the geometric-mean diagonal it couples
  (Prop Y.8, ARGUED). So P2 does not fail at leading order; its smallness is a regularity statement.
- cΛ (weight κ on the comb): every κ > 1 gives a negative direction inside the class at every μ (Cor Y.9, PROVED), so the
  positivity of Cor Y.6 is Λ-sensitive.
- Not covered: the actual prolate tails (jumps at integers, mass near t = 1 where resonances accumulate, tail beyond X), the edge
  P3b (f(λ) ≠ 0), the gauge Π. L′♯ OPEN. Row D OPEN.

## 0. Corpus / index check, and why this is not a retry
- Searched: ROUTES-TRIED-INDEX README l.449–472 (phase 199: BRIDGE_001, SYNTHESIS_MECHANISM_001, X_001 + AUDIT_20),
  06_OPEN_RESIDUES; grep "multi-cell / multi-celda / van der Corput / Langer resonance" over the index and proof-L-sharp/:
  no entry. Read: X_001, AUDIT_L_SHARP_8 (constraint 20), BRIDGE_001 §4–§5, SYNTHESIS §3.3, E_001 Thm E.1/E.1′/E.2/Cor E.3,
  J_001 Prop J.1, PRECHECK_T1_001.
- Why not a retry: this is P2 proper, recorded OPEN in X_001 §6.3/§7 and AUDIT_8 constraint 20 ("single-cell data do not test
  resonances"). The new object is the overlapping-dilate pair (1,n) on Langer phases; the new tool is the second-derivative
  van der Corput bound on a globally concave relative phase. Nothing in the index evaluates cross-dilate oscillatory pairs.

## 1. Setting (definitions as X_001 §1, E_001 §1–§3, checked against Cor E.3)
- ρ on (1,∞); u(x) := e^{x/2}ρ(e^x); Ψ̌_ρ(y) := e^{y/2}Σ_n ρ(ne^y) for y > 0, 0 for y ≤ 0;
  𝔔[ρ] := 𝒜[Ψ̌] − 2Re⟨Ψ̌,Ψ̌_log⟩ + 2Re(A_p\bar B_p) (Cor E.3, Hermitian extension). 𝒜 = full-line Lévy form of the
  zero-extended Ψ̌, killing term included; Θ_∞, b_∞, ν, C_Θ = 0.187 as in X_001.
- ℓ_n := log n; **u_n(y) := u(y+ℓ_n)·1_{y>0}** (dilate n, truncated at t = n); s := e^y; dilate n samples t = ns.
- **Class (L_η,X).** μ ≥ 4, c = 2πμ, η ∈ (0,1), X ≥ 2, ρ = a e^{iφ_c}, φ_c(t) = c√(t²−1), with
  a ∈ C²_c((1+η, X)) and **(Z₁): a(k) = a′(k) = 0 for every integer k ∈ (1+η, X)**.
  **(No edge) f(λ) = 0 is assumed** (the data are exterior tails of the core; the edge channel P3b is excluded by hypothesis).
  **The gauge Π is not involved** (no claim about dist²(ρ,𝒢̄)).
- Mellin frequency: Φ(x) := φ_c(e^x), Φ′(x) = τ(t) := c t²/√(t²−1) (t = e^x). τ′(t) = c·g(t), g(t) := t(t²−2)/(t²−1)^{3/2};
  Φ″/Φ′ = (t²−2)/(t²−1). On t ≥ 1+η: |Φ″/Φ′| ≤ β_η := max(1, 1/(2η+η²)); Φ‴/Φ′ is a rational function of t, c-free.
- Leading weight: w(t,φ_c′(t)) = H(t)log(tφ_c′/2π) − 2H₁(t) = H(t)log(μt²/√(t²−1)) − 2H₁(t) = **𝔴_μ(t)** (SYNTHESIS §3.3).
- Profile constants (c-free): ‖a‖ = L²(dt); K_a := ‖a‖ + ‖ta′‖; K̄ := (1+β_η)K_a; K₂^♯ := sup_m K₂(u_m) with K₂ the
  AUDIT_8-corrected K₂ (coefficients 1, 6, 2, 12) in the variable y (y-derivatives are t∂_t; c-free);
  T_η := (1+η)/√(2η+η²); Λ := log(μT_ηX) + 2log X.

## 2. The exact multi-cell pair expansion (PROVED)
**Lemma Y.1.** On (L_η,X):
 Ψ̌ = Σ_{n≤X} n^{−½}u_n, and
 𝔔[ρ] = Σ_{m,n≤X}(mn)^{−½}[⟨Θ_∞(D)u_m,u_n⟩ − (ℓ_m+ℓ_n)⟨u_m,u_n⟩] + 2Re(A_p\bar B_p),
 A_p = ∫ρ(t)⌊t⌋dt/t, B_p = ∫ρ(t)H(t)dt.
*Proof.* E.1 with the window parameter 0 gives Ψ̌ = Σ n^{−½}u_n (u_n = 0 for n > X since supp a ⊂ (1,X)). Bilinearity and
translation invariance of Θ_∞(D) give the archimedean part (full line, killing term included). The prime part is E.2:
−2Re⟨Ψ̌,Ψ̌_log⟩ = −Σ(mn)^{−½}(ℓ_m+ℓ_n)Re⟨u_m,u_n⟩ after symmetrisation. Pole: n^{−½}∫_{y>0}u(y+ℓ_n)e^{∓y/2}dy equals
∫_{t>n}ρ dt/t, resp. n^{−1}∫_{t>n}ρ dt; sum over n. □

**The three new effects, read off Lemma Y.1.**
- (a) **Truncation.** u_n sees ρ only on t > n. Pair (m,m): the j-sum of E.1′ at α = β = 1 and y = y′ is H(min(e^y,e^{y′})) =
  H(t); on cell N it is H_N. With (Z₁) the truncation is C¹ (no jump). Without (Z₁) each u_n has a jump of size n^{½}|ρ(n)| at
  y = 0 (Prop Y.7).
- (b) **Overlap.** For m ≠ n the supports of u_m, u_n overlap (unlike X.1): ⟨u_m,u_n⟩ = ∫_{s>1}(mn)^{½}s·a(ms)ā(ns)
  e^{iψ_{mn}(y)}ds/s with ψ_{mn}(y) := φ_c(ms) − φ_c(ns), ψ′_{mn} = τ(ms) − τ(ns).
- (c) **Phase-dependent comb.** The prime part = −2Σ_m m^{−1}ℓ_m‖u_m‖² (phase-blind, = −2∫H₁(t)|a|²dt) plus
  −Σ_{m≠n}(mn)^{−½}(ℓ_m+ℓ_n)⟨u_m,u_n⟩ (phase-dependent, oscillatory with phase ψ_{mn}).

## 3. Stationary points of the relative phase (PROVED, elementary)
**Lemma Y.2.**
- (i) g is increasing on (√2,∞) (log-derivative numerator = t²+2 > 0), g < 0 on (1,√2), g(2) = 0.7698, g(2√2) = 0.9163, g → 1.
  Hence τ′ ≥ 0.77c on [2,∞) and τ′ ≤ c on (√2,∞).
- (ii) **2 ≤ m < n:** ms ≥ 2, so by the mean value theorem τ(ns) − τ(ms) ≥ 0.77c·s(n−m) > 0: **no stationary point**; and
  |ψ″_{mn}| = |ms τ′(ms) − ns τ′(ns)| ≤ c·ns.
- (iii) **m = 1, n ≥ 2:** ψ″_{1n}(y) = s g(s)c − ns g(ns)c < 0 for every s > 1, and |ψ″_{1n}| ≥ 0.4·c·n. ψ′_{1n} has exactly one
  zero, at **s_n = √(1+n^{−2})**: the pair samples t = s_n (dilate 1, decreasing branch) and t = √(n²+1) (dilate n), common
  Mellin frequency **τ_n = c(n²+1)/n**, and ψ″_{1n}(y_n) = **−c(n⁴−1)(n²+1)/n³** (Fresnel width (cn³)^{−½}).
- (iv) Resonant pairs exist inside supp a only for s_n > 1+η, i.e. **n ≤ N_η := ⌊(2η+η²)^{−½}⌋**; they accumulate at t = 1 as
  η → 0 (s_n − 1 ≈ 1/(2n²)).
*Proof.* (i) direct. (ii) MVT. (iii) For s < √2: g(s) < 0, so |ψ″| ≥ c·ns g(ns) ≥ 0.77cn s ≥ 0.4cn (ns ≥ 2). For s ≥ √2:
t ↦ t g(t) is increasing there, so ψ″ < 0, and |ψ″| ≥ c s(n g(ns) − g(s)) ≥ c√2(0.916n − 1) ≥ 0.4cn (ns ≥ 2√2, g ≤ 1).
Monotonicity of ψ′ gives uniqueness. τ(s) = τ(ns) ⟺ n²s² − 1 = n⁴(s² − 1) ⟺ s² = 1 + n^{−2}. At s_n: s_nτ′(s_n) =
−c(n⁴−1)/n, and with T = √(n²+1), Tτ′(T) = c(n⁴−1)/n³; subtract. □
NUMÉRICO check: inf |ψ″_{1n}|/(cn) = 1.11 (n ≤ 40); inf over 2 ≤ m < n of the gap/(cs(n−m)) = 0.87; Hessian formula
reproduced to 10⁻¹⁴.

## 4. Operator form of the oscillatory log-symbol lemma (PROVED)
**Lemma Y.3.** Let u = Ae^{iΦ}, A ∈ C¹ with A′ absolutely continuous, A″ ∈ L¹, compact support, Φ′ ≥ Ω ≥ 4π on supp A,
K₀, K₂ as in X.5a/AUDIT_8. Then
 ‖Θ_∞(D)u − log(Φ′/2π)u‖₂ ≤ (2log2/Ω)K₀ + 4C_Θ‖A‖₂/Ω² + K₂(8 + 2log(1+Ω))Ω^{−3/2}.
*Proof.* As X.5a, but in L² rather than as a form.
- On τ > Ω/2, |Θ_∞ − log(τ/2π)| ≤ 4C_Θ/Ω².
- On τ ≤ Ω/2, |û| ≤ K₂(Ω/2+σ)^{−2} (X.5a(a), two integrations by parts; valid since A, A′ are continuous), and
  |Θ_∞ − log(Ω/4π)| ≤ 7 + 2log(1+Ω/2+σ); the L² norm of the product is ≤ K₂(7+2log(1+Ω))Ω^{−3/2}.
- Resolvent piece: (log D̃ − log M)u = ∫_0^∞(D̃+s)^{−1}(D̃−M)(M+s)^{−1}u ds. First part ≤ (2log2/Ω)K₀ as in X.5a(c).
  Second part: (Ω/2−D)_+v_s has L² norm ≤ K₂(A_s)(∫σ²(Ω/2+σ)^{−4}dσ/2π)^{½} = K₂(A_s)(3πΩ)^{−½}, and
  **K₂(A_s) ≤ 2K₂/(Ω+s)** (Leibniz on A/(Φ′+s): each of the four K₂-terms of A_s is bounded by at most twice the matching
  term of K₂ divided by Ω+s; coefficients 8 ≤ 12, 3 ≤ 4, 20 ≤ 24). Integrating, ≤ 2K₂(2log2/Ω)(3πΩ)^{−½} ≤ K₂Ω^{−3/2}. □
Truncated dilates u_m satisfy the hypotheses under (Z₁), with Ω_m := inf τ on dilate m ≥ max(2c, cm) and K₀(u_m) ≤ K̄.

## 5. Theorem B′ (PROVED)
**Lemma Y.4 (diagonal survives cell by cell; answers (ii)).** Σ_m m^{−1}[⟨Θ_∞(D)u_m,u_m⟩ − 2ℓ_m‖u_m‖²]
 = ∫_1^∞ 𝔴_μ(t)|a(t)|²dt + E_diag,  |E_diag| ≤ 1.6K̄‖a‖/c + O(K₂^{♯2}log c/c²).
*Proof.* X.5a (AUDIT_8 constants) for each u_m: ⟨Θ_∞u_m,u_m⟩ = ∫_{t>m}log(τ(t)/2π)|a|²dt + err_m, since ∫|u_m|²dy = ∫_{t>m}|a|²dt
and Φ′ at y = log(t/m) is τ(t). Σ_m m^{−1}1_{t>m} = H(t), Σ_m m^{−1}ℓ_m1_{t>m} = H₁(t): this is the E.1′ harmonic cut on the
diagonal, H_N on cell N, and the integrand is H(t)log(tφ_c′/2π) − 2H₁(t) = 𝔴_μ(t) exactly. The log² cancellation (X.4/B.0)
is pointwise in t and therefore holds cell by cell. Errors: Σ_m 1/(mΩ_m) ≤ 1/(2c) + Σ_{m≥2}1/(cm²) ≤ 1.15/c. □
*Sawtooth.* H(t) = log t + γ + h(t), |h| ≤ 1/t, and 2H₁(t) = log²t + 2γ₁ + O(log t/t). So
𝔴_μ = (log t + γ)log(μt²/√(t²−1)) − log²t − 2γ₁ + O(log(μt)/t): the sawtooth part is O(1/N) relative on cell N
(relative to H_N log μ). It is part of the exact weight, not an error. **B.0 applies verbatim: 𝔴_μ ≥ log 2μ on t > 1.**

**Theorem Y.5 (Theorem B′, multi-cell Langer chirps).** On (L_η,X), with f(λ) = 0 and no gauge,
 **𝔔[ρ] = ∫_1^∞ 𝔴_μ(t)|a(t)|²dt + 𝓡_res + E**, where
- 𝓡_res := Σ_{2≤n≤X} 2n^{−½}Re∫_{y>0}G_{1n}e^{iψ_{1n}}dy, G_{mn} := [½log(τ(ms)τ(ns)/(2π)²) − ℓ_m − ℓ_n]·A_mĀ_n,
  A_m(y) := (ms)^{½}a(ms);
- **|𝓡_res| ≤ 25.3·c^{−½}·H_X·(β_η‖a‖ + 2ΛK_a)‖a‖;**
- **|E| ≤ c^{−1}[1.6K̄‖a‖ + 15√X·K̄‖a‖ + 2.6H_X²(β_η‖a‖ + 2ΛK_a)‖a‖ + 24XΛ‖a‖²] + 2H_X c^{−2}(‖a′‖₁ + (1+(2η)^{−½})‖a‖₁)²
  + O(K₂^♯√X log c·c^{−3/2})**.
*Proof.* Start from Lemma Y.1. Diagonal: Lemma Y.4.
- **Symbol replacement off the diagonal.** For m ≠ n replace ⟨Θ_∞u_m,u_n⟩ by ⟨log(Φ′_m/2π)u_m,u_n⟩ in the (m,n) term and by
  the conjugate replacement on u_n in the (n,m) term (Φ′_m(y) := τ(ms)). By Lemma Y.3 the error is
  ≤ 2Σ_{m≠n}(mn)^{−½}‖err_m‖‖u_n‖ ≤ 2‖a‖·2√X·ζ(3/2)·(2log2/c)K̄ + h.o. ≤ 15√X K̄‖a‖/c + h.o. (‖u_n‖ ≤ ‖a‖, Ω_m ≥ cm).
  After replacement the pair {m,n} contributes 2(mn)^{−½}Re∫G_{mn}e^{iψ_{mn}}dy (archimedean and both comb pieces together).
- **Non-resonant pairs 2 ≤ m < n.** G_{mn} vanishes at the ends of its support ((Z₁) and compact support), so one integration by
  parts gives |∫G e^{iψ}| ≤ ∫|G′|/|ψ′| + ∫|G||ψ″|/ψ′². By Y.2(ii), 1/|ψ′| ≤ 1/(0.77c(n−m)) and |ψ″|/ψ′² ≤ 1.7n/(c(n−m)²).
  Cauchy–Schwarz in s gives ∫|A_mA_n|dy ≤ ‖a‖², ∫(|A_m′A_n| + |A_mA_n′|) ≤ 2K_a‖a‖, and |∂_y log τ| ≤ β_η, |weight| ≤ Λ. So
  |pair| ≤ 2(mn)^{−½}[(β_η‖a‖² + 2ΛK_a‖a‖)/(0.77c(n−m)) + 1.7nΛ‖a‖²/(c(n−m)²)]. Sum with Σ(mn)^{−½}/(n−m) ≤ H_X² and
  Σ√(n/m)/(n−m)² ≤ ζ(2)X + 2ζ(3/2)√X ≤ 7X.
- **Pairs (1,n): 𝓡_res.** By Y.2(iii), ψ_{1n} has |ψ″| ≥ 0.4cn on the whole support (one sign). The second-derivative
  van der Corput lemma with amplitude (CITED: Stein, *Harmonic Analysis* 1993, VIII §1.2, Prop. 2 and Cor., c₂ = 8) gives
  |∫G_{1n}e^{iψ_{1n}}| ≤ 8(0.4cn)^{−½}‖G_{1n}′‖₁ (G vanishes at the end), and ‖G_{1n}′‖₁ ≤ β_η‖a‖² + 2ΛK_a‖a‖ (as above). With the
  prefactor 2n^{−½}: ≤ 25.3c^{−½}n^{−1}(…); sum over n ≤ X.
- **Pole.** One integration by parts in t: a⌊t⌋/t and aH(t) are continuous by (Z₁); φ_c′ ≥ c, |φ_c″|/φ_c′² ≤ 1/(c√(2η)).
  So |A_p| ≤ c^{−1}(‖a′‖₁ + (1+(2η)^{−½})‖a‖₁), |B_p| ≤ H_X·(same), and 2|A_pB_p| is the stated c^{−2} term. □

**Corollary Y.6 (a proved positive region with overlapping dilates).** On (L_η,X), f(λ) = 0, no gauge:
 **𝔔[ρ] ≥ (log 2μ − R(c))‖a‖²,  R(c)‖a‖² := |𝓡_res| + |E|**,
and for a fixed profile (a in the variable t, c-free; η, X fixed) **R(c) ≤ C₁(η,X,a)·c^{−½}log c + C₂(η,X,a)·c^{−1}log c**,
with C₁ = 25.3·H_X(2K_a/‖a‖)·(Λ/log c)+… explicit above. Hence 𝔔[ρ] > 0 for c ≥ c₀(η,X,a). The (1,n) pairs are the only
c^{−½} terms; all other cross-dilate effects are O(c^{−1}·poly(X)).
- Langer-type phases: a finite combination of prolate continuations below the plunge has the common phase φ_c times an
  amplitude whose phase is c-free (relative phase 4(k−j)arcsec ω, BRIDGE §4.1). So it lies in the class with c-free K_a: the
  corollary covers finite rung combinations, cut off to [1+η,X] and made to satisfy (Z₁).
- Honest size: the constants are crude. C₁ ≈ 50H_X K_a/‖a‖ means positivity is certified only for μ ≳ 10³–10⁴, not at μ = 15.
  The P4-gap of BRIDGE §6 is not closed by this.

## 6. What the resonances can do (answers (iii))
**Leading size for smooth profiles (ARGUED, stationary phase; the bound of Thm Y.5 is the PROVED version).** For n ≤ N_η the
(1,n) term is 2n^{−½}Re[G_{1n}(y_n)√(2π/|ψ″|)e^{iψ(y_n)−iπ/4}](1 + O((cn³)^{−½}·profile)), with weight
½log(τ_n²/(2π)²) − ℓ_n = **log(μ(1+n^{−2}))** and n^{−½}|A_1A_n|(y_n) = s_n|a(s_n)a(√(n²+1))|. For the Langer density
|a|² = (2M/π)/(t√(t²−1)) (cut off at 1+η): s_n|a(s_n)a(√(n²+1))| ≈ (2M/π)n^{−½}, so the (1,n) term is
≈ (4M/π)μ^{−½}n^{−2}log(μ(1+n^{−2})), and the total over n is ≤ (2π/3)Mμ^{−½}log(1.25μ), i.e. ≤ 2.1μ^{−½}·(log μ/log 2μ)
relative to the B.0 floor M log 2μ. Phases e^{iψ(y_n)} vary with n, so the true sum is smaller; SYNTHESIS's "≈ 10 % at μ = 15"
is consistent with this upper bound (0.43 at μ = 15) but not implied by it. This replaces SYNTHESIS's ARGUED
"c^{−½}n^{−2}log(μn)" by n^{−2}log(μ(1+n^{−2})) (the log n is cancelled by the comb's −ℓ_n).

**Prop Y.8 (worst case: Fresnel-scale amplitudes; ARGUED).** The c^{−½} gain needs K_a ≪ c^{½}. If a is concentrated in a
Fresnel window (cn³)^{−½} around s_n and in the matching window around √(n²+1), the (1,n) pairing loses its oscillation and is
of the size of the diagonal. At leading order (log-symbol replacement) its modulus is ≤ 2n^{−½}log(μ(1+n^{−2}))√(P_nQ_n), with
P_n, Q_n the masses in the two windows, while the diagonal they carry is ≥ log(μn s_n²)P_n + H_n log 2μ·Q_n (B.0(ii)). So the
2×2 block is positive, with off-diagonal ≤ **1/√(nH_n) ≤ 0.58** of the geometric-mean diagonal (n = 2: 1/√3). Windows for
different n are disjoint (s_n − s_{n+1} ≈ n^{−3} ≫ (cn³)^{−½} for n ≪ c^{1/3}), so the blocks do not add up coherently.
- **Hence P2 does not fail at leading order, even adversarially**; but on Fresnel-scale data the "error" is O(1), not
  O(c^{−½}). Smallness of P2 is a regularity statement about the data, and the claim η₂ ≤ Cc^{−½}log c holds only on
  regular profiles (Thm Y.5).
- Why ARGUED: for such data K₀ ≍ (cn³)^{½}, so the replacement error of Lemma Y.3 is n^{3/2}c^{−½}, not small for n ≳ c^{1/3};
  and the mass in the n-window also enters dilates 2,…,n, whose pairs are not tracked here.
- **Where the resonances can reach diagonal size:** only (1) at Fresnel-scale amplitudes, bounded by 0.58 as above, and
  (2) in the edge layer t − 1 ≲ c^{−2} (n ≳ c), where φ_c = O(1) and there is no oscillation at all. Region (2) is the Sonin
  edge / P3b, not P2.

## 7. Truncation jumps (answers (i)(a) without (Z₁); ARGUED)
**Prop Y.7.** If a(k) ≠ 0 at integers, u_m has a jump of size m^{½}|a(m)| at y = 0. For a half-line chirp
f = Ae^{iΦ}1_{y>0}, |f̂(τ)| ≈ |A(0)|/|τ − Φ′(0)| away from the frequency, and ⟨Θ_∞f,f⟩ − ∫_{y>0}log(Φ′/2π)|A|² =
O(|A(0)|²log Φ′(0)/Φ′(0)) (log divergence of ∫|log(τ/Φ′)|/(τ−Φ′)² between scales 1 and Φ′). Summed with weight 1/m,
Ω_m ≥ cm: **jump contribution = O(Σ_k |a(k)|²log(ck)/(ck))**, i.e. O(log c/c) relative for profiles with a(k) bounded. The
off-diagonal pairs pick up boundary terms of the same order in the integration by parts. So the integer truncation is
O(log c/c), below the resonances. Not PROVED: the half-line log-symbol bound with explicit constants is not written.

## 8. The cΛ check (answers (iv))
**Corollary Y.9 (PROVED).** Let 𝔔^κ be 𝔔 with the prime part multiplied by κ > 0 (BRIDGE §7 convention). Theorem Y.5 holds
with weight 𝔴^κ_μ = H(t)log(μt²/√(t²−1)) − 2κH₁(t) and constants multiplied by max(1,κ).
- κ ≤ 1: 𝔴^κ ≥ 𝔴 ≥ log 2μ: positive **on this cone only** (constraint 20 reading; 𝔔^κ for κ < 1 is indefinite elsewhere,
  AUDIT_8 §6).
- **κ > 1, every μ ≥ 4 with c ≥ c₀(κ):** take a single-cell profile b on [N+δ, N+1−δ] (a sub-case of (L_η,X), no resonances
  since t ≥ 2) with log N ≥ (log 2μ + 2)/(κ−1) + O(1). Then 𝔴^κ ≤ H_N log(1.2μN) − 2κH₁(N) ≤ −c′(κ)log²N < 0, while
  |E| ≤ C(b,δ)H_N log N/c (X.5 with the AUDIT_8 constants, ν₀ = φ_c′ ≥ c). So 𝔔^κ < 0 on a Langer-phase chirp at every large μ:
  positivity fails uniformly for κ > 1, as in X.7. In particular Cor Y.6 is not comb-generic.
- Multi-cell negative directions for κ > 1 at large X also exist, but the crude E_osc ∝ X/c of Thm Y.5 controls them only for
  X ≪ c; the single-cell family suffices.

## 9. What remains (honest)
1. **Edge P3b.** f(λ) = 0 is a hypothesis. The extremal has f*(λ) ≠ 0, and the edge carries −51…−78 % of the chirp value
   (AUDIT_7 §4.4, PRECHECK). Theorem B′ says nothing about it.
2. **Gauge.** No statement about Π or dist²(ρ,𝒢̄). The denominator of L′♯ is not addressed.
3. **Actual tails are outside the class.** They (i) have jumps at every integer (Prop Y.7, ARGUED only); (ii) carry mass
   ≈ (2/π)√(2η) in (1,1+η), where β_η, K_a → ∞ and the resonances s_n accumulate (the cut at 1+η leaves out exactly the
   resonant region n > N_η); (iii) have mass beyond X, where E_osc ∝ X/c is not uniform. A uniform-in-η version needs the
   Langer amplitude's t → 1 behaviour (Dunster, CITED but not used) and an edge-layer analysis at t − 1 ≲ c^{−2}.
4. **Constants.** c₀ is large (μ ≳ 10³); the gap to the certified base (μ ≤ 15) is not closed.
5. Fresnel-scale worst case (Prop Y.8) is ARGUED.
No sign of row D is claimed. L′♯ OPEN. Row D OPEN.

## 10. Labels
- **PROVED:** Lemma Y.1 (multi-cell pair expansion), Lemma Y.2 (stationary points s_n = √(1+n^{−2}), Hessian, concavity,
  non-resonance for m ≥ 2), Lemma Y.3 (operator log-symbol bound), Lemma Y.4 (diagonal = ∫𝔴_μ|a|², cell-by-cell log²
  cancellation, sawtooth O(1/N) relative), **Theorem Y.5 (Theorem B′)**, Cor Y.6, Cor Y.9.
- **CITED:** van der Corput second-derivative lemma (Stein 1993, VIII.1.2); Stirling remainder (C_Θ).
- **ARGUED:** stationary-phase leading size of the (1,n) terms (§6), Prop Y.7 (jumps), Prop Y.8 (Fresnel worst case, ≤ 0.58).
- **NUMÉRICO (check only):** g(2), g(2√2); inf|ψ″_{1n}|/(cn) = 1.11; gap constant 0.87; Hessian formula.
- **OPEN:** edge P3b, gauge Π, actual PW tails (jumps, t → 1, tail beyond X), uniform constants, L′♯, (★★).
- **Corrections recorded:** SYNTHESIS §3.3(1) resonance size: n^{−2}log(μ(1+n^{−2})) (comb cancels log n); the c^{−½}
  smallness of P2 holds only for amplitudes regular on the Fresnel scale (BRIDGE (P2) must carry K_a in η₂).
- **Do not retry:** claiming P2 smallness uniformly over all chirps with Langer phase (false at Fresnel scale, Prop Y.8);
  using (Z₁)-data as evidence about integer truncation jumps or about the edge layer t → 1.
