# Phase 29 — Zeta Spectral Triples

This phase works from the Connes–Consani–Moscovici (CCM) construction of entire functions $\hat\xi_{\lambda,N}$ with all zeros real by construction, together with the associated Jacobi operator $J_\infty$, Weyl–Titchmarsh $m$-function, and spectral deficit $C_\infty(\gamma_n)$. The central question is whether the operator-theoretic construction converges to $\Xi(z)=\xi(1/2+it)$ and whether the zero set of $C_\infty$ coincides with (or is controlled by) the zero set of $\Xi$, reducing the problem to spectral/inverse-spectral theory (Borg–Marchenko, Kotani, de Branges spaces, Krein–Rutman, moment-determinacy).

## Results
- Operator self-adjointness holds by construction (Carathéodory–Fejér); the open obstacle throughout is operator/function convergence, not positivity. (PROVED for self-adjointness; convergence OPEN)
- Jacobi-coefficient recursion, Borg–Marchenko inverse-problem attack, and Möbius dynamics for $m_\infty$: structural reformulations, no closure. (OPEN)
- Euler–Lagrange characterization of $C_\infty$ and zero-counting lower bounds via Jensen's formula: partial quantitative results. (CONDITIONAL / OPEN)
- Identity $N\cdot m_\infty = C_\infty'/C_\infty$ (EF2): audited and found to have a genuine gap between two inequivalent EF2 formulations ("near miss"). (NO-GO as stated; gap identified)
- Explicit deficit formula via the Cauchy kernel and "Rigidity of the Cauchy–Poisson Transform" (single-point theorem): derived, with two candidate routes toward the inclusion needed for RH-style closure. (ARGUED)
- Poisson Completeness Theorem (kernel systems, Müntz–Szász) and theory of $\zeta$-compatible measures (axiomatics, rigidity): new structural framework built but not closing. (OPEN)
- Motivic geometry of the deficit ($\mathcal V_\zeta$, arithmetic Frobenius, cohomological positivity): exploratory construction. (OPEN)
- Three independent formalizations (I: Banach-lattice operator $\Phi$ + Krein–Rutman; II: de Branges space completeness; III: concrete category $\mathcal{MM}$, Deninger program): each pins down the precise frontier of its approach without closing it. (OPEN)
- Central Problem (injectivity of the Poisson transform at the zero sequence $\{\gamma_n\}$ without a sign hypothesis): shown to fail for generic sequences by a Beurling–Malliavin counterexample; the specific gap structure of $\{\gamma_n\}$ is essential and unresolved. (NO-GO for the generic case; OPEN for the specific case)
- Arithmetic formula for the deficit, $C_\infty(\gamma_n) = w(\gamma_n) - 2\,\mathrm{Re}[A_n]$ with $A_n$ the finite part of $\zeta'/\zeta$ at $\rho_n$: derived via Hadamard's formula and Abel regularization. (PROVED, conditional on prior docs' definitions)

## Documents
- `00-setup.md`: precise statement of the CCM construction and the semilocal Weil quadratic form.
- `01`–`12`: convergence, spectral gap, kernel positivity, Perron–Frobenius structure, zero equation, first moment, zero counting, Stieltjes transform, boundedness of zeros, Weyl sums, and an audit/correction of docs 10–11.
- `13`–`25`: Blaschke-product/H² structure, the Weyl–Titchmarsh $m$-function program, Jacobi coefficients, Borg–Marchenko/Möbius/Euler–Lagrange attacks, zeros of $C_\infty$, the reverse-inclusion attacks, spectral completeness, Kotani delocalization, derivative at zeros, lower bounds for $N_{C_\infty}(T)$.
- `26`–`41`: moment-problem determinacy, EF2 audits and the "two EF2s" gap, spectral geometry of $C_\infty/\Xi$, orthogonal polynomials and self-referential structure of $J_\infty$, four parallel directions (A–D: explicit formula, zero counting, Phragmén–Lindelöf, eigenvector delocalization/Szegő), connection to random matrix theory, complex zeros of $C_\lambda-\mu_\lambda$, extreme values, spectral $L^2$ energy (Gonek–Fujii).
- `42`–`54`: Cauchy-kernel deficit formula, rigidity of the Cauchy–Poisson transform, the zero-measure problem on $\mu_{\mathrm{off}}$, asymptotics of $C_\infty(\gamma_n)$, three new structures (Poisson completeness, $\zeta$-compatible measures, motivic geometry), the three formalized directions I–III, the Central Problem on Poisson-transform injectivity, and the arithmetic formula for the deficit.

## Relation to other phases
Feeds directly into Phase 30 (Langlands bridge for automorphic $L$-functions, built on the same CCM spectral-triple apparatus) and Phase 32 (CCM program bridge, which reuses the semilocal Jacobi/Stieltjes machinery of this phase).

## Contents

- `01-even-simple.md` — Hypothesis H1: The simple-even property
- `02-convergence.md` — Attack on convergence: Hurwitz, Montel, and the spectral gap
- `03-spectral-gap.md` — The spectral gap and the new wall
- `04-positivity-kernel.md` — Question 29.1: Non-negativity of the kernel $k_\lambda$
- `05-perron-frobenius.md` — Perron-Frobenius structure and arithmetic orthogonality
- `06-zero-equation.md` — Zero equation and quantitative convergence
- `07-first-moment.md` — First-moment equation and the Moments Conjecture
- `08-zero-counting.md` — Zero counting and weak convergence of the spectral measure
- `09-stieltjes.md` — The Stieltjes transform and the fixed-point equation
- `10-boundedness.md` — Boundedness of individual zeros and the implicit function theorem
- `11-weyl-sum.md` — The Weyl sum over the zeros and average convergence
- `12-audit-correction.md` — Audit and correction of docs 10–11
- `13-blaschke.md` — The Blaschke product and the structure of H2
- `14-m-function.md` — The Weyl–Titchmarsh m-function and the program toward RH
- `15-jacobi-coefficients.md` — Jacobi coefficients of the CCM operator
- `16-borg-marchenko.md` — Attack A: the Borg–Marchenko inverse problem for $J_\infty$
- `17-mobius-dynamics.md` — Attack C + B: Möbius dynamical system and functional equation of $m_\infty$
- `18-euler-lagrange-attack.md` — Attack D: The Euler-Lagrange equation as a spectral constraint and the potential $C_\infty$
- `19-zeros-c-infinity.md` — Doc 19: Zeros of the potential $C_\infty$ and Jensen's formula
- `20-weil-formula-attack.md` — Doc 20: The reverse inclusion and the Weil formula
- `21-inverse-inclusion-attack.md` — Doc 21: Direct attack on the reverse inclusion
- `22-spectral-completeness.md` — Doc 22: Spectral completeness and the gap between the empirical measure and the Weyl-Titchmarsh …
- `23-kotani-delocalization.md` — Doc 23: Kotani theory and delocalization of the eigenvectors of $J_\infty$
- `24-derivative-at-zeros.md` — Doc 24: The derivative $C_\infty'(\gamma_n)$ and the simplicity of the zeros of $C_\infty$
- `25-lower-bound-zeros-c.md` — Doc 25: Lower bound for $N_{C_\infty}(T)$ and the closing argument
- `26-moment-problem-determinacy.md` — Doc 26: The decisive experiment — Is the moment problem of $\mu_\gamma^{real}$ determinate?
- `27-ef2-audit.md` — Doc 27: Audit of EF2 — is the identity $N\cdot m_\infty = C_\infty'/C_\infty$ rigorous?
- `28-two-ef2-near-miss.md` — Doc 28: The Two EF2s, the Near-Miss, and the Exact Point of the Gap
- `29-spectral-quotient-geometry.md` — Doc 29: Spectral Geometry of the Quotient $C_\infty / \Xi$
- `30-orthogonal-polynomials-eigenvalues.md` — Doc 30: Orthogonal Polynomials, Eigenvalues, and the Self-Referential Structure of $J_\infty$
- `31-scale-correction.md` — Doc 31: Correcting the Scale Error of Doc 30 — $b_n \neq 0$
- `32-doc-32-direction-b-zero-counting.md` — Doc 32: Direction B — Zero Counting of $C_\infty$ and the Reverse Inclusion
- `33-doc-33-direction-a-the-explicit-formula.md` — Doc 33: Direction A — The Explicit Formula as a Fixed-Point Equation
- `34-doc-34-direction-c-the-phragm-n.md` — Doc 34: Direction C — The Phragmén-Lindelöf Principle for the Quotient $Q$
- `35-doc-35-direction-d-eigenvector-delocalization.md` — Doc 35: Direction D — Eigenvector Delocalization and the Szegő Theorem
- `36-doc-36-deep-audit-of-direction-b.md` — Doc 36: Deep Audit of Direction B — EF2-emp and Zero Counting
- `37-doc-37-connection-with-random-matrix-theory.md` — Doc 37: Connection with Random Matrix Theory and Montgomery's Conjecture
- `38-doc-38-complex-zeros.md` — Doc 38: Complex Zeros of $C_\lambda - \mu_\lambda$ in the Strip
- `39-doc-39-the-infimum-of-and-extreme.md` — Doc 39: The Infimum of $C_\lambda$ and Extreme Values of Dirichlet Sums
- `40-equivalence-rh-reverse-inclusion.md` — The Equivalence RH $\iff$ Reverse Inclusion in the Zeta Spectral Triples Program
- `41-doc-41-the-spectral-energy.md` — Doc 41: The Spectral $L^2$ Energy and the Gonek-Fujii Theorem
- `42-cauchy-kernel-explicit-deficit-formula.md` — Doc 42 — The Cauchy Kernel: Explicit Deficit Formula and the Two Routes toward Inc. Inv.
- `43-rigidity-of-the-cauchy-poisson-transform.md` — Doc 43 — Rigidity of the Cauchy-Poisson Transform: the Single-Point Theorem
- `44-zero-measure-problem-rigorous-justification.md` — Doc 44 — The Zero-Measure Problem: Rigorous Justification of the Representation and Three Attacks on …
- `45-asymptotics-of-as-mean-variance-and-connection.md` — Doc 45 — Asymptotics of $C_\infty(\gamma_n)$ as $n\to\infty$: Mean, Variance, and Connection with Montgomery
- `46-break-three-new-mathematical-structures.md` — Doc 46 — The Break: Three New Mathematical Structures for RH
- `47-poisson-completeness-theorem-kernel-systems.md` — Doc 47 — The Poisson Completeness Theorem: Kernel Systems and the Müntz-Szász Condition
- `48-theory-of-compatible-measures-axiomatics-structure.md` — Doc 48 — Theory of $\zeta$-Compatible Measures: Axiomatics, Structure, and the System Rigidity Theorem
- `49-motivic-geometry-of-the-deficit-the-arithmetic.md` — Doc 49 — Motivic Geometry of the Deficit: $\mathcal{V}_\zeta$, the Arithmetic Frobenius, and Cohomological …
- `50-formalization-of-direction-ii-the-de-branges.md` — Doc 50 — Formalization of Direction II: The de Branges Space, Exact Completeness, and the Precise Frontier
- `51-formalization-of-direction-i-the-operator.md` — Doc 51 — Formalization of Direction I: The Operator $\Phi$ on Banach Lattices and the Krein-Rutman Theorem
- `52-formalization-of-direction-iii-the-concrete-category.md` — Doc 52 — Formalization of Direction III: The Concrete Category $\mathcal{MM}$ and the Deninger Program
- `53-central-problem-injectivity-of-the-poisson.md` — Doc 53 — The Central Problem: Injectivity of the Poisson Transform without a Sign Hypothesis
- `54-arithmetic-formula-of-the-deficit.md` — Doc 54 — The Arithmetic Formula of the Deficit: $C_\infty(\gamma_n)$ as the Finite Part of $\zeta'/\zeta$ …
