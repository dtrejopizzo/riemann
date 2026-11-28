# CORPUS_CHECK_R147b — Z[Gal(K/Q)] acting on Spec O_K as the missing "+"

dtrejo@biomakers.net
Purpose: pre-phase-147(b) corpus check. Question: is the missing ring of correspondences on
`Spec O_K × Spec O_K` the group ring `Z[Gal(K/Q)]`, realized by graphs `Γ_σ` of Galois
automorphisms `σ ∈ Gal(K/Q)` acting as genuine endomorphisms of `Spec O_K`, with degrees =
fixed-point counts and Frobenius elements `Frob_p ∈ Gal(K/Q)` living inside this ring?

Note: there is already a file at `03-research/phase-147-row-d-galois-ring/single-prime-tower-corpus-check/CORPUS_CHECK_R147.md`
— that is a **different** phase-147 sub-question (single-prime towers `{Frob_{p^k}}_k` and
`Frob⋆Δ^rad`, i.e. Paper 44 §8bis + Docs 131/135). This file is the corpus check for the **Galois
group-ring** idea, filed as `R147b` to avoid collision.

---

## 1. Galois / Gal(K/Q) / graph of an automorphism / Chebotarev / Artin / group ring Z[G]

**Grep:** `Galois`, `Gal(K/Q)`, `Γ_σ`, `graph of an automorphism`, `Chebotarev`, `Frobenius element`,
`Artin L-function`, `Artin formalism`, `group ring Z[G]`, `Hecke algebra of a Galois group`,
`regular representation`, `base change L/K` — across `03-research`, `04-papers`, `05-meta-and-planning`.

**Finding: the literal statement in the phase-147 charge — "automorphisms σ ∈ Gal(K/Q) are genuine
endomorphisms of Spec O_K, their graphs Γ_σ are effective curves in Spec O_K × Spec O_K, degrees are
fixed-point counts, Frob_p ∈ Gal(K/Q) lives in the ring" — does not occur anywhere in the corpus.**
Zero hits for `Spec O_K`, `Hom(Spec Z`, `endomorphism of Spec`, `automorphisms of Spec`,
`Gal(K/Q)` as an acting ring, or `Γ_σ` in this sense.

What **does** exist, and is the closest predecessor, is Phase 139's Theorem D.20 (base change),
carried into Phase 140/141/146:

* `03-research/phase-139-row-d-two-falsifiers/R139_000_BLUEPRINT.md:76-80` — base change
  `L/K`: `ξ_L = ξ_K·∏_{χ≠1}Λ(s,χ)^{χ(1)}` (Artin formalism), restated as
  `I_∞^{(L)}(N^*F,N^*F) = I_∞^{(K)}(F,F) + Σ_χ I_∞^{(χ)}(F,F)` — "the multiplicativity of the
  Frobenius family" as T2's precise content.
* `03-research/phase-139-row-d-two-falsifiers/R139_005_CLOSING_DECISION.md:20` — **Theorem
  D.20.2**: additivity of the primitive zero form under base change, over **conjugate packets**
  `Λ_{[χ]} := Λ(·,χ)Λ(·,χ̄)`. Status: **`PROVED` for `L/K` abelian** (Hecke L-functions of
  primitive non-trivial characters are entire, unconditional); **`PROVED-CONDITIONAL` on Artin's
  holomorphy conjecture** for general (non-abelian) `L/K`.
* `R139_003_ROUND2.md:32` — the repaired statement, with the reason a naive per-`χ`
  argument fails for complex `χ`: it must be taken over self-dual conjugate packets, using
  `Λ_{[χ]}(s) = Λ_{[χ]}(1−s)` and `W(χ)W(χ̄)=1` (new Lemma D.20.2a₀).
* `R139_001_ROUND1.md:844` — "Let `L/K` be a finite **Galois** extension with group `G`.
  Artin's factorization gives, as meromorphic functions, `ξ_L = ξ_K·∏_{χ}Λ(s,χ)^{χ(1)}`" — this is
  the **only** place `Gal(L/K)` (a general Galois group, via its character table) enters the
  arithmetic side of row D. It enters through **Artin L-functions indexed by characters/
  representations of `G`**, never through `G` acting geometrically as automorphisms of a scheme.
* `R139_001_ROUND1.md:1018` — **W4 = "the graph of Frobenius `Γ_q ⊂ S`"** (bidegree
  `(1,q)`, `Γ_q·Δ = N_1`). This is the *function-field* graph-of-Frobenius correspondence (the
  `q`-power map on a curve over `F_q`), **not** a graph of a Galois automorphism of `Spec O_K`.
  It is the nearest geometric ancestor in shape (a correspondence on a square whose degree is a
  fixed-point count = Lefschetz number `N_1`), but the object acted on is `C/F_q`, and the acting
  map is the arithmetic `q`-Frobenius endomorphism of a curve over a finite field, not a Galois
  automorphism of an arithmetic scheme `Spec O_K` over `Spec Z`.
* Phase 140 (`03-research/phase-140-row-d-frobenius-square/README.md`) **Theorem D.22** ("closes
  O-9"): for **ideals** `𝔫` of `O_K`, `Frob_𝔫⋆Frob_𝔫 = Frob_{𝔪𝔫}` (an inverse-semigroup law),
  `Sh_{O_K}(Frob_𝔫) = Cone(𝔫L_S ↪ L_S)`, `H⁰ ≅ O_K/𝔫`, `deg_{det} = log N𝔫`. **This is indexed by
  ideals `𝔫`, i.e. by the norm/multiplication structure of `O_K`, not by `Gal(K/Q)`; the class
  group never appears (explicitly noted).** It is the closest existing *construction* of a
  correspondence ring attached to a number field's spectrum, and the nearest technical template
  (bidegree/`H⁰`/`deg_{det}` computation) for what a Galois-graph construction would need to
  reproduce — but it is a **different ring** (multiplication-by-ideal Hecke-type correspondences,
  commutative, indexed by `Cl(K)`-forgetting ideals) from `Z[Gal(K/Q)]` (generally non-commutative,
  indexed by automorphisms, with a *finite* group of units rather than an infinite ideal semigroup).

**Chebotarev**: no hits anywhere in `03-research`/`04-papers`/`05-meta-and-planning` for
"Chebotarev" density/positivity as such (only the "Chebotarev positivity" phrase from the present
charge — searched and not found pre-existing).

**Verdict: NEW.** The specific geometric picture — `σ ∈ Gal(K/Q)` realized as a genuine morphism
`Spec O_K → Spec O_K`, its graph `Γ_σ ⊂ Spec O_K × Spec O_K` an effective divisor/curve, `deg Γ_σ`
a Lefschetz-type fixed-point count, and `Frob_p` a distinguished conjugacy class living inside this
same ring of correspondences — has never been constructed or attempted in the corpus. The corpus's
Galois content (D.20) is purely **analytic/L-function** (Artin formalism on `ξ_L` vs `ξ_K`), not
**geometric/correspondence** (graphs of automorphisms as cycles on a square). These are different
mathematical objects addressing the same word "Galois."

---

## 2. Effective classes on Spec O_K × Spec O_K with Galois twists; twisted Frobenius; Dirichlet
character twists of Frob_n; level structure; coset indicators 1_{aK}; class group characters;
Epstein zeta as signed combination of Hecke L-functions

* **Twisted Frobenius / Dirichlet-twisted `Frob_n` / class group characters**: no hits. Nowhere in
  the corpus is `Frob_n` (or `Frob_𝔫`) convolved or twisted by a Dirichlet character, a Hecke
  character, or a class-group character. **NEW** (as a construction); note this is essentially what
  a Galois/group-ring treatment would need first (χ-isotypic projections of `Z[Gal(K/Q)]` acting on
  the Frobenius family).
* **Coset indicators `1_{aK}` (Paper 44 Gram with shifted cosets)**: real, but a different mechanism.
  `04-papers/44-row-b-arithmetic-family/main.md:3348-3390` and the level-`N` coset-indicator
  convolution machinery (Theorem 8bis.1b/1b′, `03-research/phase-131-row-b-closure/R131_015...md:11`,
  `R131_011...md:147`) is about **adelic level structure** `U_s = 1+r^N Z_r` at finite places,
  producing the volume factor `V_N(n) = ∏_{r∉P(n)}vol(1+r^NZ_r)`. This is a *congruence-subgroup*
  level structure on the idele class group, not a Galois-group action; it is the corpus's nearest
  "coset" mechanism but attached to Hecke/level structure, not to `Gal(K/Q)`-cosets.
  **Classification: TRIED–PARTIAL** as raw material (the coset-indicator technology exists and is
  proved exactly), **NEW** as applied to Galois twists specifically.
* **Epstein zeta as a signed combination of Hecke L-functions**: Phase 139's `C1`
  (`R139_000_BLUEPRINT.md:27`, `R139_001_ROUND1.md:91-135`) studies the Epstein zeta
  `Z_Q(s)` of a binary quadratic form of class number `h(−D)>1`, and (`D.19.1`–`D.19.4`) its
  decomposition via genus theory into a combination of Hecke L-functions with characters of the
  class group `Cl(−D)`, sourced from `phase-8-heat-flow-monotonicity/PLAN-RH-PHASE8-heat-flow.md:21-24` ("what separates ζ
  from Epstein zetas is the Euler product"). Real zeros of Epstein zeta functions (Potter–Titchmarsh
  1935) are cited (`R139_001_ROUND1.md:1304`) as a **known counterexample regime**: Epstein
  zetas *can* have zeros off any critical line, used in Phase 139 as falsifier T2 material, not as
  a positivity mechanism. **Classification: TRIED–PARTIAL** (D.19 decomposition exists and is used
  as a falsifier probe for row D's meta-theorem; it is not repurposed as evidence for group-ring
  positivity, which would be a new use of the same decomposition).

---

## 3. "Spec Z has no endomorphisms" / rigidity / K/Q proposal for more correspondences

Grep for `Hom(Spec Z, Spec Z)`, `no endomorphisms`, `rigidity of Spec Z`, `Spec Z has no`,
`only endomorphism`, `translation not a homomorphism`: **no hits** anywhere in
`03-research`/`04-papers`/`05-meta-and-planning`/`NO-GO-LIST.md`. The corpus never states the
folklore fact "`Spec Z` has only the identity endomorphism" as an explicit numbered wall, though it
is the background reason the whole arithmetic-Lefschetz programme (Phases 107–139, `MW-5`,
`NO-GO-LIST.md` lines 200-230) treats the correspondence ring on `Spec Z × Spec Z` as essentially
empty apart from Frobenius-type multiplier classes (`Frob_n`, not literal morphisms) and the
diagonal. Related, and closest in spirit:

* `NO-GO-LIST.md:109` — **[NG-C1] Wall A**: "the zeros of ζ are global objects — no prime 'owns' a
  zero. There is no analogue of 'Frobenius at a prime' for ζ/Q." This is the rigidity obstruction
  from the *other* direction: not "Spec Z has no endomorphisms" but "there is no local Frobenius
  object to correspond with." Phase 140's `Frob_𝔫` (ideal-indexed, D.22) is the corpus's answer that
  *this specific* wall is passable once one works over `O_K` rather than `Z` — the Frobenius family
  does exist as multiplier classes, just not as literal endomorphisms of the scheme.
* `NO-GO-LIST.md:223` **[MW-5]** and its extension (Phases 107–119): the missing ingredients for
  local-global factorization are "(1) a cohomology `H¹(Spec Z, F)`; (2) an arithmetic Frobenius `φ_p`
  at each prime; (3) a positive intersection form" — i.e. exactly a request for more structure than
  `Hom(Spec Z, Spec Z) = {id}` provides. **No prior proposal in the corpus reaches for `K/Q` field
  extensions specifically as the source of the missing endomorphisms/correspondences** — the
  existing escape routes tried are Connes–Consani's arithmetic site / Borger's Λ-ring / F₁ geometry
  (`03-research/AUDIT_CONSOLIDATED.md:87,146,155`), not passing to `O_K` and using `Gal(K/Q)`.
  **Verdict: NEW** — using field extensions `K/Q` to manufacture extra endomorphisms of the
  (enlarged) base scheme has not been tried; it is a genuinely different escape hatch from CC/Borger.

---

## 4. Curves over F_q with automorphisms; Galois covers; Hurwitz curves; End(J) ⊇ Z[G];
correspondences from automorphisms (function-field-model files, phase 145, and earlier)

`03-research/phase-145-row-d-function-field-model/CORPUS_CHECK_R145.md` and its phase files are the
directly relevant precedent, but they use **F_q-Frobenius**, not a **Galois-cover automorphism
group**:

* `CORPUS_CHECK_R145.md:20-31,42` — the model is a single elliptic curve `E/F_q`; its `q`-power
  Frobenius `F` (not a Galois automorphism group) is shown `J`-linear (`[F,J]=0`), an isometry of a
  gapped polarization, eigenvalues on `|z|=√q`. Explicitly: `"the graph of Frobenius on a curve over
  F_q, which is finite and not invertible."` (`:42`) — the arithmetic Frobenius here is
  **non-invertible** (a degree-`q` isogeny), the opposite of a Galois automorphism (which is
  invertible, degree-1 fixed-point count = a genuine correspondence of bidegree `(1,1)`... except
  for ramification). No file in the corpus constructs a **Galois cover** `C → C/G` model, no
  Hurwitz-curve automorphism-group model, and no `End(Jac) ⊇ Z[G]` statement for a group `G` acting
  on a curve. Grep for "Hurwitz curve", "automorphism group of the curve", "End(J) ⊇" returns no
  hits.
* Phase 145's own recommendation (`CORPUS_CHECK_R145.md:308`, item 1) is "reuse Frobenius/
  polarization (phase 63), dictionary template + gap (phase 125), Weil-number generator (phase 119);
  build the rest fresh" — i.e. phase 145 already flagged that the F_q model is single-curve/single-
  Frobenius, and did **not** propose or build a multi-automorphism (Galois-cover) variant.
* Phase 145 §5 (`CORPUS_CHECK_R145.md:203-312`) treats Connes–Consani's *Riemann–Roch for Spec Z̄*
  (arXiv:2205.01391) as the corpus's model for `Spec Z̄` itself carrying a Riemann–Roch-type
  cohomology; that paper's own machinery has **no Hodge-index statement** and **no automorphism-
  group action** built in (confirmed gap, reused as "CC has no Hodge-index statement of its own").

**Verdict: NEW.** No curve-with-automorphism-group / Galois-cover model exists anywhere in the
function-field-model literature reviewed by the corpus (phase 145 and its predecessors phase 63,
119, 125). The corpus's function-field analogy has always used the absolute Frobenius (a
non-invertible degree-`q` map), never a finite automorphism group `G = Aut(C/F_q)` or `Gal(C/C₀)`.

---

## 5. Positivity of the group-ring form (Frobenius/regular trace form on Z[G]); Rosati; positive
involution; Frobenius-Schur; Chebotarev positivity; connection to zeros

* **Rosati positivity, as the `g→∞` generalization of the norm form on `Z[Frob]`:**
  `03-research/phase-145-row-d-function-field-model/R145_004_CONFIRMATION.md:139-142`:
  "the rank of the endomorphism module grows, and the elementary norm form is replaced by **Rosati
  positivity** `Tr(f f†) > 0` on `End(Jac)⊗Q`." And explicitly, `R145_004...md:125-134` **Warning 1**
  — *"the arithmetic statement 'the degree form on `Z[Frob]` is positive semidefinite' is Weil
  positivity, i.e. RH. ... A round that posits a positive form on `Z[Frob]` has assumed RH exactly
  as a round positing bigness would."* **This is the single most load-bearing prior finding for
  phase 147(b):** it is a direct, explicit warning, already in the corpus, that assuming or
  positing positivity of a trace/norm form on an endomorphism ring (whether `Z[Frob]` for one curve
  or, by the obvious extension, `Z[Gal(K/Q)]` acting on `Spec O_K`) is circular — it *is* the
  Weil/RH-equivalent statement, not a route to it. Any phase-147(b) construction must therefore
  produce the *count* (fixed-point/degree numbers) unconditionally, and treat the *positivity* of
  the resulting form as the open, RH-equivalent question — exactly as row D has done throughout
  Phases 122–146 for the "polar block" and "Hodge index" clauses.
* **Frobenius-Schur indicator, positive involution (as classical group-representation notions)**:
  no hits in the corpus; not used anywhere as a mechanism.
* **Chebotarev positivity**: no hits (see §1).
* **MW-4** (`NO-GO-LIST.md`, "Hilbert–Pólya wall, wrong sign") is the general-purpose prior finding
  that *every* unconditional tool on ζ gives a lower bound on positivity while RH needs an upper
  bound — directly applicable as a risk flag to any Frobenius/Rosati/group-ring positivity claim in
  phase 147(b): unconditional group-theoretic identities (character orthogonality, class equations)
  will very likely fall on the "wrong sign" side by the same universal pattern (8 independent
  confirmations cited).

**Verdict:** the *danger* (positing group-ring positivity ⟺ assuming RH) is **TRIED–PROVED as a
warning** (R145_004 Warning 1, MW-4). The *specific mechanism* (Rosati/Frobenius-Schur positivity on
`Z[Gal(K/Q)]`, or Chebotarev-density positivity, as a route around that circularity) is **NEW** —
never attempted.

---

## 6. Uniform-in-the-field statements already proved to build on

These are the genuine reusable assets for phase 147(b):

* **T1 / Phase 139 D.20.2 base-change additivity** (over conjugate packets `Λ_{[χ]}`), `PROVED`
  unconditionally for abelian `L/K`, `PROVED-CONDITIONAL` on Artin holomorphy in general. Gives:
  for any tower `K ⊂ L` with `L/K` Galois of group `G`, the primitive zero form of `L` decomposes
  additively over the irreducible characters of `G` (in self-dual packets). This is exactly the
  decomposition a `Z[G]`-module structure on the zero data would need as its first sanity check —
  **already proved**, so phase 147(b) does not need to reprove decomposition-by-character, only to
  give it a *geometric* (graph-of-automorphism) source rather than an *analytic* (Artin L-function)
  one.
* **Phase 139 D.20.1(iii)/D.21.3**: "Euler-product step = W4 (the Frobenius correspondence and its
  composition law); field-uniform step = W2+W5 (Riemann–Roch and Hodge index on the square)" —
  `PROVED`. Names precisely which sub-step of the Weil mechanism is uniform in the field and which
  is not; phase 147(b)'s Galois-graph construction would slot into the "field-uniform step," and
  must be checked against exactly this dichotomy.
* **Phase 140 D.22** (`Frob_𝔫` for ideals of any number field `K`, `PROVED`, closes O-9): the
  worked template — semigroup law, `Sh_{O_K}`, `H⁰≅O_K/𝔫`, `deg_{det}=log N𝔫`, "non-monoidal by Tor"
  — for constructing an arithmetic correspondence object attached to `Spec O_K` uniformly in `K`.
  Directly reusable as the technical scaffold (Shimura-cone / `H⁰` bookkeeping) for computing
  `deg Γ_σ` and `Sh_{O_K}(Γ_σ)`.
  **Sharp warning inherited from D.23.12(A)/Paper 44 Thm 8bis.4a**: the *analogous* Frobenius Gram
  form (weights `Λ(q^k)q^{-k/2}`) is **unsigned at every finite chart** — i.e. the nearest existing
  concrete Gram computation on this kind of object is proved *not* positive. Any `Γ_σ`-Gram
  construction should expect the same outcome unless a structurally new ingredient (e.g. the finite
  order of `σ`, absent for `Frob_𝔫` which ranges over an infinite semigroup) changes the analysis.
* **Phase 141 D.30 (`h⁰_{RR}^+`)**: clauses (a),(c) proved unconditionally and model-uniformly (any
  number field, any polar rank) — the containment clause (b′)⁺ is the one place sign information
  could enter, and RH⟹(b′)⁺ is proved only on the zero-free locus (O-18 open in general). This is
  the sharpest general-K template for "what would have to be true of a `Z[Gal(K/Q)]`-indexed `h⁰`
  for it to certify positivity," and the open item to target if phase 147(b) tries to supply a
  concrete `h⁰` reading Galois-graph data.

---

## Summary table

| # | Question | Status | Key files |
|---|---|---|---|
| 1 | `σ∈Gal(K/Q)` as literal endomorphisms of `Spec O_K`; `Γ_σ` as effective curves; degree = fixed-point count; `Frob_p` living in `Z[Gal(K/Q)]` | **NEW** | phase-139 D.20 (analytic Galois content, different object); phase-140 D.22 (`Frob_𝔫`, ideal-indexed, different ring); `R139_001...md:1018` (function-field `Γ_q`, non-invertible Frobenius, different map) |
| 2 | Effective classes / twisted Frobenius / class-group-character twists / coset indicators / Epstein-as-Hecke-combination | mostly **NEW**; coset-indicator and Epstein-decomposition machinery **TRIED–PARTIAL** as reusable raw material | Paper 44 §8bis (`main.md:3250-3900`); phase-139 D.19 (Epstein/genus theory) |
| 3 | "Spec Z has no endomorphisms" as an explicit wall; `K/Q` extensions proposed to supply correspondences | statement itself **not previously written down explicitly** (implicit throughout MW-2/MW-5); the specific `K/Q`-extension escape route is **NEW** | `NO-GO-LIST.md:109,200-230` (NG-C1, MW-5) |
| 4 | Curves with automorphism groups / Galois covers / Hurwitz curves / `End(J)⊇Z[G]` as function-field models | **NEW** — corpus's F_q model always uses the (non-invertible) absolute Frobenius, never a finite automorphism group | phase-145 `CORPUS_CHECK_R145.md` (esp. `:20-42`), phase-63, phase-119, phase-125 |
| 5 | Positivity of a group-ring / Rosati / regular-representation trace form connected to zeros | the **danger flag** (positing it ⟺ assuming RH) **TRIED–PROVED**; the specific mechanism (Rosati/Frobenius-Schur/Chebotarev positivity as an *escape* from that circularity) is **NEW** | `phase-145 R145_004_CONFIRMATION.md:125-142` (Warning 1, Rosati); `NO-GO-LIST.md` MW-4 |
| 6 | Uniform-in-`K` results to build on | **TRIED–PROVED**, reusable directly | phase-139 D.20/D.21.3 (base change, conjugate packets); phase-140 D.22 (`Frob_𝔫` template, and D.23.12(A) unsigned-Gram warning); phase-141 D.30 (`h⁰_{RR}^+`, O-18) |

**Bottom line — what is genuinely new in "Z[Gal(K/Q)] as the missing +":**

1. The *geometric* realization of `σ ∈ Gal(K/Q)` as literal morphisms `Spec O_K → Spec O_K` with
   graphs `Γ_σ` as effective curves on the square, as opposed to the corpus's existing purely
   *analytic* treatment of Galois groups (Artin L-function decomposition, D.20) or its existing
   *ideal-indexed* Frobenius correspondences (D.22, no Galois action).
2. Realizing `Frob_p` not as a standalone multiplier class (as in Paper 44/Phase 140/141) but as a
   distinguished conjugacy class *inside* the same finite (for each degree) group ring
   `Z[Gal(K/Q)]` that also contains all the `Γ_σ` — i.e. giving Frobenius a home in a genuinely
   finite-rank ring, rather than an infinite semigroup indexed by all ideals/integers.
3. Twisting the Frobenius/Galois correspondences by class-group or Dirichlet characters, and
   reading class-group characters as data on this ring (no precedent in the corpus).
4. A Galois-cover / automorphism-group model on the function-field side (`End(Jac)⊇Z[G]`,
   Hurwitz-curve style), which the existing phase-145 model never built (it used the absolute,
   non-invertible Frobenius only).
5. Using field extensions `K/Q` specifically (rather than Connes–Consani's site, Borger's Λ-rings,
   or F₁-geometry) as the source of "more endomorphisms" of the arithmetic base — an escape route
   from the rigidity of `Spec Z` that is not on record anywhere in the corpus.

All five must be built under the explicit corpus warning (item 5 above, `R145_004` Warning 1 /
`NO-GO-LIST.md` MW-4): the count (degree/fixed-point structure) can be unconditional, but positing
the resulting bilinear/trace form's positivity is not a route to RH — it is RH (or a
Rosati/Hodge-index-equivalent restatement of it) unless a genuinely new, unconditional structural
reason for positivity (finite order of `G`, character orthogonality, an explicit Riemann–Roch
count) is supplied and verified against the sharpest existing negative results (D.23.12(A)/8bis.4a:
the nearest concrete analogue, the Frobenius Gram form, is already proved unsigned at every finite
chart).
