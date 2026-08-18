# Bordered Euler current no-go and exact target

## Purpose

This note closes the tautological part of the bordered Euler-current route for
A1 and records the exact theorem still capable of closing it.

The A1 core is
\[
  C_n
  =
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}.
\]

A bordered route would close A1 only if it proves
\[
  C_n\ge0\qquad(n\ge8)
\]
from a positive structure constructed before the Li sign is used.

## Schur complement rigidity

Let \(H>0\) be a finite Hermitian matrix, let \(v\) be a column vector, and
let \(a\in\mathbb R\). Put
\[
  B=
  \begin{pmatrix}
    H&v\\
    v^*&a
  \end{pmatrix}.
\]
Then
\[
  {\det B\over\det H}=a-v^*H^{-1}v.
\tag{1}
\]

Moreover,
\[
  B\ge0
  \quad\Longleftrightarrow\quad
  a-v^*H^{-1}v\ge0.
\tag{2}
\]

Indeed, (1) is the determinant factorization obtained by eliminating the
base block. For (2), take the congruence
\[
  \begin{pmatrix}
    I&0\\
    -v^*H^{-1}&1
  \end{pmatrix}
  B
  \begin{pmatrix}
    I&-H^{-1}v\\
    0&1
  \end{pmatrix}
  =
  \begin{pmatrix}
    H&0\\
    0&a-v^*H^{-1}v
  \end{pmatrix}.
\]
Congruence preserves positivity because the transforming matrix is
invertible, and \(H>0\).

Therefore any identity of the form
\[
  C_n={\det B_n\over\det H_n}
\tag{3}
\]
with \(H_n>0\) is exactly the same as saying that the Schur complement of
\(B_n\) is \(C_n\). The assertion \(B_n\ge0\) is then equivalent to \(C_n\ge0\).

## No-go class

The following class cannot close A1:

\[
\begin{gathered}
\text{construct }H_n>0,\ v_n,\ a_n,\\
\text{verify }C_n=a_n-v_n^*H_n^{-1}v_n,\\
\text{then infer }C_n\ge0\text{ from the bordered form itself.}
\end{gathered}
\]

This is not a proof mechanism. It is a coordinate change. The missing sign is
not produced; it is renamed as positivity of the bordered matrix.

The obstruction is sharp. For every real number \(c\), the one-dimensional
choice \(H=(1)\), \(v=0\), \(a=c\) gives
\[
  {\det B\over\det H}=c.
\]
Thus no theorem based only on the formal bordered determinant algebra can
force the quotient to be nonnegative. Any true positivity theorem must use
extra arithmetic structure not contained in the Schur identity.

## Imported Gram positivity is also insufficient

If one proves independently that \(B_n\) is a Gram matrix,
\[
  B_n=(\langle q_i,q_j\rangle)_{i,j},
\]
then A1 follows at once from (2). Such a theorem would be acceptable, but it
must be proved before the identity with \(C_n\) is interpreted as a Li sign.

The existing finite positive-star and finite Weil constructions do not supply
this for A1. They give build-neutral finite positive infrastructure. Their
unclosed step is the cofinal arithmetic identification of the uncontracted
Xi divisor or, equivalently, the positivity of the completed boundary current
for the Li test family.

Thus a finite Gram matrix is useful only if both statements are proved:

1. the exact Schur complement is \(C_n\);
2. the same bordered matrix is positive by a zeta-specific Euler--Gamma
   energy, not by choosing the matrix after the sign is known.

Without the second statement, the Gram language does not add force.

## Off-line discrimination test

A build-neutral bordered theorem cannot be the missing proof. Suppose a
bordered-current positivity principle depends only on formal data shared by a
typed off-line control: finite self-adjoint blocks, Gamma symmetry, paired
continuation, and the same determinant algebra. Then the same principle would
give nonnegative Li coefficients for that control.

But an off-line zero \(\rho\) has one Li multiplier with
\[
  \left|1-{1\over\rho}\right|>1,
\]
and the paired contribution gives a negative geometric subsequence for the
Li coefficients. Hence any principle that survives unchanged under such a
control is false as a proof of A1.

The bordered route must therefore fail for the off-line control at a named
zeta-specific identity, not merely at the final interpretation of positivity.

## Exact surviving theorem

The bordered Euler-current route closes A1 exactly if it proves the following.

For every \(n\ge8\), there exist explicitly constructed finite data
\[
  H_n>0,\qquad v_n,\qquad a_n,
\]
obtained from the completed Euler--Gamma package with the A0 cutoff \(T_n\),
such that:

\[
  C_n=a_n-v_n^*H_n^{-1}v_n,
\tag{4}
\]
and
\[
  \begin{pmatrix}
    H_n&v_n\\
    v_n^*&a_n
  \end{pmatrix}\ge0
\tag{5}
\]
is proved from a positive zeta-specific current, energy, monotonicity or
boundary-measure construction which is not valid for a typed off-line
control.

By the Schur complement theorem, (4) and (5) imply \(C_n\ge0\) for all
\(n\ge8\). Combined with A0 and the finite certificate, this closes Omega7.

Conversely, if (5) is not proved independently, the route is only the
tautology
\[
  C_n\ge0
  \Longleftrightarrow
  B_n\ge0.
\]

## Status

The determinant and Schur algebra is closed. The tautological bordered-current
class is eliminated.

No document in phase 102 or in the immediately preceding current phases
supplies the required independent positivity theorem. The live bordered target
is therefore the zeta-specific positive-current theorem above. It is another
exact formulation of A1, not a completed proof.
