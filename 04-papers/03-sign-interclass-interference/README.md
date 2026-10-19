# Paper 03 — On the Sign of Inter-Class Interference in Dirichlet Partial Sums: A Peak–Trough Reconciliation

For the ω-class decomposition of $D_F(t;N)=\sum_{n\le N}a_n n^{-1/2-it}$, the inter-class energy
ratio $r=(|D_F|^2-\sum_k|S_k|^2)/\sum_k|S_k|^2$ had been reported with opposite signs in two
earlier computations. The paper reconciles the two reports. By the mean value theorem for
Dirichlet polynomials the unconditional average of $r$ vanishes, so the sign of $r$ depends only
on the event one conditions on. $r$ increases with the conditioning quantile of $|D_F|$: it is
negative at troughs and positive at peaks. The often-cited value $r\approx-0.82$ at $t=150000$
was measured at a trough.

## Main results

- `prop:mvt`: the unconditional mean of $r$ vanishes asymptotically (mean value theorem) —
  PROVED, using CITED mean-value estimates.
- `cor:signfree`: $r$ has no intrinsic sign; its sign depends on the conditioning — PROVED.
- `thm:main` (stated as empirical): for ζ at $N=10^5$ the decile-conditional mean $\bar r(q)$
  is strictly increasing in $q$, with $\bar r=-0.998$ at troughs and a zero crossing near
  $q\approx0.69$ — NUMERICAL.
- `prop:150000`: $t=150000$ is a trough of $|D_\zeta(t;N)|$ — NUMERICAL.

## Files

- `main.tex`, `main.pdf` — source and compiled paper.
- `reproduce_colab.py` — reproduction notebook script.
- `P6_rbar_vs_quantile.pdf`, `P6_rbar_vs_quantile.png` — figure of mean $r$ against quantile.

## Relation to other papers

Builds on the ω-class decomposition of Paper 02.
