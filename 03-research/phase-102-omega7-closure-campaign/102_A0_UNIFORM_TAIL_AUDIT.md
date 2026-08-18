# 102 A0 uniform tail audit

## Verdict

The theorem `102_A0_UNIFORM_TAIL_THEOREM.md` is correct as an A0 closure. It
proves an unconditional absolute far-tail bound. The proof does not use RH,
zero locations or Li positivity; it uses only an explicit prime number theorem,
elementary Laguerre estimates and a positive archimedean lower bound in the
range \(n\ge8\).

The theorem is intentionally a tail theorem. It does not close A1.

## Laguerre derivative

With \(u=\log y\),

\[
  L_{n-1}^{(1)}(u)
  =
  \sum_{j=0}^{n-1}(-1)^j {n\choose j+1}{u^j\over j!}.
\]

For \(u\ge0\),

\[
  |L_{n-1}^{(1)}(u)|
  \le
  n(1+u)^{n-1}.
\]

Also

\[
  {d\over du}L_{n-1}^{(1)}(u)
  =
  \sum_{k=0}^{n-2}
  c_{n,k}u^k,
\]

where

\[
  |c_{n,k}|
  \le
  {1\over k!}{n\choose k+2}
  \le
  n^2 {n-2\choose k}.
\]

Hence

\[
  \left|{d\over du}L_{n-1}^{(1)}(u)\right|
  \le
  n^2(1+u)^{n-2}.
\]

This justifies the displayed estimate

\[
  |f'_{n,\varepsilon}(y)|
  \le
  3n^2 y^{-2}(1+\log y)^{n-1}
\]

uniformly for \(0\le\varepsilon\le1\).

## Cutoff \(T(n)\)

The theorem defines \(T(n)\) by the condition that for every \(u\ge T(n)\),

\[
  \eta(u)\ge (n+1)\log(1+u)+\log {12A n^2\over B_n}.
\]

This is stronger and cleaner than asking the inequality only at \(T(n)\). The
existence of such a cutoff follows from

\[
  {\eta(u)\over\log(1+u)}\to+\infty.
\]

For a final paper version one may insert a specific
Vinogradov--Korobov choice

\[
  \eta(u)=a u^{3/5}(\log u)^{-1/5}
\]

and then compute \(T(n)\) by a monotone search beyond an explicit monotonicity
threshold. That insertion is mechanical and independent of the sign problem.

## Uniformity in \(\varepsilon\)

After the change of variables \(u=\log y\), the only \(\varepsilon\)-dependent
factor left in the majorant is \(e^{-\varepsilon u}\). Since

\[
  e^{-\varepsilon u}\le1
  \qquad(0\le\varepsilon\le1),
\]

the estimate is uniform in \(\varepsilon\). No interchange of a limiting
process is used in the tail.

## Archimedean positivity

The theorem uses an explicit lower bound

\[
  0<B_n\le\lambda_n^{\rm arch}
  \qquad(n\ge8).
\]

This lower bound is supplied internally by
`151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`.  In particular, the
phase now has explicit positive \(B_n\) for all \(n\ge8\).

This is consistent with the Omega7 decomposition because paper 36 proves

\[
  \lambda_n^{\rm arch}<0
  \iff
  1\le n\le7.
\]

Thus the A0 range has a positive archimedean margin, and the final comparison
with \(\lambda_n^{\rm arch}/4\) has the correct sign.

## Exact residual

A0 closes the far tail

\[
  \int_{e^{T(n)}}^\infty E(y)f'_{n,\varepsilon}(y)\,dy.
\]

The remaining direct-route obligation is A1:

\[
  -n+\int_1^{e^{T(n)}}E(y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{\rm arch}
  \qquad(n\ge8).
\]

That is the force-bearing signed core.
