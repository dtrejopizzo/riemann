# Master context of the program toward RH

## Executive verdict

The full review finds neither a proof of RH nor an unconditional chain that closes \(\Omega_7\). It does find a solid mathematical column, an important bank of finite identities and specific no-go results, and a much narrower frontier than at the start of the program.

The defensible column is

\[
\mathrm{RH}
\Longleftrightarrow
\{\text{all zeros of }\Xi\text{ are real}\}
\Longleftrightarrow
\mathrm{ARP\!\!-P}
\Longleftrightarrow
\{J_N(z_0)\succeq0\text{ for all }N\}
\Longleftrightarrow
\{\lambda_n\ge0\text{ for all }n\}.
\]

This chain localizes the difficulty; it does not diminish it. Several arrows are equivalences of complete families obtained by passing through RH, not level-by-level positive transformations. That is why a certificate for a finite cutoff, a mesh, or an interval does not automatically propagate to every index.

The claim that \(\Omega_1\)–\(\Omega_6\) are closed requires a decisive qualification. \(\Omega_1\), \(\Omega_2\), \(\Omega_3\), and \(\Omega_6\) survive as global equivalences in the audited terms. \(\Omega_4\) mixes two whitenings with different domains. \(\Omega_5\) proves boundary continuity for each fixed \(N\), but does not produce the required uniform interior positivity. The only terminal objective remains \(\Omega_7\), although not every auxiliary piece of the constructive path is proved.

The most useful correction for the restart is

\[
\lambda_n
=
\lambda_n^{\rm arch}+\lambda_n^{\rm prime}
\ge0
\quad\Longleftrightarrow\quad
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}.
\]

Paper 36 presents, in different places, the domination

\[
|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}
\]

as if it were the exact inequality of \(\Omega_7\). It is not. It is a stronger sufficient condition when the archimedean part is positive, and it already fails as a supposed equivalence at \(n=1\):

\[
\lambda_1^{\rm arch}
=1-\frac\gamma2-\log2-\frac12\log\pi
\approx-0.55412,
\qquad
\lambda_1^{\rm prime}=\gamma\approx0.57722,
\]

while \(\lambda_1\approx0.02310>0\). This does not make \(\Omega_7\) easy: by H0, proving the one-sided bound for every index still has RH-strength. It does show that the no-go results obtained via absolute values do not close off every arithmetic route. For the indices where \(\lambda_n^{\rm arch}\ge0\), the target reduces to controlling the negative excursion of the prime part; for the indices where \(\lambda_n^{\rm arch}<0\), the full lower bound must be kept, which requires a sufficient positive prime contribution.

The audit finds a second correction along the same route. For

\[
f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\]

the correct integration by parts is

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
=
\lim_{\varepsilon\downarrow0}
\left[-n+
\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right].
\]

Paper 36 prints the negative of the integral with \(\psi-y\) and omits \(-n\). The earlier regularized pole–prime representation is still usable; the integration-by-parts formula and every signed conclusion derived from it must be corrected.

## What paper 36 actually represents

The main structural contribution is the equivalence

\[
\mathrm{ARP\!\!-P}\Longleftrightarrow\mathrm{RH}.
\]

The direction ARP-P \(\Rightarrow\) RH uses Pick–Nevanlinna interpolation, normality, analytic continuation, and detection of non-real residues. The direction RH \(\Rightarrow\) ARP-P turns each channel into a Cauchy transform of a positive measure. The architecture is mathematically significant because it serializes the problem into positivity of finite matrices, but Step 5 requires that positivity for every source and every set of nodes; that is the open input.

The audit of the H0–H8 hierarchy leaves:

| Level | Binding status | Exact burden |
|---|---|---|
| H0 | **PROVED** | Logical conservation of difficulty; does not by itself identify where all the strength lies. |
| H1 | **PROVED in the stated scalar case** | Does not automatically cover complex matrix channels. |
| H2 | **PARTIAL** | Gershgorin closes high, separated nodes; compactness plus a positive diagonal does not imply PSD at bounded height. |
| H3 | **PARTIAL** | A logarithmic region and an almost-everywhere result; not the global two-node inequality. |
| H4 | **PROVED as serialization** | The sequence of determinants characterizes RH; its sign is not proved. |
| H5 | **PROVED as equivalence** | Positive windows and ARP-P are coordinates of the same condition. |
| H6 | **QUALITATIVE; quantitative open** | Contraposition gives some finite witness. The explicit construction does not dominate the tail and loses a factor \(|\kappa|\). |
| H7 | **PARTIAL** | SOS under RH and closures on fixed boxes or bands; no global arithmetic SOS. |
| H8 | **PARTIAL** | Positivity at fixed \(N\) and high translation; uniformity in \(N\) at fixed height is missing. |

Four pieces must also be withdrawn or downgraded:

1. The isolated sum \(\sum_\rho(1-1/\rho)^n\) does not converge, even under RH; only the symmetric combination defining \(\lambda_n\) is legitimate.
2. Sampling, factorial saturation, and the de Bruijn–Newman cascade depend on uniform estimates that are still open.
3. The operator realization requires self-adjointness, uniform control of sources, and resolvent identification not constructed within the manuscript.
4. The integration by parts of the Laguerre kernel has an incorrect sign and boundary term.
5. The envelope asymptotics omits the linear term \(\frac{\gamma-1}{2}n\), and the bound \(c\sqrt n\log n\) cannot include \(n=1\).
6. The Castelnuovo/Minkowski closure applies a hypothesis stated for positive norm to a class obtained with negative norm.

These corrections do not destroy the ARP-P–RH equivalence. They prevent using auxiliary results as if they were stronger than what is actually proved.

## Compressed tour of the nine programs

### RH2017–RH2019: coefficients, \(\omega\) classes, and statistics

Dirichlet sums, decompositions by number of prime factors, coherences, extremes, classifiers, and precision protocols were built. The energy identity

\[
\left|\sum_kS_k\right|^2
=
\sum_k|S_k|^2+
\sum_{j\ne k}\Re(S_j\overline{S_k}),
\]

survives, but not its reading as a zero criterion. Liouville's function and random multiplicative controls show that multiplicativity, small decoherence, or an extremes law do not determine the geometry of the divisor. The bridge from an off-line zero to a concrete slope of the truncated observable was likewise not proved and did not appear in the operational control.

### RH2020–RH2022: peak matrices and localized Weil theory

Class covariances respond mainly to coefficient mass, conductor, support, and peak selection. The predominance of negative covariance and the causal exceptionality of \(\omega=2\) were withdrawn. A Gram matrix built only from zeros is PSD by construction and may have eliminated the horizontal coordinate it was meant to detect.

The Hermite–Gauss Weil detector does leave behind finite algebra and useful calibrations. A joint uniform bound in dimension, center, width, prime cutoff, zero tail, and normalization is missing. The observed linear and quadratic responses belong to different setups or expose an inconsistent specification; they do not constitute a universal law.

### RH2023–RH2024: calibrated detector, missing transfer

The expansion of a perturbed quartet and several trace controls are correct for fixed sections. The H1/H2 meshes and minimal eigenvalues are numerical evidence. The step

\[
Q_{J,\sigma,X,H}\longrightarrow Q_\infty
\]

with simultaneous uniformity is precisely the step capable of excluding every off-line zero. It cannot be treated as a routine extrapolation.

### RH2025: postulated geometry, not built

The program specifies what a useful geometry should deliver: a global object, a diagonal, cohomology, a spectral reader, a Lefschetz triple, and an independent polarization. Arakelov theory, scaling dynamics, noncommutative geometry, prolate/Sonin theory, and cohomological theories contribute analogies or pieces. The corpus does not build the joint object nor identify its intersection form with Weil without first inserting the divisor.

## Compressed tour of the phases

The phases are not more than a hundred cumulative closures. They are a genealogy with branches, corrections, and reparametrizations. The useful arc is

\[
\begin{aligned}
&\text{localized Weil theory and detector}
\to\text{sign walls}
\to\text{Hodge and index}\\
&\to\text{Connes/CCM}
\to\text{Feshbach--Cauchy--adjugate}
\to\text{LP+IDENT}\\
&\to\text{RDI-ANCHOR}
\to\text{current and divisor}
\to\boxed{\text{signed arithmetic identification still open}}.
\end{aligned}
\]

### Phases 0–25

The full Weil form is fixed, several sign walls are proved, and Kreĭn, heat, Carleson, de Branges, and Hodge realizations are tried. The durable results are detectors, identities, and bounded no-go results. The global geometry and its polarization are not built. The arguments with a finite number of defects depend on a finiteness hypothesis that the complement of RH need not satisfy.

### Phases 26–50

CCM, moments, de Bruijn–Newman, Selberg, Pontryagin, and Hodge turn averages and defects into partial conditions. The common lesson is

\[
\text{small average or convergent subsequence}
\not\Rightarrow
\text{absence of an atom or alignment of every zero}.
\]

The phase→inertia attempts prove no-go results for local or Tauberian classes. They do not prove that every non-local Diophantine input is impossible.

### Phases 51–75

Homotopy, Stone duality, metrics, GLT, and formal indices do not produce the arithmetic arrow. Phases 64–71 recognize that approximants with real zeros converging to \(\Xi\) would solve RH by Hurwitz; that convergence has RH-strength. Phase 65's QED label is superseded by later corrections.

Phases 72–75 deliver valuable algebraic infrastructure:

\[
\text{Feshbach}
\to\text{current}
\to\text{Cauchy}
\to\text{divisibility}
\to\text{adjugate}.
\]

The terminal names `PW-Cauchy`, `HPR-DIV`, `EG_LOCK`, and `ADJ-ARITH-LOCK` are representations of the same signed cancellation, not four distinct closures.

### Phases 76–79

Here `SAFE-LIMIT-POINT = LP + IDENT` is separated out, the LP problem is corrected to `BTG-DIV` at the true \(\mu_L\), and `GAP-Z` is decomposed exactly as

\[
g_{N+2}-g_N=\mathrm{ZERO}+\mathrm{MESH}+\mathrm{BND}.
\]

The MESH and BND bounds are proved; ZERO remains open and cannot be bounded by summing shell magnitudes. Outcome A uses finite sections and \(\mu_{\rm ref}\), not the limiting object at \(\mu_L\), so LP's neutrality is not certified.

E79.6 and the cloud discriminants are numerical or conjectural. Several signatures were retracted due to precision controls, a change of definition, or loss of discriminating power. It is not proved that `DISCRIMINANT` is necessary, sufficient, or the sole carrier of RH-strength.

### Phases 80–101

Secular identities, Euler–Möbius, Abel, shell Feshbach, bordered determinants, cofactors, Jacobians, commutators, and currents are proved. All are useful exact coordinates. The routes return to

\[
\mathrm{RDI\!-\!ANCHOR}
\sim
\mathrm{DIRECT\!-\!BORDERED\!-\!ANCHOR}
\sim
\mathrm{LOCAL\!-\!COVARIANT\!-\!IDENT}
\sim
\mathrm{STIELTJES\!-\!IDENT}.
\]

Identifying `C_core` on a safe interval already forces RH by Pick–Nevanlinna propagation. `TRUE-DIVISOR-IDENT` is even stronger because it preserves support and multiplicity. Phases 94–100 change the representation of the burden; they do not prove it.

## Bank of results that can be reused

1. The ARP-P–RH equivalence and the scalar serialization by jets at a regular point.
2. The Cayley dictionary \(w=1-1/\rho\) and the full criterion of Li.
3. Finite identities of localized Weil theory, Cauchy, Pick, Feshbach, shorting, adjugates, cofactors, Jacobians, commutators, and Abel, keeping their domains.
4. The exact decomposition of GAP-Z with controlled MESH and BND.
5. For \(\Re s>1\), the Euler–Gamma product, its logarithmic derivative, and the Laguerre identities where absolute convergence is justified.
6. Numerical detectors and falsifiers with fixed precision, normalization, catalogs, traces, and seeds.
7. Specific no-go results: zero-only Gram matrices, multiplicativity as a criterion, finite extrapolation, pseudoinverse on a singular curve, cell matching, one level of moments, products of traces, and merely postulated geometry.
8. The indispensable distinction between convergence, identification, and positivity.

## Minimal record of routes not to be repeated

| Route | Reason for closure or quarantine |
|---|---|
| Multiplicativity, \(\omega\), GEV, classifiers | Multiplicative controls and window dependence break the inference to zeros. |
| Gram or Mercer matrix built from zeros | Tautologically PSD; does not detect horizontality. |
| Li or Weil on finite cutoffs | Does not quantify over future indices or tests. |
| Positive prime truncation | The sign arises from global cancellation; finite sections can be negative. |
| Pointwise bound with absolute values | Loses the Laguerre phase; does not rule out the new one-sided target. |
| Zero-free region or zero density | Admits at least one off-line zero, enough to destroy Li's criterion at large indices. |
| Fejér–Riesz | The required nonnegativity of the symbol is the conclusion. |
| Abstract Kreĭn theory | The existence of some positive extension does not identify the required arithmetic kernel. |
| Recurrence over all phases | The Kronecker cost of the tested formulation outweighs the geometric gain. |
| Heat, de Branges, Herglotz, LP | In the useful versions real-rootedness, or an equivalent condition, reappears. |
| Hodge/Lefschetz without an external object | Postulates the polarization that must be proved. |
| Prolate theory or a single gap | Does not identify the ground state nor exclude a negative index without a Weil-equivalent bound. |
| Averaging, smoothing, moments of one level | Loses transverse support or an individual zero. |
| New RDI coordinate | Does not count as closure without a new identity or inequality. |

## Actual mathematical frontier

There is one terminal objective and several internal obligations of a specific route. These must not be confused.

| Obligation | Status | Role |
|---|---|---|
| \(\lambda_n\ge0\) for all \(n\) | **OPEN / RH-STRENGTH** | The exact terminal objective. |
| \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\) | **OPEN / RH-STRENGTH** | Minimal one-sided arithmetic form of the same objective. |
| `BTG-DIV` at the true \(\mu_L\) | **OPEN** | LP obligation; neutrality with respect to the off-line control is not proved. |
| LP interface free of a fixed \(\mu_L\) | **OPEN** | Repair needed for the build-neutral formulation. |
| `GAP-Z`, the ZERO term | **OPEN** | Signed convergence; MESH and BND do not resolve it. |
| `RDI-ANCHOR` or `C_core` identified | **OPEN / RH-STRENGTH** | Euler–Gamma identification from the recent route. |
| `RDP-SHELL`, PROLATE, and WEIL-TAIL | **OPEN** | Downstream bridges; should not be attacked before the core. |
| External geometry with polarization | **NOT BUILT** | Conceptual alternative, not available infrastructure. |

H0 allows concluding that every sufficient chain contains at least one false or RH-strength step. It does not allow concluding that it contains exactly one while the other obligations remain open. That is why the hypothesis "DISCRIMINANT is the sole milestone and GAP-Z is neutral" is not proved. `RDI-ANCHOR` is clearly of RH-strength; LP and GAP-Z have not yet been classified at the correct limiting object.

## Recommended restart

### First track: one-sided Li criterion and signed cancellation

First fix, without internal abbreviations, the regularized definition via the paired limit

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[
\sum_{k=1}^n
\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
-
\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
L_{n-1}^{(1)}(\log m)
\right]
\]

and all the pole, Gamma, and boundary terms. At the boundary the bare series is not absolutely convergent; no manipulation can separate the terms that produce the finite continuation.

The mechanism being sought must preserve the sign before any estimate is made. Writing \(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), the corrected starting identity is

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
\]

followed by the exact lower bound

\[
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
\ge-\lambda_n^{\rm arch}.
\]

When \(\lambda_n^{\rm arch}\ge0\), this is equivalent to bounding the negative part by \(\lambda_n^{\rm arch}\). For this split, the exact formula for the archimedean part and its discrete convexity give

\[
I_-:=\{n\ge1:\lambda_n^{\rm arch}<0\}=\{1,2,\ldots,7\}.
\]

The certification uses

\[
\lambda_n^{\rm arch}
=1-\frac n2(\gamma+\log(4\pi))
+\sum_{r\ {\rm odd}}
\left[\left(1-\frac1r\right)^n-1+\frac nr\right]
\]

and, for \(d_n=\lambda_{n+1}^{\rm arch}-\lambda_n^{\rm arch}\),

\[
d_{n+1}-d_n
=\sum_{r\ {\rm odd}}\frac{(1-1/r)^n}{r^2}>0.
\]

The interval evaluations \(d_3\in(0.0062,0.0063)\), \(\lambda_7^{\rm arch}\in(-0.356,-0.355)\), and \(\lambda_8^{\rm arch}\in(0.020,0.022)\), together with the direct negative values at \(n=1,2\), fix the set. At those seven indices the full lower bound must be verified, and the positive prime excursion cannot be discarded. It does not help to substitute the inequality with

\[
\lim_{\varepsilon\downarrow0}
\int_1^\infty|\psi(y)-y+1|\,|f'_{n,\varepsilon}(y)|\,dy,
\]

because that reverts to an already-explored symmetric bound of RH-strength. Three candidate classes currently identified, without claiming exhaustiveness, are a global involution between prime cells, a pole–Gamma–prime compensation identity, or a one-sided arithmetic variational principle.

### Second track: triage of LP and GAP-Z

This track must be short. For LP, an abstract theorem or a counterexample is needed in a class containing both the zeta construction and an off-line control, and concluding at the true \(\mu_L\). For GAP-Z, it must be decided whether ZERO is controlled by axioms shared by both builds or whether it already requires a specific Euler identity. No further proxy campaign is authorized.

The possible outcomes are sufficient to decide the investment:

1. a build-neutral theorem: the piece remains as infrastructure;
2. a counterexample: the formulation is withdrawn;
3. the need for a separating arithmetic property: the strength is distributed and exclusive attribution to IDENT falls.

### Third track: RDI only if a mechanism appears

If the recent route is still needed, a single coordinate is frozen, preferably `C_core`, with an explicit order of limits and Gamma–Euler source. No further equivalents of `RDI-ANCHOR` are developed. A new formulation counts only if it produces an estimate the previous one lacked. The off-line control is deductive only when it belongs to a class of completed objects with comparable coefficients, Gamma factor, functional equation, and regularization; a hand-inserted quartet is only a test of the zero-side detector.

### Bibliographic and falsification gate

Before calling an idea new, its statement must be written without repository-specific vocabulary, searched by formula and mechanism in primary sources, and its hypotheses and conclusion compared. This audit is internal; it does not certify bibliographic priority.

Before opening another phase, a candidate must:

1. fail structurally against an off-line arithmetic control belonging to a defined class; if only a planted quartet exists, surviving that test is recorded as a heuristic falsification;
2. be compatible with an on-line control without using its zeros;
3. preserve conjugation, transverse support, and linear multiplicity;
4. state the order of all limits;
5. not use Weil positivity, real-rootedness, an already-real divisor, or an adapted metric;
6. contribute a new identity or inequality, not another proxy or coordinate change.

## Advancement criterion for the next cycle

A phase is not opened for the sheer quantity of computations. It is opened when there is a new mathematical degree of freedom and at least one of these outcomes:

- a candidate signed lemma with verifiable arithmetic hypotheses;
- a counterexample that removes an open obligation;
- a strict reduction eliminating an obligation without substituting it with an equivalent;
- a build-neutral proof of LP or GAP-Z at the correct limiting object;
- an external geometric construction with an independent diagonal and polarization.

Until then, the work belongs to the planning dossier. The immediate priority is to repair paper 36's target and submit the one-sided route to the bibliographic gate. Afterward it is decided whether it merits mathematical development or whether it too falls under an already-known no-go.

## Navigation

- [`PAPER36_AUDIT.md`](PAPER36_AUDIT.md): detailed audit of the manuscript's column.
- [`RH2017_RH9_AUDIT.md`](RH2017_RH9_AUDIT.md): balance of the nine programs.
- [`PHASES_AUDIT.md`](PHASES_AUDIT.md): complete genealogy of phases.
- [`NO_GO_AND_RETRACTIONS.md`](NO_GO_AND_RETRACTIONS.md): walls, circularities, and precedence.
- [`LIVE_FRONTIER_AND_RESTART_PLAN.md`](LIVE_FRONTIER_AND_RESTART_PLAN.md): operational restart protocol.
- [`COVERAGE_INDEX.md`](COVERAGE_INDEX.md): inventory, coverage, and size.
- [`fragments/`](fragments/): block audits supporting this synthesis.
