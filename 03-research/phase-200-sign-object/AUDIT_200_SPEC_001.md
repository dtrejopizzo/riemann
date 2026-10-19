# AUDIT_200_SPEC_001: audit of SPEC_SIGN_OBJECT_001 (phase 200, stage 2)

Pen and paper; nothing new was run. Only checked against the files (MORI15_EXTREMAL_001,
AUDIT_CONSTRAINTS_001, AUDIT_L_SHARP_16 §6, PROOF_L_SHARP_FF_001, R162_2502, ROUTES-TRIED-INDEX/README).

**One-line verdict.** The elementary fact is correct (PROVED, though it is a classical fact about mollifiers, not something
new). The specification has **one internal contradiction** (P2 versus P5) and **one property that is the objective itself**
(P7). K1 falls under two index entries (Q_001, l.208) and its Λ-specificity is disproved by R162_2502: **NO-GO by
index**. K2 rests on a "cocycle" μ(n) that is not a cocycle and on a measure that is not well defined: **NO-GO**
as written. K3 is Γ-convergence (front I, l.278) plus a reduction to a sector that restriction 18 declares
false in PW: **DOUBTFUL**. Only its lemma K3.1 = (P0c) is of use.

---

## 1. Elementary fact: c_N = −μ(N) on [μ, 2μ)

Definition in FF_001 l.19: c_N := Σ_{m|N, m<μ} μ(m), with **strict** inequality m < μ (the same convention as
f = Σ_{m<μ}μ(m)H(m·) in l.6). For N > 1, Σ_{m|N}μ(m) = 0 holds, so c_N = −Σ_{m|N, m≥μ}μ(m). If μ ≤ N < 2μ and d | N with
d < N, then d ≤ N/2 < μ. Hence the only divisor ≥ μ is N and c_N = −μ(N). **PROVED.**

Edge cases:
- **N = μ with μ an integer** (for example μ = 15). With the strict convention, m = μ is excluded from the sum and c_μ = −μ(μ)
  (= −1 at μ = 15). This is correct, **but only with the strict convention**. If some document uses M_μ with m ≤ μ (common
  in the mollifier literature), then c_μ = 0 and the statement fails at N = μ. The spec must fix "m < μ"
  explicitly every time it is used. At μ = 15 this is not cosmetic: the first outer coefficient is c_15 = −1.
- **μ not an integer.** N ≥ μ means N ≥ ⌈μ⌉ and the argument does not change. Since μ ≥ 5, N = 1 does not occur.
- **Novelty.** This is the classical property of the coefficients of ζ·M_μ − 1 (they vanish on [2, μ) and equal −μ(N) in the
  first block). It must be labeled PROVED (elementary) and not presented as new input. Moreover, by restriction 28 the gap
  [2, μ) is shared with a_P. That the equality c_N = −μ(N) on [μ, 2μ) provides Λ-specificity is **ARGUED** (T3), not proved.
  The c_N are integers that depend only on μ(·). The dependence on Λ lives in Z (Poisson over ℕ), not in the c_N.

---

## 2. Table A and properties P1–P8

**Existence of the cited data (MORI15).** I checked all the numbers: 4.763·10⁻⁷⁰ (l.15, 56); the balance
−5.3722/+3.9164/+1.519/−0.0632 (l.13, 100, 104, 131); +0.340/−0.304 in the odd sector (l.14, 136); 0.0645 with φ = 0
(l.82); β = 0.83373, 0.67679 with M = 28 (l.84); 7.2·10⁻³⁵ (l.83, 90); a₄/a₀ = −1.6466 and 0.6073/0.6124 (l.163–164);
|a_{4j+2}| ≤ 6·10⁻³⁸ (l.12); κ_emp ∈ [0.56, 1.09] and 4.0824 (l.172). All exist. The resonances −0.481/−0.296/−0.197
exist (AUDIT_16 l.91, l.115). By contrast, **the assignment "n = 2, 3, 5" that K2 makes does not appear** in AUDIT_16 §6, which
only says "(1,n)". The value "(1,4) of p = +0.108" that K2 cites, I did not find it by grep either in AUDIT_16 or in GRAM_INERTIA_001.
The source must be given or it must be withdrawn.

**Defects:**

- **P7 is REF-D by definition.** "Q_μ(ι r) ≥ κμ^{−A}dist²" is (★★)/L′♯ written in another alphabet. As an *output* it is fine.
  As a *property of the object* it discriminates nothing, because any certificate for L′♯ satisfies it. It should be removed
  from the list of properties.
- **P2 contradicts P5 (internal contradiction).** P2(iii) requires that no intermediate piece of Q_μ exceed W_T by more than
  10³. P5(iii) requires that the exact identity of Q_μ reproduce the four-piece balance −5.3722 + 3.9164 + 1.5190 −
  0.0632, whose pieces are O(1), i.e. **10⁷⁰ times W_T**. The two cannot both hold in the same identity. One must choose:
  either P5 applies to an *auxiliary* identity (anatomy) that is not that of Q_μ, or P2 is relaxed to "the pieces of 𝒫 − ℛ in
  post-cancellation coordinates."
- **P3 against hard restrictions 2 and 4.** P3 asks for a 𝒫 that is "Hankel of CM kernel existing before the spectrum." The
  hard part of restriction 4 forbids "Bochner-Lévy + C–S," and restriction 2 forbids identity + comb-generic Bochner/C–S.
  A Hankel-CM square fixed by Γ_ℝ (which is exactly what K1 chooses) **is** Bochner-Lévy. Escaping restriction 4 is only
  possible if the comparison ℛ ≤ (1 − θ)𝒫 is not a C–S/Schur comparison. P3 does not require this, so it leaves the
  door open toward the forbidden class. What the spec presents as "compatibility with 4" is a declaration, not a
  verification.
- **P6, incoherent test.** The prediction ℛ^{cΛ} − ℛ^{Λ} = (c − 1)·0.0632 *at the extremal of Λ* gives, for c < 1, a more
  positive Q. P6 requires Θ(1) negativity for *each* falsifier. With c < 1 that cannot be seen at r*: one must evaluate at
  r_F, the falsifier's extremal, and for c < 1 the failure occurs in identity I1, not in Q. The test must be rewritten.
- **P4** is vague ("A ↦ −A in the sense of L2 §4"), but the carrier-inversion test between sectors is real and is
  backed by data. It is the most useful property in the list.
- **P8** is a good test (real data). It is not a structural property.
- **P1** is hygiene (restriction 17). Correct.

No property, except P3 (via restriction 4) and P2/P5 against each other, clashes with a hard restriction.

---

## 3. Candidates

### K1 (OS-Γ): NO-GO by index (with an explicit proof debt)

**(a) Class.** 𝒫 = 𝔒^∞ is the Widom/Hankel square of the Lévy kernel ν. This is Bochner-Lévy positivity (hard
restriction 4). **Concrete falsifier: DH.** R162_2502, row DH (l.35): DH has the same detector "with the energy of the poles of
Γ as weight (faithful by Müntz, same proof)" on its own lattice a_m = 2m + 3/2. Therefore the claim "conductor 1,
exponents ½ + 2j, CM ⇒ Λ-specific" is false as a source of specificity: a different Γ gives another CM square equally
good. All the Λ-specificity would have to come from ℛ = 𝔒^{Λ,≥μ}, and comparing ℛ against a CM square is comb-generic,
unless the bound uses something DH does not have. R162_2502 already concluded that C_N does not carry that term (Prop A).
Regarding Ξ_a: shifting the exponents to ½ ± a + 2j preserves full monotonicity, so "breaks the CM relative to
reflection at T" is ARGUED with no content.

**(b) Index.**
- **PROOF_L_SHARP_Q_001 (l.462)** treated exactly the outer form 𝔔 in the log variable on the half-line (T,∞). A
  Hankel form in log on the half-line *is* reflection at the boundary T. PROVED results: Q.2, the Toeplitz symbol is
  a_1 ≡ 0 for Λ (FE), and 𝔔 = Hankel with symbol ζ. Q.1, the prime part is not Hankel-CM. Also: "Do not retry: CM
  tests on log(mn) or diagonals; Nehari/AAK as a source of…"
- The "new reason" (4), "Q_001 without reflection at T nor c_N," is **cosmetic**: the half-line (T,∞) in log already is the
  center T, and the c_N are only the FF.1 expansion of the same datum.
- Worse: K1 needs a positive "diagonal Toeplitz 𝔇_μ" term with the weight of B.0, and Q.2 PROVED says that the Toeplitz
  part of 𝔔 is **identically zero** for c = 1. So either 𝔇_μ comes from another partition (and the identity in item 2
  is not that of 𝔔), or it equals zero.
- **l.208** (front A, phase 193): "reflection between places, only half-Hankel; fails with any atom, PROVED."
  K1 keeps the atoms n ≥ μ (16, 17, 19, …). The only real difference is restricting to the image ι(P_T) of the admissible
  set, and positivity on that image *is* the objective (REF-D).
- **R162_2502 Thm K** (‖K_T‖ ≥ c/λ(T)) is labeled there as a *Restatement*. K1 reproduces its Γ-detector structure.

**(c) First lemma.** The spec acknowledges that naive K1.1 is false. It is worse than stated. τ_{log N}g has support
(log N − T, log N + T) and log N ≥ 2T, so x + y − 2T ranges over (log(NN′/μ²), log NN′). The atom n = 2 enters for all
pairs with NN′ < 2μ², that is, **for pairs N, N′ ∈ [μ, √2μ), exactly where ρ* concentrates its mass** (ρ*(1) = −7.2·10⁻³⁵,
MORI15 l.88). It does not enter "through the tail of g": it enters **at leading order**. Test 5(c) ("≤ 10⁻⁷⁰ relative") will fail
almost certainly.
The "via Möbius identities" version has two outcomes:
- The contribution is Σ_{N,N′} c_N c_{N′}(NN′)^{−½}·h(log(nμ²/NN′)), a bilinear form in c_N over the hyperbola NN′ ≈ nμ².
  The identity Σ_{m|N}μ(m) = 0 is linear in each N and only collapses sums over divisors, not over products near a
  target. What remains is a Möbius correlation (class C6).
- The only exact identity available is the Mellin one: Σ c_N c_{N′}F(NN′) = (1/2πi)∫D_μ(s)²F̃(s)ds with D_μ = ζM_μ − 1.
  But this reintroduces ζ² on a line, i.e., the window form or the zero side (REF-D / Q.2).
- **Conclusion:** corrected K1.1 is either C6 or REF-D. I do not see a third outcome and the spec proposes none.

**(d) Output.** "CM square + pointwise weight" with the inequality 𝔒^{Λ,≥μ} ≤ (1 − θ)(𝔒^∞ + 𝔇) is a **disguised bound**:
it dominates atoms by a square, which is exactly the Nehari/AAK-type bound that Q_001 forbade.

**Label: NO-GO (by index: Q_001 + l.208, DH falsifier from R162_2502).** This is not a new impossibility. The remaining honest
debt is one line: write exact K1.1 and establish C6/REF-D. I recommend not pursuing a construction on K1.

### K2 (DS-×ℕ): NO-GO as written

**(a)** The object is not well defined:
- ν_r := |Σ c_N N^{−½}χ_N|² as a measure on 𝕊 requires Σ|c_N|²/N < ∞. But |c_N| ≤ d(N) and Σd(N)²/N diverges, and the
  "ĝ-weighting" is not specified.
- **The "cocycle μ(n)" is not a cocycle.** A cocycle for the ℕ^× action must be fully multiplicative in n (for
  example c(4) = c(2)² = 1), but μ(4) = 0 ≠ μ(2)² = 1.
- For prime n, σ_p^*ν − ν "coupled with weight −1" cannot describe a positive quasi-invariant measure.
- Therefore the rigidity theorem invoked ("Furstenberg–Rudolph with cocycle μ(n)") has no object, and is not CITED from
  any source: it does not exist in the literature.
- Also, σ_n preserves ι(ℝ) as a set (ι(t)^n = ι(nt)), so the reading "the defect cannot concentrate on a
  zero-entropy line" does not follow from anything: the line is invariant.

**(b) Index.**
- The projection identity is the anatomy CA_H of front H ("Near = Kronecker line minus Haar," l.263, PROVED).
- CA_E Thm 2 (l.249): the Bochner measure of the form lies in ι(ℝ).
- The consequence recorded in l.263 ("the nonlinearity can only come from the minimizer (REF-D) or from new input that
  is neither the minimizer nor a property of the comb") applies unchanged: mass outside ι(ℝ) does not enter the form,
  so any positivity of its own does not bound 𝒲_ext without a coupling, and the spec gives no such coupling.
- Front J (l.286) already recorded that the monoid's symmetries give no input.
- G1 (PROVED): the free monoid does not separate ζ from Beurling. The argument "what distinguishes is log ℕ ⊂ ℝ" sends
  everything back to ι(ℝ), that is, to CA_H.
- That a grep for "Furstenberg" comes up empty is novelty **of name** only, not of object.

**(c) First lemma.** K2.1 requires a ν_{r,n} ≥ 0 with sign μ(n). By the previous point (cocycle), it is not formulable. The
boundary term N ∈ [μ, nμ) contains c_N = −μ(N) on [μ, 2μ), i.e. the entire leak, as the spec itself fears.

**(d) Output.** The output "entropy ≥ 0 + Haar mass ≥ 0" would only be of square/counting type if rigidity existed, and
it does not.

**Label: NO-GO** (ill-defined object; identity = CA_H). If rewritten with a genuine cocycle (for example λ(n), the
Liouville function, which is indeed completely multiplicative), it would need to be justified again against CA_H and G1. That would
already be another candidate.

### K3 (renormalized Γ-limit): DOUBTFUL

**(a)**
- The limit 𝒩_∞ is a form on statistics of c_N at scale ω = N/μ, plus the weight B.0 and layer C. The spec admits
  that it can be comb-generic for c < 1: B′ is positive for κ < 1 (JJ). **Falsifier: cΛ with c ∈ (0,1).** The weight
  𝔴^c and layer C^c have positive limits, so K3 "proves" L′♯ for cΛ with c < 1, unless the limit retains
  identity I1. Hard restriction 2 requires this and the spec does not show how.
- **Restriction 18 (sector = parity only).** 𝒳_μ = span{ψ_{4j}} is a reduction to the self-dual sector, and restriction 18
  records that the exact reduction 𝔉_μ is **PROVED false in PW**. That the extremal at μ = 15 lands there (NUMERICAL) does not authorize
  restricting the class of proofs: L′♯ is stated for all admissible f.
- Renormalizing by (1 − λ₄) and requiring 𝒩_μ ≥ κ uniformly amounts to L′♯ restricted to the sector, with A = 0.

**(b) Index.**
- Front I (l.278): "Γ-convergence, concentration–compactness: dead."
- Reason (i) ("without renormalizing the limit is trivial") is real but weak: renormalizing by the leak is choosing the
  scale of the objective.
- Reason (ii) (the ψ_{4j} sector just identified) is real as a datum and clashes with restriction 18.
- Reason (iii) (compactness, not flow) is real against KK/restriction 11.
- Verdict on novelty: **partially real**.

**(c) First lemma.** K3.1 = (P0c) is plausible (Slepian–Pollak min-max with a linear restriction, ARGUED) and useful for
any candidate.

**(d) Output.**
- Compactness by contradiction gives a **non-effective** μ₀. Together with the gap 15 < μ < μ₀ (19(b) + 26), the argument
  closes nothing by itself.
- Equicoercivity in dimension J(μ) → ∞ in ℓ² does not give compactness without a stronger norm.
- Test 5 extrapolates the Hermite error of a ratio of values at 0 (0.8%) to the value of the form. That extrapolation is
  not justified.

**Label: DOUBTFUL.** Only K3.1 should be pursued as an infrastructure lemma, not K3 as a route.

---

## 4. Tensions T1–T3

- **T1. Correct.** Not depending on the scale and using only what is PROVED (BARRIER_EST) is the honest approach. But the
  consequence "exact identity + free positivity" is not enough: it also requires the free positivity to **not** be
  Bochner-Lévy/C–S (restriction 4), and K1 violates it.
- **T2. Correct**, with label PROVED-mod-CITED for μ ≤ 15.
- **T3. Partially incorrect.** "log N positions with integer coefficients c_N" remains "additive weight at log q ×
  monoid coefficient, linear in Λ," which is exactly the PROVED anatomy of front H (l.262). So T3 does not escape: it merely
  renames. The claim that the pair (gap + c_N = −μ(N) + mirror of a term) separates Λ from a_P is ARGUED. Until it is
  proved, it cannot be the premise on which the Λ-specificity of the three candidates depends.

---

## 5. Verdict, ranking, and specification change

| Candidate | Label | Reason (one line) |
|---|---|---|
| K1 OS-Γ | **NO-GO (by index)** | Hankel-log on the half-line = Q_001 (Toeplitz ≡ 0, CM forbidden) + l.208; DH has the same Γ square (R162_2502); K1.1 gives C6 or REF-D |
| K2 DS-×ℕ | **NO-GO** | μ(n) is not a cocycle, ν_r is not defined, the identity is CA_H (l.263) |
| K3 Γ-limit | **DOUBTFUL** | front I + sector reduction that contradicts restriction 18; comb-generic for c < 1; non-effective μ₀ |

**Own ranking: K3 (only lemma K3.1) > K1 > K2.** This reverses the order at the top of the spec.

**No fourth candidate from the catalog is needed; rather the specification needs to change:**

1. **Remove P7** from the list of properties: it is the output (REF-D).
2. **Resolve P2 versus P5.** P5 should refer to an anatomy identity, not that of Q_μ.
3. **Rewrite P3 (central change).** Today P3 admits as 𝒫 a square *independent of the comb* (archimedean/Γ/CM),
   and all three candidates choose it. But all the indexed evidence says that square is comb-generic or Bochner-Lévy:
   R162_2502 for DH, Q_001, front H/l.263 ("the nonlinearity can only come from the minimizer or from new input"),
   restrictions 2 and 4. The property must require that **the free positivity be nonlinear in the comb**: a square
   (or count) of an object *built with Λ or with the c_N*, of the type |Σ_{d|n}λ_d|² ≥ 0 counted against n, with an
   integer/counting output. Moreover, the comparison ℛ ≤ (1 − θ)𝒫 must be **false for DH and for cΛ with c < 1 in the
   identity itself**, not in a bound. With that P3, K1 and K3 are excluded from the outset and K2 would be excluded by
   definition.
4. **Downgrade T3 to a working hypothesis (ARGUED)** and add as a testable property the separation from a_P: the object
   must give a different value for a_P in the block N ∈ [μ, 2μ).
5. **Correct the P6 test**: evaluate at r_F, not at r*.

Row D: OPEN. L′♯: OPEN. No sign is asserted. The index entries (K1 NO-GO by index, K2 NO-GO) are left for the
synthesizer, in the same session.
