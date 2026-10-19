# Phase 38 — Final Audit and Purity

This phase subjects the main claims of Phases 35–37 to adversarial audit: the positivity sharpening of Doc 103, the dichotomy theorem of Doc 112, the almost-periodicity theorem of Doc 113, and the tensor-index identity of Doc 106, and then attempts a repair of the Jacobi-trace criterion by replacing kernel positivity with moment rigidity.

## Results
- Adversarial audit of Doc 103 (strict positivity of $W_\lambda$, single-scale trace criterion): audited. (AUDIT — see document for verdict detail)
- Adversarial audit of Theorem 2.3 of Doc 112 (the conditional dichotomy $m<\infty\Rightarrow m=0$): audited. (AUDIT)
- Adversarial audit of Theorem 5.2 of Doc 113 (non-Stepanov-almost-periodicity of $\zeta$ in the strip): audited. (AUDIT)
- Adversarial audit of the tensor-index identity (Doc 106, Proposition 3.5): audited. (AUDIT)
- Repair of the trace criterion: the Jacobi-coefficient computation for the Meixner–Pollaczek polynomials associated with $dm_\infty$ is verified exactly ($a_n^{\mathrm{MP}}=\tfrac12\sqrt{(n+1)(n+2\lambda)}$, matching $a_n^\infty/2$ at $\lambda=1/4$), and the criterion is reformulated using moment rigidity (determinacy of the Hamburger moment problem) instead of kernel positivity. (PROVED, for the reformulated moment-rigidity version; repairs a gap in the kernel-positivity approach)

## Documents
- `114-adversarial-audit-of-doc-103-positivity.md`: audit of Doc 103's positivity/sharpening claims.
- `115-adversarial-audit-of-theorem-2-3.md`: audit of Doc 112's conditional dichotomy.
- `116-adversarial-audit-of-theorem-5-2.md`: audit of Doc 113's almost-periodicity claim.
- `117-adversarial-audit-the-tensor-index-identity-doc.md`: audit of the tensor-index identity of Doc 106.
- `118-repair-of-the-trace-criterion-moment-rigidity.md`: exact Meixner–Pollaczek Jacobi-coefficient computation and the moment-rigidity repair of the trace criterion.

## Relation to other phases
Audits results from Phase 35 (Doc 103), Phase 36 (Doc 106), and Phase 37 (Docs 112, 113). The moment-rigidity repair of Doc 118 feeds forward into the G1/G2 interface work of Phase 39.
