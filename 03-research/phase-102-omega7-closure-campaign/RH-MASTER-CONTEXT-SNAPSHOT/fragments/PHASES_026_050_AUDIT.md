# Audit of phases 26–50

## Reading conventions

- **PROVED** means a consequence proved in the document, or a correctly invoked external theorem, not
  the validity of a later bridge.
- **CONDITIONAL** includes explicit hypotheses (RH, Hypothesis D, finiteness, separation, existence of
  a geometry, etc.).
- **NUMERICAL** records only computational evidence; it does not close an analytic step.
- **EQUIVALENT-TO-RH** names an exact translation of RH, not progress toward proving it.
- **REFUTED** and **NO-GO** are useful results: they invalidate a route or a concrete premise.
- **INCOMPLETE** marks an object, estimate, or step still without proof. In particular, a proposed
  construction does not become PROVED merely by having formal definitions.

## Documentary coverage

| Phase/directory | Substantive documents reviewed | Overall status |
|---|---|---|
| 26 `phase-26-krein-connes-bridge` | `00-bridge-theorem`, `01-attack-V2` | INCOMPLETE; naive realization of V.2 refuted |
| 27 `phase-27-adelic-rigidity` | `00-setup`, `01-A-B-classification`, `02-C-wall-analysis`, `03-verdict` | EQUIVALENT-TO-RH / INCOMPLETE |
| 28 `phase-28-four-fronts` | `00-setup`, `01-front-A` … `08-decomposition-sectors` | Partial PROVED + EQUIVALENT-TO-RH |
| 29 `phase-29-zeta-spectral-triples` | `00-setup`, `01-even-simple` … `54-arithmetic-formula-of-the-deficit` (55 documents) | Partial PROVED; several EQUIVALENT-TO-RH walls |
| 30 `phase-30-langlands-bridge-c-infinity` | `55-langlands-bridge-for-automorphic-l-functions`, `56-poincar-duality-on-construction-non-degeneracy`, `57-debruijn-newman-cinfty` | Partial PROVED + direct transplant REFUTED |
| 31 `phase-31-selberg-moments-c-infinity` | `58-moments-of-and-selberg-s-theorem` | Partial PROVED / INCOMPLETE |
| 32 `phase-32-ccm` | `59-bridge-between-the-ccm-program` … `69-synthesis-of-phase-32-exact-structure` | INCOMPLETE; central criterion EQUIVALENT-TO-RH |
| 33 `phase-33-dbn` | `70-de-bruijn-newman-and-the-ccm-trace` … `89-central-object-as-synthesis` | INCOMPLETE; measure/dynamics program |
| 34 `phase-34-new-directions` | `90-direction-a-external-arithmetic-information` … `97-direction-d-third-layer-the-shadow-minimizer` | INCOMPLETE |
| 35 `phase-35-five-fronts` | `98-b-d-toy-test-an-off-critical` … `103-strict-positivity-of-and-sharpening-of-p39` | Partial PROVED; open fronts |
| 36 `phase-36-ABC-forms` | `104-effective-quantitative-degeneration` … `108-sieve-index-bridge-formulation-unconditional-inventory` | Partial PROVED / INCOMPLETE |
| 37 `phase-37-physics` | `109-critical-anchoring-principle-what-forces-0` … `113-lp-112-against-the-literature-is-there` | NO-GO and explicit dependency |
| 38 `phase-38-final-audit` | `114-adversarial-audit-of-doc-103-positivity` … `118-repair-of-the-trace-criterion-moment-rigidity` | REFUTED/REPAIRED; no RH closure |
| 39 `phase-39-G1G2-interface` | `119-forced-axioms-backward-derivation`, `120-source-inventory-of-the-connes-consani-moscovici`, `121-gap-analysis-the-cc-machinery-measured-against` | INCOMPLETE; inventory and filters |
| 40 `phase-40-close-G1` | `122-symmetry-bit-the-character`, `123-construction-of-the-cohomology-of-the-square`, `124-connes-consani-s-weil-positivity` | Partial REFUTED / INCOMPLETE |
| 41 `phase-41-build-G2` | `125-construction-of-the-intersection-form`, `126-hodge-index-on-the-square-attainable` | INCOMPLETE; circularity diagnosed |
| 42 `phase-42-hodge-dynamics` | `127-dynamical-hodge-theory-as-a-framework`, `128-deninger-s-program-is-this-the-missing` | REFUTED as a non-circular route |
| 43 `phase-43-hodge-foliated-specZ` | `129-does-the-foliated-space-of-spec-admit`, `130-circularity-to-destruction-test-of-deninger-s` | CONDITIONAL / INCOMPLETE |
| 44A `phase-44-new-mathematics/hodge-witt-and-visible-inertia` | `131-phase-44-hodge-witt-and-visible-inertia` | CONDITIONAL; new proposal |
| 44B `phase-44-new-mathematics` | `131-algebra-of-arithmetic-correspondences-the-category`, `132-defect-theory-the-category-ol-of-defective`, `133-design-by-negation-the-objects-that-violate` | Abstract internal PROVED + INCOMPLETE for ζ |
| 45 `phase-45-fredholm` | `134-weil-toeplitz-algebra-symbol-compact-ideal`, `135-two-prime-theorem-positivity-for-pure`, `136-problem-133-a-the-realizability-of-under` | INCOMPLETE; Fredholm hypothesis not established |
| 46 `phase-46-audit-and-attacks` | `137-adversarial-audit-of-the-local-purity-theorem` … `143-attack-on-problem-136-a-quantitative-localized` | REFUTED/conditioned; route audit |
| 47 `phase-47-live-fronts` | `144-attack-on-lp-141-the-minimal-finiteness` … `148-gap-135-a-exponential-frames-over-unions` | INCOMPLETE; distilled gaps |
| 48 `phase-48-audit-and-purity` | `149-adversarial-audit-of-the-139-a-revival` … `153-attack-on-conjecture-144-d-gap-144` | Partial PROVED + partial REFUTED |
| 49 `phase-49-cross-the-wall` | `154-taxonomy-of-the-average-individual-crossings-catalogue`, `155-individuation-defect-a-theory`, `156-index-maslov-probe-is-2m-an-index`, `157-tauberian-probe-does-tauberian-theory-cross` | Abstract PROVED; localized NO-GO |
| 50 `phase-50-diophantine-thread` | `158-diophantine-thread-is-the-linear-independence`, `159-destroyer-of-the-diophantine-thread` | Partial NO-GO; residual literature GAP |

## Phase-by-phase reconstruction

### 26 — Kreĭn–Connes bridge

**Goal.** Realize the Weil form as a Pontryagin space and pair its negative directions with non-real
eigenvalues of the Connes scaling generator.

**PROVED.** Kreĭn–Langer only gives an "at most" type bound for non-real pairs, once the Pontryagin
realization and the appropriate self-adjointness are given. `01-attack-V2` proves the natural character
associated with an off-line zero does not belong to the considered \(L^2\) space.

**REFUTED.** The inference "negative index ⇒ exactly that many non-real pairs" does not follow from
Kreĭn–Langer. The direct realization of V.2 by characters \(x^{b+i\gamma}\) as \(L^2\) vectors is also
refuted.

**CONDITIONAL/INCOMPLETE.** Non-degenerate completion, invariance of \(Q\), distributional or localized
extension, and the full spectral bridge remain unbuilt. The assumed finiteness of the index already
depends on hypotheses about zeros.

**Inheritance.** Passes to 27 as character non-unitarity; from there to the cohomological, Fredholm,
and index routes. Every later use of "κ=2m" must carry the realization/finiteness condition.

### 27 — local/global classification

**Goal.** Translate V.2 into adelic characters and obtain global Weil positivity from local
information.

**PROVED.** Correctly identifies the formal equivalence between V.2's functional obstacle and the
presence of non-unitary characters. Distinguishes Wall A (Euler/local information against zeros) from
Wall B (local-to-global).

**EQUIVALENT-TO-RH / INCOMPLETE.** The local-global principle and the intersection form/cohomology over
\(\mathbb Q\) that would validate it are exactly the sought content; they are not proved. The phase
delivers diagnosis, not global positivity.

**Inconsistency.** `00-setup` cites the names of four documents that do not match the three files
actually present, and lists a nonexistent fourth file. Requires ledger/index correction before citing
the sequence.

### 28 — four fronts and \(\xi\)'s curvature

**Goal.** Attack RH via DBN/Kreĭn, APS-η, \(K\)-theory, and transversal energy; then identify the
correct curvature/LP criterion.

**PROVED.** There are useful formal computations: second variation, curvature formulas, polynomial/Gamma
sector separation, and conceptual unification of fronts. The file itself corrects the initial question:
the proposed transversal concavity is false even under RH, while the condition in the \(t\) direction is
presented as the correct one.

**CONJECTURAL/CONDITIONAL.** \(\Lambda=\max b_j^2/2\), vanishing of η by anticommutation, \(KK\)
homotopy, the Hessian/global minimum, and arithmetic control of the ζ sector are not proved.

**EQUIVALENT-TO-RH.** \(\xi(1/2+it)\in LP\), \(G(t)>0\), and elimination of complex pairs are RH
criteria, not independent tools. `08` explicitly concludes that the analytic sector changes sign and the
necessary arithmetic sector is the wall.

**Re-audit required.** The curvature identities and their sign conventions (especially identifying
\(G\) with logarithmic derivatives, and the "new" statements) deserve full external cross-checking: the
corpus itself contains a sign/direction correction within the same phase.

### 29 — CCM convergence, spectrum, and deficit program

**Goal.** Turn CCM approximants and the functional \(C_\infty\) into spectral convergence, inverse
inclusion, and, finally, RH.

**Partial PROVED.** Positivity of certain kernels in the large regime, cone preservation, weak
counting/convergence, several moment identities, Jacobi/measure reductions, and non-control of some
mechanisms by spectral gap are documented. These are local results of the CCM architecture, not a
complete identification of ξ's spectrum.

**CONDITIONAL.** Individual convergence, GUE/Montgomery, linear independence, WT-measure
determination, boundary Dirichlet formulas, \(L^2\) controls, and several closures require RH, GUE,
LI, simplicity, or other assumptions.

**EQUIVALENT-TO-RH.** Inverse inclusion, absence of off-critical measure, equality of spectral measures,
sign/Poisson condition for atoms, and vanishing of \(C_\infty\) are repeatedly identified as equivalent
to or coextensive with RH.

**NO-GO/INCOMPLETE.** The moment problem does not fix the required measure; pointwise convergence of
Dirichlet series does not produce \(L^2\) control; continuous completeness does not cover the atomic
part; GUE cannot enter as a premise to prove RH. Documents 46–54 are a roadmap/proposed mathematics, not
closure results.

**Inheritance.** Leaves \(C_\infty\), the deficit measure, and the "average versus individual zero"
problem to 30–38; its circularity diagnosis governs 41–50.

### 30 — Langlands, duality, and DBN

**PROVED.** The formal generalization of the framework to a class of \(L\)-functions and the formal
construction of the proposed pairing are separable from RH. `57` obtains conditional bounds linking
Λ to deficit.

**REFUTED.** `55` corrects the false direct transfer of Deligne from function fields to \(\mathbb Q\).
`56` shows the proposed duality has a trivial degree factor and does not reproduce the Weil mechanism:
there are no nontrivial eigenvalues or norm tension forcing the critical line.

**CONDITIONAL/NUMERICAL.** The vanishing of low deficits relies on computational zero verification and
is not a global analytic proof; the bounds in `57` need uniform separation, incompatible with the
expected growing density.

### 31 — Selberg moments

**Partial PROVED.** It is isolated that average/infimum allow concluding \(\inf C_\infty(\gamma_n)=0\),
under the declared ingredients.

**INCOMPLETE.** Whether the infimum is attained is the decisive step; converging to zero along a
subsequence does not give an exact zero. The resulting criterion does not close RH.

### 32 — structural CCM

**Goal.** Connect the \(C_\infty\) limit, Jacobi/Christoffel, Stieltjes, boundary scaling, and prolate
recurrences.

**Status.** The approximation lemmas and structural formulas serve as infrastructure; document
`64-ptc-is-equivalent-to-rh-closure` records the closure criterion as EQUIVALENT-TO-RH. The asymptotics and checks
in `60`–`68` do not substitute for the required strong inclusion/convergence. `69` is a synthesis, not a
closure theorem.

### 33 — DBN, trace, and the \(d\nu\) measure

**Goal.** Make the DBN flow, the explicit formula, and Li/Nyman–Beurling criteria control a deficit
measure.

**Status.** There are formal/conditional identities and reductions; the central object \(d\nu\), its
sign, and the required completeness remain INCOMPLETE. The transfer from function fields, arithmetic
Frobenius, positivity of \(L_z\), and prime cancellation do not become an independent proof.

### 34 — new Pontryagin/variational directions

**Goal.** Extract arithmetic and second-variation information in a Pontryagin space, with inverse
problems and a shadow minimizer.

**Status.** The formulations isolate finiteness, uniqueness, and dissipation conditions; none delivers
condition C5, the inverse solution, or global uniqueness. Classification: INCOMPLETE, with conditional
conclusions assuming the Pontryagin structure.

### 35 — five fronts

**Partial PROVED.** The toy tests, the DBN/rigidity relation, and local checks separate plausible
mechanisms from failing ones.

**INCOMPLETE.** Semilocal Maslov, Fourier frames, Bagchi–Voronin, strict positivity of \(W_\lambda\), and
the two-prime couplings do not give global coercivity. This is the direct source of the 37–38 attacks
and audits.

### 36 — ABC forms

**Goal.** Seek effective degeneration, two-dimensional coupling, amplification, diagonal kernel, and a
sieve-based index.

**Status.** Reductions and form computations are obtained; uniform degeneration/positivity and the
sieve–index bridge remain INCOMPLETE. There is no RH conclusion or independent inertia finiteness.

### 37 — physics/inertia

**PROVED/NO-GO.** The documents fix the critical anchoring, inertia readers, and the "finiteness implies
vanishing" dichotomy only under the precise hypotheses. `113` confronts LP-112 with the literature and
avoids selling density or universality as an inertia reading.

**Dependency.** The L8 target and quartet finiteness are not proved; they pass as conditions to 38, 43,
and 49–50.

### 38 — final audit and repair

**REFUTED.** The audits eliminate the naive use of positivity \(W_\lambda\ge0\), Stepanov readings, and
unjustified tensor steps. `118` repairs the trace criterion only after making the block/index gap
explicit.

**Partial PROVED.** The corrections are valid as delimitation: they do not turn the repaired trace into
an RH proof. Any inheritance invoking "approximate Weil positivity" without the compact defect or
index control must be rejected.

### 39 — G1/G2 interface

**PROVED.** `119` forces a list of axioms and dependency order; `120` distinguishes what is verified in
Connes–Consani from interpretation; `121` detects forbidden uniformizations and applies
anti-circularity filters.

**INCOMPLETE.** There is still no square cohomology with an intersection/signature form. The inventory
reports duality and RR in dimension one, not the G2 signature nor a global Lefschetz result.

**Re-audit.** References flagged as unverified and negative search results must remain so; they cannot
be elevated to mathematical nonexistence.

### 40 — closing G1

**REFUTED.** `122` shows the tolerance duality is Pontryagin group-dual, not a self-form with symmetry
character; moreover the proved self-dual point is empty. It provides neither the signature bit nor
polarization.

**CONDITIONAL/INCOMPLETE.** `123` builds, subject to A1–A3, combinatorial Čech finiteness; not integer
dimension nor finiteness of the impure part. `124` separates geometric positivity from Weil positivity:
the latter is EQUIVALENT-TO-RH.

### 41 — building G2

**Partial PROVED.** `125` gives a finite toy with the correct signature and isolates candidate
correspondences/form.

**INCOMPLETE.** Integrality over the continuous flow (G-125.A) is missing and, centrally, persistence of
the signature (G-125.B). `126` explains that AHK does not apply and Babaee–Huh prevents deducing a
tropical Hodge index from generic positivity.

**EQUIVALENT-TO-RH / CIRCULAR.** Applying the signature only to ζ's correspondences falls back into Weil
positivity. An external matroid/Lefschetz-type theorem for the whole square would be the only escape,
and it does not exist in the file.

### 42 — Hodge dynamics and Deninger

**REFUTED as an independent route.** `127` identifies a structural analogy with Kontsevich–Forni, but
the scale flow with spectral content already carries primes/zeros; its curvature would be Weil
positivity. Moreover the relevant flow is isometric, not hyperbolic.

**INCOMPLETE.** `128` only programs Deninger's geometry; it does not build the required external
variation/polarization.

### 43 — foliated Hodge over Spec ℤ

**CONDITIONAL.** Polarizable Hodge theory and the circularity test specify what object would need to
exist and what its properties would be. Building such an object, its polarization, and the step from
purity to zeros remain INCOMPLETE; the test is not a substitute for construction.

### 44A — Hodge–Witt and visible inertia

**CONDITIONAL.** `131-phase-44-hodge-witt-and-visible-inertia` proves consequences within an explicitly assumed
Hodge–Witt family. The existence of \(X_\zeta\) and a pre-RH, zero-independent, external polarization is
the central wish.

**Inheritance.** Useful as a specification of a possible inertia reader; not as a proved bridge to RH.

### 44B — algebra, defect, and design by negation

**Abstract internal PROVED.** The algebra of correspondences, orbit/defect theorems, and the
negation-based taxonomy are results within the new definitions.

**INCOMPLETE for ζ.** Realization in the global object, axiom H, robust positivity, and any
identification with the Weil form depend on earlier gaps. Do not confuse decidability in
subcategories/toys with the global arithmetic case.

### 45 — Fredholm

**Goal.** Build a Weil–Toeplitz symbol, a two-prime theorem, and 133A realizability to turn a compact
defect into index/finiteness.

**Partial PROVED.** The symbol/corona/compact language and several normalization no-go results identify
where zero-to-zero information lives.

**INCOMPLETE.** Fredholmness, remainder control, repulsion/semilocality, and realizability remain gaps.
The property that would make the symbol robust against compacts is precisely the sought inertia
information; no independent index is available.

### 46 — audits and attacks

**REFUTED/CONDITIONAL.** The local-purity, two-prime, logistics, and Weil–Toeplitz audits trim several
illegitimate jumps. The attacks on LP134, 135B, and 136A find additional quantitative hypotheses, not
closures.

**Inheritance.** Fix the gaps that 47 and 48 re-attack: finiteness/pivot, spectrality,
Davenport–Heilbronn, dominance, and incommensurable frames.

### 47 — live fronts

**INCOMPLETE.** `144` leaves Conjecture 144.D and GAP-144.C; `145` does not decide spectrality; `146`
shows the Davenport–Heilbronn threat is macroscopic; `147` does not turn dominance into global control;
`148` finds the two-prime frames are not Riesz in the required regime.

**Useful result.** The files do not prove RH, but turn supposed levers into named, attackable, verifiable
gaps.

### 48 — audit, purity, and the 144.D attack

**Partial PROVED.** The audits eliminate the automatic revival of 139A and refine documents 144–148.
`152` identifies that purity/rigidity does not arise from local continuity.

**REFUTED.** `153` quantitatively kills the de la Vallée Poussin attack at \(1/2\) and corrects the
"purity ⇒ repulsion" arrow as it was formulated.

**INCOMPLETE.** 144.D is neither proved nor refuted. GAP-144.C remains, distilled to window regularity
on the prime side, plus declared embedding/selection gaps.

### 49 — crossing the wall

**Abstract PROVED.** `154` classifies transversality certificates; `155` formalizes the individuation
defect and proves that an average alone does not recover the oscillatory signal. `157` proves a NO-GO
for the local class of Tauberian conditions and uses Littlewood to refute non-oscillation.

**REFUTED/NO-GO.** `156` shows the Maslov/Toeplitz route does not evade the wall: Fredholmness already
requires finiteness of off-line zeros; even granted, computing the class counts the zeros.

**INCOMPLETE.** GAP-157.A: a non-local spectral Tauberian condition with Diophantine input. The
exhaustiveness of `154` is relative to its T1–T5 classification, not an absolute metatheorem.

### 50 — Diophantine thread

**Partial PROVED/NO-GO.** `158` proves that \(\mathbb Q\)-linear independence of \(\{\log p\}\) gives
transversality on the phase torus, but not in the inertia coordinate. `159` confirms Nyman–Beurling uses
integers, not merely primes; it kills the Bohr/Voronin ambient reading and classical quantification via
Beurling–Malliavin density.

**INCOMPLETE.** A genuine Diophantine quantification (discrepancy/irrationality) transporting phase to
inertia is not ruled out. GAP-159.C = refined GAP-157.A: no known theorem performs that transport
without reintroducing the explicit formula or zero counting.

## Dependencies and critical inheritance

```text
26 V.2 not realized
  -> 27 non-unitarity / local-global wall
  -> 28 LP-curvature criterion = RH
  -> 29–33 C_infinity, measures, and convergence: average is not enough
  -> 35–38 positivity/trace attacks and corrections
  -> 39–43 G1/G2, polarization, and Hodge: missing or circular object
  -> 44–48 new algebras/Fredholm/purity: require an inertia reader
  -> 49–50 taxonomy: average/phase do not recover inertia without new input
```

## Critical findings for re-audit

1. **There is no proof of RH in this block.** The claims that reach RH do so under hypotheses that
   already contain Weil positivity, zero localization, finiteness/Fredholmness, or an unbuilt
   geometry/polarization.
2. **Finiteness κ=2m is not a free datum.** It requires the bridge of 26 and, in the index routes, is a
   condition for the existence of the Fredholm object. It must be marked CONDITIONAL in later
   references.
3. **Phase 28 needs an external analytic audit of conventions and signs.** There was an internal
   correction of the convexity direction; the curvature criteria must be verified from ξ's definitions
   before reuse.
4. **The transfer from function fields is restricted.** 30 refutes the direct Deligne/\(\mathbb Q\)
   version; 41–43 show that invoking Hodge theory, tropicality, or dynamics is not enough without an
   external polarization for the whole space.
5. **Positivity is the common bottleneck.** If computed from the explicit formula it is
   EQUIVALENT-TO-RH; if intended geometrically, the external signature/polarization theorem is
   missing. This fork must accompany every claim about G2, Deninger, Hodge–Witt, or Fredholm.
6. **The later no-go results are partial, not an absolute closure.** 49–50 close local classes,
   average/value, and density-based quantification; they leave the phase→inertia Diophantine GAP as a
   literature gap, not a proved impossibility.
7. **Phase 27's metadata is inconsistent.** Correct the names/listing before using it as a dependency
   ledger.
8. **Citations and negative searches flagged by the documents themselves remain unverified.** In
   particular, do not turn an absence of localized results into a claim of nonexistence.
