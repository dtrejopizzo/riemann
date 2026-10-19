# Audit of RH4–RH6

## Executive verdict

The three programs leave a useful base of instrumentation, controls, and counterexamples, but not a
chain toward RH. RH4 discards its central premise: negative inter-class covariance and a singular role
for \(\omega=2\). RH5 correctly identifies that zero Gram matrices are PSD by construction and,
therefore, cannot detect a horizontal deviation. RH6 supplies an interesting numerical calibration of
the localized Weil formulary, but does not resolve — nor can it substitute for — the uniform step from
finite data to Weil positivity. That step is precisely equivalent to RH when formulated for the whole
class of admissible tests.

The joint reading imposes a strict separation between:

1. elementary identities and inequalities of the \(\omega(n)\) decomposition;
2. numerical results for fixed length, window, normalization, and family;
3. classical equivalences with RH; and
4. inferences that do not survive construction, truncation, or cross-family validation controls.

## Status convention

| Status | Meaning in this inventory |
|---|---|
| **PROVED** | Self-contained derivation or correctly applied classical theorem, with no essential numerical step. |
| **CONDITIONAL** | Valid after adding an explicit unproved hypothesis. |
| **NUMERICAL** | Observed in the indicated data, mesh, precision, and controls; not extrapolable by itself. |
| **CONJECTURAL** | Proposal without proof or sufficient validation. |
| **REFUTED** | Contradicted by the audit or by the prescribed control. |
| **EQUIVALENT-REFORMULATION-OF-RH** | Correct criterion whose universal closure is RH under another formulation. |

## Documentary coverage

The three `README.md` files and all existing `OVERVIEW.md` files were read. Notebooks, result files,
and mathematical sources were used only to check points that change the verdict: DH normalization, PSD
matrices, the explicit formula, zero lists, moments, and shift scales.

| Program | Directories covered | Directories without an answer | Use in the synthesis |
|---|---|---|---|
| RH4 | `task1`–`task83` | `task11`, `task19`, `task22`, `task35`, `task39`, `task46`, `task49`, `task60`, `task68`, `task70`, `task73` | \(\omega\) engine, classification, arithmetic ablation, inverse-bridge attempts, and audit of inherited assumptions. |
| RH5 | `task1`–`task60` | `task5` | Reconstruction from zeros, power calibrations, Jacobi/Gram/Weil, TDA, and a bottleneck log. |
| RH6 | `task1`–`task68` | `task7`, `task26` | Localized Weil form, zero generation, \(\omega\)-moments, H0 persistence, and sensitivity tests. |

The table's intervals are inclusive: they constitute the complete list of `task` directories for each
program, including those without an answer.

## RH4 — reconstruction

### Goal and actual method

RH4 tried to turn peak statistics of Dirichlet polynomials stratified by \(\omega(n)\) into an
analytic chain distinguishing functions with and without off-line zeros. The design combined:

- an audit of the Davenport–Heilbronn constant and coefficients;
- the decomposition \(D=\sum_k S_k\), peak matrices
  \(M_{jk}=\mathbb E\,\Re(S_j\overline{S_k})\), amplification ratios, and spectral entropies;
- classification with per-family and per-time-window controls;
- zero injection into a truncated explicit formula; and
- coefficient ablations at ramified primes.

The important methodological result is negative: \(M_{jk}\) is, above all, an observable of
coefficients, conductor, support, and peak conditioning. It does not behave as an inverse
reconstruction of a zero's real part.

### Claim ledger

| Claim | Status | Evidence and scope |
|---|---|---|
| DH's \(\kappa\) is real, about \(0.28408\), and not \((1+i)/2\) | **NUMERICAL** | Vanishing at the four canonical zeros and coherence with the functional equation resolve the operative inconsistency. The phase derivation must be kept separate from the truncated-sum check. |
| Kahan/`mpmath` validation and \(\sum_kS_k=D\) | **NUMERICAL** | About twelve-digit agreement on the completed sample; the audit records that not all planned points were completed. It is an engine certificate, not an RH property. |
| The bound \(1+r\le K_N\) and \(|D|^2\le K_N^2\max_k|S_k|^2\) | **PROVED** | Cauchy–Schwarz and class counting. Does not depend on peaks or zeros. |
| \(\max_{t,k}|S_k(t;N)|^2\le N^\varepsilon\Rightarrow\) Lindelöf | **CONDITIONAL** | The implication is sufficient and stronger than Lindelöf; it is not an equivalence and does not imply RH. |
| 67% predominance of negative off-diagonal covariances | **REFUTED** | `task55` and the synthesis: resampling intervals include 50% and exclude 67% in the largest run; peak conditioning shifts the pattern toward positive couplings. |
| \(\omega=2\) as the sole cause of an approximately 30% change | **REFUTED** | `task47`: \(\omega=1,2,3\) have comparable masses and ablations; the Erdős–Kac maximum explains a large contribution, not a singularity. |
| Positive, low-dimensional leading mode in peak matrices | **NUMERICAL** | Reappears for \(\zeta\) and DH. Describes conditioned constructive interference; does not by itself separate RH from non-RH. |
| Spectral entropy of averaged matrices as a separator of the available classes | **NUMERICAL** | Strong separation in the panel and LOOCV near 10/11, but Liouville is a counterexample to the "RH" reading; the class size is small and the constructed functions do not form a sample of the Selberg class. |
| Peak classifier as proof of a universal signature | **REFUTED** | Per-family, temporal, and per-class validations show AUC falling toward chance or F4/F12 asymmetries. The in-sample and stratified-bootstrap figures measure family identity. |
| \(M_{kk}\) is scaled by \(C_k=\sum_{\omega(n)=k}|a_n|^2/n\) | **NUMERICAL** | Strong log-log relation and moderate linear relation; peak conditioning adds class- and stratum-dependent amplification. |
| Unconditioned cross-moments predict \(M_{jk}\) | **REFUTED** | The global fit is weak; the within-class fit does not authorize a transversal law. |
| Injecting one or four DH zeros reproduces \(M_{jk}(DH)-M_{jk}(\zeta)\) | **REFUTED** | `task25`; sign and norm mismatch. The F12-versus-\(\zeta\) analogue also fails in `task26`. |
| Ablating multiples of conductor primes reproduces DH/F12 differences against \(\zeta\) | **NUMERICAL** | High cosine similarities in the tested pairs. Explains a specific arithmetic mechanism, not a law for every \(L\)-function. |
| An off-line zero's location can be recovered from norms/spectra of \(\Delta M\) | **REFUTED** | No stable correlation with \(\beta\); after removing \(|\kappa|\), the signal disappears. |
| The inherited GEV fit with blocks \(2\pi/\log N\) | **REFUTED** | Switching to \(2\pi/\log T\) moves the parameter outside the inherited interval. |

### Dependencies, retractions, and closed routes

1. The DH, F12, and F14 controls are constructions without an Euler product or additive combinations.
   They serve to refute inferences, but a binary "GRH true/false" label on that set does not identify a
   universal property of the Selberg class.
2. Columns `S_0` and, for modulus-5 families at this length, `S_7`, are structural leaks. They must not
   enter a classifier as arithmetic evidence.
3. The following are withdrawn: negative inter-class signal, \(S_2\) exceptionality, prediction by
   degree/conductor, in-sample/LOOCV SVM as a frank test, and inverse zero reconstruction from
   \(M_{jk}\).
4. The valid inheritance is more modest: use the \(\omega\) decomposition as energy accounting and as a
   control bank to distinguish coefficient effects from zero effects. Do not again present a peak
   signature as a bridge to RH without a theorem eliminating those confounders.

## RH5 — reconstruction

### Goal and actual method

RH5 shifted focus to zero lists: reconstruction of Jacobi matrices, Li coefficients, Mercer matrices,
Weil forms, and TDA. It introduced a healthy calibration: deform \(\zeta\)'s zeros and measure
sensitivity before interpreting an observable. It also documented zero-list generation and precision
failures for DH, \(L(\chi)\), and \(L(\Delta)\).

### Claim ledger

| Claim | Status | Evidence and scope |
|---|---|---|
| A Gram matrix built only from on-line zero evaluations can generate negativity | **REFUTED** | It is PSD by construction. Positivity of such a matrix is tautological and does not prove RH. |
| Jacobi reconstructions using only ordinates detect horizontal shifts | **REFUTED** | The real coordinate was discarded; the power calibration shows structural blindness. |
| Finite positive Li coefficients verify RH | **REFUTED** | Positivity for every index is Li's criterion; verifying a finite stretch does not transfer to infinity. |
| Li's criterion / universal Weil positivity | **EQUIVALENT-REFORMULATION-OF-RH** | These are classical equivalences, useful for locating the obstacle, not solutions by truncation. |
| TDA H1 and numerical variance separate DH from the available controls | **NUMERICAL** | Finite separation of a counterexample without an Euler product; there is no implication for RH nor invariance across families. |
| The localized Weil form, subtracting the full arithmetic side, detects a DH anomaly near its height | **NUMERICAL** | Local calibration and controls are informative as a detector of a known anomaly. They do not exclude unknown zeros. |
| A finite zero list and finite prime cutoff allow concluding global positivity/nonexistence | **REFUTED** | The ledger itself acknowledges zero tails, arithmetic cutoff, basis dependence, and absence of a uniform bound. |
| Generation of the target-size catalogs | **REFUTED** | Several tasks end with partial lists, effective precision below what is required, or interrupted processes. Any analysis presupposing complete catalogs must be marked incomplete. |

### Circularity that must be corrected

There are two different objects that must be kept separate.

- The Weil form \(B(f,f)\), defined by the explicit formula, has universal positivity equivalent to RH.
- The numerical discrepancy "zero side minus truncated arithmetic side" is a truncation residue. When
  both sides are complete, the explicit formula equates them; that discrepancy is not itself a new
  positive form.

Therefore, a claim that a uniform bound on the finite-section residue implies universal positivity must
prove a new inequality that does not presuppose Weil's criterion. If the uniform bound is already
equivalent to Weil positivity, the step is **EQUIVALENT-REFORMULATION-OF-RH**, not an available technical
lemma. This distinction prevents confusing an excellent detector calibration with deductive progress
toward RH.

### Inheritance and no-go

Keep: calibration via controlled shifts, resolution-versus-\(\delta\) comparison, and the requirement of
convergence curves for deterministic objects. Do not repeat: Gram PSD as a detector, extrapolating
finite Li/Mercer signs, calling TDA a "proof", or regenerating in each task lists that should be a single
validated artifact.

## RH6 — reconstruction

### Goal and actual method

RH6 concentrated effort on a localized Hermite–Gauss basis for the explicit formula, sensitivity to
zero shifts, and \(\omega\)-class moments. It is the program with the best separation between an
operative detector and the proof gap, although its own tasks reveal scale and data inconsistencies that
prevent elevating the result.

### Claim ledger

| Claim | Status | Evidence and scope |
|---|---|---|
| A zeros-only form is PSD | **PROVED** | Sum of outer products. Explains `task44`'s failure and closes off that route. |
| The H0 response to a small horizontal shift is quadratic | **PROVED** | For the vertical-cloud model, \(\sqrt{s^2+\delta^2}-s=O(\delta^2)\); the bottleneck and Wasserstein measurements agree. |
| H0 separates DH from controls at comparable heights | **REFUTED** | Non-significant permutations and strong confounding by height range. |
| Second-moment fractions by \(\omega\) converge to a signature | **REFUTED** | They migrate with \(N\), as Erdős–Kac anticipates. |
| Moment-fit exponents distinguish \(\zeta\), \(L(\Delta)\), DH on the available mesh | **NUMERICAL** | Descriptive fits over few values of \(N\); unstable on removing a point and window-dependent. |
| Fourth-moment decomposition gives a finite fingerprint of the Euler product | **NUMERICAL** | Residuals change sign and magnitude with window and length; it is a description of a finite regime. |
| The localized form detects a prescribed \(\zeta\) deformation and the DH anomaly when centered nearby | **NUMERICAL** | Well-calibrated spatial and basis sensitivity; depends on knowing height, geometry, and the arithmetic side. |
| Quadratic law in \(\delta\) for a shifted symmetric quartet | **NUMERICAL** | `task32` gives an exponent near two in that setup. |
| Universal linear law in the real shift | **REFUTED** | `task68` reports a linear law in a different setup; both cannot be the same universal law. Parity, which zeros shift, and the matrix definition must be declared before comparing. |
| Superpolynomial amplification with basis dimension | **NUMERICAL** | Sensitive to truncation, center, and incomplete arithmetic; not a uniform bound in \(J\). |
| Hermite–Gauss prime tail controlled sufficiently to pass to RH | **CONDITIONAL** | A kernel's Gaussian decay can bound a tail for fixed parameters, but a joint bound in center, width, dimension, zero tail, and normalization is missing. Without it there is no global transfer. |
| Finite localized positivity implies RH | **REFUTED** | Rule R6/R7 and the results acknowledge it: it is a finite section, not the form over every test. |
| Weil positivity for every admissible test is equivalent to RH | **EQUIVALENT-REFORMULATION-OF-RH** | This is the problem's correct framework; the new part must be an independent inequality reaching that quantification. |

### Open dependencies and operative errors

- The catalogs required by the caching rule were not all present; repeated DH generation tasks ended at
  partial checkpoints. Lists of different completeness must not be mixed as if they were the same
  experiment.
- Sign and scale consistency of \(Q\) requires a single specification of transform, polar/archimedean
  contributions, quartet symmetrization, and each truncation's error. The divergence between the linear
  and quadratic laws is a specification alarm, not a new physical phenomenon.
- Claims about Keating–Snaith and moment limits need an asymptotic regime and error bounds; four or
  fewer values of \(N\) do not provide that.

### Valid inheritance and routes not to repeat

Keep the local power proof, basis/cutoff controls, the separation of data error from formula error, and
the H0 no-go. Do not repeat: using DH as the sole substitute for a general alternative to RH, promoting
exponent fits to asymptotic laws, or treating cancellation of the explicit-formula residue as a new
positivity.

## Cross-cutting dependencies and decision map

| Component | Inheritable result | Non-negotiable limit |
|---|---|---|
| \(\omega\) decomposition | Energy accounting, support controls, and arithmetic-confounder testing | Not an RH criterion nor an inverse zero predictor. |
| Classification | Diagnostic for building controls and detecting variable leakage | Does not substitute for a mathematical quantification; constructed classes are not a distribution of counterexamples. |
| DH and additive combinations | Counterexamples to invalidate inferences using only the functional equation | Do not represent a family of \(L\)-functions with an Euler product. |
| TDA | Auxiliary geometric measurement and the H0 no-go | No finite cloud distance proves a claim about every zero. |
| Weil form | The exact framework in which RH is positivity | The uniform step from truncations to every test is the problem, not a consequence of the simulation. |

## Recommended global reformulation

1. Fix a single target object: the classical Weil form, with domain, Fourier convention, and complete
   terms written once. Explicitly distinguish the form from its truncated numerical residue.
2. Formulate any new lemma as a verifiable uniform inequality that does not assume Weil positivity. It
   must simultaneously quantify basis dimension, center, width, prime cutoff, and zero tail. If its
   conclusion is positivity for every test, classify it from the start as
   **EQUIVALENT-REFORMULATION-OF-RH**.
3. Keep RH4/RH6 only as a falsification bank: before attributing an effect to zeros, rule out
   coefficients, conductor, support, window, peak selection, and normalization. The minimal proof must
   survive controls with an Euler product and synthetic deformations whose arithmetic side is coherently
   defined.
4. Freeze versioned zero catalogs, with a coverage and precision certificate. No later result may combine
   partial checkpoints with complete lists without flagging the effective cutoff.
5. Treat the moment, entropy, and TDA fingerprints as negative or descriptive numerical results, never
   as proof milestones. The only front retaining logical relevance is a new uniform estimate for the
   Weil form, with a prior adversarial circularity audit.

## Critical findings not to lose

- The negative-interference hypothesis that motivated the omega front is withdrawn; the observed peaks
  are constructive and the \(\omega=2\) mass is not singular.
- Peak matrices mainly encode coefficient arithmetic; the success of ramified-prime ablations and the
  failure of zero injections close off the proposed inverse bridge.
- Every zeros-only Gram positivity is tautological. The Weil form and the truncated discrepancy must
  stop being interchanged in language and in code.
- The localized form is a calibrated numerical detector, not an exclusion of every off-line zero. Its
  uniform obstacle is the real core of RH under that formulation.
- H0, the classifiers, and the moment fits remain as no-go results or finite phenomenology; they must
  not receive proof-level budget.
