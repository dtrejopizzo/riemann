# R162_1603 — One signed Euler-channel scalar (target R-B of R162_1501) — **NO-GO (PROVED)**, with four exact structures

Note. Pure mathematics, no numerics.
Inputs: README (F1–F4), R162_590, R162_1501 (Lemma D, §5 R-B), R162_1201 (Thm 1.2, Thm 2.1 (S_m), Thm 2.2, Thm 3.1,
Thm 5.1), R162_1502 Lemma 1 (collar spill C_N = −ZXZ⁻¹ on the collar), R162_406 (composite-threshold cancellation),
R162_802 (O802.1).

**Labels.**
- Prop H (H_sign holds under the minimal oscillation budget: S(F) = 2 even, S(F) = 3 odd) PROVED.
- Lemma S (H_sign forces a simple contact, dim N = 1) PROVED. **New.**
- Lemma E (edge–sign coupling: x ≥ 0 ⇒ F(T⁻) ≥ 0, via the log singularity of κ) PROVED (one-sided limit assumed). **New.**
- Thm P (Euler positivity lock: every Λ/1/μ/log Dirichlet combination on the Gamma lattice is a positive multiplier) PROVED. **New.**
- Thm R (dual-cone reduction: R-B ⟺ Gate 1 on N, stated as one positive functional) PROVED.
- Thm Q (quantitative form: R-B ⟺ bounded resolvent pairing of one vector, which is the rate law #13) PROVED
  (simple gapped contact, which Lemma S supplies).
- Thm X (the exact Euler-scalar identity Σ_m γ_m(S_m), sampling at log p ± log n; its sign audit) PROVED as an
  identity. NO-GO as a mechanism.
Gate 1 OPEN. No label moves.

## 0. Corpus check

I grepped "Euler-channel", "positivity lock", "dim N", "simple contact", "edge trace", "log(t−T)", "dual cone" in
phase 162 and R155/R160. What exists: R-B is stated only in R162_1501 §5. Edge traces u(T⁻) appear only in R162_802
(O802.1), as open. Coherence is only float-observed (R162_1501 §4). Not found: Lemma S, Lemma E, Thm P, Thm R, Thm Q.

## 1. Falsifier lines, stated first

The requested closing step is: "under H_sign, an exact λ = 0 identity forces one Euler scalar E_γ(F) = Σγ_m x_m
(γ_m > 0) to be ≤ 0". Each line below says where it breaks.

| model | H_sign available? | Euler multiplier on the lattice | where the closing step fails |
|---|---|---|---|
| deletion Λ1_{n≥5} | yes (Prop H is weight-blind) | Σ_{n≥5}Λ(n)n^{−σ} > 0 | Thm P holds verbatim: every Euler scalar stays coherent. Deletion has first contacts, so no identity built from Euler scalars alone can close |
| κ-models | yes | positive | same |
| Λχ₂ | yes | −L′/L(σ,χ) takes both signs (n = 2 term dominates, χ(2) = −1) | the Euler scalar is **not** sign-determined by H_sign. R-B cannot even be formulated. A proof passing here "fails" for the wrong reason |
| DH | Prop H only after its own lattice a_m = 2m + 3/2; Prop N1 (positive ground state) fails because v_n is signed | signed coefficients | H_sign is not implied. First contacts with x ≠ 0 exist (R162_102) |
| Beurling | yes | positive (−ζ_B′/ζ_B > 0 for σ > 1) | Thm P holds verbatim, because Λ_B*1 = log holds |

Conclusion of the table. Coherence is weight-blind. The Euler scalars are positive for every nonnegative weight. The
sign reversal must therefore come from a non-Euler term. §5 shows that all such terms are weight-blind in form.

## 2. H_sign from the oscillation budget

Notation (R162_1201):
- x_m = ∫_I F e^{a_m u} du = εK_F(a_m), with a_m = 2m + ½.
- G(t) = Σ_{m≥1} x_m e^{−a_m t} = (𝒦F)(t) for t > T.
- H_sign: after replacing F by ±F, x_m ≥ 0 for all m. This implies G > 0 and G is completely monotone on (T, ∞).

**Prop H.** Let 0 ≠ F ∈ P_T.
- If F is even and S(F) ≤ 3, then S(F) = 2 and H_sign holds.
- If F is odd and S(F) ≤ 3, then S(F) = 3 and H_sign holds.

*Proof.*
- An even F cannot change sign at 0, and its sign changes come in ± pairs, so S(F) is even. Prop N2 gives S ≥ 2, so
  S = 2.
- By Lemma D, the real zeros of K_F number at most 2. They are ±½ (Tate). So K_F has constant sign on (½, ∞).
- Odd case: K_F is odd and vanishes at 0 and ±½. Lemma D(ii) gives S ≥ 3. With S = 3 there are no other real zeros.
- In both cases x_m = εK_F(a_m) have one sign. ∎

At S = 4 (even), Lemma D permits a pair of zeros ±b with b > ½. It therefore does not imply H_sign. The budget in
Prop H is exactly the Lemma D threshold. So H_sign is proved under R-A with S₀ = 2 (even) or 3 (odd). Otherwise it is
the single hypothesis.

## 3. Two structural consequences of H_sign

**Lemma S (simplicity).** If H_sign holds for every 0 ≠ F ∈ N, then dim N = 1.

*Proof.*
- Put K = {F ∈ N : x_m(F) ≥ 0 ∀m}. By Müntz faithfulness (eq:Gammaenergy), K ∩ (−K) = {0}.
- If dim N ≥ 2, take a 2-plane V ⊂ N and its unit circle 𝕊. Then 𝕊 = (𝕊∩K) ⊔ (𝕊∩−K). The two pieces are disjoint,
  closed (x_m is continuous) and nonempty (F ↦ −F).
- This contradicts the connectedness of 𝕊. ∎

So the H_sign contact is automatically the simple contact that R162_1402 Thm 3(b) and R162_1502 Thm 5 had to assume.
The gap hypothesis (isolation of 0) is still separate.

**Lemma E (edge–sign coupling).** Let F ∈ N have a one-sided limit f₀ = F(T⁻). Then as t ↓ T,

  G(t) = −(f₀/2)·log(t − T) + O(1).

Hence H_sign (x ≥ 0) forces f₀ ≥ 0, and by parity F(−T⁺) = εf₀.

*Proof.*
- κ(u) = e^{−u/2}/(1 − e^{−2u}) = 1/(2u) + O(1) as u ↓ 0.
- Therefore G(t) = ∫_{T−η}^T f₀/(2(t−u))du + O(1) = (f₀/2)log((t−T+η)/(t−T)) + O(1).
- If f₀ < 0, then G → −∞, which is impossible when x ≥ 0. ∎

Reading.
- This is the only place where coherence reaches the **edge trace** u(T⁻), the object of O802.1.
- It is archimedean (only κ enters), hence weight-blind: it holds for deletion and for Beurling.
- The interior equation shares the same log singularity at the edge (the finite-part 𝒦_I gives +(F(T)/2)log(T−t)). So
  f₀ is not pinned by HF = 0 to have a sign. The edge coupling adds no constraint that deletion lacks.

## 4. Positivity lock

**Thm P.** For σ > 1, each of the following is > 0:
- ζ(σ) = Σ n^{−σ};
- 1/ζ(σ) = Σ μ(n)n^{−σ};
- −ζ′/ζ(σ) = Σ Λ(n)n^{−σ};
- −ζ′(σ) = Σ log n·n^{−σ};
- and any product of these.

Consequently, for x ≥ 0 and every s with s + log 2 > T, every Euler scalar of the form

  E_α(s) := Σ_n α(n)n^{−½}G(s + log n) = Σ_m x_m e^{−a_m s}·𝔇_α(2m+1),   𝔇_α ∈ {ζ, ζ⁻¹, −ζ′/ζ, −ζ′, products},

is ≥ 0, and is > 0 unless x = 0.

*Proof.*
- Positivity: ζ(σ) > 0 (sum of positive terms). ζ has no zero on σ > 1 (Euler product), so ζ⁻¹ > 0.
- −ζ′/ζ = Σ Λ n^{−σ} > 0, and −ζ′ = ζ·(−ζ′/ζ) > 0. This last step is Λ*1 = log.
- Resummation: substitute G(s + log n) = Σ_m x_m n^{−a_m}e^{−a_m s}. This is Thm 3.1 of R162_1201. Fubini holds by
  absolute convergence on s + log n > T. ∎

Reading.
- Λ*1 = log, in operator form M(Λ)Z = M(log) = [X, Z] (so M(Λ) = X − ZXZ⁻¹; this is R162_1502 Lemma 1), acts on the
  lattice as the scalar identity (−ζ′/ζ)·ζ = −ζ′ for each m. That identity is a relation between **positive**
  multipliers. It cannot turn a coherent scalar into an opposite-sign one.
- The same lock holds for every weight a ≥ 0: take 𝔇_a = Σ a(n)n^{−σ} > 0. It holds for Beurling.
- Opposite signs appear only after analytic continuation off σ > 1. The reflection gives ζ′(−2m), whose sign is
  (−1)^m (item #11 of R162_1501, closed in R162_402/1101), or a character (Λχ₂).
- **So no identity among absolutely convergent Euler scalars can carry the reversal.**

## 5. The exact Euler-scalar identity and its sign audit

**Thm X.** Fix p with log p > T, and put κ_p := κ(log p − ·)1_I. For F ∈ N, with r = AF ∈ Tate,
⟨HF, Πκ_p⟩ = 0 expands as follows, with γ_m = p^{−a_m} and all sums absolutely convergent:

  Σ_m p^{−a_m}[(μ_m^reg − T)x_m + x′_m] + (Hankel)_p
   − Σ_{n∈N_T} w_n ( 𝒦[F]_{>}(log p + log n) + 𝒦[F·1_{u<T−ℓ_n}](log p − log n) )  = ⟨r, Πκ_p⟩ = 0.     (X)

Here 𝒦[·](s) is the archimedean potential sampled at s. The first comb family samples G at the multiplicative points
log(pn). The second samples the potential of the **sub-window** restriction of F at log(p/n).

*Proof.*
- Take Σ_m p^{−a_m}(S_m) of R162_1201 Thm 2.1, which is legitimate because Σ_m p^{−a_m}e^{a_m T} < ∞.
- Resum each Dirichlet family by Σ_m n^{∓a_m}p^{−a_m}e^{a_m u} = κ(log p ± log n − u), valid on the relevant range
  of u.
- The combinations n^{2m}(x_m − ρ⁺_{n,m}) = ∫_{−T}^{T−ℓ_n}Fe^{a_m u} give the sub-window term.
- The Tate side vanishes because Πκ_p ⊥ Tate. ∎

Averaging (X) over p with weights w_p Λ-sums gives the Λ*Λ-sampled scalar Σ_{p,n}w_pw_nG(log pn). Inserting Z (the
1-channel) converts Λ*Λ-type sums into Λ*1 = log sums via Thm P. That is the only way Λ*1 = log enters (X).

Sign audit under H_sign (x ≥ 0):
- (a) Σ p^{−a_m}(μ_m^reg − T)x_m: its sign is fixed only if μ_m^reg < T for all m. That fails for large m
  (μ_m^reg ~ log m). **No sign.**
- (b) x′_m = ∫uFe^{a_m u}: this is not a function of x. H_sign constrains only full-window moments. **No sign.**
- (c) G(log pn) terms: coherent, with sign −σ in (X) (Thm P).
- (d) Sub-window potentials 𝒦[F1_{u<T−ℓ_n}]: these are moments of F restricted to [−T, T−ℓ_n]. H_sign and Lemma D say
  nothing about them. A 2-node F restricted to a sub-window is not coherent in general. **No sign.**
- (e) Hankel couplings e^{±(a_m∓a_k)T}x_k/(a_m ∓ a_k): signs alternate with k − m. **No sign.**

So the only coherent block is (c). It is exactly balanced by (a), (b), (d), (e), which have no sign. Forcing (c) to
vanish or to reverse needs a sign for (b) + (d). These are interior, sub-window data: the collar residual at ½log n
versus ½log nm of O802.1.

Evaluated at a composite threshold n = n₁n₂ ∈ N_T, the Λ-specific coefficient of (d) is (Λ*1 − log)(n) = 0. This is
exactly the R162_406 cancellation. On the unregularised side it is the Ward defect B_a = DS(a*1 − log) of R162_204,
which vanishes at a = Λ. So the step that would read Λ*1 = log **deletes** the only Λ-specific term instead of signing
it.

## 6. Reduction theorems

**Thm R (dual cone).** Let the contact satisfy H_sign (so N = span F by Lemma S, and x(F) ≥ 0, x ≠ 0). Let ν ≥ 0 be a
nonzero finite measure on (T, ∞) with ∫e^{−a_m t}dν e^{a_m T} summable. Put Φ_ν := Π∫κ(t − ·)1_I dν(t). Then:

  ⟨F, Φ_ν⟩ = ∫G dν > 0.

Hence no exact identity can give "∫G dν ≤ 0" unless the contact does not exist. R-B for ν is equivalent to
Φ_ν ⊥ N, i.e. Φ_ν ∈ closure ran H. On the H_sign class this is equivalent to Gate 1. Every Euler scalar
(ν = Σ c_n w_n δ_{log n}, c_n ≥ 0) is of this form.

*Proof.* G > 0 on (T, ∞) (x ≥ 0, x ≠ 0), and Fubini. Then N^⊥ = closure ran H (H self-adjoint), and N = span F. ∎

**Thm Q (F1, quantitative).** Assume the contact is simple and gapped (dim N = 1 by Lemma S; the gap is assumed), and
ψ_T → F along T ↑ T_*. Then for Φ = Φ_ν:

  ⟨Φ, H_T⁻¹Φ⟩ ≥ |⟨Φ, ψ_T⟩|²/λ(T),   with ⟨Φ, ψ_T⟩ → ∫G_F dν > 0.

So R-B, in the form "Φ ∈ ran H_{T_*}", holds iff the resolvent pairing stays bounded. That is the rate law
|E_ν(ψ_T)|² = O(λ(T)), i.e. R162_1501 #13 restricted to one positive functional.

*Proof.* Spectral theorem on P_T, keeping only the bottom term. Then norm continuity of ψ ↦ ⟨Φ, ψ⟩. ∎

**F1 reading.**
- For T < T_*, H_T is invertible. So Φ ∈ ran H_T is trivially true, and the λ-version of (X) reads
  E(ψ_T) = λ(T)⟨ψ_T, h_T⟩.
- If a λ-independent sign estimate "weight-free side ≤ 0 whenever x ≥ 0" existed, it would contradict the bottom
  eigenvectors at T < T_*. Those are coherent whenever S(ψ_T) = 2 (Prop H) and have λ > 0.
- Therefore the sign bound must use λ = 0 non-perturbatively. Thm Q says that using it is the rate law, which is E1.

## 7. Falsifiers F1–F4

- **F1.** Passed only in the sense of Thm Q: λ = 0 enters through ran H, and that is Gate 1 / the rate law. No new use.
- **F2.** (X) is linear in F; the PC orientation does not appear. H_sign is a cone condition, not a square, so it is
  not F2-dead by itself. But its only sign-carrying block, (c), is fixed by Thm P for every a ≥ 0. Not passed.
- **F3.** Failed. Thm P and Prop H hold for deletion, κ and Beurling. For Λχ₂ the scalar has no sign. The Λ-specific
  term of (X) at composite thresholds is (Λ*1 − log) = 0 (R162_406).
- **F4.** (X) is exact at finite T (no graph limit). The proof dies at Thm P / Thm R, not at F4.

## 8. Verdict and the single hypothesis

- H_sign is PROVED under S(F) ≤ 3 (Prop H). Otherwise it is the single hypothesis. It forces simplicity (Lemma S) and
  a nonnegative edge trace (Lemma E).
- The requested contradiction "Σ Λ(n)(positive)G(log n) = weight-free terms of opposite sign" does not exist in the
  absolutely convergent Euler channel (Thm P, the positivity lock).
- In the exact identity (X), the opposite-sign side consists of interior sub-window moments and x′_m. Their
  Λ-specific coefficient at composite thresholds is killed by Λ*1 = log (R162_406).
- R-B is logically Gate 1 on the coherent class (Thm R), quantitatively the one-functional rate law (Thm Q).

**NO-GO (PROVED).** No label moves.

**Surviving candidate.** A sign for the sub-window moment family (d) of a 2-node radical vector. For example: "the
restriction of F to [−T, T − ℓ_n] has at most 1 sign change". Via Lemma D this would sign (d). It is weight-blind as
stated, so it must be coupled to a term that fails for deletion (a′ ≠ 1 in R162_1502 Prop 3) before it can close
anything.

For R162_590: add "R-B / one Euler scalar — positivity lock (Thm P) + dual-cone reduction (Thm R) — NO-GO; residual:
sign of sub-window moments (d)".
