# Strong margin RH-strength audit

## Purpose

After `221` and `223`, the absolute PNT-envelope routes are no longer
viable.  One remaining route in `196` is the strong margin
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{1}
\]

This note records the logical strength of (1).  It is not a mild estimate:
together with the finite certificate for \(1\le n\le7\), it implies the
full Li criterion and therefore RH.

Thus any proof of (1) must contain RH-strength information, not merely the
already available A0/VK size input.

## Strong margin implies Li positivity

The finite Omega7 certificate already proves the required Li positivity for
\[
  1\le n\le7.
\]

For \(n\ge8\), (1) gives
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}.
\tag{2}
\]

The archimedean coefficients in this phase satisfy
\[
  \lambda_n^{\rm arch}>0
  \qquad(n\ge8),
\tag{3}
\]
as recorded in the base and asymptotic audits.  Hence
\[
\boxed{
  \lambda_n\ge0
  \qquad(n\ge1).
}
\tag{4}
\]

By Li's criterion, (4) is equivalent to RH.  Therefore
\[
\boxed{
  \hbox{finite certificate for }1\le n\le7
  \quad+\quad
  \hbox{strong margin (1)}
  \quad\Longrightarrow\quad
  \mathrm{RH}.
}
\tag{5}
\]

This is why Theorem C of `196` is a valid closure route for Omega7.

## Zero-side obstruction

The same conclusion can be seen directly from the zero formula
\[
  \lambda_n=\sum_\rho\left[1-\left(1-{1\over\rho}\right)^n\right],
\tag{6}
\]
under the standard symmetric limiting interpretation.

If a zero lies off the critical line, then one of its functional-equation
partners produces a factor
\[
  z_\rho=1-{1\over\rho}
\]
with
\[
  |z_\rho|>1.
\tag{7}
\]

The terms \(z_\rho^n\) then create exponentially large oscillatory
contributions to \(\lambda_n\).  Along infinitely many \(n\), those
contributions force the Li sequence below any fixed linear-logarithmic
archimedean lower barrier, unless canceled by a still larger off-line
contribution.  The standard Li theorem packages this dominance argument
precisely: nonnegativity of all \(\lambda_n\) is equivalent to excluding all
off-critical zeros.

Thus the strong margin is not just a positivity improvement; it excludes
the same off-line zero mechanisms as RH.

## Consequence for the phase

The strong-margin route remains viable, but it cannot be proved from:

1. A0 alone, because A0 is only an absolute tail estimate;
2. VK PNT decay alone, because `221` and `223` show absolute VK estimates
   lose exponentially in the Laguerre bulk;
3. finite \(n\le8\) checks alone, because (1) is an infinite Li-family
   assertion.

A proof of (1) must therefore supply one of the missing RH-strength
objects already listed in `196`:

- a positive increment/Fejer measure with enough logarithmic density;
- a one-sided tail theorem;
- a comparative Loewner--Schur positivity theorem;
- or a global half-plane theorem.

## Status

Closed as a logical-strength audit.

A1 remains open.  The strong margin would close Omega7, but proving it is
an RH-strength task.
