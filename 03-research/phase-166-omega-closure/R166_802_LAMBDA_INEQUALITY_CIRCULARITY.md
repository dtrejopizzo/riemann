# R166_802 — Which inequality on Λ would close row D, and why it is circular

Phase 166. Memo. No numerics. Inputs read: R166_190 (rounds 9–11), R166_501 (Thm A, Rem A.3),
R164_601 (Thm 3.1–3.3), R166_405 (families P, Q).

**Two corrections to the brief come first, because the theorems below depend on them.**
- **C1.** "Upper bounds on Λ-sums are useless" is **false as stated.** Von Koch's bound ψ(x) − x = O(x^{1/2}log²x) is an upper bound on a Λ-sum, and it is equivalent to RH. The correct statements are:
  - for a single test K, only a *lower* bound on Tail_K can exclude the witness (Thm 1);
  - in an asymptotic family K_Y, an *upper* bound O(Y^{δ'}) with δ' < δ_q would exclude it (Thm 3);
  - the upper bounds that are proved without zeros (sieve bounds) have the trivial exponent, so they exclude nothing (Thm 4).
- **C2.** "The needed lower bound ⇔ the zero exists" has the direction wrong. By the identity, the lower bound that excludes the witness is equivalent to a bound on the **true** zero sum (Thm 2). Asymptotically, a lower bound of size Y^{δ} is *implied* by an off-line zero (Landau), so a lower bound supports ¬RH. What excludes the witness is the matching O-bound, and that is equivalent to a zero-free statement. Either way the result is circular, but the circularity is not the one the brief described.

## 0. Status table

| Item | Statement | Label |
|---|---|---|
| Thm 0 | Adding a Λ-sentence true for ζ to the identity does not change the compatible set | PROVED (logic) |
| Thm 1 | Single K: exclusion ⟺ Tail_K > 𝔄_K − Q_K^{hyp} − S; any upper bound Tail_K ≤ U_K is jointly satisfiable with the witness | PROVED |
| Thm 2 | Transfer: the exclusion inequality ⟺ a zero-side inequality on the true zero sum Z_K(ζ) | PROVED |
| Prop 2.1 | Kernels localised at γ_q: Tail_K is a weighted Λ-sum twisted by n^{−iγ_q} over log n ∈ [2T_c, 2T_c+Δ] | PROVED |
| Thm 3 | Growth exponent of every twisted, polar-corrected Λ-sum beyond X is Θ − ½. Ω-size Y^{δ} ⟺ Θ ≥ ½+δ; O-bound ⟹ Θ ≤ ½+δ' | PROVED-CITED (Landau, Hardy–Riesz) + PROVED (twist, smoothing) |
| Thm 4 | Brun–Titchmarsh, Selberg sieve and large sieve are true without zeros, give exponent ½ only, and imply nothing beyond Θ ≤ 1 | PROVED-CITED + PROVED |
| Prop 4.1 | Λ ≥ 0 is a one-sided bound: a lower bound on Tail for Ψ̌ ≥ 0. It excludes only the dlVP region | PROVED-CITED (dlVP); loss = R164_601 Thm 3.3 |
| Main Thm | Boxed circularity theorem (§5) | PROVED for single K and for power-size families; ARGUED for "any inequality whatsoever" |

## 1. Setting

- Witness F of type T_c, with G = F̂ real-rooted. Hypothetical quartet at t_q = γ_q − iδ_q, 0 < δ_q < ½. X = e^{2T_c}.
- Family P (R166_501 B(3)): Ψ = G²K, with K ≥ 0 on ℝ of type ≤ Δ ("room"). The explicit formula reads
  (1.1) Z_K := Σ_ρ Ψ(t_ρ) = 𝔄_K − Tail_K(Λ),
  where 𝔄_K collects the archimedean, polar and window-prime parts and Tail_K(Λ) = Σ_{n≥X} Λ(n) n^{−1/2} Ψ̌_K(log n).
- Split Z_K = Q_K + R_K + O_K:
  - Q_K is the quartet at t_q, Q_K = 4 Re Ψ(t_q) = 4 Re[G(t_q)²K(t_q)];
  - R_K covers the other off-line quartets;
  - O_K = Σ_{γ real} G(γ)²K(γ) ≥ 0.
- Since (G²)^∨ has support in [−2T_c, 2T_c] and Ǩ has support in [−Δ, Δ], the sum Tail_K has finitely many terms: X ≤ n ≤ Xe^{Δ}.

Λ_ζ denotes ζ's von Mangoldt function, Σ_ζ its zero multiset, and Q_K^{hyp} the value of Q_K for a hypothetical quartet with given (t_q, G).

## 2. Theorem 0: the general drop-term principle

**Thm 0. PROVED.**
- Let 𝓘 be the family of identities (1.1) over all admissible K, read as constraints on (Σ, λ) with λ = Λ_ζ fixed.
- Let B be any sentence about λ alone, for example |Tail_K(λ)| ≤ U_K, Tail_K(λ) ≤ U_K, λ ≥ 0, or a sieve bound.
- Write Comp(·) = {Σ : (Σ, Λ_ζ) satisfies ·}. If B(Λ_ζ) is true, then Comp(𝓘 ∧ B) = Comp(𝓘).

*Proof.* B does not contain Σ. It is a closed true statement, so conjoining it changes no truth set. ∎

What Thm 0 does **not** say: it does not say that B is unable to imply RH. Comp(𝓘) contains Σ_ζ, whatever that is. A proof of exclusion from B therefore has to establish a property of the map Σ ↦ τ(Σ) := (𝔄_K − Z_K(Σ))_K, namely that witness-type Σ have τ(Σ) ∉ B. Thms 1–3 describe what that property must look like. Thm 0 is the abstract form of R164_601 Thm 3.1, and Rem A.3 of R166_501 (conjunctions of drop-term inequalities) is a special case of it.

## 3. Single test: the exclusion inequality is a lower bound

**Thm 1. PROVED.** Fix K ≥ 0 on ℝ with room. Assume an independent bound R_K ≥ −S, which is the (★_cell)-type input of R164_601 Thm 3.2.
- (a) Under (1.1), the witness is incompatible with "Tail_K ∈ I" (I an interval) iff every point of I satisfies Tail_K > 𝔄_K − Q_K^{hyp} + S.
- (b) Hence a one-sided upper bound Tail_K ≤ U_K never excludes the witness. A two-sided bound |Tail_K| ≤ U_K excludes it iff Q_K^{hyp} > 𝔄_K + U_K + S.

*Proof.* (1.1) gives O_K = 𝔄_K − Tail_K − Q_K − R_K. The only constraint the witness puts on Tail_K is O_K ≥ 0, i.e. Tail_K ≤ 𝔄_K − Q_K − R_K ≤ 𝔄_K − Q_K + S. This is an upper bound. It contradicts I iff I lies entirely above it. An upper bound on Tail_K together with this upper bound is satisfiable, for example by Tail_K very negative. The two-sided case uses the lower end −U_K. ∎

*Remark on signs.* The phase of K(t_q) is free inside the class K ≥ 0 on ℝ. For example, K = h h^* gives K(t_q) = h(t_q)·conj(h(conj t_q)). So Q_K^{hyp} > 0 can always be arranged. The light-cone sign Re G(t_q)² < 0 of R163_401 makes this harder, but it does not change the logical form.

**Thm 2 (transfer). PROVED.** By (1.1) with the true data, Tail_K(Λ_ζ) = 𝔄_K − Z_K(Σ_ζ). So the exclusion inequality of Thm 1(a) is equivalent to
  Q_K^{hyp} − S > Z_K(Σ_ζ) = Q_K^{true} + R_K^{true} + O_K^{true}.
This is an upper bound on the *true* zero sum by the hypothetical quartet's own contribution.
- If the witness is real (Q^{hyp} = Q^{true}, R^{true} ≥ −S), the inequality reads O_K^{true} < 0. That is false. So the inequality is true only if the witness is absent.
- Any proof of it from properties of Λ is therefore a proof of a zero-side bound in the precise sense of R166_501 Thm A(c). ∎

**Prop 2.1 (localised kernels). PROVED.** Take K Poisson- or Fejér-localised at a = γ_q (R164_601 §(iv)), meaning K(t) = k(t − γ_q) + k(t + γ_q) with k̂ supported in [−Δ, Δ]. Then
  Ψ̌_K(u) = 2 Re[e^{iγ_q u}((G²)^∨ * ǩ)(u)].
Hence
  Tail_K = 2 Re Σ_{X ≤ n ≤ Xe^{Δ}} Λ(n) n^{−1/2} n^{iγ_q} w_K(log n), with w_K = (G²)^∨ * ǩ,
and w_K is determined by the window. *Proof:* modulation rule for the Fourier transform. ∎

So, as R166_190 notes, the needed object is the frequency-γ_q Fourier coefficient of Λ just beyond X. For fixed finite Δ it is **one computable number**. The exclusion question is then whether that number exceeds 𝔄_K − Q_K^{hyp} + S, uniformly over the hypothetical parameters (t_q, G). By Thm 2, this is the same as Σ_ζ's own zero sum being small, which is a zero-side fact.

## 4. Asymptotic families: Ω and O are equivalent to zero location

Let A_γ(Y) := Σ_{n≤Y} Λ(n) n^{−1/2−iγ} − Y^{1/2−iγ}/(½ − iγ), the twisted sum with the polar term removed. Smoothed versions use weights w(log n − log Y) with w ∈ C_c^∞. Let Θ = sup Re ρ.

**Thm 3. PROVED-CITED, with the twist and smoothing steps PROVED.**
- (a) For every fixed γ: A_γ(Y) = O(Y^{Θ−½+ε}) and A_γ(Y) = Ω(Y^{Θ−½−ε}).
  - Sources: ψ(x) − x = O(x^{Θ+ε}) and Ω_±(x^{Θ−ε}) (Landau; Montgomery–Vaughan, *Multiplicative Number Theory I*, Thm 15.3). The twist n^{−iγ} and the weight n^{−1/2} transfer by partial summation, which changes no exponent.
  - In the Ω direction, partial summation recovers ψ − x from A_γ with only polynomially bounded loss in the exponent.
- (b) Hence, for δ ∈ (0, ½):
  - "A_γ(Y) ≥ cY^{δ} for unbounded Y" ⟹ Θ ≥ ½ + δ;
  - Θ > ½ + δ ⟹ A_γ(Y) = Ω(Y^{δ}).
  - "A_γ(Y) = O(Y^{δ'})" ⟺ Θ ≤ ½ + δ'. This is the Hardy–Riesz abscissa formula σ_c = limsup log|A(Y)|/log Y, applied to −ζ′/ζ(s+½+iγ) − 1/(s−½+iγ). That function is holomorphic exactly where ζ has no zeros, and σ_c = σ_h here because the untwisted coefficients Λ ≥ 0 (Landau).
- (c) Smoothed sums: S_w(Y) = (2πi)^{−1}∫(−ζ′/ζ)(½+iγ+s)Y^s ŵ(s)ds. Shifting the contour shows that a zero ρ contributes Y^{ρ−½−iγ}ŵ(ρ−½−iγ).
  - The localisation in height is only through the decay of ŵ. Over unbounded Y the largest Re ρ eventually dominates for every height.
  - So frequency γ_q does **not** isolate the quartet asymptotically. The exponent is the global Θ − ½. (PROVED.)

**Consequence.** Take a power-size family K_Y (Δ = log(Y/X) → ∞) used to exclude the quartet at δ_q. Then:
- The quartet forces |Tail_{K_Y}| to have size Y^{δ_q} through (1.1). This is the Ω direction, and it holds *because* of the zero.
- An exclusion therefore needs Tail_{K_Y} = O(Y^{δ'}) with δ' < δ_q. By Thm 3(b) this is equivalent to Θ ≤ ½ + δ' < ½ + δ_q, which is the absence of the zero.
- A lower bound of size Y^{δ_q} is equivalent to the zero's existence (Θ ≥ ½ + δ_q). It confirms the witness and never refutes it.

In both directions the needed Λ-inequality is logically equivalent to the zero-location statement being tested.

## 5. The three sieve bounds and positivity

**Thm 4. Each statement PROVED-CITED. Each is proved from the integers alone (sieve combinatorics, Λ = μ * log, duality) and uses no zero information.**
- (S1) Brun–Titchmarsh (Montgomery–Vaughan 1973): π(x+y) − π(x) ≤ 2y/log y for y ≥ 2.
- (S2) Selberg's upper-bound sieve: #{n ≤ x : n avoids residue classes a_p mod p, p ≤ z} ≤ x/L(z) + O(z²), with L(z) = Σ_{d≤z, μ²(d)=1} ∏_{p|d} 1/(p−1).
- (S3) Large sieve: Σ_r |Σ_{M<n≤M+N} a_n e(nα_r)|² ≤ (N + δ^{−1}) Σ|a_n|² for δ-spaced α_r. In the multiplicative form: Σ_{q≤Q} (q/φ(q)) Σ*_χ |Σ a_n χ(n)|² ≤ (N + Q²)Σ|a_n|².

**Why each is an upper bound that falls under Thm 1 and is too weak for Thm 3. PROVED.**
- (S1) and (S2) bound counts of primes, and hence Σ Λ(n)|w(log n)|, *from above*. The best they give for a twisted sum is |Tail_{K_Y}| ≤ C Σ_{n≤Y} Λ(n) n^{−1/2}|w| ≪ Y^{1/2}, i.e. exponent ½. By Thm 3(b) an O(Y^{1/2}) bound is equivalent to Θ ≤ 1, which is already known.
- (S3) is an upper bound on a mean square. With a_n = Λ(n)n^{−1/2}1_{[X,Y]} and Σ|a_n|² ≍ log Y, the individual-frequency bound it gives is |Tail| ≪ (Y log Y)^{1/2}, again exponent ½. Its averaged form allows exceptional frequencies, so it cannot single out γ_q.
- As two-sided bounds, they enter Thm 1(b) only through Q_K^{hyp} > 𝔄_K + U_K. The quartet's Q^{hyp} has size ≤ ∫|Ψ̌_K|e^{δ_q|u|}du, while U_K ≥ c∫_{2T_c}^{∞}|Ψ̌_K|e^{u/2}du. Since δ_q < ½, the inequality cannot hold with tail mass alone. Whether window mass could carry it is exactly the window-consistency of the falsifier f_t (R166_501 Lem A.1), which excludes it. Label: **ARGUED**, not a theorem for every K.

**Prop 4.1 (Λ ≥ 0). PROVED-CITED.**
- Λ ≥ 0 is one-sided. For tests with Ψ̌ ≥ 0 beyond X it gives Tail_K ≥ 0, which is a *lower* bound and so is the useful type in Thm 1.
- With the classical 3–4–1 kernels it yields exactly the de la Vallée Poussin region δ_q ≥ ½ − c/log γ_q, and nothing more (R164_601 Thm 3.3: the dlVP loss). The factor G² destroys Ψ̌ ≥ 0 for family P (R164_601 Thm 3.2).
- As a cone condition beyond the window together with the functional equation, it identifies ζ (R164_401 Thm R; R166_501 Rem A.3). That is the W-identification wall, not an exclusion.

## 6. Main theorem

> **Theorem (Λ-inequality circularity).** Let B be an inequality on Λ that is true for ζ.
> 1. (Thm 0) Adding B to the explicit-formula identities does not change the set of compatible zero configurations.
> 2. (Thm 1, Thm 2) For a single test K of family P, B can exclude the first-contact witness only through a **lower** bound on Tail_K exceeding 𝔄_K − Q_K^{hyp} + S. By the true identity, any such bound is equivalent to the zero-side inequality Z_K(Σ_ζ) < Q_K^{hyp} − S.
> 3. (Prop 2.1, Thm 3) For kernels localised at γ_q, Tail_K is the frequency-γ_q Λ-sum beyond X = e^{2T_c}. In power-size families, an exclusion requires its O-bound at exponent δ' < δ_q, which is equivalent to Θ ≤ ½ + δ'. A lower bound of size Y^{δ_q} is equivalent to the zero's existence.
> 4. (Thm 4) The sieve bounds (S1)–(S3) are upper bounds of exponent ½, equivalent at most to Θ ≤ 1. Positivity Λ ≥ 0 reaches only the dlVP region.
>
> **Hence no inequality on Λ that holds for ζ excludes the witness unless it is a statement about the oscillatory Λ-sum at the quartet frequency beyond the window of exactly the strength that is equivalent to the absence of the off-line zero. Such a statement is the hypothesis being tested.**

Labels:
- PROVED for single tests (items 1–2) and for power-size families (item 3, using cited Landau/Hardy–Riesz).
- **ARGUED** for "every possible inequality on Λ". A non-power, non-linear B is not covered. This matches R166_501 Rem A.3 / O166.501.1.

## 7. Falsifier and consistency checks

- **Thm A (R166_501).** Thm A requires H to use Λ beyond the window. Here: the Λ-data beyond the window must reach exponent δ' < δ_q, i.e. carry zero-location strength. Consistent, and it sharpens (N).
- **Falsifiers.** f_t shares 𝔄_K and the window, so Thm 1 applies to it verbatim. M_m = ξ·∏R_j has no Λ, and its Tail is β_q-modified (non-atomic). (S1)–(S3) fail for it as statements about integers, consistent with Thm A(b).
- **Identification.** The Λ ≥ 0 cone together with FE gives only ζ (Thm R). Prop 4.1 is consistent with this.
- **Von Koch check.** C1 is forced by von Koch: an upper bound can imply RH. Thm 3(b) is the correct form.
- **Finite sums.** A finite Tail_K (fixed Δ) is one number. Thm finZ (Paper 46 §7: no finite zero set carries a certificate) is consistent with item 2, since no single K excludes the witness without a zero-side input.

## 8. Ledger

- PROVED: Thm 0, Thm 1, Thm 2, Prop 2.1, Thm 3(c) and the transfers in Thm 3(a,b), and the exponent comparisons in §5.
- PROVED-CITED: Landau Ω/O for ψ (MV Thm 15.3), Hardy–Riesz abscissa formula, Landau's theorem σ_c = σ_h for nonnegative coefficients, (S1) Montgomery–Vaughan 1973, (S2) Selberg, (S3) Montgomery / Montgomery–Vaughan large sieve, dlVP.
- ARGUED:
  - the "tail mass" inequality in §5 for all K;
  - the extension of the Main Theorem to arbitrary non-power, non-linear B (O166.802.1, linked to O166.501.1).
- Corrections recorded: C1 (upper bounds can be decisive, by von Koch) and C2 (Ω-lower bounds confirm the zero and do not exclude it).
- Grid: cell "new Λ-inequality beyond the window" is **NO-GO (circular)**. Reopening it requires a B that is neither power-size nor a single-K drop term.
