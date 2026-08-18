# Program 10 — The Research Program (Phases 0–107)

This folder is the core of the project: a single continuous research program on the Riemann
Hypothesis, run as a sequence of numbered phases (currently through **phase 107**) after nine
early exploratory computational programs (now conducted in Lise Science)
(see [`../01-context/`](../01-context/), *Research Programs 1–9*).

Each `phase-*/` folder is a self-contained block of work: setup, attacks, audits, and a
verdict. The program's governing principle is **absolute candor** — *a false victory would
be worse than a failure*. No proof of RH was reached; every wall and every dead end is named.

> **Language note.** Phase folder names are in English. Front-door and per-phase *summary*
> documents are in English; some granular working notes inside the phases remain in their
> original Spanish (they are the raw research record). See [`../00-README.md`](../00-README.md).

## How the phases connect to the papers

The publishable results distilled from these phases live in [`../04-papers/`](../04-papers/)
(catalogued in [`../04-papers/README.md`](../04-papers/README.md)).
The complete narrative is in
[`../COMPLETE-PROGRAM-SUMMARY.md`](../COMPLETE-PROGRAM-SUMMARY.md) and
[`../00-MAP.md`](../00-MAP.md); every refuted approach is logged in
[`../NO-GO-LIST.md`](../NO-GO-LIST.md).

## Phase index

| Phase | Theme |
|---|---|
| phase-0-foundations | The Weil form Q in Weil–Guinand language; normalization pinned |
| phase-3-uniform-inequality | Stability geometry of the localized Weil quadratic form (Lise Science run 9) |
| phase-4-handoff | Faithful semibounded Kreĭn realization of the Weil functional (Theorem B-2) |
| phase-5-structural | The semi-local Connes residual; PW_d ↔ prolate question |
| phase-6 | The Weil form as an Osterwalder–Schrader reflection-positive form (per-place positivity fails) |
| phase-7 | Second order: Weil–Carleson form = sine-kernel determinantal process |
| phase-8 | A clean monotonicity theorem; why the heat flow alone cannot prove RH |
| phase-9 | Verdict N6; forced pivot to unconditional partial results |
| phase-10 | Deep run (M=25, T≤10⁴, 10154 ζ-zeros); Hodge-index entry |
| phase-11 | Interlacing = total positivity; the wrong-sign capstone behind it |
| phase-12 | Multiplicative chaos; the capstone first escaped (N7 barrier) |
| phase-13 | The ω-class structure of ζ's multiplicative-chaos exponents (RH-independent) |
| phase-14 | The anchor framework: a ζ-free classification of zero-absence mechanisms |
| phase-15 | The Anatomy–Kreĭn–Hodge program; spectral entry to the arithmetic Hodge index |
| phase-16 | SURF specification sheet — acceptance criteria for the witness variety |
| phase-17 | SURF 2.0 internal design (involution / resolvent routes) |
| phase-18 | A portrait of the negative directions of the Weil form |
| phase-19 | The forward flow of the ω-class (closure document) |
| phase-20 | The zero–ω bridge: the information barrier |
| phase-21 | Geometry of negative directions |
| phase-22 | Arithmetic consequences of the finite Pontryagin defect |
| phase-23 | Two-scale structure and spectral compatibility of the defect |
| phase-24 | Lower bounds for b_j and local rigidity of log\|ζ\| |
| phase-25 | Lower bounds for b_j: full audit of classical mechanisms (15 no-goes) |
| phase-26 | The bridge theorem: Kreĭn ↔ Connes |
| phase-27 | Adelic rigidity (Hasse–Minkowski wall) |
| phase-28 | Four simultaneous fronts; all reduce to ξ ∈ Laguerre–Pólya |
| phase-29 | Zeta spectral triples: precise setup |
| phase-30 | The Langlands bridge: C_∞ for automorphic L-functions |
| phase-31 | Moments of C_∞(γ_n) and the Selberg theorem |
| phase-32-ccm | Bridge between the CCM program and the C_∞ deficit |
| phase-33-dbn | de Bruijn–Newman and the CCM trace; Λ as extinction time |
| phase-34-new-directions | External arithmetic information via the explicit formula (inverse Jacobi, Pontryagin) |
| phase-35-five-fronts | Five fronts; off-critical quadruple toy tests; H_x convergence / CF rigidity |
| phase-36-ABC-forms | Effective SR_d; two-prime 2D coupling; the sieve–index bridge |
| phase-37-physics | The critical-anchoring principle: what forces Λ=0? |
| phase-38-final-audit | Adversarial audit of the W_λ positivity / sharpening claims |
| phase-39-G1G2-interface | The forced axioms: backward derivation of the cohomology requirements |
| phase-40-close-G1 | The symmetry bit; duality pairing on the divisor |
| phase-41-build-G2 | The intersection form on the square of the scaling site |
| phase-42-hodge-dynamics | Dynamical Hodge theory as a foliated Kähler-package framework (Deninger) |
| phase-43-hodge-foliated-specZ | Does the foliated Spec ℤ admit a polarizable Hodge structure? |
| phase-44-new-mathematics | The algebra of arithmetic correspondences: the category 𝒜rith |
| phase-44-creative-breakthrough | Hodge–Witt and visible inertia |
| phase-45-fredholm | The Weil–Toeplitz algebra: symbol, compact ideal, two-prime theorem |
| phase-46-audit-and-attacks | Adversarial audit of the local-purity theorem; semilocal attacks |
| phase-47-live-fronts | Attack on the Paley–Wiener finiteness pivot (LP-141) |
| phase-48-audit-and-purity | Audits of the revival attempts; purity/rigidity attacks |
| phase-49-cross-the-wall | Taxonomy of "average → individual" crossings; Tauberian / Maslov probes |
| phase-50-diophantine-thread | Is ℚ-linear independence of {log p} the certificate? |
| phase-51-functor-construction | Constructing the phase→inertia functor/transport |
| phase-52-homotopy-inertia | Homotopy inertia: is m a metric-free secondary invariant? |
| phase-53-quantum-import | Importing Stone's theorem: structural unitary evolution |
| phase-54-index-dynamics | Deformation theory of the metric space over the Kreĭn space; κ dynamics |
| phase-55-two-arrows | The structural representation of I(0⁺): sum-rules, the shadow theorem |
| phase-56-two-towers | Lemma 177.B by three routes (gap-ODE, KKL, polylog repulsion) |
| phase-57-brick-A | The desingularized Dirichlet energy identity |
| phase-58-full-audit | Adversarial audit of the energy dichotomy and GAP 175 |
| phase-59-full-closure | Adversarial audit of the universal moment floor; closure ledger |
| phase-60-discriminant | The discriminant: isolate the arithmetic invariant controlling the Weil sign (NG-F1 no-go) |
| phase-61-open-problems | Open-problems inventory (CCM frame); what remains genuinely open |
| phase-62-cesaro-closure | Cesàro-in-λ attack on 2.3.F boundedness (NG-62 no-go: averaging is RH-equivalent, not neutral; `b_bulk` is a detector) |
| phase-63-lefschetz-realization | MW-5 realization frontier (NG-63): F_q has J-linear Frobenius + gapped polarization, ζ window has antilinear scaling + gapless — MW-5 made precise by direct contrast |
| phase-64-connes-route | Connes' route: L1 reclassified as RH criterion (Task A confirmed; D proven parity no-go); target = regularized positivity (relative determinant / de Branges Schur), not finite gap |
| phase-65-signature-continuity | Signature-continuity package: index-graded determinant/topology; wall = renormalization-stable self-adjoint completion |
| phase-66-rank-one-escape | Rank-one escape and whitening calibration; scalar whitening fails, matrix whitening is essential |
| phase-67-quantum-q-index | Quantum/q-index route; q-overlay and leakage of off-line directions audited, Woronowicz/free-product no-goes |
| phase-68-glt-symbol | GLT/Toeplitz symbol route; symbol positivity is gauge-fragile and does not close Ω7 |
| phase-69-exact-signed-index | Gauge-free Nevanlinna/signed-index formulation; detector solid, forcing mechanism still absent |
| phase-70-lee-yang-dbn | Lee-Yang / de Bruijn-Newman route; Ω7 localized to Λ≤0, the arithmetic direction |
| phase-71-cand1-convergence | CAND-1/CCM finite self-adjoint convergence; real finite zeros are automatic, content is stable-divisor convergence |
| phase-72-feshbach-leakage-calculus | New pole-relative Feshbach leakage calculus; replaces global residual convergence by one-vector arithmetic leakage below the prolate gap |
| phase-73-cauchy-projection | Cauchy projection gate; the transformed compact branch reduced to the single finite Cauchy-Schur nodal identity NAT-PROJ |
| phase-74-hilbert-eigenline-cancellation | Hilbert eigenline cancellation; NAT-PROJ reduced to an exact Hilbert product rule (HPR-DIV) on the projected eigenline |
| phase-75-arithmetic-numerator-divisibility | Arithmetic numerator divisibility; attacks the ARITH-LOCK ⇒ CCM-ROOT-LOCK ⇒ CRIT-NUM-DIV ⇒ CAUCHY-EIG-LOC ⇒ HPR-DIV chain via a new signed arithmetic identity |
| phase-76-normalized-adjugate-arithmetic-lock | Normalized adjugate arithmetic lock; safe-ratio closure theorem SR-SAFE ⇒ Ω7, exact Sherman–Morrison/displacement algebra, and the closing split SAFE-LIMIT-POINT = LP ∧ IDENT (closed at 67 documents; see PHASE_76_CLOSURE.md) |
| phase-77-weyl-limit-point | Weyl limit-point closure; proves (or refutes) LP (limit-point for the semi-infinite CCM system, via Kato–Putnam on the rank-two displacement commutator) and IDENT (Gamma-prime identification in absolute convergence), the two halves left by phase 76 |
| phase-78-build-neutral-lp-and-ident | Build-neutral LP and IDENT: separating the two halves from the construction that produced them |
| phase-79-shared-convergence-and-ident-discriminant | The shared convergence lemma (GAP-Z) and the IDENT discriminant |
| phase-80-relative-determinant-identification | Relative determinant identification |
| phase-81-secular-arithmetic-anchor | Secular arithmetic anchor |
| phase-82-coupled-generator-continuum | Coupled generator continuum |
| phase-83-gamma-euler-coboundary | Gamma–Euler arithmetic coboundary |
| phase-84-distributional-endpoint-module | Distributional endpoint module |
| phase-85-parity-weyl-defect | Parity Weyl defect |
| phase-86-signed-spectral-abel | Signed spectral Abel reduction |
| phase-87-euler-deformation-discriminant | Euler deformation discriminant |
| phase-88-endpoint-layer-pencil | Endpoint layer pencil |
| phase-89-projective-layer-rotation | Projective layer rotation |
| phase-90-projective-kato-euler-current | Projective Kato–Euler current |
| phase-91-kato-coboundary-equivalence | Kato–coboundary equivalence |
| phase-92-cluster-adjugate-projectivization | Cluster adjugate projectivization |
| phase-93-direct-bordered-anchor | Direct bordered anchor |
| phase-94-global-cofactor-cell-current | Global cofactor cell current |
| phase-95-characteristic-jacobian-current | Characteristic Jacobian current |
| phase-96-determinantal-prime-response | Determinantal prime response |
| phase-97-euler-sensitivity-commutator | Euler sensitivity commutator |
| phase-98-sensitivity-shell-split | Sensitivity shell split |
| phase-99-adjugate-boundary-sandwich | Adjugate boundary sandwich |
| phase-100-characteristic-cofactor-factorization | Characteristic cofactor factorization |
| phase-101-covariant-bordered-current | Covariant bordered current; planted-falsifier controls |
| phase-102-omega7-closure-campaign | Omega-7 closure campaign; finite certificates and the surviving direct inequality |
| phase-103-direct-a1-closure | Exact direct-A1 reduction, compact--tail identity, finite certificates and Laguerre transport |
| phase-104-unconditional-a1-closure | Unconditional A1 campaign; exact equivalences, Deep/Blaschke reduction and adversarial closure ledger |
| phase-105-a1-geometry-and-deep-limit | Visual geometry of A1 and the literal Deep limit; clean restart from the two surviving targets |
| phase-106-global-modular-star-audit | Global modular-star audit; self-adjoint Euler determinant no-go, second-resolvent target, and adelic half-density descent obstruction |
| phase-107-arithmetic-lefschetz-reconstruction | Reverse engineering of a finite-support arithmetic Lefschetz divisor; function-field calibration, proper-global support rule, exact radical audit, and arithmetic surface program |
| phase-108-row-a-construction | Row (a): the space over ℤ; the graded family, and the closure of principal invariance and of both pairing routes |
| phase-109-one-sided-pairing | Does the one-sided assembly carry a pairing? No: any pairing reading the prime-power coefficients is blind to the zeros, for every kernel |
| phase-110-principal-xi-divisibility | Does ξ-divisibility supply the principal subspace row (d) needs? Impossible on compactly supported data, by a growth argument independent of the zeros |
| phase-111-schwartz-admissibility | Does I_∂ converge on Schwartz-class data? The threshold, and Assumption T |
| phase-112-effective-cone | Requirement d5, the effective cone — satisfied formally; superseded by 113_10 |
| phase-113-the-trace-on-schwartz-data | The trace on Schwartz data: rad = the χ-ideal, a Frobenius \*-algebra with a zero-free trace, d0/d2/d4/d5/K=0 built, d3 impossible inside 𝒟 — and row (d) proved **equivalent to RH** |
| phase-114-closing-the-four-rows | Rows (a)–(c) completed and written up (paper 42); row (d) reduced to the sharp Douglas gate and then to one explicit joint residual — but the local-construction campaign re-proved two obstructions already in the paper |
| phase-115-the-mixed-class-and-the-green-extension | Row (d) is missing an **object**, not an inequality: row (a)'s Green term is a rank cut r→1 (`ℓℓᵀ − diag ℓ`) and row (a) attains B=0 on its own primitive space — so it is row (d)'s equality case. Target: the mixed class **M**_f |
| phase-116-the-logarithmic-schur-angle-conjecture | Audits and rejects a proposed Cauchy–Schwarz/Gamma-gap closure of row (d)'s constant/mean-zero Schur block, then extracts and names the estimate that survives: the Logarithmic Schur Angle Conjecture, ρ_N ≤ 1/(20 log N). Carried verbatim into paper 42, where row (d) is completed **conditionally** on it |
| phase-117-the-transfer-comparison-measured | Measures the one item neither paper nor corpus addressed — the comparison carrying the Gamma–Tate *source model* to the *exact* threshold condition. **c_N < 1 at every threshold, decaying like (log N)^-0.6: the source route does not reach the target.** Galerkin bounds c_N from above, so this is one-sided-robust. Also falsifies ρ_N ≤ 1/(20 log N) at 4 of the 5 points in paper 42's own audit table. The exact target *does* hold on every threshold tested — so the redirect is to prove it directly in the output-defect metric |

| phase-118-the-exact-threshold-inequality | Attacks the exact threshold condition directly — and **verifies against real zeros of ζ, to 10 digits, that `⟨A_T F,F⟩ = Σ_ρ h(γ_ρ)`**. The row-(d) inequality *is* localized Weil positivity on the primitive space, hence equivalent to RH (Weil 1952; Yoshida 1992; Bombieri 2000), so no internal reformulation can close it. `m₀`, the primitive space and the truncation all turn out **forced**, not chosen. Also: balanced factorization re-verified by an independent code path; Toeplitz/Hankel structure for the scattering operator refuted; the log-2 certificate reproduced and its limit diagnosed as analytic, not numerical. Closed |
| phase-119-what-a-finite-compression-certifies | Pivot: stop asking whether Weil's form is positive (that question's only answer is RH) and ask what a **finite compression** certifies unconditionally — its inertia constrained by Sylvester, its moments computable from the prime side. Distinctive assets: the exact filtration, the balanced factorization as a second signature decomposition, a working Arb pipeline. Gated on the Davenport–Heilbronn test: does `Λ(n) = deg_det 𝕃_n` separate ζ from an object whose RH-analogue is false? |

*Note: there are two `phase-44-*` folders (parallel threads run under that number).*

*The phase index runs through **phase 119**; the header's "Phases 0–107" refers
to the original scope of this folder.  The backward-map audit that organises
phases 107–113 is [`THE_BACKWARD_MAP.md`](THE_BACKWARD_MAP.md).*
