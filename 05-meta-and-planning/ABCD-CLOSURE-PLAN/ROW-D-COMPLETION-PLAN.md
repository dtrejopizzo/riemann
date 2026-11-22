# Row D completion plan — phases 139–143

*Brief: complete row D (the sign); new mathematics is required,
little can be reused from outside; one construction memo and one adversarial audit per round; every idea checked against the corpus before it is built (`CORPUS_CHECK_ROW_D_PLAN.md`).*

## 0. Where we stand (from `R138_005`, the ASCII map)

Built: the frame (canonical class `K`, degree, affine duality, transfer theorem `h⁰ ⟹ RH`), the
intrinsic characterization of the primitive sector (`D^W = Λ ⊥ P^W`), detecting cones (`E = {F ≥ 0}`,
triangles, Landau criterion), the separating zero-free invariant (equimodularity of `|p−½|`) and its
ceiling. Painted: finite windows, magnitude methods, Hilbert–Pólya, Laguerre–Pólya/Li, PNT routes,
`h⁰_Z` growth, phase-65 chain.

**The two theorems that shape the plan.**
* (T1, R137_007/R138_005) Every zero-free "local" structure the corpus can write (polar block, unimodular
  local roots, Frobenius unimodularity, positivity of kernels, functional equation) is shared by every
  Dedekind zeta `ζ_K`. So a proof of the sign from such structure must be **uniform in the global field**,
  i.e. it proves GRH for Dedekind zetas — and must be built as such.
* (T2, to be proved in phase 139) Epstein zeta functions of class number `> 1` share **all** of the above
  except the Euler product (positive coefficients, functional equation, simple pole, equimodular polar
  block) and have off-line zeros. So the proof must use the **Euler product / Frobenius multiplicativity
  essentially** — the phase-136 meta-theorem ("sign = polar block × Frobenius lattice") becomes a theorem
  about methods with two falsifiers pinning its two factors: `Ξ_a` pins the polar block (non-equimodular),
  Epstein pins the Frobenius side (no Euler product).

**Consequence.** The sign must be proved for all global fields at once, using the Euler product
essentially. That is exactly the shape of Weil's theorem for function fields (uniform in the curve; the
Frobenius correspondence is the Euler product). The plan therefore has one organizing question:

> **Q139.** What, in Weil's function-field proof, is the *Euler-product step*, what is the
> *field-uniform step*, and which of them the arithmetic rows A–C already supply. The remaining
> step is the object to construct.

## 1. Phases

### Phase 139 — the two falsifiers and the method theorem
* **D.19 Epstein falsifier in row D's frame (NEW).** For a positive binary quadratic form `Q` of
  discriminant `−D` with class number `> 1`, completed Epstein zeta `Λ_Q(s) = (√D/2π)^s Γ(s) Z_Q(s)`,
  `Λ_Q(s) = Λ_Q(1−s)`, simple pole at `s = 1`, coefficients `r_Q(n) ≥ 0`, off-line zeros (Davenport–
  Heilbronn 1936; CLASSICAL, cite). Build the canonical class `K_Q > 0` with `Φ_{K_Q} = Λ_Q` (Pólya-type
  theta kernel of `Q`), the polar block (`P = {0,1}`, equimodular), the Weil class and `I_∞^{(Q)}`. Prove:
  Hodge index fails; give an effective witness if one exists on the translation cone (expected: **no** —
  the translation cone of an equimodular `Z` is Lorentzian by D.15.4b — so the witness must come from the
  detecting cone `E`, and the theorem is that *equimodularity + positivity + functional equation are
  insufficient*). Label: the method theorem **T2**.
* **D.20 Field-uniform frame (RESTATEMENT + new relations).** Carrier `C_{K,S}`, Weil class, `K_K` with
  `Φ = ξ_K`, `I_∞^{(K)}` for every number field `K`; base change `L/K`: restriction of `I_∞^{(L)}` to
  `K`-classes `= I_∞^{(K)} + Σ_χ I_∞^{(χ)}` over Artin characters (Artin formalism; RESTATEMENT). New:
  which relations base change imposes on the family `{I_∞^{(K)}}` that are *not* consequences of each
  `I_∞^{(K)}` alone (e.g. positivity for `L` is the sum; monotonicity in towers; what the Galois action
  does to the polar blocks). Falsifier: Epstein `Z_Q` sits inside `ζ_{Q(√−D)}` as a class-group-character
  combination — so base change *does* see Epstein: this is where Euler product enters (`ζ_K` is a product
  of Hecke L-functions; `Z_Q` is a sum). Make that precise.
* **D.21 Weil's proof transcribed, step by step (ledger).** Each step of Weil's second proof (Riemann–Roch
  on `C×C`, Castelnuovo–Severi, Hodge index, graph of Frobenius `Γ_q`, `Γ_q·Γ_q' `, trace inequality) with
  its arithmetic analogue in rows A–C (`Frob_n`, `Sh_Z(Frob_n) = [L_S → n → L_S]`, bidegrees, Gram forms,
  `Δ·Δ = −∞`, `K`, degree) and a label: PRESENT / PRESENT-CONDITIONAL / ABSENT. Identify which step is
  the Euler-product step (Frobenius as a correspondence) and which the field-uniform step (RR on the
  square). Reuse Paper 42's ledger if it exists (corpus check item 3).
* **Deliverable:** the exact object missing, stated as a construction problem `(P139)` with its
  acceptance tests: must use the Euler product (fail for Epstein), must be field-uniform (no property
  distinguishing `Q` from `K`), must fail for `Ξ_a`.

### Phase 140 — the Frobenius-side construction
Attack `(P139)` from row B, since T2 says the Euler product is essential. Candidates, checked against the
corpus first: the inverse-semigroup Gram of `{Frob_n}` as a positive-definite kernel on `C_S` and its
relation to the prime term of the explicit formula (`h(log n) = ⟨F, τ_{log n}F⟩`, so the prime term is
`⟨F, 𝒫F⟩` with `𝒫 = Σ Λ(n)n^{−1/2}τ_{log n}`); Rankin–Selberg-type squares (`Frob_n ⋆ Frob_n^†`) as the
arithmetic analogue of Deligne's tensor-power trick — determine precisely what positivity they give
(expected: a Ramanujan-type *weight* bound, not the sign; prove which); the shadow `Sh_Z` as the place
where `deg_det` replaces `h⁰`. Decision rule: any candidate that survives Epstein (uses Euler product) and
`Ξ_a` (uses equimodularity) and does not distinguish `Q` from `K` advances; otherwise it is recorded.

### Phase 141 — the field-uniform step: positivity in towers and families
If phase 140 leaves the field-uniform step open: study `{I_∞^{(K)}}` as `K` varies. What is provable
unconditionally about the *sum* over a family (trace-formula positivity is the one place analytic number
theory proves positivity without hypotheses) and exactly which individual statement remains. Corpus check
first (item 5). This phase either produces the uniform structure or proves that family positivity cannot
descend to individual fields within the frame.

### Phase 142 — assembly or obstruction theorem
Either assemble `(P139)` from the outputs of 140–141 into a construction satisfying (a),(b′),(c) of
Theorem 12.3, or prove the **obstruction theorem**: every construction meeting the acceptance tests of
`(P139)` and built from the structures of rows A–C is equivalent to GRH for Dedekind zetas. The second
outcome is a theorem of record about the programme, not a failure.

### Phase 143 — Paper 47 Part III and label
Enter all corrections of record (P47-1…P47-4 and later), the method theorems T1, T2, the detecting-cone
frame, and the outcome of 142. Label row D by the grep-verified record.

## 2. Rules for every phase
1. Corpus check file before the blueprint; construction memo has a "Corpus check" section per idea.
2. Construction memo and adversarial audit per round; final audit of record; repairs by construction; no relabeling.
3. Three falsifiers, always run: `Ξ_a` (non-equimodular polar block), Epstein `Z_Q` (no Euler product),
   and the `ζ_K` non-distinction test (a proof that distinguishes `Q` from `K` is suspect unless it names
   the distinguishing property).
4. Nothing defined through zero locations; `ξ`, `ξ_K`, `Λ_Q` admissible as data.
5. Numerics only to certify a constant, with a stated robustness margin.
6. A statement that with Paper 47 Thm 3.7 would prove RH or ¬RH is FATAL: flag, do not fix.
7. Each phase ends with a closing decision, PLAN.md paragraph, memory update.

## 3. What would count as completing row D
A function `h⁰` (or an equivalent structure) on the field-uniform frame satisfying (a), (b′), (c) of
Theorem 12.3 for every number field, whose construction uses the Euler product essentially (fails for
Epstein) and the polar block's equimodularity (fails for `Ξ_a`), audited by the adversarial arbiter, with the
transfer theorem giving the sign. Anything less is labelled for what it is.
