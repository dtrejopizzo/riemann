# Phase 31 — Moments of $C_\infty$ and Selberg's Theorem

This one-document phase studies the moments $M_k(T) = \frac{1}{N(T)}\sum_{\gamma_n\le T} C_\infty(\gamma_n)^k$ of the CCM spectral deficit, aiming to connect its decay with Selberg's distribution theorem for $\log|\zeta'(\rho_n)|$ and to show that the infimum of the deficit is attained.

## Results
- $M_1(T)=0$ for every $T$ iff RH, directly from non-negativity of $C_\infty$ and the Inc. Inv. $\iff$ RH equivalence. (PROVED)
- $M_1(T)\ll T^{1-2\sigma_{\min}}\log T\to0$ (Ingham estimate) and the global variance $V^{\mathrm{glob}}(T)\to0$. (PROVED)
- $c_* := \inf_n C_\infty(\gamma_n) = 0$ unconditionally. (PROVED)
- RH $\iff$ the infimum $c_*=0$ is attained $\iff M_1(T)\equiv0$. (PROVED as a reformulation; the attainment question itself is left open)
- Whether the infimum $c_*=0$ is actually attained at some $n$: identified as a question of compactness/semicontinuity of $\gamma\mapsto C_\infty(\gamma)$. (OPEN)

## Documents
- `58-moments-of-and-selberg-s-theorem.md`: full derivation of the moment formulas, the Ingham bound, and the reformulation of RH as attainment of the infimum.

## Relation to other phases
Builds on Phase 29 Docs 42–44, 54 (deficit formula, positivity, arithmetic formula). The open attainment question motivates Phase 32's search for a compactness/positivity mechanism via Jacobi operators.
