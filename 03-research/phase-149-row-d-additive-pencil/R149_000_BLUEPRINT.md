# R149.000 — Blueprint, phase 149: the additive pencil of `Spec Z` and the Deligne extraction

`Spec Z` with closed points over each `F_q` — seen from three sides (no ring of correspondences, 146–148; no a
priori poles of the tensor square, phase 36 + R147/R148 reading; no finite base field, `F₁`); the task is to
CREATE what that object would provide, not to reuse existing mathematics. Corpus check: items
(1)–(5) below are NEW in the corpus; only the Goldston–Montgomery variance ⟺ pair-correlation link (NG-B8,
wrong-signed) and the generic large-sieve magnitude wall (NG-B1) are adjacent. Literature check: the
extraction implication of §D.59 is not stated anywhere (folklore chain, never chained); Hooley's variance
conjecture is REFUTED in some regimes (Bober–Goldmakher; "weaker form" 2024) — binding warning W-H below.*

## The idea, in one paragraph
Deligne's proof of the Weil conjectures does not use a surface, a Hodge index or a sign. It uses: (i) even
tensor powers give nonnegative traces (Rankin); (ii) Landau's lemma; (iii) the poles of the tensor-power
L-function of a FAMILY are computed a priori by invariant theory of the monodromy group, without knowing any
fibre; (iv) an extraction lemma (Weil I, 3.2) bounding each fibre by the family; (v) Künneth amplification.
Over `Z`, (i), (ii), (v) exist verbatim and (iv) is elementary; the object to create is (iii). The family is
the **additive pencil**: `Z(s;α) := Σ_n Λ(n) e(nα) n^{−s}`, `α ∈ R/Z`; fibres at `a/q` are combinations of
`L(s,χ)`, `χ mod q`; the fibre at `α = 0` is `ζ`; the analogue of the field size `q^n` is the length `N`.
The additive structure of `Z` (the `+` that phases 142/146–148 identified as the missing linear-system
structure) enters as the pencil `(a,b) ↦ a + b`, i.e. as the *correlations* of the prime measure.

## D.59 — The extraction theorem (prove first; pure, short, must be exact)
**Statement to prove.** Let `w ∈ C_c^∞(0,∞)`, `w ≥ 0`, and `Λ_Q` the level-`Q` Selberg/Green–Tao majorant
model of `Λ` (fix one; state it). For `N ≥ 2`, `Q = N^c` (`0 < c < 1` fixed), define
`S̃(a/q; N) := Σ_n (Λ(n) − Λ_Q(n)) e(na/q) w(n/N)` and `M_{2k}(N) := Σ_{q≤Q} Σ*_{a mod q} |S̃(a/q;N)|^{2k}`.
**If** for every `k ≥ 1` there are `C_k, B_k` with `M_{2k}(N) ≤ C_k (log N)^{B_k} Q² N^k` for all `N`,
**then** `ψ_w(N) − N ŵ(0) ≪_ε N^{½+ε}` for every `ε > 0`, hence RH. Proof: the `q = 1` term is ≤ `M_{2k}`;
`Σ_n Λ_Q(n)w(n/N) = Nŵ(0) + O(Q²N^{−A})`; take `2k`-th roots; `k → ∞`. Also prove the continuous version
(`∫_0^1 |S̃(θ;N)|^{2k}dθ ≪_k N^{k+ε}` for all `k` ⟹ RH, via Bernstein: a degree-`N` trigonometric
polynomial with sup `V` exceeds `V/2` on measure `≫ 1/N`), and the converse-strength remark: the continuous
hypothesis for all `k` is equivalent to `sup_θ |S̃(θ;N)| ≪ N^{½+ε}` (the additive-twist RH), which is
STRONGER than RH. Label PROVED; novelty: literature check says unstated — record as "folklore chain, first
stated here", not as a discovery. Falsifiers: for `Ξ_a` there is no `Λ`; state what the analogue of `S̃`
would be (`Λ_a(n) = Λ(n)(n^a + n^{−a})`) and check the extraction still runs (it does: the theorem is about
any Dirichlet-series coefficients) — so D.59 is `Ξ_a`-uniform and by itself carries no arithmetic; the
arithmetic must enter in D.60–D.61.

## D.60 — The kill test (decides the phase): what do PROVED moment bounds give?
1. `k = 1`: the large sieve / Barban–Davenport–Halberstam. Write the sharpest unconditional form with its
   error term (`Σ_{q≤Q}Σ_a (ψ(x;q,a) − x/φ(q))² = Qx log Q + O(...)`, Montgomery–Hooley), and run the
   extraction: what does it give for `|ψ(x) − x|`? (Expected: nothing beyond the trivial bound; the
   Siegel–Walfisz-type error `x²(log x)^{−A}` is exactly where the zeros hide. State this precisely: the
   error term of BDH is the `H¹_c` block; the main term is the `H²_c`/coinvariant block.)
2. `k = 2` and higher: what is PROVED unconditionally about `Σ_{q≤Q}Σ_a |ψ(x;q,a) − x/φ(q)|^{2k}`
   (Hooley's BDH series; Vaughan; large-sieve moment inequalities; Green–Tao restriction for the UNcentered
   sum `∫|Σ_{p≤N}e(pθ)|^r ≪ N^{r−1}`)? For each, run the extraction and record the resulting bound on
   `ψ(x) − x`. FATAL rule: if any chain yields a zero-free region beyond the known ones, STOP, re-derive the
   range of `Q` and every error term, run `Ξ_a`; a "new zero-free region from known theorems" is almost
   certainly an error in the range of uniformity.
3. **W-H (binding).** Hooley's conjecture in its literal uniform form is FALSE in some regimes
   (Bober–Goldmakher; the 2024 disproof of a weaker form). Read both, state exactly which ranges of `Q`
   and which normalisations fail, and determine whether the hypothesis of D.59 (with `Q = N^c`, `c < 1`
   fixed, `(log N)^{B_k}` losses allowed) survives the known counterexamples or is already refuted by them.
   If refuted: the phase closes with the theorem "the Deligne extraction over the additive pencil requires
   a hypothesis known to be false" — a genuine finding; then examine whether a different family (Dirichlet
   characters with weights; short intervals per Montgomery–Soundararajan; Farey with restricted denominators)
   evades the counterexamples.

## D.61 — The coinvariant block: additive correspondences and their pairing
1. Define `D_h := {(p,q) : p + q = h}` and `T_h := {(p,q) : q | p − h}` on the "prime square", and the
   density-normalised pairing `⟨D_h, D_{h′}⟩ := lim_X (#(D_h ∩ D_{h′})_{≤X}) / π(X)` where it exists; prove
   `⟨T_h, T_{h′}⟩ = κ(h − h′) := Σ_{q | h−h′} 1/φ(q)` (for `q ∤ hh′`; state exactly), `κ(0) = ∞`.
2. Prove `κ` is a positive-definite function on `Z` (Bochner: `1_{q|d} = q^{−1}Σ_a e(ad/q)` gives `κ` as
   a nonnegative combination of characters), and that it is zero-blind (depends on local densities only).
   Identify it with the singular-series/coinvariant block of D.59's family moments: the main term of
   `M_{2k}` for `k = 1` in terms of `κ`. Label. Compare with the model (`E/F_q`: `Γ_α·Γ_β = deg(α − β)`) and
   with phase 146's degree form (indefinite, zero-blind): here the additive pairing is positive-type.
3. The Künneth of the additive square (CLASSICAL, cite exactly): the average Goldbach function
   `Σ_{h≤X} Σ_{p+q=h} Λ(p)Λ(q) = X²/2 − 2Σ_ρ X^{ρ+1}/(ρ(ρ+1)) + Σ_{ρ,ρ′} X^{ρ+ρ′+1} Γ(ρ)Γ(ρ′)/Γ(ρ+ρ′+2) + …`
   (Fujii; Languasco–Perelli) — exponents add, coefficients are Beta functions. State it as "Künneth for
   the additive square", with the zero–zero block explicit, and explain why Landau on it is useless (top
   pole at 2) and why twisting kills Rankin positivity on the additive square (signed `χ(p)χ(q)`), so the
   Rankin/Landau step must live on the multiplicative square (mean square of `ψ_χ`) while the invariant
   theory lives on the additive one. That split is the finding to state precisely.

## D.62 — The object to create (state as a problem, not a claim)
**Problem (P149).** Find a structure `G` acting on the additive pencil (candidates: the affine group
`Z ⋊ {±1}` on sections; `SL₂(Z)` on `R/Z ∪ Q`; the Bost–Connes / `Ẑ^×` action; a random-matrix
"Katz–Sarnak" law for the fibres) whose invariant theory computes the moments `M_{2k}(N)` — or bounds them
as D.59 requires — WITHOUT knowledge of any individual fibre, and which is compatible with the known
counterexamples to Hooley (W-H): i.e. the law must predict the observed large deviations. State what is
known: Katz–Sarnak equidistribution is a theorem over `F_q` (Deligne) and a conjecture over `Q`; the
large sieve is the only unconditional "invariant theory" (`k = 1`). Record any partial mechanism found
(e.g. Ramanujan-sum orthogonality computes the family moment's diagonal exactly: `M_{2k} ≈ Q²∫|S̃|^{2k} +`
off-diagonal), label, and say exactly what a solution would have to contain.

## D.63 — Synthesis
One page: D.59 proved; D.60 outcome (what known moments give; whether W-H already refutes the hypothesis);
D.61 the coinvariant block; D.62 the problem; the three falsifiers; the reading for row D (the `+` as
additive correlations; where zeros live). Recommendation.

## Deliverables and rounds
`R149_001_ROUND1.md` (D.59–D.63; corpus check per idea; paper-facing; open list; labels), README;
`R149_002`; repairs; confirmation; `R149_005`. Scripts: none required (numerics only if a
counterexample range in D.60.3 needs checking; `--fast`, margins).

## Warnings
* Positivity is free in this route (squares); the gain must come from POLES/moments. Any "positivity
  result" is a restatement — do not label it as progress.
* FATAL: a zero-free region from known moment theorems means a range error. Stop, recheck `Q`-uniformity
  and error terms, run `Ξ_a`.
* W-H: Hooley is false in regimes; the hypothesis of D.59 must be stated with exact ranges and checked
  against the counterexamples before anything is built on it.
* Do not reopen NG-B8 (pair correlation is wrong-signed) or NG-B1 (magnitude-only large sieve cannot fix
  a sign): cite them; the present route does not claim a sign.
