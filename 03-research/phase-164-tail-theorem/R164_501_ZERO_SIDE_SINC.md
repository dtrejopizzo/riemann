# R164_501 — Transport of the sinc annihilation (Thm R, Lemma 2) to the zero side at the first-contact witness

*Phase 164, round 3. Pure mathematics, no numerics, no commits. Only this file was written. No label of record changes.*
*Read first: R164_190 (identification theorem), R164_401 (Thm R, Lemma 2), R163_401 (§1.1, §2.4, Lemma 3.1, §4.6–4.8, Rem 4.8a), R163_801 (Thm 1, Thm 3, Thm 5), Paper 46 `thm:Z`.*
*Corpus check.* Grepped phases 135, 151, 163, 164 for sinc / Pólya kernel / de Bruijn / Fejér–Riesz / annihilator. The positive-annihilator theorem SA below is not in the corpus. It is a Fejér–Riesz/Akhiezer argument and is probably folklore for Toeplitz forms, so it is labelled PROVED rather than claimed as new. The Pólya kernel is phase 135 (class 𝒦, falsifier Ξ_a). dlVP is phase 151 (capped by the archimedean density).

## 0. Status table

| # | statement | label |
|---|---|---|
| Prop 1 | (the pair) Z = Σ_ρ δ_{t_ρ} and P_ζ = c₀δ₀ + 2cosh(u/2)du − ν, where ν = Σ_n Λ(n)n^{-1/2}(δ_{log n}+δ_{−log n}) + e^{−|u|/2}(1−e^{−2|u|})^{-1}du (finite part at 0), form a Fourier pair: ⟨Z,ĝ⟩ = ⟨P_ζ,g⟩. ν ≥ 0, and **supp ν = ℝ** (the archimedean density) | PROVED (Weil's explicit formula, CITED; the sign of the arch density is read off ψ's integral representation) |
| Prop 2 | (self-duality does not transport linearly) the self-dual object is the comb N (R164_401 Lem 1). Z is dual to P_ζ ∝ log-derivative of N, a non-linear image. On the zero side the self-duality m̂=m is visible only as the quartet symmetry t ↦ −t, t̄ | PROVED (observation) |
| **Thm SA** | (positive annihilator = kernel) Let 𝒜 = span{Φ̂K̂^# : Φ ∈ E_c, K ∈ 𝒟_T}, the tests that the kernel equation forces the zero measure to annihilate. If Ψ ∈ 𝒜 and Ψ ≥ 0 on ℝ, then Ψ = ĤĤ^# for some H ∈ E_c. Hence the cone 𝒜⁺ has real dimension ≤ (dim E_c)² < ∞ | PROVED |
| Cor SA.1 | (polynomial ladder) if Φ ∈ E_c and z²Φ̂ ∈ 𝒟_T, then zΦ̂ ∈ Ê_c. Consequently z^{2m}Φ̂ ∉ 𝒟_T for m = dim E_c | PROVED |
| Cor SA.2 | (no room) the zero-side analogue of Lemma 2 yields exactly W|_{E_c} = 0. For the witness F this is Σ_ρ G(t_ρ)² = 0, the circular identity of Rem 4.8a. The mechanism is **E1** (it holds for the witnesses of M_m, f_t and f_χ) | PROVED |
| Prop 3 | no nonzero test in PW_T vanishes on all on-line ordinates (zero sinc at the on-line zeros is impossible) | PROVED-CITED (Selberg's positive proportion; Jensen zero-count bound for PW_T) |
| **Prop 4** | (EF_y: the Λ-tail at real height) For y>½, with Ψ_y = G²·y/(z²+y²) ≥ 0 on ℝ: Σ_ρ Ψ_y(t_ρ) = 𝔄_y − G(iy)²𝒯(iy), with 𝒯(iy) = Σ_{log n≥2T}Λ(n)n^{−½−y} = −ζ′/ζ(½+y) − Σ_{log n<2T}Λ(n)n^{−½−y} > 0. 𝔄_y uses only the window | PROVED (explicit formula for a test of exponential decay; residue computation §4) |
| Prop 4.1 | in Prop 4 the off-line quartet at t_q has weight y/γ_q² + O(yδ_q/γ_q³). The all-height datum 𝒯 enters at relative size e^{−(log n₀−2T)y}. Translating the kernel to height a ≠ 0 replaces 𝒯 by −ζ′/ζ(½+y−ia), which has no sign. Recovering a sign there requires trigonometric positivity (3+4cos+cos2), i.e. the de la Vallée Poussin mechanism | PROVED (weights); "the only sign available at a≠0 is dlVP-type" ARGUED |
| §5 (2) | exp_* on the zero side is the Hadamard product, ξ = exp_*(Z). The comb forces Pólya's kernel Φ > 0 (CITED). This is class 𝒦 of phase 135 and contains the falsifier Ξ_a. The Fredholm/Gram determinant of the witness on node tests is ∏d_x ≥ 0 (R163_801 Thm 1). No new positivity | PROVED-CITED (record) / PROVED (Gram) |
| (★_cell), (TC), RH, row D | | **OPEN** |

**Verdict.** The sinc mechanism transports exactly, and it has **no room**. On the zero side the hole of Lemma 2 is played by the kernel equation, and the lattice is played by the node set X of the witness, which has critical density T_c/π (R163_401 2.4(i)). Thm SA shows that the nonnegative annihilated tests are precisely the squares ĤĤ^# with H in the finite-dimensional kernel. In Lemma 2 the family {|ψ̂|²} was infinite-dimensional, because the hole was wider than the lattice spacing. The zero-side annihilation therefore says only W|_{E_c} = 0, which is Rem 4.8a. Leaving the annihilator brings in ζ's Λ at all heights. With a sign, this happens only at real height (Prop 4), where the off-line zeros carry weight y/γ_q² (invisible). At complex heights the only sign comes from dlVP positivity, which is capped (W2/M). Boxed stop in §6.

---

## 1. The duality (question 1, formulation)

**Prop 1. PROVED (Weil, CITED).** For g ∈ C_c^∞(−2T,2T), or more generally for g = Ψ̌ with |g(u)| ≪ e^{−y|u|}, y>½, and Ψ holomorphic in |Im z| < y,

  Σ_ρ Ψ(t_ρ) = ⟨P_ζ, g⟩,  P_ζ = c₀δ₀ + (e^{u/2}+e^{−u/2})du − ν,

  ν = Σ_{n≥2} Λ(n)n^{−1/2}(δ_{log n}+δ_{−log n}) + pf[e^{−|u|/2}/(1−e^{−2|u|})]du.

Here (0.1) of R163_801 is rewritten in u. The polar pair Ψ(±i/2) gives the density 2cosh(u/2). For the archimedean part, ψ(z) = ∫_0^∞(e^{−t}/t − e^{−zt}/(1−e^{−t}))dt with z = ¼+iτ/2 and t = 2u gives
m(τ) = const − ∫_ℝ e^{−|u|/2}(1−e^{−2|u|})^{−1}e^{iτu}du (finite part). So the archimedean distribution is a δ₀ term plus a **negative density on all of ℝ∖0**.

*Consequences (PROVED).*
- (a) The sign on the prime side is exact and ζ-specific in its atomic part: off 0, P_ζ = (positive polar density) − ν with ν ≥ 0.
- (b) **There is no hole for ν.** The atoms have the gap (0, log 2), but ν contains the archimedean density, whose support is all of ℝ. Lemma 2 used a hole of m − 𝖢, a difference of two self-dual measures. Here the reference that would have to be subtracted is the Γ_ℝ-only distribution, and every system with ζ's Γ-factor shares it (f_t, M_m, the deletion of Prop D). The gap of the atoms is already spent: it is the regime T ≤ ½log 2 (Yoshida, Bombieri), which is contained in T_c > 0.8047.
- (c) The zero side has sign only on ℝ. An on-line t_ρ contributes |Ĥ(γ)|² to ĤĤ^#; an off-line quartet contributes 4Re(ĤĤ^#)(t_q), which has no sign (Lemma 3.3 of R163_401: cos 2Θ).

**Prop 2. PROVED (observation).** In Thm R the measure is self-dual: m̂_f = m_f, so the hole and the sign sit on the *same* measure. Here Z and P_ζ are different measures. P_ζ is (up to the archimedean and polar parts) the Λ-measure, i.e. the logarithmic derivative of the comb N under exp_* (Λ = log·exp_*^{−1}(N), multiplicatively). So the comb's self-duality, which is the FE, reaches Z only through a non-linear map. Its linear trace on Z is the quartet symmetry {t, t̄, −t, −t̄} and nothing else. A Lemma-2 argument on Z therefore needs its own hole and its own sign. §2 identifies both.

## 2. The zero-side hole is the kernel equation; the zero-side sinc is the kernel

At T = T_c let E_c = ker W_{T_c} (finite-dimensional, R163_401 2.3). By §4.6 of R163_401 and (1.1), for Φ ∈ E_c and K ∈ 𝒟_T,

  Σ_ρ (Φ̂K̂^#)(t_ρ) = W(Φ,K) = 0.  (2.1)

So Z annihilates 𝒜 := span{Φ̂K̂^# : Φ ∈ E_c, K ∈ 𝒟_T}. This is the zero-side hole: a linear family of tests on which Z integrates to 0. It is the exact analogue of ⟨η,φ⟩ = 0 for supp φ ⊂ (−X,X). It is not translation-invariant: it is a module over the witness transforms. Lemma 2 needs nonnegative members of the hole whose zeros cover the region where the sign is uncontrolled.

**Theorem SA. PROVED.** If Ψ ∈ 𝒜 and Ψ ≥ 0 on ℝ, then Ψ = ĤĤ^# with H ∈ E_c.

*Proof.*
1. Ψ = Σ_i Φ̂_iK̂_i^# is entire. As a finite sum of products of two PW_T functions it has exponential type ≤ 2T and lies in the Cartwright class. It is real and ≥ 0 on ℝ. By assumption on the forms, |Ψ| ≤ ½Σ(|Φ̂_i|²+|K̂_i|²) on ℝ, so ∫log(2+|τ|)Ψ < ∞.
2. Akhiezer–Krein factorisation (CITED: Akhiezer, *Lectures on Approximation Theory*, §59; Levin, *Lectures on Entire Functions*, Lecture 16, Thm 3). A nonnegative Cartwright function of type τ₀ is SS^# for an entire S of type τ₀/2 with all zeros in the closed upper half-plane. Here τ₀ ≤ 2T, and |S|² = Ψ ∈ L¹(ℝ), so S ∈ PW_T (Paley–Wiener). The log-weight condition passes to S, so S = Ĥ with H ∈ 𝒟_T.
3. By (1.1), polarised, and (2.1): W(H) = Σ_ρ(ĤĤ^#)(t_ρ) = Σ_ρΨ(t_ρ) = Σ_i W(Φ_i,K_i) = 0.
4. W_{T_c} ≥ 0, so W(H) = 0 forces H ∈ E_c (Cauchy–Schwarz). ∎

**Cor SA.1 (polynomial ladder). PROVED** (repaired per R164_491 F5). Suppose Φ ∈ E_c and z²Φ̂ ∈ 𝒟_T. Do not argue through Thm SA: spectral factorisation is not unique (zeros can be flipped), so Thm SA only yields *some* H ∈ E_c with |Ĥ|² = τ²|Φ̂|². Argue directly. By (1.1), polarised, W(zΦ̂) = Σ_ρ t_ρ²(Φ̂Φ̂^#)(t_ρ) = W(Φ, z²Φ) = 0, since Φ ∈ ker W_{T_c}. Then W ≥ 0 gives zΦ̂ ∈ Ê_c. *Ladder.* 𝒟_T is monotone under lower polynomial weights. So z^{2m}Φ̂ ∈ 𝒟_T (m = dim E_c ≥ 1) implies z^kΦ̂ ∈ 𝒟_T for every k ≤ 2m, in particular for k ≤ m+1. By induction on j ≤ m, W(z^jΦ̂) = W(z^{j−1}Φ̂, z^{j+1}Φ̂) = 0, which needs z^{j−1}Φ̂ ∈ Ê_c and z^{j+1}Φ̂ ∈ 𝒟_T. So Φ̂, zΦ̂, …, z^mΦ̂ all lie in Ê_c. They are linearly independent (multiplication by z has no eigenvectors), and m+1 of them contradict dim Ê_c = m. *(Reading: the witness cannot vanish to high order at ±T_c. This is the only "room" of polynomial (zero-type) multipliers, and it is absorbed into the kernel.)*

**Cor SA.2 (no room; the transported Lemma 2 is Rem 4.8a). PROVED.**
- In Lemma 2 the nonnegative hole tests |sinc·χ̂|² form an infinite-dimensional cone. This is because sinc has type π, which is the critical type for the lattice ℤ, and the hole (−X,X) with X>1 leaves the extra type π(X−1) for the free factor χ̂. Varying χ̂ moved Z(χ̂) and forced the support.
- On the zero side the uncontrolled set must be covered by zeros of nonnegative members of 𝒜. For Φ = F write a member as Ψ = G²·r with r = εK̂^#/G (ε = 1 or i by parity). Positivity on ℝ forces r to have even-order behaviour at every node, so the test must vanish on X. X is the zero set of a type-T function with density T/π: that is critical type with zero excess. Thm SA states this exactly: 𝒜⁺ ⊂ {ĤĤ^# : H ∈ E_c}, a finite-dimensional cone.
- So the whole zero-side annihilation content is "W = 0 on E_c". For the real-rooted witness F it is Σ_ρG(t_ρ)² = 0, i.e. Σ_j(P_j − N_j) = 0 (R163_401 §4.7). That is the circular identity of Rem 4.8a, verbatim.
- *Falsifiers.* No step uses Λ, the Euler product or integrality. Only (1.1), W ≥ 0 at the contact and Akhiezer are used. Thm SA therefore holds verbatim at the first contact of M_m (R163_801 Thm 5), of f_t (R163_901) and of f_χ (R163_1001), all of which have off-line zeros. **Code E1.** ∎

*Remark SA.3 (the reference "comb" on the zero side; conditional).* On the 𝒟-closure of N = ℂF̂ + span{Ĥ_x}, the quadrature 2.4(iii) (Q0, PROVED) says that Z pairs with products exactly like the positive real measure Q = Σ_x w_xδ_x. If (Q) held (OPEN, RH-neutral), η := Z − Q would annihilate all products ĤĤ^#, H ∈ 𝒟_T. This is a literal hole with Q as the comb, and the sign would be η ≥ 0 on ℝ∖X. The uncontrolled set would then be X ∪ {t_q}. A type-T test vanishing on X is cF̂ (Thm SA again), so the mechanism stops at the same point. **ARGUED** (conditional on (Q)).

**Prop 3 (sinc at the on-line zeros). PROVED-CITED.** A nonzero f ∈ PW_T has at most (2T/π)R + o(R) zeros in [−R,R] (Jensen / Levinson, CITED: Levin, Lecture 17). The on-line ordinates number ≫ R log R there (Selberg, CITED). So no test vanishes on all on-line zeros. Vanishing on a finite set of them is possible, and that is exactly the freedom (I1-b) of R163_401 §4.8, which the minimiser already uses. Nothing new.

## 3. Leaving the annihilator: where ζ's Λ at all heights enters (question 1, second half)

The only way past Cor SA.2 is a test outside 𝒜 whose prime side is computable with a sign. Within type 2T the prime side involves only the window (R163_401 §4.6: "the arithmetic of ζ at a fixed window is a finite vector"). So the test must leak beyond u = 2T. The canonical leak is a Poisson factor.

**Prop 4 (EF_y). PROVED.** Let F be the witness, G as in Lemma 3.1, y > ½, and Ψ_y(z) := G(z)²·y/(z²+y²). Then Ψ_y ≥ 0 on ℝ and is holomorphic in |Im z| < y.
1. For |u| ≥ 2T: Ψ̌_y(u) = ½G(iy)²e^{−y|u|}.
   *Proof.* For u > 2T, G²e^{−izu} decays in the lower half-plane (G² has type 2T). Close the contour downward and pick up the residue at z = −iy: (1/2π)(−2πi)·G(−iy)²·(y/(−2iy))·e^{−yu}, which equals ½G(iy)²e^{−yu}, using the parity of G. The case u < −2T is symmetric.
2. The explicit formula (Prop 1, admissible since y > ½ makes Σ Λ(n)n^{−1/2−y} converge) gives
   Σ_ρ Ψ_y(t_ρ) = 𝔄_y − G(iy)²𝒯(iy),
   - 𝔄_y := (1/2π)∫σ_TΨ_y + Ψ_y(i/2) + Ψ_y(−i/2), which uses the window only;
   - 𝒯(iy) := Σ_{log n≥2T}Λ(n)n^{−1/2−y} = −ζ′/ζ(½+y) − Σ_{log n<2T}Λ(n)n^{−1/2−y} > 0.
3. This is R163_801 Thm 3 at x = iy, taking imaginary parts: pairing t with −t gives 1/(t−iy) + 1/(−t−iy) = 2iy/(t²+y²).
4. G(iy)² = (−1)^m|G(iy)|², so the tail term has the definite sign −(−1)^m. ∎

This is the first place where **ζ individually** (Λ ≥ 0 beyond every window, i.e. the Euler product at all heights) enters a witness identity with a sign. The sign fails for f_χ (Λχ has mixed sign) and for f_t (mixed-sign coefficients, Cor R.3).

**Prop 4.1 (what the sign can see). PROVED (weights); last sentence ARGUED.**
- (i) Write K_y = y/(z²+y²) = y^{−1}(1 − z²/(z²+y²)). Since Σ_ρG(t_ρ)² = 0, Prop 4 is equivalent to Σ_ρ G(t_ρ)²·t_ρ²/(t_ρ²+y²) = −y𝔄_y + yG(iy)²𝒯(iy).
- (ii) For an off-line quartet at height γ_q > 3·10^{12}, K_y(t_q) = y/γ_q²·(1 + O(y²/γ_q² + δ_q/γ_q)). Its contribution is 4Re G(t_q)²·y/γ_q² + O(|G(t_q)|²yδ_q/γ_q³). The on-line low zeros dominate the left side. The off-line effect is suppressed by γ_q^{−2}.
- (iii) As y → ∞, the tail term is G(iy)²n₀^{−1/2−y}(1+o(1)) with n₀ = min{n: log n ≥ 2T, Λ(n)>0}. Relative to the moment terms this is e^{−(log n₀−2T)y}, which lies beyond all orders of the 1/y expansion **provided log n₀ > 2T**. *Edge case (R164_491 F6):* if log n₀ = 2T exactly (2T_c is the logarithm of a prime power), the tail is G(iy)²Λ(n₀)n₀^{−1/2−y}, of relative size O(1) against the leading term. It is then not beyond all orders, and Prop 4.1(ii)–(iii) must be read with that term kept explicitly. The conclusion of §6 is unchanged, because the off-line weight is still y/γ_q². The expansion itself is the moment hierarchy Σ G²t^{2k}, which is finite only up to the ladder order of Cor SA.1 and is annihilated there.
- (iv) To weight height a ≈ γ_q one must use K_{y,a} = y/((z−a)²+y²) + y/((z+a)²+y²). The same residue computation gives the tail −2Re[G(a+iy)²(−ζ′/ζ)(½+y−ia)]_{beyond window}, and −ζ′/ζ(½+y−ia) = ΣΛ(n)n^{−1/2−y}e^{ia log n} has no sign.
- (v) The classical way to restore a sign from Λ ≥ 0 at complex heights is a nonnegative trigonometric polynomial (3+4cos θ+cos 2θ ≥ 0). That is the de la Vallée Poussin mechanism, which yields zero-free regions of width ≍ 1/log γ and is capped by the archimedean density (phase 151, record). At the witness, where there is no margin (Rem 4.8a; Paper 48 `thm:M`(b)), any such slack estimate is **code W2/M**. (ARGUED: that no other sign-restoring device exists for Λ at complex heights; not a theorem.)

**Test of Prop 4 against the falsifiers (question 3).**
- *Circularity.* Prop 4 is not the identity Σ_j(P_j−N_j) = 0. It is a one-parameter family of distinct identities, and its y→∞ limit, multiplied by y, is that identity. But Prop 4 is a **theorem for ζ whether or not RH holds**, so by itself it yields no inequality on the off-line part.
- *f_χ, f_t.* The sign of 𝒯 fails for both. So this step does use ζ individually. That is necessary but not sufficient.
- *M_m.* In the windowed model of R163_801 Thm 5, the prime side beyond 2T is ζ's, so 𝒯 > 0 holds, while M_m has off-line zeros. For the unwindowed zero set "ζ + quartets" the tail acquires ∫_{|u|>2T}Σ_j4cos(γ_ju)cosh(δ_ju)·½G(iy)²e^{−y|u|}du. For large y this dominates n₀^{−y}, so the sign is not guaranteed (ARGUED). Either way, the sign of 𝒯 is not violated by off-line zeros as such. Consequently **no argument that uses only the sign of 𝒯(iy) can exclude a first contact** (PROVED for the windowed M_m, in the sense that M_m satisfies every hypothesis used).

## 4. Question (2): exp_* on the zero side

- **The object.** The zero-side exponential is the Hadamard product: Ξ(t) = Ξ(0)∏_ρ(1 − t²/t_ρ²), i.e. ξ = exp_*(Z) in the additive variable. On the prime side, ζ = exp_*(Λ/log), and N = comb. Both routes produce ξ: through the theta Mellin transform of N (Lemma 1 of R164_401) and through the Hadamard product of Z.
- **Positivity forced by the comb (PROVED-CITED, Pólya 1926).** Ξ(t) = ∫Φ(u)cos(tu)du with Φ(u) = Σ_n(2π²n⁴e^{9u} − 3πn²e^{5u})exp(−πn²e^{4u}) > 0. Positivity uses the theta modularity, i.e. the comb's self-duality. This is the canonical class 𝒦 of phase 135, which contains the falsifier Ξ_a (positive kernel, off-line zeros). So positivity of exp_*'s kernel does not separate (record, PROVED-CITED).
- **What would suffice is not a positivity of a measure.** RH ⟺ Ξ ∈ Laguerre–Pólya ⟺ the de Bruijn–Newman constant Λ_dBN ≤ 0 (with Λ_dBN ≥ 0, Rodgers–Tao 2020, CITED) ⟺ hyperbolicity of all Jensen polynomials (Pólya; Griffin–Ono–Rolen–Zagier 2019 prove it for each fixed degree and large shift, CITED). Each of these is an equivalent form, not a consequence of N ≥ 0.
- **The witness determinant.** On the node tests the Gram matrix is diag(d_x) (R163_801 Thm 1), so every Fredholm/Gram determinant is ∏d_x ≥ 0. On E_c the determinant vanishes by definition. Neither carries a sign beyond W ≥ 0 (PROVED).
- **Answer to (2).** No zero-side exp_* object is known whose positivity is forced by the comb and which is stronger than Pólya's Φ > 0. The S2 requirement (non-linearity) is met by exp_*, but the positivity it delivers is class 𝒦's, which Ξ_a falsifies. **DEAD [W-identification / falsifier Ξ_a].**

## 5. Falsifier summary (question 3)

| step | uses comb / Euler at all heights? | f_t | f_χ | M_m | verdict |
|---|---|---|---|---|---|
| Prop 1 (pair, sign of ν) | atoms: yes (Λ ≥ 0); arch: no | fails sign | fails sign | windowed: sign kept | tool |
| Thm SA, Cor SA.1–2 | **no** | holds | holds | holds | **E1**; output = Rem 4.8a |
| Rem SA.3 (Q as comb) | no | holds | holds | holds | E1, conditional on (Q) |
| Prop 4 (EF_y) | **yes** (𝒯 = −ζ′/ζ(½+y) − window) | sign fails | sign fails | windowed M_m: sign holds | identity; no inequality |
| Prop 4.1(iv)–(v) | yes, via trigonometric positivity | — | — | — | **W2/M** (dlVP cap) |
| §4 exp_* | yes (theta) | — | — | — | class 𝒦; falsifier Ξ_a |

## 6. Where the argument stops

> **Box (R164_501).** The sinc annihilation of Lemma 2 transports to the zero side at the witness with the kernel equation as the hole and the node set X as the lattice. **Thm SA (PROVED):** every nonnegative test annihilated by the zero measure through the kernel equation is ĤĤ^# with H ∈ E_c. The cone is finite-dimensional, because X has the critical density T_c/π, leaving zero excess type (Lemma 2 needed X > 1). Its content is W|_{E_c} = 0, which is Rem 4.8a, and the step is **E1**.
>
> To go further one needs a test outside 𝒜 with these three properties:
> - **(i)** it is nonnegative on ℝ;
> - **(ii)** its prime side involves Λ beyond the window with a **definite sign** (this is the step that would use ζ individually);
> - **(iii)** at the off-line points t_q it is comparable in size to its real-line values near γ_q, with a phase error o(cos 2Θ) uniformly in the cone.
>
> Real-height Poisson tests (Prop 4, PROVED) satisfy (i) and (ii) but give weight y/γ_q² at the off-line zeros, so (iii) fails. Height-a tests satisfy (i) and (iii) but lose (ii). Restoring (ii) by trigonometric positivity is dlVP, which is capped (W2/M). **A test with (i)+(ii)+(iii) simultaneously is OPEN.** Its existence for ζ at T_c is not shown to be weaker than (★_cell).

## 7. Ledger

| Id | content | label |
|---|---|---|
| R164_501.P1 | Fourier pair (Z, P_ζ); ν ≥ 0, supp ν = ℝ (arch density); no hole on the prime side | PROVED (Weil CITED) |
| R164_501.P2 | self-duality is of N, not of P_ζ; on Z it is only the quartet symmetry | PROVED (observation) |
| R164_501.SA | positive annihilator = {ĤĤ^#: H ∈ E_c} | PROVED (Akhiezer–Krein CITED) |
| R164_501.SA1 | polynomial ladder: z²Φ̂ ∈ 𝒟 ⇒ zΦ̂ ∈ Ê_c; finite ladder order ≤ 2dim E_c | PROVED |
| R164_501.SA2 | zero-side sinc = Rem 4.8a; E1 (holds for M_m, f_t, f_χ) | PROVED |
| R164_501.SA3 | Q = Σw_xδ_x as zero-side comb under (Q); same stop | ARGUED (conditional on (Q)) |
| R164_501.P3 | no PW_T test vanishes on all on-line zeros | PROVED-CITED |
| R164_501.P4 | EF_y with Λ-tail 𝒯(iy) = −ζ′/ζ(½+y) − window > 0 | PROVED |
| R164_501.P41 | off-line weight y/γ_q²; tail beyond all orders; complex height loses sign; sign restoration = dlVP | PROVED / last clause ARGUED |
| R164_501.X | exp_* = Hadamard; comb ⇒ Pólya Φ > 0 = class 𝒦 (Ξ_a); Gram det ∏d_x | PROVED-CITED / PROVED |
| O164.501.1 | test with (i)+(ii)+(iii) of the Box at T_c | **OPEN** |
| (★_cell), (TC), RH, row D | | **OPEN** |

## 8. Grid cells (proposal; the editor decides symbols per rule §8.3)

- **7A** (zero side × one window). New PROVED-TOOL: Thm SA (positive annihilator = kernel), Cor SA.1 (ladder). Route "zero-side sinc / Lemma 2 on Z at the witness": **DEAD [E1, no room: critical node density]**. The residue D.16-γ is untouched. Symbol: no change (◧).
- **7F** (zero side × global transforms in T). New PROVED-TOOL: Prop 4 (EF_y, Λ-tail at real height in closed form via ζ′/ζ(½+y)). Route "Λ-tail sign at the witness": **DEAD as stand-alone** (identity; off-line weight y/γ_q²; windowed M_m satisfies the sign). Complex-height variant: **DEAD [W2/M, dlVP cap]**. New live residue: **O164.501.1** (the Box). Symbol: no change (◧).
- **2A** (positivity/support × one window). Route "Thm R's sign + gap on the prime side": **DEAD**. The atomic gap (0, log 2) is not a hole of ν, because the arch density has full support, and the gap is spent in T ≤ ½log 2 ⊂ T_c > 0.8047. Symbol: no change (◩).
- Walls used: E1 (Thm SA), W2/M (dlVP), W-identification/Ξ_a (exp_*).

**Honest summary.** I did not prove (★_cell). What is proved is that the Thm R mechanism, transported faithfully to the zero side, closes on the kernel (Thm SA), and its output is the circular identity. The one place where ζ's Λ at all heights enters with a sign (Prop 4) is an identity whose off-line weight vanishes like γ_q^{−2}. The precise missing object is a test with properties (i)+(ii)+(iii) of the Box.
