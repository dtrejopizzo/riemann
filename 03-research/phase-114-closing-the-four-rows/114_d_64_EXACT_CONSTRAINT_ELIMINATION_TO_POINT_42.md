# D.64 — Exact constraint elimination and the route to `T=0.42`

## 1. Purpose

The rank-two penalty of D.63 is convenient but pays an avoidable moment
projection residual.  This note removes that loss exactly.  With the same
shift-invariant step space and the same rigorous kernel residual, the
resulting finite lower matrix remains positive through `T=0.42`.

The formulas and center diagnostics are complete.  A finite Arb interval
cover, rather than point diagnostics, is still required before the entire
interval is declared closed.

## 2. Exact high-space elimination

Let `P` be the shift-invariant step projection, `Q=1-P`, and let

\[
 M:F\longmapsto(\langle F,h_+\rangle,\langle F,h_-\rangle).
\]

Write `M_P=P M^*`, `M_Q=Q M^*`, and

\[
 G_Q=M_Q^*M_Q=MM^*-M_P^*M_P.                            \tag{2.1}
\]

The two-by-two total Gram matrix is explicit:

\[
 MM^*=
 \begin{pmatrix}2\sinh T&2T\\2T&2\sinh T\end{pmatrix}. \tag{2.2}
\]

Let

\[
 \epsilon={2h_{max}\over\pi}\sqrt{I_{19}(T)},\qquad
 \alpha=C_{19}-c-\epsilon.                              \tag{2.3}
\]

The high block is bounded below by `alpha`.  If `F=p+q` is primitive, then
`M_Q^*q=-M_P^*p`.  Minimizing `alpha||q||^2` under this exact constraint
gives

\[
 \|q\|^2\geq
 \langle M_PG_Q^{-1}M_P^*p,p\rangle.                    \tag{2.4}
\]

Consequently the full primitive form is bounded below by the finite matrix

\[
 \boxed{
 R_T=P(A_0-K_{19})P-\epsilon P
 +\alpha M_PG_Q^{-1}M_P^*.}                             \tag{2.5}
\]

Unlike a penalty parameter, (2.5) loses no moment direction.  Every entry
is an elementary exponential expression and `G_Q` is only two by two.

## 3. Center diagnostics with `hmax<=0.002`

Using equal translated boundary cells and equal middle cells gives:

| `T` | dimension | `epsilon` | `alpha` | `lambda_min(R_T)` |
|---:|---:|---:|---:|---:|
| 0.347 | 349 | 0.084013 | 1.264389 | 0.404978 |
| 0.350 | 352 | 0.084374 | 1.264028 | 0.386595 |
| 0.360 | 362 | 0.085565 | 1.262838 | 0.316749 |
| 0.380 | 382 | 0.087896 | 1.260507 | 0.177611 |
| 0.400 | 402 | 0.090163 | 1.258240 | 0.073014 |
| 0.410 | 412 | 0.091274 | 1.257129 | 0.033533 |
| 0.420 | 422 | 0.092370 | 1.256032 | 0.000968 |

At `T=.42`, the eigenvalues of `G_Q` are approximately

\[
 2.0494\,10^{-9},\qquad1.4073\,10^{-7}.                 \tag{3.1}
\]

Their smallness is expected: cell averages approximate the smooth moment
vectors well.  It requires high-precision ball inversion, but the matrix is
strictly positive and only two dimensional.

## 4. Interval implementation requirement

For a reproducible cover, each subinterval must:

1. keep fixed boundary and middle cell counts;
2. evaluate disjoint kernel entries in the factored form
   \[
   {e^{bu}\operatorname{expm1}(b|I|)\,
    e^{-bs}\operatorname{expm1}(b|J|)
    \over b^2\sqrt{|I||J|}},                             \tag{4.1}
   \]
   avoiding four-exponential cancellation;
3. invert the `2 by 2` ball `G_Q` only after proving its determinant
   positive;
4. split parity and certify the shifted blocks;
5. include the Frobenius radius in Weyl's inequality.

Near `.42`, refining to `hmax<=.001` approximately halves `epsilon` and
creates a comfortable interval margin.  Near the endpoint, the D.61
capacity interval must be joined by geometrically expanding positive-width
balls because the boundary overlap length starts at zero.

## 5. Status

Proved algebraically: the exact primitive Feshbach lower matrix (2.5) and
its complete residual bound.

Verified diagnostically: positive center matrices through `T=.42`.

Not yet claimed: a directed overlapping cover of every `T` between `T_2`
and `.42`.  Pointwise floating diagnostics cannot replace that cover.
