# Audit of the RH1–RH9 programs

## Overall balance

The nine programs produce neither a proof of RH nor a reduction of proven lesser strength. Their value lies elsewhere: they build falsifiers, calibrate detectors, identify normalization errors, and close off several tempting but false explanations. The trajectory runs from coefficient statistics to cohomological geometry:

\[
\text{coefficient phases}
\to
\omega\text{ classes}
\to
\text{zero-based reconstruction}
\to
\text{localized Weil form}
\to
\text{finite stability}
\to
\text{Lefschetz geometry}.
\]

At every transition the same cut reappears: the finite objects describe or detect, but do not force global positivity or construct the real divisor.

## Canonical table

| Program | Goal | Durable result | Closed route or pending burden |
|---|---|---|---|
| RH1 | Detect resonance via Dirichlet sums, phases, coherence, and extremes | Numerical instrumentation, precision controls, and Liouville counterexample | Multiplicativity alone does not suppress resonance; the growth signature attributed to an off-line zero was neither derived nor observed operationally. |
| RH2 | Convert decoherence, GEV, and non-growth into a non-vanishing chain | Stricter validation protocol and class-wise perturbations | The GEV correlations and parameters are not universal; the uniform step to non-vanishing is missing and has strength at least comparable to the goal. |
| RH3 | Study the geometry of \(\omega(n)\) classes, moments, and finite causality | Energy identities, reproducibility, and a bank of confounders | The anomalies depend on selection, scale, and implementation; there is no transfer from truncated peaks to zeros of the full function. |
| RH4 | Reconstruct zero information from peak and covariance matrices | Elementary bounds, arithmetic ablation, and leak diagnosis | Negative inter-class covariance and the singularity of \(\omega=2\) were refuted; the matrices encode mostly coefficients, conductor, and support. |
| RH5 | Use Jacobi, Mercer, Li, TDA, and zero lists | Power calibration via synthetic shifts | Zero-only Gram is tautologically PSD; finite positivity of Li or Mercer does not exclude an unknown zero; the full form and the truncated residual are not the same object. |
| RH6 | Localize the Weil form with a Hermite–Gauss basis | Calibrated detector, quartet response, and error separation | A joint uniform bound in dimension, center, width, prime cutoff, zero tail, and normalization is missing. The linear and quadratic laws cannot be mixed. |
| RH7 | Build a local detector with a controlled tail | Finite low-rank expansion and assembly controls | The calibration is numerical; the step to the infinite functional is global Weil positivity in another coordinate. |
| RH8 | Study stability as basis, width, and window grow | Trace gate and division of computational regimes | H1/H2 are mesh evidence; there is no variational monotonicity or uniformity as all parameters grow. |
| RH9 | Build the arithmetic surface, diagonal, Frobenius, and Lefschetz triple | G1–G4 list of conditions and conditional no-gos | The surface, cohomology, spectral reader, and polarization were not built; imposing its positivity from the zeros would be circular. |

## RH1–RH3: why the multiplicativity explanation failed

The programs start from

\[
D_F(t;N)=\sum_{n\le N}a_n n^{-1/2-it},
\qquad
D_F=\sum_k S_k,
\quad
S_k=\sum_{\substack{n\le N\\\omega(n)=k}}a_n n^{-1/2-it}.
\]

The identity

\[
|D_F|^2
=
\sum_k|S_k|^2
+
\sum_{j\ne k}\Re(S_j\overline{S_k})
\]

is proved and useful as bookkeeping. By itself it does not relate the cross terms to the absence of zeros. Liouville's function offers the decisive conceptual falsifier: it is completely multiplicative and its series is \(\zeta(2s)/\zeta(s)\), so "multiplicative" does not imply the intended zero geometry. Random multiplicative functions also break the identification between an Euler product, small coherence, and benign tails.

The assumed bridge

\[
\rho=\beta+i\gamma,\ \beta>\tfrac12
\quad\Longrightarrow\quad
|D_F(\gamma;N)|\asymp N^{\beta-1/2}
\]

was not proved for the truncated observable. In the Davenport–Heilbronn control the predicted slope did not appear. This refutes the proposed detector, not the classical fact that that function has zeros off the line.

The SVM/LDA, CAS, entropy, ACF, moment, and GEV classifiers separate specific generators but do not characterize an analytic property. Their results change with the observable, the window, the block, the peak selection, and the sign convention. RH2 explicitly breaks the arrows

\[
R_{\rm comp}\text{ small}
\not\Rightarrow
\xi_{\rm GEV}<0
\not\Rightarrow
\text{no growth}
\not\Rightarrow
\text{no off-line zeros}.
\]

The valid legacy of RH1–RH3 is instrumental: compensated summation, high precision, seeds and hashes, an identical selection criterion, class-wise perturbations, and Liouville/random controls. The causal hypothesis by \(\omega\) classes is withdrawn.

## RH4–RH6: from the peak observable to the Weil detector

RH4 checks that the matrices

\[
M_{jk}=\mathbb E\,\Re(S_j\overline{S_k})
\]

respond strongly to coefficient mass, conductor, support, and peak conditioning. Injecting zeros does not reproduce the differences between families, whereas certain ablations by ramified primes do. For that reason the proposed inverse bridge from \(M_{jk}\) to the real part of a zero is closed off. The inherited claim of negative covariance and the causal exceptionality of \(\omega=2\) are also refuted.

RH5 uncovers an essential no-go: if

\[
G_{ij}=\sum_{\rho}v_i(\rho)\overline{v_j(\rho)},
\]

then \(G\succeq0\) by construction, even when the design has discarded the horizontal coordinate it was meant to detect. That PSD property says nothing about RH. Likewise, checking \(\lambda_n>0\) for a finite set of indices or a finite list of zeros does not control the remaining indices.

A distinction must always be kept between:

\[
\text{the full Weil form}
\qquad\text{versus}\qquad
\text{the difference between two truncations of the explicit formula}.
\]

The first has universal positivity equivalent to RH. The second measures cutoff, data, and normalization; it does not inherit a sign.

RH6 improves the localized detector but keeps an inconsistency that serves as an alarm: one setup produces a quadratic response in the shift and another reports a linear response. Before comparing, parity, the shifted quartet, the transform, the polar/archimedean terms, and the exact definition of the matrix must be fixed. The Gaussian decay of Hermite–Gauss controls tails for fixed parameters; by itself it does not provide the uniform inequality needed for a full proof.

## RH7–RH8: valid detector, invalid global inference

The finite expansion of a perturbed quartet produces a low-rank symmetric operator with quadratic dependence on \(\delta\) for the specified setup. The trace controls, verified lists, and Hermite–Gauss tails are real assets. Their status splits as follows:

- algebraic identity of the expansion: **PROVED** for the fixed section;
- agreement with meshes, traces, and thresholds: **NUMERICAL**;
- uniform step to the full functional: **RH-STRENGTH**.

RH8 adds a strong methodological rule: do not interpret \(\lambda_{\min}\) if the trace residual does not close. With a narrow width or an insufficient prime cutoff, the truncation dominates and the apparent instability is not spectral information. The observed H1/H2 curves do not prove

\[
Q_{J,\sigma,X,H}\longrightarrow Q_\infty
\]

uniformly in center, dimension, width, and windows. Precisely that convergence, combined with detection of a perturbation, would exclude off-line zeros and cannot be treated as a numerical detail.

## RH9: the geometry does not yet exist

The program requires a construction that simultaneously delivers:

1. a global object \(S\) and a diagonal \([\Delta]\);
2. a cohomology whose degree one carries the relevant spectrum;
3. a Lefschetz triple \((L,\Lambda,H)\) with well-defined domains;
4. a positive polarization identified with the Weil form without having used the zeros.

Arakelov theory, \(\lambda\)-rings, TC/prismatic cohomology, scaling dynamics, prolate/Sonin theory, and noncommutative geometry contribute pieces or analogies, but not that joint construction. Local Frobenii are not automatically a global Frobenius with the zero spectrum; Adams weights are not the required Cartan operator; a metric manufactured from the roots interpolates the divisor instead of explaining it.

The \(\Delta_3\) statistic and the GUE comparisons are numerical. A proposed prime formula for the plateau includes a divergent series and is withdrawn in its literal form. RH9 survives as the G1–G4 filter, not as an already-built active route.

## Incompatibilities blocking automatic reuse

1. **Davenport–Heilbronn.** Periodic combination, restriction to squarefree numbers, constants, coordinates, and different catalogs were mixed together. No number carries over from one variant to another without reconstructing the definition.
2. **Perturbation law.** "Linear" and "quadratic" correspond to different setups or to an inconsistency; there is no audited universal law.
3. **Form and residual.** The equality of the full explicit formula does not turn the truncated error into a positive form.
4. **Zeros and arithmetic.** A Gram matrix built only from zeros is not an independent control on the prime side.
5. **Averaging and universality.** A statistical separation of constructed families does not quantify over the class of all alternatives to RH.
6. **Partial catalogs.** Incomplete lists, or ones with different precision, do not combine into a single sample.

## Outcome of the review

The programs fall into three bins:

- **instrument bin:** precision, tails, traces, falsifiers, perturbations, and data control;
- **no-go bin:** multiplicativity, \(\omega\) classes, zero-only Gram matrices, classification, TDA, finite extrapolation, and merely postulated geometry;
- **RH-strength objective bin:** full Weil positivity, uniform convergence of the detector, the real divisor, and the identified polarization.

The continuation must not open a tenth exploratory program of the same kind. It must start from a signed arithmetic statement that fails against a planted quartet and whose proof does not depend on the position of the zeros.

The task audits supporting this balance are at:

- [`fragments/RH1_RH3_AUDIT.md`](fragments/RH1_RH3_AUDIT.md)
- [`fragments/RH4_RH6_AUDIT.md`](fragments/RH4_RH6_AUDIT.md)
- [`fragments/RH7_RH9_AUDIT.md`](fragments/RH7_RH9_AUDIT.md)
