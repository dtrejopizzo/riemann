# RH2023–RH2025 Audit: local detector, stability and geometry

## Scope and legend

The three README files, every `OVERVIEW.md`, and, when they provided material evidence, the associated CSVs, notebooks and specifications were reviewed. The label expresses the exact scope of the claim, not its aspiration.

| Label | Operational meaning |
|---|---|
| **PROVED** | Identity, reduction or bound proved in the finite space and with explicit hypotheses. |
| **CONDITIONAL** | Depends on a mathematical hypothesis, on an unconstructed identification, or on a complete external specification. |
| **NUMERICAL** | Reproduced on data, a finite mesh or an implementation; not an asymptotic theorem. |
| **CONJECTURAL** | Architecture, extrapolation or research direction. |
| **REFUTED** | The tested formulation fails, is inconsistent, or lacks sufficient data for the claimed use. |
| **EQUIVALENT-REFORMULATION-TO-RH** | Replaces RH with a condition that, if true, already contains the positivity or the uniform step that decides RH. It does not provide an independent proof. |

## RH2023 — Local detector of the Weil quadratic form

**Goal and method.** Build a localized form
\(Q=M_{\rm zeros}-M_{\rm arith}\) in a Hermite–Gauss basis, validate it on \(\zeta\), \(L(\chi_4\bmod 5)\) and \(L(\Delta)\), inject shifted zero quartets, measure \(\lambda_{\min}\), and separate the signal of an off-line zero from the error of cutting off primes and zeros. The correct dependence is on \((T_0,\sigma,J,X,H)\); any reading that suppresses it is out of scope.

### Closed results and evidence

- **[PROVED, finite]** The Taylor expansion of the synthetic quartet model gives a term of order \(\delta^2\) and a low-rank real symmetric operator built from \(\phi,\phi',\phi''\). The algebraic part of this claim is finite-dimensional, once the quartet convention, basis and zero list are fixed.
- **[NUMERICAL]** `task32` compares the minimum of the sum operator with the simulated surface over 60 cells and records an \(R^2\) rounded to one; `task31` contrasts it at another center. This is very strong evidence that the code and the expansion use the same convention, not a proof about an unknown real zero nor about the infinite functional.
- **[NUMERICAL]** The engine passes control traces in the regimes declared resolved; `task20` gives for \(L(\Delta)\) a trace residual close to machine precision after raising the cutoff and repairing the zero data. `task40` provides the \(\zeta\) control. This validates concrete assembly instances, not an independent implementation nor a uniform identity across the family.
- **[PROVED with finite scope / NUMERICAL in the calibration]** The Hermite–Gauss product transform has a Gaussian tail and allows bounding the arithmetic tail by absolute values using an explicit bound for \(\psi(x)\). `task34` and the README compare that envelope with seven values of \(X\). The observed correlation and slack factor are **NUMERICAL**; to call the integral a bound one must replace the approximate PNT density with an explicit inequality and keep all the constants.
- **[NUMERICAL]** The detectability tables (`task15`, `task18`, `task21`) estimate when \(c\delta^2\) exceeds an observed floor. They interpolate in \(J\), use seven prime cutoffs and, at one point, reach the floating-point floor: these are design rules, not certified mathematical thresholds.

### Dependencies, open points and logical status

| Claim | State | Audit |
|---|---|---|
| Passage from a synthetic perturbation to negativity of the finite model | **PROVED** | Valid only after fixing the quartet convention and the basis operator. |
| \(\delta^2\), locality and amplification in \(J\) for the meshes run | **NUMERICAL** | The shifted zeros are fabricated data; there is no uniform control as \(J\) grows. |
| Validation of \(Q\) for \(\zeta\), a complex character and \(\Delta\) at control points | **NUMERICAL** | A trace match does not by itself certify every entry nor other normalizations. |
| Prime tail with Hermite–Gauss basis | **PROVED** if formulated with an explicit Chebyshev/PNT bound; **NUMERICAL** for the fitted constant | Replacing the discrete sum with a density is not, by itself, a proof of the bound. |
| Zero tail and uniform convergence of \(Q_X\) to \(Q_\infty\) in the decisive regime | **EQUIVALENT-REFORMULATION-TO-RH** | This is precisely the step that would carry the finite negativity over to global Weil positivity. It was not proved. |
| "The detector proves RH if it never sees negativity" | **REFUTED** | A finite search does not cover every center, width, order, height or shift. |

### Errors, retractions and no-go

- **Davenport–Heilbronn:** the absolute reference value is not reproducible with the available information. A single definition of the arithmetic sequence analogous to \(\Lambda\) is missing, and a linear combination of \(L\)-functions does not allow combining derived logarithms term by term. `task11`, `task24` and `task41` force its retraction as a quantitative control. It remains only as a qualitative contrast: **REFUTED** for numerical calibration.
- **\(L(\Delta)\) normalizations:** `task2`, `task12` and `task17` discard the factor-of-two corrections tested. The earlier trace and zero-list failures (`task4`, `task5`, `task8`, `task23`, `task36`, `task37`) were partly overcome by `task20`, but must not be mixed with the final result.
- **Zeros of \(\Delta\):** the fixed-cutoff integrator lost zeros; some initial lists contain doubtful entries. Only the verified lists and the subsequent refinement protocol may feed a quantitative claim.
- **Non-self-dual character:** the initial formula had a phase bias. RH2023 uses a real-part correction; RH2024 adopts a symmetrized formulation. Numbers must not be transferred between the two without fixing exactly the zero side, conductor, gamma terms and conjugation convention.
- **Documentary inconsistency:** the perturbative-operator formula written in the RH2023 synthesis does not literally match the one derived in `task32`. The canonical formula must be reconstructed from the expansion and checked against the CSV before being cited as a theorem.
- **Law fits:** seven values of \(X\) do not identify a "zero-density regime." `task9` acknowledges overfitting; therefore its inference about the weaker hypothesis is **REFUTED** as a logical deduction, even though the fit is a useful data point.

### Inheritance and route not to repeat

RH2024 inherits an engine that must be traced with a specification, a validated zero list and a cutoff depending on \(\sigma,J\). It leaves a single analytic task for any continuation: a norm inequality that simultaneously controls prime tails, zero tails and numerical error over an explicit class of parameters. Do not repeat: turning empirical fits into arithmetic hypotheses, using Davenport–Heilbronn quantitatively, or confusing a synthetic \(\Delta Q\) with a proof about \(Q_\infty\).

## RH2024 — Basis stability and localization monotonicity

**Goal and method.** Study, across the three controls, the stability of \(\lambda_{\min}(Q(T_0,\sigma,J))\) as \(J\) increases (H1) and its response to \(\sigma\) and to nested zero windows (H2). The program reuses the RH2023 engine, imposes a trace gate before interpreting an eigenvalue, and quantitatively excludes Davenport–Heilbronn.

### Audited result

- **[NUMERICAL]** In the domains where the trace passes the gate, the available curves for \(\zeta\), \(L(\chi_4\bmod5)\) and \(L(\Delta)\) approach the numerical floor as \(J\), \(\sigma\) or the zero window are enlarged. `task4`, `task9`, `task14` and `task17` are point controls; `task1`, `task16`, `task19`, `task25` and `task27` give the H1 meshes.
- **[NUMERICAL]** H2 is supported in the resolved regime: `task2`, `task20`, `task21` and `task26` do not find the sought obstruction pattern under window widening. This is absence of a counterexample on a finite mesh, not a proved variational monotonicity.
- **[NUMERICAL / implementation correction]** `task3` replaces the non-self-dual formula with the symmetrized form that combines a character and its conjugate, and removes the \(X\)-independent residual. This is a necessary correction for this implementation; it does not prove that every generalization of Weil's complex-character case has been uniquely normalized.
- **[REFUTED in the computed domain]** At \(\sigma=0.5\) and accessible cutoffs, the trace gate does not close; `task6` even observes growth of the defect. The H1/H2 curves there are not spectral evidence.

| Claim | State | Limit |
|---|---|---|
| H1 for the finite \(J\), \(\sigma\) and \(X\) resolved | **NUMERICAL** | Does not prove the limit \(J\to\infty\), nor uniformity outside the sampled centers. |
| H2 on nested windows and resolved widths | **NUMERICAL** | There is no theorem of form ordering or monotonicity for every test function. |
| H1/H2 at \(\sigma=0.5\) with the available cutoffs | **REFUTED** as a spectral reading | Arithmetic truncation dominates. |
| "Finite stability or monotonicity implies RH" | **REFUTED** | The design itself forbids it; it also depends on the transition to the full functional. |
| Sufficient scaling of \(X\) for the whole family \((T_0,\sigma,J)\) | **CONDITIONAL** | Practical boundaries were measured, not a proved uniform law. |

**Dependencies and inheritance.** RH2024 depends directly on the local validity of RH2023; its durable contribution is methodological: do not interpret \(\lambda_{\min}\) without a trace residual, and separate three regimes: validated, recoverable by raising \(X\), and inaccessible with the current cutoff. It hands forward an admission condition for every numerical exploration, but no new route toward RH.

**No-go and corrections.** Do not reuse the results of `task8`, `task10`, `task12`, `task13`, `task22` and `task23` as validations: they record incomplete implementation, missing data or computation limits. Nor present the symmetrized correction as if it automatically reconciled the earlier RH2023 conventions. The correct route is to fix a single mathematical specification, add an independent check of matrix entries, and prove a tail bound before claiming asymptotic H1/H2.

## RH2025 — Arithmetic surface and Lefschetz structure

**Goal and method.** Search for a geometry independent of the spectrum that produces an absolute surface \(S\), a diagonal \([\Delta]\), a Lefschetz triple and a Hodge–Riemann form linked to Weil's criterion. Three routes are investigated: Arakelov/\(\lambda\)-rings, prismatic/TC, and scale noncommutative geometry; spectral statistics are also used as a design constraint.

### Overall verdict

No \(S\), \([\Delta]\), a cohomology with spectral \(H^1\), nor a triple \((L,\Lambda,H)\) passing G1–G4 was built. The program is valuable as a map of incompatibilities and requirements, but not as demonstrative progress toward RH. The initial reduction stating that the existence of G1–G4 is equivalent to RH must be catalogued as **EQUIVALENT-REFORMULATION-TO-RH** until an independent proof of the reduction is provided and, above all, a construction that does not encode the zeros.

### Routes, results and dependencies

| Route | What remains | Audited state |
|---|---|---|
| Arakelov and \(\lambda\)-rings | There are Chern classes, intersections, arithmetic Hodge indices and Adams gradings in existing contexts. The variation of the metric suggests independence from an operator defined by zeros. | **CONDITIONAL / CONJECTURAL.** Missing: the absolute object, the map to \(\Pi^\perp\), the diagonal, \(\Lambda\), a common space in which to prove \(L\notin W^*(T)\), and the identification of arithmetic positivity with the required form. |
| Prismatic, TC and Sen | Local Frobenii, Nygaard filtrations and local comparisons are real tools; the literature does not provide a global generator with a zero spectrum. | **CONJECTURAL** as scaffolding; the absence of an object in the survey is not a universal refutation. G1, G3 and G4 remain open. |
| Scale, adeles and prolate/Sonin | Scale dynamics produce the trace structure and \(\log p\) weights of primitive orbits. The relevant generator is noncompact, and the examined realizations do not give the required minimal-weight integer grading. | **CONDITIONAL** as an obstruction: solid for the specified representations and domains, but it does not prove a no-go for every noncommutative geometry. |
| \(\Delta_3\) statistic | CSVs and notebooks record a plateau near \(0.1908\) for a sample of zeros and its difference from finite/infinite GUE. | **NUMERICAL.** It is a phenomenological constraint for a future model, not a cohomological identity. |

### Open points, circularities and retractions

- **G1:** there is no proved identification between geometric cohomology and \(\Pi^\perp\), nor a Frobenius with spectrum \(\gamma_\rho\). Variable metric versus fixed spectrum is heuristic evidence of independence, not a certificate of membership in a von Neumann algebra without a common representation.
- **G2:** Adams gives rationalized integer weights, but not the Cartan operator of a Lefschetz \(\mathfrak{sl}_2\). The abelian-variety cases use duality and a Poincaré kernel that are absent for \(\mathrm{Spec}\,\mathbb Z\). A prolate triple with a continuous scale generator does not satisfy the requirement.
- **G3:** imposing \([T,L]=cL\) within the zero basis again demands arithmetic translations of the spectrum. The argument is conclusive for bounded operators with suitable domain hypotheses; for unbounded operators the notebooks and reviews give only a domain warning, not a general theorem.
- **G4:** the arithmetic Hodge index is a source of positivity in its own context, but its primitive part has not been identified with that of Weil's criterion. If positivity is defined using the signs of off-line zeros, or is equivalent to \(Q\succeq0\), it is circular and remains **EQUIVALENT-REFORMULATION-TO-RH**.
- The proposed prime-sum formula to explain the plateau, containing \(\sum_{p,k}(\log p)^2/p^k\), diverges; `task14` discards it. Only a formula with a dynamic cutoff and a complete derivation may be used: the literal formula is **REFUTED**.
- The computations in `task14`, `task36`, `task46`, `task59` and `task70` are exploratory and contain unfolding, GUE and semiclassical-formula approximations. They cannot be turned into a theorem of absence of scales, of linear independence, or of the existence of a geometric constant.
- The bibliography in the `OVERVIEW.md` files is orientational evidence. Before turning any of its claims into a mathematical dependency, the primary sources, hypotheses and notation must be verified; the summaries do not replace that verification.

### Inheritance and route not to repeat

The useful inheritance is a set of gates: independence from \(W^*(T)\), a genuine integer grading, a global operator with the correct spectrum, and positivity that does not restate RH. No route should start by defining \(L\) from moments or zeros, invoke a surface over \(\mathbb F_1\) as existing, confuse local Frobenii with the global spectrum, or infer a Lefschetz triple from spacing statistics. The next legitimate step is to choose a single, already-built geometric category and prove one concrete piece of G1–G4 without identifying it in advance with RH.

## Directory coverage

| Program | Directories covered | Evidence type and fate |
|---|---|---|
| RH2023 | `task1, task3, task7, task13, task14, task27, task30, task33, task38, task39, task43` | No substantive answer; they do not support conclusions. |
| RH2023 | `task2, task4, task5, task6, task8, task11, task12, task17, task23, task24, task25, task26, task28, task35, task36, task37, task40, task41, task42` | Engine, normalization, data and limits diagnostics; several are retracted or superseded by later validations. |
| RH2023 | `task9, task10, task15, task16, task18, task19, task20, task21, task22, task29, task31, task32, task34` | \(\delta^2\) signal, tails, detectability and final validations; a mix of finite and numerical results, per the table above. |
| RH2024 | `task7, task8, task10, task12, task13, task15, task22, task23, task24` | No closure, or insufficient implementation/data; excluded as H1/H2 evidence. |
| RH2024 | `task4, task9, task14, task17` | Trace gates and point controls: numerical assembly evidence in the resolved regime. |
| RH2024 | `task1, task2, task3, task5, task6, task11, task16, task18, task19, task20, task21, task25, task26, task27` | H1/H2 curves, cutoff sweeps and non-self-dual correction; exclusively numerical, regime-dependent evidence. |
| RH2025 | `task1–task13` | Review of Arakelov, scale, prismatic routes and correspondences; bibliographic evidence, mostly conditional. |
| RH2025 | `task14` | \(\Delta_3\) notebook, retracted divergent formula and semiclassical comparison: numerical/exploratory. |
| RH2025 | `task15–task35` | Gradings, Lefschetz, independence, trace and prismatic: a map of dependencies and gaps, not a construction. |
| RH2025 | `task36` | Zero-pair statistics: numerical; does not prove a general spectral obstruction. |
| RH2025 | `task37–task45` | Arithmetic positivity, operators, \(\lambda\)-rings and partial no-go results: conditional. |
| RH2025 | `task46` | Replication of \(\Delta_3\): numerical and not independent of the same data pipeline. |
| RH2025 | `task47–task54` | \(\Lambda\), correspondences, Frobenius/Sen and absolute cohomology: identified gaps, not closed G1–G4 pieces. |
| RH2025 | `task55` | Commutator-construction notebook; an exploratory artifact without certification of a geometric route. |
| RH2025 | `task56–task62` | Kernel transforms, Adams, traces and statistics: proposals and constraints, not global proofs. |
| RH2025 | `task63` | Extensive literature synthesis; useful as an inventory, not as proof of the reduction nor of a construction. |
| RH2025 | `task64–task66` | Compatibility, Weil operator and arithmetic star: conditional; the global objects are missing. |
| RH2025 | `task67` | Incomplete preprocessing; no usable evidence. |
| RH2025 | `task68–task69` | \(\log p\) weights and quantum deformation: partial/conjectural mechanisms. |
| RH2025 | `task70` | Riemann–GUE comparison of \(\Delta_3\): numerical, with normalizations and approximations to be checked. |
| RH2025 | `task71–task79` | Prolate, star, Hecke, unbounded operators and von Neumann algebra: conditional constraints and literature review. |

## Synthesis for the global restatement

1. RH2023 provides a detector and a tail bound for a finite basis; RH2024 shows which numerical regimes are admissible. Neither resolves the jump to the infinite functional: that is the logical bottleneck and it is **EQUIVALENT-REFORMULATION-TO-RH**.
2. RH2025 does not deliver an absolute geometry; it delivers filters that a geometry would have to satisfy without circularity. Its best assets are the conditioned no-go results and the G1–G4 list, not an already-open demonstrative route.
3. The continuation must separate three layers: a proved finite identity, an explicit analytic bound, and a global claim. The same numerical calibration must not be allowed to occupy two of those layers.
