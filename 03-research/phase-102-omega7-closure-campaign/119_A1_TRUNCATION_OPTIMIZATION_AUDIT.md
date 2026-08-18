# A1 truncation optimization audit

## Purpose

This note tests whether A1 can be closed by changing only the cutoff
\(T_n\) after A0 has made the tail small.  The answer is negative: A0 is a
tail-removal theorem, not a sign theorem.

## Notation

For \(n\ge8\), write
\[
  A_n=\lambda_n^{\rm arch}>0,
\]
and decompose the paired prime contribution as
\[
  \lambda_n^{\rm prime}
  =
  K_n(T)+R_n(T),
\]
where
\[
  K_n(T)
  =
  -n+\int_1^{e^T}(\psi(y)-y)f'_{n,0}(y)\,dy
\]
and
\[
  R_n(T)
  =
  \lim_{\varepsilon\downarrow0}
  \int_{e^T}^{\infty}(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
\]
whenever the cutoff is already beyond the A0 range.  The A0 theorem gives
\[
  |R_n(T)|\le {1\over4}A_n
\]
for admissible \(T=T_n\).

A1 asks for
\[
  K_n(T_n)+{3\over4}A_n\ge0.
\tag{A1}
\]

## Algebraic comparison with Li positivity

Since
\[
  \lambda_n
  =
  K_n(T)+R_n(T)+A_n,
\]
one has the exact identity
\[
  K_n(T)+{3\over4}A_n
  =
  \lambda_n-R_n(T)-{1\over4}A_n.
\tag{1}
\]

Thus even if \(\lambda_n\ge0\) were already known, the A0 estimate alone
would give only
\[
  K_n(T)+{3\over4}A_n
  \ge
  \lambda_n-{1\over2}A_n.
\tag{2}
\]

Consequently, A1 is not a formal consequence of Li positivity plus the
absolute A0 tail estimate unless one also proves the stronger margin
\[
  \lambda_n\ge {1\over2}A_n
\]
or a one-sided tail statement
\[
  R_n(T)\le \lambda_n-{1\over4}A_n.
\]
Neither of these statements is supplied by A0.

More generally, if A0 is run with a budget
\[
  |R_n(T)|\le \alpha A_n,\qquad 0<\alpha<1,
\]
and the compact target is chosen as
\[
  K_n(T)+(1-\alpha)A_n\ge0,
\tag{3}
\]
then
\[
  K_n(T)+(1-\alpha)A_n
  =
  \lambda_n-R_n(T)-\alpha A_n.
\tag{4}
\]
The absolute tail bound plus \(\lambda_n\ge0\) yields only
\[
  K_n(T)+(1-\alpha)A_n\ge \lambda_n-2\alpha A_n.
\tag{5}
\]

Thus decreasing the tail budget improves the algebraic loss, but it does
not create a sign proof.  For every fixed positive \(\alpha\), a
truncation-only argument still needs a positive lower margin for
\(\lambda_n\) or a one-sided theorem for \(R_n(T)\).

## Consequence

Changing \(T_n\), making \(T_n\) very large, or shrinking the A0 budget cannot
by itself close A1.  The missing ingredient is still a signed theorem:

\[
  \lambda_n-R_n(T_n)\ge {1\over4}A_n
\]
for the present budget, or equivalently the original compact inequality
\[
  K_n(T_n)+{3\over4}A_n\ge0.
\]

This theorem must use arithmetic sign information beyond the absolute PNT
tail estimate.

## Eliminated class

The following proof pattern is eliminated:

1. choose \(T_n\) so that A0 gives a small absolute tail;
2. let \(T_n\to\infty\) or optimize over admissible cutoffs;
3. infer A1 from the limiting identity alone.

Step 3 is invalid unless it also proves a one-sided tail sign or a stronger
Li margin.  Therefore A1 remains a genuine compact signed problem after A0.

## Status

Closed as a no-go for truncation-only closure.  No new proof of A1 is
obtained.
