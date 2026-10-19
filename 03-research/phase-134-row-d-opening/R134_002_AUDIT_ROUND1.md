# R134.002 — Audit of record, round 1 (Paper 46, row D opening)

Target: `04-papers/46-intersection-frame-defect/archive/main.md` (1310 lines),
against `R134_000_BLUEPRINT.md`, `R134_001_ROUND1.md`, Papers
43–45 by number, `P124.013`, `P124.014`, and both scripts re-run.

**Headline.  The paper does not violate the no-sign rule anywhere — verified
by grep and by reading every occurrence.  Nothing is FATAL.  Seven MAJOR
findings, of which three are substantive: (M1) the Bochner–Schwartz step of
Theorem 3.7 is justified by a false temperedness claim — `ϖ = 2\cosh(t/2)` and
`W_{fin}` are *not* tempered distributions; the step is repairable and the
repair strengthens it; (M2) §5's Gram matrix is cited to a theorem (Paper 44
Thm 8bis.1e) whose width hypothesis and `0 ∉ supp(h_m⋆h_n^†)` hypothesis both
fail over the entire informative window `ε ≥ 0.5` of the §5.4 table — the
object survives, the citation does not; (M3) Definition 6.8's concluding
inequality runs the wrong way.  Grades: D.1 `RESTATEMENT` (+ two small genuine
`PROVED` lemmas), D.2 `PROVED` (structural) `+ COMPUTATIONAL`, D.3
`COMPUTATIONAL` with one real theorem (5.8), D.4 `PROVED` negatives with a
defective synthesis, D.5 `PROVED`.  Of the three findings against the corpus:
finding 2 **confirmed and strengthened** (it also governs Paper 46's own §4
numerics), finding 3 **confirmed by independent re-run**, finding 1
**overstated and partially refuted**.**

All numerics below were re-run by me from the repository scripts; every number
I quote is my own output, not the construction's.

---

## 0. Reproduction performed

* `d134_gram.py --model zeta --N 10 --eps 2.0 1.0 0.5 0.3 0.1 --check`:
  reproduces the paper's `ζ` column exactly — `(0,0,7)` at every `ε`, full `G`
  inertia `(1,0,8)` — and the `--check` validation table to all printed
  digits (`1.476009/1.470692/1.469943` against `K = 1.469694`, etc.).
* `d134_sigma.py --model zeta --tmin 0.72 --tmax 2.2 --steps 8` at
  `refine = 2`: reproduces `B_T`, `Σ(0.72)`, the swap defect (`7.1·10^{−15}` …
  `4.1·10^{−13}`) and the non-monotone `λ_{\min}Σ` sequence exactly.
* **New:** the same at `refine = 3,4,5,6` (§4 below) and a `refine = 5` sweep
  in `T`; and an independent `Ξ_{0.35}` resolution sweep of `λ_{\min}(L_T)`
  (§8 below).

---

## 1. Findings, graded

### MAJOR

**(M1) Theorem 3.7, proof of (c) ⟺ (d) — the temperedness justification is
false.**  *Location:* main.md ll. 389–393: "`𝔏` is tempered because `ϖ`,
`W_{fin}`, `ω_∞` are (Paper 44 Definition–Theorem 3bis.8 for the last two) and
`Π²` preserves `S'(R)`."
*Error.*  `ϖ(t) = 2\cosh(t/2)` grows exponentially and is **not** in `S'(R)`.
`W_{fin} = Σ(\log q)q^{−k/2}(δ_{±k\log q})` carries mass `Λ(n)n^{−1/2}` at
`t = ±\log n`, i.e. mass `≈ e^{|t|/2}·|t|` per unit length: pairing it with a
Schwartz function diverges (`ΣΛ(n)n^{−1/2}(\log n)^{−k} = ∞` for every `k`), so
`W_{fin} ∉ S'(R)` either.  Paper 44 Def–Thm 3bis.8 constructs these as Radon
measures against `C_c^∞` tests and does **not** assert temperedness.  As
written, the one hypothesis-check of the section's central theorem is wrong,
and Bochner–Schwartz (X3) is being applied outside its stated domain.
*Repair (and it strengthens the result).*  Two steps, both available.
(i) `Π ϖ = 0` identically — `(−∂_t²+¼)e^{±t/2} = 0` — so `Π²ϖ = 0` and
`𝔏 = −Π²(W_{fin}+ω_∞)`; the exponentially growing summand is not in `𝔏` at all
(the paper's own repair note (b) says the polar packet "drops"; it should say
it drops *identically*, and then not cite `ϖ` for temperedness).
(ii) Do not claim temperedness a priori.  The correct import is
Bochner–Schwartz in its `D'(R)` form (L. Schwartz): *a positive-definite
distribution on `D(R)` is automatically tempered and is the Fourier transform
of a positive tempered measure.*  Then (c) ⟹ (d) needs no hypothesis, and
(d) ⟹ (c) is trivial.  `𝔏` must be typed as an element of `D'(R)`, not
`S'(R)`, in (3.2), and (d) must read "`𝔏` extends to a tempered distribution
and equals `\hatμ`".  With that, the equivalence stands.  **(X3) must be
restated in §8 accordingly.**

**(M2) Definition 5.1 / (5.1) — two hypotheses of Paper 44 Theorem 8bis.1e are
dropped, and both fail over the whole informative window of §5.4.**
*Location:* ll. 648–667 ("(5.1) is the **integral** form (8bis.6), which
carries **no** width hypothesis") and l. 667 ("the finite atoms contributing
nothing at `Δ = 0` once `2ε < \log 2`").
*Error, in three parts.*  (a) Paper 44 Theorem 8bis.1e carries the width
hypothesis `ε < ε_0(A,S)` **in its own statement** (main.md l. 3503 ff.,
"[REBUILT … findings `m1` and `M4`: the two hypotheses this statement inherits
are now carried explicitly.  (a) *Width* …]"), not only in the concentrated
reading; Paper 46 re-reads Paper 44 against its own hypothesis-carrying rule.
(b) Theorem 8bis.1e also assumes `0 ∉ supp(h_m⋆h_n^†)`, because its proof goes
through Theorem 3bis.7, which assumes it.  At `ε = 2.0, 1.0, 0.5` every pair
`m,n ≤ 30` has `|Δ_{mn}| ≤ \log 15 < 2ε` or close to it, so `0 ∈ supp` for
essentially every entry, and `ω_∞ = K(|t|)dt` is **not integrable at `0`**
(`K(t) ∼ 1/2t`): the displayed integral (5.1) does not converge.
(c) The paper's own sufficient condition `2ε < \log 2` for the diagonal
treatment means `ε < 0.347`, which **fails at `ε = 2.0, 1.0, 0.5`** — four of
the six rows of the §5.4 table, including every row in which the falsifier
fires.
*What is actually computed.*  `d134_gram.py` evaluates the archimedean half in
`τ`-space against `\hatω(τ)`, i.e. the **regularized** object of Paper 43
(14.1) with `c = 0`, and includes all finite atoms in `t`-space.  That is a
perfectly well-defined object for every `ε` — but it is
`I_∞(Γ_{h_m},Γ_{h_n})` **as given by Paper 45 Theorem 9.6 / Paper 43 (14.1)**,
not by Paper 44 (8bis.6).
*Repair.*  Re-derive (5.1) from Paper 45 Theorem 9.6 (which carries no width
hypothesis, handles `0 ∈ supp h` through Lemma 5.1a, and is the theorem Paper
45's own proof insists must be used in place of 3bis.7 exactly here), or
equivalently from Paper 43 (14.1) in `τ`-space.  Cite 8bis.1e only for the
*interpretation* of the entries as the Frobenius Gram form, in the regime
where its hypotheses hold (`2ε < \min|Δ|`, i.e. `ε = O(1/N)`) — which, as
Remark 5.9(2) already says, is disjoint from the informative window.  **The
numbers survive verbatim; the attribution does not.**

**(M3) Definition 6.8 — the concluding inequality runs the wrong way.**
*Location:* ll. 1043–1046.  From (R3), `h(F) − h(F^∨) = ½I_∞(F,F) + ℓ(M(F)) +
χ`, the paper concludes from "`h ≥ 0` and `h(F^∨) = 0` on the primitive
sector" that `I_∞(F,F) ≤ −2ℓ − 2χ`.  Substituting `h(F^∨) = 0` gives
`h(F) = ½I_∞ + ℓ + χ ≥ 0`, i.e. `I_∞ ≥ −2ℓ − 2χ`: a **lower** bound, the
opposite of row D's target.
*Repair.*  The vanishing theorem must be on `h(F)` for primitive `F`, with
nonnegativity used on the dual: `h(F) = 0`, `h(F^∨) ≥ 0` gives
`½I_∞ = −h(F^∨) − ℓ − χ ≤ −χ` on primitive classes, i.e. `I_∞ ≤ −2χ ≤ 0`
when `χ ≥ 0`.  (R2) and (R4) must be rewritten so that the declared vanishing
class is the one carrying the quadratic term, not its dual.  This is the
requirement list the rest of row D is supposed to shoot at, so it must be
right; and it is a *directional* error in the one paper whose rule is that no
direction may be assumed.

**(M4) Theorem 5.4 is not proved as stated.**  *Location:* ll. 711–717.  The
step "the Dirichlet factor `Σc_nn^{−iτ}` is almost periodic, hence cannot
concentrate" is an assertion, not an estimate, and it is very likely false in
the only form that matters: a Dirichlet polynomial can be resonated
(`c_n = a_nn^{iτ_0}` gives a Dirichlet-kernel peak at `τ_0` of height `Σ|a_n|`
and width `∼1/\log N`), and against the **fixed** envelope `|\hatφ_ε|` — which
decays only polynomially — a peak at `τ_0` with `N` growing with `τ_0`
can carry an arbitrarily large share of the weighted mass.  The bound
`|\hat F| ≤ |\hatφ_ε|Σ|c_n|` does not exclude it, because `Σ|c_n|` is free.
*What is true, and is all that is needed.*  At **fixed `N` and `ε`** the span
is `(N−1)`-dimensional, so Theorem 14.1's infinite-dimensional conclusion is
vacuous on it for trivial reasons; and the concentration profiles
`φ_{a,δ}(t) = δ^{−1/2}e^{iat}φ_0(t/δ)` are not elements of the span, so 14.1's
construction is not literally available.  Whether the mechanism revives in the
colimit `N → ∞` is **`OPEN`, not refuted** — and by Theorem 5.5 it may not be
asserted in either direction.  *Repair:* restate 5.4 with the trivial
dimension argument and the non-membership of the profiles, and mark the
colimit question `OPEN` (it is already implicitly so by 5.5).  The refutation
of blueprint D.3(a) survives, carried by Theorem 5.5 alone.

**(M5) Finding 4.8 is overstated; P124.013 Corollary 3.3's criterion is not
basis-dependent in the sense claimed.**  *Location:* ll. 624–636, §9.3(1).
Corollary 3.3's criterion is `\liminf_{T↑T_*}λ_{\min}Σ(T) > −∞` with
`T_* = T_q < ∞`.  Under a congruence `Σ ↦ C(T)^{\mathsf T}Σ C(T)` with `C`
continuous and nonsingular on a neighbourhood of the **finite** `T_*`, the
condition numbers are bounded on that neighbourhood, so `\liminf > −∞` is
**invariant**; and the two bases compared (named vs Gram-orthonormalized)
differ exactly by such a `C(T)` (`‖φ_σ‖ ∼ e^{T/2}`, bounded near finite `T_*`).
What is correct is the weaker statement: the **numerical value** of
`λ_{\min}Σ(T)` is not a congruence invariant and may not be quoted or compared
across bases or papers, and `Σ(T) ≥ 0` is the form to carry.  *Repair:* state
Finding 4.8 in that weaker form; withdraw "basis-dependent as stated"; the
recommendation to the corpus ("carry (3.2)") stands on the weaker ground.

**(M6) The paper does not apply its own §9.3(2) finding to its own §4
numerics.**  `d134_sigma.py` uses `p124_lab.assemble` unchanged — the same
piecewise-constant Galerkin space.  Both `λ_{\min}(L_T)` **and** `Σ(T)` are
therefore variational **upper bounds**: `Σ_T(z) = \inf\{𝒲(F+φ_z) : F ∈ P_T\}`
restricted to a subspace of `P_T` is `≥` the true Schur complement.  My
resolution sweep at `T = 0.72` confirms it (table in §4 below):
`λ_{\min}Σ = 2.58, 1.33, 1.19, 0.93, 0.79` (`×10^{−2}`) at `refine = 2,…,6`,
decreasing at every step, and `λ_{\min}(L_T) = 2.95, 2.79, 1.72, 1.29, 1.02`
(`×10^{−1}`), likewise.  Consequence, which §4 must state: **every positive
`Σ(T)` reported in §4.3–§4.4 certifies nothing**, and Corollary 4.4's two
scalar inequalities are not being tested by these numbers.  *Repair:* add the
scope sentence of §9.3(2) to §4.3 and §4.4 explicitly.

**(M7) Paper 46 diagnoses the `B_T` collision and then perpetuates it.**
(1.8) defines `B_T = C⊕C`, the ruling plane; Theorem 4.1 and Theorem 4.2 then
use `B_T` for the Tate **block** of `𝒲` — the very conflation §4.2 exists to
refute.  *Repair:* rename the block (e.g. `𝔅_T`) throughout §4 and say so in
(1.8).  Cosmetic in mathematics, structural in a paper whose §4.2 is a
`REFUTED` about three objects sharing one letter.

### MINOR

**(m1) (3.2) is well defined only modulo a `δ_0` finite part, and that
ambiguity *is* the constant `c` of Corollary 9.6a.**  `ω_∞` is not integrable
at `0`; the parenthetical "with the regularization of Paper 44 (8.5∞)" is
load-bearing.  Two regularizations differ by `κδ_0`, and
`⟨Π²(κδ_0), g⋆g^†⟩ = κ‖Πg‖_{L²}²` — exactly the `c‖F‖²` term Corollary
9.6a(i) isolates.  So the normalization `c = 0` is not merely carried in the
preamble of §3; it *is* the definition of `𝔏`.  Say so in (3.2).

**(m2) (b) ⟺ (c) changes the quantifier from real to complex tests**
("the two quantifiers are the same quantifier", l. 388).  True, but it needs
one line: `𝔏` is real and even, so for `g = u+iv` the cross terms
`𝔏(v⋆u^† − u⋆v^†)` pair an even distribution against an odd function and
vanish, leaving `𝔏(g⋆g^†) = Λ(u) + Λ(v)`.

**(m3) `C_φ` in Theorem 5.8 is imported from Paper 44 (8bis.4c), whose
constant contains a "bounded finite-place mean" — a *chart* quantity** (Thm
8bis.2 is explicitly exempted from `(C1)`).  In Theorem 5.8's own regime
(`2ε < \log 2`, so no finite atom reaches the diagonal) the constant is purely
archimedean.  State the constant that is actually used.

**(m4) Theorem 5.8 mixes a `(C1)`-exempt diagonal with a `(C1)` off-diagonal.**
Harmless in the stated regime (the `t`-space sums are finite), but the
hypothesis-carrying rule requires it to be said, as Definition 5.1 half-says.

**(m5) Theorem 5.2's proof contains a garbled clause** ("`κ_∓(ε) > 0` because
`φ_ε ≥ 0` is not required — it is enough that `κ_∓(ε) ≠ 0`").  The proof is
correct; the sentence is not a sentence.

**(m6) `d134_gram.py`'s docstring still advertises the refuted asymptotic**
("the script checks its `−\log(1/ε) + (γ + \log 4π)` asymptotics"), which
Remark 5.9(3) exists to refute; and `gram(..., verbose=True)` prints that
comparison as though it were the reference.  Stale; fix the docstring.

**(m7) "The blueprint's display is RH written as a definition" (l. 132 of
R134.001; softened in main.md l. 299 to "presupposes the very conclusion") is
one slip too strong.**  With `|ρ(1−ρ)|²` alone the summand
`Φ_g(ρ)Φ_g(1−ρ)` is still not manifestly nonnegative; the triviality needs the
*second* slip `Φ_g(1−ρ) = \overline{Φ_g(ρ)}`, which the blueprint did not
write.  The `REFUTED` verdict is nevertheless **correct**: I re-checked the
arithmetic — `ρ(1−ρ) = 196.24 − 2.8i`, `[·]² = 38502.30 − 1098.94i`,
`|·|² = 38517.98` — and the identity is simply false off the critical line.
Remark 3.5 gets the general statement right.

**(m8) Theorem 4.2's §4.2 numbers are not converged, though its conclusion
is.**  See §4 below: the off-diagonal of `B_T` moves `0.0767 → 0.0854` from
`refine = 2` to `refine = 6` (11%), so the printed matrix must carry a
resolution caveat.  `\det B_T > 0` is robust (`+6.81·10^{−3}` at `refine = 2`,
`+5.20·10^{−3}` at `refine = 6`), so **Theorem 4.2(iii) survives**.

**(m9) Label hygiene.**  R134.001's summary table grades Theorem 4.2 `PROVED`
(+ one `COMPUTATIONAL` witness); main.md's own closing line grades (i),(ii)
`PROVED` and (iii) `COMPUTATIONAL-ILLUSTRATION`.  The paper is right, the
report is loose; the paper's split is the one of record.

### NOTE

**(n1)** §5.4's `ζ` column (`(0,0,7)`/`(0,0,27)` everywhere) and §4's positive
`λ_{\min}Σ` values are, taken alone, sign-suggestive.  They are defused in
place — §5.4 reading item 4, Honest remark 4.5, §9.3(2) — and I record that
the defusal is explicit and adequate.  With (M6) added to §4 it becomes
airtight.

**(n2)** Theorem 4.1's conditionality is stated with unusual honesty ("has no
content for `ζ` unless row D's target fails") and is correct: `T_q < ∞` is the
negation of item 9.1(1).  This is the model for how the rest of the corpus
should cite P124.013.

**(n3)** Proposition 2.1's self-assessment against the P122 acceptance test is
accurate: (ii) is absent, (ii) is row D, and the paper says so.

---

## 2. Verification of the derivations the review asked me to check

**Lemma 3.1 (the bijection).  CORRECT, and it is genuinely new.**
`(−∂_t²+¼)e^{−|t|/2} = δ_0`: away from `0` the symbol annihilates `e^{±t/2}`;
at `0` the first derivative jumps by `−1`, so `u'' = −δ` and `−u'' = δ`.  ✓
For `t` right of `supp F`, `(G_{1/2}∗F)(t) = e^{−t/2}∫e^{s/2}F(s)ds =
e^{−t/2}Φ_F(1)`; left, `e^{t/2}Φ_F(0)`.  ✓  So **the two Tate conditions are
exactly the two conditions that make the Green potential compactly supported**
— the statement is right, and it is the one place in the paper where
primitivity acquires a non-linear-algebraic meaning.  Paper 45 Corollary 10.2
indeed proves only "into … and is injective" (l. 1655 ff.), so the blueprint's
"bijection" citation was wrong and the `REPAIRED` verdict is correct.  Without
Lemma 3.1, Theorem 3.7(b) would be an implication.

**Theorem 3.4 / the Fourier–Mellin dictionary of Theorem 3.6.  CORRECT.**
`Φ_{(Πg)⋆(Πg)^†}(s) = [s(1−s)]²Φ_{g⋆g^†}(s) = Φ_{Π²(g⋆g^†)}(s)`, and equality
of entire Mellin transforms of compactly supported distributions gives
`(Πg)⋆(Πg)^† = Π²(g⋆g^†)`. ✓  `Φ_h(0)+Φ_h(1) = ∫h(e^{−t/2}+e^{t/2}) = ⟨h,ϖ⟩`
✓.  Moving `Π²` onto the distribution is legitimate (`Π` formally
self-adjoint) ✓.  Paper 45 Theorem 9.4 rearranges exactly as displayed ✓.  The
one omission is (m1), and the one simplification the paper misses is
`Π²ϖ = 0`.

**Theorem 3.7 (a) ⟹ (b).  CORRECT** (`1−ρ = \barρ` on the line; `Φ_g(\bar s) =
\overline{Φ_g(s)}` for real `g`; `[ρ(1−ρ)]² = (¼+γ²)² > 0`).
**(b) ⟹ (a)** is Paper 45 Theorem 10.4 plus Lemma 3.1, correctly attributed
and used once and in one direction, as l. 386 says.
**The identification of `μ = Σ_γ(¼+γ²)²δ_γ`** is a tempered positive measure
(`∫(1+|γ|)^{−7}dμ < ∞` by `N(T) ∼ T\log T`) ✓.
**(c) ⟺ (d) ⟺ (e)** is (M1).

**Is there content beyond Weil + Bochner?  No — the construction's press point P1
is upheld.**  I searched the paper for a statement whose *proof* uses the
identification of the group with the carrier's modulus group or of the flow
with `Frob_∞`: there is none.  `(1.2)`/`(1.5)` are used to *name* the group in
Theorem 3.7(e) and nowhere else; deleting the identification changes no proof.
Remark 3.9's two observations (the primitive sector is an ideal, not a unital
subalgebra; the representation comes from Bochner, i.e. from the conclusion)
are correct and are the honest reason the section is not progress.
**Verdict: D.1 must be graded `RESTATEMENT`, not `CLASSICAL +
PROVED-IN-REPOSITORY`** — with Lemma 3.1 and Theorem 3.6 carved out and kept
at `PROVED`, since both are small new theorems and Lemma 3.1 is needed.

**Theorem 4.2(i).  CORRECT, checked by hand.**  `Φ_{φ_+}(1) = ∫_{I_T}e^t =
2\sinh T`, `Φ_{φ_+}(0) = 2T`, and symmetrically; with `M(Γ_F) =
(Φ_F(1),Φ_F(0))` and `β_T(z,w) = z_-\overline{w_+} + z_+\overline{w_-}` the
matrix is `[[8T\sinh T, 4T²+4\sinh²T],[·,·]]` ✓ and
`\det = 64T²\sinh²T − 16(T²+\sinh²T)² = −16(T²−\sinh²T)²< 0` ✓.  This matches
P124.013 (2.3) verbatim (`⟨𝒜φ_σ,φ_τ⟩ + Φ_{φ_σ}(0)Φ_{φ_τ}(1) +
Φ_{φ_σ}(1)Φ_{φ_τ}(0)`) and `p124_lab.assemble`'s `Polar`, which I read.
**The naming question is settled in Paper 46's favour**: Paper 45 Theorem 8.1's
`B_T` is the ruling plane `C⊕C` and is hyperbolic; P124.013's `B_T` is the
Tate block of `𝒲` and is a different object; the blueprint conflated them.
Subject to (M7), Paper 46's §4.2 is correct and is the right correction of
record.

**Theorem 4.3 (the swap law).  PROVED, not numerical.**  The proof is a
genuine invariance argument: `R` preserves `𝒲` term by term (`W_{fin}` even,
`K(|t|)` even, the Gamma multiplier even in `τ`, the polar packet symmetric),
preserves `P_T`, and acts on the border by `σ`; then `X_Tσ = UX_T` and
`σX^*L^{−1}Xσ = X^*L^{−1}X`. ✓  Both algebraic steps check.  The even/odd
splitting and Corollary 4.4 are the spectral decomposition of a symmetric
Toeplitz `2×2` ✓.  The numerics (`swap defect ≤ 4.1·10^{−13}`, reproduced) are
a check, not the proof.  **This is the one structural gain of §4 and it is
real.**

**Theorem 4.6 (monotonicity fails).  PROVED as a statement about the
argument** — the border vectors move with the window, `P_T ⊆ P_{T'}` alone
gives only (4.4).  Correct.  The accompanying numerical non-monotonicity is
discussed in §4 below and **survives my refinement test**, contrary to my
initial expectation.

**Theorem 5.8.  CORRECT, and it is the strongest theorem in the paper.**
I re-derived it: with `ψ̂_ε(τ) = \mathrm{sinc}^4(ετ/2)` and
`\hatω(τ) = −\log|τ| + \log2π + O(|τ|^{−1})` (Paper 44 (8bis.8)), substituting
`σ = ετ` gives diagonal `= (1/ε)[−\log(1/ε)‖φ_1‖² + O(1)]` with
`(2π)^{−1}∫|\hatφ_1|² = ψ_1(0) = c_φ = 2/3` for the triangle ✓ — this is Paper
44 Theorem 8bis.2 (8bis.4b), which does carry the `‖φ‖²/ε` factor (I read the
statement: `−(‖φ‖²_{L²}/ε)(\log(1/ε)+O(1))`).  So the construction's *first* draft
(`εG_N(ε) → c_φA'_N`) was indeed false and the correction is right.  Numerical
check of my own: `(2/3ε)(−\log(1/ε)+2.00)` gives `−2.02` at `ε = 0.1` and
`−173.7` at `ε = 0.01` against the computed `−1.98` and `−175.56` ✓.
Gershgorin then gives unconditional negative definiteness below
`ε_1(N) = \exp(−C_φ−r_N−1)` ✓, and compression preserves it ✓.  Part (c) for
`Ξ_a` is the same computation with `c_φ ↦ 2c_φ` ✓ (the computed diagonal ratio
is `2.00`).
**The deflation conclusion is correct and honestly labelled**: below `ε_1(N)`
the finite inertia is unconditionally negative definite for *every* model, so
it is evidence of nothing; the `Ξ_a` separation lives at `ε` of order one; and
that is precisely where 8bis.7's concentrated reading is invalid — and, by
(M2), where 8bis.1e itself is inapplicable.  Remark 5.9 states all three
consequences against the programme, including the record of the construction's own
refuted first draft.  This is the paper at its best.

**Theorem 5.6.**  Correct and correctly labelled as conditional on its own
hypothesis; its converse is correctly routed to Paper 44 Theorem 8bis.7(c) and
correctly noted to be *harder*, not easier, in view of 5.8(b).  The withdrawn
import `(Wgr)` is not reintroduced (I checked: no occurrence in main.md
outside §8's "withdrawn" line).

**Theorem 5.2.**  Correct (modulo (m5)); `(n^{1/2})` and `(n^{−1/2})` are
independent for `N ≥ 3` ✓; `ε`-freeness is right and is what the compression
in `d134_gram.primitive_compression` implements ✓.

**§6.**  Theorems 6.1, 6.3–6.7 are correct as far as they go; 6.1 is two lines
from Paper 43 Theorem 10.3c(a) (verified: `λ_∓(F) = ∫F|w|^{∓1/2}d^*w > 0` for
`F ≥ 0`, `F ≠ 0`) and Remark 6.2's gloss on what Weil actually does (`h⁰ ≥ 0`
for `aΔ+bΓ`, not for an effective class) is right.  6.5's two counterexamples
are Paper 43 Theorem 10.2(e) verbatim ✓; 6.6 is Theorem 10.8 ✓; 6.4(ii)'s
appeal to P122 §1's prohibition is apt.  6.3 is true but trivial (a single
linear functional), and should be labelled as the strawman it is.  The
synthesis, Definition 6.8, carries (M3).

**§7.**  Theorem 7.1 is correct and is the best-aimed result in the paper:
`n^a+n^{−a} > 2` ✓, the contact of the smeared Frobenius is the shell volume
`\mathrm{vol}(p^kZ_p^×) = \log p` with no free parameter (Paper 44 (3bis.8),
Theorem 3ter.10) ✓, so the would-be Frobenius satisfies
`F_n⋆F_n^† = (n^a+n^{−a})Δ^{(n)}` and fails Theorem 3ter.6's partial-isometry
relation ✓ — and this is a **pre-comparison** failure, as P122 §5 demands.  The
bracketed note that the location of `Ξ_a`'s zeros is *not used* is exactly
right and is the rule-compliant way to handle it.  Theorem 7.4 (DH) is
structural and correctly scoped (`RH1_RH9_AUDIT` retires DH quantitatively;
no DH computation is reported).  Proposition 7.5(b),(c) are honestly declared
unanswered.  Rule 7.6 is the right gate.

---

## 3. What survives, re-derived

1. **`Π : C_c^∞(I_T) → P_T` is a bijection with inverse `e^{−|t|/2}∗`, and the
   two Tate conditions are exactly the compact-support conditions for the
   Green potential.**  (Lemma 3.1; new; needed for the equivalence.)
2. **`Λ(g) = 𝔏(g⋆g^†)` with `𝔏 = −Π²(W_{fin}+ω_∞) ∈ D'(R)`**, the `ϖ` term
   dropping identically because `Πϖ = 0`, and the `δ_0` finite part fixed by
   `c = 0`.  (Theorem 3.6 as repaired by (M1)(i) and (m1).)
3. **RH ⟺ row D's target ⟺ `𝔏` positive-definite on `D(R)` ⟺ `𝔏 = \hatμ`,
   `μ ≥ 0` tempered ⟺ `Λ(g) = ‖π(g)Ω‖²` in a cyclic unitary representation of
   `(R,+)`** — by Weil's criterion (both directions supplied by the
   repository), Lemma 3.1, and Bochner–Schwartz **in its `D'` form**.  A
   restatement; the missing object is named and typed and is not constructed.
4. **The swap law `σΣ(T)σ = Σ(T)`**, hence `Σ(T)` symmetric Toeplitz with even
   and odd eigenvectors and `Σ ≥ 0 ⟺ α ≥ |β|`.  Proved, structural, and the
   only genuinely new structure in §4.
5. **`B_T` (the Tate block) is the `β_T`-pullback plus `⟨𝒜_Tφ,φ⟩` and has no
   predetermined signature**; it is positive definite at `T = 0.72`, robustly
   under refinement.  The blueprint's identification is refuted.
6. **Schur monotonicity in `T` is unavailable** (the border moves); (4.4) is
   all that follows.
7. **`G_N(ε)` is unconditionally negative definite for `ε < ε_1(N)`, for every
   model, because the archimedean diagonal beats the prime atoms by
   `\log(1/ε)`** — so finite inertia at small `ε` is uninformative, and the
   `ζ`/`Ξ_a` separation lives in a window of `ε` of order one where the
   Frobenius reading of the entries is unavailable.  (Theorem 5.8; the
   citation of the entries must be repaired per (M2).)
8. **Blueprint D.3(a) cannot be proved**: under `(C1)` it would negate the
   target (Theorem 5.5, valid); under the chart reading it leaves the window of
   its own kernel formula.  (Theorem 5.4's separate argument needs (M4).)
9. **Five negatives about the shape of a nonnegative invariant**, each with a
   counterexample, and a requirement list — which must be repaired per (M3).
10. **`Ξ_a` fails a row-B axiom before any comparison** (unimodularity of the
    local roots / partial isometry), and DH fails D.1 at its first step.

---

## 4. The resolution study the paper does not have (mine)

`d134_sigma.py --model zeta --tmin 0.72 --tmax 0.72 --refine r`:

| `refine` | `dim P` | `λ_{\min}(L_T)` | `B_T` diag / off | `\det B_T` | `λ_{\min}Σ` |
|---|---|---|---|---|---|
| 2 | 6 | `+2.949·10^{−1}` | `0.11264 / 0.07670` | `+6.81·10^{−3}` | `+2.585·10^{−2}` |
| 3 | 10 | `+2.786·10^{−1}` | `0.11124 / 0.08402` | `+5.31·10^{−3}` | `+1.327·10^{−2}` |
| 4 | 14 | `+1.724·10^{−1}` | `0.11181 / 0.08414` | `+5.42·10^{−3}` | `+1.189·10^{−2}` |
| 5 | 18 | `+1.291·10^{−1}` | `0.11152 / 0.08522` | `+5.17·10^{−3}` | `+9.254·10^{−3}` |
| 6 | 22 | `+1.023·10^{−1}` | `0.11175 / 0.08538` | `+5.20·10^{−3}` | `+7.891·10^{−3}` |

Readings: (i) `\det B_T > 0` is **stable**, so Theorem 4.2(iii) is safe, but
the off-diagonal is only 90%-converged at `refine = 2` (m8); (ii) both
`λ_{\min}(L_T)` and `λ_{\min}Σ` fall monotonically with refinement, which is
(M6) and confirms corpus finding 2 in a second place.

`d134_sigma.py --model zeta --tmin 0.72 --tmax 2.2 --steps 8 --refine 5`
(`λ_{\min}Σ`, `×10^{−3}`): `9.25, 8.29, 10.03, 10.25, 7.90, 6.60, 8.98, 5.30`
— sign pattern of successive differences `−,+,+,−,−,+,−`, **identical** to the
`refine = 2` sequence of Observation 4.7.  So the non-monotonicity is
reproducible across a `3×`-shift in absolute values and is not a
discretization artifact, and it does not track the jumps in `\dim P`.
**Observation 4.7 survives my attempt to kill it**; only its absolute values
must not be quoted.

---

## 5. Verdicts on D.1–D.5

| item | verdict | reason |
|---|---|---|
| **D.1** (§3) | **`RESTATEMENT`** — with Lemma 3.1 and Theorem 3.6 carved out at `PROVED` | Theorem 3.7 is Weil's criterion (both directions from the repository) plus the Bochner–Schwartz/SNAG/GNS dictionary; no proof in the paper uses the identification of the group with the carrier's modulus group.  The construction's press point P1 is upheld; the current label `CLASSICAL + PROVED-IN-REPOSITORY` over-credits the section.  Subject to (M1). |
| **D.2** (§4) | **`PROVED`** (Thm 4.3, Cor 4.4, Thm 4.2(i)(ii), Thm 4.6) **+ `COMPUTATIONAL`** (Thm 4.2(iii), Obs 4.7).  Thm 4.1 `PROVED-IN-REPOSITORY`, **conditional** on `T_q < ∞` | The swap law is a real theorem and the refutations of the blueprint are correct.  Subject to (M5), (M6), (M7). |
| **D.3** (§5) | **`COMPUTATIONAL`**, with **one genuine theorem** (5.8) and two structural ones (5.2, 5.5) at `PROVED`; 5.4 **`OPEN` as stated**; 5.6 `PROVED` from its hypothesis; the tables `COMPUTATIONAL-ILLUSTRATION` | D.3 is deflated by its own Theorem 5.8 over most of its parameter range, and the surviving window is where its kernel citation fails (M2).  Answer to the construction's press point P2: **what is left of D.3 is Theorem 5.8 and the observation that the two models separate in a window; nothing about `ζ`.** |
| **D.4** (§6) | **`PROVED`** negatives (6.1, 6.3–6.7); the synthesis (Def 6.8) **defective** (M3) and, once repaired, `OPEN` | Each negative is a theorem with a counterexample, as required; 6.3 is a strawman and should be labelled so. |
| **D.5** (§7) | **`PROVED`** (7.1, 7.4, 7.5(a)); 7.5(b),(c) correctly declared unanswered | The best section in the paper: the falsifier's failure is identified with a named theorem of row B and is pre-comparison. |

---

## 6. The three findings against the corpus, verified independently

1. **P124.013 Corollary 3.3 "basis-dependent as stated" — PARTIALLY REFUTED.**
   See (M5).  The `liminf` criterion at a **finite** `T_*` is invariant under
   any `T`-continuous nondegenerate rebasing of the border, which is what the
   two bases compared are.  What survives: the *value* `λ_{\min}Σ(T)` is not a
   congruence invariant and must never be quoted across papers or bases; carry
   `Σ(T) ≥ 0`.  The recommendation to the corpus is right; the stated reason is
   not.
2. **Galerkin eigenvalues are variational upper bounds — CONFIRMED, and it is
   the most consequential finding of the round.**  I verified the mechanism in
   the source: `p124_lab.assemble` builds exact form matrices (`gamma_form`,
   `shift_form`, `exp_moments` are exact integrals against cell indicators) on
   a piecewise-constant **subspace**, and the primitive constraint is imposed
   exactly inside it; so the computed `λ_{\min}(L_T)` is `≥` the true infimum.
   My own sweep at `T = 0.72` (§4) shows monotone decrease at every step, in
   agreement with the paper's `T = 1.7` table.  **Extension the paper does not
   make: the same holds for `Σ(T)`, because `Σ_T(z)` is itself an infimum over
   `P_T`** — so every `Σ(T) > 0` in phases 118/124 *and in Paper 46 §4* is
   uninformative, while every negative eigenvalue remains a certificate.  The
   scope carve-out for P123.036's interval-arithmetic endpoint certificate is
   correct and should be retained.  **Answer to press point P4: yes, this
   should be recorded as a standing methodological rule next to "numerics
   illustrate and falsify", and any statement resting on a positive
   double-precision Galerkin eigenvalue must be relabelled.  I found none
   carried at `PROVED` in Papers 43–46; the exposure is in phases 118–124.**
3. **P124.014's `Ξ_a` first-contact brackets are not resolution-stable —
   CONFIRMED by independent re-run.**  My own assembly at `a = 0.35`:
   `λ_{\min}(L_T) = +1.3051·10^{−1}, −1.5833·10^{−1}, −4.3345·10^{−1}` at
   `T = 1.68`, `refine = 2,3,4`; and at `T = 1.7419` (inside the published
   bracket `[1.7413,1.7425]`): `+6.58·10^{−3}, −2.2677·10^{−1},
   −4.6850·10^{−1}`.  By finding 2 the refined values are certificates, so
   `T_q(Ξ_{0.35}) ≤ 1.68`, **outside** the printed bracket.  P124.014 §3
   disclaims convergence explicitly, so this is within its declared scope; its
   four printed decimals must not be cited as a bracket, and its qualitative
   conclusions (a genuine first contact exists; Gate R fails there; case 2 of
   the dichotomy is realized) are untouched.

On the construction's press point **P3** (the falsifier's threshold in `N`): I did
not run `N = 15,20,25` or the `a → 0` degeneration either, and I concur that
until that is done §5.4 item 2 is a statement about the grid.  Given (M2) and
Theorem 5.8, my recommendation is *not* to spend the cycles: the window where
the table is informative is the window where the entries cannot be cited to
8bis.1e, so a finer grid would sharpen a statement that has no theorem behind
it.

---

## 7. Hypothesis-carrying, imports, independence, and the no-sign rule

* **(C1) and the four travelling hypotheses.**  Carried in §0.1, in the
  preamble of §3, in Definition 5.1 and in Theorems 5.5, 5.6, 5.8.  The two
  defects are (M2) (a dropped hypothesis of an imported theorem) and (m3)/(m4)
  (a `(C1)`-exempt constant used inside a `(C1)` statement).  No statement
  silently drops `c = 0`; (m1) notes where it is doing invisible work.
* **Imports.**  §8's table is honest and complete for what the paper uses.
  (X3) must be restated per (M1).  (X6) (Weyl) is listed for Theorem 5.8(b)
  but the proof uses **Gershgorin**, not Weyl — a trivial mismatch, fix the
  tag.  The two withdrawn imports `(Wgr)` and `c_{cut}` do not appear anywhere
  (grep-verified).
* **Independence / zeros.**  Statements about the zeros of `ζ` occur only
  inside (1.9), Theorem 3.7 (where the equivalence *is* with RH), Theorem 5.6
  (under its own hypothesis), and the bracketed note in §7.1 about `Ξ_a`'s
  zeros, which is explicitly not used.  That is exactly the permitted set.
* **The no-sign rule.**  I grepped every occurrence of `positive`,
  `nonnegative`, `≥ 0`, `≤ 0`, `definite` and `sign` in main.md and read each
  in context.  **Every occurrence of a sign attached to `I_∂`, `q_T`, `Λ`,
  `𝔏` or `G_N^{prim}` is one of: the boxed target (quoted), a hypothesis, an
  `OPEN` item, a conditional-on-RH statement, or an explicit disclaimer.**
  The sign statements that *are* asserted concern other objects — `\det B_T > 0`
  at one `T`, `G_N(ε) < 0` for `ε < ε_1(N)` (unconditional, for every model,
  and presented as a *deflation*), `λ_∓(F) > 0` on the effective cone — and
  none of them is, or is presented as, evidence about the target.  §10 says
  `None.`  **Conclusion: the paper does not violate the no-sign rule.**  The
  only latent risk is (n1), closed by adding (M6) to §4.
* **Consistency with the boxed target.**  Paper 46 §0.1 reproduces Paper 45
  §14.4's box character for character, including the standing negatives and the
  `(H_L)` conditionality of 8bis.7; and §5.5/§9.1(1) respect §14.4's four
  "facts row D may not ignore", in particular that the target is a colimit
  statement false at a finite chart.  **Consistent.**

---

## 8. Recommendation to the review

Accept Paper 46 as a skeleton **after** the repairs (M1), (M2), (M3), (M4),
(M5), (M6), (M7) and the minors; none of them costs a result, and (M1) and
(M2) each *improve* the statement they repair.  Regrade D.1 to `RESTATEMENT`
per the construction's own press point.  Record finding 2 as a standing
methodological rule of the corpus.  Do not spend a round on press point P3.
**No label for row D; none is warranted by this campaign.**
