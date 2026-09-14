# CORPUS_CHECK_ROW_D_PLAN — what the corpus already did on the 8 candidate row-D inputs

Purpose: before launching the row-D completion plan, check each of the 8 items against
`03-research/` (phases 0–138), `04-papers/`, `05-meta-and-planning/`, `NO-GO-LIST.md`, quoting
the decisive sentences with `path:line`, classifying NEW / TRIED–PROVED / TRIED–REFUTED /
TRIED–NO-GO / TRIED–PARTIAL, and giving a one-line recommendation. Method: targeted `grep -rn`
across the four locations, then read the surrounding passage in the top hits.

---

## 1. Epstein zeta functions as falsifiers

**Status: TRIED–PARTIAL.** The corpus knows and uses Epstein zetas as a *category-level*
falsifier (positive `r_Q(n)`, functional equation, simple pole, off-line zeros, no Euler
product), explicitly distinguished from the signed Davenport–Heilbronn (DH) combination — but
never builds a canonical class / Weil form / polar block for a specific Epstein zeta; it is used
only as a name in a classification argument.

- `03-research/phase-8/PLAN-RH-PHASE8-heat-flow.md:21-24`:
  > "Epstein zeta functions (lattice zeta functions) **generically violate RH** (off-line zeros
  > are proven for many quadratic forms / class number `>1`)... what separates ζ from Epstein
  > zetas is the **Euler product**."
- `03-research/phase-58-full-audit/192-conj-179-6-rigidez-de-euler.md:87` (search for a
  counterexample in the Selberg-class category):
  > "Zetas de Epstein con número de clase h>1: ceros off conocidos (Davenport–Heilbronn mismo
  > método) pero **sin Euler** (la forma cuadrática no es multiplicativa para h>1) — fuera de la
  > categoría ✓ consistente... No se conoce ningún miembro de la clase de Selberg con un solo
  > cero off... Resultado de la búsqueda: vacía, y vacía por la razón estructural correcta (todo
  > lo que tiene ceros off conocidos carece de Euler)."
- `03-research/phase-137-row-d-canonical-coupling/R137_006_HOSTILE_FINAL.md:141-142`:
  > "**Epstein zeta functions** `Z_Q(s)` do have a simple pole, a functional equation and, for
  > class number `> 1`, **proven off-line zeros** (Davenport–Heilbronn) — but they have no Euler
  > product, so `−Z_Q'/Z_Q`..." [excluded from the falsifier class G4 needs].
- `03-research/phase-4-handoff/proofs/00-PROOF-LOG.md:1446`: "Epstein (lattice) zetas
  **generically violate RH**" (same conclusion, independent phase).
- `NO-GO-LIST.md:638`: records that "Epstein zetas have off-line zeros but no Euler product" as
  part of the reason a Dedekind/Epstein falsifier search came back empty for a specific chain
  (phase 137's N9 correction — see item 2).

Distinguishing point requested: the corpus is careful that Epstein zetas are a **different**
falsifier from the signed DH combination — DH is a linear combination of two Dirichlet L-functions
(no Euler product, signed coefficients from the character combination); Epstein zetas are a single
zeta of a binary quadratic form (no Euler product for h>1, but *positive* `r_Q(n)` coefficients,
unlike DH's signed weights). This distinction is made explicitly in phase-58 doc 192 (`(i)`
Epstein vs `(ii)` DH as two separate, non-identical members of the search).

No document constructs a canonical class, Weil form, or "polar block" specifically for an Epstein
zeta (no hits for "Epstein" + "canonical class"/"polar block"/"Weil form" anywhere in the corpus).

**Recommendation:** reuse the existing classification (Epstein = positive-coefficient, no-Euler,
off-line-zero exhibit; distinct from DH's signed no-Euler exhibit) as a ready-made falsifier
description; do **not** reopen the search for an Epstein counterexample inside the Selberg-class
axiom system (phase 58 already closed it as empty, for the structurally correct reason). If row D
needs a concrete non-Eulerian falsifier with positive coefficients, build the canonical-class /
polar-block construction for a specific Epstein zeta (h=2, e.g. discriminant −15 or −20) from
scratch — this specific construction is genuinely new.

---

## 2. Dedekind zeta / Artin L-functions / field-uniform GRH / Selberg class

**Status: TRIED–NO-GO (as a completed falsifier route) + TRIED–PARTIAL (as a named, unresolved
open question).** The corpus explicitly identifies "every Dedekind zeta function ζ_K" as
belonging to the same structural class the row-D machinery needs (simple pole, positive atoms,
functional equation, Euler product) — and just as explicitly records that **no member of that
class has a proven off-line zero**, so it cannot be used to adjudicate the row-D chain either
way. This is a corrected finding (an earlier claim that the falsifier class was *empty* was
itself found **false**).

- `03-research/phase-137-row-d-canonical-coupling/R137_006_HOSTILE_FINAL.md:14`:
  > "the vacuity claim... is **false as stated** — the falsifier class is not empty, it contains
  > every Dedekind zeta function."
- Same file, the corrected no-go paragraph (§4, "The falsifier test is vacuous here, not
  passed"):
  > "The class with G4's shape (Euler product with positive atoms, one simple pole, functional
  > equation) is large: every Dedekind zeta function `ζ_K` is in it and G1, G2, G4 and point 4
  > transfer to `ζ_K` (point 4 with a factor `[K:Q]`). But **no member of that class with proven
  > off-line zeros is known** (GRH for `ζ_K` is open; Epstein zetas have off-line zeros but no
  > Euler product; `ζ_K/ζ` has no pole). So the corpus's faithfulness test cannot adjudicate this
  > chain either way — and a sound chain would prove GRH for all number fields."
  > "**No-go recorded.** *Do not reuse the pattern "uniform bound on a renormalized `P`-family +
  > Vitali/Montel across the strip" as a route to RH.*"
- `03-research/phase-137-row-d-canonical-coupling/R137_007_LEAD_CLOSING_DECISION.md:29`:
  > "the falsifier class... is large — every Dedekind zeta `ζ_K` — but contains no member with
  > proven off-line zeros."
- `NO-GO-LIST.md:638` (same finding, corpus-wide reference copy).
- Artin L-functions and Selberg-class emptiness: `03-research/phase-58-full-audit/192-conj-179-6-rigidez-de-euler.md:87`:
  > "L de Artin no probadamente enteras: tienen Euler; su pertenencia a S depende de holomorfía
  > (Artin abierta), y bajo las conjeturas estándar son automorfas ⟹ GRH esperada — ningún cero
  > off conocido."
- "Field-uniform" / "uniform in the field" / "for every global field" formulations of the Weil
  form or carrier: no hits anywhere in the corpus (`grep -rniE "field.uniform|uniform in the
  field|for every global field"` returns nothing outside this search). This specific framing —
  proving or targeting a statement uniform across *all* number fields / global fields — is
  **NEW**; only the single-field (`ζ_K` fixed) falsifier-class question has been touched, and only
  as a negative ("no falsifier exists yet, not that GRH-uniform-in-K is provable or false").
- Towers of fields: no hits (`grep -rn "tower of field\|field tower"` empty). NEW.

**Recommendation:** do not reopen "find a Dedekind/Artin counterexample to falsify the row-D
chain" — closed, and correctly closed (would require GRH-for-number-fields, itself open, hence
this route cannot adjudicate anything). If row D wants a genuinely new construction, "field-
uniform" formulations of the Weil form / carrier, base change, or towers of fields are **untried
territory** — build only if the plan specifically needs a multi-field carrier, not as a falsifier
search (that search structurally cannot succeed without solving GRH itself).

---

## 3. Weil's finite-field RH proof transcribed step by step; Grothendieck/Deligne; "arithmetic
Lefschetz" in Paper 42

**Status: TRIED–PARTIAL, extensively.** The corpus has repeatedly transcribed Weil's mechanism at
the level of *naming* the three pillars (Frobenius, Poincaré duality, positivity/Castelnuovo–
Severi) and has run a ~140-document, dedicated phase (107) plus a full paper (42) attempting the
arithmetic transcription of the Hodge-index / Castelnuovo–Severi step specifically — with the
consistent, explicit verdict that the geometric intersection identities and Hodge index on the
square are the missing, unconstructed piece, not something re-derived from scratch.

- `03-research/phase-33-dbn/74-campos-de-funciones-mecanismo-weil.md:153`:
  > "Weil utilizó la teoría de correspondencias en la variedad producto `C × C` sobre `F_q`. La
  > forma de intersección sobre divisores de `C × C` es positiva definida en cierto sentido (la
  > desigualdad de Castelnuovo-Severi), y esto fuerza `|α_j| = q^{1/2}`."
  > "El Teorema de Weil no es trivial. Su demostración (completada por Weil y clarificada por
  > Grothendieck-Deligne) reposa sobre tres pilares." (line 127)
- `03-research/phase-33-dbn/80-castelnuovo-severi-aritmetico.md:11`: attempts to build the
  arithmetic analogue of the Castelnuovo–Severi quadratic form directly:
  > "El resultado es un diagnóstico preciso: se construye una candidata natural `Q`... se
  > establece que es semidefinida positiva (Proposición 5.2), y se identifica con precisión el
  > obstáculo que impide cerrar el argumento: el núcleo de `Q` no es trivial..."
  Also (line 45): "no puede servir como análogo de Castelnuovo-Severi, por la razón siguiente:
  `Tr(M_N) = 0` para todo `N`..." — a specific negative result about a specific candidate form,
  not a general refutation.
- `04-papers/42-arithmetic-lefschetz-programme/main.tex:130,165`:
  > "(d) the Hodge index theorem, in the Castelnuovo--Severi form." ... "derived from the explicit
  > formula does no work, because Weil's Hodge index [theorem does not transcribe]."
  (Paper 42's own stated content, per `main.tex:105`, is to transcribe "a geometric intersection
  product with a Hodge index theorem" — the paper is the deliberate, sustained attempt at this
  transcription; see also `main.log:601` citing Mattuck–Tate's *On the inequality of
  Castelnuovo–Severi* directly.)
- `03-research/phase-107-arithmetic-lefschetz-reconstruction/107_241_HODGE_INDEX_FOR_THE_CORNER_PAIRING.md:184,195,239`:
  > "Corollary 3.3 (Hodge index `⟺` RH)"..."This is verbatim the classical Hodge index theorem for
  > a surface, whose [proof does not transfer]."..."the constructed pairing, *Hodge index* and
  > *RH* are the same statement, in [the arithmetic setting]" — i.e. the transcription collapses
  > to a restatement of RH, not an independent proof route.
- `03-research/phase-39-G1G2-interface/120-inventario-CC-fuente.md:533,547` and
  `03-research/phase-39-G1G2-interface/119-axiomas-forzados.md:165,186`: the model proof (Mattuck–
  Tate/Grothendieck) and Grothendieck's *Standard Conjectures on Algebraic Cycles* (Gro69) are
  both named and cited as the classical machinery whose arithmetic analogue is sought, with
  standard-conjecture-style positivity of the Lefschetz form on motivic cohomology named as the
  needed ingredient (`03-research/phase-29/46-matematica-nueva-quiebre.md:255`,
  `03-research/phase-29/49-geometria-motivica-deficit.md:195,222` — via Beilinson–Deligne mixed
  motives, explicitly flagged as conjectural).
- Deligne's Weil I tensor-power / Rankin–Selberg weight argument: named and used piecemeal
  (`03-research/phase-116-.../previous-phase-114/114_a_183_DELIGNE_NUCLEAR_SPHERICAL_SURFACE.md:107-143`,
  tensor powers of determinant lines) but never assembled into the full weight-monodromy /ρ⊗ρ̄
  argument (see item 7 for the Rankin–Selberg-square usages specifically).
- What is explicitly marked **missing**, corpus-wide: a literal, sign-definite arithmetic Hodge
  index theorem for `Spec Z̄ × Spec Z̄` itself. `03-research/phase-136-row-d-map/MAP_5_LITERATURE_VS_CORPUS.md:40-46`:
  > "genuine, sign-definite 2-dimensional Hodge index theorem on a combinatorial stand-in object.
  > This is not `Spec Z̄ × Spec Z̄`." — the only genuine sign-definite Hodge-index results found
  are on *tropical/combinatorial* stand-ins (Cartwright 1506.02023; Adiprasito–Huh–Katz), never
  on the arithmetic object itself.

There is no single consolidated "ledger" document that goes literally line-by-line through Weil's
proof (Riemann–Roch on C×C, the graph of Frobenius, `σ(Γ)=2g·d(Γ)−...`, `Tr(Γ∘Γ')≥0`) and marks
each step's arithmetic analogue as proved/open — the closest is phase-107's `107_02_PAPER_0_FUNCTION_FIELD_CALIBRATION.md`
(function-field calibration of the mechanism, §8 "Hodge index and the Weil bound") together with
phase-33 doc 74/77/80, but these are dispersed across two different phases (33 and 107) using two
different formalisms (Jacobi operators vs. arithmetic-divisor sheaves), not one master ledger.

**Recommendation:** do not re-derive the pillar-by-pillar naming (Frobenius / Poincaré duality /
Castelnuovo–Severi) — already done repeatedly and consistently (phase 33, phase 39, phase 107,
Paper 42). Build (new, useful for row D): a single consolidated line-by-line ledger cross-
referencing phase-33's Jacobi-operator transcription against phase-107/Paper 42's divisor-sheaf
transcription, explicitly marking, for each step of Weil's proof, which arithmetic analogue is
(a) constructed, (b) constructed but collapses to RH, or (c) not attempted — this ledger itself
does not exist and would consolidate ~140 scattered documents into one reference.

---

## 4. Bost–Connes system, KMS states, β=1 phase transition, Connes spectral realization

**Status: TRIED–NO-GO (as a positivity route) — repeatedly, independently, across multiple
phases, converging on the same wall.** The Bost–Connes partition function is identified as
*literally* `Z(β) = ζ(β)`, which the corpus treats as proof that any KMS/Tomita–Takesaki route
re-imports the zero data instead of deriving it.

- `03-research/AUDIT_A_CATEGORY_CHANGES.md:25` (Teorema 161.9, "cleanest full no-go in the
  corpus"):
  > "the topological fundamental class exists RH-freely (Connes–Thom) but pairs only with
  > K-homology of the *phase* torus (blind to inertia); the only canonical *orientation* turning
  > it into a signed metric is the **dual weight** of the crossed product, whose flow is that of
  > the Bost–Connes system, whose **partition function is literally `Z(β)=ζ(β)`**."
  > "**THEOREM.** This is the cleanest full no-go in the corpus: canonicity and RH-freedom are
  > proved structurally incompatible for the entire family of approaches..."
- `03-research/phase-6/M-OS-2-S2-local-REFUTATION.md:61-63,102,110,120`:
  > "making that precise — and gluing the KMS states across places — is precisely the
  > Connes–Bost–Connes program. So the OS route, pushed candidly, **reduces to Connes**..."
  > "Connes–Bost–Connes KMS/partition-function positivity, which is the field's open core, not
  > something our [construction discharges]."
  > "Salvage (multiplicative/KMS per-place positivity) — ⬜ = Connes/Bost–Connes; low odds; the
  > candid frontier."
- `03-research/phase-8/PLAN-RH-PHASE8-heat-flow.md:23-24` (item 3 of the candid triage):
  > "the archimedean place is provably positive (prolate `λ<1`), the obstruction is the finite
  > places, same wall... the obstruction does not become a thermodynamic invariant; it stays the
  > finite-place positivity. *Verdict: done; same wall.*"
- `03-research/phase-52-homotopy-inertia/163-destructor-inercia-homotopica.md:176` and
  `162-construccion-inercia-homotopica.md:12,330,421` (three independent occurrences, same
  finding): "función de partición ζ (D161 §161.5: Z(β)=Σk^{-β}=ζ(β), idéntico a Bost–Connes)... el
  muro es la *signatura de inercia*."
- Connes' actual spectral realization (not a self-adjoint operator with eigenvalues γ_ρ, but a
  trace-formula-as-sum-over-places reading): `03-research/phase-53-quantum-import/165-destructor-import-cuantico.md:87`:
  > "Connes (1999)... **no** construye un operador autoadjunto cuyos autovalores sean los γ_ρ."
- Connes–Consani's archimedean-place positivity (2006.13771) is the one genuinely *positive*
  (unconditional) result extracted from this cluster — see item 6's cross-reference to
  `03-research/phase-136-row-d-map/MAP_5_LITERATURE_VS_CORPUS.md:16` and the "unpainted-but-lit"
  square #1 in `PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:35` ("Archimedean-only Weil positivity for
  `supp ⊂ [2^{−1/2},2^{1/2}]`... phase 118 `T ≤ log 2`").

**Recommendation:** do not reopen "Bost–Connes/KMS positivity ⟹ Weil positivity" as a route — it
is the single most independently-rediscovered no-go in the corpus (at least 4 separate phases:
6, 8, 51/52, 136-audit). Reuse Connes–Consani's archimedean-only positivity result (item above) as
the one genuinely usable unconditional fragment; do not attempt to extend it to the finite places
via KMS — that is exactly the wall.

---

## 5. Positivity in families / on average (Petersson, Kuznetsov, one-level density, ILS)

**Status: TRIED–PARTIAL (touched only tangentially, as an input to a different mechanism, never
as a proof strategy in its own right) — effectively NEW as a direct row-D avenue.**

- The only substantial engagement is with the **Motohashi/Kuznetsov spectral expansion of the
  shifted-convolution problem** (phase 14), used to check whether a *different* invariant
  (a `z`-weighted moment) is sensitive to ζ's zeros — not to derive positivity:
  `03-research/phase-14/M14.2-verdict-nontrivial-spectral-modification.md:36`:
  > "the spectral weight in the Motohashi/Kuznetsov expansion therefore **carries the ζ**-zeros
  > [information]" — a detection-sensitivity finding, not a positivity result, and not pursued
  > further as a proof avenue in later phases.
- No hits anywhere for "Iwaniec–Luo–Sarnak", "one-level density", "GRH on average", or "family
  positivity" as a named structural statement (`grep -rniE "Iwaniec.Luo.Sarnak|one-level
  density|GRH on average"` returns nothing beyond the empty set already reported). Petersson
  formula: no hits at all.
- The corpus's own "Family / averaging methods" cluster (item D in the phase-136 meta-table,
  `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:33`) is about *density /
  large-sieve / mollifier* methods for the *individual* ζ, not about statistical family results
  over a family of L-functions (Petersson/Kuznetsov families, symmetry-type families) — the
  "theorem of method obstruction" quoted there (phase 60) is a different, adjacent no-go (see
  Row-D map item on "D. Magnitude / density / averaging methods"): it says bounds using only
  `‖Λ(n)‖` cannot decide the sign, which is a statement about ζ alone, not about family averages.

**Recommendation:** genuinely open territory — build, if wanted. No individual (unconditional,
non-average) statement has ever been extracted from a family-positivity result in this corpus; the
family literature (Kuznetsov, ILS, one-level density) is essentially untouched. Caution: the
generic lesson of this corpus (item D's "phase not magnitude" theorem, phase 60) suggests such
methods are likely to face the same magnitude-vs-phase obstruction that killed every other
"average"/"density" approach — flag this risk before investing effort.

---

## 6. Unimodularity of local roots (Ramanujan bound), Frobenius unimodularity, "phase coherence"

**Status: TRIED–PARTIAL, with the stopping point precisely identified and repeatedly confirmed.**
This is the corpus's single most load-bearing partial result: local unimodularity is proved (both
as bilateral purity and as a two/n-primes theorem), but every attempt to promote it to a *global*
positivity statement stops exactly at the archimedean/polar block, or at the coupling of many
primes.

- `03-research/phase-45-fredholm/...` (bilateral purity, cited by the map):
  `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:35,item 2,3`:
  > "Single-prime local purity: Axiom H holds for `F_{p,α}` **iff** `|α| = √p` (phase 44 Doc 131
  > Thm 6.7)." "**Two-primes theorem** with incommensurable periods, extended to `n` primes: Weil
  > positivity for the prime-only object **iff** bilateral purity (phase 45 Doc 135 Thms A, A′,
  > B) — *without* archimedean/polar block."
- The "phase not magnitude" theorem (phase 60), the precise obstruction statement:
  `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:33,54`:
  > "the sign lives in the *phase coherence* of `cos(t log n)`; off-line zeros give secular growth
  > `λ^{2β−1}` no average removes" ... "**Frobenius lattice, and it is a phase-coherence
  > phenomenon of unimodular local roots.**"
- Paper 44's own construction `Frob_n ⋆ Frob_n^† = Δ^{(n)}`, bidegree `(n^{1/2}, n^{-1/2})`:
  `04-papers/44-row-b-arithmetic-family/main.tex:76-78,133-188` (the identity, the bidegree, and
  the "shadow" `Sh_Z(Frob_n)` construction that turns it into a degree-map statement,
  `cfin(Frob_n)=n^{-1/2}·degdet Prim(Sh_Z)_n`, `degdet Sh_Z(Frob_n)=log n`).
- Where it explicitly stops — no source, including the literature surveyed in phase 136,
  promotes unimodularity to global positivity: `03-research/phase-136-row-d-map/MAP_5_LITERATURE_VS_CORPUS.md:99-105`:
  > "no source uses unimodularity of local roots, or a partial-isometry/unitarity property of a
  > Frobenius-type operator, in a positivity argument... the specific mechanism the corpus's
  > row-D construction needs (`Frob_n ⋆ Frob_n^† = Δ^{(n)}`) has no precedent here... it must be
  > built from scratch."
- `03-research/phase-136-row-d-map/MAP_4_PHASES_111_135_AND_PAPERS.md:43`:
  > "No **model-free** derivation of (a)+(b′)+(c) can exist: any valid proof must, at some line,
  > read a datum of `ξ`/`ζ` that the falsifier `Ξ_a`... lacks... The natural discriminating datum,
  > heuristically, is unimodularity `Frob_n⋆Frob_n^†=Δ^{(n)}` (fails for `Ξ_a`... `(n^a+n^{-a})Δ^{(n)}`)
  > — Remark 12.4b, Theorem 7.1, **a direction, not a theorem**."
- Same synthesis document: "No object in the corpus does all three [reads (i) support growth,
  (ii) the bigrading, (iii) unimodularity]. Several do two." (`PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:66`).

**Recommendation:** reuse the two proved local-purity theorems (phase 44 Thm 6.7 single-prime;
phase 45 Thms A/A′/B two/n-primes) and the "phase not magnitude" obstruction (phase 60) as the
standing input and standing warning, respectively. Do not re-attempt "unimodularity ⟹ global
positivity" as a generic-mechanism search — the map (phase 136) already surveyed the entire
relevant literature and confirmed no precedent exists; if row D is to close this, it must build a
genuinely new coupling argument across primes (Paper 44's `Frob_n` shadow construction is the
best current scaffold to extend, per Paper 44's own definition and the phase-136 recommendation).

---

## 7. Rankin–Selberg / tensor-power tricks (Deligne), Sato–Tate, nonnegative-coefficient sign/weight
bounds

**Status: TRIED–PARTIAL, used constructively in at least two independent constructions (M1's
self-intersection theorem, and a local Tate-colligation positivity test), but never assembled into
a full Deligne-style weight-monodromy argument, and Sato–Tate itself is not engaged at all.**

- `03-research/phase-15/M1-arithmetic-intersection-pairing.md` — Theorem B, the strongest
  concrete use of the Rankin–Selberg trick in the corpus:
  > "**Theorem B** — the Frobenius self-intersection is a nonnegative Rankin–Selberg second
  > moment (effectivity), `Γ·Γ≥0`" (line 175) — verified numerically to `2×10⁻⁶` relative error
  > (§7). But M1's own conclusion (line 183, quoted in item 3/8 below) is that this reduces RH to
  > the *separate*, unresolved arithmetic Hodge index (M3) — Rankin–Selberg effectivity alone is
  > not sufficient.
- `03-research/phase-64-connes-route/CONSTRUCTION-local-Tate-colligation-p-adic.md:128,208` and
  `03-research/phase-64-connes-route/LETTER-to-Connes.md:46`:
  > "factor having nonnegative coefficients... iff the Euler factor has nonnegative coefficients;
  > DH fails locally." — nonnegative-coefficient Euler factors used as a *local* passivity test
  > (distinguishing ζ from DH at each prime), not a global sign/weight bound via ρ⊗ρ̄.
- `03-research/phase-30/55-puente-langlands-cinfty.md:118-132` engages Rankin–Selberg
  `L(s,π×π̃)` positivity on `(1/2,∞)` directly and states a proposition (6.2) about it, but this is
  used for a *different* functional `C_∞^{(F)}`, not for RH's sign.
  Also `03-research/phase-15/M2-ample-cone-edge-positivity.md:156` and
  `03-research/phase-15/SYNTHESIS-M1-to-M3-and-the-precise-gap.md:23`: Rankin–Selberg-square
  language reused across the M1–M3 milestone chain, all converging on the same open M3 gap.
- Deligne's actual weight/tensor-power argument (Weil I, ρ⊗ρ̄ has nonnegative coefficients as a
  weight bound): only fragmentary use of "tensor powers of determinant lines" appears (phase-116
  previous-phase-114 docs, e.g. `114_a_183_DELIGNE_NUCLEAR_SPHERICAL_SURFACE.md:107-143`), applied
  to determinant-line bookkeeping, not to a Rankin–Selberg-style sign argument. No document
  assembles the classical "L(ρ⊗ρ̄,s) has a pole at s=1 with nonnegative Dirichlet coefficients ⟹
  weight/sign bound" argument end-to-end for the row-D object.
- Sato–Tate: zero hits anywhere in the corpus (`grep -rniE "sato.tate"` returns nothing outside
  this search) — **NEW**, completely untouched.

**Recommendation:** reuse M1's Theorem B (`Γ·Γ≥0` as a Rankin–Selberg second moment) directly if
row D needs a nonnegative self-intersection statement — it is proved and numerically verified.
Do not expect Rankin–Selberg alone to close row D: M1 itself shows this reduces to, rather than
resolves, the Hodge-index gap. Building the full Deligne tensor-power/weight argument for the
row-D carrier, and any use of Sato–Tate, is genuinely new work.

---

## 8. Castelnuovo/trace inequality / Hodge index on the square, rows B/C terms

**Status: TRIED–PARTIAL, and identified in the corpus's own synthesis as the single central open
gap of the entire program (not specific to row D).** This overlaps heavily with item 3; the
row-B/C-specific vocabulary (`Sh_Z(Frob_n)`, bidegrees `(n^{1/2},n^{-1/2})`, Gram forms) is used,
but the trace-inequality / Castelnuovo step on the arithmetic square is not closed.

- Direct attempt at the arithmetic Castelnuovo–Severi quadratic form:
  `03-research/phase-33-dbn/80-castelnuovo-severi-aritmetico.md:11,45,53,177-353` (already quoted
  in item 3): builds a candidate `Q`, proves it PSD (Prop. 5.2), but identifies a nontrivial kernel
  and an unresolved regularization; explicitly states "no existe... una desigualdad lineal entre
  `Tr(M_N²)` y la traza de `M_N` que transporte información no trivial." (line 53).
- `03-research/phase-107-arithmetic-lefschetz-reconstruction/107_241_HODGE_INDEX_FOR_THE_CORNER_PAIRING.md:184,195`
  (already quoted in item 3): a "corner pairing" Hodge index statement collapses to a restatement
  of RH (Corollary 3.3).
- Paper 44's bidegree/Gram-form language (`Sh_Z(Frob_n)`, `(n^{1/2},n^{-1/2})`) is the row-B
  carrier used throughout Paper 44's main.tex (already cited item 6) — but Paper 44 itself does not
  claim a Castelnuovo/trace-inequality theorem; it stops at the degree-map identity
  `degdet Sh_Z(Frob_n)=log n`.
- The tropical/combinatorial stand-in with a genuine sign-definite result:
  `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:35` item 6: "Tropical toy
  `C_p × C_p`: exact Hodge index `(1,2)` on `⟨f₁,f₂,Δ⟩` (phase 41 Doc 125)" — a genuine,
  sign-definite Hodge index theorem, but only on a finite tropical toy model, explicitly noted
  (item 3 above, MAP_5) as *not* the arithmetic object itself.
- Corpus's own headline statement of the gap (this is the master finding row D must respect):
  `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:9-12`:
  > "Row D is about 20% built as a *frame* and 0–5% as *difficulty*... The difficulty is one
  > object: a dimension of sections `h⁰` on the square `Spec Z̄ × Spec Z̄` with a Riemann–Roch
  > inequality whose quadratic term is `I_∞(E,E)`. Everything the corpus can currently define
  > grows logarithmically or linearly where `¼m²` is required."
  This is the corpus's own diagnosis that `Δ·Δ = −∞` (the self-intersection of the diagonal is
  the un-constructed negative/degenerate term) is exactly the missing Castelnuovo/Hodge-index
  ingredient.

**Recommendation:** do not re-attempt a from-scratch Castelnuovo/Hodge-index proof by any of the
mechanisms already tried (Jacobi-operator quadratic form, phase 33; corner-pairing, phase 107;
these all either hit a nontrivial kernel or collapse to RH). Reuse the tropical toy model (phase
41 Doc 125) as the structural template — it is the only place a literal sign-definite Hodge index
theorem exists in this corpus — and reuse Paper 44's `Frob_n`/bidegree carrier as the arithmetic
object to transport the tropical argument onto, per phase-136's own recommendation
(`MAP_5_LITERATURE_VS_CORPUS.md`, Cartwright/Adiprasito–Huh–Katz citation). This transport is the
one open, buildable task; a "from nothing" re-derivation is not recommended.

---

## Summary table

| # | Topic | Status | Key files | Recommendation |
|---|---|---|---|---|
| 1 | Epstein zeta falsifiers | TRIED–PARTIAL | phase-8 PLAN; phase-58 doc192; phase-137 R137_006 | reuse classification; build canonical class/polar block if needed |
| 2 | Dedekind/Artin/field-uniform GRH | TRIED–NO-GO (falsifier route) / NEW (field-uniform framing) | phase-137 R137_006, R137_007; phase-58 doc192 | do not reopen falsifier search; field-uniform formulations are open if truly needed |
| 3 | Weil's proof transcribed; Grothendieck/Deligne; Paper 42 | TRIED–PARTIAL | phase-33 docs 74/77/80; phase-107 (140 docs); Paper 42; phase-39 docs 119/120 | do not re-derive pillar naming; build one consolidated ledger |
| 4 | Bost–Connes/KMS positivity | TRIED–NO-GO | AUDIT_A_CATEGORY_CHANGES (Thm 161.9); phase-6 M-OS-2-S2; phase-8 PLAN; phase-52 docs | do not reopen; reuse Connes–Consani archimedean-only result only |
| 5 | Family positivity (Kuznetsov/ILS/one-level density) | NEW (essentially untouched) | phase-14 M14.2 (tangential) | build, with caution re: phase-60 "phase not magnitude" risk |
| 6 | Unimodularity → global positivity | TRIED–PARTIAL (stopping point precisely known) | Paper 44; phase-136 MAP_4, MAP_5, SYNTHESIS | reuse proved local-purity theorems; build the coupling step, no precedent exists |
| 7 | Rankin–Selberg/tensor tricks/Sato–Tate | TRIED–PARTIAL / NEW (Sato–Tate) | phase-15 M1 Thm B; phase-64 Tate-colligation; phase-30 doc55 | reuse Thm B; Deligne weight argument and Sato–Tate are open |
| 8 | Castelnuovo/Hodge index on the square | TRIED–PARTIAL (corpus's central open gap) | phase-33 doc80; phase-107 doc241; phase-136 SYNTHESIS; phase-41 doc125 | reuse tropical toy (phase 41) as template; transport onto Paper 44 carrier |
