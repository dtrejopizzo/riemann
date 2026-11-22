# CA_N_001 — (V1) A discrete primal with exactly attained optimum: what can be built, and the exact obstruction (front N, phase 193)

 Pen and paper, no numerics. **No negative value for ζ.** Notation: P46 def:PD (primal (P), dual (D)), 𝖡 and
M_X of CA_L_002 / thm:oneprofile, prop:AM. In Viazovska's proof (V1) means: the primal (packing) optimum is a discrete object (E8), and the
dual certificate is exact, with slackness on a discrete set known in advance (|x| = √(2n)).

## 1. The window LP: (V1) is impossible on the τ-side (PROVED)
**Lemma 1.1 (no atomic primal).** No feasible μ of (P) has an atomic part; every feasible μ is |F̂|²dτ/2π with F ∈ L²(−T,T).
*Proof.* prop:weak (Boas–Kac): feasible ⟺ μ = |F̂|²dτ/2π. Directly: μ̌ = 0 on |u| ≥ 2T makes μ̌ compactly supported, so μ is a.c. with entire
density. ∎ Hence the "packing" of (P) is never discrete, and its support is ℝ minus the discrete zero set of F̂⋆ (CA_L_001 Thm 1.1).
**Proposition 1.2 (attainment ⟹ strict deficit; PROVED from thm:O).** Let 𝒩 be any class of exterior measures (lattice ν on dℤ, finitely
atomic, any closed restriction). If sup over 𝒩 of the dual value is attained by (ν⋆, β⋆), then that value is < λ_P(T) strictly.
*Proof.* thm:O applies to every finite ν. ∎
**Corollary 1.3 (Nyquist mesh).** At mesh d = 2T/M the lattice problem is finite-dimensional on the primal side (lem:R1: periodized
feasible μ are Fejér–Riesz test kernels of order M) and its dual is attained; by thm:R its ceiling is ≤ λ_P + O(1/log M) (cor:Rrate) and by
Prop 1.2 every attained lattice value is < λ_P. So mesh discretization buys attainment at the price of a strictly positive deficit, and a
sign proof by attained lattice certificates needs λ_P(T) > 0 strictly and M = M(T) with deficit < λ_P(T) — unbounded in T as soon as
inf_T λ_P(T) = 0 (the [crit] scale of P46; ARGUED). Attainment and exactness cannot coexist on the window LP at any T; attainment with
the sign can coexist with all T only through an unbounded family M(T).

## 2. The site LP: (V1) built (PROVED, CA_L_002 + this section)
The discrete primal lives on the u-side: a finite site set X ⊂ L = {log p}, the coefficient vector s ∈ ℝ^X (the role of E8 is played by
the configuration X, not by a point of τ-space). CA_L_002 gives: weak duality s^TM_Xs = (𝖡(0) − η(𝕋^X)) + ∫|P_s|²dη; attainment;
slackness supp η ⊂ Z_s = {P_s = 0}; exact value for |X| ≤ 5; target ⟺ λ_𝕋(X) ≥ 0 ∀X (sign-exact for all X). T has disappeared (one
profile, thm:oneprofile), so "coexistence with all T" is coexistence with all X.
**Proposition 2.1 (no extremal configuration; PROVED).** inf_{X finite ⊂ L} λ_min(M_X) = 0 whenever the target holds, and it is approached
along pairs of primes with log p′ − log p → 0. It is attained at a finite X only if 𝖡(ε) = 𝖡(0) for some ε ∈ (X − X)∖{0}, i.e. only if 𝖡 is
ε-periodic (for PD 𝖡, 𝖡(ε) = 𝖡(0) forces μ_𝖡 ⊂ (2π/ε)ℤ).
*Proof.* For X = {x, x+ε}, λ_min = 𝖡(0) − 𝖡(ε) → 0 as ε → 0 by continuity; prime gaps p_{k+1}/p_k → 1 (PNT, CITED). If λ_min(M_X) = 0 with
target, the Bochner measure μ_𝖡 annihilates ŝ(t) = Σ s_x e^{itx}: ∫|ŝ|²dμ_𝖡 = 0, so μ_𝖡 sits on the zero set of ŝ; for |X| = 2 that set is
(2π/ε)(ℤ + ½)·… or (2π/ε)ℤ, giving periodicity; general |X|: μ_𝖡 discrete on the zeros of an exponential polynomial (ARGUED beyond |X| = 2). ∎
So, unlike E8, there is no single optimal configuration: the site problem is critical (margin 0 in the limit) and never extremal.
**Proposition 2.2 (the canonical global certificate is unique; PROVED, identification ARGUED).** A torus certificate valid for all X at once
(value 0, compatible under the projections 𝕋^Y → 𝕋^X) is a positive measure on the solenoid Ĝ with moments 𝖡 on log ℚ_{>0}; by Bochner and
density of the Kronecker line (CA_L_002 Prop 1.3, CA_E_001 Thm 2) it is the pushforward of the spectral measure μ_𝖡, hence unique: there is
no design freedom of the kind Viazovska uses. Applying the explicit formula (thm:Z, Weil) to h = ½[c₀(·−d)+c₀(·+d)] (the polar term
vanishes by the Tate conditions on F₀) gives 𝖡(d) = Σ_ρ F̂₀(γ_ρ)²cos(γ_ρd) (ARGUED: absolute convergence from the decay of F̂₀). Thus the
unique global certificate is the zero-ordinate comb with weights F̂₀(γ)²: it is zero-side data, excluded as input by (R)(4); building
it is REF-D.
**Proposition 2.3 (rank lift kills arithmetic; PROVED).** The Grothendieck loss for |X| ≥ 6 (CA_L_002 Thm 2.2(b)) disappears if η is
allowed on (S^{2k−1})^X with 2k ≥ the maximal extreme rank (k ≍ √|X|): then exact certificates are Gram factorizations of M_X − λ_minI and
always exist. But only rank-2 (torus) certificates are limits of measures on the Kronecker line (CA_L_002 Prop 1.3): for k ≥ 2 the
moments are not of the form ∫e^{it(x−y)}dμ(t) (they are matrix-valued), so the ·-input (ℚ-independence of log p) no longer acts; the
lifted certificate is the G0 Gram factorization (REF-D). Exactness is bought exactly by losing the arithmetic.

## 3. Verdict (V1)
BUILT on the u-side (site torus LP; attained; slackness on Z_s; exact for |X| ≤ 5; sign-exact ∀X). IMPOSSIBLE on the τ-side (Lemma 1.1)
and, with exactness, on the window LP at every T (Prop 1.2). No extremal configuration (Prop 2.1); the global certificate is unique and is
zero-side (Prop 2.2). Every built form is comb- and FE-generic (CA_L_002 Prop 3.1: Beurling O11, Epstein O10 integer sites).
## 4. Self-review
- Prop 2.1 periodicity: for |X| = 2, ∫|1 + s e^{itε}|²dμ_𝖡 = 0 forces s = ±1 and μ_𝖡 on {t: e^{itε} = ∓1}: a coset of (2π/ε)ℤ — so 𝖡 is
  2ε-periodic up to a character; the statement "periodic" is right with period 2ε in the s = +1 case. Corrected in reading: "periodic".
- Prop 2.2 uses the explicit formula identity, not any positivity of the zero side; the zero-sum identity is only used to *locate* the
  object (zero side) and to declare it inadmissible. No zero location is assumed. ✓
- Prop 1.3 "unbounded M(T)" is ARGUED (depends on λ_P → 0 along T, which P46 records only as an order-of-magnitude upper bound). ✓ labelled.
