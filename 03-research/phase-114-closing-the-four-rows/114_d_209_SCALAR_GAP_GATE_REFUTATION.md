# D.209 — The scalar complement gap cannot close the corrected Schur gate

## Result

The flat-order-60 split solves the safe-side coupling problem and its
post-600 tail is negligible.  It does **not** close the final endpoint by
the scalar estimate `A_QQ >= 0.219 I`.

At FFT resolution `2^20`, the split-invariant scalar-gap Schur matrix on
the 198-dimensional primitive finite block is

\[
 K_{\rm scalar}=\operatorname{diag}(\lambda)-{1\over0.219}H,
\]

where `H=C C*` is the complete measured finite-to-complement residual
Gram.  Its numerical spectrum has 43 negative eigenvalues and

\[
 \lambda_{\min}(K_{\rm scalar})=-5.3259444363\ldots.
\]

For the source-defined decomposition

\[
 S=E_{60,200}\cap\ker J_+\cap\ker J_-,\qquad D=S^\perp,
\]

the restrictions give

\[
 \lambda_{\min}(K_{\rm scalar}|_D)=-5.2744572709\ldots
\]

with 40 negative directions, whereas

\[
 \lambda_{\min}(K_{\rm scalar}|_S)=0.7083032732\ldots.
\]

Thus endpoint flatness places the safe block correctly, but the crude
replacement of the Green operator by `0.219^{-1}I` destroys the delicate
block.  Promoting or repartitioning finite directions cannot repair the
full scalar-gap matrix, because the matrix above is invariant under such a
finite orthogonal split.

## Resolution check

The same calculation at grids `2^16,2^17,2^18,2^20` gives respectively
40, 41, 42 and 43 negative eigenvalues, with minima

\[
 -1.718,\quad-2.393,\quad-9.219,\quad-5.326.
\]

These are diagnostics rather than directed enclosures, but their order-one
negative scale rules out treating the failure as roundoff.  No negative
statement about the true Schur complement follows: only the **scalar-gap
proof route** is refuted.

## Required next object

The correct gate is

\[
 A_{PP}-A_{PQ}A_{QQ}^{-1}A_{QP}>0,
\]

or its exact `D/S/Q` Feshbach form.  The next certificate must therefore
construct a directed upper enclosure of

\[
 A_{PQ}A_{QQ}^{-1}A_{QP},
\]

retaining the growth of `A_QQ` on high Legendre modes.  The uniform bound
`A_QQ^{-1} <= 0.219^{-1}I` discards precisely that information.  D.208
still supplies the useful post-600 capacity estimate, but it cannot decide
this operator-valued Green gate.

The reproducible calculation is
`114_d_209_t6_scalar_gap_gate_diagnostic.py`.  It does not edit or support
any claim in the paper.
