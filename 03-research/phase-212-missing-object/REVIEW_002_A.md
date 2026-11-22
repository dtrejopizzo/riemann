# REVIEW_002_A — Critical review of ROUND_002_A (exterior tail of the hyperbola as a sum of squares)

Scope: line-by-line reading of the memo; independent derivation of identity (1), of the Lemma and of
Observation (2) against P46 §sec:firstcontact (`04-papers/46-row-d-dual-certificates/main.tex`,
l. 6625–6946: operators on the line, thm:PCfinite, eq:Gammaenergy, eq:collar, eq:Qbalance,
eq:Qrecombine, eq:Qspectral, prop:GEgap, eq:equivgate, rem:returnremarks); opening of the
cited antecedents (`R170_816`, `819`–`821`, `835`, `837`, `841`, `870`; `R161_030`–`039`, `071`,
`072`, `081`; catalogue 04 of the index, rows G4C-R161_030-032, 033-034, 035-038, 039-045, G8B-161);
search for counterexamples; delimitation of what is not excluded. No existing file was modified.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Summary of verdicts

| Claim of the memo | Verdict | Correction |
|---|---|---|
| Identity (1) | ACCEPTED WITH CORRECTIONS | identity PROVED; "the only functionals", "the only sum", "exactly three ways" are not proved (ARGUED); description of ℓ_k imprecise (§1.1) |
| Lemma (indefiniteness of C^w − ⟨α,Bα⟩ on P_T, L finite) | ACCEPTED, PROVED; statement to be corrected | the hypotheses w ≥ 0 and k > N are not used: it holds for every nonzero complex weight of finite support in k ≥ 1; it does not see h or Λ. The per-parity-sector version is missing (proved here, §2.4). Exact class in §2.5 |
| "not even for a single k" | ACCEPTED, PROVED | — |
| Observation (2) | ACCEPTED, PROVED (one point validated, NUMERICAL) | only with finite M; the matrix is not canonical (overcomplete moment system) and its norm is exponential in MN e^{2T}; "alternating" is the Taylor series of the cosine (§3) |
| Cross-check | ACCEPTED WITH CORRECTIONS | citations correct except one section; "same difficulty as R161_033" inaccurate: C is linear in k and has no cross terms between distinct k (§4) |
| Result "no new mechanism" | ACCEPTED | — |
| "Do not relaunch … in any variant of … finite-rank test" | REJECTED in that wording | explicit counterexample with a rank-one test (§5.1); replace by the class of §2.5 |
| "The only thing left not excluded is the matrix (2)" | REJECTED | list of what is not excluded in §5.2 |
| "Row K1 closed in the finite-L formulation" | ACCEPTED WITH CORRECTIONS | closed only for the isolated tail, modulo forms in finitely many Gamma moments, with non-negative remainder on P_T or on a parity sector (§6) |

No mathematical error was found in any proof labelled PROVED. The defects are of scope:
the Lemma is more general than it says (and for that very reason says less about the tail), and the closure that the
memo asks to record is wider than what the Lemma supports.

## 1. Identity (1)

### 1.1 Verification

By thm:PCfinite, for M ≥ N the operator H_{M,N} = L_MS_N − S′_N has coefficient h(k) at k > N and
zero at k ≤ N. Evaluating the Dirichlet series of the coefficients at s = s_m = a_m + ½:

    Σ_{N<k≤MN} h(k) k^{−s_m} = (Σ_{d≤M} Λ(d) d^{−s_m})(Σ_{n≤N} n^{−s_m}) − Σ_{n≤N} (log n) n^{−s_m}
                             = d_{m,M} Z_N(s_m) − Z_N^{log}(s_m),

with d_{m,M} that of P46 (l. 6765). Multiplying by b_m²|μ_m^+(F)|² = |(𝒪_LF)_m|² and summing over m ≤ L
gives (1). Correct, PROVED. The diagonal matrix D_{M,L}Z_{N,L} − Z^{log}_{N,L} is non-negative entry
by entry (it is Σ_{k>N} h(k)k^{−s_m}). The comparison with c_{N,L} = Σ_n Λ(n)‖ℓ_n‖² of eq:Qbalance is
correct: same ℓ_n, different weight.

### 1.2 Corrections

- The gloss "the vector 𝒪_L of the translate of F by log k, with the factor k^{−1/2}" does not describe ℓ_k:
  that vector has components b_m k^{−s_m}μ_m^+(F), not b_m k^{−s_m/2}μ_m^+(F). The exact statement is
  ‖ℓ_k(F)‖² = ⟨𝒪_LF, 𝒪_L(k^{−1/2}V_{log k}F)⟩ with the moment of the translate taken without truncation to the
  window (the truncated moment is the one producing the collar eq:collar). ℓ_k is a chosen diagonal square
  root of that pairing.
- "The only functionals … that the structure offers", "the only sum … with explicit ℓ_k" and "there are
  exactly three ways" are exhaustiveness claims without proof. Label: ARGUED. Under
  "What was proved" only the identity should remain.
- §(5), cΛ: what changes is the shape of the identity (the interior block
  (c − 1)Σ_{k≤N}(log k)‖ℓ_k‖² appears), not its validity. The memo's conclusion (not a sign step; it reproduces
  restriction R1 of REVIEW_001_ABD §4.3) is correct.

## 2. The Lemma

### 2.1 Conventions checked

P46 l. 6649–6661: V_{−log k}F(t) = F(t + log k), H_{M,N} = Σ h(k)k^{−1/2}V_{−log k}; phases 161 and 170
write τ_aF(t) = F(t + a) (`R161_031` §1). With F(t) = e^{t/2}f(e^t), 𝓕F(t) = e^{t/2}f̂(e^t) and
(k^{−1/2}τ_{log k}𝓕F)(t) = e^{t/2}f̂(ke^t). The adjoint of τ_{log k} is F ↦ F(· − log k), so that

    (H^w)* e_m^±(t) = e^{t/2} g(e^t),   g(x) = x^{∓a_m−1/2} Σ_k w(k) k^{−1/2±a_m} 1_{(ke^{−T}, ke^{T})}(x),

as in the memo. 𝓕* = 𝓕 (P46 l. 6640) gives ⟨H^w𝓕F, e_m^±⟩ = ⟨F, φ_m^±⟩ with φ_m^± = 1_{I_T}𝓕(H^w)*e_m^±
= e^{t/2}ĝ(e^t) on I_T, ĝ(ξ) = 2∫_0^∞ g(x)cos(2πxξ)dx. Correct.

### 2.2 Step (i)

q(F) = Re⟨α(F), β′(F)⟩ is the quadratic form of the Hermitian form
s(G, F) = ½(⟨α(G), β′(F)⟩ + ⟨β′(G), α(F)⟩). If q is semidefinite on V and α(F) = 0, then q(F) = 0 and,
by Cauchy–Schwarz for semidefinite forms, s(G, F) = 0 for every G ∈ V; since α(F) = 0 this leaves
⟨α(G), β′(F)⟩ = 0 for every G ∈ V, and surjectivity of α on V gives β′(F) = 0. Hence
ker α ∩ V ⊂ ker β′ ∩ V and β′ = B′α on V. Surjectivity on P_T is equivalent to no nontrivial
combination of e_m^± (m ≤ L) lying in the span of e^{±t/2}, true by
linear independence of exponentials with distinct exponents. Correct. The step holds equally for real F
(the real symmetric form and its Hermitian extension are semidefinite simultaneously).

### 2.3 Step (ii)

β − Bα = B′α on P_T means that each φ_m^±, as a function on I_T, lies in the span of
e_j^± (j ≤ L) and e^{±t/2} (a bounded functional vanishing on P_T is represented by a Tate
vector). Dividing by e^{t/2} and with ξ = e^t: ĝ(ξ) = Σ_j (c_j^+ ξ^{−2j−1} + c_j^− ξ^{2j}) + d_+ + d_−ξ^{−1}
on (e^{−T}, e^{T}). ĝ is entire (g bounded with compact support in (0,∞)); the equality propagates to
ℂ∖{0}; an entire function has no principal part at 0, so ĝ is a polynomial; bounded on ℝ, it is
constant; it tends to 0 (Riemann–Lebesgue), so it is zero; g = 0. Correct.

g ≠ 0: the indicators of the intervals (ke^{−T}, ke^{T}) are linearly independent (on the
stretch (k_0e^{−T}, (k_0+1)e^{−T}), with k_0 the smallest index in the support of w, only k_0 contributes). Hence
g ≠ 0 **for every nonzero w, real or complex, with no sign condition**.

Conclusion: the proof is complete and supports the quantifiers "every finite L", "every Hermitian
2L × 2L B", "a single k". The corollary on ±C = Σ_k h(k)|ℓ_k|² + ρ is correct: a sum
(finite or convergent) of squared moduli of functionals factoring through α is ⟨α, Bα⟩ with
B ≥ 0, and the case −C is obtained with −B.

Search for counterexamples: tried (a) w with signs, (b) k ≤ N, including k = 1, (c) overlapping
intervals, (d) real F. In all four the proof still holds; there is no counterexample.

### 2.4 What the statement says too much and too little

**Too much in the hypotheses.** Neither w ≥ 0, nor k > N, nor M ≥ N ≥ e^{2T}, nor the value of b_m (b_m ≠ 0
for some m suffices) intervene. The correct statement is: for every complex weight w ≠ 0 of finite support
in k ≥ 1. Consequence for the reading: the Lemma is not a fact about the tail k > N nor about h; it is the
fact that the span of finitely many Gamma exponentials, modulo Tate, is not invariant
under the compression of H^w𝓕 to the window. It holds equally for the interior block, for cΛ, for a_P and
for any comb: it survives the whole battery, as the memo acknowledges. It is a format
obstruction, not an arithmetic one.

**Extensions given by the same proof (PROVED, same lines).**
(a) ℓ_k and B may use moments up to any finite L′ ≥ L with the test Σ_L: apply step (i)
with α of order L′ and β padded with zeros.
(b) The test may be 𝒪_L*G𝒪_L + J𝒪_L*G′𝒪_LJ with any invertible Hermitian G, G′, or
any invertible Hermitian form on the 2L moments: replace β by Gβ.
(c) The exponentials of the test may be finitely many e^{ct} with any real c: if ĝ agrees on an
interval with Σ_p c_p ξ^p (distinct real exponents), it agrees on (0,∞) by real analyticity; the
term of largest exponent forces, with ĝ → 0 at +∞, that there be no exponents ≥ 0, and the one of smallest
exponent forces, with ĝ bounded at 0+, that there be no exponents < 0.

**Too little: the parity sector.** The vectors on which the sign is needed have definite
parity, Σ_L commutes with J, but C is not J-invariant (J𝓕J = J u_∞(D) ≠ 𝓕). Indefiniteness
on P_T does not imply indefiniteness on P_T^ε = {F ∈ P_T : JF = εF}, and the memo does not prove it.
It holds, with the following proof (written in this review; pending the usual independent
verification before being cited as part of the NO-GO).

*Complement (PROVED).* For w ≠ 0 of finite support, ε = ±1, finite L and Hermitian L × L B, the form
F ↦ C^w(F) − ⟨α^+(F), Bα^+(F)⟩ is not semidefinite on P_T^ε.
*Proof.* On P_T^ε, α_m^− = εα_m^+, hence C^w = Re⟨α^+, β^+ + εβ^−⟩, and α^+ is surjective
onto ℂ^L (the functions e^{−a_mt} + εe^{a_mt} and e^{t/2} + εe^{−t/2} are independent). By step
(i), if the form were semidefinite, the parity-ε part of ψ_m = φ_m^+ + εφ_m^− would lie in the
span of e^{−a_jt} + εe^{a_jt} (j ≤ L) and e^{t/2} + εe^{−t/2}. With ψ_m = e^{t/2}G(e^t),
G = ĝ_+ + εĝ_− entire, bounded on ℝ and with G(ξ) → 0 as ξ → ±∞, and multiplying by ξ^{1/2}:

    ξG(ξ) + εG(1/ξ) = Σ_{j≤L} c_j (ξ^{−2j} + εξ^{2j+1}) + d(ξ + ε)   on (e^{−T}, e^{T}),

and by analyticity on ℂ∖{0}. For ξ → +∞ the left-hand side is o(ξ), hence c_j = 0 and d = 0. There remains
G(1/ξ) = −εξG(ξ) on ℂ∖{0}; as ξ → 0 the right-hand side tends to 0, i.e. G(z) → 0 as
|z| → ∞ in all of ℂ, and G ≡ 0 by Liouville. Then g_+ + εg_− = 0, where

    (g_+ + εg_−)(x) = x^{−1/2} Σ_k w(k) k^{−1/2} [ (k/x)^{a_m} + ε (x/k)^{a_m} ] 1_{(ke^{−T}, ke^{T})}(x).

On (k_0e^{−T}, min(k_0, (k_0+1)e^{−T})) only k_0 contributes and the bracket is nonzero (x < k_0).
Contradiction. ∎

### 2.5 Exact class of the NO-GO

Class 𝒞_fin: exact identities, on all of P_T or on a whole parity sector P_T^ε, of the form

    ± Re⟨H^w𝓕F, ΣF⟩ = ⟨α_{L′}(F), Bα_{L′}(F)⟩ + ρ(F),   ρ ≥ 0,

with Σ an invertible Hermitian test on finitely many moments of real exponentials (in particular
Σ_L), α_{L′} finitely many Gamma moments, B any Hermitian matrix (in particular B ≥ 0, which covers
Σ_k h(k)|ℓ_k|² with ℓ_k factoring through α_{L′}) and w any nonzero weight of finite support. No
member of 𝒞_fin exists. The NO-GO is exact, not quantitative: the Gamma exponentials are
complete in L²(I_T) and remain so after removing finitely many (CITED: Müntz's theorem on an interval
[a,b] with a > 0; it is the density argument of P46 after eq:Gammaenergy), so that each φ_m^± is
approximated in norm by combinations of e_j^±, j ≤ L′, with error as small as desired as
L′ grows. The Lemma excludes equality, which is what zero slack demands, and nothing more.

## 3. Observation (2)

### 3.1 Verification

ĝ(ξ) = 2∫_0^∞ g(x)cos(2πxξ)dx = Σ_{j≥0} γ_j ξ^{2j}∫_0^∞ g(x)x^{2j}dx with γ_j = 2(−1)^j(2π)^{2j}/(2j)!
(the memo's integral should be read over (0,∞)). For φ_m^+ with weight h:

    ∫_0^∞ g x^{2j} dx = Σ_k h(k) k^{a_m−1/2} ∫_{ke^{−T}}^{ke^{T}} x^{2j−a_m−1/2} dx
                      = Σ_k h(k) k^{2j} ∫_{e^{−T}}^{e^{T}} y^{2(j−m)−1} dy = Θ_j σ_{j−m}(T),

and for φ_m^−, Θ_j · 2 sinh((2m+2j+1)T)/(2m+2j+1). Since e^{t/2}ξ^{2j} = e^{a_jt}, (2) follows; the term
j = 0 is A(F) = 0. All σ are positive, hence the sign of column j is (−1)^j. Correct.

Convergence: Θ_j is a finite sum (N < k ≤ MN), Θ_j ≤ (MN)^{2j}Σh(k); |μ_j^−(F)| ≤ ‖F‖√(2T)e^{a_jT};
σ_{j−m} ≤ e^{2jT}/max(1, j−m) for large j. The general term is dominated by
C(2πMNe^{2T})^{2j}/(2j)!: absolute convergence. Correct.

Validation of one point (NUMERICAL; T = 0.3, w = δ_2, m = 1, F a cubic polynomial projected to P_T,
80 terms, 40 digits): both sides of (2) give −3.005922708983058…·10⁻⁴, agreeing to 33 digits.

### 3.2 Scope corrections

- **Finite M only.** With the range k > N unbounded, Θ_j diverges for every j ≥ 0; (2) has no limit
  version in M. This should be stated.
- **Cancellation.** The terms of (2) grow up to j ≈ πMNe^{2T} before decaying; their maximal size
  is of order exp(2πMNe^{2T}), whereas |⟨F, φ_m^+⟩| ≤ ‖F‖‖φ_m^+‖ is bounded by the mass
  W_{M,N}. With N ≥ e^{2T} and M ≥ N the cancellation between columns is at least exp(2πe^{6T}). The
  alternation (−1)^j is the Taylor series of the cosine at a large argument; it is not a sign
  structure and no column-by-column argument can use it.
- **Not canonical.** The system {e^{a_jt}}_{j≥1} is overcomplete in L²(I_T) (§2.5), so the
  coefficients of a functional in the moments μ_j^− are not unique. (2) is one expansion, the Taylor
  one; there are others. "The factorization" should read "an expansion in all the moments".
- **Cancellation-free form (PROVED, direct computation).** From 𝓕τ_a = τ_{−a}𝓕 and 𝓕* = 𝓕 it follows that H^w𝓕
  is self-adjoint for real w, with explicit Hankel kernel on the window:

      (H^w𝓕F)(t) = ∫ κ_w(t + s) F(s) ds,    κ_w(v) = 2 e^{v/2} Σ_k w(k) cos(2πk e^{v}).

  Σ_L is also a sum of two Hankel forms (kernels Σ b_m² e^{∓a_m(t+u)}). Thus
  C(F) = ½⟨F, (K_hΣ_L + Σ_LK_h)F⟩ is the Jordan product of two explicit self-adjoint operators,
  K_h compact without sign and Σ_L ≥ 0 of rank 2L. This is the exact expression of which (2) is the
  series expansion; the Lemma says that Ran Σ_L is not invariant under K_h modulo Tate. It has not been
  cross-checked whether this formulation already appears in the corpus; no novelty is claimed and it carries no sign.

Verdict: (2) PROVED as an exact expansion, without sign, with the four precisions.

## 4. Cross-check

Citations opened and checked:

- `R170_816` §§2–7: (3) Φ = B − C, (2) vanishing by support, (6)–(7) two-sided bound, §4 falsification of
  "h(k) ≥ 0 ⟹ pairing ≥ 0", §6 channel d = 2 with two unsigned correlations. Agrees.
  In 816, g = S_LF with S_L = R_L*R_L + JR_L*R_LJ (`R170_811`), which is Σ_L. Agrees.
- `R170_820` (ΔH with the same h_{M,N}, without sign), `821`. Agrees. `819` was read only in its
  setup and at line 287.
- `R170_837` §4 (distinct cells), Thm. 5.1 (literal common residue ⟹ zero radical; "building it
  is building the closure"), (6.7) (weight independence after recombination). Agrees.
- `R170_835` Prop. 4.1 and §4.2. Agrees in content; the ledger is §8, not §9. The proposition
  treats another functional (the product germ) and its proof uses an object foreign to the definitions of
  STATEMENT_001; the memo rightly does not use it. The memo's Lemma is a different statement, with
  its own proof inside the sandbox.
- `R170_841` §4.2, `R170_870` §8: agree.
- P46 eq:Qbalance, eq:Qrecombine, eq:Qspectral, eq:equivgate, rem:returnremarks: agree
  literally with what is cited. `R161_072` §2 (arbitrary non-negative weights), `R161_081`: agree.

On R161_030–039, two corrections.

1. **Status in the index.** Rows G4C-R161_030-032 and G4C-R161_035-038 are listed PARTIAL; rows
   G4C-R161_033-034 and G8B-161 (037–039) are listed DEAD. `R161_033` withdraws the claim of
   `R161_031` that the discrete realization was complete and leaves two OPEN exits: an isometric
   source dilation (§5 A) and the exact compensation of the cross Gram by the polar and
   Tate terms (§5 B). `R161_034` identifies the cross Gram with the product–quotient channel of phase
   106 (DEAD row: it does not cancel against the rank-two Tate in the translation-invariant algebra).
   `R161_037`–`039`: coherent saturation forces F = 0 but does not follow from (PC) and radicality
   (2 × 2 countermodel); terminal equivalence. The memo summarizes "route closed in the index"; the
   exact statement is "realization withdrawn, exits A and B without object, terminal saturation".
2. **It is not the same difficulty.** The obstacle of `R161_033` is the difference between ‖Σ_k u_k‖² and
   Σ_k‖u_k‖², i.e. the Gram terms between distinct k in the **norm** of a coherent sum.
   C is not a norm: it is linear in H, so C = Σ_k h(k)k^{−1/2}Re⟨τ_{log k}𝓕F, Σ_LF⟩
   exactly, without cross terms between distinct k. The direct sum in k is automatic for C; what is
   missing is that each summand be a square, and that is what the Lemma denies in 𝒞_fin. The sentence "the
   recorded obstacle (coherence in k …) depends on neither of the two things" mixes two
   obstacles. The antecedent that does record the real difficulty is `R170_816` §4 (pairing of
   two distinct vectors with positive coefficient) and P46 eq:Qspectral. The repetition verdict
   holds by these, not by R161_033. The LEDGER note ("literal conversion not attempted in
   any memo") remains true; the Lemma is the first proved statement about it.

Sandbox: the memo neither names nor uses external equivalences. Compliant.

## 5. What the memo discards too much

### 5.1 "Finite-rank test": counterexample

Let K be the compression of H^w𝓕 to P_T (w real, nonzero, finite support). K is self-adjoint (§3.2),
compact and nonzero: a finite-rank Hankel operator has a polynomial-exponential kernel
(Kronecker), which would force Σ_k w(k)cos(2πkx) to be on (0,∞) a finite sum of terms
x^p(log x)^q; the entire extension of the left-hand side forces a polynomial, bounded, constant: impossible.
Let u ∈ P_T, ‖u‖ = 1, Ku = λu, λ ≠ 0 real, and Σ_u = |u⟩⟨u|. For F ∈ P_T,

    Re⟨H^w𝓕F, Σ_uF⟩ = Re ⟨F, Ku⟩⟨u, F⟩ = λ |⟨F, u⟩|².

It is a square of fixed sign on all of P_T, with a positive rank-one test, for any w and in
particular for w = δ_k with a single k > N. Hence "do not relaunch with any finite-rank test" is not
a consequence of the Lemma and, as an impossibility claim, is false. (PROVED.)

This reopens nothing: the square is generic in the weight, survives the whole battery, loses the
moment cell that produces D_Δ (`R170_837` §4) and has no written relation with a_T; it is the
finite-rank variant of the memo's own (D2). But the closure must be phrased with the class
𝒞_fin of §2.5 and not with "finite-rank test".

### 5.2 What remains NOT excluded (delimitation)

The Lemma and the Complement say nothing about:

1. **L = ∞.** With Σ_∞ = 𝒪*𝒪 + J𝒪*𝒪J (Hankel kernel −(k_Γ^+)′ of eq:Gammaenergy) or with ℓ_k and B
   on the whole sequence of moments, the proof does not apply (the span is dense). The
   semidefiniteness of C_∞ − ⟨α, Bα⟩ with B bounded on ℓ² is OPEN, no object.
2. **B and C together.** The Lemma treats the isolated tail modulo forms in moments. The real obligation of
   `R170_816` (8), (11) is B − C − (1 − q_0)‖𝒪_LF‖² with B = Re⟨({X,E_N} − L_M*E_N)F, Σ_LF⟩ minus the
   Tate term. The functionals of B do not factor through moments and nothing has been proved about the
   sum. An identity in which the non-factorizable part of the tail cancels against that of E_N is
   not in 𝒞_fin.
3. **ℓ_k that do not factor through finitely many moments.** Functionals of the exterior values of 𝓕F, of
   the collar tails, or any ℓ_k continuous on L²(I_T) outside the space of finitely many
   exponentials.
4. **Tests outside finite real exponentials**, including those adapted to the operator (§5.1) and
   those of infinite rank.
5. **Domains other than P_T or a complete parity sector.** On a finite-dimensional subspace
   where α is injective every form factors through α (it is the a posteriori factorization of
   `R170_835` §4.2); the Lemma does not restrict cones or proper subspaces.
6. **Nonlinear operations in F.** The memo says it found none and that the available ones
   give (D2) or per-vector statements; this is a search report (ARGUED), not a closure. Not
   examined: the envelope in the free parameters of the family of identities (thm:PCfinite holds
   for all M ≥ N ≥ e^{2T}, all L and all δ > 0; infimum or average over (M, N, L, δ) depending on F);
   the choice of Σ depending on F outside the radical; compositions of C with itself.
   None has a written object; none is excluded.
7. **Remainders without a manifest sign separately** that are non-negative only when added to the
   E_N and Tate blocks.

The sentence "the only thing left not excluded is the complete matrix (2)" must be replaced by this list.
The memo's final requirement (interior block with sign opposite to the exterior) is a design
indication consistent with restriction R1 of REVIEW_001_ABD; it is not a proved necessity (ARGUED).

## 6. Exact corrections to ROUND_002_A

1. Lemma, statement: replace "w(k) ≥ 0, not all zero, with finite support in k > N" by "w complex,
   nonzero, of finite support in k ≥ 1", and add that the Lemma does not use h, Λ or the range k > N.
2. Add the parity Complement (§2.4) or state that the Lemma is proved only on P_T.
3. Class: that of §2.5 (finitely many real exponentials in the test, finitely many moments in ℓ_k and B, non-negative
   remainder on P_T or P_T^ε, exact identity).
4. (D1): withdraw "the only ones", "the only one", "exactly three ways", or label them ARGUED;
   correct the gloss of ℓ_k (§1.2).
5. Observation: add "finite M; Θ_j diverges without a cap in k", the note on exponential cancellation, the
   non-uniqueness of the expansion, and the Hankel form κ_w.
6. Cross-check (1)a: "R170_835 Prop. 4.1 and §8". Cross-check (1)b and (3): rewrite according to §4, points 1–2.
7. "Next step": replace "in no variant of range of k, weight or finite-rank test" by
   "in no variant of range of k or of weight with a test of finitely many real exponentials and ℓ_k in
   finitely many Gamma moments"; replace "the only thing left not excluded" by the list of §5.2.
8. LEDGER K1: not "closed in the finite-L formulation", but "the conversion of the isolated tail into
   Σ_k h(k)|ℓ_k|² with ℓ_k in finitely many Gamma moments plus non-negative remainder is NO-GO (𝒞_fin); the
   joint conversion of the pairings of H_{M,N} and E_N, which is how the row states the
   residue, remains without object and without exclusion".

## 7. Annotation text for the index and the grid

> **Phase 212, exterior tail of the hyperbola as a sum of squares in Gamma moments — NO-GO with
> class, PROVED (`ROUND_002_A.md`, Lemma; review `REVIEW_002_A.md` §§2.4–2.5).** Class: exact
> identities ±Re⟨H^w𝓕F, ΣF⟩ = ⟨α, Bα⟩ + ρ(F), ρ ≥ 0, on all of P_T or on a parity sector, with Σ
> an invertible test on finitely many real exponentials (in particular Σ_L), α finitely many Gamma
> moments, B any Hermitian matrix and w any nonzero weight of finite support (in particular h(k),
> k > N, or a single k). None exists: the functionals F ↦ ⟨τ_{log k}𝓕F, e_m^±⟩ do not factor through
> finitely many moments (entire cosine transform of a compactly supported function). The Lemma does not use
> h, Λ or k > N: it is generic in the comb, survives the whole battery and carries no sign. It does NOT exclude:
> L = ∞; the sum of the tail with the E_N and Tate blocks; ℓ_k or tests outside finitely many
> exponentials (with a rank-one test adapted to the operator the tail is a square, generic
> and unrelated to a_T); proper domains of P_T; nonlinear operations in F. Antecedents:
> `R170_816` §4, P46 eq:Qbalance–eq:Qspectral, `R161_033`. Global sign OPEN.

## 8. What was checked and what was not

Checked by independent derivation: (1); steps (i) and (ii) of the Lemma; g ≠ 0 for arbitrary w; (2) with its
convergence; self-adjointness and kernel of H^w𝓕; counterexample of §5.1; parity Complement.
Checked by reading: the citations of §4. Not checked: `R170_819` and `R170_821` beyond the
cited lines; grid rows other than the phase 212 section; whether the Hankel
formulation of §3.2 has an antecedent in the corpus. The Complement of §2.4 and the counterexample of §5.1
are proofs of this review and have not passed a second reader.
