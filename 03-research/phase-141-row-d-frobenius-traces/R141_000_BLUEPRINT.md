# R141.000 — Blueprint, phase 141: an `h⁰` that reads the Frobenius traces

(phase 141, re-targeted by `R140_005`). Inputs of record: `R139_005` ((P139), tests AT-1..3, axioms A1–A9,
T2); `R140_005` (complementary failure of `h⁰_Z` and `h⁰_□`; Cor. D.24.12: an admissible `h⁰` must read
`Z(E)` through pairings `I_∞(E,X)` with `Z(X) ≠ 0`; the three Gram forms (A)/(B)/(C); residues R2, R8,
R11). Corpus: `CORPUS_CHECK_ROW_D_PLAN.md` items 6–8; round-1 memo must grep in addition for "Frobenius
trace", "trace of Frobenius", "Gram of translates", "quadratic form in the prime sums", "Rankin–Selberg
Gram", "moment problem" before writing D.26–D.28 and record the outcome per idea.*

Standing rules as in R139_000/R140_000. Three falsifiers (`Ξ_a`, `Ξ_Q`, `ζ_K` non-distinction); T2's
naming clause (N) carried as audit protocol; the 8bis.4a warning (the pure Frobenius form is unsigned at
every finite chart; colimit version OPEN) must accompany every use of family (A).

## The object (R11 made well-posed)

Fix a real even `g ∈ C_c^∞(R)`, `g ≥ 0`, `g ≢ 0` (so `Z(g) ≠ 0` generically — prove: `Φ_g` has a zero of
`ξ` as a zero only for `g` in a proper closed subset; choose `g` outside it, or simply require
`Φ_g(ρ) ≠ 0` for all `ρ` and show such `g` exist). Define the **Frobenius traces** of `E ∈ D^W`:

    t_n(E) := I_∞(E, τ_{log n} g)   (n ≥ 1),      t_0(E) := (deg⁻E, deg⁺E).

By Paper 46 Def. 11.4 / Lemma 11.4a each `t_n(E)` is `PRIME − ARCH` of `E ⋆ (τ_{log n}g)^∨` — an
arithmetic quantity naming no zero — and by the explicit formula
`t_n(E) = [polar] − Σ_ρ Φ_E(ρ)Φ_g(1−ρ) n^{½−ρ}`. (Variant to compare: `X_n := Frob_n^{sm}` of Paper 44
mapped into `D^W` through the radial profile — decide which family is used and why; the smeared Frobenius
family carries A8 directly through the weights `Λ(q^k)q^{−k/2}`; the translate family carries A8 through
the prime sum inside `PRIME`.)

**O-14′ (well-posed).** Find `Ψ` such that `h⁰(E) := Ψ(t_0(E), (t_n(E))_{n≥1})` satisfies (a), (b′), (c)
of Theorem 12.3 for every `ξ_K` (with `g`, `τ`, `I_∞` read over `K`), and name the lines using A3 and A8.

## D.26 — What the traces determine (RESTATEMENT + new)
1. Prove: `(t_0(E), (t_n(E))_n)` determines `E` modulo `𝓝_∞` (Paper 46 Thm 11.11 gives `(M(E), Z(E))`;
   the exponentials `n ↦ n^{½−ρ}` separate the zeros — give the argument: a finite or convergent linear
   combination `Σ_ρ a_ρ n^{½−ρ} = 0` for all `n ≥ 1` forces `a_ρ = 0`, by uniqueness for general Dirichlet
   series / Bohr almost-periodicity in `log n`). So `h⁰` may legitimately be a function of the traces.
2. The **moment cone** (O-15, as a tool): `𝔐 := {(t_0(E), (t_n(E))_n) : E ∈ D^W, E ≥ 0}`. (b′) for
   `h⁰ = Ψ(t)` reads: `Ψ(t) > 0 ⟹ t ∈ 𝔐 + (traces of 𝓝_∞)` — but traces of `𝓝_∞` vanish (`Z = 0`,
   `M = 0`), so (b′) is `Ψ(t) > 0 ⟹ t ∈ 𝔐`, and (b′) with `E' ≢ 0` needs `t ≠ 0`. State (b′) exactly as
   a statement about `𝔐`. Describe `𝔐` as far as possible **without zeros**: necessary conditions on
   `(t_n)` for `E ≥ 0` (e.g. from `|Φ_E(ρ)| ≤ (deg⁻E)^{β}(deg⁺E)^{1−β}`, R140 D.24; from positivity of
   `E ⋆ (τ g)^∨` when `g ≥ 0` — is `t_n(E) = PRIME − ARCH` of a nonnegative function; what sign
   information does that give?).
3. Falsifier check: the same definitions for `Ξ_a`, `Ξ_Q`, `ξ_K`. Where does A3 enter `𝔐`? Where A8?

## D.27 — The quadratic candidate (new)
Growth forces `Ψ` to be (asymptotically) 2-homogeneous on the ray `mK`: `t_n(mK) = m·t_n(K)` and
`t_n(K) = ½(n^{½}+n^{−½})·(…)` (compute: `Z(K) = 0`, so `t_n(K)` is pure polar). Hence any `Ψ` with the
(c)-growth `¼m²` must be quadratic in `m` along that ray. Test the natural class:

    h⁰_C(E) := max( Σ_{m,n≥0} C_{mn} t_m(E) t_n(E), 0 )   (or a positive-part of a quadratic form),

with `C` a symmetric kernel on `N_0 × N_0` to be chosen — a **quadratic form in the Frobenius traces**.
1. (a) trivial. (c) at general `E`: write it out — it compares the quadratic form `Q_C(t(E)) + Q_C(t(K−E))`
   with `½I_∞(E,E) − ½I_∞(E,K) + χ`, where `I_∞(E,E) = 2deg⁻deg⁺ − W(E)`; both sides are quadratic in `E`;
   (c) is an inequality between two quadratic forms on `D^W`, i.e. a **choice of `C` making
   `Q_C ∘ t + Q_C ∘ t ∘ σ_K − ½I_∞ + ½I_∞(·,K) − χ ≥ 0`**. Determine whether some `C` achieves this
   unconditionally (that would be a theorem with sign — check FATAL rule: with (b′) it would prove RH,
   so expect either (b′) to fail for every such `C`, or the inequality to be RH; find which).
2. (b′): `Q_C(t(E)) > 0 ⟹ t(E) ∈ 𝔐`. For `C` positive semidefinite this says the cone `{Q_C > 0}` lies
   inside the moment cone — a **containment of cones defined without zeros** (this is where the new
   mathematics would live). Decide: does any nonzero PSD `C` satisfy it? If (b′) fails for every `C`,
   exhibit the witness in the manner of R140 Thm D.24.7 (an `E` with `Q_C(t(E)) > 0` not equivalent to a
   nonnegative class — note `E ↦ t(E)` is linear and `𝓝_∞`-invariant, so the witness must have
   `t(E) ∉ 𝔐` while `Q_C(t(E)) > 0`).
3. The interaction with 8bis.4a: `C_{mn} = ` Paper 44's Frobenius Gram entries is the arithmetically
   natural choice; its form is unsigned at finite charts. Compute what `Q_C` is for that `C` on
   `E = mK + λ` and on primitive `E`.

## D.28 — O-17 (primitive bridge for `Ξ_Q`; R8)
Transpose Paper 46 Prop. 12.4B to `Z = Ξ_Q` with `P = {0,1}`: from R139's effective non-primitive witness
produce a `Ξ_Q`-primitive `C_c^∞` test with `Ŵ^{(Ξ_Q)} > 0`; use a non-real Davenport–Heilbronn zero
(`γ_0 ≠ 0`) and widen the strip as R8 says. If it closes, (AT-1)(ii) returns to a refutation.

## D.29 — Synthesis input
One page: is there any `Ψ` (quadratic or not) for which (b′) is a zero-free cone containment and (c) an
unconditional inequality — or does the pair force one of them to be RH? State which clause, with the
witness or the reduction, and where A8 is used. Recommendation for phase 142 (assembly or obstruction
theorem).

## Deliverables and rounds
`R141_001_ROUND1.md` (D.26 complete; D.27 items 1–3 with the exact inequality and the (b′) decision;
D.28; D.29), README; audit `R141_002`, repairs `R141_003`, confirmation `R141_004`, closing decision `R141_005`.
Scripts only to certify a constant.

## Warnings
* Do not define anything through zeros; `t_n` is defined by the arithmetic side.
* If (c) closes unconditionally for some `C`, STOP and flag (FATAL rule) — check (b′) first.
* Do not reuse the collapsed realization `r(Frob_n) = τ_{log n}(2K)` (R140: it has `Z = 0`).
* Every use of family (A) carries the 8bis.4a warning; the colimit version is OPEN (R3).
