# P1_BBSTAR_001 — Gap P1 (phase 204f): does there exist 𝔅_T = B_T^*B_T on 𝒳_T ⊋ P_T whose restriction is 𝒲?

phase 204f. Pure mathematics, no numerics.
Row D / L′♯: independent goal.
Inputs read: BARRIER_SOUND_001 §1 (row P1) and §3 (Gap 1, Lemma P1.1); SPEC_SIGN_OBJECT_009 (Lemma 19.1, Prop 19.2,
table X1–X5); Paper 46: thm:shape (l. 8922), thm:sos (l. 8255), lem:shape-lin (l. 8660), prop:opcalc (l. 8237),
prop:primeblind (l. 7792), def:W/eq:nuw (l. 1193), def:PD (l. 636), thm:D1 (l. 684), rem:shape-additive (l. 8554).

## Summary (≤300 words)

The P1 form «positivity in a larger space, PSD by exact BB* factorization, with the arithmetic entering only in the
restriction identity» is resolved **negatively in the class in which it can be formulated**. There are five results.

1. **Collapse lemma (PROVED, trivial).** If 𝒲 = ι^*(B^*B)ι, with ι: P_T → 𝒳_T, then 𝒲 = (Bι)^*(Bι). Enlarging the
   space adds nothing to a BB* argument: everything reduces to an explicit square root of 𝒲 in P_T. «B exists» holds
   if and only if 𝒲 ⪰ 0 in P_T (square root), so the content lies only in the class of B.
2. **Theorem P1.A (PROVED).** thm:sos extends literally to Dirichlet polynomials with arbitrary real
   frequencies, in particular log ℚ_{>0}. Hence no shift-multiplier type B (dilations
   weighted by Λ, Λ₂, μ, log, or by any Dirichlet convolution) pays for the comb with the archimedean part paying a
   constant, for T ≥ ½log3. If the archimedean part is left free, the decompositions are the certificates of
   def:PD and its value is λ_P (lem:shape-lin(ii), thm:D1).
3. **Atoms lemma (PROVED).** 𝒞^*𝒞, with 𝒞 = Σ Λ(n)n^{−½}D_n, has atoms with coefficient exactly
   log p·log q/√(pq) > 0 at log(p/q). 𝒲 does not have them. The Selberg identity Λ∗Λ = Λ₂ − Λ·log enters only in 𝒞², which
   is not PSD, and the same holds for a_P (O₁).
4. **Lemma P1.1, answered.** Φ.12 and Prop 19.2 only kill the Rankin route (products of L-functions). The bilinear forms in Λ of
   convolution type fall by P1.A and by the collapse to certificates, independently of Φ.12. Term-by-term polarization
   (non-convolutive B, truncated to the window) falls by prop:primeblind.
5. **Weil-curves reading (ARGUED, standard citation).** In Weil, the Hodge index **is not** proved by BB*, but by
   Riemann–Roch and ampleness (growth of h⁰). The only explicit BB* is the cohomological one, B = realization in H¹, which is
   built with the eigenvalues, i.e. on the zero side. The part of the form of the argument that survives is
   «h⁰», which is already indexed.

Verdict: P1-BB* is NO-GO PROVED in the convolutive class and collapses in general. Gap P1 remains open only in the
non-BB* form (PSD by Riemann–Roch-type structure), which is not new.

---

## 0. Corpus check and new reason

**Index search** (05-meta-and-planning/ROUTES-TRIED-INDEX/, README and tables) with the terms «BB*»,
«Cholesky», «SOS», «square», «Λ∗Λ», «Rankin», «Φ.12», «Prop 19.2», «C8», «cancelling base», «thm:shape», «Castelnuovo»,
«Hodge index», «Frobenius graph», «h⁰». Relevant matches:

- A_MU_FACTORIZATION_001 (b): «Cholesky grouped NO-GO (C8/thm:shape/P10)»; (a) Fejér–Riesz NO-GO; (e) Selberg = SQ.
- INV_B_001/002: ⟨Γ_g,Γ_g⟩ = 𝔞_T tautological. NO-GO in the class (dilation, convolution power, power of the
  Euler product). Residue «h⁰ outside the multiplicative diagonal».
- INV_C_001 Thm 4: no measure on log ℚ equals 𝔞_T on 𝒫_T. Pairs = atomic measure on log ℚ.
- R11_2_ORIGIN_001: «Selberg identity (Λ∗Λ) as an order-2 relation: NO-GO (C-data; comb-generic)».
- SPEC_009 X1b: Rankin f×f̄ NO-GO PROVED (Lemma 19.1 + Prop 19.2).
- ES-21 (Castelnuovo/Minkowski), P33-6 (Castelnuovo–Severi via moments), G4H-106 (finite Castelnuovo–Severi), R135_007
  (Hodge index conditional on h⁰), D_CONSTRUCTION_001 (𝔇, quadratic h⁰, Thm 3/5).
- BARRIER_SOUND_001: P1 is recorded as a «reduced/OPEN» gap, not as NO-GO.

**New reason, against C8 («cancelling base»), thm:shape and Φ.12/Prop 19.2.** C8 and A_MU (b) attack a
factorization in a **fixed basis of tests** (grouped Cholesky). thm:sos excludes squares of Dirichlet polynomials
**with frequencies in log ℕ** and constant archimedean part. Φ.12/Prop 19.2 exclude the route of products of L-functions. The
question P1, as formulated by BARRIER_SOUND, differs on two points:

- (i) the factorization space is a larger 𝒳_T, with diagonal restriction;
- (ii) the factor B is built with Λ and is quadratic in Λ, with frequencies in log ℚ (ratios n/m), not in log ℕ. That is,
  the «basis» depends on the comb (h1).

None of the recorded closures literally covers (i) or (ii). This is the written reason. The result of the memo is that
(i) collapses trivially (§1) and that (ii) falls by an extension of thm:sos that had not been written (§2). This closes the
residue with a new statement, not retrying an old one.

---

## 1. Collapse lemma: the larger space does not help a BB* argument

**Lemma 1.1 (PROVED).** Let 𝒳_T be a Hilbert space, ι: P_T → 𝒳_T linear and bounded (diagonal g ↦ (g,g), section,
inclusion in correspondences, etc.), and B: 𝒳_T → 𝒴 linear. If 𝒲(g) = ⟨ιg, B^*Bιg⟩ for all g ∈ P_T, then
𝒲 = B̃^*B̃ with B̃ := Bι: P_T → 𝒴.

*Proof.* ⟨ιg, B^*Bιg⟩ = ‖Bιg‖² = ‖B̃g‖². ∎

**Corollary 1.2 (PROVED).** For each T, *some* B̃ with 𝒲 = B̃^*B̃ on P_T exists if and only if 𝒲 ⪰ 0 on P_T (take
B̃ = 𝒲^{1/2}). Hence «the identity 𝒲 = (B^*B)|_diag» is not an identity that can be proved by structure except
within a **restricted class** of B. Outside such a class, it is the goal itself.

**Comment.** The scheme of the goal («BB* is tautologically PSD; the content is in the identity») is correct,
but by Lemma 1.1 the space 𝒳_T plays no role. It would only play a role if positivity on 𝒳_T were proved **without**
factorization, by an argument using the structure of 𝒳_T (§5). In the BB* scheme, everything is decided by the class of
B̃ = Bι. The natural classes are:

- (K1) shift multipliers with almost-periodic symbol, which include the «comb as an operator»
  𝒞 = Σ Λ(n)n^{−½}D_n and everything built with Euler via Dirichlet convolution;
- (K2) mixtures of (K1) with L¹-kernel convolutions (the archimedean part);
- (K3) non-convolutive operators (truncated to the window, Hankel-type, T-dependent).

We treat them in order.

**Direction correction (PROVED, trivial).** The goal proposes «𝒲 = 𝒞^*𝒞 − R with R ≥ 0 for another reason» as a
Weil-curves form. That direction gives 𝒲 ≤ 𝒞^*𝒞, which is an **upper** bound and contributes no sign. The useful form is
𝒲 = B^*B + R with R ⪰ 0. In that case R ⪰ 0 is a positivity statement of the same type as 𝒲 ⪰ 0 and **stronger**
(R ≤ 𝒲), unless R has a sign for a reason unrelated to the window (Bochner, or constant archimedean part). This is what
§2 measures.

---

## 2. Class K1/K2: extension of thm:sos and atoms lemma

### 2.1 Notation (verified against Paper 46)

In the convention of eq:fw/thm:Z and rem:shape-additive, for F ∈ P_T:

  𝔞_T(F) = (1/2π) ∫ σ_T(τ) |F̂(τ)|² dτ,  σ_T(τ) = m(τ) − S_T(τ),  S_T(τ) = Σ_{n<e^{2T}} v_n cos(τ log n),  v_n = 2Λ(n)/√n,

with m the archimedean symbol (C_0 plus the kernel K) and the polar term vanishing on P_T. The form only sees the Fourier
measure of the symbol on (−2T, 2T) (prop:opcalc).

For a shift multiplier B̃ with symbol b(τ) = Σ_j β_j e^{iτθ_j} (finite, θ_j ∈ ℝ arbitrary), one has
‖B̃F‖² = (1/2π)∫|b(τ)|²|F̂|². The dilations D_n on the multiplicative side are translations by log n on the additive side, so
𝒞 = Σ Λ(n)n^{−½}D_n has symbol ĉ(τ) = Σ Λ(n)n^{−½−iτ}. It is K1.

### 2.2 Theorem P1.A (extension of thm:sos; PROVED)

**Statement.** Let T ≥ ½log3. There are no almost-periodic polynomials D_i(τ) = Σ_j x^{(i)}_j e^{iτθ_j}, with
**arbitrary** frequencies θ_j ∈ ℝ (for example logarithms of rationals, or any set built from Λ, μ, Λ₂, log), and a
constant μ_0 such that

  Σ_i |D_i(τ)|² = μ_0 − S_T(τ) for all τ ∈ ℝ,  and  m − μ_0 ⪰ 0 on P_T.

*Proof.* It is that of thm:sos, word for word. That argument never uses the fact that the frequencies of D_i lie
in log ℕ. The identity is between functions of τ, so the atoms outside log ℕ appearing in Σ|D_i|² cancel
**within** the sum, and the right-hand side is what it is. Since Σ|D_i|² ≥ 0 pointwise, μ_0 ≥ sup_τ S_T(τ) = 𝒜_T
(lem:mbounds(iii)). The second condition gives λ_{∞,P}(T) ≥ μ_0. For T ≥ ½log3: 2 ∈ 𝒩_T, so 𝒜_T ≥ v_2 = 0.9802…,
while λ_{∞,P}(T) ≤ 0.311 (values cited in the proof of thm:sos). ∎

**Corollary 2.3 (PROVED).** No B̃ in K1 —in particular no combination of 𝒞, 𝒞_2 := Σ Λ₂(n)n^{−½}D_n,
𝒞_{Λlog}, M_μ = Σ μ(n)n^{−½}D_n, their products, adjoints and sums— gives 𝒲 = B̃^*B̃ + (m − μ_0) with m − μ_0 ⪰ 0, for
T ≥ ½log3.

### 2.4 Class K2: with the archimedean part free one falls into def:PD

If one allows B̃ = B_at + B_ac (atoms plus an L¹ convolution), or a remainder R that is a PD measure with no restriction on the
window, one falls into lem:shape-lin. By (i), every expression Σ Re⟨A_i∗F, B_i∗F⟩ is ∫_{(−2T,2T)} Re ℱ dν for some measure ν
on the window. By (ii), with the positive-definite part free, the decompositions are exactly the certificates of
def:PD, whose value is λ_P (thm:D1).

**Corollary 2.5 (PROVED, compilation).** In K1 ∪ K2, «𝒲 = B̃^*B̃ + R with R ⪰ 0 by Bochner» is the existence of a
dual certificate in the window T. Its existence is row D in T as read by thm:D1/thm:Z (REF-D in the corpus's
nomenclature). The larger space (Lemma 1.1) and the use of Euler to build B do not change the class.

### 2.6 Atoms lemma: 𝒞^*𝒞 versus 𝒲 (PROVED)

The goal asks to compute 𝒞^*𝒞 exactly. On the symbol side:

  |ĉ(τ)|² = Σ_{m,n} Λ(m)Λ(n)(mn)^{−½} (m/n)^{iτ}.

We group by the ratio r = n/m ∈ ℚ_{>0}. The coefficient of the atom at log r is c(r) = Σ_{n/m=r} Λ(m)Λ(n)(mn)^{−½}. Since
m and n are prime powers:

- **r = 1:** c(1) = Σ_n Λ(n)²/n. This is the constant (the analogue of «Γ^t∘Γ = q·Δ»: D_n^*D_n = I, unitarity gives only the
  scalar).
- **r = p^k (k ≥ 1):** m = p^a, n = p^{a+k}, and c(p^k) = (log p)² p^{−k/2} Σ_{a≥1} p^{−a} (with truncation, a
  finite sum). It is quadratic in log p, not linear.
- **r = p^j/q^i, p ≠ q:** m = q^i, n = p^j are the **unique** representation (unique factorization). Then
  c(p^j/q^i) = log p·log q·(p^j q^i)^{−½} > 0.

The frequencies log r, with r ∈ ℚ_{>0}, are distinct for distinct r. The Fourier measure of 𝒲 on (−2T, 2T) has
atoms only at ±log n, with n ∈ ℕ (and the atom at 0 comes from C_0), plus an absolutely continuous part (K).

**Lemma 2.7 (PROVED).** For every T with some pair p ≠ q of primes such that
|log(p/q)| < 2T and p, q < e^{2T}, for example T ≥ ½log3 with (p,q) = (3,2)— there are no α ≠ 0 and a measure ν **supported on
log ℕ ∪ (a.c. part)** such that 𝒲 = α𝒞^*𝒞 + (form of ν) on P_T. Every decomposition 𝒲 = α𝒞^*𝒞 + R forces R to
have atoms −α log p log q/√(pq) at ±log(p/q).

*Proof.* Equality of forms on P_T is equality of Fourier measures on (−2T, 2T) (prop:opcalc). The atom at
log(3/2) ≈ 0.405 is in the window from T ≈ 0.203 on. Moreover, 2, 3 < e^{2T} from T ≥ ½log3 on, and its coefficient in 𝒞^*𝒞 is
log 2·log 3/√6 ≠ 0. ∎

This agrees with INV_C_001 Thm 4 (pair forms live on log ℚ and no measure on log ℚ equals 𝔞_T). There the
object was the h⁰ count and here it is the comb-operator, so it is the same obstruction seen from B.

**Consequence.** To use 𝒞^*𝒞 one must cancel the atoms at non-integer ratios with another square having negative
atoms at log(p/q). That is precisely a sum of squares with frequencies in log ℚ and, by Theorem P1.A, it dies for
T ≥ ½log3 if the archimedean part pays a constant. If it does not pay a constant, it falls into Corollary 2.5.

### 2.8 Where Selberg (Λ∗Λ) enters: in 𝒞², not in 𝒞^*𝒞 (PROVED)

D_mD_n = D_{mn}, while D_m^*D_n = D_{n/m}. Hence:

  𝒞² = Σ_N (Λ∗Λ)(N) N^{−½} D_N = 𝒞_2 − 𝒞_{Λ·log}  (Selberg identity: Λ₂ = μ∗log² = Λ·log + Λ∗Λ, verified).

On P_T, which are even tests, ∫ĉ²|F̂|² = ∫Re(ĉ²)|F̂|² and Re(ĉ²) = (Re ĉ)² − (Im ĉ)². Moreover S_T = 2Re ĉ (truncated). This
gives the **exact symbol identity (PROVED)**:

  S_T²/4 = (Im ĉ)² + Σ_N (Λ₂ − Λ·log)(N) N^{−½} cos(τ log N),

and the square completion:

  σ_T = |1 − ĉ|² + (m − 1 − |ĉ|²).

The first summand is BB* with B = I − 𝒞, which is explicit and built with Λ. The remainder requires m − 1 − |ĉ|² ⪰ 0 on
P_T. But |ĉ|² has mean Σ_{n<e^{2T}} Λ(n)²/n ~ 2T² (Mertens), and m − 1 has a bounded floor on P_T, so the remainder is
negative for large T. For T ≥ ½log3 this is exactly a case of Theorem P1.A, with D = 1 − ĉ. In general, every
square completion 𝒲 = |1 − λĉ|² + (m − 1 − |λĉ|² + (λ − 1)S_T)… falls into P1.A for every λ.

**Where does a_P fail?** What the goal asked for is a negative certificate that the identity uses Euler. This must be
split into two.

- The Selberg identity holds for any system with an Euler product, in particular for a_P (Λ_P∗Λ_P =
  Λ_{P,2} − Λ_P·log, because ζ·∏_{p∈P}(1 − p^{−s}) is still an Euler product). Every deduction that uses only that
  structure is closed under O₁ (Euler erasure). By thm:shape(A) and prop:shape-eulerdel, which gives negative witnesses in
  T ∈ [0.60, ½log P], it does not prove the goal in those windows.
- So **there is no** «archimedean/polar» point where a_P fails within the algebra. The algebra is Euler-generic
  (R11_2_ORIGIN_001 already recorded this for Selberg as an order-2 relation, and here we confirm it for the
  operator version). Moreover, Lemma O1/C-pol (R11_2): the pole and the residue vanish on P_T. Hence the polar term cannot
  be the point of separation.
- For Epstein and DH, Λ_Q∗Λ_Q does not reduce to a Λ_{Q,2} supported on prime powers. But this does not matter, because
  P1.A uses no structure of the frequencies.

---

## 3. Class K3: non-convolutive B (truncated to the window)

The most natural candidate outside K1/K2 is **term-by-term polarization with truncation**. Let I = [−T, T] be the
support of the tests, τ_a the translation, and B_n F := 1_I τ_{log n}F − F (not convolutive). For F ∈ L²(I):

  −2Re⟨τ_{log n}F, F⟩ = ‖B_nF‖² − ‖F‖² − ‖1_Iτ_{log n}F‖²,  and  ‖1_Iτ_{log n}F‖² = ∫ 1_{x ≥ log n − T}|F(x)|² dx.

Then 𝒲(F) = Σ_n (v_n/2)‖B_nF‖² + [arch(F) − ⟨F, w F⟩], with the multiplier
w(x) = Σ_n (v_n/2)(1 + 1_{x ≥ log n − T}) ≥ ½Σ_{n<e^{2T}} v_n. The first term is explicit BB* and is **linear in Λ**
(weights √Λ, no quadrature in Λ). The remainder requires arch ⪰ w in L²(I). But Σv_n ≍ e^T (Chebyshev), while arch
has a bounded floor on P_T in the low-frequency directions. It fails for moderate T.

**Proposition 3.1 (PROVED mod. prop:primeblind).** Every decomposition 𝒲 = Σ_n ‖B_nF‖² + R in which each term of the
comb is paid for with its own square (in K1 or in truncated K3) costs, in R, at least the mass ½Σ v_n of the comb. By
prop:primeblind («a bound that treats the comb term by term costs its full mass»), R ⪰ 0 fails for T outside a
small window.

The non-term-by-term (grouped) K3's are exactly the grouped Cholesky of A_MU (b) / C8: indexed, not retried.

**K3 residue (OPEN, but not BB*).** A non-convolutive B̃, not term-by-term and not grouped in a fixed basis, whose
identity with 𝒲 is structural. By Corollary 1.2, as long as the class is not declared, «B̃ exists» is the goal. There
is no candidate other than a rewriting of 𝒲^{1/2}. I do not record this as NO-GO, but as an **empty class of candidates**.

---

## 4. Answer to Lemma P1.1

**Question (BARRIER_SOUND §3).** Do Φ.12 + Prop 19.2 kill every bilinear form in Λ, or only those going through Rankin?

**Answer (PROVED, with the following partition).**

- (a) **Via products of L-functions (Rankin, f×f̄, Kurokawa):** Φ.12/rem:shape-additive (additivity 𝔞^{L₁L₂} = 𝔞^{L₁} + 𝔞^{L₂}) and
  Prop 19.2(ii). Subtracting is rewriting the goal.
- (b) **Bilinear forms in Λ realized as B̃^*B̃ with B̃ convolutive** (𝒞^*𝒞, (I − 𝒞)^*(I − 𝒞), squares in Λ₂, μ, log,
  frequencies in log ℚ): Φ.12 does **not** kill them, it is irrelevant here. They are killed by Theorem P1.A (T ≥ ½log3), Lemma 2.7
  (ratio atoms) and, with the PD part free, Corollary 2.5 (= def:PD, value λ_P).
- (c) **Bilinear forms in Λ as 𝒞², via Selberg:** not PSD. Moreover they are Euler-generic, so O₁ and prop:shape-eulerdel
  exclude them.
- (d) **Linear forms in Λ with B ∝ √Λ** (polarization): prop:primeblind, plus P1.A when they are convolutive.

Therefore **P1 rises to PROVED at degree 2 for the BB* method**. No bilinear form in Λ realized as an explicit square,
convolutive or term-by-term, on the declared carrier, closes the sign for T ≥ ½log3. The ARGUED statement
of thm:noimport(iv)/C-pos(β) («stronger ⇒ not more tractable») **remains** ARGUED in general. What remains
PROVED is only the sub-class «PSD by explicit factorization».

---

## 5. The Weil-curves lesson: the surviving form is not BB*

Reminder (CITED, standard: Weil 1948; Grothendieck/Mattuck–Tate for Castelnuovo–Severi). On C×C over 𝔽_q, for
D = aΓ_F + bΔ + c·f₁ + d·f₂:

- The intersection numbers Γ_{F^j}·Γ_{F^k} depend **linearly** on the counts N_{|j−k|} = #C(𝔽_{q^{|j−k|}})
  (with factors q^{min(j,k)}). The Gram matrix of the correspondences is linear in the arithmetic data, just as
  𝒲 is linear in Λ. The identity Γ_F^t∘Γ_F = q·Δ (in NS) is what normalizes the diagonal. Its analogue is D_n^*D_n = I, and
  §2.6 shows that it only contributes the constant c(1).
- Positivity (Hodge index: the form is negative definite on ⟨H, F⟩^⊥) **is not proved by factoring**. It is proved
  by Riemann–Roch on the surface plus ampleness: if D² > 0 and D·H = 0, then h⁰(nD) or h⁰(−nD) grows and one reaches a
  contradiction. It is an argument about the **dimension of sections**, not about squares.
- The only explicit BB* factorization of the Weil form for curves is the **cohomological** one: Γ·Γ' = Σ tr on H^*. Its B
  is the ℓ-adic realization on H¹, whose data are the Frobenius eigenvalues α_i. On the arithmetic side, that is the
  spectral measure (zeros). Its analogue in the window is the spectral factorization: Fejér–Riesz/mass on zeros
  (A_MU (a), thm:Z), already recorded as REF-D.

**Reading (ARGUED).** The Weil pattern «positivity on a larger space with structure» has two halves:

- (W-BB*) an explicit factorization. By §§1–3 it collapses, and its cohomological version is on the zero side.
- (W-RR) a PSD proof by **counting sections**. This second half is exactly the «h⁰» row of the corpus:
  R135_007 (Hodge index conditional on h⁰), INV_B_001/002, INV_C_001 (h⁰ outside the diagonal, REF-D), and
  D_CONSTRUCTION_001 (𝔇: Thm 3, «no χ depending only on supports/orders has leading term ½I_∞»; Lemma 𝔇-Sch
  OPEN).

Hence, the part of gap P1 that BARRIER_SOUND marked as «open and unindexed» is not in BB*. The live part is in
W-RR, which is already indexed with its residue (𝔇-Sch). This memo does **not** retry W-RR.

---

## 6. Test on Mori and request to the calibrator

No numerics are needed for any statement in this memo: P1.A, Lemma 2.7 and Prop 3.1 are exact. For illustration
(optional, not necessary), the calibrator could give, at T = ½log15, on Mori's minimizer g*:

- (i) ‖(I − 𝒞)g*‖², ⟨g*, (m − 1 − |ĉ|²)g*⟩, and the check that their sum reproduces 𝒲(g*) ≈ λ_A (control of the
  identity in §2.8);
- (ii) the floor of m − 1 − |ĉ|² on P_T, expected to be of order ≲ −2T² ≈ −3.7.

Expected label: NUMERICAL. It changes no verdict.

---

## 7. Labels

| Statement | Label |
|---|---|
| Lemma 1.1 (collapse of 𝒳_T ⊋ P_T under BB*) | PROVED |
| Cor 1.2 («B exists» ⟺ 𝒲 ⪰ 0) | PROVED |
| Direction correction (𝒞^*𝒞 − R gives an upper bound) | PROVED |
| Theorem P1.A (thm:sos with arbitrary real frequencies) | PROVED |
| Cor 2.5 (K1 ∪ K2 with free PD = def:PD, value λ_P) | PROVED (by lem:shape-lin, thm:D1) |
| Lemma 2.7 (log(p/q) atoms of 𝒞^*𝒞) | PROVED |
| Identity §2.8 (S²/4 = (Im ĉ)² + comb of Λ₂ − Λ·log; σ = \|1 − ĉ\|² + remainder) | PROVED |
| Euler-genericity of the Selberg algebra (O₁) | PROVED (thm:shape(A), prop:shape-eulerdel) |
| Prop 3.1 (term-by-term polarization) | PROVED mod. prop:primeblind (PROVED in P46) |
| Lemma P1.1, partition (a)–(d) | PROVED |
| §5: Hodge in Weil via RR, not BB*; cohomological BB* = spectral side | CITED (Weil) + ARGUED (reading) |
| K3 structural residue, non-term-by-term | OPEN, no candidate |
| thm:noimport(iv)/C-pos(β) in general | remains ARGUED |

## 8. Verdict

P1 restricted to the method «quadratic operator in Λ, PSD by exact BB* factorization, in a larger space with
diagonal restriction» is **NO-GO PROVED** in the convolutive classes (K1/K2) and term-by-term (K3 polarized), for
T ≥ ½log3. The larger space collapses (Lemma 1.1). Selberg enters only in 𝒞², which is not PSD and is Euler-generic. The
Weil form that stays alive is the section-counting one (h⁰), which is already indexed. BARRIER_SOUND's gap P1 reduces to
«PSD on 𝒳_T by a non-factored argument». That is the h⁰/𝔇 row, with residue Lemma 𝔇-Sch (OPEN).

## 9. Entry for the index (README)

- **P1_BBSTAR_001 (phase 204f, gap P1, not yet audited):** BB* on 𝒳_T ⊋ P_T collapses (Lemma 1.1 PROVED:
  𝒲 = (Bι)^*(Bι); «B exists» ⟺ 𝒲 ⪰ 0). **Theorem P1.A PROVED: thm:sos holds with arbitrary real frequencies (log ℚ,
  dilations with weights Λ, Λ₂, μ, log), T ≥ ½log3**. With PD free = def:PD (λ_P). Lemma 2.7 PROVED: 𝒞^*𝒞 has atoms
  log p·log q/√(pq) at log(p/q), absent in 𝒲. Selberg (Λ∗Λ = Λ₂ − Λ·log) only in 𝒞² (not PSD, Euler-generic ⇒ O₁).
  σ = |1 − ĉ|² + (m − 1 − |ĉ|²) PROVED, remainder negative. Term-by-term polarization dies by prop:primeblind.
  Lemma P1.1: Φ.12/Prop 19.2 kill only Rankin, and the rest falls by P1.A/def:PD. Weil-curves: Hodge by RR, not BB*; the
  cohomological BB* is on the zero side. Residue = h⁰/𝔇-Sch (indexed). Do not retry BB*/explicit square roots of 𝒲
  in enlarged spaces.
