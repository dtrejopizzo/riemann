# Point 11 - Li assembly

## Inputs already closed

The finite range is certified:
\[
  \lambda_n>0,\qquad 1\le n\le7.
\]

The exact split and the boundary-corrected arithmetic formula are fixed:
\[
  \lambda_n
  =
  \lambda_n^{\rm arch}
  +
  \lambda_n^{\rm prime},
\]
and
\[
  \lambda_n^{\rm prime}
  =
  \lim_{\varepsilon\downarrow0}
  \left[-n+\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right].
\]

## Missing input

For every \(n\ge8\), one must prove
\[
  \lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}.
\]
After A0, this is reduced to A1:
\[
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{\rm arch}.
\]

## Assembly theorem

If A1 holds for all \(n\ge8\), then:

1. A0 gives a tail error at most \({1\over4}\lambda_n^{\rm arch}\).
2. Point 06 passes to \(\varepsilon=0\) without separating divergent pieces.
3. Hence \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\) for all \(n\ge8\).
4. Together with the finite certificate, \(\lambda_n\ge0\) for all \(n\ge1\).
5. By Li's criterion, RH follows.

## Status

The assembly is conditionally closed. The only missing mathematical theorem
in the direct route is A1.
