# The research record (phases 0–214)

This folder is the core of the project: a single continuous research programme, organised as a
sequence of numbered phases. It follows nine early exploratory computational programmes,
RH2017–RH2025, kept in [`../01-context/`](../01-context/).

Each `phase-*/` folder is a self-contained block of work with its own README: the question, the
results with their status labels (PROVED / CITED / CONDITIONAL / ARGUED / NUMERICAL / NO-GO / OPEN;
see the [root README](../README.md#conventions-and-status-labels)), the files, and the relation to
other phases.

- Phases 0–107 build the Weil-form framework and map its obstructions.
- Phases 108–133 construct rows A, B and C and close them on the declared carrier
  (Papers 43–45).
- Phases 134 onward work on row D, the sign of the window form (Paper 46), which remains OPEN;
  structural results of this work are in Paper 47, and the routes tried are surveyed in Paper 48.

## How the phases connect to the papers

The results distilled from these phases are in [`../04-papers/`](../04-papers/), catalogued in
[`../04-papers/README.md`](../04-papers/README.md). Every route tried for the sign is indexed in
[`../05-meta-and-planning/ROUTES-MASTER-INDEX.md`](../05-meta-and-planning/ROUTES-MASTER-INDEX.md).

## Phase index

The outcome column is a one-line summary; the README of each phase gives the precise statements
and labels.

| Phase | Topic | Outcome |
|---|---|---|
| [phase-0-foundations](phase-0-foundations/) | The Weil form Q in Weil–Guinand language; normalization pinned | Normalization fixed; classical formula translated (CITED) |
| [phase-3-uniform-inequality](phase-3-uniform-inequality/) | Stability geometry of the localized Weil quadratic form | Uniform positivity limit identified as equivalent to RH; forced negativity under an off-line zero; no reduction |
| [phase-4-handoff](phase-4-handoff/) | Faithful semibounded Kreĭn realization of the Weil functional (Theorem B-2) | Theorem B-2 PROVED modulo one hypothesis (H) strictly weaker than RH |
| [phase-5-structural](phase-5-structural/) | The semi-local Connes residual; PW_d ↔ prolate question | The P8 no-go does not transport to the Connes residual; question left OPEN |
| [phase-6-osterwalder-schrader-reflection](phase-6-osterwalder-schrader-reflection/) | The Weil form as an Osterwalder–Schrader reflection-positive form (per-place positivity fails) | Faithful OS recasting PROVED; per-place positivity fails (NO-GO); one variant retracted |
| [phase-7-weil-carleson-sine-kernel](phase-7-weil-carleson-sine-kernel/) | Second order: Weil–Carleson form = sine-kernel determinantal process | Exact Carleson identity PROVED; sine-kernel structure NUMERICAL |
| [phase-8-heat-flow-monotonicity](phase-8-heat-flow-monotonicity/) | A clean monotonicity theorem; why the heat flow alone cannot prove RH | Monotonicity theorem PROVED; heat flow alone cannot prove RH (NO-GO) |
| [phase-9-unconditional-universality](phase-9-unconditional-universality/) | Verdict N6; forced pivot to unconditional partial results | Monotone functionals of the flow classified (N6); pivot to unconditional results |
| [phase-10-hodge-envelope-degeneration](phase-10-hodge-envelope-degeneration/) | Deep run (M=25, T≤10⁴, 10154 ζ-zeros); Hodge-index entry | Hodge gap degenerates toward ζ (NUMERICAL) |
| [phase-11-hyperbolicity-total-positivity](phase-11-hyperbolicity-total-positivity/) | Interlacing = total positivity; the wrong-sign capstone behind it | Jensen interlacing NUMERICAL; wrong-sign obstruction identified |
| [phase-12-meta-obstruction-moment-problem](phase-12-meta-obstruction-moment-problem/) | Multiplicative chaos; the capstone first escaped (N7 barrier) | S(T) log-correlated (NUMERICAL); exact dictionary PROVED; N7 barrier |
| [phase-13-omega-class-multiplicative-chaos](phase-13-omega-class-multiplicative-chaos/) | The ω-class structure of ζ's multiplicative-chaos exponents (RH-independent) | ω-class identity PROVED; RH-independent |
| [phase-14-off-diagonal-anchor-asymmetry](phase-14-off-diagonal-anchor-asymmetry/) | The anchor framework: a ζ-free classification of zero-absence mechanisms | Explicit formula is ω-blind (PROVED); ζ-free classification |
| [phase-15-arithmetic-hodge-index](phase-15-arithmetic-hodge-index/) | The Anatomy–Kreĭn–Hodge program; spectral entry to the arithmetic Hodge index | Intersection pairing and ample-cone positivity PROVED; Hodge index for ζ OPEN |
| [phase-16-surf-witness-variety](phase-16-surf-witness-variety/) | SURF specification sheet — acceptance criteria for the witness variety | Acceptance specification fixed; candidate routes triaged |
| [phase-17-surf-2-design](phase-17-surf-2-design/) | SURF 2.0 internal design (involution / resolvent routes) | Acceptance test fixed; design routes, no construction |
| [phase-18-negative-directions-portrait](phase-18-negative-directions-portrait/) | A portrait of the negative directions of the Weil form | Four structural properties of negative directions (NUMERICAL) |
| [phase-19-omega-rate-freezing](phase-19-omega-rate-freezing/) | The forward flow of the ω-class (closure document) | Moment exponent k² from Erdős–Kac PROVED (no zeros used) |
| [phase-20-zero-omega-bridge](phase-20-zero-omega-bridge/) | The zero–ω bridge: the information barrier | Zeros invisible to ω-moments: information barrier (NO-GO) |
| [phase-21-negative-directions-geometry](phase-21-negative-directions-geometry/) | Geometry of negative directions | Negative index κ is even (PROVED) |
| [phase-22-pontryagin-finite-defect](phase-22-pontryagin-finite-defect/) | Arithmetic consequences of the finite Pontryagin defect | Defect constructions under finitely many off-line zeros (CONDITIONAL) |
| [phase-23-two-scale-defect-structure](phase-23-two-scale-defect-structure/) | Two-scale structure and spectral compatibility of the defect | Closed-form orbit contribution to log\|ζ\| PROVED |
| [phase-24-lower-bounds-bj](phase-24-lower-bounds-bj/) | Lower bounds for b_j and local rigidity of log\|ζ\| | No lower bound on b_j from classical estimates (NO-GO) |
| [phase-25-lower-bounds-bj-audit](phase-25-lower-bounds-bj-audit/) | Lower bounds for b_j: full audit of classical mechanisms (15 no-goes) | Fifteen classical mechanisms audited: all NO-GO |
| [phase-26-krein-connes-bridge](phase-26-krein-connes-bridge/) | The bridge theorem: Kreĭn ↔ Connes | Bridge κ(Q) = neg.ind(H_C) stated; absent from literature; OPEN |
| [phase-27-adelic-rigidity](phase-27-adelic-rigidity/) | Adelic rigidity (Hasse–Minkowski wall) | Consequences of the bridge PROVED conditionally; Hasse–Minkowski wall |
| [phase-28-four-fronts](phase-28-four-fronts/) | Four simultaneous fronts; all reduce to ξ ∈ Laguerre–Pólya | All four fronts reduce to ξ ∈ Laguerre–Pólya; no closure |
| [phase-29-zeta-spectral-triples](phase-29-zeta-spectral-triples/) | Zeta spectral triples: precise setup | Self-adjointness PROVED; convergence OPEN |
| [phase-30-langlands-bridge-c-infinity](phase-30-langlands-bridge-c-infinity/) | The Langlands bridge: C_∞ for automorphic L-functions | GRH_F ⟺ C_∞ ≡ 0 PROVED (reformulation) |
| [phase-31-selberg-moments-c-infinity](phase-31-selberg-moments-c-infinity/) | Moments of C_∞(γ_n) and the Selberg theorem | M_1 ≡ 0 ⟺ RH and moment bounds PROVED |
| [phase-32-ccm](phase-32-ccm/) | Bridge between the CCM program and the C_∞ deficit | Jacobi-discrepancy results PROVED; bridge to the deficit OPEN |
| [phase-33-dbn](phase-33-dbn/) | De Bruijn–Newman and the CCM trace; Λ as extinction time | New characterization of Λ PROVED; Λ = 0 only CONDITIONAL |
| [phase-34-new-directions](phase-34-new-directions/) | External arithmetic information via the explicit formula (inverse Jacobi, Pontryagin) | Explicit formula supplies no external information (NO-GO); directions OPEN |
| [phase-35-five-fronts](phase-35-five-fronts/) | Five fronts; off-critical quadruple toy tests; H_x convergence / CF rigidity | H_x convergence PROVED; Maslov test OPEN |
| [phase-36-ABC-forms](phase-36-ABC-forms/) | Effective SR_d; two-prime 2D coupling; the sieve–index bridge | Dichotomy as posed is false (NO-GO); refined behaviour reported |
| [phase-37-physics](phase-37-physics/) | The critical-anchoring principle: what forces Λ=0? | Guiding question only; OPEN |
| [phase-38-final-audit](phase-38-final-audit/) | Adversarial audit of the W_λ positivity / sharpening claims | Audits of the W_λ positivity and dichotomy claims |
| [phase-39-G1G2-interface](phase-39-G1G2-interface/) | The forced axioms: backward derivation of the cohomology requirements | Forced axioms derived backward (framework) |
| [phase-40-close-G1](phase-40-close-G1/) | The symmetry bit; duality pairing on the divisor | Duality pairing identified as Pontryagin type |
| [phase-41-build-G2](phase-41-build-G2/) | The intersection form on the square of the scaling site | Toy Gram matrix of signature (1,2) computed; G2 OPEN |
| [phase-42-hodge-dynamics](phase-42-hodge-dynamics/) | Dynamical Hodge theory as a foliated Kähler-package framework (Deninger) | Source of positivity not external: circular (NO-GO) |
| [phase-43-hodge-foliated-specZ](phase-43-hodge-foliated-specZ/) | Does the foliated Spec ℤ admit a polarizable Hodge structure? | No polarizable Hodge structure on Morishita's space (NO-GO) |
| [phase-44-creative-breakthrough](phase-44-creative-breakthrough/) | Hodge–Witt and visible inertia | Lemmas internal to a new framework; bridge to RH CONDITIONAL |
| [phase-44-new-mathematics](phase-44-new-mathematics/) | The algebra of arithmetic correspondences: the category 𝒜rith | Category constructed; connection to RH declared, not proved |
| [phase-45-fredholm](phase-45-fredholm/) | The Weil–Toeplitz algebra: symbol, compact ideal, two-prime theorem | Strict essential positivity ⇒ finite defect PROVED |
| [phase-46-audit-and-attacks](phase-46-audit-and-attacks/) | Adversarial audit of the local-purity theorem; semilocal attacks | Audits of the local-purity and two-prime theorems |
| [phase-47-live-fronts](phase-47-live-fronts/) | Attack on the Paley–Wiener finiteness pivot (LP-141) | LP-141 refuted by a Hadamard counterexample (NO-GO) |
| [phase-48-audit-and-purity](phase-48-audit-and-purity/) | Audits of the revival attempts; purity/rigidity attacks | Revival attempts fail (NO-GO) |
| [phase-49-cross-the-wall](phase-49-cross-the-wall/) | Taxonomy of "average → individual" crossings; Tauberian / Maslov probes | Taxonomy of crossings (framework) |
| [phase-50-diophantine-thread](phase-50-diophantine-thread/) | Is ℚ-linear independence of {log p} the certificate? | Equivalences PROVED; the thread collapses to a restatement |
| [phase-51-functor-construction](phase-51-functor-construction/) | Constructing the phase→inertia functor/transport | RH-free transport constructed; the required metric is missing |
| [phase-52-homotopy-inertia](phase-52-homotopy-inertia/) | Homotopy inertia: is m a metric-free secondary invariant? | Candidate secondary invariant constructed; OPEN |
| [phase-53-quantum-import](phase-53-quantum-import/) | Importing Stone's theorem: structural unitary evolution | Source of unitarity located; OPEN |
| [phase-54-index-dynamics](phase-54-index-dynamics/) | Deformation theory of the metric space over the Kreĭn space; κ dynamics | Conservation and Hessian pieces correct but empty (audit) |
| [phase-55-two-arrows](phase-55-two-arrows/) | The structural representation of I(0⁺): sum-rules, the shadow theorem | Shadow–signal obstruction PROVED |
| [phase-56-two-towers](phase-56-two-towers/) | Lemma 177.B by three routes (gap-ODE, KKL, polylog repulsion) | Lemma 177.B not closed by three routes |
| [phase-57-brick-A](phase-57-brick-A/) | The desingularized Dirichlet energy identity | Desingularized energy identity PROVED |
| [phase-58-full-audit](phase-58-full-audit/) | Adversarial audit of the energy dichotomy and GAP 175 | Energy-dichotomy chain certified, with errata |
| [phase-59-full-closure](phase-59-full-closure/) | Adversarial audit of the universal moment floor; closure ledger | Moment floor certified; closure ledger; two downgrades |
| [phase-60-discriminant](phase-60-discriminant/) | The discriminant: isolate the arithmetic invariant controlling the Weil sign (NG-F1 no-go) | CCM engine validated (NUMERICAL); NG-F1 (NO-GO) |
| [phase-61-open-problems](phase-61-open-problems/) | Open-problems inventory (CCM frame); what remains genuinely open | O1–O3 CLOSED; remaining problems catalogued OPEN |
| [phase-62-cesaro-closure](phase-62-cesaro-closure/) | Cesàro-in-λ attack on 2.3.F boundedness (NG-62 no-go: averaging is RH-equivalent, not neutral; `b_bulk` is a detector) | Cesàro route NO-GO (averaging is RH-equivalent) |
| [phase-63-lefschetz-realization](phase-63-lefschetz-realization/) | MW-5 realization frontier (NG-63): F_q has J-linear Frobenius + gapped polarization, ζ window has antilinear scaling + gapless — MW-5 made precise by direct contrast | NG-63: MW-5 made precise; closed |
| [phase-64-connes-route](phase-64-connes-route/) | Connes' route: L1 reclassified as RH criterion (Task A confirmed; D proven parity no-go); target = regularized positivity (relative determinant / de Branges Schur), not finite gap | L1 ⟹ RH PROVED (criterion); regularized positivity OPEN |
| [phase-65-signature-continuity](phase-65-signature-continuity/) | Signature-continuity package: index-graded determinant/topology; wall = renormalization-stable self-adjoint completion | Construction package; the wall (D8.5) isolated, OPEN |
| [phase-66-rank-one-escape](phase-66-rank-one-escape/) | Rank-one escape and whitening calibration; scalar whitening fails, matrix whitening is essential | Rank-one escape dichotomy PROVED as a reformulation |
| [phase-67-quantum-q-index](phase-67-quantum-q-index/) | Quantum/q-index route; q-overlay and leakage of off-line directions audited, Woronowicz/free-product no-goes | Candidate only; Woronowicz/free-product NO-GOs |
| [phase-68-glt-symbol](phase-68-glt-symbol/) | GLT/Toeplitz symbol route; symbol positivity is gauge-fragile and does not close Ω7 | Symbol positivity gauge-fragile (NUMERICAL); does not close Ω7 |
| [phase-69-exact-signed-index](phase-69-exact-signed-index/) | Gauge-free Nevanlinna/signed-index formulation; detector solid, forcing mechanism still absent | Signed-index detector; forcing mechanism absent (OPEN) |
| [phase-70-lee-yang-dbn](phase-70-lee-yang-dbn/) | Lee-Yang / de Bruijn-Newman route; Ω7 localized to Λ≤0, the arithmetic direction | Ω7 localized to Λ ≤ 0; no forcer (OPEN) |
| [phase-71-cand1-convergence](phase-71-cand1-convergence/) | CAND-1/CCM finite self-adjoint convergence; real finite zeros are automatic, content is stable-divisor convergence | Real finite zeros automatic; content is stable-divisor convergence (OPEN) |
| [phase-72-feshbach-leakage-calculus](phase-72-feshbach-leakage-calculus/) | New pole-relative Feshbach leakage calculus; replaces global residual convergence by one-vector arithmetic leakage below the prolate gap | Reduced to one-vector leakage; not closed |
| [phase-73-cauchy-projection](phase-73-cauchy-projection/) | Cauchy projection gate; the transformed compact branch reduced to the single finite Cauchy-Schur nodal identity NAT-PROJ | Reduced to the nodal identity NAT-PROJ; not closed |
| [phase-74-hilbert-eigenline-cancellation](phase-74-hilbert-eigenline-cancellation/) | Hilbert eigenline cancellation; NAT-PROJ reduced to an exact Hilbert product rule (HPR-DIV) on the projected eigenline | Reduced to HPR-DIV; not closed |
| [phase-75-arithmetic-numerator-divisibility](phase-75-arithmetic-numerator-divisibility/) | Arithmetic numerator divisibility; attacks the ARITH-LOCK ⇒ CCM-ROOT-LOCK ⇒ CRIT-NUM-DIV ⇒ CAUCHY-EIG-LOC ⇒ HPR-DIV chain via a new signed arithmetic identity | Divisibility chain attacked; endpoint not closed |
| [phase-76-normalized-adjugate-arithmetic-lock](phase-76-normalized-adjugate-arithmetic-lock/) | Normalized adjugate arithmetic lock; safe-ratio closure theorem SR-SAFE ⇒ Ω7, exact Sherman–Morrison/displacement algebra, and the closing split SAFE-LIMIT-POINT = LP ∧ IDENT (closed at 67 documents; see PHASE_76_CLOSURE.md) | Endpoint corrected (PROVED); closed at the split endpoint |
| [phase-77-weyl-limit-point](phase-77-weyl-limit-point/) | Weyl limit-point closure; proves (or refutes) LP (limit-point for the semi-infinite CCM system, via Kato–Putnam on the rank-two displacement commutator) and IDENT (Gamma-prime identification in absolute convergence), the two halves left by phase 76 | Operational LP holds for both builds; IDENT is the discriminant |
| [phase-78-build-neutral-lp-and-ident](phase-78-build-neutral-lp-and-ident/) | Build-neutral LP and IDENT: separating the two halves from the construction that produced them | Build-neutral reductions PROVED; IDENT OPEN |
| [phase-79-shared-convergence-and-ident-discriminant](phase-79-shared-convergence-and-ident-discriminant/) | The shared convergence lemma (GAP-Z) and the IDENT discriminant | Mesh and boundary bounds PROVED; GAP-Z OPEN |
| [phase-80-relative-determinant-identification](phase-80-relative-determinant-identification/) | Relative determinant identification | Exact reduction; remaining identification passed on |
| [phase-81-secular-arithmetic-anchor](phase-81-secular-arithmetic-anchor/) | Secular arithmetic anchor | Exact reduction; remaining target passed on |
| [phase-82-coupled-generator-continuum](phase-82-coupled-generator-continuum/) | Coupled generator continuum | Exact reduction; obstruction to the outer limit |
| [phase-83-gamma-euler-coboundary](phase-83-gamma-euler-coboundary/) | Gamma–Euler arithmetic coboundary | Ground-vector obstruction; distributional repair proposed |
| [phase-84-distributional-endpoint-module](phase-84-distributional-endpoint-module/) | Distributional endpoint module | Parity split; cofinal-rank obstruction |
| [phase-85-parity-weyl-defect](phase-85-parity-weyl-defect/) | Parity Weyl defect | Exact defect formulas; obstruction audit |
| [phase-86-signed-spectral-abel](phase-86-signed-spectral-abel/) | Signed spectral Abel reduction | Finite Abel identity; ceiling autopsy |
| [phase-87-euler-deformation-discriminant](phase-87-euler-deformation-discriminant/) | Euler deformation discriminant | Bordered tangent anomaly computed; no closure |
| [phase-88-endpoint-layer-pencil](phase-88-endpoint-layer-pencil/) | Endpoint layer pencil | Scaled-pencil limit; single-scale falsifier |
| [phase-89-projective-layer-rotation](phase-89-projective-layer-rotation/) | Projective layer rotation | Surviving endpoint object = the safe Cauchy profile |
| [phase-90-projective-kato-euler-current](phase-90-projective-kato-euler-current/) | Projective Kato–Euler current | Exact Kato current; matching defect |
| [phase-91-kato-coboundary-equivalence](phase-91-kato-coboundary-equivalence/) | Kato–coboundary equivalence | No-bypass theorem; minimal remaining target |
| [phase-92-cluster-adjugate-projectivization](phase-92-cluster-adjugate-projectivization/) | Cluster adjugate projectivization | Corrected endpoint ledger; no closure |
| [phase-93-direct-bordered-anchor](phase-93-direct-bordered-anchor/) | Direct bordered anchor | Shortest sufficient route identified; OPEN |
| [phase-94-global-cofactor-cell-current](phase-94-global-cofactor-cell-current/) | Global cofactor cell current | Finite identities certified; remaining theorem OPEN |
| [phase-95-characteristic-jacobian-current](phase-95-characteristic-jacobian-current/) | Characteristic Jacobian current | Remaining determinant identity isolated; OPEN |
| [phase-96-determinantal-prime-response](phase-96-determinantal-prime-response/) | Determinantal prime response | Global response kernel; coupled-sum decision |
| [phase-97-euler-sensitivity-commutator](phase-97-euler-sensitivity-commutator/) | Euler sensitivity commutator | Canonical boundary target; finite signs certified |
| [phase-98-sensitivity-shell-split](phase-98-sensitivity-shell-split/) | Sensitivity shell split | Exact shell split; corrected boundary target |
| [phase-99-adjugate-boundary-sandwich](phase-99-adjugate-boundary-sandwich/) | Adjugate boundary sandwich | Sandwich identity; final target OPEN |
| [phase-100-characteristic-cofactor-factorization](phase-100-characteristic-cofactor-factorization/) | Characteristic cofactor factorization | Determinant form identified; recombination decision |
| [phase-101-covariant-bordered-current](phase-101-covariant-bordered-current/) | Covariant bordered current; planted-falsifier controls | Several NO-GOs; covariant determinant problem OPEN |
| [phase-102-omega7-closure-campaign](phase-102-omega7-closure-campaign/) | Omega-7 closure campaign; finite certificates and the surviving direct inequality | Finite certificates; one direct inequality survives (OPEN) |
| [phase-103-direct-a1-closure](phase-103-direct-a1-closure/) | Exact direct-A1 reduction, compact--tail identity, finite certificates and Laguerre transport | Reduced to one inequality; unproved claims withdrawn |
| [phase-104-unconditional-a1-closure](phase-104-unconditional-a1-closure/) | Unconditional A1 campaign; exact equivalences, Deep/Blaschke reduction and adversarial closure ledger | Closed; objective not proved; exact equivalences recorded |
| [phase-105-a1-geometry-and-deep-limit](phase-105-a1-geometry-and-deep-limit/) | Visual geometry of A1 and the literal Deep limit; clean restart from the two surviving targets | Prime-side subexponential bound OPEN (equivalent to RH) |
| [phase-106-global-modular-star-audit](phase-106-global-modular-star-audit/) | Global modular-star audit; self-adjoint Euler determinant no-go, second-resolvent target, and adelic half-density descent obstruction | Closed as an audit; determinant and descent NO-GOs |
| [phase-107-arithmetic-lefschetz-reconstruction](phase-107-arithmetic-lefschetz-reconstruction/) | Reverse engineering of a finite-support arithmetic Lefschetz divisor; function-field calibration, proper-global support rule, exact radical audit, and arithmetic surface program | Function-field calibration; finite local route NO-GO |
| [phase-108-row-a-construction](phase-108-row-a-construction/) | Row (a): the space over ℤ; the graded family, and the closure of principal invariance and of both pairing routes | Character classification and stage 1 PROVED; pairing routes closed |
| [phase-109-one-sided-pairing](phase-109-one-sided-pairing/) | Does the one-sided assembly carry a pairing? No: any pairing reading the prime-power coefficients is blind to the zeros, for every kernel | One-sided pairing blind to the zeros (PROVED, negative) |
| [phase-110-principal-xi-divisibility](phase-110-principal-xi-divisibility/) | Does ξ-divisibility supply the principal subspace row (d) needs? Impossible on compactly supported data, by a growth argument independent of the zeros | ξ-divisibility impossible on compact data (PROVED, negative) |
| [phase-111-schwartz-admissibility](phase-111-schwartz-admissibility/) | Does I_∂ converge on Schwartz-class data? The threshold, and Assumption T | Convergence on Schwartz data PROVED; Assumption T |
| [phase-112-effective-cone](phase-112-effective-cone/) | Requirement d5, the effective cone — satisfied formally; superseded by 113_10 | Formal only; superseded by 113_10 |
| [phase-113-the-trace-on-schwartz-data](phase-113-the-trace-on-schwartz-data/) | The trace on Schwartz data: rad = the χ-ideal, a Frobenius \*-algebra with a zero-free trace, d0/d2/d4/d5/K=0 built, d3 impossible inside 𝒟 — and row (d) proved **equivalent to RH** | Frobenius ∗-algebra with zero-free trace built; d3 impossible inside D |
| [phase-114-closing-the-four-rows](phase-114-closing-the-four-rows/) | Rows (a)–(c) completed and written up (paper 42); row (d) reduced to the sharp Douglas gate and then to one explicit joint residual — but the local-construction campaign re-proved two obstructions already in the paper | Rows (a)–(c) written up (Paper 42); row (d) reduced to one residual, OPEN |
| [phase-115-the-mixed-class-and-the-green-extension](phase-115-the-mixed-class-and-the-green-extension/) | Row (d) is missing an **object**, not an inequality: row (a)'s Green term is a rank cut r→1 (`ℓℓᵀ − diag ℓ`) and row (a) attains B=0 on its own primitive space — so it is row (d)'s equality case. Target: the mixed class **M**_f | Axioms 1–2 PROVED (after a retraction); sign unresolved |
| [phase-116-the-logarithmic-schur-angle-conjecture](phase-116-the-logarithmic-schur-angle-conjecture/) | Audits and rejects a proposed Cauchy–Schwarz/Gamma-gap closure of row (d)'s constant/mean-zero Schur block, then extracts and names the estimate that survives: the Logarithmic Schur Angle Conjecture, ρ_N ≤ 1/(20 log N). Carried verbatim into paper 42, where row (d) is completed **conditionally** on it | Proposed closure rejected; conjecture stated, OPEN |
| [phase-117-the-transfer-comparison-measured](phase-117-the-transfer-comparison-measured/) | Measures the one item neither paper nor corpus addressed — the comparison carrying the Gamma–Tate *source model* to the *exact* threshold condition. **c_N < 1 at every threshold, decaying like (log N)^-0.6: the source route does not reach the target.** Galerkin bounds c_N from above, so this is one-sided-robust. Also falsifies ρ_N ≤ 1/(20 log N) at 4 of the 5 points in paper 42's own audit table. The exact target *does* hold on every threshold tested — so the redirect is to prove it directly in the output-defect metric | Transfer comparison measured (NUMERICAL) |
| [phase-118-the-exact-threshold-inequality](phase-118-the-exact-threshold-inequality/) | Attacks the exact threshold condition directly — and **verifies against real zeros of ζ, to 10 digits, that `⟨A_T F,F⟩ = Σ_ρ h(γ_ρ)`**. The row-(d) inequality *is* localized Weil positivity on the primitive space, hence equivalent to RH (Weil 1952; Yoshida 1992; Bombieri 2000), so no internal reformulation can close it. `m₀`, the primitive space and the truncation all turn out **forced**, not chosen. Also: balanced factorization re-verified by an independent code path; Toeplitz/Hankel structure for the scattering operator refuted; the log-2 certificate reproduced and its limit diagnosed as analytic, not numerical. Closed | Exact identity derived and checked against zeros (NUMERICAL) |
| [phase-119-what-a-finite-compression-certifies](phase-119-what-a-finite-compression-certifies/) | Pivot: stop asking whether Weil's form is positive (that question's only answer is RH) and ask what a **finite compression** certifies unconditionally — its inertia constrained by Sylvester, its moments computable from the prime side. Distinctive assets: the exact filtration, the balanced factorization as a second signature decomposition, a working Arb pipeline. Gated on the Davenport–Heilbronn test: does `Λ(n) = deg_det 𝕃_n` separate ζ from an object whose RH-analogue is false? | Separates ζ from Davenport–Heilbronn; not sufficient for positivity |
| [phase-120-global-polarization](phase-120-global-polarization/) | Global polarization | Source-side constructions PROVED; global square inequality OPEN |
| [phase-121-negative-witness-rigidity](phase-121-negative-witness-rigidity/) | Negative-witness rigidity, beyond the positive-lift architecture | Opened; no theorem assumed |
| [phase-122-row-d-integrity-and-construction](phase-122-row-d-integrity-and-construction/) | Row (d): integrity audit before construction | Integrity audit; no construction of row (d) |
| [phase-123-weil-strength-abc](phase-123-weil-strength-abc/) | Weil-strength A/B/C | Row A carrier work (superseded by 125–130) |
| [phase-124-direct-first-contact](phase-124-direct-first-contact/) | Direct first-contact route | Exploration; no new positivity theorem |
| [phase-125-row-a-completion](phase-125-row-a-completion/) | Row A completion campaign | Row A labelled complete (label withdrawn in 128) |
| [phase-126-row-b-completion](phase-126-row-b-completion/) | Row B completion | Row B labelled complete (label withdrawn in 128) |
| [phase-127-row-c-completion](phase-127-row-c-completion/) | Row C completion | Row C labelled complete (label withdrawn in 128) |
| [phase-128-adversarial-audit](phase-128-adversarial-audit/) | Adversarial audit of rows A, B, C, and its corrections | All three completion labels withdrawn; errors recorded |
| [phase-129-row-a-rebuild](phase-129-row-a-rebuild/) | Row A rebuild | Rebuild converged |
| [phase-130-row-a-closure](phase-130-row-a-closure/) | Row A closure: A.8, A.5, A.7, A.1 (construction/audit loop, round 2) | Row A complete on the declared carrier |
| [phase-131-row-b-closure](phase-131-row-b-closure/) | Row B closure (construction/audit loop) | Row B complete on the declared carrier |
| [phase-132-row-c-closure](phase-132-row-c-closure/) | Row C closure (round/audit loop) | Row C complete on the declared carrier |
| [phase-133-abc-review-panel](phase-133-abc-review-panel/) | Review of Papers 43–45 after the closures of rows A–C | Three independent reviews; one repair round |
| [phase-134-row-d-opening](phase-134-row-d-opening/) | Row D opening campaign (the sign) | Row D opened; no sign claimed; Paper 46 skeleton |
| [phase-135-row-d-canonical-class](phase-135-row-d-canonical-class/) | Row D, first construction campaign: the canonical class and the affine duality | Canonical class and affine duality; Hodge-index transfer CONDITIONAL |
| [phase-136-row-d-map](phase-136-row-d-map/) | The map of where not to go (row D), and the plan | Map of no-gos and plan |
| [phase-137-row-d-canonical-coupling](phase-137-row-d-canonical-coupling/) | The coupling of the canonical class with the Frobenius lattice (row D) | Coupling studied; no label change |
| [phase-138-row-d-detecting-cones](phase-138-row-d-detecting-cones/) | Row D: the primitive radial sector and detecting cones | Confirmed with repairs; no label change |
| [phase-139-row-d-two-falsifiers](phase-139-row-d-two-falsifiers/) | Row D: the two falsifiers and the method theorem | Two falsifiers and the method theorem |
| [phase-140-row-d-frobenius-square](phase-140-row-d-frobenius-square/) | Row D: the Frobenius side of (P139); the square as a tensor structure | Tensor structure of the square; labelled results |
| [phase-141-row-d-frobenius-traces](phase-141-row-d-frobenius-traces/) | Row D: an `h⁰` that reads the Frobenius traces | Row D reduced to one clause |
| [phase-142-row-d-the-clause](phase-142-row-d-the-clause/) | Row D: the clause (b′)⁺ | Theorem D.31.12 stands after audit |
| [phase-143-row-d-trace-positive-cone](phase-143-row-d-trace-positive-cone/) | Row D: `s_*`, the trace-positive cone B4, and a repaired transfer theorem | Repaired transfer theorem |
| [phase-144-row-d-fixed-index](phase-144-row-d-fixed-index/) | Row D: the fixed-index inequality | Fixed-index inequality studied |
| [phase-145-row-d-function-field-model](phase-145-row-d-function-field-model/) | Row D: the function-field model of the frame | Frame defect holds in the function-field model; prediction refuted |
| [phase-146-row-d-coupled-pairing](phase-146-row-d-coupled-pairing/) | Row D: the degree form on `Z[Frob]` with a count interpretation | Count interpretation (Q0, Q1) |
| [phase-147-row-d-galois-ring](phase-147-row-d-galois-ring/) | Row D: the Galois group ring `Z[Gal(L/F)]` as the missing `+` | Group ring supplies a partial answer; no sign |
| [phase-147-row-d-single-prime-tower](phase-147-row-d-single-prime-tower/) | Single-prime Frobenius towers and Frob ⋆ Δ^rad (corpus check only) | Corpus check only |
| [phase-148-row-d-mixed-effectivity](phase-148-row-d-mixed-effectivity/) | Row D: mixed effectivity on the full square | Kill test outcome (i); no sign |
| [phase-149-row-d-additive-pencil](phase-149-row-d-additive-pencil/) | The additive pencil of `Spec Z` and the Deligne extraction | Extraction theorem D.59 PROVED; rationality wall |
| [phase-150-row-d-method-theorems](phase-150-row-d-method-theorems/) | Method theorems T3, T4, T5 (row D) | T5 PROVED, T4 reduced, T3 conditional; CLOSED, no sign |
| [phase-151-row-d-the-bridge](phase-151-row-d-the-bridge/) | "The bridge" (T6): can any nonnegative family supply Deligne's a priori pole over `Z`? | T6: no for nonnegative families; CLOSED |
| [phase-152-row-d-new-approach](phase-152-row-d-new-approach/) | Round 0: two never-analyzed non-positivity mechanisms (resonances/FUP; Berkovich–Poineau) | No route found; no impossibility proved |
| [phase-153-row-d-sign-carrying-endpoint](phase-153-row-d-sign-carrying-endpoint/) | Row D: does the certified endpoint carry sign? — **CLOSED** | D.12-α PROVED at ({∞,2,3}, log 2); CLOSED |
| [phase-154-row-d-law-of-the-body](phase-154-row-d-law-of-the-body/) | Row D: the law of the body → the dual-certificate theory of Weil positivity — rounds 1–4 CLOSED (phase open on P154.1) | Dual-certificate theory (Theorems A, O, D1, …); rounds 1–4 CLOSED |
| [phase-155-row-d-flat-kernel-criterion](phase-155-row-d-flat-kernel-criterion/) | Row D: class-dependent value bounds, and the flat-kernel criterion (opened) | Rounds 1–7 CLOSED; class-dependent bounds; retraction recorded |
| [phase-156-row-d-per-window-converse](phase-156-row-d-per-window-converse/) | Row D: the per-window converse and the residuals | CLOSED; reduced statement of row D |
| [phase-157-row-d-mechanism-search](phase-157-row-d-mechanism-search/) | Row D: the mechanism search under the proved filters | CLOSED; no survivor with an object |
| [phase-158-row-d-mw5-object](phase-158-row-d-mw5-object/) | Row D: building an MW-5 object | CLOSED; MW-5 not excluded, unbuilt |
| [phase-159-row-d-two-front-construction](phase-159-row-d-two-front-construction/) | Two fronts: constructing the object (G1) and the mechanism (G2) for row D | No object; one negative structural theorem |
| [phase-160-row-d-infinite-T](phase-160-row-d-infinite-T/) | Survey, brief, and round 1–2 construction attempts for row D beyond T > 0.8 | Survey done; no construction reached the goals; stopped |
| [phase-161-row-d-sum-product-square](phase-161-row-d-sum-product-square/) | Row D: the sum×product square | OPEN; product-Hardy port constructed |
| [phase-162-row-d-first-contact-closure](phase-162-row-d-first-contact-closure/) | Row D: the first-contact closure | λ_A continuity PROVED; Gate 1 OPEN |
| [phase-163-integrality-defect](phase-163-integrality-defect/) | Canonical exchange and integrality defect | Partial construction; OPEN |
| [phase-164-tail-theorem](phase-164-tail-theorem/) | The tail theorem | (★_cell) ⟹ (TC) tail theorem; (★_cell) OPEN |
| [phase-165-critical-interlacing](phase-165-critical-interlacing/) | Critical interlacing and the detection theorem | T_c bracket PROVED; geometric branch refuted |
| [phase-166-omega-closure](phase-166-omega-closure/) | Closing ω(E): the quartet's sign at first contact | Closed; requirements (G), (N′) for future routes; OPEN |
| [phase-167-witness-weighted-sieve](phase-167-witness-weighted-sieve/) | The witness-weighted sieve bound (WS) | (WS*) bound stated; unreachable by the sieve class |
| [phase-168-untried-inputs](phase-168-untried-inputs/) | Untried inputs: a semantic survey and audit of candidate mathematical mechanisms | Survey of untried inputs |
| [phase-169-input-architecture](phase-169-input-architecture/) | Architecture of the single missing input needed to close row D | Skeleton with one missing input 𝓘 |
| [phase-170-global-prime-inequality](phase-170-global-prime-inequality/) | The global inequality on the primes | OPEN; audit and formulation |
| [phase-171-discrete-beurling-frontier](phase-171-discrete-beurling-frontier/) | Discrete Beurling frontier: a counterexample with integer multiplicities | Discrete Beurling counterexample PROVED |
| [phase-172-p171-probe](phase-172-p171-probe/) | Using the phase-171 counterexample (P₁₇₁) as a probe | Dependency classification PROVED; working hypothesis refuted |
| [phase-173-object-01](phase-173-object-01/) | Construction attempt for object (0.1): a Hermitian form satisfying (Q1)–(Q4) | Adelic Schwartz–Bruhat route NO-GO |
| [phase-174-total-exclusion](phase-174-total-exclusion/) | Toward a general classification theorem excluding all standard constructions | Classification theorem pending; module construction PROVED |
| [phase-175-third-coordinate](phase-175-third-coordinate/) | Searching the literature for a geometric triple (H¹, Q, transfer map) | Literature: no geometric triple found |
| [phase-176-euler-poisson-transversality](phase-176-euler-poisson-transversality/) | Quick audit: a two-projection Euler–Poisson transversality proposal | Proposed reduction mod N not canonical (PROVED, negative) |
| [phase-177-euler-poisson-petz](phase-177-euler-poisson-petz/) | Euler–Poisson recovery law via conditional mutual information / Petz recovery | Divisor-fibre decomposition PROVED; no sign |
| [phase-178-fermionic-interference](phase-178-fermionic-interference/) | Fermionic interference and the sign gate | Two-mode cumulant takes both signs (PROVED, negative) |
| [phase-179-oriented-interference](phase-179-oriented-interference/) | The common-radical chain gate | Chain-gate identity PROVED |
| [phase-180-kadison-interference](phase-180-kadison-interference/) | Kadison equality and oriented Euler-Poisson interference | Kadison defect formula PROVED |
| [phase-181-complex-polarization](phase-181-complex-polarization/) | Complex polarization of the logarithmic prime current | Oriented square identity; no sign |
| [phase-182-rectangular-tunnel](phase-182-rectangular-tunnel/) | Rectangular Gram tunnel | Rectangular tunnel lemma PROVED |
| [phase-183-connes-consani-sufficiency](phase-183-connes-consani-sufficiency/) | Connes-Consani semilocal sufficiency | Rough-integer gap PROVED |
| [phase-184-frontier-and-residues](phase-184-frontier-and-residues/) | Frontier and live residues | Live residues decided round by round; no closure |
| [phase-185-crossword](phase-185-crossword/) | Filling in the crossword | Barrier theorems; no sign; D OPEN |
| [phase-186-toolbox](phase-186-toolbox/) | Toolbox to close D | Thm A/B and Cor (L1) PROVED; (L2) OPEN |
| [phase-187-pattern](phase-187-pattern/) | Campaign of 100 non-contiguous windows: data to extract the λ_A(T) pattern | Data for 100 windows (NUMERICAL) |
| [phase-188-closing-D](phase-188-closing-D/) | Closing D: the (L2) and (N) tracks, combs and one profile | Polar elimination lemma, positive combs PROVED; (L2), (N) OPEN |
| [phase-189-new-theory](phase-189-new-theory/) | A new theory aimed at the near-coincidence part of row D: the two-metric group and the height flow | New flow theory; row D OPEN |
| [phase-190-near-coincidence-experiment](phase-190-near-coincidence-experiment/) | Near-coincidence discovery experiment on the integer-lattice matrices A_M | A_M(Λ) ⪰ 0 at every point computed (NUMERICAL); critical decay |
| [phase-191-design-T-star](phase-191-design-T-star/) | Design specifications for a statement T* | Design specifications; no T* found |
| [phase-192-exact-identity](phase-192-exact-identity/) | Exact identity: three constructions on the minimizer and on the phase-190 family, with column bookkeeping | Exact identities; no sign |
| [phase-193-creation-campaign](phase-193-creation-campaign/) | Creation campaign | Candidates excluded front by front |
| [phase-194-invention](phase-194-invention/) | Invention | Invented objects; NO-GO on audit |
| [phase-195-modern-tools](phase-195-modern-tools/) | Modern tools | Modern tools; NO-GOs (e.g. real stability) |
| [phase-196-global-object](phase-196-global-object/) | The missing global object | No global object found |
| [phase-197-barrier-theorem](phase-197-barrier-theorem/) | Barrier theorem (tool, not an ending) | Barrier trichotomy theorem |
| [phase-198-parity-split](phase-198-parity-split/) | Parity split of row D (track AA) | Odd-sector form PROVED; D_odd only for T ≤ ½log5 |
| [phase-199-frontier-pattern](phase-199-frontier-pattern/) | Frontier pattern | Five certified frontiers; margin law NUMERICAL |
| [phase-200-sign-object](phase-200-sign-object/) | The sign object | Ledger and specification; no object |
| [phase-201-untried-families](phase-201-untried-families/) | Families nobody used | Six viable families selected; no sign |
| [phase-202-exterior-plank](phase-202-exterior-plank/) | The exterior table (★★): direct attempt | Direct attempt; no proof |
| [phase-203-invent](phase-203-invent/) | Variation of the extremal with respect to the comb; three proper objects | Retracted reading refuted; three objects, no sign |
| [phase-204-refd-tractability](phase-204-refd-tractability/) | Discarded reformulations: does any of them resolve independently of D? | Tractability review; partial |
| [phase-205-composing-object](phase-205-composing-object/) | The object that composes E and F | Pieces PROVED; no sign node |
| [phase-206-node-and-rigidity](phase-206-node-and-rigidity/) | The node (step 4) and the rigidity family E∧F | Node PROVED for T ≤ ½log5; OPEN in general |
| [phase-207-class-impossibility-and-empty-cell](phase-207-class-impossibility-and-empty-cell/) | (1) Class impossibility theorem; (2) The empty-cell object | Class impossibility theorem; empty-cell object |
| [phase-208-node-scope-audit](phase-208-node-scope-audit/) | Audit of the node's scope | Restrictions consolidated; no new route |
| [phase-209-nonlocal-kernel](phase-209-nonlocal-kernel/) | A genuine two-variable kernel (program O1); nonlocal kernel | D OPEN; goal blocked after LINK_016 |
| [phase-210-qrh-four-fifths](phase-210-qrh-four-fifths/) | Quasi-RH exponent study, from 7/8 to 4/5 (zero-free half-plane Re s > 4/5); independent of row D | Theorem R PROVED conditional on MS(α) |
| [phase-211-sign-sandbox](phase-211-sign-sandbox/) | The sign of the Paper 46 window form, treated as an isolated problem | (★) PROVED for T ≤ ½log5, global sign OPEN |
| [phase-212-missing-object](phase-212-missing-object/) | Construction of the object that carries the sign | No construction meets OBJECT_SPEC; OPEN |
| [phase-213-new-constructions](phase-213-new-constructions/) | New constructions for the global positivity of the Paper 46 form | Global positivity OPEN; rounds with stated labels |
| [phase-214](phase-214/) | An explicit lower bound W_T(f) ≥ exp(−K)‖f‖₂² on every window, from the positive representation; reconstruction notes on the arithmetic inputs of Paper 46 | Bound PROVED conditional on the spectral conclusion of Paper 46; target theorem of the reconstruction not proved |

Notes. There are no folders for phases 1 and 2. Two `phase-44-*` and two `phase-147-*` folders exist
(parallel threads under the same number). The hidden folder
[`.phase-102-discard/`](.phase-102-discard/) holds discarded phase-102 material. The folder name
`phase-4-handoff` is historical; the phase is the Kreĭn-space realization described in its README.
