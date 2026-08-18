# Papers

Publication-ready preprints by David Alejandro Trejo Pizzo (`dtrejopizzo@gmail.com`), independent
researcher. This is the single index for the corpus — the three older `.md` indices it replaced
are gone; this file is now the only source of truth.

**No paper in this corpus claims a proof of the Riemann Hypothesis.** The corpus is a set of
rigorous partial results, reformulations, no-go theorems, and — in papers **36** and **42** — two
independent, structurally different reductions of RH to a single classical open input. Paper 36
reaches the Li–Keiper criterion via a fifteen-step arithmetic Pick/Nevanlinna chain (phases 0–76).
Paper 42 imitates Weil's own 1948 method for curves over finite fields directly over
$\operatorname{Spec}\mathbb Z$ (phases 107–119); its row (d) is proved equivalent to RH twice,
independently — algebraically (phase 113) and analytically, verified against real zeta zeros
(phase 118). Read the "Key content" column below before citing any single paper out of context.
See [`../OPTIONS.md`](../OPTIONS.md) for where the corpus's own audit says work can still usefully
continue.

## How to read this table

- **#** — publication order. Folder names carry this number as a prefix; it is publication order
  only and never appears inside any `.tex` source.
- **Depends on** — which earlier papers (by #) are cited in the body and therefore must already
  have an arXiv id before this one is submitted. A blank means the paper is self-contained.
- **arXiv** — filled in as each paper is posted; see "Publication flow" below.

| # | Folder | Title | Type | Depends on | Key content | arXiv |
|---|--------|-------|------|------------|--------------|-------|
| 01 | `01-critical-line-survey` | The Critical Line: A Survey of Recent Progress on the Riemann Hypothesis | **Survey** | — | Frames the whole program: state of the art across the analytic, spectral, and algebro-geometric approaches; the thesis that every front reduces to a positivity condition. |
| 02 | `02-omega-class-decomposition` | The ω-Class Decomposition of Dirichlet Polynomials: A New Framework for the Lindelöf Hypothesis | Original result | — | ω-class decomposition of Dirichlet polynomials; $B(N)\le N^\varepsilon\Rightarrow$ Lindelöf (a sufficient, plausibly-stronger-than-LH condition); moment-exponent fingerprint. |
| 03 | `03-sign-interclass-interference` | On the Sign of Inter-Class Interference in Dirichlet Partial Sums: A Peak–Trough Reconciliation | Original result | — | The conditioning correction: inter-class interference $r$ is constructive at peaks, destructive at troughs, mean zero. Prerequisite consistency note for 04. |
| 04 | `04-davenport-heilbronn-null` | Absence of Power-Law Growth in Partial Sums of the Davenport–Heilbronn Function at Off-Line Zeros | Original result | 03 | Candid null result: no power-law growth at off-line DH zeros up to $N=10^9$; converts into an onset-scale lower bound $N^*\gtrsim10^{14}$. |
| 05 | `05-omega-hierarchy-chaos` | The ω-Class Hierarchy of the Riemann Zeta Function: Per-Prime Weights, Multiplicative Chaos, and the Branching Structure of the Maximum | **RH-independent** | — | Structural dictionary $z=\beta^2$ linking the moment exponent, multiplicative-chaos freezing, large deviations of $\omega(n)$, and a branching-random-walk picture of the maximum. |
| 06 | `06-why-rh-resists` | Why the Riemann Hypothesis resists: a classifier for zero-absence mechanisms, the finite-to-full positivity gap, and a finitization obstruction under linear independence | Structural | — | Conceptual classifier $D_0$; identifies the finitization-under-linear-independence obstruction common to the finite-dimensional routes. |
| 07 | `07-localized-weil-detector` | A Rigorous Localized Weil Detector for Off-Critical Zeros: Forced Negativity, Unconditional Truncation Control, and the Logical Status of the Truncation Lemma | **Flagship** | — | The localized Weil quadratic form $Q$; forced negativity with explicit constants; unconditional truncation control (PNT only). Names the RH-equivalent inequality precisely. |
| 08 | `08-weil-krein-realization` | A Faithful Kreĭn-Space Realization of the Weil Quadratic Form, with a No-Go Theorem for the Zero-Side Attack on Positivity | Structural | — | Semibounded self-adjoint realization collapsing the program to one axis ($\mathrm{RH}\iff\|K\|\le1$); no-go theorem: the zero side alone cannot decide the sign. |
| 09 | `09-stable-arithmetic-fingerprints` | Stable Local Arithmetic Fingerprints from Localized Weil Forms | **RH-independent** | 07 | Autonomous stability theorem: $Q(L)$ and its per-prime profile are exponentially stable functionals of the small-prime arithmetic. |
| 10 | `10-anatomy-local-invariant` | The localized-Weil anatomy as a complete local invariant of $L$-functions: Euler products, Satake recovery, and functoriality | **RH-independent** | 07 | Euler product $\iff$ factorizing anatomy (proved converse); GL($n$) Satake recovery, functoriality, GL(1)/GL(2). |
| 11 | `11-pontryagin-index-finite-defect` | The off-line zeros as a Pontryagin index: a tail relative-form-bound reduction, and two computations closing the finite-defect route | Negative/structural | 08 | Closes the finite-defect route computationally; three-regime classification of the index $\kappa$. |
| 12 | `12-band-limited-weil-carleson` | The Band-Limited Weil–Carleson Form: a saturated positivity constant, its sine-kernel second order, and a five-language map of the Riemann wall | Consolidation | 07, 08, 09, 10 | Carleson saturation theorem; sine-kernel second order = Montgomery pair correlation; the five-language map of the positivity wall. |
| 13 | `13-heat-flow-lyapunov` | A Lyapunov Theorem for the de Bruijn–Newman Flow, a Dynamical No-Go, and the Extremal Form of the Riemann Hypothesis as Gap Universality | Consolidation | 12 | Lyapunov theorem for the dBN flow (critical line = attractor); dynamical no-go (flow is arithmetic-blind); RH as an extremal GUE-gap-universality statement. |
| 14 | `14-modern-routes-wrong-sign` | Two Modern Routes to the Riemann Hypothesis and the Robustness of the Wrong-Sign Obstruction: the Hodge-index and hyperbolicity reformulations | Consolidation | 12, 13 | Hodge-index and Jensen-polynomial hyperbolicity reformulations both pursued to their foundation; the wrong-sign obstruction confirmed across eight paradigms. |
| 15 | `15-finite-to-full-uniformity` | Finite-to-full positivity is a uniformity gap: a criterion, a Hodge–Riemann stability theorem for towers, and the place of ζ | Analysis | 06, 14 | Uniformity criterion; Hodge–Riemann stability theorem for towers, generalizing prior finite-dimensional results to families. |
| 16 | `16-unconditional-finite-bottom` | An unconditional finite bottom for the localized Weil form: a verified second-moment identity, an almost-everywhere clean bound, and the residue as a uniform short-interval prime variance | Sub-RH theorem | 11 | Verified second-moment identity; a.e. clean bound off a super-sparse exceptional set; residue = uniform short-interval prime variance (non-circular). |
| 17 | `17-lefschetz-dichotomy` | The Lefschetz dichotomy: why the hard-Lefschetz route to the Riemann Hypothesis is obstructed by linear independence | Structural no-go | 06, 08, 11, 14, 16 | First explicit $\mathcal T$-independent hard-Lefschetz $\mathfrak{sl}_2$ on the continuum; the dichotomy theorem: linear independence forbids an HR-carrying grading on the zeros. |
| 18 | `18-localized-weil-krein-index` | The localized Weil form and its Kreĭn–Pontryagin index: localization, obstruction, and rigidity | Structural | 19 (companion; 18 published first) | Fuses the off-axis evaluation localization, the bilinear/sesquilinear classification, the positive-kernel obstruction theorem, and structural rigidity of any finite-defect realization into one paper. |
| 19 | `19-arithmetic-defect-offline-zeros` | The arithmetic defect of off-line zeros: parity, the modified explicit formula, and two-scale structure | Structural | 18 | Parity/angular-separation theorem $\kappa=2m$; modified explicit formula; two-scale (x-scale growth / t-scale depression) barrier theorem. |
| 20 | `20-herglotz-criterion` | The Riemann Hypothesis as a Herglotz positivity: $\Re\,\xi'/\xi>0$ in the right half-plane, an unconditional boundary identity, and the Hilbert–Pólya reformulation | Reformulation | 08, 11, 14, 17, 18 | Cleanest analytic form of the de Branges criterion; unconditional boundary identity $\Re\,\xi'/\xi(\tfrac12+i\tau)=0$ from the functional equation alone. |
| 21 | `21-omega-information-barrier` | An exact information barrier in the ω-class: the unique RH-sensitive window and the impossibility of algebraic cancellation | **RH-independent** | 01, 09 | Closes the ω-class program: the unique RH-sensitive window in the ω-class, and a theorem that positivity of $q^{\omega(n)}$ forbids algebraic cancellation of zeros. |
| 22 | `22-moment-rigidity-criterion` | The Riemann Hypothesis as moment rigidity over Meixner–Pollaczek polynomials | Reusable criterion | — | Standalone: RH $\iff$ $\Delta_n$ constant, via Carleman and Hardy-space moment rigidity. Cited by 23 and 24. |
| 23 | `23-ccm-jacobi-incidence-equivalence` | A Jacobi-operator spectral-triple reformulation of the Riemann Hypothesis and the incidence equivalence | Spectral-triple | 22 | Self-adjoint Jacobi operators $D_\lambda^N$ and their limit operator; full bidirectional equivalence RH $\iff$ incidence invariance; a complex-zero-free region $\mathrm{Im}>\tfrac12$. |
| 24 | `24-trace-measure-criterion` | A trace and measure criterion for the Riemann Hypothesis from the zeta spectral triple | Spectral-triple | 22 | The measure $d\nu\ge0$, $d\nu=0\iff$RH; eight equivalences; a trace lower bound; the Hadamard barrier. |
| 25 | `25-bridge-theorem` | Pontryagin spectral index of the Weil form and the Connes scaling operator: a bridge theorem for the Riemann Hypothesis | Bridge | — | The bridge identity $\kappa(Q)=\mathrm{neg.ind}(H_C)$ connecting the Weil-form index to the Connes scaling operator. |
| 26 | `26-weil-toeplitz-logistic-criterion` | An operatorial geometry for ζ: the Weil–Toeplitz algebra and a logistic criterion for the Riemann Hypothesis | New framework | 18, 24, 25 | Defect spaces and the Weil–Toeplitz field; criterion $\mathrm{RH}\iff\lim\sigma_{\mathrm{loc}}^{(k)}=0$, with $\mathrm{RH}\Rightarrow 0$ a theorem and the converse flagged open. |
| 27 | `27-exhaustion-1d-propagation` | The exhaustion of one-dimensional propagation: a structural no-go for the Riemann Hypothesis, and two directions that survive it | Structural no-go | 18, 24, 25 | Structural no-go for the one-dimensional propagation route; identifies exactly which two forms survive it. |
| 28 | `28-amplification-survivor` | Two closures and a survivor: the amplification route to the Riemann Hypothesis through almost-prime sieve bounds | Structural | 24, 25, 27 | Two of the three forms from 27 are closed; the amplification form survives, bridged to almost-prime sieve bounds. |
| 29 | `29-master-quantifier` | One wall in many coordinates: closure of the propagation trichotomy and the master quantifier for the Riemann Hypothesis | Synthesis | 24, 25, 27, 28 | Unifies the walls found in 27–28 into a single master quantifier; value vs. inertia distinction. |
| 30 | `30-two-lemma-architecture` | Finiteness and rigidity: a two-lemma architecture for the Riemann Hypothesis | Architecture | 24, 25, 27, 28, 29 | $\mathrm{RH}\Leftarrow(m<\infty)\wedge\text{rigidity}$; the closing dichotomy theorem of the CCM/Pontryagin arc (27–30). |
| 31 | `31-curvature-lp-synthesis` | A curvature criterion for the Riemann Hypothesis and the unification of four analytic frameworks | Synthesis | — | Explicit Hadamard curvature formula; $\mathrm{RH}\iff\mathcal C(\gamma)>0$; unifies four analytic frameworks (de Bruijn–Newman, APS, K-theory, transversal energy) as equivalent to $\xi(\tfrac12+it)\in\mathrm{LP}$. |
| 32 | `32-stepanov-band` | The Riemann zeta function is not Stepanov almost periodic in any sub-strip of the critical strip | **RH-independent** | — | Standalone unconditional theorem: $\zeta$ fails Stepanov almost-periodicity in the band sense on every sub-strip. |
| 33 | `33-energy-decomposition` | An Energy Decomposition of the Riemann Hypothesis: the Off-Line Energy $I$, its Integral Representation, and Structural Barriers | Capstone | — | $\mathrm{RH}\iff A\wedge\mathrm{Dic}$ with $I=\sum b_j^2$; unconditional bound $E(T)\ll T/\log T$; energy dichotomy; several structural barriers to closing $A$. |
| 34 | `34-architecture-of-obstruction` | The Architecture of Obstruction: A Complete Mathematical Map of the Riemann Hypothesis Program: from ω-Class Statistics to the Symmetry/Positivity Wall | **Survey** | 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 16, 17, 18 | The full obstruction map: every approach catalogued in this corpus, its precise logical status, and where it stops. The pre-Pick synthesis that **36** builds on and supersedes as the final ledger. |
| 35 | `35-colligation-route` | The Colligation Route to the Riemann Hypothesis: de Branges Realization, a Curvature Theorem, and the Pole-Pinned Spectral Radius at the Wall | Reformulation | — | de Branges/Lax–Phillips colligation; curvature theorem $\Gamma_2\ge0$; crystallizes RH as the *sign* $\varepsilon_0\ge0$ — the one quantity invisible to all Doob/scale-invariant structure. |
| **36** | `36-obstruction-ledger` | The Riemann Hypothesis: An Obstruction Ledger and the Arithmetic Pick Architecture It Shaped | **Culmination** | — | **The current endpoint of the program.** A fifteen-step arithmetic Pick/Nevanlinna chain (ARP-P) reducing RH to one open input: the classical Li–Keiper criterion $\lambda_n\ge0$. Fourteen of fifteen steps are fully closed; catalogues the structural walls blocking every other route in this corpus and assigns each a precise logical status. Already on arXiv. |
| 37 | `37-death-of-the-positivity-family` | The Limits of the Positivity Family in the Li–Keiper Route to the Riemann Hypothesis | Structural no-go | 36 | Audits the adaptive-cutoff margin, records exact witnesses against sixteen positivity transfers, and isolates density-relaxed and signed non-local successors without claiming their missing arithmetic estimate. | — |
| 38 | `38-li-fir-stability` | The Li Sequence as a Sampled Control System: FIR Window Stability, Off-Line Modes, and the Arithmetic Closure Problem | Structural/control reformulation | — | Maps critical zeros to unit-circle modes and off-line zeros to unstable modes; proves fixed-window, cascaded-FIR, adjacent-bank energy, eventual-window-positivity, vanishing-trim and geometric-rate criteria; gives the exact prime–Laguerre FIR lift and isolates the unproved ordinary-prime dissipativity estimate. | — |
| 39 | `39-cofinal-weil-summability` | Cofinal Weil Quotients: Exact Transport Defects, Fixed-Cutoff Summability, and the Global Curvature Gate | Spectral/operator analysis | — | Builds canonical cross-level maps for the CCM radical quotients; derives the exact rank-two/Loewner transport defect, scalar Cauchy-trace formula, cofinal fixed-cutoff summability, shell reduction, divisor rigidity, bilateral negative tests, the moving co-Poisson gate, the centered prime--Gamma jump square, and the exact PNT-discrepancy compensation formula. | — |
| 40 | `40-connes-proof-skeleton` | Branch Selection and Global Polarization in the Connes–CCM Route to RH: Finite Prime–Gamma Inertia, Tate Boundary Geometry, and the Divisor-Sensitivity Obstruction | Spectral/operator analysis | 39 | Joint prime–Gamma finite-source refinement removing finite-selection, tail, and form-core losses; identifies the local geometric data (a cyclic root Laplacian) the surviving sign was trying to express; isolates the remaining sign as a strict physical source surplus over an anti-shorted deficit. | — |
| 41 | `41-obstruction-catalogue` | Obstructions to Weil Positivity: A Catalogue of No-Go Theorems, Falsifiers and Countermodels in the Prime–Gamma Doob Coordinate | Structural no-go catalogue | 40 | Companion to 40: does not attempt the surviving inequality, but records thirty-one mechanisms across eight families (order/total positivity, coupling/transport/martingale, local squares and Hodge–Korn completions, determinants, finite heads, spectral/operator detectors, realization/factorization rigidity, semilocal branch selection) which provably cannot prove it, each classified as a no-go, a conditional falsifier, or a countermodel. | — |
| **42** | `42-arithmetic-lefschetz-programme` | An Arithmetic Lefschetz Programme over $\Z$: A Metrized Bivariant Correspondence Square, its Determinant Pairing and its Corner Trace | **Culmination (Arc C)** | — | **The second current endpoint of the program.** Constructs rows (a)–(c) of Weil's own 1948 method directly over $\operatorname{Spec}\mathbb Z$: a noncollapsed spherical square with periodic section cohomology, a faithful Witt–Frobenius correspondence family of degree $\Lambda(n)$, and the complete nuclear Lefschetz character in Meyer's Poisson quotient. For row (d), gives the primitive operator a balanced channel factorization, proves full-space positivity for $0<T\le\log2$ unconditionally, and proves the threshold condition equivalent to a unit capacity bound — then proves that bound **equivalent to RH**, independently, twice: algebraically (phase 113, inside the corpus) and analytically, verified against real zeta zeros to $10^{-10}$ relative precision (phase 118). |

## Surveys vs. results

Two papers are surveys rather than original-result papers, and should be read as maps, not
theorems: **01** (early framing — state of the art as of the start of the program) and **34** (the
mid-program obstruction map, once the corpus had grown large enough to need one). **36** and **42**
are neither surveys nor single results: they are the corpus's **two culminations**, reached by
independent constructions. **36** takes every wall catalogued across 01–35 and shows they all
terminate at the same open input (Li–Keiper positivity). **42** is Arc C — a direct, Weil-style
construction over $\operatorname{Spec}\mathbb Z$, built in phases 107–119, whose own open input
(row d) is shown equivalent to RH by two unrelated methods inside that construction. **37**–**41**
continue **36**'s Li–Keiper route (37, 38, 39 pushing the architecture further; 40, 41 the
Connes–CCM branch-selection route and its own catalogue of obstructions) without superseding it.

## Candor

Per the program's governing principle, **no paper claims a proof of RH.** Several papers are
explicitly negative or no-go results; several are RH-independent theorems that stand on their own
regardless of RH's truth (05, 09, 10, 21, 32). Papers 36 and 42 both state plainly that their open
input, being equivalent to RH, carries the full difficulty of the Hypothesis — closing nothing, but
locating precisely where the corpus still needs one classical positivity statement, reached by two
structurally unrelated routes. See [`../OPTIONS.md`](../OPTIONS.md) for the sub-RH targets the
corpus's own audit found and never closed.

## What was archived or removed

- `P51-riemann-hypothesis-proof/` and `P52-riemann-proof-audit/` were unified into **36** and are
  no longer part of the corpus.
- `NOTE-CC-specification/`, `NOTE-CC-spectral-gap/` (private notes addressed to the
  Connes–Consani–Moscovici program) and `roadmap-rh/` (an internal navigation diagram) were removed;
  their content is superseded by **34** and **36**.
- `00-INDEX.md`, `00-PUBLICATION-INDEX.md`, and `CONSOLIDATED-INDEX.md` — three overlapping,
  partially stale indices from earlier renumberings — are superseded by this file and were deleted.

## Publication flow

1. Publish in ascending order (01 → 42); dependencies in the table above tell you what must
   already have an arXiv id before a given paper is submitted.
2. When each arXiv id arrives, paste it into the **arXiv** column above.
3. Update the corresponding bibitem in every later paper that cites it (replace "preprint, 2026"
   with the arXiv reference) before submitting that later paper.
4. **18** and **19** are companions: **18** is published first; its `Defect` bibitem reads
   "companion paper" until **19** has an id, then gets updated.
5. **36** is already on arXiv.
