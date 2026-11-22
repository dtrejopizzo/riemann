# COMPOSE_EF_001 — First attempt at a genuine composition (E, F): the FE as a symmetry of h_par (phase 204q)

Pure mathematics; no new computation (the quoted numbers are NUMERICAL from previous sources).

## Summary (≤300 words)

The (S1)–(S4) template of O1_COMPOSITION_001 is attacked with the target's idea: use the FE as a **symmetry** of the
object h_par = 𝔄⁻¹χ/q (prop:WT), where Euler has already entered nonlinearly (q(a) = ⟨(𝔄_a)⁻¹χ,χ⟩ is rational in the
weights a).

1. **Starting correction (PROVED, from P46).** In prop:WT, 𝔄 = archimedean + comb, **without** a polar term. The full
   form is W^par = 𝔄 + 2ε χχᵀ. The pole enters only through χ.
2. **Lemma C1 (PROVED).** Everything the FE leaves in the window form (the Γ_ℝ factor of conductor 1, χ = e^{t/2}±e^{−t/2}
   with equal residues at s = 1 and s = 0, parity) is **independent of the weights a**. The only nontrivial symmetry of
   𝔄 that is known is parity, and parity is common to all forms 𝔞^a with real weights.
3. **Theorem C2 (NO-GO, PROVED).** If, in a sign step about q, h_par or 𝔊_T, the FE enters only as a symmetry or shape
   property of 𝔄 (prime side), then a_P (prop:shape-eulerdel) is a common falsifier of E ∧ "F-of-shape". That sign step
   **chains** (s(A) = {E}) and is excluded by lem:transfer for T ∈ [0.60, ½log P]. When the FE enters through the zero
   side (rem:ext-killing(iii)), the sign step is the positivity of the sum over zeros, i.e. REF-D.
4. **Diagnosis.** In the forms model, F is not a property of a. It only becomes non-constant through the coupling
   "summation coefficients ↔ comb" (Λ∗1 = log, rem:ext-killing(ii)) plus Poisson/Hamburger. This is why the closest
   composition is the **Hamburger inequality with defect** (C★, §5): Euler enters as an inequality (Q-P2.2) on the
   gauge quotient, and the FE as exact Poisson on the summation coefficients b ≡ 1. It remains OPEN, stated but not
   proved.
5. **Numerical test.** Measured against Mori/½log3, any bound of the form q_ev + ½ ≤ −c(T) needs c(½log3) ≤ 2·10⁻⁸.
   Guo/thm:shape(B′)'s quantitative precision in that window is ~10⁵, some 13 orders worse than that. It is advisable
   to attack the **odd sector** first (margin 2.5·10⁻⁴).

Verdict: "FE as a symmetry of h_par": **NO-GO (PROVED)**. Composition (C★): **OPEN**.

---

## 0. Index and corpus check (mandatory)

I grepped `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` for "h_par", "prop:WT", "FE symmetry", "Hamburger",
"Λ∗1", "deleted primes", "composition", "Q-P2.2" and "CALIB". Relevant entries:

- l.598 **POLAR_CAP_001**: h_par as a bordered Schur complement, TRANSFER/NO; PC-2 (𝔤_ev ≲ 9e−8, NUMERICAL).
- l.606 **AUDIT_204_CLOSURES_001** §3: invertibility of 𝔄 suffices; 𝔞_T(h_par) = 1/q; Lemma WT → prop:WT.
- l.614 **WT_HALVES_001**: 𝔄 without a polar term; **Prop S**: h* ∝ (𝔄−λ^W)⁻¹χ, q + ε/2 = −λ^W⟨𝔄⁻¹χ,(𝔄−λ^W)⁻¹χ⟩;
  h_par = h* + O(λ^W); "𝔄g = χ" does not dodge Theorem X / restriction 11; "deleted primes" falsifier at ½log3.
- l.613/615 **O1_COMPOSITION_001 + INTEGRATION_O1_001**: Φ200′; F mandatory via a_P and "E as a Dirichlet series over ℕ"
  mandatory via the quartets (editor's correction: the quartets **preserve** the FE).
- l.387 **INV_A_001** and l.422 **BARRIER_D1_001**: Hamburger rigidity. Quantitative Hamburger with sign from the comb
  side: linear Hamburger space = ℂζ.
- l.446: Rankin–Selberg and FE rigidity share the Kronecker parity blind spot.
- l.400 **INV_O_001**: bootstrap with direct spectrum = explicit formula = thm:Z.
- l.453/454 **PROOF_L_SHARP_C/D**: E = multiplication by ζ in Mellin; gauge.

**New reason (written, mandatory):** genuine composition (Def O1.2), not chaining. No index entry asks whether the FE
acts as a **symmetry** of h_par, nor applies the O1.E criterion to a conjunction (E, F) whose sign step is q.
POLAR_CAP and WT_HALVES treat h_par as a single-channel object and discuss its relation to λ_A, not which channel
decides the sign of q. §5 (C★) uses Hamburger. That entry exists (INV_A, BARRIER_D1), but as **linear rigidity**, and
it stands closed as a retry without a new reason. What changes here is that Hamburger enters as the F-identity of a
conjunction whose sign step is an E-inequality (Q-P2.2) on the gauge quotient. BARRIER_D1 used it as the sign step of a
single channel. If (C★) collapses to BARRIER_D1, that is recorded as such (see §5.3).

Definitions checked against P46 (main.tex): prop:WT (l.4371), thm:parityschur (l.4176), prop:polarcap (l.4316),
rem:polarcapdiag (l.11251), prop:shape-eulerdel (l.8545), lem:shape-quartet (l.8560), thm:ext-half (l.9792),
rem:ext-killing (l.9814), prop:ext-gauge (after rem:ext-killing).

---

## 1. The exact object and a correction to the target

**Notation (P46, prop:WT).** Fix T and the parity. χ_ev = cosh(t/2)1_{I_T} and χ_odd = sinh(t/2)1_{I_T} (P46's
normalization, l.4371 and POLAR_CAP §1). Also ℓ_par = ⟨·,χ_par⟩, ε_ev = +1, ε_odd = −1. 𝔄 := 𝔞_T|𝒟^par_T is the form
**archimedean plus comb, without the Tate condition and without a polar term**. The full form is

  W^par = 𝔄 + 2ε_par χ_par χ_parᵀ        (thm:parityschur(o), PROVED).

If 0 ∉ spec 𝔄 and q := ⟨𝔄⁻¹χ, χ⟩ ≠ 0, then h_par = 𝔄⁻¹χ/q, 𝔞_T(h_par) = 1/q and 𝔤_par = (1 + 2εq)/q. The inertia per
sector is prop:WT's:
- odd: W_odd ≻ 0 ⟺ 𝔄_odd ≻ 0 ∧ q_odd < ½;
- even: W_ev ≻ 0 ⟺ (n₋(𝔄_ev) = 0 ∧ q_ev > −½) ∨ (n₋(𝔄_ev) = 1 ∧ q_ev < −½).

**Correction.** The target describes 𝔄 as "archimedean + polar + comb." That is the full form W^par, not prop:WT's 𝔄
(WT_HALVES_001 already corrected this). The difference matters for the channel analysis. The pole (residue 1, which
together with the FE fixes the two exponents ±½) enters **only** through χ. Euler (the weights a = Λ) enters **only**
through 𝔄.

**Dependence on the weights.** Write 𝔄_a = A_∞ − C_a, where A_∞ is the archimedean part (Γ_ℝ, conductor 1) and C_a is
the comb operator, C_a = Σ_n a(n) n^{−½} (translation by log n, symmetrized), restricted to the window. C_a is
**linear** in a. Then

  q(a) = ⟨(A_∞ − C_a)⁻¹ χ, χ⟩        (rational in a; Neumann series Σ_k ⟨A_∞⁻¹(C_a A_∞⁻¹)^k χ, χ⟩ when it converges).

**Answer to target question (1) (which channel decides the sign of q).** The candidate sign step is the scalar
q_ev + ½ < 0 (or q_odd − ½ < 0). As a function of the data, q is **nonlinear** in a: it involves products
a(n₁)…a(n_k) of every order. Hence Lemma O1.E alone does **not** force chaining. The escape route "sign step nonlinear
in a" is available, and that is the good part of the idea. The question is which channels appear in the inequality
that would prove that sign:
- **E** appears as a property of a. For instance, multiplicativity would make C_a factor over primes ("truncated
  Euler product" operator, legitimate S1).
- **F** would appear as a property of A_∞, of χ, or of a symmetry U of 𝔄. §2 shows that **none of the three depends on a**.

## 2. What does the FE leave in the window form? (answer to (2))

**Lemma C1 (the FE's footprint in the forms model; PROVED).** Consider the family of window forms
𝔉 := {W^{a} = A_∞ − C_a + 2ε χχᵀ : a real weights}, which is the model in which P46 defines 𝔞_T^a and where a_P, cΛ,
a_θ, Beurling and the "deleted primes" live. Then:
(i) A_∞, χ_ev, χ_odd and the decomposition by parity are the same for every a.
(ii) The involution P: F ↦ F(−·) commutes with A_∞ and with C_a for every real a. Hence P is a symmetry of every W^a
and the sector decomposition (ev/odd) holds across the whole family.
(iii) If U is a bounded operator on L²(I_T) that commutes with A_∞ and fixes χ_ev and χ_odd, the condition "U commutes
with C_a" is linear in a. If imposed for every a in a set generating the finitely supported sequences over
log ℕ ∩ (0,2T), then U commutes with every truncated symmetrized elementary translate τ_{log n} + τ_{−log n}.

*Proof.* (i) This is the definition of 𝔞_T^a in P46: the archimedean part and the polar term are fixed and only the
comb weights change (forms section, Def. def:shape-class; prop:shape-eulerdel uses it this way with a_P). (ii) The
archimedean kernel is even (depends on |t−s|, in Theorem A's form). For real weights, C_a is a sum of symmetrized
translates, τ_{log n} + τ_{−log n}, compressed to I_T, and P swaps them. (iii) This is linearity of a ↦ C_a. ∎

**Consequence.** In the forms model, ζ's FE leaves **three footprints**: the Γ_ℝ factor of conductor 1 in A_∞, the
pair of exponents ±½ with equal residues in χ (the pole at s = 1 and its mirror image under s ↦ 1−s), and the parity
P. All three are **constant on 𝔉**. That is, F-of-shape is not a predicate on a. Any "FE" symmetry of h_par derived
from these footprints holds equally for h_par^{a} with arbitrary a.

**Is there a nontrivial FE symmetry of h_par beyond parity?** Candidates, one by one:
- **Parity P.** Already used; h_par is even or odd by construction. It contributes no channel.
- **Poisson/Tate involution of the comb.** The Poisson identity relates Σ_n f(n) to Σ_n f̂(n) over the **summation
  coefficients** b_n ≡ 1, not over the comb Λ. Passing from the comb to b ≡ 1 requires Λ∗1 = log
  (rem:ext-killing(ii)), which is exactly Euler. This "symmetry" does not act on L²(I_T) as an operator commuting with
  𝔄. It acts on the test space of the summation-side half-line (thm:ext-half), where the window stops being the
  support. It is not a symmetry of h_par. It is a change of model (see §5).
- **Zero-side symmetry** ρ ↦ 1−ρ (rem:ext-killing(iii): W_T(Ef) = Σ_ρ Φ_{Ψ_f}(ρ)Φ_{Ψ_f}(1−ρ)). Writing
  𝔄 = W − 2εχχᵀ with W = Σ_ρ (·)(ρ)(·)(1−ρ) gives 𝔄⁻¹ as the inverse of a sum over zeros minus a rank-1 term. By
  Sherman–Morrison, q = ⟨W⁻¹χ,χ⟩/(1 − 2ε⟨W⁻¹χ,χ⟩) when W is invertible. This is the same inertia identity of prop:WT
  read backwards: **q + ε/2 has the sign imposed by W** (compare with WT_HALVES's Prop S). The sign of W on the sum
  over zeros is the goal. **REF-D (P4).**

Conclusion of §2 (ARGUED as an exhaustive list; PROVED for each element): **h_par inherits no nontrivial FE symmetry**
in the forms model. The only way the FE says more than "constant" is through the zero side, where the sign step is
the goal itself.

## 3. Theorem C2: the FE as a symmetry of h_par chains (NO-GO)

**Theorem C2 (PROVED, given prop:shape-eulerdel and lem:transfer).** Let A be an argument whose sign step (Def O1.2)
is an inequality Ψ(q, h_par, 𝔊_T, 𝔄) ≥ c(T) > 0 implying W^par ⪰ 0 in some sector, for T in an interval J. Suppose
that in that step the inputs are:
(a) properties of the weights a that hold for every a with completely multiplicative Dirichlet coefficients, of
modulus ≤ 1 and non-negative integers (E in O1's form, plus I3), in any combination, linear or not;
(b) the FE only through A_∞, χ, parity, or any operator U depending only on A_∞ and χ (F-of-shape, Lemma C1).
Then A does not prove its conclusion for any T ∈ J ∩ [0.60, ½log P] for any P ≥ 3.

*Proof.* By prop:shape-eulerdel (PROVED), a_P = Λ·1{p ≥ P} has generating series ζ(s)Π_{p<P}(1−p^{−s}), which is a
Euler product over ℕ with coefficients 1{(n, Π_{p<P}p) = 1}: completely multiplicative, integer, in [0,1]. So a_P
satisfies (a). Its form belongs to 𝔉 with the same A_∞, χ and P, so it satisfies (b) by Lemma C1(i)–(ii). If U depends
only on A_∞ and χ, U is the same for a_P. Moreover a_P fails WP_T, and hence fails W_T ⪰ 0 (W_T ⪰ 0 ⟹ WP_T, P46), on
T ∈ [0.60, ½log P]. By lem:transfer with q₀ = q_ζ and q₁ = W^{a_P}, no deduction of that form is valid in that range.
By Def O1.2, s(A) effectively reduces to {E}, because F-of-shape is constant on the class and enters as a prior
identity fixing A_∞ and χ. Prop. O1.C's abstract falsifier coincides here with a concrete one. ∎

**Scope observations.**
1. C2 does **not** depend on linearity. It works even if q(a) is rational in a. O1.E's escape (nonlinear sign step) is
   necessary but not sufficient: the nonlinearity was in a (channel E). To compose, the nonlinearity or the inequality
   must **mix** E with something from F that varies within the class, and F-of-shape does not vary.
2. Why does the intuition "χ is exactly the direction the conductor-1 FE leaves invariant" fail? Because it is true
   for every member of 𝔉: χ is fixed in the model, not fixed by ζ. DH has no pole and so χ = 0. But that
   discriminates the **pole**, not the FE, and a_P has a pole.
3. Epstein? Q = x²+5y² has a pole, A_∞ of degree 2 and conductor 20. Its χ is different (the exponents and residues
   change with the normalization by √20 and Γ_ℝ(s)Γ_ℝ(s+1)), so it does not belong to 𝔉. Epstein is **not** the
   relevant falsifier for C2. It is not needed either: a_P suffices. The value of q_Epstein (requested in CALIB_R4)
   informs about the "pole + degree-2 FE" channel, not about C2.
4. Quartets? EDITOR_O1 corrects that they preserve the FE but break "E as a Dirichlet series over ℕ" (the absolutely
   continuous part −kβ_z on the arithmetic side). Their form is W^ζ − kB_z, which is **not** in 𝔉. C2 does not use them.

**Relation to Theorem X and to h* (requested in the target).** h_par ≠ h*. Prop S (WT_HALVES) gives
h_par = h* + O(λ^W), i.e. **h_par is the minimizer up to a term of the order of the floor**. In the even sector at
½log3 the floor is λ^W_ev ~ 10⁻⁸ (NUMERICAL), so, for every Lipschitz functional Ψ, Ψ(h_par) = Ψ(h*) + O(10⁻⁸).
Theorem X forbids first-order discriminants that are functionals of h*. A sign step that is **linear** in h_par
inherits the obstruction up to O(λ^W), and that is not enough to separate from it when the sought margin is of the
same order (§6). The target asks why the candidate "is not Theorem X." The honest answer is that **it is, at first
order**. A step nonlinear in h_par (for example q itself, a quadratic form ⟨𝔄⁻¹χ,χ⟩) escapes Theorem X's literal
statement, but not C2.

## 4. The most honest candidate with h_par (answer to (3))

Stated to record exactly where it breaks.

**Candidate K (odd sector; statement).** For all T > 0: 𝔄_odd(T) ≻ 0 and

  q_odd(T) ≤ ½ − c_odd(T),  with c_odd(T) > 0,        (K)

proved as follows: E enters as an inequality, "C_Λ is dominated by A_∞ on the complement of χ with defect δ_E(T)"
(the quantitative form Q-P2.2: the Euler comb is almost radical at scale ε). F enters as a symmetry fixing χ
(Lemma C1).

- *Sign step:* (K), a scalar.
- *Channel as inequality:* E (domination of C_Λ).
- *Channel as symmetry:* F-of-shape.
- *Criterion O1.E:* there is an inequality (E) and the step is nonlinear (q). O1.E does **not** exclude.
- *Criterion Φ200′ / C2:* F-of-shape is constant on 𝔉 and a_P satisfies E. By C2, (K) proved this way is false on
  [0.60, ½log P]. Concretely, with deleted primes at ½log3, rem:polarcapdiag and WT_HALVES give q_odd ≈ −0.056 with
  n₋(𝔄_odd) = 1 (NUMERICAL): the first half of (K) fails. And prop:shape-eulerdel gives the PROVED failure of WP_T for a_P.
- *Why is it not Theorem X?* q is quadratic in the resolvent. At first order in h_par it is indeed (§3).
- *OPEN:* none within class (K). The class is closed by C2.

**Verdict (3): NO-GO (PROVED).** The idea "FE as a symmetry of h_par" does not close even as a statement: any
inequality with that architecture has a_P as a PROVED counterexample. Where F enters must change.

## 5. The closest genuine composition (answer to (4))

### 5.1 Where the FE varies with the data

By Lemma C1, F can only be a non-constant channel if the model does **not** fix A_∞ and χ by decree, but instead
obtains them from the data. The only place in the corpus where this happens is the half-line model (thm:ext-half,
rem:ext-killing, prop:ext-gauge):
- the **summation** coefficients b (with E: b = 1 ⟺ a = Λ by Λ∗1 = log; for a_P, b = 1{(n,∏_{p<P}p)=1}, via
  Möbius/Euler; the map a ↦ b is the Dirichlet exponential, **nonlinear** in a);
- the FE at conductor 1 is exact Poisson for b ≡ 1: Σ_n f(n) = Σ_n f̂(n) + (polar terms) (Hamburger: among ordinary
  series, b ≡ 1 is the only one with that FE, CITED);
- the gauge 𝒢̄_T is the radical (Guo L4.4) and ℓ(g) = 2 dist²_{L²(λ,∞)}(r_f, 𝒢̄_T) (prop:ext-gauge, PROVED).

Here F **does** depend on a: for a_P, b does not satisfy exact Poisson, and the defect is
Σ_n (b_n − 1) f(n) = Σ_{p<P}-terms (partial Möbius series). For DH, b is periodic mod 5, with Poisson of conductor 5
and no pole. So F stops being constant on the class. This is the structural difference from §2–§4.

### 5.2 Statement (C★) — Hamburger inequality with defect (OPEN)

**Definitions.** For weights a with E, let b = b(a) be the summation sequence (Dirichlet exponential of a/log). For f
in thm:ext-half's core, let

  𝔇_F(a; f) := Σ_n b_n f(n) − [Σ_n b_n f̂(n) + pole]        (conductor-1 Poisson defect; 𝔇_F(Λ; ·) ≡ 0 by F).

Let δ_E(a; f) := dist_{L²(λ,∞)}(r_f^{a}, 𝒢̄_T^{a}) be the quantitative radicality defect (Q-P2.2), with r_f^a the
representative built with b(a).

**(C★) (OPEN).** There exist T₁ > ½log15 and a function c(T) > 0 such that, for all T ≤ T₁ and all g = Ef from the
core in the even or odd sector,

  W_T(g) ≥ 2 δ_E(Λ; f)² − K(T) · sup_{a ∈ 𝒱(Λ)} |𝔇_F(a; f)|² / ‖a − Λ‖² ,

where 𝒱(Λ) is a neighborhood of Λ in the family E (Euler weights) and K(T) is an explicit constant. The right-hand
side combines the leakage (Euler as inequality: the mass the gauge cannot absorb) with the **derivative** of the FE
in the direction of the data. That second term is null in the forms model (Lemma C1), but it is not here.

**Sign step.** (C★) with right-hand side > 0 on χ's complement.
**Channels:** E as an inequality (δ_E, Q-P2.2) and F as a **derived identity**, 𝔇_F(Λ; ·) = 0 with nonzero derivative
in the direction a_P. Thus F enters as a first-order restriction on the variation of the data, not as a constant.
**Why it does not chain (O1.E applied):** (i) the map a ↦ b is nonlinear; (ii) the F term is a sup over a neighborhood
of the family E, i.e. a quantity **joint** in (E, F) that does not factor into "prior F-identity + E-inequality." If F
is removed, 𝔇_F no longer vanishes at Λ and the right-hand side loses its sign. If E is removed, 𝒱(Λ) is no longer
defined (there is no summation sequence for the given comb) and δ_E loses its radical meaning (DH: Φ^{DH}_f ∈ rad
𝒲_{DH} without Euler, GUO_QUANT §1(d)). This is (S3).
**Why it is not Theorem X:** the discriminant is quadratic in f and its F term depends on the variation in a, not on h*.
**(S4):** it must be shown that no rearrangement turns 𝔇_F into a prior identity. This is OPEN, and it is exactly the
risk in §5.3.

### 5.3 Recorded risks (honesty)

1. **Collapse to BARRIER_D1.** If the sup in (C★) is attained in the tangent direction and "linear Hamburger space =
   ℂζ" (BARRIER_D1 Prop 1) trivializes it, the F term reduces to a linear projection and (C★) chains (O1.E). This is
   ARGUED as the main risk. Test: compute the tangent of {𝔇_F = 0} at Λ within the family E. If it is {0}, the term is
   coercive (good). If it is linear of dimension ≥ 1, it collapses.
2. **thm:shape(B′).** Q-P2.2's precision 4·10⁹ T e^{−15.449T} transports with (1 + ‖K‖)². At T = ½log3 that gives
   ≈ 4.5·10⁵, which is not a margin. (C★) needs a **constant-free**, structural version of δ_E, not the rate.
3. **Kronecker (index l.446).** Rankin–Selberg and FE rigidity share the blind spot d(p^j) ↦ (−1)^j d(p^j). If the
   family 𝒱(Λ) contains Λ's Kronecker twist with 𝔇_F equal at second order, (C★) does not separate. This is tested by
   computing 𝔇_F at a = Λ·λ_K (Liouville weights on powers) to second order.
4. **Zero side.** Written with rem:ext-killing(iii), W_T(Ef) is a sum over zeros. If (C★)'s proof goes through there,
   it is REF-D (P4). The proof must stay on the summation side.

**§5 label:** (C★) is OPEN. It is the only form found in which F is a non-constant channel and the sign step needs it
together with E. It is not proved and has three concrete collapse risks (1, 3 and 4).

## 6. Test at Mori/½log3: what each inequality predicts

Data (NUMERICAL, P46 prop:WT and rem:polarcapdiag; at T = ½log3, not ½log15):
q_ev + ½ ≈ −2·10⁻⁸ with n₋(𝔄_ev) = 1; q_odd ≈ ½ − 2.5·10⁻⁴ with 𝔄_odd ≻ 0. With deleted primes: q_ev ≈ −0.408 and
q_odd ≈ −0.056 with n₋(𝔄_odd) = 1.

**Universal restriction (PROVED, from Prop S).** q_ev + ½ = −λ^W_ev·⟨𝔄⁻¹χ, (𝔄 − λ^W)⁻¹χ⟩. Every true bound
"q_ev + ½ ≤ −c(T)" satisfies c(½log3) ≤ 2·10⁻⁸, and c is of the order of λ^W_ev times a resolvent factor.
Consequences:
- (K) in the even sector would have predicted a separation ~0.09 between ζ and a_P (−0.5 vs −0.408) using a margin
  ≤ 2·10⁻⁸ in ζ. That asymmetry (tiny margin in ζ, large jump in the falsifier) is the footprint of the even sign
  being almost degenerate. **No inequality with Guo-type constants (10⁵ at ½log3) can see it.**
- (C★) predicts, in the even sector, W_T(h_ev) ≈ 𝔤_ev ≈ 9·10⁻⁸ ≥ 2δ_E² − K·(F term). So δ_E(Λ; h_ev)² and the F term
  must cancel to within 10⁻⁷. Verifiable prediction: **δ_E(Λ; h_ev)² ≈ K·(F term) with difference ≲ 10⁻⁷**. If the
  calibrator finds one of the two to be ≫ 10⁻⁷ and the other not, (C★) is false in the even sector (numerical
  falsifier of the architecture).
- In the odd sector the margin is 2.5·10⁻⁴: **I recommend that (C★)'s first test be odd**, with
  𝔤_odd ≈ 10⁻³ ≥ 2δ_E² − K·(F term).

## 7. Requests to the calibrator (answer to (5))

In addition to q(T), the inertias and the floor of 𝔄_odd, which are already measured:
1. **q_par for a_P with P = 3, 5, 7** at T ∈ {0.60, ½log3, ½log5} (cross-check of C2 against the PROVED falsifier;
   there is already a datum for "deleted primes," but an explicit P = 3 is worthwhile, since prop:shape-eulerdel
   requires P ≥ 3).
2. **Sensitivity ∂q/∂a** in the direction a_P − Λ and in the direction of the Kronecker twist (Λ·(−1)^{j+1} at p^j):
   is it O(1) or suppressed? Measures whether the nonlinearity of q in a mixes anything (§3, obs. 1).
3. **Hamburger tangent.** In the finite family E, truncated to p ≤ 7 and j ≤ 3 with free multiplicatively linked
   weights a(p^j), compute the derivative matrix of 𝔇_F(·; f) at Λ, for f in a basis of 8–16 core tests. Give rank
   and singular values (risk 1 from §5.3).
4. **δ_E(Λ; h_par)** = distance of h_par's representative to the gauge, at ½log3, in both sectors (risk 2, test
   from §6).
5. **q_ev for Epstein at T = 1.59 and at ½log3** (CALIB_R4). Serves as information about the "pole + degree-2 FE"
   channel, not as a C2 test (§3, obs. 3).
6. For the five quantities: stability at 16/24/32 modes, as in rem:polarcapdiag.

## 8. Entry for ROUTES-TRIED-INDEX (for the editor to add)

> - **COMPOSE_EF_001 (phase 204q): "FE as a symmetry of h_par" NO-GO (PROVED).** Correction: in prop:WT, 𝔄 has no
>   pole; F enters only through A_∞, χ and parity. **Lemma C1 (PROVED):** the FE's footprint in the window form is
>   constant across the weight family 𝔉. h_par has no other symmetry (Poisson acts on summation; ρ ↦ 1−ρ is REF-D via
>   Sherman–Morrison). **Theorem C2 (PROVED):** every sign step on q/h_par/𝔊_T with E (linear or not) ∧ F-of-shape has
>   a_P (prop:shape-eulerdel) as a common falsifier ⇒ it chains; candidate (K) dies. h_par = h* + O(λ^W): Theorem X at
>   first order. Closest composition: **(C★) Hamburger with defect** (E as inequality δ_E/Q-P2.2, F as the derivative
>   of summation Poisson in the direction of the data), OPEN, with risks of collapse to BARRIER_D1, Kronecker and the
>   zero side. Test: at ½log3, δ_E² and the F term cancel to within 10⁻⁷ (even); it is advisable to test the odd
>   sector first (2.5e−4). Do not retry symmetries of 𝔄 or of h_par as the F channel.
