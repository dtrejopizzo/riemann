# Audit of RH7–RH9: local detector, stability, and geometry

## Scope and legend

The three READMEs, all `OVERVIEW.md` files, and, when they supplied material evidence, the associated
CSVs, notebooks, and specifications were reviewed. The label expresses the claim's exact scope, not its
aspiration.

| Label | Operative meaning |
|---|---|
| **PROVED** | Identity, reduction, or bound proved in finite space with explicit hypotheses. |
| **CONDITIONAL** | Depends on a mathematical hypothesis, an unbuilt identification, or a complete external specification. |
| **NUMERICAL** | Reproduced on data, a finite mesh, or an implementation; not an asymptotic theorem. |
| **CONJECTURAL** | Architecture, extrapolation, or research route. |
| **REFUTED** | The tried formulation fails, is inconsistent, or lacks sufficient data for the claimed use. |
| **EQUIVALENT-REFORMULATION-OF-RH** | Swaps RH for a condition that, if true, already contains the positivity or the uniform step deciding RH. Supplies no independent proof. |

## RH7 — Local detector of the Weil quadratic form

**Goal and method.** Build a localized form
\(Q=M_{\rm zeros}-M_{\rm arith}\) in a Hermite–Gauss basis, validate it on \(\zeta\),
\(L(\chi_4\bmod 5)\), and \(L(\Delta)\), inject shifted-zero quartets, measure \(\lambda_{\min}\), and
separate an off-line zero's signal from the error of cutting primes and zeros. The correct dependence is
on \((T_0,\sigma,J,X,H)\); any reading that suppresses it is out of scope.

### Closed results and evidence

- **[PROVED, finite]** The Taylor expansion of the synthetic quartet model gives an order-\(\delta^2\)
  term and a real symmetric low-rank operator built from \(\phi,\phi',\phi''\). The algebraic part of
  this claim is finite-dimensional, once the quartet convention, basis, and zero list are fixed.
- **[NUMERICAL]** `task32` compares the sum operator's minimum against the simulated surface at 60
  cells and reports \(R^2\) rounded to one; `task31` contrasts it at another center. This is very
  strong evidence that the code and the expansion use the same convention, not a proof about an unknown
  real zero nor about the infinite functional.
- **[NUMERICAL]** The engine passes trace controls in the regimes declared solved; `task20` gives for
  \(L(\Delta)\) a trace residual near machine precision after raising the cutoff and repairing the zero
  data. `task40` provides the \(\zeta\) control. This validates concrete assembly instances, not an
  independent implementation nor a uniform identity across the family.
- **[PROVED with finite scope / NUMERICAL in calibration]** The Hermite–Gauss product transform has a
  Gaussian tail and allows bounding the arithmetic tail by absolute values using an explicit bound for
  \(\psi(x)\). `task34` and the README compare that envelope with seven values of \(X\). The observed
  correlation and slack factor are **NUMERICAL**; to call the integral a bound, the approximate PNT
  density must be replaced by an explicit inequality, keeping all constants.
- **[NUMERICAL]** The detectability tables (`task15`, `task18`, `task21`) estimate when \(c\delta^2\)
  beats an observed floor. They interpolate in \(J\), take seven prime cutoffs, and, at one point, reach
  the floating-point floor: these are design rules, not certified mathematical thresholds.

### Dependencies, open points, and logical status

| Claim | Status | Audit |
|---|---|---|
| Step from a synthetic perturbation to negativity of the finite model | **PROVED** | Valid only after fixing the quartet convention and the basis operator. |
| \(\delta^2\), locality, and amplification in \(J\) for the run meshes | **NUMERICAL** | The shifted zeros are fabricated data; there is no uniform control as \(J\) grows. |
| Validation of \(Q\) for \(\zeta\), a complex character, and \(\Delta\) at control points | **NUMERICAL** | A trace match does not by itself certify every entry or other normalizations. |
| Prime tail with the Hermite–Gauss basis | **PROVED** if formulated with an explicit Chebyshev/PNT bound; **NUMERICAL** for the fitted constant | Substituting the discrete sum by a density is not, by itself, a proof of a bound. |
| Zero tail and uniform convergence of \(Q_X\) to \(Q_\infty\) in the decisive regime | **EQUIVALENT-REFORMULATION-OF-RH** | This is precisely the step that would let finite negativity transfer to global Weil positivity. It was not proved. |
| "The detector proves RH if it never sees negativity" | **REFUTED** | A finite search does not cover every center, width, order, height, or shift. |

### Errors, retractions, and no-go

- **Davenport–Heilbronn:** the absolute reference value is not reproducible with the available
  information. A single definition of the arithmetic sequence analogous to \(\Lambda\) is missing, and a
  linear combination of \(L\)-functions does not allow combining derived logarithms term by term.
  `task11`, `task24`, and `task41` force its withdrawal as a quantitative control. It remains only as a
  qualitative contrast: **REFUTED** for numerical calibration.
- **\(L(\Delta)\) normalizations:** `task2`, `task12`, and `task17` discard the tried factor-of-two
  corrections. The initial trace and zero-list failures (`task4`, `task5`, `task8`, `task23`, `task36`,
  `task37`) were partly overcome by `task20`, but must not be mixed with the final result.
- **Zeros of \(\Delta\):** the fixed-cutoff integrator lost zeros; some initial lists contain doubtful
  entries. Only the verified lists and the later refinement protocol may feed a quantitative claim.
- **Non-self-dual character:** the initial formula had a phase bias. RH7 uses a correction with the real
  part; RH8 adopts a symmetrized formulation. Numbers must not be transferred between the two without
  fixing exactly the zero side, conductor, gamma terms, and conjugation convention.
- **Documentary inconsistency:** the perturbative-operator formula written in RH7's synthesis does not
  literally match the one derived in `task32`. The canonical formula must be reconstructed from the
  expansion and verified against the CSV before being cited as a theorem.
- **Law fits:** seven values of \(X\) do not identify a "zero-density regime". `task9` acknowledges
  overfitting; hence its inference about the weaker hypothesis is **REFUTED** as a logical deduction,
  even though the fit is a useful datum.

### Inheritance and route not to repeat

RH8 inherits an engine that must be specified, with a validated zero list and a cutoff dependent on
\(\sigma,J\). It leaves a single analytic task for any continuation: a norm inequality simultaneously
controlling prime tails, zero tails, and numerical error over an explicit parameter class. Do not
repeat: turning empirical fits into arithmetic hypotheses, using Davenport–Heilbronn quantitatively, or
confusing the synthetic \(\Delta Q\) with a proof about \(Q_\infty\).

## RH8 — Basis stability and localization monotonicity

**Goal and method.** Study, across the three controls, the stability of
\(\lambda_{\min}(Q(T_0,\sigma,J))\) as \(J\) grows (H1) and its response to \(\sigma\) and nested zero
windows (H2). The program reuses RH7's engine, imposes a trace gate before interpreting an eigenvalue,
and quantitatively excludes Davenport–Heilbronn.

### Audited result

- **[NUMERICAL]** In domains where the trace passes the gate, the available curves for \(\zeta\),
  \(L(\chi_4\bmod5)\), and \(L(\Delta)\) approach the numerical floor as \(J\), \(\sigma\), or the zero
  window widen. `task4`, `task9`, `task14`, and `task17` are pointwise controls; `task1`, `task16`,
  `task19`, `task25`, and `task27` give H1's meshes.
- **[NUMERICAL]** H2 is supported in the solved regime: `task2`, `task20`, `task21`, and `task26` find
  no obstruction pattern under window widening. This is absence of a counterexample on a finite mesh,
  not a proved variational monotonicity.
- **[NUMERICAL / implementation correction]** `task3` replaces the non-self-dual formula with the
  symmetrized form combining character and conjugate, and removes the \(X\)-independent residual. This
  is a necessary correction for this implementation; it does not prove that every complex-character Weil
  generalization has been uniquely normalized.
- **[REFUTED in the computed domain]** At \(\sigma=0.5\) and accessible cutoffs, the trace gate does not
  close; `task6` even observes growth of the defect. The H1/H2 curves there are not spectral evidence.

| Claim | Status | Limit |
|---|---|---|
| H1 for finite \(J\), solved \(\sigma\) and \(X\) | **NUMERICAL** | Does not prove the limit \(J\to\infty\), nor uniformity outside the sampled centers. |
| H2 in nested windows and solved widths | **NUMERICAL** | There is no theorem of form ordering or monotonicity for every test. |
| H1/H2 at \(\sigma=0.5\) with the available cutoffs | **REFUTED** as a spectral reading | Arithmetic truncation dominates. |
| "Finite stability or monotonicity implies RH" | **REFUTED** | The design itself forbids it; it also depends on the transition to the full functional. |
| Sufficient scaling of \(X\) for the whole \((T_0,\sigma,J)\) family | **CONDITIONAL** | Practical frontiers were measured, not a proved uniform law. |

**Dependencies and inheritance.** RH8 depends directly on RH7's local validity; its durable
contribution is methodological: do not interpret \(\lambda_{\min}\) without a trace residual, and
separate three regimes: validated, recoverable by raising \(X\), and inaccessible with the current
cutoff. It passes forward an admission condition for every numerical exploration, but no new route
toward RH.

**No-go and corrections.** Do not reuse the results of `task8`, `task10`, `task12`, `task13`,
`task22`, and `task23` as validations: they record incomplete implementation, missing data, or
computational limits. Nor should the symmetrized correction be presented as if it automatically
reconciled RH7's earlier conventions. The correct route is to fix a single mathematical specification,
add independent verification of matrix entries, and prove a tail bound before claiming asymptotic
H1/H2.

## RH9 — Arithmetic surface and Lefschetz structure

**Goal and method.** Seek a geometry independent of the spectrum that produces an absolute surface
\(S\), a diagonal \([\Delta]\), a Lefschetz triple, and a Hodge–Riemann form linked to Weil's criterion.
Three routes are investigated: Arakelov/\(\lambda\)-rings, prismatic/TC theory, and noncommutative scale
geometry; spectral statistics are also used as a design constraint.

### Overall verdict

\(S\), \([\Delta]\), a cohomology with spectral \(H^1\), and a triple \((L,\Lambda,H)\) passing G1–G4
were not built. The program is valuable as a map of incompatibilities and requirements, but not as
demonstrable progress toward RH. The initial reduction declaring that the existence of G1–G4 is
equivalent to RH must be catalogued **EQUIVALENT-REFORMULATION-OF-RH** until an independent proof of the
reduction is supplied and, above all, a construction that does not encode the zeros.

### Routes, results, and dependencies

| Route | What remains | Audited status |
|---|---|---|
| Arakelov and \(\lambda\)-rings | There are Chern classes, intersections, arithmetic Hodge indices, and Adams gradings in existing contexts. Metric variation suggests independence from a zero-defined operator. | **CONDITIONAL / CONJECTURAL.** The absolute object, the map to \(\Pi^\perp\), the diagonal, \(\Lambda\), a common space to prove \(L\notin W^*(T)\), and the identification of arithmetic positivity with the required form are missing. |
| Prismatic theory, TC, and Sen theory | Local Frobenii, Nygaard filtrations, and local comparisons are real tools; the literature supplies no global generator with the zero spectrum. | **CONJECTURAL** as scaffolding; the absence of an object in the survey is not a universal refutation. G1, G3, and G4 remain open. |
| Scale, adeles, and prolate/Sonin theory | Scale dynamics produces the trace structure and \(\log p\) weights of primitive orbits. The relevant generator is non-compact and its examined realizations do not give the required minimal-weight integer grading. | **CONDITIONAL** as an obstruction: it is solid for the specified representations and domains, but does not prove a no-go for every noncommutative geometry. |
| \(\Delta_3\) statistic | CSVs and notebooks record a plateau near \(0.1908\) for a zero sample and its difference from finite/infinite GUE. | **NUMERICAL.** It is a phenomenological constraint for a future model, not a cohomological identity. |

### Open points, circularities, and retractions

- **G1:** there is no proved identification between geometric cohomology and \(\Pi^\perp\), nor a
  Frobenius with spectrum \(\gamma_\rho\). Variable metric versus fixed spectrum is heuristic evidence of
  independence, not a certificate of membership in a von Neumann algebra without a common
  representation.
- **G2:** Adams gives rationalized integer weights, but not the Cartan operator of a Lefschetz
  \(\mathfrak{sl}_2\). The abelian-variety cases use duality and a Poincaré kernel absent for
  \(\mathrm{Spec}\,\mathbb Z\). A prolate triple with a continuous scale generator does not satisfy the
  requirement.
- **G3:** imposing \([T,L]=cL\) within the zero basis again asks for arithmetic translations of the
  spectrum. The argument is conclusive for bounded operators under suitable domain hypotheses; for
  unbounded operators the notebooks and reviews only give a domain warning, not a general theorem.
- **G4:** the arithmetic Hodge index is a source of positivity in its own context, but its primitive
  part has not been identified with that of Weil's criterion. If positivity is defined using the signs
  of off-line zeros or is equivalent to \(Q\succeq0\), it is circular and remains
  **EQUIVALENT-REFORMULATION-OF-RH**.
- The proposed prime-sum formula explaining the plateau, containing \(\sum_{p,k}(\log p)^2/p^k\),
  diverges; `task14` discards it. Only a formula with a dynamic cutoff and a full derivation may be used:
  the literal formula is **REFUTED**.
- The computations in `task14`, `task36`, `task46`, `task59`, and `task70` are exploratory and contain
  unfolding, GUE, and semiclassical approximations. They cannot be turned into a theorem of scale
  absence, linear independence, or the existence of a geometric constant.
- The bibliography in the `OVERVIEW.md` files is orientation evidence. Before turning any of its claims
  into a mathematical dependency, primary sources, hypotheses, and notation must be verified; the
  summaries do not substitute for that verification.

### Inheritance and route not to repeat

The useful inheritance is a set of gates: independence from \(W^*(T)\), a genuine integer grading, a
global operator with the correct spectrum, and positivity that does not restate RH. No route should
begin by defining \(L\) from moments or zeros, invoke a surface over \(\mathbb F_1\) as existing,
confuse local Frobenii with the global spectrum, or infer a Lefschetz triple from spacing statistics.
The legitimate next step is to pick a single already-built geometric category and prove a concrete piece
of G1–G4 without identifying it in advance with RH.

## Directory coverage

| Program | Directories covered | Evidence type and fate |
|---|---|---|
| RH7 | `task1, task3, task7, task13, task14, task27, task30, task33, task38, task39, task43` | No substantive answer; do not support conclusions. |
| RH7 | `task2, task4, task5, task6, task8, task11, task12, task17, task23, task24, task25, task26, task28, task35, task36, task37, task40, task41, task42` | Engine, normalization, data, and limit diagnostics; several are withdrawn or replaced by later validations. |
| RH7 | `task9, task10, task15, task16, task18, task19, task20, task21, task22, task29, task31, task32, task34` | \(\delta^2\) signal, tails, detectability, and final validations; a mix of finite and numerical results, per the table above. |
| RH8 | `task7, task8, task10, task12, task13, task15, task22, task23, task24` | No closure or insufficient implementation/data; excluded as H1/H2 evidence. |
| RH8 | `task4, task9, task14, task17` | Trace gates and pointwise controls: numerical assembly evidence in the solved regime. |
| RH8 | `task1, task2, task3, task5, task6, task11, task16, task18, task19, task20, task21, task25, task26, task27` | H1/H2 curves, cutoff sweeps, and the non-self-dual correction; exclusively numerical, regime-dependent evidence. |
| RH9 | `task1–task13` | Review of Arakelov, scale, prismatic, and correspondence routes; bibliographic evidence, mostly conditional. |
| RH9 | `task14` | \(\Delta_3\) notebook, withdrawn divergent formula, and semiclassical comparison: numerical/exploratory. |
| RH9 | `task15–task35` | Gradings, Lefschetz, independence, trace, and prismatic theory: dependency and gap map, not a construction. |
| RH9 | `task36` | Zero-pair statistic: numerical; does not prove a general spectral obstruction. |
| RH9 | `task37–task45` | Arithmetic positivity, operators, \(\lambda\)-rings, and partial no-go: conditional. |
| RH9 | `task46` | \(\Delta_3\) replica: numerical and not independent of the same data pipeline. |
| RH9 | `task47–task54` | \(\Lambda\), correspondences, Frobenius/Sen theory, and absolute cohomology: identified gaps, not closed G1–G4 pieces. |
| RH9 | `task55` | Commutator-construction notebook; exploratory artifact without certification of a geometric route. |
| RH9 | `task56–task62` | Kernel transforms, Adams theory, traces, and statistics: proposals and constraints, not global proofs. |
| RH9 | `task63` | Extensive literature synthesis; useful as inventory, not as proof of the reduction or of a construction. |
| RH9 | `task64–task66` | Compatibility, Weil operator, and arithmetic star: conditional; the global objects are missing. |
| RH9 | `task67` | Incomplete preprocessing; no usable evidence. |
| RH9 | `task68–task69` | \(\log p\) weights and quantum deformation: partial/conjectural mechanisms. |
| RH9 | `task70` | Riemann–GUE comparison of \(\Delta_3\): numerical, with normalizations and approximations to be checked. |
| RH9 | `task71–task79` | Prolate theory, star, Hecke, unbounded operators, and von Neumann algebra: conditional constraints and literature review. |

## Synthesis for the global reformulation

1. RH7 supplies a detector and a tail bound for a finite basis; RH8 shows which numerical regimes are
   admissible. Neither resolves the jump to the infinite functional: that is the logical bottleneck and
   it is **EQUIVALENT-REFORMULATION-OF-RH**.
2. RH9 does not deliver an absolute geometry; it delivers filters that a geometry would have to satisfy
   without circularity. Its best assets are the conditioned no-go results and the G1–G4 list, not an
   already-open demonstrative route.
3. The continuation must separate three layers: a proved finite identity, an explicit analytic bound,
   and a global claim. The same numerical calibration must not be allowed to occupy two of those layers.
