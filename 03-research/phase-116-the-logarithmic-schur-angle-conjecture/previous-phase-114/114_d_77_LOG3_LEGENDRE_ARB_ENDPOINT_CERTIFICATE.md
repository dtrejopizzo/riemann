# D.77 — Directed Legendre--Schur certificate at \(T=\frac12\log3\)

## Result

At the right endpoint of the first prime cell, the complete primitive form
satisfies

\[
 \boxed{
 QW_{\log3/2}(F,F)>1.15\,10^{-4}\|F\|_2^2
 }
\]

for every nonzero two-Tate-moment primitive function.  The directed Arb
certificate gives the separate lower bounds

\[
 \gamma_e>0.0006547054607,
 \qquad
 \gamma_o>0.0001159930558.                              \tag{1.1}
\]

At this endpoint the shift \(\log3\) has only null-set contact.  Thus the
finite part consists exactly of the \(n=2\) contact retained below.

## Finite Gamma block and tail

Retain the first 80 Gamma energies

\[
 \mathcal E_{b_j}(F)=\int_0^\infty e^{-b_jr}
 \|F-S_rF\|_2^2\,dr,
 \qquad b_j=2j+\tfrac12,quad0\le j<80.                 \tag{2.1}
\]

The omitted infinite tail is not discarded numerically.  D.76, with
\(B=b_{80}=160.5\), proves exactly

\[
 \sum_{j\ge80}\mathcal E_{b_j}\ge {B\over4}\mathcal E_B.\tag{2.2}
\]

Directed Robin root isolation at \(T=\log3/2\), including the exact even
Tate constraint, gives

\[
 {B\over4}d_{B,e}>0.0011586663336,
 \qquad
 {B\over4}d_{B,o}>0.0006199539287.                       \tag{2.3}
\]

The even inequality is used only after restriction to
\(\langle F,\cosh(t/2)\rangle=0\), as required by D.76.
Writing \(r\) for the normalized overlap with the first even Robin mode,
the exact bound used by the verifier is

\[
 d_{B,e}={2\over B}-\lambda_0
          +(\lambda_0-\lambda_1)r^2.                    \tag{2.4}
\]

Its directed lower enclosure uses \(\lambda_0^{\rm upper}\) in the
negative term and
\((\lambda_0^{\rm lower}-\lambda_1^{\rm upper})
\cdot(r^2)^{\rm lower}\) in the positive product.  The Robin roots are enclosed
as balls before evaluating \(r^2\); no monotonicity of the overlap in a
root endpoint is assumed.

## Legendre compression

Split the window into the three shift-compatible pieces

\[
 [-T,T-\log2],\quad[T-\log2,\log2-T],
 \quad[\log2-T,T].                                      \tag{3.1}
\]

Use respectively 28, 20 and 28 equal cells and the orthonormal Legendre
polynomials of degrees 0 through 9 on every cell.  The total dimension is
760 and reflection produces two blocks of dimension 380.  Translation by
\(\log2\) identifies corresponding boundary cells and preserves every
local polynomial degree exactly.

For distinct cells the exponential kernel is semiseparable.  If \(I<J\),

\[
 \langle\phi_{I,k},K_b\phi_{J,l}\rangle
 =\left(\int_I\phi_{I,k}(x)e^{bx}dx\right)
  \left(\int_J\phi_{J,l}(y)e^{-by}dy\right).             \tag{3.2}
\]

All factors are evaluated by rational Legendre coefficients and directed
exponential moments; no quadrature is used.

On one cell, \(u=K_bf\) solves

\[
 (b^2-\partial_x^2)u=2bf,quad
 u'(l)=bu(l),\quad u'(r)=-bu(r).                         \tag{3.3}
\]

For polynomial \(f\), its particular solution is the finite polynomial

\[
 v={2\over b}\sum_{m\ge0}{f^{(2m)}\over b^{2m}},        \tag{3.4}
\]

and \(u-v=Ae^{b(x-c)}+Be^{-b(x-c)}\).  Equations (3.3)--(3.4) give every
diagonal-cell matrix entry exactly and also give the exact finite Gram of
\((1-P)K_{\rm local}P\).

The two Tate moments are inserted as the positive rank-two penalty
\(1000H\).  On primitive vectors this penalty is identically zero.  Arb
congruence by an explicitly lower-triangular rational preconditioner and
directed Gershgorin disks proves, on both parity blocks,

\[
 \lambda_{\min}\bigl(P(q_{80}+1000H)P\bigr)>-0.00050.   \tag{3.5}
\]

The floating Cholesky used to choose the preconditioner has no evidentiary
role: the preconditioner is triangular with nonzero rational diagonal, and
the sign is proved on its Arb congruence.

## Infinite-dimensional complement

For the off-cell kernel, Taylor's formula and Young's inequality give for
cellwise degree nine

\[
 \|(1-P)g\|_2\le {h^{10}\over10!}\|g^{(10)}\|_2.       \tag{4.1}
\]

The derivatives of (3.2) have closed exponential rectangle integrals.  The
directed computation gives

\[
 \beta_{\rm cross}<0.000360559.                          \tag{4.2}
\]

The exact local Gram from (3.3)--(3.4) gives

\[
 \beta_{\rm local}<0.002382542,                          \tag{4.3}
\]

and the moment cross term is below \(2.6\,10^{-25}\).  The high--high
off-cell part is bounded by applying (4.1) in both variables.  After this
subtraction the high block satisfies

\[
 D_{\rm high}>1.8997318247I.                             \tag{4.4}
\]

Consequently its Schur loss is directedly bounded by

\[
 {\beta^2\over\alpha}<3.961\,10^{-6}<10^{-5}.           \tag{4.5}
\]

Combining (3.5) and (4.5), the first 80 channels plus the moment penalty
are larger than \(-0.00051I\).  On primitive vectors the penalty vanishes;
adding (2.3) yields (1.1).

## Reproduction

The complete calculation is in
`114_d_77_log3_legendre_arb_verify.py`.  It uses 512 bits for the
cancellation-sensitive local Grams and 224 bits after those enclosures have
been formed.  A successful run ends with

```text
PASS primitive endpoint margins: even=... odd=...
PASS T=log(3)/2 primitive endpoint certificate
```

No point diagnostic, unbounded Gamma truncation or sampled support interval
is used in the conclusion.
