# R151.000 — Lead blueprint: phase 151, "the bridge" (T6) and what remains of it

*Lead: Fable 5.1, 2026-09-19. Owner's order: advance towards closing row D; the map of failures is sharp enough
that the bridge making global positivity exist should be found or shown impossible by theorem. Circuit: builder
(Opus) → hostile audit (Opus) → repairs → lead decision. Rules as in phases 149–150. No sign is claimed.*

Read first: `04-papers/46-row-d-the-sign/main.md` §§26–28 (esp. Thm 27.3 (T5), Thms 27.10–27.11, §28.2, §28.4
six clauses); `03-research/phase-36-ABC-forms/106-funtor-amplificador-busqueda.md` §1.1, Thm 1.4, Prop. 3.9
(sterility lemma), §5 (Lema Faltante 5.3, Forma B, Problema 5.4); `03-research/phase-149-row-d-additive-pencil/
R149_005_LEAD_CLOSING_DECISION.md`; `05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-CLOSURE-PLAN-2026-09-19.md` §9.

## 0. The question

Over `F_q`, Deligne's global positivity rests on: (P) the family sum `Σ_x |tr F_x^n|^{2k} ≥ 0`; (R) rationality:
`L(U, F^{⊗k}⊗F̄^{⊗k}, T) = det(1−FT|H¹_c)/det(1−FT|H²_c)`, so the only poles are the a priori ones (`H²_c` =
coinvariants, weight `kw+1`) and the zero block enters as a **numerator**; (L) Pringsheim–Landau: a power series
with nonnegative coefficients has a singularity at its radius of convergence on the positive axis, and that
singularity cannot be a pole of negative residue; hence the radius equals the a priori pole and every local
factor converges up to it, giving `|α_x|^{2k} ≤ q^{kw+1}`. The owner asks for the bridge that makes (R)–(L) work
over `Z`. Phase 151 must decide, by theorem, whether such a bridge can exist for **any family of L-functions over
`Z` in which the fibres enter additively with nonnegative weights**, and, if not, name exactly what shape of
bridge survives.

## 1. T6 — the bridge theorem (to prove)

**Setting.** A *nonnegative additive family* is: an index set `ℱ_N` (finite for each `N`), fibre functionals
`S_f(N)` (`f ∈ ℱ_N`), weights `w_f(N) ≥ 0`, and the family moment `M_{2k}(N) := Σ_{f∈ℱ_N} w_f(N)|S_f(N)|^{2k}`;
the distinguished fibre `f_0` (the one whose zeros are `ζ`'s) has `w_{f_0}(N) ≥ w_0 > 0` and
`S_{f_0}(N) = ψ_w(N) − Nŵ(0)` (or its `μ`-analogue), so that by Theorem 27.10 `|S_{f_0}(N)| = N^{β_max − o(1)}`
along a sequence `N → ∞` (Landau's oscillation theorem on the rightmost zero; state the exact form used).

**T6 (statement to prove).** For every nonnegative additive family and every `k ≥ 1`:
(i) the Mellin transform `𝓜_{2k}(s) := ∫_1^∞ M_{2k}(N) N^{−s−1} dN` has nonnegative "coefficients" (it is the
Laplace transform of a nonnegative measure) and its abscissa of convergence `σ_c(k)` satisfies
`σ_c(k) ≥ 2k β_max`, attained at a real singularity (Pringsheim–Landau for Laplace transforms);
(ii) consequently **any a priori bound `M_{2k}(N) ≪ N^{a_k + ε}` implies `β_max ≤ a_k/2k`**, and conversely the
bound `M_{2k}(N) ≪ N^{2kβ_max + ε}` cannot be improved for the single fibre; so a "bridge" supplying the a priori
exponent `a_k` for all `k` with `a_k/2k → 1/2` **is equivalent to RH**, at every level `k`, for every such family,
independently of the family type (Farey / archimedean / quadratic twists / characters mod `q` / number fields);
(iii) no cancellation between fibres can remove the singularity at `2kβ_max`: the contribution of `f_0` is a
nonnegative summand, and the singularities of a Laplace transform of a nonnegative measure at its abscissa are
not removable by adding further nonnegative measures (make this precise: abscissa of a sum of nonnegative
Laplace transforms is the maximum of the abscissae);
(iv) **the `F_q` mechanism (R) has no additive analogue over `Z`**: in `F_q` the fibre's local pole at
`|T| = |α_x|^{−2k}` lies *outside* the disc of convergence because the total is a rational function with a priori
denominator; over `Z` the fibre's singularity at `s = 2kβ_max` lies *at or inside* the abscissa of the total
(by (iii)). State this as the theorem: *rationality is the one ingredient of Deligne's argument with no
nonnegative-additive counterpart over `Z`, and its role is precisely to place the fibre singularities outside the
region of convergence.* Relate to Doc 106 Prop. 3.9 (sterility) and Lema Faltante 5.3: T6 is their sharp form.

**Corollaries to state.** (a) T5 (Thm 27.3) is the special case where the a priori bound is Parseval; (b) the
`k`-tuple / Hooley VII / Montgomery–Soundararajan moment conjectures are, by T6(ii), RH-strength at every `k ≥ 2`
for their families (recover D.62.2 without Granville); (c) the "promotion of the singular series from density to
polar divisor" (R149_002 §3) is, by T6, the statement `a_k = k + 2c` for all `k`, i.e. RH.

**Falsifiers/gates.** `Ξ_a`: T6 must give `β_max = 1/2 + a` correctly for the `Λ_a` family (a consistency check);
`Ξ_Q`, Beurling: T6 is blind to Euler product and `+` (it is a statement about nonnegative measures) — say so: T6
is a **method theorem about family positivity**, not about `ζ`; `ζ_K`: field-uniform.

## 2. What survives as a bridge shape (to state precisely, not to build)

By T6 the only positivity mechanisms not covered are those where positivity is **not a sum of nonnegative fibre
terms**: (α) self-adjointness / Kreĭn–Hilbert–Pólya positivity `⟨Hf,f⟩ ≥ 0` where the zeros are the spectrum of
one operator (Connes' realization, MW-5); (β) positivity of a form on the square with an *indefinite* signature
controlled by an index theorem (Hodge index; the corpus's rows A–D frame: closed negative in Parts I–IV);
(γ) counting/integrality positivity (degree of an isogeny; number of points): requires a ring of correspondences
(Thm 22.17: none). Write §2 as a **classification of positivity mechanisms** (additive-family / spectral /
index / counting), prove that (β) and (γ) are closed by the theorems already in Paper 46 (cite numbers), and
state (α) as the single open shape, with the corpus's record of it (MW-5, CAND-1, phases 6–8, 29–76, 106) in one
paragraph. Corpus check by grep for each mechanism name.

## 3. Deliverable

`R151_001_BUILDER_ROUND1.md`: §0 summary; §1 corpus check (grep commands + results); §2 T6 with full proofs
(Pringsheim–Landau for Laplace transforms with exact statement and reference; Landau's oscillation theorem for
the rightmost zero, exact form); §3 corollaries; §4 the classification of positivity mechanisms and the single
surviving shape; §5 gates; §6 labels; §7 open list; §8 ≤ 1 page of proposed text for Paper 46 §28 (a "§28.6 The
bridge theorem" addendum). FATAL rule in force. No sign claimed. English.
