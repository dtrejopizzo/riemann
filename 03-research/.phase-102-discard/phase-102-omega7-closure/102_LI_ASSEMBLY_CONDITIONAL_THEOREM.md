# 102 Li assembly conditional theorem

## Theorem

Assume:

1. the finite certificate

[
  \lambda_n>0\qquad(1\le n\le7);
]

2. the infinite signed inequality

[
  \lambda_n^{prime}\ge-\lambda_n^{arch}
  \qquad(n\ge8);
]

3. the paired definitions of `lambda_n^{prime}` and `lambda_n^{arch}` agree
   with the Li--Keiper coefficients of

[
  \xi(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
]

Then

[
  \lambda_n\ge0\qquad(n\ge1).
]

By Li's criterion, RH follows.

## Proof

For `1<=n<=7`, positivity is exactly assumption 1.

For `n>=8`, the split gives

[
  \lambda_n
  =
  \lambda_n^{arch}+\lambda_n^{prime}
  \ge
  \lambda_n^{arch}-\lambda_n^{arch}
  =
  0.
]

Thus all Li--Keiper coefficients are nonnegative.  Li's criterion applies to
the completed zeta function `xi`, so all nontrivial zeros lie on the critical
line.

## Status

The assembly is closed as a conditional theorem.  It becomes an unconditional
closure of Omega7 exactly when A1, together with the A0 tail and boundary
limit, proves the infinite signed inequality.
