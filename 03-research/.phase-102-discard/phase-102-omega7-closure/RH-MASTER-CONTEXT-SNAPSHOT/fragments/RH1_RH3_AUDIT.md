# Audit of RH2017–RH2019: usefulness, limits, and restart

## Executive verdict

The three programs contain neither a proof of RH nor a new reduction that demonstrably brings it closer.
Their useful output is diagnostic: they fix several numerical controls, show that multiplicativity alone
does not classify the finite geometry of Dirichlet polynomials, and locate failures that a reformulation
must block from the start. RH2017's governing thesis — "the Euler product/multiplicativity suppresses the
resonance that would allow off-line zeros" — is **REFUTED** as a general explanation by random
multiplicative families and, decisively, by Liouville. RH2018 further eliminates the empirical arrows that
tried to turn those observables into a proof. RH2019 keeps a phenomenology of \(\omega(n)\) classes, but
only at finite scale and with marked sensitivity to the definition, peak selection, and implementation.

**Reading rule.** PROVED means a mathematical identity or correctly invoked external theorem, not a
chart. CONDITIONAL means an implication that would require a new bound. NUMERICAL means a reproducible
finite computation within an identified implementation. CONJECTURAL means interpretation or
extrapolation. REFUTED means the program itself supplied a counterexample, a negative trial, or a
methodological impossibility. EQUIVALENT-REFORMULATION-OF-RH flags a phrase that, if true over the whole
relevant domain, would already be RH and not an independent route.

## Documentary coverage

The three READMEs, the 266 `OVERVIEW.md` files, and the mathematical or validation documents needed to
resolve conflicts were read: in particular the Davenport–Heilbronn validation reports, the moment
decompositions, the canonical \(r\) reports, the code or report for the canonical random function, and
the sweep-network manuscript. Coverage is exhaustive over contiguous intervals; no task directory is left
outside the table.

| Program | Directories reviewed | Coverage | Dominant focus |
|---|---|---:|---|
| RH2017 | `task1`–`task89` | 89/89 | resonance detector, phases, GEV, classification, and DH crisis |
| RH2018 | `task1`–`task94` | 94/94 | proof–diagnosis chain attempt, perturbations, and controls |
| RH2019 | `task1`–`task83` | 83/83 | \(\omega\)-class geometry, moments, finite causality, and infrastructure |
| **Total** | `RH2017/task1`–`task89`; `RH2018/task1`–`task94`; `RH2019/task1`–`task83` | **266/266** | — |

## Mathematical status inventory

| Claim | Status | Correct scope |
|---|---|---|
| The classical Davenport–Heilbronn function has no Euler product and has zeros off the critical line. | **PROVED** | External calibration fact; useful for ruling out detectors, not for inferring RH. |
| \(\lambda\) is completely multiplicative and its series is \(\zeta(2s)/\zeta(s)\). | **PROVED** | Conceptual counterexample to "multiplicative implies suppression". |
| \(\mu(n)^2(-1)^{\omega(n)}=\mu(n)\), so the corresponding series is \(1/\zeta(s)\). | **PROVED** | Corrects the false presentation of that object as a new independent function. |
| \(|D|^2=\sum_k|S_k|^2+\sum_{j\ne k}\Re(S_j\overline{S_k})\). | **PROVED** | Algebraic identity. The ratio \(r\) is a parametrization of those cross terms, not a bound on zeros. |
| Mean orthogonality of Dirichlet polynomials and the Montgomery–Vaughan paradigm for second moments. | **PROVED** | Does not turn the \(\omega\)-decomposition into information about \(\zeta(\rho)=0\). The finite trials are only consistent with the theorem. |
| Vinogradov–Korobov and the Selberg CLT. | **PROVED** as external theorems; **NUMERICAL** as finite-scale checks in RH2018. | Equidistribution or Gaussianity of averages does not give a uniform exclusion of off-line zeros. |
| Deforming \(S_k\mapsto -S_k\) reduces peaks of a selected Dirichlet polynomial. | **NUMERICAL** | Causal only for that finite variable, that mesh, those peaks, and that partition; not causality on the zeros of an \(L\)-function. |
| SVM/LDA separation by CAS, \(M_{\rm coh}\), \(R_{\rm comp}\), entropy, or ACF. | **NUMERICAL** | Classifies the samples and generators used. Even a perfect separation is not an analytic characterization nor an RH criterion. |
| \(M_4\) anomaly near \(N\approx10^5\). | **NUMERICAL**, partially **REFUTED** as universal. | Appears in several real and arithmetic families, is absent in the i.i.d. null and in the complex random multiplicative function; also depends on the decomposition. |
| "The phase or \(\omega\)-class architecture is the deep cause of RH." | **CONJECTURAL** | The data only describes truncated polynomials and admits counterexamples among the compared families. |
| "A root \(\beta+i\gamma\), \(\beta>1/2\), forces \(|D(\gamma;N)|\asymp N^{\beta-1/2}\)." | **CONDITIONAL** with no proof presented; **REFUTED** as an operational DH signature. | No theorem was derived for that truncated observable. In DH the observed slope was consistent with zero up to large scales. |
| \(R_{\rm comp}\) small \(\Rightarrow\xi<0\Rightarrow\) absence of growth \(\Rightarrow\) no off-line zero. | **REFUTED** | RH2018 finds the \(R_{\rm comp}\)-\(\xi\) relation is not universal and that GEV fits change with observable, blocks, and selection. |
| Uniform decoherence bound for \(D_\zeta\), deduced from prime exponential sums. | **CONDITIONAL** | It is the only recognizable bridge toward RH, but precisely the uniform bound for composite classes and the step from finite extremes to non-vanishing are missing. |
| "The sweep regions cover the critical half-plane and there \(\zeta\ne0\)." | **EQUIVALENT-REFORMULATION-OF-RH** and **REFUTED as proof** | Covering the whole strip and excluding zeros is already equivalent to RH. The manuscript uses that \(\zeta\) stays away from zero and controls \(\zeta'/\zeta\) across possible poles: these are the sought conclusions. |

## RH2017 — resonance detector and actual result

**Goal and method.** RH2017 compares \(\zeta\), Dirichlet characters, a random multiplicative function, DH,
and DH perturbations via truncated sums
\[
D_F(t;N)=\sum_{n\le N}a_n n^{-1/2-it}.
\]
It measures extremes, tails, cross-scale coherence, prime and composite phases, \(M_{\rm coh}\),
\(R_{\rm comp}\), CAS, and GEV. It uses Kahan compensation and pointwise high-precision contrasts. The
design was correctly falsifiable: a serious detector had to distinguish a validated DH from families
with an Euler product.

**Closed results.**

- **NUMERICAL / REFUTED:** the killer signature did not appear. At DH's supposed first zero, the fitted
  slope up to \(N=10^9\) was about \(0.00044\pm0.00045\), not \(0.3085\); following the shifted maximum
  did not recover it either. This is a negative detector result, not evidence that the classical fact
  about DH is false.
- **NUMERICAL / REFUTED:** tails, the resonance score, and coherence do not order the classes as
  "multiplicative versus non-multiplicative". The random multiplicative function and Liouville can be
  more extreme or more coherent than DH.
- **NUMERICAL:** in concrete versions, \(\zeta\)'s peaks show prime-phase bias and DH can show structure
  in composites; dephasing by class changes the peaks. It is a description of the computed polynomials,
  not of their zeros.
- **NUMERICAL:** CAS, periodicity, and entropy separate the generated sets very well. The useful finding
  is the inverse of the original program: the metrics capture coefficient organization, not
  multiplicativity nor RH validity.

**Dependencies and valid inheritance.** Compensated evaluation, comparison against high precision,
reproducible random controls, the peak-selection log, and the class energy identity are inherited. The
Liouville counterexample also remains as a mandatory stress test.

**Retraction, no-go, and circularity.**

- Growth \(N^{\beta-1/2}\) was treated as an automatic consequence of an off-line root without a
  derivation connecting the truncated series on \(\Re s=1/2\) to that root. It must not be used again as
  a lemma.
- The success of a classifier trained and evaluated on coefficients or sibling variants cannot certify a
  zero property. It is overfitting the analytic question even if internal cross-validation is flawless.
- DH was implemented in incompatible ways: periodic character combination, artificial restriction to
  squarefree numbers, and reference data of different provenance. The "zero" and \(\kappa\) coordinates
  also vary. Any comparative conclusion mixing those variants is **REFUTED for lack of object identity**.
- The periodic variant without the squarefree restriction is the only candidate that passed the internal
  numerical gate at the four refined points; even so, a small truncated sum is only **NUMERICAL**, not
  certification of the full function's zeros. A definition, normalization, coordinates, and a convergence
  proof must be fixed before reuse.

## RH2018 — from intuition to a proof chain that did not close

**Goal and method.** RH2018 tries to standardize a single engine, validate DH before analyzing, and turn
three empirical targets into a chain: composite decoherence \(\to\) GEV shape \(\to\) no growth \(\to\)
absence of zeros. It adds \(\omega\)-class perturbations, pretentious distance, \(\xi\) fits,
regressions, and numerical checks of known theorems.

**Closed results.**

- **NUMERICAL / REFUTED:** low \(R_{\rm comp}\) does not universally predict \(\xi<0\); the correlation
  changes sign, family, and protocol. The chain's second link therefore breaks.
- **NUMERICAL / REFUTED:** GEV fits offer no robust classifier nor reliable asymptotic trend. There are
  reports with opposite sign of \(\xi\), and SciPy's convention \(c=-\xi\), the use of \(|D|\) versus
  \(\log|D|\), the window, and the block size alter the reading.
- **NUMERICAL:** inverting \(S_2\) or composite classes alters covariances and \(\zeta\)'s peaks in the
  samples; it is an interesting finite sensitivity, not a uniform inequality.
- **NUMERICAL / REFUTED:** pretentious distance, global moments, and regression models do not sustain a
  generalizable tail or coherence predictor. Good internal \(R^2\) values fail under cross-validation.
- **PROVED / NUMERICAL:** the engine and precision controls are an operational improvement, and the
  checks of classical results are sanity controls, not new proofs.

**Dependencies.** RH2018 depends on a single validated DH, a fixed definition of \(S_k\), the same peak
criterion, and a frozen GEV protocol. These conditions were not kept globally: the repository itself
retains failed validations, different coordinates, and tasks stopped by the precondition.

**Do not repeat.** Do not chain finite-scale correlations as logical implications; do not interpret
penultimate \(\xi\) as an asymptotic tail type; do not use Vinogradov–Korobov or Selberg evidence to
substitute for the missing uniform bound; do not accept DH results if the validation gate is not
documented for exactly the same function.

## RH2019 — \(\omega\) geometry, moments, and computational limits

**Goal and method.** RH2019 studies \(S_k=\sum_{\omega(n)=k}a_n n^{-1/2-it}\), the canonical ratio \(r\),
phase inversion of a class, second and fourth moments, and their evolution with \(N\). It compares
\(\zeta\), Liouville, Möbius, characters, random functions, and DH; it adds a fixed-seed canonical random
multiplicative function and compiled acceleration.

**Closed results.**

- **PROVED:** the energy identity defining \(r\) and the reproducibility of the fixed-seed canonical
  random function. These are infrastructure, not RH content.
- **NUMERICAL:** at selected peaks \(r\) is usually positive and at valleys it can be negative; inverting
  \(S_2\) or \(S_3\) reduces peaks. The correct interpretation is vector interference conditioned by
  selection.
- **NUMERICAL:** transversal second moments decrease in the trials and are compatible with mean
  orthogonality; the fourth moment and its categories show non-monotone finite changes across several
  families.
- **NUMERICAL / REFUTED:** the \(M_4\) anomaly is not universal to multiplicativity: it fails in the
  complex null and appears in non-multiplicative families. It is also not established as a "real
  coefficients" property: some tasks fix parts of the decomposition by pre-assigned proportions.
- **REFUTED:** narratives of monotone evolution of \(r\), of adjacent-pair dominance, or of a fine
  resonance in \(\kappa\) collapse once the peak-selection criterion is equalized or the sweep is widened.

**Decisive errors and limits.**

- Comparing peaks chosen by \(r\) at one scale with peaks chosen by magnitude at another introduced bias;
  homogeneous reanalysis undoes it.
- Several tasks do not reach \(N=10^7\); hence there is no evidence of a limit nor of monotonicity. "Not
  computable within budget" is not a negative result about the mathematical hypothesis.
- In one \(M_4\) decomposition only initial terms were computed and fixed proportions were imposed for
  the rest. Its percentages are not evidence and must be marked **REFUTED as a decomposition**.
- A sweep-network manuscript claims absence of zeros via bounds and convergences that presuppose
  avoiding the poles of \(\zeta'/\zeta\). It is circular and must not be inherited as a proof.
- The DH validation that tests points \(1/2+it\) using only heights of alleged off-line zeros is a
  poorly posed control: the real parts are missing. Its failure neither validates nor invalidates DH; it
  only invalidates that protocol.

## What the global reformulation must inherit

1. **PROVED / reusable:** explicit algebraic identities, external theorems with written hypotheses,
   coefficient arithmetic, numerical compensation, high precision, and hashes or seeds for nulls.
2. **NUMERICAL / reusable as exploration:** \(S_k\) perturbations, phase maps, \(r\), CAS, and moments,
   always with a single definition, versioned data, identical selection, and uncertainty bars.
3. **CONDITIONAL / genuine frontier:** a uniform, explicit, proved bound connecting the arithmetic
   structure of coefficients to non-vanishing of \(\zeta\) off the line. It must be independent of RH and
   stable when passing from truncated polynomials to the analytic continuation.
4. **REFUTED / forbidden:** multiplicativity as a sufficient criterion; statistical classification as a
   certificate; GEV or correlations as proof links; the DH growth signature without a theorem; combining
   DH implementations; extrapolating from \(N\le10^7\); and arguing from differently defined peaks.
5. **EQUIVALENT-REFORMULATION-OF-RH / forbidden as progress:** directly asserting non-vanishing in a
   family of regions covering the critical strip, or introducing a bound on \(\zeta'/\zeta\) valid only
   if there are no zeros. Such statements must be labeled as the goal, not as available lemmas.

## Minimal gate before any new program

Fix a single definition for each function, especially DH; accompany it with a proof of coefficient
identity, high-precision reference values, and complete calibration coordinates. Separate in the
repository theorems, conditional lemmas, numerical observations, and conjectures. For every
\(N\to\infty\) transfer claim, require an explicit inequality with constants and an analytic step toward
the full function. If that step does not exist, the result must remain NUMERICAL even if all software
tests pass.
