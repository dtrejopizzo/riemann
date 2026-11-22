# R139.000 — Blueprint, phase 139: the two falsifiers and the method theorem

`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-COMPLETION-PLAN.md` §1 (phase 139). Corpus check of
reference: `05-meta-and-planning/ABCD-CLOSURE-PLAN/CORPUS_CHECK_ROW_D_PLAN.md` (read it first; reuse
what it marks as proved; do not reopen what it marks no-go; a "Corpus check" section per idea is
mandatory in the report).*

Standing rules: pure mathematics; every arrow labelled (PROVED / PROVED-IN-REPOSITORY / CLASSICAL /
RESTATEMENT / IMPORTED / CANDIDATE / HEURISTIC / REFUTED / NOT-APPLICABLE / OPEN); nothing defined
through zero locations (`ξ`, `ξ_K`, `Λ_Q` admissible as data); numerics only to certify a constant with
a stated margin; FATAL rule (a statement that with Paper 47 Thm 3.7 proves RH or ¬RH: flag, do not fix).
Three falsifier tests from now on: `Ξ_a` (non-equimodular polar block), Epstein `Z_Q` (no Euler
product), and the `ζ_K` non-distinction test (any argument that distinguishes `Q` from a number field
`K` must name the distinguishing property; otherwise it is suspect).

## Setting (RESTATEMENT of record)
Paper 47 §§11–12 (Weil class `D^W`, `I_∞`, canonical class `K`, `Φ_K = ξ`, Theorem 12.3 transfer, §12.5
admissible `Z` with polar set `P` and canonical class `K_Z`, Prop. 12.6); phase 138 `R138_001` D.15
(splitting `D^W = Λ ⊥ P^W`, Lorentzian criterion, Theorem D.15.4b equimodularity: the translation cone
`Λ_Z^+` satisfies Hodge index iff `|p−½|` is constant on `P`), D.17 (detecting cones `E`, `C_c^∞`;
Landau criterion); `R138_005` (answer to Q; the open quadrant is clause (iii) on `E`).

## D.19 — The Epstein falsifier in row D's frame (NEW; target: the method theorem T2)

1. **Data (CLASSICAL, cite precisely).** `Q(x,y) = ax² + bxy + cy²` positive definite, discriminant
   `−D = b² − 4ac < 0`, class number `h(−D) > 1`. Epstein zeta `Z_Q(s) = ½ Σ'_{(m,n)} Q(m,n)^{−s}`
   `= Σ_{n≥1} r_Q(n) n^{−s}`, `r_Q(n) ≥ 0`. Completed `Λ_Q(s) := (√D/(2π))^s Γ(s) Z_Q(s)`, entire except
   simple poles at `s = 1` and `s = 0`, `Λ_Q(s) = Λ_Q(1−s)`. `Z_Q = (w/…)·Σ_χ \overline{χ}(𝔄) L(s,χ)` over
   class-group characters (Hecke). Davenport–Heilbronn (1936): for `h(−D) > 1` (and `Z_Q` not a multiple
   of a single `L(s,χ)`), `Z_Q` has infinitely many zeros with `Re s > 1` and zeros off `Re s = ½` in the
   strip; Voronin: infinitely many in `½ < Re s < 1`. State exactly what is cited and from where
   (Davenport–Heilbronn, J. London Math. Soc. 11 (1936); Voronin 1976; Bombieri–Hejhal for the
   distribution). Check which polar/zero facts are needed and cite only those.
2. **The canonical class.** `K_Q(t)` := the theta-type kernel with `Φ_{K_Q} = Λ_Q` (Mellin/Laplace
   inversion of `Λ_Q` along `Re s = ½`; the analogue of the Pólya kernel through
   `θ_Q(x) = Σ_{(m,n)} e^{−πQ(m,n)x/…}`). Prove: `K_Q ∈ D^W`-type class (decay), `K_Q > 0` (from the theta
   series, as for `K`: Paper 47 §11.7), `deg K_Q = Λ_Q(0)+Λ_Q(1)` (compute the residues), polar set
   `P = {0,1}` — **equimodular**. Note the residue at `s = 1` of `Z_Q` is `π/√D` (independent of the
   class!), so `Λ_Q` residues are explicit.
3. **The Weil class and the form.** Define `I_∞^{(Q)}(F,G)` by Paper 47's recipe with zero sum over
   `Z(Λ_Q)` and polar block from `P` (Prop. 12.6 hypotheses: check which hold — in particular the
   admissibility clause requiring `Λ_Q > 0` on `R`, which follows from `K_Q > 0`; and the explicit
   formula for `Z_Q`, which is the sum of the Hecke explicit formulas — RESTATEMENT). Prove the
   splitting `D^W = Λ_Q ⊥ P^W_Q` and that `K_Q` is the Lorentzian normalization.
4. **Hodge index fails.** Since `Z_Q` has off-line zeros, by the Landau argument (Theorem D.17.2 run for
   `Λ_Q`: `G_Q(z) = 2z^{−2}(Λ_Q'/Λ_Q)(½+z)`, real singularities only at `z = 0` iff `Λ_Q` has no real
   zeros in `(0,1)` — **check this**: `Z_Q(σ)` for real `σ ∈ (0,1)` can vanish? For `Z_Q` with `h > 1`
   the real zeros question must be settled or the argument adapted: Landau needs only that the abscissa
   of convergence be a real singularity; if `Λ_Q` has a real zero `σ_0 ∈ (½,1)` that is itself a pole of
   `G_Q` on the real axis and the argument must be rerun — do it carefully) there is `T` with
   `W_Q(h_T) < 0`, i.e. an effective `F_T^{(δ)}` violating Hodge index. Exhibit the mechanism.
5. **T2 — the method theorem.** Statement: *Let `𝔖` be the class of inequalities between `I_∞^{(Z)}`-
   quantities whose proof uses only: the polar block with equimodular `P`, positivity of `K_Z`, the
   functional equation, positivity of the Dirichlet coefficients, and the degree. Then any such inequality
   valid for `ξ` is valid for `Λ_Q`; since Hodge index fails for `Λ_Q`, no `𝔖`-proof of Hodge index for
   `ξ` exists.* Make `𝔖` precise enough to be a theorem (a list of axioms satisfied by both data sets and
   a transfer lemma), or state it as a METHOD-CONSTRAINT with the exact axiom list if a clean theorem is
   out of reach — and say which. Companion (from R137_007 §2.2): the `ζ_K` non-distinction: the same
   axioms plus **Euler product with unimodular local roots** are satisfied by every `ξ_K`; so any proof
   must be uniform in `K`.
6. **What the Euler product adds, concretely.** `ζ_{Q(√−D)}(s) = ζ(s)L(s,χ_{−D})` is a product; `Z_Q` is a
   *sum* `Σ_χ \overline{χ}(𝔄)L(s,χ)` of Hecke L-functions (for `h > 1` a genuine sum of ≥ 2 terms). Identify
   the row-B structure that exists for `ζ_K` and not for `Z_Q`: multiplicativity of the coefficients
   (`Frob_n`'s inverse-semigroup law `Frob_m ⋆ Frob_n = Frob_{mn}` for coprime `m,n`; Paper 44) — for
   `r_Q(n)` multiplicativity fails exactly because of the class group. Formulate: "the sign proof must use
   the multiplicativity of the Frobenius family" as the precise content of T2.

## D.20 — Field-uniform frame and base change (RESTATEMENT + new relations)

1. For a number field `K` with places `S ⊇ S_∞`: carrier `C_{K,S}`, Weil class, `K_K` with
   `Φ_{K_K} = ξ_K` (completed Dedekind zeta, polar set `{0,1}`, equimodular), `I_∞^{(K)}`, splitting,
   Lorentzian normalization, transfer theorem. Prove the frame transfers verbatim (RESTATEMENT) and list
   any place where the number of archimedean places or the units enter (the archimedean block is now a sum
   over real and complex places: `Ŵ_∞` changes; the regulator enters the residue).
2. Base change `L/K`: `ξ_L = ξ_K · Π_{χ ≠ 1} Λ(s,χ)^{…}` (Artin formalism, Aramata–Brauer: `ζ_L/ζ_K`
   entire). For `F` a `K`-class pulled back along the norm `C_L → C_K`, prove
   `I_∞^{(L)}(N^*F, N^*F) = I_∞^{(K)}(F,F) + Σ_χ I_∞^{(χ)}(F,F)` (RESTATEMENT of the Artin formalism at
   the level of forms). New: the polar block of `L` restricted to `K`-classes equals the polar block of
   `K` (only `ζ_K` has the pole), so **all** the extra terms are primitive (in `P^W`) — the Artin
   factors contribute only to the zero form. State what this says about Hodge index in towers
   (monotone? additive?).
3. Where Epstein sits: `Z_Q` is a `K = Q(√−D)`-object built from class-group characters; the base change
   `K/Q` sees `ζ_K = ζ · L(χ_{−D})` (product), while `Z_Q` is the sum. Make D.19.6 precise here.

## D.21 — Weil's function-field proof, transcribed step by step (ledger)

Use Paper 42's arithmetic-Lefschetz ledger if the corpus check finds it (item 3); otherwise write it.
For each step of Weil's second proof (Riemann–Roch on `C×C`; Castelnuovo–Severi inequality
`(D·D) ≤ 2 d_1 d_2` for `D` with `D·(fibres) = d_1, d_2`; Hodge index on `C×C`; the graph `Γ_q` of
Frobenius, `Γ_q·Γ_q = q(2−2g)`, `Γ_q·Δ = N_1`, bidegree `(1,q)`; the trace inequality `σ(Γ∘Γ') ≥ 0`;
conclusion `|N_1 − q − 1| ≤ 2g√q`) give: the arithmetic analogue in rows A–C with its label
(PRESENT: `K`, degree, bidegrees `(n^{1/2}, n^{−1/2})`, `Sh_Z(Frob_n) = [L_S → n → L_S]`, `Δ·Δ = −∞`,
Gram forms; PRESENT-CONDITIONAL: Thm 12.3 given `h⁰`; ABSENT: `h⁰`/RR on the square, Castelnuovo). Mark
which step is the **Euler-product step** (the Frobenius correspondence and its composition law) and
which the **field-uniform step** (RR holds for every curve). Deliverable: the construction problem
`(P139)` — the missing object, with acceptance tests: fails for Epstein (uses multiplicativity), fails for
`Ξ_a` (uses equimodularity), does not distinguish `Q` from `K`.

## Deliverables and rounds
`R139_001_ROUND1.md` (D.19 complete with T2; D.20 items 1–2; D.21 ledger and `(P139)`), README,
then `R139_002_AUDIT.md`, repairs, confirmation, closing decision `R139_005`. Scripts only to certify
a constant (e.g. a real zero of `Z_Q` in `(0,1)` if needed for D.19.4 — do it exactly, or prove absence).

## Warnings
* D.19.4 has a genuine subtlety (possible real zeros of `Z_Q`); do not wave it.
* Do not claim T2 as a theorem unless `𝔖` is defined; a METHOD-CONSTRAINT with an explicit axiom list is
  the honest fallback and is still the deliverable.
* Do not reopen anything the corpus check marks as no-go; cite PROVED-IN-REPOSITORY with paths.

## Corpus consequences (binding; from `CORPUS_CHECK_ROW_D_PLAN.md`)
* **Epstein** was classified (phase 8 PLAN lines 21–24; phase 58 doc 192 line 87; R137_006 lines 141–142) as
  positive-coefficient / no-Euler-product / off-line zeros, distinct from the signed Davenport–Heilbronn
  combination. Cite that classification as PROVED-IN-REPOSITORY; build only the canonical class `K_Q`,
  the polar block, the form and the failure witness (D.19.2–4), which do not exist.
* **Dedekind falsifier search**: closed (would need GRH); the *field-uniform frame* (D.20) is new — build.
* **Weil's proof pillars** were named ≥ 3 times (phase 33 docs 74, 80 "Castelnuovo–Severi aritmético";
  phase 107 doc 241; Paper 42 main.tex lines 105, 130, 165; phase 39 docs 119–120). Do NOT re-derive the
  naming; D.21 must be the **consolidated line-by-line ledger** with labels and the `(P139)` statement,
  citing those files.
* **Reuse**: phase-15-arithmetic-hodge-index `M1-arithmetic-intersection-pairing.md` Thm B (`Γ·Γ ≥ 0`, verified); Paper 44's
  local purity theorems (Thm 6.7 single prime; Thms A/A′/B for two/n primes) as the proved local side of
  item 6; phase-41 Doc 125 tropical toy as the one literal sign-definite Hodge-index instance — for D.21
  mark what the toy has that the arithmetic square lacks.
* **Do not reopen**: Bost–Connes / KMS positivity (Thm 161.9 in `AUDIT_A_CATEGORY_CHANGES.md`; phases 6,
  8, 51/52 all converge on `Z(β) = ζ(β)`).
* The phase-136 synthesis names item 8 (Hodge index on the square, the `¼m²` diagnosis) as *the* single
  remaining difficulty of the whole programme; `(P139)` must be stated so that it is visibly that object.
