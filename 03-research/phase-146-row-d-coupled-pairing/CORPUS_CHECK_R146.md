# CORPUS_CHECK_R146 — prior art audit before building option α (a new coupled pairing J ≠ I_∞)

*Purpose: before phase 146 attempts to build a bilinear pairing `J` on `D^W`, different from `I_∞`,
satisfying `J(F,F) ≥ I_∞(F,F)` on primitive classes and `J(F,F) ≤ 0` provable there (⇒ `I_∞ ≤ 0` on
primitives ⇒ RH), built from `Frob_m ⋆ Frob_n = Frob_{mn}` and a prime/archimedean coupling — locate every
earlier attempt of this shape and its outcome. Classification: `NEW`, `TRIED–PROVED`, `TRIED–REFUTED`,
`TRIED–NO-GO`, `TRIED–PARTIAL`.*

---

## 1. Auxiliary/modified/dominating/comparison forms (`W_S`, `J(F,F)`, "second form", cross term)

**Status: TRIED–PARTIAL.** This is option α's own genesis, and the corpus already ran one full round on
exactly the object phase 146 is being asked to build.

* **Phase 137, D.12/S2** is the one attempt in the corpus at a semilocal coupled form:
  > `03-research/phase-137-row-d-canonical-coupling/R137_000_BLUEPRINT.md:14`: *"Define for finite
  > `S ⊇ {∞}` and real `F ∈ D^W`: `W_S(F) := Σ_{v∈S} ⟨F⋆F^∨, W_v⟩ − 2Φ_F(0)Φ_F(1)`... (iii) the first `S`
  > and `T` where positivity is not provable by these means, and what exactly is unpaid (**the cross term
  > prime×archimedean**)."*

  Outcome, `03-research/phase-137-row-d-canonical-coupling/R137_001_ROUND1.md:479-481` (quoted):
  the archimedean-only piece is positive up to `T ≤ log 2` (Connes–Consani 2006.13771 / phase-118's own
  bound), and beyond `S={∞,2}` "what is unpaid is the **cross term prime × archimedean**: `2(\log2)2^{−1/2}
  (F⋆F^∨)(\log 2)`... **archimedean Sonin space, with no term available to absorb a prime contribution of
  either sign.**" — no proof, no refutation delivered; the phase closes on a different sub-question
  (`h⁰_Z(mK)` growth) without resolving the cross-term sign.

* **The exact sign that must be targeted was corrected after phase 137**, in
  `05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-SYNTHESIS-PHASES-135-144.md` §3(α):
  > *"the alternative is a different pairing `J` on the same carrier with `J ≥ I_∞` on `P^W` and `J ≤ 0`
  > provable there... Nothing in the corpus has attempted a pairing `I_∞^(coupled) := I_∞^prime +
  > I_∞^arch` with a cross term built from `Frob_n ⋆ Frob_n^† = Δ^(n)` — this is the one untried square
  > adjacent to what is proved."*
  This is a load-bearing correction: an unqualified "dominating positive form" is useless (per
  `R144_004_CONFIRMATION.md:93-98`); the object needed is a **dominating non-positive** form,
  i.e. `J` must be *larger* than `I_∞` on primitives while itself provably `≤ 0` there. Phase 146 must
  state the inequality in exactly this direction, not the naively "obvious" one.

* **Phase 141** records the Frobenius Gram `C_mn` (Paper 44 Thm 8bis.1/8bis.4a) as the raw material for
  the cross term but never assembles it into a pairing with a proved sign — see §2 below.

* An unrelated earlier "coupled pairing" (different carrier, row A/Cauchy projection, not to be conflated):
  `03-research/phase-73-cauchy-projection/E73_279_COUPLED_APR_QUOTIENT_AUDIT.md:111,161` — *"The next
  theorem cannot be a quotient theorem. It must be a coupled pairing..."*; left **open**, unrelated to
  `I_∞`/`D^W`.

**Recommendation:** reuse (i) `W_S` as the concrete starting definition, (ii) the sign-corrected target
`J ≥ I_∞`, `J ≤ 0` provable, (iii) the precise location of the gap: the term
`2(\log 2) 2^{-1/2} (F⋆F^\vee)(\log 2)` at `S = \{\infty, 2\}, T > \log 2` is exactly where any new `J`
must supply something `W_S` could not. **Do not re-run phase 137's search from scratch** — extend past
its stopping point.

---

## 2. Rankin–Selberg / Frobenius-squares Gram; positive/negative form from `Frob_n ⋆ Frob_n^† = Δ^(n)`

**Status: TRIED–PARTIAL (raw material identified and proved unsigned at every finite chart; never
assembled into a global pairing).**

* **Paper 44, Thm 8bis.1 / 8bis.1b / 8bis.4a** (`04-papers/44-row-b-arithmetic-family/`, see
  `TEX_CONVERSION_NOTES.md:103-113`, `TEX_HOSTILE_REVIEW_R1.md:542-554`): defines the Frobenius Gram
  `C_{mn}` (off-diagonal Thm 8bis.1, diagonal Thm 8bis.1b) and Thm 8bis.4a — the theorem that this Gram is
  positive **only in a restricted, finite-chart sense**; the corpus's standing warning (carried into
  phase 141) is *"the pure Frobenius form is unsigned at every finite chart; colimit version OPEN"*
  (`03-research/phase-141-row-d-frobenius-traces/R141_000_BLUEPRINT.md:8-9`).

* **Phase 141 (`h⁰` reading Frobenius traces)** built exactly the candidate `Q_{C^{Frob}}` using this Gram
  as `C`:
  `03-research/phase-141-row-d-frobenius-traces/R141_000_BLUEPRINT.md:67`: *"The interaction with
  8bis.4a: `C_{mn} = ` Paper 44's Frobenius Gram entries is the arithmetically natural choice."*
  Outcome, `R141_001_ROUND1.md` tail table: `D.27.7 (C^Frob)` — **NAMED CHOICE** (diagonal set,
  not regularized); entries **PROVED-IN-REPOSITORY** (cites Paper 44 8bis.1/K1/Cor 8bis.1d); `D.27.8` —
  **PROVED**: *"auditor verified `γ_C > 0`, zero-trace indefiniteness, the trace-level unsignedness"* —
  i.e. `Q_{C^{Frob}}` is **proved indefinite at trace level**, not sign-definite. The FATAL screen was
  narrowed across rounds to: *"nothing with a sign is proved [for case (A), which includes `C^{Frob}`];
  for `C` in case (A) the status of (c) is not decided"* (`R141_003/004`). Phase 141 closed instead on an
  unrelated construction `h⁰_{RR}^+` (§D.30) reducing all of row D to the single open clause `(b′)⁺`.

* **"Gram of Frobenius as a form" / positive-definite kernel on the idele class group / Bochner /
  reproducing kernel** — searched broadly; the corpus's positive-definite-kernel constructions on
  ζ-related objects are consistently found to be the **wrong type** for carrying the Weil sign:
  - `03-research/phase-16-surf-witness-variety/04-MSZ-pairing-hits-CAP.md:37-70`: the natural resonance pairing on zeros is
    Bochner-**positive** (definite), *not* the indefinite Weil form `Q`; *"A definite Bochner form
    **cannot** carry `κ`"* (the off-line count) — a proved type-mismatch obstruction, generalizable: any
    literally positive-definite kernel built on this data cannot equal an indefinite form with the sign
    information RH needs.
  - `03-research/phase-136-row-d-map/MAP_4_PHASES_111_135_AND_PAPERS.md:26`: Paper 46 §6's `h⁰` candidates
    include `h⁰_spec`, and Remark 6.9's `h(g) = ‖π(g)Ω‖²` (a literal Bochner/GNS construction) is flagged
    *"the right type/wrong construction — never built from correspondence theory rather than from the
    conclusion."*

**Recommendation:** reuse `C_mn` (Paper 44 8bis.1/8bis.4a) as raw material exactly as phase 141 did, but
**do not re-derive its finite-chart unsignedness** — import it. The open task specific to phase 146 is the
one phase 141 explicitly did **not** attempt: turning `C^{Frob}` (or a repaired variant) into a *global*
`J` with the corrected sign target (`J ≥ I_∞`, `J ≤ 0`), not into a quadratic form `Q_C(t(E))` on Frobenius
traces alone (which is what phase 141 tried and left undecided). Any Bochner/reproducing-kernel route by
itself is flagged as the wrong type (phase 16).

---

## 3. Positivity via convolution squares / Fejér / SOS / Positivstellensatz / Hankel / Toeplitz

**Status: TRIED–NO-GO or TRIED–PARTIAL, in every located instance — no SOS/Positivstellensatz decomposition
of the Weil functional survives; several sharp local no-gos are on record.**

* `03-research/phase-104-unconditional-a1-closure/PHASE_104_CLOSURE.md:96`: closure list of routes tried
  and abandoned explicitly names *"positividad local, PSD, PF2/TP2, SOS o medidas completamente
  monótonas"* as exhausted for that sub-programme.
* `03-research/phase-104-unconditional-a1-closure/README.md:556` (`104_26`): *"ataque cuártico cerrado
  como no-go SOS. `J_u^{*4}` da una cuarta diferencia exacta, pero falla PF2 y los bloques completos
  cambian de signo."* — a concrete SOS-style quartic construction fails total positivity.
* `03-research/phase-103-direct-a1-closure/103_29_THETA_MLR_LOG_CONCAVITY_AND_SQUARE_NO_GO.md:105`: fails
  to give Toeplitz positivity of the relevant increment sequence (named no-go in the title).
* `03-research/phase-103-direct-a1-closure/README.md:87` (`103_64`): exact cell–lobe moment matrix
  computed; gives a **rational minimal obstruction** (`q=5, n=1`) to local PSD/total-positivity closure —
  i.e. Hankel/Toeplitz-style positivity is refuted at a concrete finite witness.
* `03-research/phase-102-omega7-closure-campaign/300_CENTERED_FEJER_TESTS_NOT_TOEPLITZ_NO_GO.md`: title
  states directly that centered Fejér tests do **not** imply Toeplitz positivity.
* `03-research/phase-102-omega7-closure-campaign/195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md:199,237`:
  *"Why global Toeplitz positivity is insufficient"*; *"Li positivity, increment Toeplitz positivity, nor
  Schoenberg positivity"* close the route.
* `03-research/phase-129-row-a-rebuild/R129_001_REPORT.md:193`: `§1` **refutes** by a two-point
  example that `(e−t)^†(e−t) = 2e−2t` is a sum of squares — a specific SOS identity shown false/misleading
  as evidence.
* Phase 36 (`03-research/phase-36-ABC-forms/105-coupling-first-test-of-form.md:249-251`): a Bochner-positive
  quantity `B_{λ₀}` is proved to have **sign changes for all sufficiently large N** despite Bochner
  positivity of the underlying measure — an explicit demonstration that Bochner/positive-definiteness of
  one representation does not transfer to pointwise or aggregate sign control needed for the Weil form.

**Recommendation: do not reopen** any SOS/Positivstellensatz/Hankel/Toeplitz route as a stand-alone
mechanism for `J`; every located instance in this corpus fails at either a concrete finite rational
witness or a proved insufficiency theorem. If phase 146 uses moment-matrix language for `C_mn`, treat it
only as bookkeeping for the raw Frobenius Gram (§2), not as a positivity mechanism in itself.

---

## 4. A different explicit formula (twisted/weighted/smoothed/Guinand/Bombieri/Yoshida/Li) as the route to Weil positivity

**Status: TRIED–PARTIAL / background only — no attempt in the corpus builds a *second* explicit formula
and compares it against the Weil form to extract a sign; existing material treats every explicit-formula
reformulation as *equivalent to* RH, not as independent leverage.**

* `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md` row A (quoted below, §6): *"each is
  RH restated; the explicit formula is a *bijection* between primes and zeros, so no side carries
  independent leverage (phase 34 Doc 90; phase 64 letter)"* — this covers Krein index, Pick passivity,
  Nevanlinna/Hermite–Biehler, Li kernels, Herglotz on `ξ'/ξ`, and by the same argument any twisted/weighted
  variant of the explicit formula (Guinand-type smoothing, Bombieri/Yoshida variants) inherits the same
  bijection obstruction: it is a restatement, and comparing two restatements does not manufacture new
  leverage unless one side is independently pinned down.
* Li-transform/Toeplitz-positivity material (`03-research/phase-102-omega7-closure-campaign/`,
  `161_LI_TOEPLITZ_MOMENT_GATE.md`, `192_ONE_SIDED_TAIL_FROM_GLOBAL_POSITIVITY_AUDIT.md`) is the corpus's
  most worked Li-criterion route; already covered under §3's Toeplitz no-gos.

**Recommendation:** treat as `TRIED–NO-GO` **at the level of the general strategy** ("compare two explicit
formulas to extract a sign") — cite the phase-136 bijection argument rather than re-deriving it; a genuinely
new such attempt would need to name what independent, non-bijective input it adds (the same standard the
programme applies to every candidate, per P122.028 below).

---

## 5. Deninger / Connes–Consani 2006.13771 mechanisms as a pairing; Sonin space; prolate operator as a candidate J

**Status: TRIED–NO-GO for direct transport as `J` (obstruction named); TRIED–PARTIAL for the underlying
machinery as raw material.**

* **Connes–Consani 2006.13771** (the actual source of the archimedean-only positivity already used in
  `W_S`) is fully catalogued in `03-research/phase-137-row-d-canonical-coupling/cc_2006.13771_text.txt`.
  Its quadratic form on the window is exactly what phase 118/137 already extract (`T ≤ log 2`); nothing
  further beyond `S={∞}` is available from this paper alone — the cross term is the corpus's own naming of
  what CC's mechanism does *not* reach (§1 above).

* **Deninger's geometric/foliated mechanism** (phase 43) is a **TRIED–NO-GO for transport**, for a
  reason directly relevant to any `J` built by analogy with a geometric intersection pairing:
  `03-research/phase-43-hodge-foliated-specZ/130-circularity-to-destruction-test-of-deninger-s.md:22,66,82`: the one realized
  case (elliptic curve over F_q) builds its Kähler/positive-definite metric **using Hasse's theorem
  (`|ξ|²=q`, the function-field RH) as input** — *"The RH follows from the index computation on this
  pre-constructed space, not from positivity alone."* Any `J` modeled on Deninger's construction would
  import this circularity unless the archimedean-place analogue can be built independently of an assumed
  RH-type input — no such independent construction exists in the corpus.

* **Connes–Consani–Moscovici, "Prolate Wave Operators" (2310.18423)** — catalogued at
  `03-research/phase-136-row-d-map/MAP_5_LITERATURE_VS_CORPUS.md:17`: semilocal prolate operator `W_λ`
  from `D² + grading` on `L²(X_S)^{K_S}`, with a positive part (↦ low-lying zeros) and a **Sonin-space**
  part (↦ UV behavior); *"No square/diagonal/Hodge-index language anywhere; unitary operators ... establish
  Jacobi normal form, not a positivity-via-unimodularity argument."* General-`S` asymptotics are
  **explicitly deferred by CCM themselves** ("a forthcoming paper"), and a second candidate operator
  (metaplectic Weil representation) is likewise left open by the source paper. The corpus's phase 137/138
  use of "Sonin space" is a direct citation of this same CCM vocabulary (`R137_001_ROUND1.md:481`;
  `R138_000_BLUEPRINT.md:76`), already folded into `W_S`'s stated gap — it is not a separate untried
  route, it is the source of the archimedean side already in hand.

**Recommendation: do not reopen** Deninger's construction as a template for `J` (circularity named); reuse
CC 2006.13771 and CCM 2310.18423 only as the already-imported archimedean ingredient inside `W_S`, and note
that CCM's own paper stops exactly where phase 146's cross term begins (general `S`, deferred by the source).

---

## 6. Phase-136 meta-theorem ("sign = coupling of polar block and Frobenius lattice") and concrete objects built after it (phases 137–145)

**Status: TRIED–PARTIAL — the meta-theorem is the direct ancestor of option α; every concrete coupled
object attempted since (137, 138, 141) either stalled unsigned or was redirected to a different clause.**

* The meta-theorem itself, `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:53`
  (quoted in full): *"**The sign is the interaction term between the polar/archimedean block and the
  Frobenius lattice, and it is a phase-coherence phenomenon of unimodular local roots.**"* Three
  independent formulations are noted as coinciding: phase 60's "phase not magnitude" theorem, Paper 46's
  Restatement 12.4a ("no model-free derivation; the datum is `Frob_n ⋆ Frob_n^† = Δ^{(n)}`" — the exact
  identity phase 146 is asked to use), and Connes–Consani's `Δ`-into-`Σ` mechanism. The consequence stated
  there: *"its definition must **couple** `K` to the Frobenius lattice through an object that (i) is not
  model-uniform, (ii) grows quadratically, and (iii) reads unimodularity. No object in the corpus does all
  three; several do two."* (same file, following paragraph). This is the exact admissibility triple any
  `J` must satisfy — see final section.

* **Concrete attempts after the meta-theorem:**
  - Phase 137's `W_S` (§1) — does (iii) partially (Sonin-space purity), fails (i)/(ii) beyond `S={∞,2}`.
  - Phase 138 (`R138_000_BLUEPRINT.md:76,91`) explores whether "translation" (the operation coupling
    the polar block and Sonin space) survives various transports, and whether `h = F⋆F^∨` factoring via
    Bochner is available — concluded **wrong type** again (no zero of `ξ` enters the construction it
    reaches; see `R138_001_ROUND1.md:654`).
  - Phase 141's `Q_{C^Frob}` (§2) — does (ii) (quadratic) and uses `C_mn` (reads unimodularity, partially),
    but is proved indefinite/unsigned at trace level ("(iii)" fails at finite chart) and is not
    model-uniform in the needed sense; abandoned in favor of `h⁰_{RR}^+` and clause `(b′)⁺`.
  - Phases 142–144 (row-D "the clause", "fixed index") redirect to the frame-defect/`h⁰` growth question
    (§2 of R145 above) rather than resuming the coupled-pairing search; phase 145 explicitly **defers**
    option α to phase 146 (`R145_000` and its `CORPUS_CHECK_R145.md` §6, quoted above).

**Recommendation:** phase 146 is the first phase actually chartered to resume the coupled-pairing search
past phase 141's stopping point. **Reuse** the meta-theorem's three-clause admissibility test verbatim as
the design spec for `J`; **do not** repeat phase 138's `h=F⋆F^∨`/Bochner factoring attempt (wrong type,
already shown) or phase 141's bare quadratic-in-traces ansatz (shown indefinite) without a materially new
ingredient satisfying all three of (i)–(iii) at once.

---

## 7. Explicit no-go: no bilinear form built from PRIME and ARCH terms alone can be sign-definite

**Status: TRIED–NO-GO, precisely stated, and directly on point for phase 146's admissibility.**

* **Phase 60, "phase not magnitude" (cited throughout the corpus, e.g.
  `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:22` row D):** *"any bound using only
  `‖Λ(n)‖` cannot decide the sign, because Davenport–Heilbronn has the same magnitudes and the opposite
  sign; the sign lives in the *phase coherence* of `cos(t log n)`; off-line zeros give secular growth
  `λ^{2β−1}` no average removes."* This is the corpus's standing theorem that **magnitude-only** data
  (`log p`, `p^{-1/2}`) cannot supply a sign — any `J` built solely from `|Frob_n|`-type magnitudes without
  phase information is automatically inadmissible.

* **P122.028 (Gate S, the two-prime finite Green complex) — the sharpest, most literal match to the
  requested no-go statement:**
  `03-research/phase-122-row-d-integrity-and-construction/P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md:168-186`
  (quoted): *"Future work on `S` is admissible only if it introduces an independent input that proves the
  missing middle arrow. Relations derived solely from `log p`, `p^{-1/2}`, `N` and `Γ` cannot be cited as
  such an input: those data already define both sides of the scalar explicit formula."* And earlier on the
  same page: *"Adding (4.2) as a positive summand to an asserted Green decomposition would prove the sign
  only if the remaining term were positive; P122.014 shows that constructing that positive comparison from
  Gram columns is equivalent to row (d)."* Recorded verdict (per
  `03-research/phase-136-row-d-map/MAP_4_PHASES_111_135_AND_PAPERS.md:22`): *"PROVED-IMPOSSIBLE for the
  cited relation classes; wall, not route... any input independent of `log p, p^{-1/2}, N, Γ` is explicitly
  named as the only admissible next move and untried."*

* **P3_COMMON_FAILURE_ARCHITECTURE, §2 (Theorem 2.1, "positive-lift theorem") and §8** —
  `03-research/phase-120-global-polarization/P3_COMMON_FAILURE_ARCHITECTURE.md`: the general theorem behind
  every attempted global positive/dominating object: *any* construction of the "manufacture a positive
  ambient object and let it descend" shape is covered and fails (§2); §8's admissibility checklist for a
  *different-in-kind* successor is reproduced in full in the final section below, since it applies
  verbatim to `J` if `J` is understood as another "positive-lift"-style object rather than the
  negative-witness route §8 recommends instead.

**Recommendation:** treat P122.028 as the operative, literal no-go: **any candidate `J` built purely as a
function of `log p, p^{-1/2}, N, Γ` (i.e. of the Frobenius family's magnitudes and the archimedean Gamma
data alone, with no further independent input) is already proved unable to supply the missing sign.** Phase
146 must identify what independent, non-magnitude, non-bijective ingredient `J` adds beyond
`Frob_m ⋆ Frob_n = Frob_{mn}` and the polar/Gamma data — otherwise it is asking P122.028's already-refuted
question again under a new name.

---

## Summary table

| # | Topic | Status | Key file(s) | Recommendation |
|---|---|---|---|---|
| 1 | `W_S` / auxiliary coupled form, cross term prime×arch | TRIED–PARTIAL | phase-137 `R137_000/001`; ROW-D-SYNTHESIS §3(α) | Reuse `W_S` + corrected sign target (`J≥I_∞`, `J≤0`); resume past `T>log2, S⊇{∞,2}` gap, don't restart |
| 2 | Frobenius Gram `C_mn` (Paper 44 8bis.1/8bis.4a) as pairing material | TRIED–PARTIAL | Paper 44 Thm 8bis.1/8bis.4a; phase-141 `R141_000/001` | Reuse `C_mn` as raw material; import "unsigned at every finite chart" fact; do not re-run phase 141's bare quadratic-trace ansatz (proved indefinite) |
| 3 | SOS / Positivstellensatz / Hankel / Toeplitz positivity mechanisms | TRIED–NO-GO (multiple concrete refutations) | phase-104 `PHASE_104_CLOSURE`, `104_26`; phase-103 `103_29`,`103_64`; phase-102 `300_CENTERED_FEJER...NO_GO`, `195` | Do not reopen as a stand-alone mechanism for `J` |
| 4 | Second explicit formula / twisted-weighted comparison for a sign | TRIED–NO-GO at strategy level | phase-136 `PHASE_136_MAP_SYNTHESIS_AND_PLAN.md` (row A, bijection argument) | Do not reopen unless a non-bijective independent input is named |
| 5 | Deninger / CC 2006.13771 / CCM prolate-Sonin as template for `J` | TRIED–NO-GO (Deninger, circularity) / TRIED–PARTIAL (CC, CCM — already imported) | phase-43 `130-circularity-to-destruction-test-of-deninger-s.md`; MAP_5 `:17`; CCM 2310.18423 catalog | Do not use Deninger's metric; CC/CCM already fully used inside `W_S`; general-`S` is where CCM itself stops |
| 6 | Phase-136 meta-theorem and post-136 coupled attempts | TRIED–PARTIAL | `PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:53`; phase-137/138/141 | Reuse (i)(ii)(iii) admissibility triple as `J`'s design spec; don't repeat 138's Bochner factoring or 141's bare quadratic ansatz |
| 7 | "No bilinear form from PRIME+ARCH alone can be sign-definite" | TRIED–NO-GO (proved for named relation classes) | P122_028 (Gate S) `:168-186`; phase-60 "phase not magnitude"; P3_COMMON_FAILURE_ARCHITECTURE §2/§8 | `J` must add an independent, non-magnitude ingredient beyond `log p, p^{-1/2}, N, Γ`, or it re-asks a proved-impossible question |

---

## Constraints any new pairing `J` must satisfy according to the corpus

Combining the phase-136 meta-theorem's three-clause test, P122.028's admissibility rule, and
P3_COMMON_FAILURE_ARCHITECTURE §8's checklist for a genuinely different successor:

1. **Not model-uniform.** `J` cannot be defined by a formula that transfers verbatim to `Ξ_a` or `Ξ_Q`
   (the falsifier classes used throughout rows C/D) — if it does, it is either already-known-false there
   (per Restatement 12.4a) or it proves too much. (Phase-136 clause (i).)
2. **Must grow quadratically** in the relevant degree/window parameter, matching the moment-cone /
   Riemann–Roch growth already established for `I_∞` and its candidates (`h⁰` family, phases 139–144).
   A merely linear or bounded `J` cannot dominate `I_∞` in the needed sense. (Phase-136 clause (ii).)
3. **Must read unimodularity** of the local Frobenius roots (`|α|=√p`) directly, not just their
   magnitudes — this is the corpus's diagnosis of what Connes–Consani's `Δ→Σ` move and the two/`n`-primes
   purity theorems (phase 44 Doc 131, phase 45 Doc 135) actually use, and what the phase-60 "phase not
   magnitude" theorem says is indispensable. (Phase-136 clause (iii).)
4. **Independent input beyond `log p`, `p^{-1/2}`, `N`, `Γ`.** Per P122.028: any construction expressible
   purely in these four data (which is what `Frob_m⋆Frob_n=Frob_{mn}` and the polar/Gamma data reduce to)
   already defines both sides of the scalar explicit formula and is proved unable to supply the missing
   sign. `J` must be built from, or supply, something outside this list — e.g. a genuinely new coupling
   object with independent provenance, not a rearrangement of known quantities.
5. **Correct inequality direction.** `J ≥ I_∞` on primitives with `J ≤ 0` provable there — *not* "`J` is a
   dominating positive form" (shown useless by `R144_004`). Any write-up must state and re-check this sign
   at every stage; getting it backwards silently reproduces a known-dead architecture.
6. **Must not be a positive-lift / manufactured-ambient-object construction covered by
   P3_COMMON_FAILURE_ARCHITECTURE Theorem 2.1.** If `J` is, in effect, "construct a positive object and let
   it descend to bound `I_∞`", it is already covered and fails; the corpus's own recommended alternative
   framing is the negative-witness route (§8: assume a mixed primitive `F` with `q_T(F)<0` and derive a
   forbidden object from exact Euler-specific rigidity — this reverses the quantifiers relative to a
   positive-lift `J` and has not itself been constructed, but is flagged as the structurally different
   target if `J` construction stalls the same way phases 137/141 did).
7. **Must not repeat a type-mismatch already proved fatal.** A literally Bochner/positive-definite kernel
   construction (GNS-style `h(g)=‖π(g)Ω‖²`, or the MSZ resonance-pairing route) is proved to be the *wrong
   type* to carry an indefinite Weil-form sign (phase 16); avoid building `J` as a positive-definite kernel
   outright.
8. **Falsifier discipline.** Whatever `J` is, it must be checked against `Ξ_a` (must fail there, since
   `Ξ_a` is a known non-RH object — D.30.16) and against Davenport–Heilbronn-type magnitude-matched but
   phase-differing data (phase 60), before being trusted on the genuine object.

**Overall assessment for phase 146:** option α is `NEW` only in the sense that no attempt has carried
`W_S` or `Q_{C^Frob}` past their respective stopping points into a single object satisfying all of
constraints 1–4 simultaneously; both prior attempts satisfy at most two of the three phase-136 clauses.
The corpus does **not** contain a proof that this is impossible in general (P122.028 only rules out the
*named magnitude-only relation classes*) — so building `J` is not pre-empted, but it must visibly clear
the checklist above, and should explicitly state which of phases 137/138/141's near-misses it is extending
and why the new ingredient escapes P122.028's rule.
