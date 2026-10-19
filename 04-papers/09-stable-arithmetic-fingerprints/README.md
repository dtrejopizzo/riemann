# Paper 09 — Stable Local Arithmetic Fingerprints from Localized Weil Forms

To a localization of the explicit formula (height $T_0$, width $\sigma$, a finite band-limited
basis) and an $L$-function $L$, the paper attaches a finite Hermitian form $Q(L)$, its bottom
eigenvalue $\lambda_{\min}$ and a per-prime anatomy profile $(R_p(L))_p$. If two $L$-functions share
$\Lambda_L(n)$ for $n\le P$, these objects differ by at most $A e^{-\alpha(\log P)^2}$, with
$\alpha\approx\sigma^2/8$. The paper also proves an exact anatomy identity, a gradient formula and
a concavity/monotonicity structure. All results are elementary and do not depend on the Riemann
hypothesis.

## Main results

- `prop:anat`: $\lambda_{\min}=R_\infty-\sum_p R_p$ (anatomy identity) — PROVED.
- `prop:grad`: explicit Hellmann–Feynman gradient — PROVED (simple bottom eigenvalue assumed).
- `thm:stab`: exponential stability of $Q$ and $\lambda_{\min}$ under agreement of local data up to
  $P$ (Ramanujan bound, Gaussian window) — PROVED; profile stability with constant $C/g$ —
  PROVED given a spectral gap $g$.
- `cor:finger`: $Q(L)$ and the profile are local-arithmetic fingerprints — PROVED.
- `thm:concave`: concavity and monotonicity of $\lambda_{\min}$ in the coefficients; extremal
  reduction over coefficient boxes — PROVED.
- Illustrations of the bounds — NUMERICAL.

## Files

- `main.tex`, `main.pdf` — source and compiled paper.

## Relation to other papers

Uses the localized form of Paper 07; Paper 10 extends the anatomy to a complete local invariant.
