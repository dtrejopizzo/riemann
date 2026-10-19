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
