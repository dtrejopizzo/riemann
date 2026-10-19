# P2_SCHUR_001 — Exact Schur complement «Euler ⊕ gap» (gap P2, phase 204i)

**Single file.** No own computation; numeric requests go to the calibrator (§5).
---

## Summary (≤250 words)

I build the partition that BARRIER_SOUND_001 §Gap 2 proposes for cor:shape(b). Block A is the Euler combs
R_P = (ζP)(∂)g from Lemma R. Block B is the post-cancellation FF.1 exterior datum, Ψ̌ = Σ_{N≥μ} c_N N^{−½} τ_{log N} g, which
carries the gap c_N = 0 for 2 ≤ N < μ. The central result is elementary and **PROVED, given Lemma R**. Since Lemma R gives
𝒲(R_P, X) = 0 for **every** X, block A lies inside the radical of 𝒲. Hence **𝒲_AA ≡ 0 and 𝒲_AB ≡ 0 exactly**, not
«archimedean ≻ 0» (Lemma P2-S.1).

Consequently the Schur complement does not exist in the requested sense: 𝒲_AA is singular, and the generalized
complement (Moore–Penrose) is S = 𝒲_BB = 𝒲|_B. This is 𝒲 in the quotient by the radical, already recorded as Π.3 (PI_MU_001) and Lemma I.1.
Haynsworth's formula degenerates to In(𝒲) = (0,0,dim A) + In(𝒲_BB). Question (1) has a negative answer: 𝒲_AA is not
arch|_A. What holds is arch|_A = comb|_A. In (2), what remains in 𝒲_BB is the full comb via ratios N′/N (K1.1′). This
is R-K1, not something «almost archimedean». In (3) the coupling is zero, so there is no premise (iii) left to couple. In (4) the
conjunction collapses: the Euler premise only **removes** block A, and all the sign is left in 𝒲_BB, which is REF-D.

Variant with A' = positive archimedean part (block A_⊥⊥(1) of LEMMA_I3): it is a duplicate. I also examined the variant
with the split form arch − comb: the coupling falls into the DD/EE norm bound. **Verdict: NO-GO (PROVED) for
«exact Euler/gap Schur» as a method.** Gap P2 itself, the branch composition *rule*, remains **OPEN**. This memo
closes a method, not the rule, and leaves a shape lemma for any future attempt (Lemma P2-S.3).

---

## 0. Index and corpus check (mandatory)

I grepped `05-meta-and-planning/ROUTES-TRIED-INDEX/` for «Schur», «Haynsworth», «LEMMA_I3», «I.3», «R-K1», «Lemma R», «gap»,
«conjunction», «cor:shape», «A_⊥⊥». What appears:

- **LEMMA_I3_001 (README l.538):** exact pencil A(c) = Lᵀ[(1−c)C ⊕ (A_⊥⊥(1) + (1−c)Q/C)]L. A_⊥⊥(1) ≻ 0 with gap 3.77. It is
  𝒲 in the quotient by the gauge, i.e. (★★) in block form. «Comb modulo gauge ≽ 0» is FALSE.
- **Lemma I.1 (SPEC_004, l.536):** Haynsworth + Guo. The sign is in the complement, which is REF-D.
- **Q2_LADDER_001 (l.517):** Lemma R PROVED. Restriction **R-Q2:** levels, classes p and divisor bands are coordinates
  inside the radical.
- **K1_OSG_001 (l.511):** restriction **R-K1**. The gap only protects products NN′, and the window's atoms enter via
  ratios N′/N.
- **PI_MU_001 (l.524):** Π.3 PROVED (Guo). 𝒲 descends to Π_μ(𝒟). 𝒢̄_T is identical for Λ, a_P, cΛ, Beurling and DH.
- **AUDIT_202_R1_001 (l.582):** the pattern «each falsifier falls through a different hypothesis» is just a partition of
  (★★). No hypothesis appears in the statement: only the shape changes.
- **DD_001 / EE_001 (l.484–485):** Schur via norms. ‖QGp‖/√ℓ(p) = 0.644. The required bound is 0.82/0.95. Coercivity via
  norms NO-GO.
- **AUDIT_14_B (l.53, l.94):** Eberwein's inertia identity is a duplicate of the 2×2 polar Schur.

**New reason, in writing:**
- LEMMA_I3 defined the block by the **gauge** (𝒢_T, two Fourier intervals, no ℕ; PI_MU Π.0′).
- R-K1 deals with Hankel forms at the boundary.
- DD/EE bound the coupling by **norms**.
- Here block A is defined by **Euler arithmetic** (combs (ζP)(∂)g with P a finite Dirichlet polynomial, where ℕ does enter). The
  B block is defined by the **gap** of the Möbius lattice. And the **exact** identity of the coupling is requested.

The hypothesis that changes is that the partition is dictated by the objects that cor:shape(b) names. That difference would evade the reason
for LEMMA_I3's failure (the gauge is Λ-blind) and that of DD/EE (norms lose the sign) **if** 𝒲_AB were nonzero and exact.
§1 shows that it is not. That is why the result is a closure of the method and not a repetition.

---

## 1. The partition and the three blocks

### 1.1 Objects

Fix T and μ (Mori level, μ = 15 in the test). Let g be in the core with A(g) = 0 (B(g) = 0 by the usual reduction of the class). I use
the registered identities:

- **Lemma R (Q2_LADDER §1, PROVED given Guo L4.4):** for every finite Dirichlet polynomial P,
  R_P := (ζP)(∂)g satisfies 𝒲(R_P, X) = 0 for **every** X in the class of def:ext.
- **FF.1 / GG (PROVED with the AUDIT_28 corrections):** with M_μ the level-μ mollifier, Σ c_N N^{−s} = ζM_μ − 1 and
  c_N = 0 for 2 ≤ N < μ. One has the identity Ψ̌^{[μ]} = R_{M_μ} − g, i.e.

  g = R_{M_μ} − Ψ̌,  Ψ̌ = Σ_{N≥μ} c_N N^{−½} τ_{log N} g.

### 1.2 Definition of the blocks

- **𝒜 (Euler block):** 𝒜 := span{R_P : P a finite Dirichlet polynomial} (closure in the form's topology). Here live
  the subcombs p|N, the mollifiers and the «coordinates inside the radical» of R-Q2.
- **ℬ (gap block):** ℬ := span{Ψ̌_h : h admissible test}, with Ψ̌_h the post-cancellation exterior datum of h. It is the natural
  algebraic complement, because every test h is written h = R_{M_μ}(h) − Ψ̌_h.

The partition is direct in the quotient by 𝒜 ∩ ℬ. If part of Ψ̌ falls into 𝒜 it is absorbed, and nothing that follows depends on
the choice of complement.

### 1.3 Lemma P2-S.1 (diagonal and cross blocks). **PROVED (given Lemma R).**

Let 𝒲 be the full form of def:ext, or its window restriction, whichever form Lemma R holds in. Then:

(a) 𝒲_𝒜𝒜 ≡ 0;
(b) 𝒲_𝒜ℬ = 𝒲_ℬ𝒜 ≡ 0;
(c) 𝒲_ℬℬ(Ψ̌_h, Ψ̌_h) = 𝒲(h, h) for every h.

*Proof.*
- (a) and (b) are Lemma R with X ∈ 𝒜 ∪ ℬ. 𝒲(R_P, X) = 0 for every X, and by symmetry also 𝒲(X, R_P) = 0.
- (c) Expand 𝒲(h,h) = 𝒲(R − Ψ̌, R − Ψ̌) with R = R_{M_μ}(h). By (a) and (b) the three terms containing R vanish.
  □

**Answer to (1).** 𝒲_AA is not «arch|_A ≻ 0». It is **zero**. By blocks of the decomposition def:W = arch − comb + polar,
what holds on 𝒜 is arch|_𝒜 + polar|_𝒜 = comb|_𝒜. It is an exact cancellation, not a positive form with a gap.

LEMMA_I3 already saw this on the gauge side: C_RR = (arch + 2AB)|_𝒢 has inertia (2,0,dim 𝒢 − 2), with a great deal of nullity, and is not
at gap scale. The gap 3.77 of A_⊥⊥(1) lives in the **complement** of the radical, not in the radical. My question (1) conflated
these two sites. Mori's smallness remains a carrier restriction, as LEMMA_I3 says.

---

## 2. The Schur complement

### 2.1 Degenerate Haynsworth (PROVED)

Since 𝒲_𝒜𝒜 = 0 is singular, the classical complement S = 𝒲_ℬℬ − 𝒲_ℬ𝒜𝒲_𝒜𝒜^{−1}𝒲_𝒜ℬ is not defined. The generalized one, with the
pseudoinverse, is

  S = 𝒲_ℬℬ − 0·(0)^†·0 = 𝒲_ℬℬ.

The rank condition of the generalized Haynsworth formula (ran 𝒲_𝒜ℬ ⊂ ran 𝒲_𝒜𝒜) holds trivially, because both are
0. Hence

  In(𝒲) = (0, 0, dim 𝒜) + In(𝒲_ℬℬ).

This is **exactly** Π.3 (PI_MU_001: «𝒲 descends to the quotient») and the «radical ⊕ quotient» structure of Lemma I.1, now
with the radical enlarged from the gauge 𝒢_T to 𝒜 (𝒢̄_T ⊂ 𝒜 ⊂ rad 𝒲 by Guo).

### 2.2 What remains in 𝒲_ℬℬ: answer to (2). PROVED in shape, OPEN in sign

By Lemma P2-S.1(c), 𝒲_ℬℬ[Ψ̌_h] = 𝒲[h]. This is GG's linear identity already recorded, W_T(g) = 𝒲[Ψ̌], and also R-Q2:
«W_T(g) = 𝒲[0/1 μ-rough comb]».

What comb does it contain? In Ψ̌'s Toeplitz form (thm:ext-half), atom n of the window's comb pairs translates
τ_{log N}, τ_{log N′} with N′/N ≈ n. This is Lemma K1.1′ (PROVED). Its exact contribution for n < μ is

  Σ_{P∈[μ², μ²n)} (c∗c)(P) P^{−½} G(log(μn/P)) ≠ 0.

The gap c_N = 0 for 2 ≤ N < μ eliminates the **products** NN′ < μ², but does not eliminate the **ratios**. So 𝒲_ℬℬ is **not**
«almost archimedean in the window»: it contains the full comb for n < μ, reorganized as a Möbius correlation of the lattice
(c_N). This is literally R-K1 (HARD): «the sign lives in the ratio structure N′/N». My question (2) falls into that
restriction, as the goal warned.

### 2.3 The coupling: answer to (3)

𝒲_𝒜ℬ ≡ 0. It is «finite rank» and «of known sign» in the strongest possible sense, and therefore carries no content. The
identity T.1 (𝓕Ψ̌ = ĝ·D_μ with D_μ = ζM_μ − 1) gives the **same** information as Lemma R seen from ℬ. What it does is
compute 𝒲_ℬℬ as an integral over the line with a |D_μ|²-weighted multiplier. There is no cross term that T.1 could
bound.

The place where «Euler and FE touch», which BARRIER_SOUND imagined to be in 𝒲_AB, is actually **inside the proof of Lemma
R**. That is where Poisson (FE of conductor 1) and multiplicativity (ζ·P) enter, and that place produces a **zero**, not an inequality.

### 2.4 Lemma P2-S.2 (the complement is 𝒲). **PROVED.**

For every partition 𝒜 ⊕ ℬ in which 𝒜 ⊂ rad 𝒲, the generalized Schur complement is S = 𝒲|_ℬ ≅ 𝒲 in the quotient V/𝒜, and the
inequality left is S ⪰ 0 ⟺ 𝒲 ⪰ 0 on ℬ.

Moreover, since the map h ↦ Ψ̌_h is (up to the radical) the identity on the quotient, S is 𝒲 in other coordinates. By the
goal's criterion: **NO-GO**. There is no expression of S with visible sign other than the definition. The only thing gained is the
coordinate c_N, which is already recorded (GG, FF.1, R-Q2).

---

## 3. Variants that might save the format (and why they don't)

So as not to close via a bad choice of blocks, I examine the three reasonable ways of obtaining a nontrivial 𝒲_AA ≻ 0.

**V1. A' = orthogonal complement (in the quotient L²) of the radical, with its positive block.**
- This is A_⊥⊥(1) from LEMMA_I3, which is ≻ 0 with gap 3.77.
- But A_⊥⊥(1) **is** 𝒲 in the quotient, i.e. (★★) in block form. Its positivity is the goal, not a premise. Using it as a
  «D-free» block is circular. Its positivity is NUMERICAL at M = 8 modes, not PROVED.
- **Duplicate of LEMMA_I3.** The new reason (Euler block) does not apply, because A' is not defined by Euler.

**V2. Split the form, not the space: 𝒲 = 𝔄 − ℭ, with 𝔄 = arch + polar (branch 4, blind to ζ) and ℭ = comb.**
- To do Schur on the block matrix [[𝔄, ·],[·, ℭ]] a dilation is needed: the form 𝒲 as the Schur complement
  of a larger operator 𝕄 = [[𝔄, B],[Bᵀ, I]] with BBᵀ = ℭ.
- That requires ℭ ⪰ 0, factored as BBᵀ. But the comb 𝔠_p of a single prime is indefinite (Lemma B.2, SPEC_007), and the full ℭ
  is indefinite.
- If one sets ℭ = ℭ₊ − ℭ₋, the part ℭ₋ is added to 𝔄, and the positivity of 𝔄 + ℭ₋ − ℭ₊ with coupling via B₊ reduces to the
  bound ‖B₊‖ against 𝔄 + ℭ₋. That is exactly DD/EE (0.644 against what is required). **Duplicate (Schur via norms)**, unless
  there is an exact identity for B₊, which leads to gap P1 (quadratic BB* form in Λ), not P2.

**V3. Partition by windows: 𝒜 = level μ/2 tests, ℬ = level μ (the «bridge» that Q2 left OPEN).**
- By Lemma Q2.1, M_μ − M_{μ/2} is a finite Dirichlet polynomial, so the difference Ψ̌^{[μ]} − Ψ̌^{[μ/2]} is radical
  (Lemma R).
- The two blocks coincide modulo the radical: 𝒲_AA = 𝒲_BB = 𝒲_AB in the quotient. The block matrix is [[W, W],[W, W]] and its
  complement is W − W·W⁻¹·W = 0.
- It is an **identically zero** Schur: it says that the levels are the same coordinate (R-Q2), nothing more. NO-GO (PROVED given Lemma
  R).

**Lemma P2-S.3 (shape of any Schur useful for P2). PROVED, elementary.**

If an exact Schur complement is to carry the format of cor:shape(b), then:
- (i) 𝒲_AA must be nonsingular in the quotient, so 𝒜 ∩ rad 𝒲 = 0. Hence 𝒜 **cannot** be defined by Lemma R
  nor by the gauge.
- (ii) 𝒲_AB ≠ 0.
- (iii) The positivity of 𝒲_AA must be PROVED without going through 𝒲 in the quotient. Hence 𝒜 cannot contain the
  entire complement of the radical (otherwise, V1).

*Proof.*
- (i) If 𝒜 ∩ rad ≠ 0, that part separates as in §2.1 and contributes nothing.
- (ii) If 𝒲_AB = 0, the form is a direct sum and the inertia is the sum of inertias: there is no coupling or conjunction.
- (iii) Otherwise, the argument is circular. □

**Consequence.** The two arithmetic tools that cor:shape(b) names and that the corpus has in PROVED form are:
- Lemma R (Euler), which lives **in** the radical;
- the gap (integrality/mollifier), which lives in the **coordinate** of the quotient.

Neither of the two can define a block A with properties (i)–(iii). A third object needs to be invented. That is the
specification this memo leaves.

---

## 4. Composition of premises: answer to (4)

The goal proposed three premises: (i) Lemma R for 𝒲_AA, (ii) the gap/FE for 𝒲_BB and (iii) «something» for 𝒲_AB, each with
its own falsifier.

**Failure table (from Q2_LADDER §P3/P6, PI_MU, AUDIT_202_R1).**

| premise | where this Schur uses it | falsifiers that break it | falsifiers that preserve it |
|---|---|---|---|
| (i) Lemma R (Euler + Poisson) | 𝒜 ⊂ rad ⇒ 𝒲_AA = 𝒲_AB = 0 | cΛ (c<1), Beurling (no radical ζP(∂)), DH (no multiplicative inverse) | a_P (with ζ_P) |
| (ii) gap c_N = 0 | coordinate Ψ̌ of ℬ | (definition of c_N via M_μ; for a_P the gap is different, but GG §4 gives a two-term mirror) | — it is combinatorial data (Lemma Z.2′: c_N depends only on {m<μ : m|N}, Beurling-generic) |
| (iii) coupling | 𝒲_AB ≡ 0 | — empty | — empty |

**Reading (ARGUED in what it says about the rule, PROVED in what it says about the method).**

1. Premise (iii) is empty, so the «conjunction of three» reduces to two.
2. Premise (i) appears only **subtractively**: it says what is discarded (𝒜), it contributes no inequality.
3. After discarding it, the only statement with content is S = 𝒲_ℬℬ ⪰ 0. That is a statement about **one** form, and its
   proof is again subject to lem:transfer for any falsifier for which the reduction of §2 remains defined.
4. Where the reduction is not defined (cΛ, Beurling, DH), the falsifier does not break the **inequality**: it breaks the **identity**.
   This is exactly the pattern already recorded in AUDIT_202_R1 X1: «each falsifier falls through a different hypothesis = only the
   shape of the identity changes».
5. Concrete question of the goal: «Does 𝒲_AB involve the residue 1 / a_n ≡ 1 in a way that cΛ breaks it?» No. cΛ already breaks
   premise (i), because the residue enters Lemma R via A(g)=0 and the pole of ζ. No residue remains in 𝒲_AB, because 𝒲_AB is 0.

**Conclusion on P2.** This method does **not** produce the format that would make lem:transfer inapplicable. The premises do not
**compose** nonlinearly. They **chain**: (i) is a change of coordinates, (ii) is the coordinate, and (iii) does not exist.

This gives a **data point** about the Φ200 rule, not a proof: in the only exact Schur that the corpus knows how to write with Euler and
integrality, the composition falls into «the worst branch» (branch 2, REF-D) because the nonlinear operation (the Schur) is trivial. That
**every** composition falls this way remains ARGUED. BARRIER_SOUND's Lemma P2.1 remains OPEN.

There is a candidate counterexample to the rule that this memo does not close: a Schur with an 𝒜 satisfying P2-S.3 (i)–(iii) and
defined by a third arithmetic object that is not radical. Today no such object exists in the corpus. A grep for «non radical»
+ «Euler» in the index: only quantitative Guo L4.4 (R-Z1 (β), «the only living site»).

**Link suggestion (OPEN):** the only Euler input outside the radical that the index leaves alive is R-Z1 (β), **quantitative**
Guo L4.4. That is, the rate of approximation to the radical, not its inclusion. An 𝒜 defined as «near-radical at scale
ε», with 𝒲_AA ~ ε and 𝒲_AB ~ ε^{½}, would give a Schur with content. But then it would be subject to thm:shape(B′): the precision
4·10⁹Te^{−15.449T} carries over to the complement via the factor (1+‖K‖)². I do not construct it. It remains as Q-P2.2.

---

## 5. Test on Mori (request to the calibrator; not computed here)

Request for μ = 15, T = ½log15, on the basis of LEMMA_I3/analyse_i3.py:

1. **Verification of P2-S.1:** the block matrix of 𝒲 in the basis {R_P : P ∈ {1, 1−2^{−s}, 1−3^{−s}, M_μ, M_{μ/2}}} ∪ {Ψ̌ of
   the 8 modes of W_J}. Expected: ‖𝒲_AA‖, ‖𝒲_AB‖ at the level of quadrature error. The relative residue against
   ℓ* ≈ 1e−70 is of interest: if the quadrature residue exceeds ℓ*, the test is not conclusive for the sign, but it is for the structure.
2. **𝒲_BB:** inertia and minimum eigenvalue on the 8 modes of the quotient. Expected: equal to A_⊥⊥(1), spectrum ≈ {3.77, …}, by
   P2-S.1(c). A discrepancy would indicate that ℬ does not cover the quotient.
3. **Variant V3:** blocks at level μ = 15 and μ/2 = 7 (or 8). Expected: complement ≈ 0.
4. **K1.1′ contribution** of the atoms n < 15 within 𝒲_BB, atom by atom, at the minimizer: to document «what remains
   of the comb» (§2.2).

None of these numbers can change the method verdict. They only validate the blocks.

---

## 6. Verdict

- **PROVED (given Lemma R/Guo L4.4):** Lemma P2-S.1. With 𝒜 = Euler combs, 𝒲_AA ≡ 0 and 𝒲_AB ≡ 0. 𝒲_BB[Ψ̌_h] = 𝒲[h].
- **PROVED:** Lemma P2-S.2. The generalized Schur complement is S = 𝒲|_ℬ, which is 𝒲 in other coordinates. Degenerate
  Haynsworth: In(𝒲) = (0,0,dim𝒜) + In(𝒲_BB).
- **PROVED:** Lemma P2-S.3, necessary conditions (i)–(iii) for an exact Schur to carry the format of cor:shape(b). Neither Lemma R, nor the
  gauge, nor the gap can define block A.
- **NO-GO (PROVED):** exact «Euler ⊕ gap» Schur (including V3 by levels). **Duplicates:** V1 = LEMMA_I3; V2 = DD/EE
  (norms), unless exact BB* = gap P1.
- **ARGUED:** in this Schur the conjunction of premises chains and does not compose. It contributes one data point in favor of the Φ200
  rule at degree 2.
- **OPEN:** the composition rule (BARRIER_SOUND's P2.1); Q-P2.2 (near-radical block via quantitative Guo L4.4, subject to
  thm:shape(B′)). L′♯ / row D: OPEN, no change.

### Entry for the index (ROUTES-TRIED-INDEX/README)

- **P2_SCHUR_001 (phase 204i, gap P2): exact Euler/gap Schur NO-GO (PROVED given Lemma R).** With 𝒜 = span(ζP)(∂)g,
  Lemma R gives 𝒜 ⊂ rad 𝒲 ⇒ 𝒲_AA ≡ 0, 𝒲_AB ≡ 0, S = 𝒲_BB = 𝒲[Ψ̌] = 𝒲 in the quotient (Π.3/GG/R-Q2). 𝒲_BB keeps the comb
  for n < μ via ratios (K1.1′, R-K1). Variants: by levels μ/μ/2 gives Schur ≡ 0; positive complement = LEMMA_I3; split
  form = DD/EE. **Lemma P2-S.3:** a useful Schur requires a block A outside the radical, with 𝒲_AB ≠ 0 and positivity PROVED without
  going through the 𝒲-quotient; Lemma R, gauge and gap do not work. Premises chained, not composed. The P2 rule remains OPEN (ARGUED). Q-P2.2
  (near-radical, quantitative Guo L4.4) OPEN.
