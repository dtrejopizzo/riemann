# CORPUS_CHECK_R146b — prior art for the redefined α: "the degree form on Z[Frob] with a count
interpretation" (arithmetic analogue of the elliptic-curve proof of RH)

*Purpose: phase 146's α is being reframed around
`deg(m + nπ) = #ker(m + nπ) ≥ 0` for all integers `m,n`, a positive-definite quadratic form on
`End(E) ⊇ Z[π]`, with the infinite genus `Δ·Δ = −∞` (Paper 44 Thm 8bis.2) as the named obstruction to
transporting this argument to Spec Z. Supersedes / extends `CORPUS_CHECK_R146.md`, which covered the
"coupled pairing J" framing of α; this note covers the specific elliptic-curve-analogy framing.*

---

## 1. "End(J)"/"Z[π]"/"Z[Frob]" — additive structure on Frobenius as a ring

**Status: TRIED–PARTIAL.** The corpus has the Frobenius family `Frob_n` as a **multiplicative**
inverse semigroup, with Rankin–Selberg-type products (`Frob_m ⋆ Frob_n^† = Frob_{m/n}`), but no
prior construction treats `{Frob_n}` (or their smeared/measure-theoretic avatars) as generators of a
commutative ring under **addition**, i.e. no `Z[Frob]` or `Z[π]`-module structure is built anywhere.

* `04-papers/44-row-b-arithmetic-family/main.md:3250` ff. (Thm 8bis.1) constructs the *convolution*
  algebra (`I_A(Frob_m,Frob_n) = T(Frob_{m/n,...})`) — a semigroup/groupoid law, not an additive ring.
  No sum `m·1 + n·Frob` is ever declared a single object with its own norm/degree.
* Phase 136's meta-theorem (`03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:53`,
  quoted in `CORPUS_CHECK_R146.md` §6) already names the needed shape without building it: *"its
  definition must **couple** `K` to the Frobenius lattice through an object that (i) is not
  model-uniform, (ii) grows quadratically, and (iii) reads unimodularity. No object in the corpus does
  all three."* An additive `Z[Frob]`-degree form is exactly a candidate for "coupling K to the
  Frobenius lattice" that has never been tried in this additive form.
* Paper 46's Restatement 12.4a (cited in `CORPUS_CHECK_R146.md` §6) records the identity
  `Frob_n ⋆ Frob_n^† = Δ^{(n)}` — the multiplicative self-pairing — but never combines two different
  `n` **additively** before pairing (i.e. never forms `(m·Δ + n·Frob_k)` and pairs it with itself).

**Recommendation:** NEW as an additive/ring-theoretic construction; nothing to reuse beyond the raw
multiplicative Gram entries of Thm 8bis.1 (§4 below), which would become the off-diagonal terms of the
new quadratic form.

---

## 2. "Degree of a correspondence" as a count: `#ker`, Lefschetz numbers, `N_1 = q+1−a`, Hasse bound
via degree, elliptic-curve proof of RH, positive-definite quadratic form on End(E)

**Status: TRIED (as background/analogy) — NEW (as the object built for Spec Z).**

* The elliptic-curve/function-field analogy is a **recurring reference point**, always cited as the
  *model case* that the programme cannot yet transport, never as something disproved for Spec Z:
  - `03-research/phase-43-hodge-foliated-specZ/130-test-circularidad-deninger.md:22,66,82` (quoted in
    `CORPUS_CHECK_R146.md` §5): the elliptic-curve-over-`F_q` case "builds its Kähler/positive-definite
    metric **using Hasse's theorem (`|ξ|²=q`, the function-field RH) as input**... RH follows from the
    index computation on this pre-constructed space, not from positivity alone." This is a **TRIED–
    NO-GO for direct transport**: the finite-field model's positivity argument is circular *there*
    because it bakes Hasse's bound in; it is not a statement that the `#ker ≥ 0` shape itself fails —
    only that copying the *construction* imports Hasse as an unearned input.
  - `03-research/phase-107-arithmetic-lefschetz-reconstruction/107_00_REVERSE_ENGINEERING_ARITHMETIC_LEFSCHETZ_PROGRAM.md:222`:
    `correspondence ⟶ Lefschetz number` is exactly the "count of fixed points" reading of degree, but
    built as a **reconstruction target**, not proved; `107_133_CURRENT_ROW_C_CLOSURE_GATE.md:78-80`
    records it **PROVED-IMPOSSIBLE for the "row-c" legacy source grammar** — a real-curve counterexample
    kills that *specific* local-packet realization, not the abstract degree-form idea.
  - Lefschetz-number language recurs at `03-research/phase-125-row-a-completion/A125_006_FIXED_POINT_DICHOTOMY_AND_THE_MIXED_SECTOR.md:20`
    and `03-research/phase-15/M1-arithmetic-intersection-pairing.md:80` ("the (local) zero count, the
    arithmetic Lefschetz number") — always as the *intended* meaning of an arithmetic intersection
    number with the diagonal, never assembled into a positive-definite form on an additive Frobenius
    ring.
* No hit anywhere in the corpus for the literal phrases "positive definite quadratic form on End",
  "deg(m + nπ)", "elliptic curve proof of RH" as a named/labelled prior attempt at Spec Z (the phrase
  exists only in the general-knowledge background, e.g. via the Deninger discussion above).

**Recommendation:** the *analogy* (elliptic curve Frobenius degree form ⟹ Hasse bound) is well known in
the corpus **as the standard picture Spec Z fails to instantiate**, always cited for why Spec Z is
harder (no finite field, no abelian variety, infinite genus — see §3). Framing phase 146's α as "build
the literal analogue, `deg(m+nFrob)=#ker≥0`, for Z[Frob]" is **NEW**: it has not been attempted as a
construction, only invoked as the unreachable target case.

---

## 3. "Infinite genus", `Δ·Δ = −∞`, self-intersection of the diagonal — the named obstruction

**Status: TRIED–PROVED (as a standing, repeatedly re-derived negative result) — this is the corpus's
single most robust recurring finding, and directly the obstruction phase 146 must confront.**

* **Paper 44, Theorem 8bis.2** (`04-papers/44-row-b-arithmetic-family/main.md:3669`, "infinite genus";
  full derivation §8bis, `main.md:3250-3669`) is the canonical statement: the Gram/self-intersection
  quantity diverges — `Delta . Delta = -infinity (infinite genus), AT A FIXED CHART` (also recorded
  verbatim at `04-papers/44-row-b-arithmetic-family/main.md:72,330`, and rebuilt across
  `03-research/phase-131-row-b-closure/R131_007_BUILDER_ROUND3.md:65,71`,
  `R131_014_AUDIT_ROUND5.md:157`, `R131_017_AUDIT_ROUND6.md:66`, `R131_018_BUILDER_ROUND7.md:64`).
* Earlier independent derivations of the same fact, predating Paper 44:
  - `03-research/phase-10/M10.1-verdict-degenerate-hodge.md:31`: "candidate 'arithmetic surface' has
    **infinite genus with a vanishing Hodge gap**: the primitive intersection..." — the finite-rank
    Hodge argument (which is exactly what powers the elliptic-curve `#ker ≥ 0` proof) **does not
    transfer** (`03-research/phase-10/experiments/M10_1_hodge_envelope.py:16,44,58`).
  - `03-research/phase-63-lefschetz-realization/E99_RESULTS.md:38,52`: "gaplessness is the analytic
    shadow of Spec Z having 'infinite genus'... because it has infinitely many, accumulating zeros...
    The crossing requires an candidly infinite-dimensional [argument]."
  - `03-research/phase-106-global-modular-star-audit/106_162_PRINCIPAL_DIVISOR_SYMPLECTIC_REDUCTION_NO_GO.md:142`:
    "infinite genus carried by the zeta resonances" — filed as a **NO-GO** for a symplectic-reduction
    construction.
* Independent literature confirmation, catalogued at
  `03-research/phase-136-row-d-map/MAP_5_LITERATURE_VS_CORPUS.md:13`: Connes–Consani state *"the
  arithmetic curve has infinite genus (g=∞) … the target space is not an abelian variety but an
  idempotent semilattice"* — i.e. even the literature's own source for the analogy confirms `End`
  is not the endomorphism ring of an abelian variety, which is precisely why the elliptic-curve
  argument (which needs `End(E)` finite-rank, positive-definite on a lattice) does not transfer as-is.
* `03-research/phase-139-row-d-two-falsifiers/R139_001_BUILDER_ROUND1.md:1044` (table row W4c) states
  the comparison explicitly: `Δ·Δ = 2−2g` (finite genus, the elliptic/function-field case) **vs.**
  `Δ·Δ = −∞` (Spec Z) — classified **PRESENT** "as a recorded degeneration, not as an analogue," citing
  Paper 46 §13.3 "the three genera, recorded and not reconciled" (`04-papers/46-row-d-the-sign/main.md:3561`
  region — three different growth regimes for the diagonal self-intersection, never reconciled into one
  finite invariant).
* Attempts to assign the divergence a **finite regularized value** exist and are recorded as the
  **rate**, not a fix: `R131_017_AUDIT_ROUND6.md:66` "Delta.Delta = -infinity (infinite genus), **rate
  computed**"; and the Tate-residue normalization (Paper 44 Thm 8bis.8, `main.md:1999`) fixes
  `vol(Z_p^×)=log p` uniquely but does **not** make the diagonal self-intersection finite — it only
  normalizes the *finite-place* measure feeding into the (still divergent) archimedean/global object.
  `04-papers/45-row-c-explicit-formula/main.md:100,1311,1588` (Paper 44 Remark 8bis.4b(1)):
  `Ŵ_fin^∞(0) = +∞`, explicitly "**not a function**" — the divergence is unbounded, stated as a standing
  fact, not sidestepped.

**Recommendation:** treat `Δ·Δ = −∞` as **TRIED–PROVED / settled** — do not attempt to re-derive it or
to "fix" it by renormalization (already tried, rate computed, still infinite); phase 146's job is to
show the redefined degree form `deg(m+nFrob)` either (a) lives on a *different*, finite-rank slice where
this obstruction doesn't apply, or (b) must confront it head-on as the reason the naive elliptic-curve
transport fails. Cite Thm 8bis.2 and W4c directly rather than re-deriving genus divergence.

---

## 4. Frobenius Gram form (Paper 44 Thm 8bis.1, 8bis.1b, 8bis.4a, Rem 8bis.4b) read as a degree form

**Status: TRIED–PARTIAL** (exists as raw material, proved unsigned; never read as "the degree form of
`Z[Frob]`" or checked for `#ker`-type nonnegativity of off-diagonal entries as a count).

* **Off-diagonal entries** (Thm 8bis.1, `main.md:3317-3386`, quoted above in the Read): the finite part is
  `(8bis.2)`:
  > `contact_fin(Frob_{r,F}) = (log q) q^{−k/2}` if `r = q^{±k}` (single prime power), else `0`.

  These entries are **manifestly nonnegative** (a log times a positive power) — this is the one piece of
  the redefined picture that already has a positivity fact recorded, but it has never been read as
  "off-diagonal Gram entries of a degree form are `Λ(m/n)`-type counts, hence `≥0`" in the corpus's own
  language; it is filed purely as a convolution identity.
* **Diagonal / archimedean part**: `(8bis.2a)` — vanishes for large `N` in one convention, and Remark
  8bis.1c (`04-papers/44-row-b-arithmetic-family/main.md:3312`, quoted above) states the point-class
  self-pairing `I_A(Frob_n,Frob_n)` **does not exist** (`Frob_n ∉ D_A`). This is the corpus's own
  statement that the "diagonal" of this particular Gram form is **ill-defined**, not merely negative —
  a sharper obstruction than "positivity fails on the diagonal": there may be no diagonal to evaluate.
* **Thm 8bis.4a** (positivity result, referenced throughout `04-papers/45-row-c-explicit-formula/main.md:158,1766,2156,2171`):
  > "positivity fails on the pure radial sector" / "positivity fails on the pure Frobenius primitive
  radial sector **in the colimit**" (`main.md:862`, citing 8bis.4a and (8bis.10), tagged `CLASSICAL`).

  The recorded reason positivity fails is explicitly attributed to the **unbounded/divergent diagonal**
  contribution once the colimit over all primes is taken (§8bis (C1), the `T_∞` chart-quantifier
  discussion, `main.md:3273-3313`) — i.e. the same infinite-genus phenomenon of §3, arrived at from the
  Gram-form side rather than the intersection-theory side.
* Phase 141 (`03-research/phase-141-row-d-frobenius-traces/`) already built the candidate quadratic form
  `Q_{C^Frob}` directly from this Gram (`R141_000_LEAD_BLUEPRINT.md:67`, quoted in full in
  `CORPUS_CHECK_R146.md` §2) and the outcome was: **"auditor verified `γ_C > 0`, zero-trace
  indefiniteness, the trace-level unsignedness"** — proved **indefinite at trace level**, not
  sign-definite, and the phase closed on an unrelated clause. This is the closest existing attempt to
  "the degree form on Z[Frob]" and it is `TRIED–REFUTED` as a source of an unconditional sign — the
  positive off-diagonal terms are outweighed/undefined on the diagonal, exactly mirroring the
  infinite-genus obstruction of §3.

**Recommendation:** `TRIED–PARTIAL/REFUTED`. Cite Thm 8bis.1 (positive off-diagonal counts — reusable
verbatim as the "count interpretation" half of α), Remark 8bis.1c (diagonal ill-defined), Thm 8bis.4a
(colimit positivity fails), and phase 141's `Q_{C^Frob}` (already-tried assembly, indefinite at trace
level) as the direct ancestor of any new degree-form construction. A genuinely new phase-146 attempt
must say what is different from phase 141's `Q_{C^Frob}` — most likely: restricting to genuinely
finite-rank sublattices of `Z[Frob]` (finite `m,n`) where the diagonal *is* well-defined, rather than
the colimit/all-primes object phase 141 used.

---

## 5. Hurwitz / finite-genus approximation / Laguerre–Pólya closure under limits / curves over finite
fields approximating ζ

**Status: TRIED–EQUIVALENT-TO-RH / TRIED–NO-GO (as a route in itself), well documented, phases 28 and 103
as expected.**

* `03-research/phase-28/08-decomposition-sectors.md:184,209,238`: "Esto es esencialmente el programa de
  la clase de Laguerre–Pólya y el problema de Pólya (pregunta abierta desde 1927)"; final line: RH ⟺
  `ξ(1/2+it) ∈` Laguerre–Pólya class — a full equivalence, not a proof route. Filed program-wide as
  `EQUIVALENT-TO-RH`.
* `03-research/phase-136-row-d-map/MAP_1_WALLS_AND_MASTER_DOCS.md:156` (row ES-17): "Real-zero
  approximants converging to Ξ — If they converge locally to Ξ, Hurwitz transmits reality — building
  that convergence IS the work" — classified `EQUIVALENT-TO-RH`, `NO_GO_AND_RETRACTIONS.md:42`.
* `03-research/phase-138-row-d-detecting-cones/CORPUS_CHECK_R138.md:220-263` (item 9): explicit prior
  corpus-check verdict, "Laguerre–Pólya / Jensen / Turán / Li / Keiper" = `TRIED–EQUIVALENT-TO-RH /
  TRIED–NO-GO (unconditional descendants)"; recommendation there: "do not reopen ... as a route to an
  unconditional [proof]."
* No hit for the specific phrase "curves over finite fields approximating ζ" as a named construction;
  the closest is the Deninger/elliptic-curve analogy of §2 (finite-field model case), and Connes–
  Consani's remark (§3) that the target is "not an abelian variety."
* `03-research/phase-55-two-arrows/175-dicotomia-de-energia.md` (extensive, Spanish) develops a
  quantitative Rouché–Hurwitz "energy dichotomy" for self-approximation of ζ, concluding (per its own
  text) that self-approximation with a zero off the line is unprecedented in either direction in the
  literature — filed as an open dichotomy conditional on "LP-112", not a resolved approximation route.

**Recommendation:** confirm `TRIED–EQUIVALENT-TO-RH` status per the phase-138 corpus check; do not
reopen finite-genus/Hurwitz approximation as an independent route for phase 146 — if used at all, use
only as a *heuristic* for what a finite-rank truncation of `Z[Frob]` would need to satisfy, citing
phase-28/103/138 rather than re-deriving the equivalence.

---

## 6. Power maps / dilations `x ↦ x^k` on the idele class group as correspondences

**Status: TRIED (unrelated context) — the corpus's power-map work is on `G_m/Z` cyclotomic geometry
(row A / phase 123), not on the idele class group / scaling site, and is not a "sign" or "degree form"
construction.**

* `03-research/phase-123-weil-strength-abc/P123_037_POWER_MAP_PRIMITIVE_COTANGENT_CUBE.md`,
  `P123_060_INTEGRAL_NORMAL_GRAPH_AND_RAMIFICATION.md:53`, `P123_061_INTEGRAL_POWER_TO_NORMAL_DEFORMATION.md`,
  `P123_063_UNIT_PARAMETER_LOCAL_CONJUGACY.md`: build composable integral power maps `π_n : z ↦ z^n` on
  `G_m`, their cotangent complexes `C_ram(n) = [Z →^n Z]`, and a deformation joining power maps to
  "normal dilations." This is **row A / cyclotomic contact geometry**, feeding the arithmetic-Lefschetz
  reconstruction (phase 107/123), not a construction on the idele class group / scaling site, and it is
  not read as a "graph of a dilation correspondence with slope k" in the Connes–Consani sense.
* No hit anywhere for "dilation correspondence," "graph of dilation," or power maps of the idele class
  group / Weil group in the row-B/C/D material (Papers 43–46) or in phases 131–146.

**Recommendation:** `NEW` as far as the idele-class-group / scaling-site setting phase 146 needs; the
existing `π_n` machinery (phase 123) is a genuinely different object (multiplicative self-maps of `G_m`
in the cyclotomic-integral setting) and should not be conflated with a hypothetical dilation
correspondence on the idele class group — but its cotangent-complex/ramification bookkeeping technique
could in principle be reused if a `[k]`-dilation correspondence on Spec Z̄ is ever built.

---

## 7. "The sign is in the additive structure" / "multiplicative semigroup is not enough" / Hecke sums,
or a no-go that additive combinations of `Frob_n` cannot carry the sign

**Status: NEW — no direct match; closest recorded principle is the phase-136 meta-theorem (multiplicative
coupling, not additive) and Restatement 12.4a's stated absence of a model-free derivation.**

* Literal phrases "sign is in the additive structure," "multiplicative semigroup is not enough," "Hecke
  sums" (in this sense) return **no hits** anywhere in `03-research`, `04-papers`, or `05-meta-and-
  planning`.
* The closest standing principle is the **opposite emphasis** — phase 136's meta-theorem
  (`03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:53`, quoted in full in
  `CORPUS_CHECK_R146.md` §6): "the sign is the interaction term between the polar/archimedean block and
  the Frobenius lattice, and it is a **phase-coherence phenomenon of unimodular local roots**" — i.e. the
  corpus's standing hypothesis locates the sign in a *phase/coupling* structure, not explicitly in
  additive vs. multiplicative algebra on `Frob`. Paper 46 Restatement 12.4a is cited alongside as: "no
  model-free derivation; the datum is `Frob_n ⋆ Frob_n^† = Δ^{(n)}`" — a purely multiplicative identity,
  offered as the *only* model-free datum in hand, which is indirect evidence *for* (not against) the idea
  that the multiplicative semigroup alone is insufficient and something more (additive combination) is
  needed — but this inference is not drawn anywhere in the corpus.
* No no-go specifically refutes additive combinations `m + nFrob` as sign-incapable; this shape has
  simply never been tried (consistent with §1's finding).

**Recommendation:** `NEW`. This is the most clearly novel piece of the redefined α: no prior phase has
proposed, still less refuted, the idea that summing (not just convolving) Frobenius classes with integer
coefficients could carry a sign. Frame it explicitly against phase 136's "phase-coherence" principle
(§7) as a candidate alternative or refinement, not a contradiction of it.

---

## What is genuinely NEW in the redefined α

1. **The additive ring `Z[Frob]` (or `Z[π]`) itself** — no prior construction anywhere in the corpus
   treats Frobenius classes as generators of a commutative ring under integer addition; only the
   multiplicative/convolution semigroup (`Frob_m ⋆ Frob_n^†`) has been built (§1).
2. **The literal degree form `deg(m+nπ) = #ker(m+nπ)` read as a count, applied to `Z[Frob]`** — the
   elliptic-curve/Hasse analogy is a constant background reference (Deninger, phase 43, phase 107) but
   has never been *constructed* for Spec Z as a labelled object; it has only been invoked as the
   unreachable target case (§2).
3. **Reading Paper 44's Thm 8bis.1 positive off-diagonal entries explicitly as "#ker/Λ-type nonnegative
   counts" of a degree form**, rather than purely as convolution/Rankin–Selberg identities (§4) — a
   reframing of existing material, not existing material itself.
4. **Naming `Δ·Δ = −∞` (Thm 8bis.2) as *the* obstruction to transporting the elliptic-curve proof
   specifically**, rather than as a free-floating fact about genus — the corpus has the fact (§3,
   extremely well established, TRIED–PROVED) but has not previously framed it as "this is why `deg(m+nπ)
   ≥ 0` cannot be run verbatim on `End(Spec Z) ⊇ Z[Frob]`."
5. **The additive-vs-multiplicative locus-of-sign question** (§7) — entirely unexamined in either
   direction.

Everything else adjacent (the Gram form's raw entries, phase 141's `Q_{C^Frob}` trace-indefiniteness,
the general "coupled pairing J" framing) is `TRIED–PARTIAL` or `TRIED–REFUTED` prior art, catalogued in
full in `CORPUS_CHECK_R146.md`, and should be cited rather than re-derived.

---

## Summary table

| # | Item | Status | Key path:line |
|---|------|--------|----------------|
| 1 | `Z[Frob]`/`Z[π]` additive ring structure | NEW | `44/main.md:3250` (mult. only); `136/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:53` |
| 2 | Degree form `deg(m+nπ)=#ker≥0`, elliptic-curve-proof analogy for Spec Z | NEW (analogy TRIED as background/no-go-for-transport) | `43/130-test-circularidad-deninger.md:22,66,82`; `107/107_00_...md:222`; `107/107_133_...md:78-80` |
| 3 | Infinite genus `Δ·Δ=−∞` as named obstruction | TRIED–PROVED (settled, recurring) | `44/main.md:3669` (Thm 8bis.2); `10/M10.1-verdict-degenerate-hodge.md:31`; `139/R139_001...md:1044` (W4c) |
| 4 | Frobenius Gram form read as degree form (off-diag counts, diagonal undefined/divergent) | TRIED–PARTIAL/REFUTED | `44/main.md:3317-3386` (Thm 8bis.1); `44/main.md:3312` (Rem 8bis.1c); `141/R141_000_LEAD_BLUEPRINT.md:67` (`Q_{C^Frob}` indefinite) |
| 5 | Hurwitz/finite-genus approximation/LP-class closure | TRIED–EQUIVALENT-TO-RH / NO-GO | `28/08-decomposition-sectors.md:238`; `138/CORPUS_CHECK_R138.md:220-263` |
| 6 | Power maps/dilations `x↦x^k` as correspondences | TRIED (unrelated context, row A/cyclotomic) — NEW for idele class group | `123/P123_037...md`; `123/P123_061...md` |
| 7 | "Sign in additive structure" vs. "multiplicative semigroup not enough" | NEW | no hits; closest is `136/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:53` (phase-coherence, not additive) |

