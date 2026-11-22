# RH2020–RH2022 Audit

## Executive verdict

The three programs leave a useful base of instrumentation, controls and
counterexamples, but not a chain toward RH. RH2020 discards its central premise:
negative inter-class covariance and a singular role for \(\omega=2\). RH2021
correctly identifies that zero Gram matrices are PSD by construction and,
therefore, cannot detect a horizontal deviation. RH2022 provides an interesting
numerical calibration of the localized Weil formulary, but does not resolve
—nor can it replace— the uniform step from finite data to Weil positivity.
That step is precisely equivalent to RH when formulated for the entire class
of admissible test functions.

The joint reading imposes a strict separation between:

1. elementary identities and inequalities of the decomposition by
   \(\omega(n)\);
2. numerical results of fixed length, window, normalization and family;
3. classical equivalences with RH; and
4. inferences that do not survive construction, truncation or
   family-validation controls.

## State convention

| State | Meaning in this inventory |
|---|---|
| **PROVED** | Self-contained derivation or classical theorem correctly applied, without an essential numerical step. |
| **CONDITIONAL** | Valid when adding an explicit, unproved hypothesis. |
| **NUMERICAL** | Observed in the indicated data, mesh, precision and controls; not extrapolable by itself. |
| **CONJECTURAL** | Proposal without proof or sufficient validation. |
| **REFUTED** | Contradicted by the audit or by the prescribed control. |
| **EQUIVALENT-REFORMULATION-TO-RH** | Correct criterion whose universal closure is RH under another formulation. |

## Documentary coverage

The three `README.md` files and every existing `OVERVIEW.md` were read. The
notebooks, result files and mathematical sources were used only to check
points that change the verdict: DH normalization, PSD matrices, explicit
formula, zero lists, moments and shift scales.

| Program | Directories covered | Directories without an answer | Use in the synthesis |
|---|---|---|---|
| RH2020 | `task1`–`task83` | `task11`, `task19`, `task22`, `task35`, `task39`, `task46`, `task49`, `task60`, `task68`, `task70`, `task73` | \(\omega\) engine, classification, arithmetic ablation, reverse-bridge attempts and audit of inherited assumptions. |
| RH2021 | `task1`–`task60` | `task5` | Reconstruction from zeros, power calibrations, Jacobi/Gram/Weil, TDA and bottleneck log. |
| RH2022 | `task1`–`task68` | `task7`, `task26` | Localized Weil form, zero generation, moments by \(\omega\), H0 persistence and sensitivity tests. |

The intervals in the table are inclusive: they constitute the complete list
of `task` directories of each program, including those without an answer.

## RH2020 — reconstruction

### Goal and actual method

RH2020 attempted to convert peak statistics of Dirichlet polynomials stratified
by \(\omega(n)\) into an analytic chain distinguishing functions with and
without zeros off the line. The design combined:

- an audit of the Davenport–Heilbronn constant and of coefficients;
- the decomposition \(D=\sum_k S_k\), peak matrices
  \(M_{jk}=\mathbb E\,\Re(S_j\overline{S_k})\), amplification ratios and
  spectral entropies;
- classification with controls by family and by time window;
- injection of zeros into a truncated explicit formula; and
- ablations of coefficients at ramified primes.

The important methodological result is negative: \(M_{jk}\) is, above all,
an observable of coefficients, conductor, support and peak conditioning. It
does not behave as an inverse reconstruction of the real part of a zero.

### Claims ledger

| Claim | State | Evidence and scope |
|---|---|---|
| Real DH \(\kappa\), approximately \(0.28408\), and not \((1+i)/2\) | **NUMERICAL** | The vanishing at the four canonical zeros and the consistency with the functional equation resolve the operational inconsistency. The phase derivation must be kept separate from the verification of truncated sums. |
| Kahan/`mpmath` validation and \(\sum_kS_k=D\) | **NUMERICAL** | Agreement of about twelve digits in the completed sample; the audit records that not all planned points were completed. It is an engine certificate, not a property of RH. |
| The bound \(1+r\le K_N\) and \(|D|^2\le K_N^2\max_k|S_k|^2\) | **PROVED** | Cauchy–Schwarz and class counting. It does not depend on peaks or on zeros. |
| \(\max_{t,k}|S_k(t;N)|^2\le N^\varepsilon\Rightarrow\) Lindelöf | **CONDITIONAL** | The implication is sufficient and is stronger than Lindelöf; it is not an equivalence and does not imply RH. |
| Predominance of 67% of negative off-diagonal covariances | **REFUTED** | `task55` and the synthesis: resampling intervals include 50% and exclude the 67% in the largest run; peak conditioning shifts the pattern toward positive couplings. |
| \(\omega=2\) as the sole cause of an approximately 30% change | **REFUTED** | `task47`: \(\omega=1,2,3\) have comparable masses and ablations; the Erdős–Kac maximum explains a large contribution, not a singularity. |
| Dominant positive, low-dimensional mode in peak matrices | **NUMERICAL** | Reappears for \(\zeta\) and DH. It describes conditioned constructive interference; it does not by itself separate RH from non-RH. |
| Spectral entropy of averaged matrices as a separator of the available classes | **NUMERICAL** | Strong separation in the test set and an LOOCV result near 10/11, but Liouville is a counterexample to the "RH" reading; the class size is small and the constructed functions do not form a sample of the Selberg class. |
| Peak classifier as proof of a universal signature | **REFUTED** | Family, temporal and class validations show AUC falling toward chance or F4/F12 asymmetries. The in-sample and stratified bootstrap figures measure family identity. |
| \(M_{kk}\) is scaled by \(C_k=\sum_{\omega(n)=k}|a_n|^2/n\) | **NUMERICAL** | Strong log-log relation and moderate linear relation; peak conditioning adds class- and stratum-dependent amplification. |
| Unconditioned cross moments predict \(M_{jk}\) | **REFUTED** | The global fit is weak; the within-class fit does not authorize a cross-sectional law. |
| Injecting one or four DH zeros reproduces \(M_{jk}(DH)-M_{jk}(\zeta)\) | **REFUTED** | `task25`; sign and norm mismatch. The F12 vs. \(\zeta\) analogue also fails in `task26`. |
| Ablating multiples of conductor primes reproduces DH/F12 differences vs. \(\zeta\) | **NUMERICAL** | High cosine similarities in the tested pairs. It explains a specific arithmetic mechanism, not a law for all \(L\)-functions. |
| The location of an off-line zero can be recovered from norms/spectra of \(\Delta M\) | **REFUTED** | There is no stable correlation with \(\beta\); after removing \(|\kappa|\), the signal disappears. |
| The inherited GEV fit with blocks \(2\pi/\log N\) | **REFUTED** | Switching to \(2\pi/\log T\) shifts the parameter outside the inherited interval. |

### Dependencies, retractions and closed routes

1. The DH, F12 and F14 controls are constructions without an Euler product
   or additive combinations. They are useful for refuting inferences, but a
   binary "GRH true/false" label over that set does not identify a universal
   property of the Selberg class.
2. The `S_0` columns and, for modulus-5 families at this length, `S_7`, are
   structural leaks. They must not enter a classifier as arithmetic evidence.
3. Retracted: inter-class negative signal, exceptionality of \(S_2\),
   prediction by degree/conductor, in-sample/LOOCV SVM as an honest test, and
   inverse reconstruction of zeros from \(M_{jk}\).
4. The valid inheritance is more modest: use the \(\omega\) decomposition as
   energy accounting and as a control bank to distinguish coefficient effects
   from zero effects. Do not again present a peak signature as a bridge to RH
   without a theorem that eliminates those confounders.

## RH2021 — reconstruction

### Goal and actual method

RH2021 shifted the focus to zero lists: reconstruction of Jacobi matrices, Li
coefficients, Mercer matrices, Weil forms and TDA. It introduced a healthy
calibration: deform zeros of \(\zeta\) and measure sensitivity before
interpreting an observable. It also documented failures in generation and
precision of zero lists for DH, \(L(\chi)\) and \(L(\Delta)\).

### Claims ledger

| Claim | State | Evidence and scope |
|---|---|---|
| A Gram matrix built only from on-line zero evaluations can generate negativity | **REFUTED** | It is PSD by construction. The positivity of such a matrix is tautological and does not prove RH. |
| Jacobi reconstructions that use only ordinates detect horizontal shifts | **REFUTED** | The real coordinate was discarded; the power calibration shows structural blindness. |
| Finite positive Li coefficients verify RH | **REFUTED** | Positivity for all indices is Li's criterion; verifying a finite stretch does not transfer to infinity. |
| Li's criterion / universal Weil positivity | **EQUIVALENT-REFORMULATION-TO-RH** | These are classical equivalences, useful for locating the obstacle, not solutions by truncation. |
| TDA H1 and numerical variance separate DH from the available controls | **NUMERICAL** | Finite separation from a counterexample without an Euler product; there is no implication for RH nor invariance across families. |
| Localized Weil form, subtracting the full arithmetic side, detects a DH anomaly near its height | **NUMERICAL** | The local calibration and controls are informative as a detector of a known anomaly. They do not exclude unknown zeros. |
| A finite zero list and a finite prime cutoff allow concluding global positivity/nonexistence | **REFUTED** | The ledger itself acknowledges zero tails, arithmetic cutoff, basis dependence and the absence of a uniform bound. |
| Generation of the target-size catalogs | **REFUTED** | Several tasks end with partial lists, effective precision below what was required, or interrupted processes. Any analysis presupposing the complete catalogs must be flagged as incomplete. |

### Circularity to be corrected

There are two different objects that must be kept separate.

- The Weil form \(B(f,f)\), defined by the explicit formula, has universal
  positivity equivalent to RH.
- The numerical discrepancy "zero side minus truncated arithmetic side" is a
  truncation residue. When both sides are complete, the explicit formula
  equates them; that discrepancy is not by itself a new positive form.

Therefore, a claim that a uniform bound on the residue of finite sections
implies universal positivity must prove a new inequality that does not
presuppose Weil's criterion. If the uniform bound is already equivalent to
Weil positivity, the step is **EQUIVALENT-REFORMULATION-TO-RH**, not an
available technical lemma. This distinction prevents confusing an excellent
detector calibration with a deductive advance toward RH.

### Inheritance and no-go

Keep: calibration via controlled shifts, resolution-vs-\(\delta\)
comparison, and the requirement of convergence curves for deterministic
objects. Do not repeat: Gram PSD as a detector, extrapolating finite Li/Mercer
signs, calling TDA a "proof," or regenerating in every task lists that should
be a single validated artifact.

## RH2022 — reconstruction

### Goal and actual method

RH2022 concentrated effort on a localized Hermite–Gauss basis for the explicit
formula, sensitivity to zero shifts and \(\omega\)-class moments. It is the
program with the best separation between an operational detector and the
proof gap, although its own tasks reveal scale and data inconsistencies that
prevent elevating the result.

### Claims ledger

| Claim | State | Evidence and scope |
|---|---|---|
| A zero-only form is PSD | **PROVED** | Sum of outer products. It explains the failure of `task44` and closes that route. |
| The H0 response to a small horizontal shift is quadratic | **PROVED** | For the vertical-cloud model, \(\sqrt{s^2+\delta^2}-s=O(\delta^2)\); bottleneck and Wasserstein measurements agree. |
| H0 separates DH from controls with comparable heights | **REFUTED** | Permutations are not significant and there is strong confounding by height range. |
| Second-moment fractions by \(\omega\) converge to a signature | **REFUTED** | They migrate with \(N\), as anticipated by Erdős–Kac. |
| Moment-fit exponents distinguish \(\zeta\), \(L(\Delta)\), DH on the available mesh | **NUMERICAL** | Descriptive fits over few values of \(N\); unstable when removing one point and window-dependent. |
| Fourth-moment decomposition offers a finite fingerprint of the Euler product | **NUMERICAL** | Residuals change sign and magnitude with window and length; it is a description of a finite regime. |
| The localized form detects a prescribed deformation of \(\zeta\) and the DH anomaly when centered nearby | **NUMERICAL** | Well-calibrated spatial and basis sensitivity; it depends on knowing height, geometry and the arithmetic side. |
| Quadratic law in \(\delta\) for a shifted symmetric quartet | **NUMERICAL** | `task32` gives an exponent close to two in that setup. |
| Universal linear law in the real shift | **REFUTED** | `task68` reports a linear law in another setup; both cannot be the same universal law. Parity, which zeros are shifted, and the matrix definition must be declared before comparing. |
| Superpolynomial amplification with basis dimension | **NUMERICAL** | Sensitive to truncation, center and incomplete arithmetic; it is not a uniform bound in \(J\). |
| Hermite–Gauss prime tail controlled sufficiently to pass to RH | **CONDITIONAL** | The Gaussian decay of a kernel can bound a tail for fixed parameters, but a joint bound in center, width, dimension, zero tail and normalization is missing. Without it there is no global transfer. |
| Finite localized positivity implies RH | **REFUTED** | Rules R6/R7 and the results acknowledge it: it is a finite section, not the form over all test functions. |
| Weil positivity for every admissible test function is equivalent to RH | **EQUIVALENT-REFORMULATION-TO-RH** | This is the correct framework of the problem; the new part must be an independent inequality that achieves that quantification. |

### Open dependencies and operational errors

- The catalogs required by the caching rule were not all present; repeated
  DH generation tasks ended at partial checkpoints. Lists of different
  completeness must not be mixed as if they were the same experiment.
- The sign and scale consistency of \(Q\) requires a single specification of
  transform, polar/archimedean contributions, quartet symmetrization and the
  error of each truncation. The divergence between the linear and quadratic
  laws is a specification alarm, not a new physical phenomenon.
- The claims about Keating–Snaith and about moment limits need an asymptotic
  regime and error bounds; four or fewer values of \(N\) do not provide that.

### Valid inheritance and routes not to be repeated

Keep the local power test, the basis/cutoff controls, the separation of data
error from formula error, and the H0 no-go. Do not repeat: using DH as the
sole substitute for a general alternative to RH, promoting exponent fits to
asymptotic laws, or treating the cancellation of the explicit-formula residue
as a new positivity.

## Cross-cutting dependencies and decision map

| Component | Heritable result | Non-negotiable limit |
|---|---|---|
| \(\omega\) decomposition | Energy accounting, support controls and arithmetic-confounder testing | It is not an RH criterion nor an inverse predictor of zeros. |
| Classification | Diagnostic for building controls and detecting variable leakage | It does not replace a mathematical quantification; constructed classes are not a distribution of counterexamples. |
| DH and additive combinations | Counterexamples to invalidate inferences that use only the functional equation | They do not represent a family of \(L\)-functions with an Euler product. |
| TDA | Auxiliary geometric measurement and H0 no-go | No finite cloud distance proves a statement about all zeros. |
| Weil form | Exact framework in which RH is positivity | The uniform step from truncations to all test functions is the problem, not a consequence of the simulation. |

## Recommended global restatement

1. Fix a single target object: the classical Weil form, with domain,
   Fourier convention and complete terms written once. Explicitly distinguish
   the form from its truncated numerical residue.
2. Formulate any new lemma as a uniform, verifiable inequality that does not
   assume Weil positivity. It must simultaneously quantify basis dimension,
   center, width, prime cutoff and zero tail. If its conclusion is positivity
   for every test function, classify it from the start as
   **EQUIVALENT-REFORMULATION-TO-RH**.
3. Keep RH2020/RH2022 only as a falsification bank: before attributing an effect
   to zeros, rule out coefficients, conductor, support, window, peak
   selection and normalization. The minimal proof must survive controls with
   an Euler product and synthetic deformations whose arithmetic side is
   coherently defined.
4. Freeze versioned zero catalogs, with a coverage and precision
   certificate. No later result may combine partial checkpoints with
   complete lists without flagging the effective cutoff.
5. Treat the moment, entropy and TDA fingerprints as negative or descriptive
   numerical results, never as proof milestones. The only front that retains
   logical relevance is a new uniform estimate for the Weil form, with prior
   adversarial circularity auditing.

## Critical findings not to lose

- The negative-interference hypothesis that motivated the omega front is
  retracted; the observed peaks are constructive and the \(\omega=2\) mass
  is not singular.
- Peak matrices mainly encode coefficient, conductor and support arithmetic;
  the success of ramified-prime ablations and the failure of zero injections
  close the proposed inverse bridge.
- Any positivity of a zero-only Gram matrix is tautological. The Weil form
  and the truncated discrepancy must stop being interchanged in language and
  in code.
- The localized form is a calibrated numerical detector, not an exclusion of
  all off-line zeros. Its uniform obstacle is the real core of RH under that
  formulation.
- H0, the classifiers and the moment fits remain as no-go results or finite
  phenomenology; they must not receive proof budget.
