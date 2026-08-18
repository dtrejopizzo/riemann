# Audit A — Category-change escape attempts

**Scope.** `THE_BACKWARD_MAP.md` proves — inside the Schwartz-data class `D` — that no lattice
exists (O1: `D` is a C-vector space, `h^0(nD)=h^0(D)`; O2: correspondences have infinite mutual
intersection, `|(n/m)^ρ|=(n/m)^{1/2}↛0`; O3: no spectral gap). This document inventories every
attempt found in the corpus to sidestep O1–O3 by changing the *category* or the *kind of
invariant* used to read RH, rather than working inside `D`. Method: full read of
`THE_BACKWARD_MAP.md`, full read of every document below, targeted search for additional
candidates (`grep` across `03-research` for Witt/K‑theory/topos/motive/homotopy/KK/prismatic
vocabulary). Not exhaustive — see §4 for declared gaps.

Convention: **THEOREM** = the corpus proves the route is closed (a specific proposition/theorem
with a complete proof). **STALL** = the route is unbuilt, abandoned, or reduced to a named open
problem, with no proof that it is impossible.

---

## 1. Inventory table

| # | Phase / doc (path) | Category / invariant proposed | What was actually PROVED | How it failed — where ζ re-enters | Verdict |
|---|---|---|---|---|---|
| 1 | `phase-44-creative-breakthrough/131-hodge-witt-inercia-visible.md` | Real Witt group `W(ℝ)≅ℤ` as codomain for an "inertia defect" `Def(X)∈W(ℝ)`, on a new object type "Hodge-Witt". | Teorema 1: no scalar/trace-only invariant can decide the negative index (two forms with equal trace, different neg.ind). Teorema 2: the Witt class + dimension *does* determine neg.ind (Sylvester). Teorema 3–4: internal consistency lemmas about the design contract. | N/A — doc is purely definitional/foundational; no construction of the actual pre-RH polarization is attempted, only its requirements are listed (Conjetura 131.A, tagged `[DESEO]`). | **STALL.** Explicitly a "documento de arranque"; superseded immediately by doc 132. |
| 2 | `phase-44-new-mathematics/132-teoria-del-defecto.md` | Category **𝒫ol_δ** (Hermitian spaces with a marked primitive subspace and a defect `δ=neg.ind`), built from Krein-space / Witt-group technology; the off-critical part `K_off` of the Pontryagin space is analyzed as a Witt class. | Teorema A (Prop. A.4): the **only** additive-under-⊕, multiplicative-under-⊗ invariants of the category are dimension `d` and reduced signature `σ`; `δ=(d−σ)/2` is provably **not** a character. Teorema E (§7–8.2): `K_off` has signature `(2m,2m)`, i.e. `σ(K_off)=0`, `θ=1/2` — **`K_off` is Witt-trivial** and sits in the tensor-absorbing "hyperbolic ideal." Teorema C (§5, Gershgorin argument): a replicable negative vector forces `δ=∞` (abstracts Doc 112's Rouché mechanism without mentioning ζ). | Applying Teorema C to the ζ-object requires "Axiom R" (every negative vector of `K_off` is replicable). Of its three sub-hypotheses, two are theorem/model-gap; the third — that translated copies of the vector are genuine ζ-isometries — is **identified explicitly as LP-112, the pre-existing open self-approximation conjecture on ζ** ("§8.2(d): la hipótesis restante ... es la vieja LP-112 disfrazada — sí, es ella"). ζ re-enters at the point where the abstract "replicability" axiom must be cashed out as an analytic statement about ζ approximating its own translates. | **THEOREM** that every character-valued (Witt/dimension) invariant is blind to `δ` (Prop. A.4 + Teorema E), combined with a **STALL**: the one route that could still see `δ` (Teorema C) reduces to the unsolved LP-112. |
| 3 | `phase-51-functor-construction/160-construccion-functor-fase-inercia.md` | Noncommutative-dynamics category: crossed product `𝒜=C(𝕋)⋊_φℝ` of the Kronecker flow on the Bohr torus; three candidate transport functors phase→inertia (`𝔉_coh`, `𝔉_KMS`, `𝔉_ind`). | Prop. 160.7: `𝔉_KMS` is a genuine, non-tautological morphism (not the explicit-formula identity) that transports the prime side of the Weil formula into a function of the "height" dual variable `s`, **without using Q**. Prop. 160.10 (THEOREM): to read the transported object as the *inertia* form (signature `m`), the inner product on `H_altura` **must be** the Weil form `∑_ρ ĥ(γ_ρ)ĥ'(γ_ρ)*`, which enumerates the zeros. | ζ re-enters exactly at the **polarization metric**: the only known inner product with signature `m` on the height space names the `γ_ρ`; the flat/dynamics-only inner product is RH-free but has signature 0 (blind). Diagnosed as structurally identical to Phase 43's Kähler–Riemann metric circularity. | **THEOREM** (Prop. 160.10) that the metric, not the transport, carries ζ. Verdict recorded in-doc as "(D) with a core of (B)" — a genuine partial construction with the residual gap named (GAP-160.A), not a full no-go of the whole family. |
| 4 | `phase-51-functor-construction/161-metrica-canonica-kk.md` | KK-theory / noncommutative Poincaré duality: fundamental class `[Δ]∈KK_d(𝒜⊗𝒜°,ℂ)` of the crossed product, via Connes–Thom, as the canonical candidate for GAP-160.A's missing metric. | **Teorema 161.9** (circularity theorem, full proof): the topological fundamental class exists RH-freely (Connes–Thom) but pairs only with K-homology of the *phase* torus (blind to inertia); the only canonical *orientation* turning it into a signed metric is the **dual weight** of the crossed product, whose flow is that of the Bost–Connes system, whose **partition function is literally `Z(β)=ζ(β)`** (Cálculo 161.5, elementary once the modular Hamiltonian's spectrum is identified as `{log k}`). | ζ enters at the **orientation/normalization of the KK fundamental class** — the canonical peso dual's partition function is `ζ(β)` (Bost–Connes identification), and the resulting metric's signature at `Re β=½` is governed by the zeros. Triple-stress-tested (T1/T2/T3, §3.4) against a "grail" reading; all three refute it. | **THEOREM.** This is the cleanest full no-go in the corpus: canonicity and RH-freedom are proved structurally incompatible for the entire family of approaches "read inertia off the KK/Poincaré-dual class of the crossed product of the primes' flow" (§5.3 states the closed family explicitly). |
| 5 | `phase-52-homotopy-inertia/162-construccion-inercia-homotopica.md` | Stable-homotopy secondary invariants: an **L-theory cofiber spectrum** `𝔼_off` (Ranicki), whose π₀ is the Witt class; an **e-invariant of Adams** `e_ζ∈ℚ/ℤ` (Chern character mod ℤ, metric-free) built from a stable map Φ ("the explicit formula as a duality zeros↔primes"). | Prop. 162.4: the primary invariant (Witt class of `𝔼_off`) vanishes homotopically (re-derives Doc 132's finding at the level of L-theory, no metric used). **Teorema 162.7a**: `e_ζ∈ℚ/ℤ` is well-defined using only the Chern character (genuinely metric-free — passes the anti-circularity guard). Teorema 162.7c: the Chern character of the extension class, evaluated against the fundamental class `[C_Φ]`, reproduces `Σ_ρ δ_{γ_ρ}` exactly. Prop. 162.9: the functional symmetry `σ:s↦1−s` forces the first secondary differential `d_2` to vanish too (transfer of a free Klein-group cover) — the blindness propagates one floor up. | ζ re-enters **not in the metric** (that step is genuinely evaded — the documented novelty) **but in the identification of the carrier spectrum**: the stable map Φ's fundamental class *is* the zero-counting distribution; computing `e_ζ` RH-freely requires already knowing `{γ_ρ}` (or, dually, the spectrum `{log k}`, whose partition function is ζ again — same node as doc 161). | **THEOREM** (162.7c) that the metric-free secondary invariant, though genuinely constructed, still re-encodes ζ — at the carrier, one node deeper than doc 161's orientation node. Author's own verdict: "B (localized re-entry) with a fragment of C." |
| 6 | `phase-52-homotopy-inertia/163-destructor-inercia-homotopica.md` | Adversarial re-examination of doc 162's construction (same category). | Three independent theorems: **(i)** Hallazgo 163.1 — the nullhomotopy/filler required to define *any* secondary invariant over the vanished Witt class is exactly the Lagrangian witnessing `K_off`'s hyperbolicity, and a Lagrangian `L=L^⊥` is by definition data *of* `Q`; the "metric-free" filler silently reintroduces `Q`. **(ii)** Hallazgo 163.2 (flagged as new, not in docs 156/161) — since `2m=κ` is even and an *integer*, its image in the natural Adams-style receptor `ℚ/ℤ` is identically 0; a secondary invariant valued in `ℚ/ℤ` cannot carry an integer at all, by group-theoretic necessity, **before ζ gets a chance to enter**. **(iii)** Vía 3 — any carrier spectrum built from the primes has spectrum `{log k}` and partition function ζ (same node as doc 161); a carrier *not* built from the primes is RH-free but its equality to `2m` is exactly the nonexistent Connes/Deninger object (doc 156's central gap). | Two of the three kill-mechanisms are ζ-re-entry (same nodes as docs 161/162); the third (parity/receptor) is **not** a ζ-re-entry mechanism at all — see §2. | **THEOREM** (three independent, fully proved). Verdict: "the three ways all kill the construction; it is one obstruction seen three times... one of them (parity) is genuinely new and does not even reach ζ." |
| 7 | `phase-49-cross-the-wall/156-probe-indice-maslov.md` | Index theory: spectral flow / Maslov index of a Lagrangian path / APS η-invariant / Toeplitz winding number, applied to the self-adjointified operator `H_J=JH_C` on the Pontryagin space. | **Teorema 156.5**: under `m<∞`, `κ=neg.ind(Q)=−Ind(T_φ)=winding(φ)=sf{H_C(t)}=Mas(L(0),L(1))=2m` — spectral flow, Maslov index and Toeplitz winding are literally the same integer (Cappell–Lee–Miller + Phillips). **Prop. 156.6** (THEOREM): the Toeplitz operator `T_φ` fails to be Fredholm at all once `m=∞` — RH-strength input is needed just for the index *object to exist*, not merely to compute it. **Prop. 156.7** (THEOREM): even granted Fredholmicity, the winding number = zero-position count. | ζ enters in **two layers**, and the primary one is existence: the symbol `φ` is invertible in the corona iff the off-line zeros are finite (`m<∞`), i.e. Fredholmicity of the candidate index operator is already RH-adjacent. Secondarily (granted Fredholmicity), the class itself is the zero count (principle of the argument). | **THEOREM**, two-layered. Establishes the "trifurcation" (existence / orientation-normalization / escape) that docs 160/161/162/163 explicitly map their own findings onto. |
| 8 | `phase-65-signature-continuity/` (D0–D12, M1, D3, culminating in `RH-PROOF.md`, `D8.5-COMPLETE.md`) | Krein–Langer / de Branges category: **index-graded determinant category 𝒢**, objects `(D,D^src,K,𝔟,ℛ)`, Kreĭn–Langer negative index realized as a **functor** `κ:𝒢→(ℤ_{≥0},≤)` (Lemma functor, D3 Theorem d3); "Witt principle" that a positive pole is a positive line (`κ` unaffected). | D1–D7, D9–D11 unconditionally proved (functoriality, monoidal structure, DH-falsifier separating ζ from Davenport–Heilbronn at the object level, closedness of `κ=0` in the constructed topology). **D12 audit**: the entire package reduces to one named load-bearing input, **D8.5** (source-level Tate×Binet local-factor convergence): *"If D8.5 holds, RH follows; if D8.5 fails, the package does not conclude, and an off-line zero is consistent with everything proved."* | Not a clean ζ-re-entry diagnosis of the doc-156/161 type; the residual is an explicit open analytic convergence claim, not an identified point where a discreteness-imposing step forces ζ back in. Later documents in the same phase (`RH-PROOF.md`, `D8.5-COMPLETE.md`, `D8.5d-...`) claim D8.5 is discharged and the chain closes unconditionally, hinging on a single flagged input **H1** ("`Λ≥0`" / self-adjointness of `A_P`). This claim was **not** promoted to `04-papers/`, and the programme's later phases (66 onward, through 118) continue attacking RH without treating it as resolved — an internal inconsistency the corpus itself does not reconcile. | **STALL** by the phase's own final audit (D12); the phase's *later* self-assessment (`RH-PROOF.md`) claims closure, but this claim is not corroborated by the rest of the corpus and is flagged here as **unresolved / disputed**, not verified. See gap note in §4. |
| 9 | `phase-67-quantum-q-index/` (PHASE67-MAP.md, E67_1–E67_20) | Compact-quantum-group / q-deformation category: Woronowicz CQG comultiplication, Cuntz `ℕ^×`-semigroup, Jantzen filtration at roots of unity, as a reader for the "Omega_7" defect `δ_N=neg.ind(A_N−P_λ)≥0`. | A sequence of small, explicit no-go propositions for each positive/canonical algebraic handle tried: group-like Euler corepresentation collapses to Bost–Connes (E67.2); free-product Haar orthogonality destroys the needed interference (E67.4); Woronowicz-modular Cauchy–Schwarz gives only the incoherent ceiling `S_abs` (E67.5–7); the semigroup isometry route detects the wrong invariant, divisibility not log-distance (E67.8); diagonal q-twists at roots of unity fabricate spurious negatives (E67.12/13). Positive result: a **faithful signed index** `ind_-(A_N−P_λ)` (E67.9) equivalent to Omega_7, and a rigorous reformulation as a 2-variable **GLT/pseudodifferential symbol positivity** condition (E67.16–20). | Every *positive* (Haar-state, CP-map, q-dimension) construction gives only an "incoherent ceiling" blind to the phase cancellation that carries RH's content; the one faithful reader is already exactly as hard as Omega_7 (itself an open RH-equivalent reduction from phases 52–53). No single, localized "ζ re-enters here" step is isolated — the wall is diagnosed as the *quantum form* of the general Weil-positivity / master-quantifier wall. | **STALL.** Explicit final line: "Omega_7 is open, exactly as in P52/P53 — no regression." Multiple **THEOREM**-level sub-rejections of specific positive constructions along the way. |
| 10 | `phase-15/M6-the-prismatic-route-assessment.md` | Prismatic cohomology (Bhatt–Scholze): Frobenius + Sen/monodromy operator on `RΓ_Δ(X/A)` as a source of a *canonical integer grading* (Hodge–Tate weights), proposed to repair the missing integer-graded Hard Lefschetz of the archimedean route (M5). | **Proposition M6** (full argument): the prismatic Frobenius eigenvalues are the *local* Satake parameters `{α_{i,p}}` (anatomy side of the explicit formula), not the global zeros `{γ_ρ}` (spectral side); for `ζ_ℚ` the local structure is trivial (`N=0`, rank-1 Tate motive) so the integer monodromy grading it supplies is trivial. | ζ's zeros never come into contact with the prismatic Frobenius at all — the two live on opposite sides of the explicit formula's duality. Not a "ζ re-enters" failure; a **wrong-object** failure: the category computes the anatomy, not the zeros. | **THEOREM.** "No escape... relocates to SURF [the missing global arithmetic surface], not to a new obstruction." Predates the O1/O2/O3 framework (phase 15 vs. phase 113) but is the same shape of attempt. |
| 11 | `phase-107-arithmetic-lefschetz-reconstruction/107_166_MONOID_TOPOS_COHOMOLOGICAL_DIMENSION_NO_GO.md` | Topos-theoretic cohomology: derived global sections (`Ext`) in the presheaf topos `Ñ^{×2}` on the two Frobenius rulings, proposed as row-(a)/(b) cohomology for the arithmetic square. | **Theorem (§2, full proof)**: for `r` finite primes, `Ext^k_{R_P}(ℤ,ℤ)≅⋀^kℤ^{2r}`, nonvanishing up to `k=2r`, i.e. **unbounded cohomological amplitude** as the prime-support grows, whereas a Weil-type square needs amplitude `[0,2]`. | Not a ζ-re-entry: the category fails on a pure dimension/combinatorics count before any invariant tied to zeros is even defined. | **THEOREM.** Clean dimension no-go; explicitly scoped as not ruling out *other* geometric realizations, only the raw monoid-topos derived-invariants functor. |
| 12 | `phase-114-closing-the-four-rows/114_a_36…58_I7_WITT_*` (≈15 docs; two sampled in full: `114_a_36`, `114_a_38`) | F₁/Haran generalized-ring geometry: Witt-vector Verschiebung operators `V_n` on Haran's cyclotomic Witt Hilbert space, sought as **correspondence classes** on Haran's literal arithmetic square `X×_{Spec 𝔽{±1}}X`. | `114_a_36` Theorem 2.1/3.1: `V_n` give a faithful multiplicative representation of the correspondence algebra whose diagonal trace recovers `Λ(n)` **exactly** (cyclotomic identity `Φ_n(1)`), no metric, no averaging — genuinely new and correct. `114_a_38` Theorem 2.1 + Corollary: any transport of the Witt graphs onto Haran's square through an *ordinary commutative* scalar map factors through the diagonal fold and **collapses** `δ_1=δ_2`, destroying the off-diagonal structure that would carry intersection data — a clean impossibility for the naive route. | Neither doc reaches ζ: `114_a_36` is "closed operatorially, open geometrically" (no map to actual divisors/cycles exists yet); `114_a_38` fails on a universal-property/diagonal argument, before any arithmetic content is read off. | **Mixed, and largely THEOREM-of-partial-closure**: real positive construction (faithful `Λ(n)`-reading operator algebra) plus a real no-go (scalar transport collapses). This cluster targets rows (a)/(b) of the Weil analogy (the space and its correspondences), not the O1/O2/O3 escape from `D` directly — flagged as adjacent, not a direct answer to the corridor asked about. Not fully audited (13 further docs in the cluster unread; see §4). |

---

## 2. Is there a common mechanism?

**The working hypothesis** (stated in the task): every route needs a discrete/integral invariant;
every construction tried is C-linear or continuous; ζ re-enters exactly at the point where
discreteness is imposed.

**Strong confirmations.**

- **Doc 132, Prop. A.4** is close to a formal proof of the hypothesis for one whole family: in the
  Grothendieck ring of the category 𝒫ol_δ, the *only* character-valued invariants are dimension and
  reduced signature; the defect `δ` (the discrete thing you actually want) is provably not a
  character — i.e. not obtainable from any C-linear/multiplicative structure. What replaces it
  (Teorema C, the replicability dichotomy) is exactly where ζ's own self-approximation (LP-112)
  has to be smuggled back in.
- **Doc 161, Teorema 161.9** is the cleanest instance: the KK-theoretic fundamental class is
  RH-free and continuous/topological (K-homology of the phase torus); the *only* canonical way to
  turn it into a signed (discrete) invariant is to orient it, and the canonical orientation is a
  Tomita–Takesaki modular weight whose partition function is literally `ζ(β)`. Discreteness
  (signature) is imposed exactly at the orientation step, and ζ is exactly what supplies it.
- **Doc 162/163**: the metric-free e-invariant lives in the continuous-looking group `ℚ/ℤ`
  (a colimit of finite cyclic groups — genuinely "discrete" in one sense, but built to be
  RH-free); it fails not because ζ invades the group but because reading off *which* class
  represents the arithmetic duality (the carrier's fundamental class) already needs `{γ_ρ}`.
  This still fits the hypothesis if "discreteness" is read as "the specific integer/finite datum
  that ties the abstract invariant to the arithmetic object," not merely "the target group is
  discrete."
- **Doc 156**: the plainest case — the index (a literal integer) simply does not exist as an
  object until Fredholmicity is granted, and Fredholmicity **is** `m<∞`. Discreteness is not
  imposed gradually; the whole index-theoretic apparatus is gated on it from the start.
- **Doc 67 (quantum route)**: every *positive* (hence order-preserving, "continuous-flavoured")
  construction is explicitly shown to give only an incoherent upper bound; the one *faithful*
  reader is already a signed (discrete) index, and it is exactly as hard as RH.

**Genuine counterexamples / complications** — cases where the failure has nothing to do with ζ
re-entering:

- **Doc 163, Hallazgo 163.2 (parity kills the receptor).** Since `2m` is already an even integer
  (Doc 132/156), its image in the natural secondary receptor `ℚ/ℤ` is trivially 0 — the
  construction dies from group theory (integers vanish in `ℚ/ℤ`) *before* any ζ-dependent step is
  reached. This is a real counterexample to a *literal* reading of the hypothesis: not every
  failure is "continuous construction, ζ enters at discretisation" — some fail because the
  discreteness *was* achieved (an integer, `2m`) but the receiving structure cannot represent it.
- **`107_166` (topos amplitude no-go)** and **`114_a_38` (diagonal collapse)**: both are pure
  dimension-counting / universal-property failures. ζ is not reachable at all — the category is
  the wrong shape before any invariant-reading step exists. These show that some category-change
  attempts die on **row (a)/(b) construction grounds**, independent of the O1–O3 / ζ-reentry
  story that governs the row (c)/(d) attempts.
- **Phase 65** does not cleanly fit either column: its residual (D8.5) is a named open analytic
  convergence statement about local factors, not a diagnosed point where imposing discreteness
  reveals ζ. It is best read as *unresolved*, not as evidence for or against the hypothesis.
- **Phase 15 (prismatic)**: fails for a third, distinct reason — it computes the wrong side of
  the explicit-formula duality (local Satake data, not the global zeros). Not a discreteness
  failure at all; a category/target mismatch.

**Net assessment.** The hypothesis holds with real force for the sub-family of attempts that get
far enough to try to *extract a signed integer from an operator-algebraic or homotopy-theoretic
structure built around the primes/Kronecker flow* (docs 132, 156, 160, 161, 162, and — more
loosely — 67): in every one of these, a fully continuous/topological/character-valued layer is
constructed successfully and is proved RH-free, and ζ demonstrably re-enters at the specific step
that imposes a signed or discrete reading (orientation, Fredholmicity, replicability, or the
identification of a carrier's fundamental class). It does **not** hold universally: at least three
attempts (163's parity argument, 107_166, 114_a_38) fail for reasons that have nothing to do with
ζ — pure representation-theoretic, dimension-counting, or diagonal-collapse obstructions that kill
the route before ζ is ever in scope. So: **confirmed as the dominant mechanism among routes that
reach the invariant-reading stage; not universal, because several routes die earlier on pure
category-shape grounds.**

---

## 3. Category-changes not attempted in the corpus (candidates, with a note each)

Based on the searches run (see §4 for their limits), the following category-theoretic escapes do
not appear to have been tried anywhere in `03-research`:

- **Genuine (Bredon/equivariant) `RO(G)`-graded stable homotopy** for the Klein-four
  symmetry `⟨σ:s↦1−s, c:conjugation⟩` acting on the off-critical divisor. Doc 162 uses the group
  action only to kill `d_2` (Prop. 162.9); it never builds the equivariant spectrum itself, whose
  fixed-point/geometric-fixed-point invariants (tom Dieck splitting, equivariant Euler classes)
  are a different — and untried — reading of the same Klein symmetry. Might or might not evade
  O1–O3: it inherits the same "carrier spectrum = zero-counting distribution" problem diagnosed in
  doc 162, so it is *not* obviously safe, but it has not been tried.
- **Quillen algebraic K-theory of `Spec ℤ` directly** (`K_n(ℤ)`), as opposed to Connes' analytic
  KK-theory of a crossed-product algebra (doc 161). K-theory of the integers is a genuinely
  discrete invariant with no continuous parameter to begin with — it might sidestep the
  "orientation" node of Teorema 161.9 since there is no modular weight to canonically choose. No
  attempt in the corpus connects `K_*(ℤ)` (or higher regulators / Beilinson's conjectures) to the
  inertia invariant `m`.
- **Condensed mathematics / pyknotic objects (Clausen–Scholze)** as a replacement for the
  topological-vector-space category `D` itself. Since O1 is precisely a statement about `D` being
  a plain C-vector space with no compatible discrete structure, working in condensed abelian
  groups (which carry both continuous and discrete structure natively, e.g. `ℤ` as a condensed
  set is genuinely discrete inside a category that also holds `ℝ`) is a natural candidate for
  dissolving O1 — not attempted anywhere found.
- **Non-archimedean / Berkovich analytic geometry** over the "generic fibre at infinity"
  (as opposed to the prismatic route of doc M6, which is p-adic/local per prime). No Berkovich
  space over `Spec ℤ` or over the completed adeles is built anywhere in the corpus.
- **Full Deninger-style leafwise-cohomology "zero-carrying" object**, as opposed to the
  Kronecker-flow crossed product used in docs 160/161 (which was explicitly diagnosed, doc 160
  Prop. 160.5, as computing the *integers* `{log k}`, not the zeros). Doc 156 §4.5 and doc 161
  §5.3 both name "a triple spectral object whose Chern character gives `κ` without its zeta
  spectral function being ζ" as the central unbuilt object (`[GAP de literatura central]`) — this
  is arguably the sharpest named-but-unattempted target in the whole corpus.
- **Cluster categories / cluster algebras**, **Floer-theoretic invariants beyond the bare Maslov
  index** (e.g. Heegaard Floer or contact-geometric refinements of doc 156's Lagrangian path), and
  **motivic homotopy theory (`𝔸¹`-homotopy)** in the Morel–Voevodsky sense: none appear in the
  corpus.

---

## 4. Candid gaps in this search

- **Phase 114's I7-Witt cluster** (`114_a_36` through at least `114_a_58`, and further `_57`,
  `_58`, `_69` files) contains roughly 15 documents; only two (`114_a_36`, `114_a_38`) were read in
  full. The row header in this table for entry #12 is based on those two plus filenames only
  (several are explicitly titled `*_NO_GO.md` or `*_NOGO.md`: `114_a_37`, `114_a_41`, `114_a_42`,
  `114_a_48`, `114_a_57`, `114_a_58`). The overall shape (partial positive construction,
  operatorially closed / geometrically open, several no-go corollaries for naive transports) is
  inferred from the sample, not fully verified document-by-document.
- **Phase 49 docs 154, 155, 157** (taxonomy of averaging-crossings, "individuation defect",
  Tauberian probe) were skimmed for their opening sections only. They set up the general
  "master-quantifier" framework that doc 156 instantiates, but were not fully read for additional
  category-change sub-attempts; none surfaced in the skim.
- **Phase 65's final status is unresolved by this audit.** The phase's own `D12` audit (its most
  careful self-check) reports an candid open reduction to D8.5. Later files in the same directory
  (`RH-PROOF.md`, `D8.5-COMPLETE.md`, `D8.5d-FIXED-CHANNEL-REALIZATION.md`, three rounds of
  `CORRECTIONS-CONNES-R{1,2,3}.md`) claim the gap is closed modulo a single flagged hypothesis
  (H1). This audit did **not** read those closure documents in full — only headers/summaries —
  and could not adjudicate whether H1 is trivial (as its stated form, "`Λ≥0`," would suggest,
  which would be strange since the von Mangoldt function is nonnegative by elementary definition)
  or conceals RH-strength content (as the rest of the corpus's persistent open status for RH
  through phase 118 suggests it must). This is flagged as **the single most important item for a
  follow-up audit**: either phase 65 contains a claimed unconditional proof that the rest of the
  corpus silently ignores (a serious red flag for the programme's internal consistency), or the
  claim is unsound and should be labeled as such explicitly rather than left as an unresolved
  loose end. This audit does not resolve it and explicitly does not endorse the claim.
- **Search method for §3** ("never tried") was `grep` over `03-research` for a fixed vocabulary
  list (K-theory, topos, motive, Arakelov, Berkovich, condensed, perfectoid, derived category,
  stable homotopy, Witt theory) plus manual judgment; it is a **negative claim from absence of
  keyword hits**, not a proof of absence. A differently-worded attempt (e.g. under a personal
  name for the construction, as is common in this corpus's style) could exist and not have been
  found.
- Papers in `04-papers/` were not cross-checked against this inventory; it is possible a
  category-change route reached publication-draft form there under a different label than its
  `03-research` phase name.

---

## 5. One-line summary

Every category-change attempt that reaches far enough to try to read a signed/discrete invariant
off a continuous or operator-algebraic construction is eventually caught re-importing ζ at a
specific, named step (orientation of a KK class, Fredholmicity of an index, replicability of a
Witt-trivial vector, identification of a homotopy carrier) — five independent, fully-proved
theorems (docs 132, 156, 161, 162, 163) locate this at five closely related nodes of what doc 156
calls the existence/orientation/escape trifurcation. A smaller number of attempts (topos
cohomology, Haran-square scalar transport, prismatic cohomology) fail earlier, for reasons that
never touch ζ at all. One large package (phase 65) claims full closure in its latest documents but
this claim is not corroborated by the rest of the corpus's continued open status for RH and is
flagged, not endorsed. No route in the corpus is shown to escape O1–O3; several are shown, by
proper theorems, that they cannot.
