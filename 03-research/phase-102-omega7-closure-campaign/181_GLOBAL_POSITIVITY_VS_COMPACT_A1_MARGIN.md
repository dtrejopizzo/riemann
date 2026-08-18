# Global positivity versus compact A1 margin

## Purpose

The documents `172`--`180` sharpened a global positivity route:
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2).
\]

That route is equivalent to RH and would close Omega7 through Li.  This note
separates it from the compact A0/A1 decomposition.

The point is simple but important:

- global RH/Li positivity closes the project goal;
- compact A1, as isolated by the A0 tail budget, requires an additional
  quantitative margin or a direct signed-core proof.

## Global route

The chain from `172`--`175` is:
\[
\begin{array}{c}
[g_{|j-k|}]_{1\le j,k\le N}\ge0\quad(N\ge1)\\
\Updownarrow\\
\Re(\xi'/\xi)(s)\ge0\quad(\Re s>1/2)\\
\Updownarrow\\
RH\\
\Downarrow\\
\lambda_n\ge0\quad(n\ge1).
\end{array}
\tag{1}
\]

This is enough to close Omega7, because Omega7 is Li positivity.

## Compact A1 route

The A0/A1 decomposition instead writes, for \(n\ge8\),
\[
  C_n(T_n)
  =
  \lambda_n-R_n(T_n)-{1\over4}\lambda_n^{\rm arch},
\tag{2}
\]
as in `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`.

A0 supplies
\[
  |R_n(T_n)|\le {1\over4}\lambda_n^{\rm arch}.
\tag{3}
\]

Therefore compact A1 follows from the stronger margin
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}
  \qquad(n\ge8),
\tag{4}
\]
because then
\[
  C_n(T_n)
  \ge
  {1\over2}\lambda_n^{\rm arch}
  -{1\over4}\lambda_n^{\rm arch}
  -{1\over4}\lambda_n^{\rm arch}
  =
  0.
\tag{5}
\]

But ordinary Li positivity gives only
\[
  \lambda_n\ge0.
\tag{6}
\]

Thus
\[
  \lambda_n\ge0
  \quad\not\Longrightarrow\quad
  C_n(T_n)\ge0
\tag{7}
\]
from the A0 estimate alone.

## Margin in the Schoenberg language

The Schoenberg diagonal is
\[
  K(n,n)=2\lambda_n.
\]

The compact A1 sufficient margin (4) is
\[
  K(n,n)\ge\lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{8}
\]

This is strictly stronger than diagonal nonnegativity:
\[
  K(n,n)\ge0.
\]

Similarly, Toeplitz positivity of the increment sequence \(g_m\) gives
\[
  K_N\ge0
\]
and therefore \(K(n,n)\ge0\), but it does not automatically give the
archimedean lower bound (8).

## What would bridge global positivity to compact A1

To close compact A1 through the global route, one needs one of the following
additional theorems.

### Margin theorem

Prove
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{9}
\]

This is the strong-margin route already isolated in
`122_STRONG_MARGIN_REDUCTION.md` and `164_A1_TOEPLITZ_SCHUR_MARGIN.md`.

### One-sided tail theorem

Improve A0 from an absolute bound to a signed bound:
\[
  R_n(T_n)\le \lambda_n-{1\over4}\lambda_n^{\rm arch}.
\tag{10}
\]

For this to be useful, the right side must be bounded from Euler--Gamma data
without assuming the conclusion.

### Direct compact signed-core theorem

Prove
\[
  C_n(T_n)\ge0
  \qquad(n\ge8)
\tag{11}
\]
by one of the local arithmetic mechanisms:
Laguerre lobe balance, raised balances, finite prime-power certificates, or
the recurrence forcing theorem.

## Consequence

The phase should not require both:

1. a global RH/Li proof; and
2. an independent compact A1 proof.

Either one closes Omega7.  But if the goal is to close every internal A0/A1
obligation as written, then a global proof must be supplemented by a margin
or direct compact argument.

This distinction prevents the following false inference:
\[
  \Re(\xi'/\xi)\ge0
  \Longrightarrow
  RH
  \Longrightarrow
  \lambda_n\ge0
  \Longrightarrow
  C_n(T_n)\ge0.
\]

The last implication is not supplied by A0.

## Status

Closed as a load-separation document.  A1 remains open.

The project can close through the global half-plane theorem, but the compact
A1 component remains open unless a margin, one-sided tail, or direct
signed-core proof is added.
