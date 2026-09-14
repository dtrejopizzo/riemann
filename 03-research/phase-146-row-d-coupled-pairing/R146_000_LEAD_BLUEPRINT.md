# R146.000 — Lead blueprint, phase 146: the degree form on `Z[Frob]` with a count interpretation

*Lead: Fable 5.1. Date 2026-09-14. Owner's decision: α in phase 146, redefined after phase 145. Inputs of
record: `R145_005` (the named ingredient: the frame has `⋆` and no `+`; missing effective classes = graphs of
sums `Γ_{m+nπ}`; for `g = 1` bigness = positive-semidefiniteness of the norm form `deg(m+nπ)` on `Z[π]`, a
COUNT; obstruction `Δ·Δ = 2−2g → −∞`; Prop. D.42.5 bigness ⟺ RH), `R145_004` (Q0, Q1, two warnings),
`CORPUS_CHECK_R146.md` (admissibility checklist for any new pairing; P122.028: nothing expressible in
`log p, p^{−½}, N, Γ` alone), `CORPUS_CHECK_R146b.md` (the additive ring structure on Frobenius classes, the
count interpretation of degrees, and the additive-vs-multiplicative locus of the sign are NEW in the corpus;
`Δ·Δ = −∞` is old — Paper 44 Thm 8bis.2, Rem 8bis.1c; Paper 46 Prop 14.2), Paper 44 (Frob_n, `⋆`, `†`,
Thm 3ter.4, Thm 3ter.10 Gram `Λ(n)n^{−½}`, Thm 8bis.1 as corrected §12, 8bis.4a, `Sh_Z(Frob_n) = [L_S →n→ L_S]`,
`deg_det = log n`), Paper 46 §§11–12, the phase-145 model (`R145_001` §D.41 dictionary and Gram).*

Standing rules as before. **Two binding warnings (R145_004):**
(W-a) *Deliver the count, never the positivity.* "The degree form on `Z[Frob]` is positive semidefinite" is
Weil positivity, i.e. RH (Prop. D.42.5 and R144's family `tF + dK`). A round whose output is a positivity
claim for that form has proved nothing; the deliverable is an **object whose degree is a cardinality (or a
Haar measure of a fixed-point set) and is therefore nonnegative by construction**, or the theorem that no
such object exists in the frame.
(W-b) `g = 1` is degenerate twice: `rk End = 2g`, and as `g` grows the norm form becomes Rosati positivity.
Falsifiers: `Ξ_a` (any count-object must not exist or must fail to be a count there), `Ξ_Q` (no Euler
product: the additive structure must be unavailable — say why), `ζ_K` (must be uniform).

## The object
The multiplicative semigroup `{Frob_n}` (Paper 44) with `Frob_m ⋆ Frob_n = Frob_{mn}`, dagger `†`,
`Frob_n ⋆ Frob_n^† = Δ^{(n)}`, bidegree `(n^{½}, n^{−½})`, and the pairing data: off-diagonal
`⟨Frob_m, Frob_n⟩ = Λ(m/n)(m/n)^{−½}`-type when `m/n` is a prime power (a nonnegative count-like weight:
the Haar measure `log p` of the fixed circle of `Frob_{p^k}`), `0` otherwise; diagonal `⟨Frob_n, Frob_n⟩ =
Δ·Δ = −∞` (Paper 44 Thm 8bis.2). In the model: `Γ_α·Γ_β = deg(α−β)`, `Γ_{π^a}·Γ_{π^b} = q^{min}N_{|a−b|}`,
diagonal `2−2g` finite, and the ring `Z[π]` with `deg(m+nπ) = m² + amn + qn² = #ker(m+nπ) ≥ 0`.

## D.44 — Q0: the form is already in the Euler product (interpretation, not data)
1. In the model, `a = q+1−N_1` is read off `κ(1)` (the first Frobenius trace), and the norm form
   `deg(m+nπ)` is determined by `a` and `q`. Write the exact analogue for `ξ`: the "would-be norm form" on
   pairs `(m·1 + n·Frob_ℓ)` from the explicit-formula data (`⟨Frob_ℓ, Δ⟩ = Λ(ℓ)ℓ^{−½}`, bidegrees). Show that
   every entry except the diagonal is a Haar-measure count of fixed points (Lemma: the fixed-point set of
   `Frob_{p^k}` acting on `C_S` and its measure — Paper 44/45's shell volume `vol(Z_p^×) = log p`), and that
   the diagonal is the only entry that is not a count. Label.
2. The shadow's additive structure: `Sh_Z(Frob_n) = [L_S →n→ L_S]` makes `Z[Frob] → Z`, `Frob_n ↦ n`, with
   `deg_det(m + n·Frob_ℓ) = log|m + nℓ|` — a genuine count (`log #(L/(m+nℓ)L)`), additive, but of **rank 1**:
   the endomorphism ring of `Spec Z` seen by the shadow is `Z`. Prove: this is the only additive structure
   compatible with `Sh_Z` (rigidity), and locate exactly what a rank-2 structure would require (a finite
   "trace of Frobenius" `a`; the total trace over `Spec Z` is `Σ_p Λ(p)p^{−½}·…`, divergent — the infinite
   genus seen from the ring).
3. Two degrees of `Frob_n`: `deg_det Sh_Z(Frob_n) = log n` (finite, `H⁰/H²`-type, the bidegree datum) vs
   `⟨Frob_n, Frob_n⟩ = −∞` (the `H¹`-type self-intersection). In the model `Γ_π² = q(2−2g) = (deg π)·χ(C)`.
   State the arithmetic identity `⟨Frob_n,Frob_n⟩ = (log n or n)·(2−2g)` with `2−2g = −∞` and make precise
   that the infinite genus is the infinite dimension of `H¹` (the zero set). RESTATEMENT; cite Paper 46
   Prop 14.2.

## D.45 — Q1: does the additive module `M := Z⟨Frob_n⟩` admit a finite, symmetric degree form?
1. **Difference-only form.** In the model `Γ_α·Γ_β = deg(α−β)` depends only on `α−β`; define arithmetically
   `⟨⟨Frob_m, Frob_n⟩⟩ := "deg(Frob_m − Frob_n)"` := the fixed-point measure of `Frob_m ⋆ Frob_n^†`
   (`= Frob_{m/n}` when `n | m`, transposes otherwise; Paper 44's inverse-semigroup law) — this is the
   off-diagonal Gram entry and is finite and `≥ 0`; **set the diagonal by the same rule**: `deg(Frob_n −
   Frob_n) = deg(0) = ?` — in the model `deg(0) = 0` by convention (`Γ_α² = 2−2g` is a *different* number:
   adjunction). Decide: is there a consistent assignment of the diagonal (a `2−2g` counterterm, finite) making
   `⟨⟨·,·⟩⟩` a symmetric bilinear form on `M` that (i) agrees with `I_∞` on differences `Frob_m − Frob_n`
   (which are in the radical? check: `Φ_{Frob_m − Frob_n}` at zeros — translates of `2K` have `Z = 0`
   (R140 collapse) — the frame's realization is the wrong one; use Paper 44's Gram of `Frob_n^{sm}` instead:
   R140 §D.23.3bis), (ii) is a count on every element `Σ a_n Frob_n` with `a_n ∈ Z` (the analogue of
   `#ker(Σ a_n π^n)`)? Expected: (i) can be arranged (a finite counterterm is a choice), (ii) **cannot** — and
   the exact statement of why (the counterterm's sign, W-a) is the deliverable. Do not claim positivity.
2. **The sum classes.** Model: `[Γ_{φ+ψ}] = [Γ_φ] + [Γ_ψ] − F_2 + 2⟨φ,ψ⟩F_1` (the class map `φ ↦ [Γ_φ] −
   deg(φ)F_1 − F_2` is additive) — prove this in the model and exhibit that `Γ_{1+π}` has a **negative**
   coefficient in the frame's basis `{F_1, F_2, Γ_{π^n}}` (so it is effective but not in `𝓔_C`). Arithmetic:
   define the would-be classes `c_{m,n} := Frob_m + Frob_n − e_+ + 2G_{mn}e_−`-type (fix which ruling and
   the constant from the model's formula and Paper 44's Gram `G_{mn}`); their intersection numbers with
   everything are forced. **Test effectivity in the frame** with the cosh lemma (R142 D.31.4) at `ρ_1`: is
   `|Re e^{iθ}Φ_{c_{m,n}}(ρ_1)| ≤ ½ s_1 deg c_{m,n}`? Compute for small `m, n` (e.g. `(1,2), (2,3), (1,p)`).
   If it fails for some pair, the additive structure **cannot** be realized by nonnegative radial classes and
   the arithmetic `Γ_{m+n Frob}` must be a genuinely two-variable object (a class on `C_S × C_S` not supported
   on shifted diagonals) — state that as the finding and the precise shape it would need. If it passes for
   all tested pairs, say so and mark the general case OPEN.
3. **What `m + n·Frob_ℓ` could mean on `C_S`.** `C_S` is an abelian group; its endomorphisms are power maps
   `x ↦ x^k` composed with the Frobenius translations `x ↦ ℓ·x`; the affine maps `x ↦ ℓ x^k` have graphs
   `{t' = k t + log ℓ}` in the square (slope `k`), but act on characters by `s ↦ ks` and do **not** preserve
   the zero set — so they carry no Lefschetz formula with `ζ`. The model's `m + nπ` is *not* of this form
   (it is addition in `End(E)`, `x ↦ [m]x + π(x)` using the group law of `E`, which has no analogue on `C_S`
   because `C_S`'s group law is the one already used by the Frobenius action). Prove: **the only additive
   structure on Frobenius correspondences compatible with the Lefschetz/explicit formula is the formal one
   (`Z⟨Frob_n⟩` with bilinear extension of the pairing)**, i.e. there is no "sum of correspondences realized
   as a single correspondence" on `C_S`. Label; falsifier: the same is true for `Ξ_a`, so this is not where A3
   enters — record.
4. **The count that does exist.** Fixed points of `Frob_{p^k}` on `C_S`: the shell `|x|_p = p^{−k}`… with
   Haar measure `log p` (Paper 44/45). Fixed points of a *formal* sum are not defined; but fixed points of
   the *composition* `Frob_m ⋆ Frob_n^†` are (that is the off-diagonal count). State the theorem: **on
   `Z⟨Frob_n⟩` the degree is a count exactly on the monomials and on differences, never on sums** — and
   that this is precisely the difference between the multiplicative semigroup and the ring `Z[π]`.

## D.46 — Synthesis input
One page: the answer to Q1 (finite symmetric form: yes/no; count on sums: no, with the theorem); what the
phase proves about **where the sign lives** (additive structure of a ring that `Spec Z` does not have vs the
multiplicative semigroup it has); whether any object on `C_S × C_S` (two variables) could carry the missing
sums; the constraints P122.028/T1/T2 on it; recommendation for phase 147 (an archimedean-bearing model,
O-32, or a two-variable square).

## Deliverables and rounds
`R146_001_BUILDER_ROUND1.md` (D.44 complete; D.45 items 1–4 with the cosh test computed; D.46; corpus check
per idea; paper-facing; open list; label), README; hostile `R146_002`, repairs, confirmation, lead
`R146_005`. Scripts only for the cosh test on `c_{m,n}` (`--fast`, margin).

## Warnings
* Any positivity statement about the degree form is RH (W-a): if one appears "proved", stop, run `Ξ_a`, flag.
* The frame's Pólya realization `τ_{log n}(2K)` has `Z = 0` (R140): use Paper 44's smeared Frobenius Gram
  for all pairings involving zero data.
* Do not redo `Δ·Δ = −∞` (cite); do not reopen Laguerre–Pólya/finite-genus approximation (no-go).
