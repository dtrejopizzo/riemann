# Point 05 - Global signed inequality

## Statement

Let
\[
  f_{n,\varepsilon}(y)
  =y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
  \qquad
  E(y)=\psi(y)-y .
\]
The open Li target for the infinite range is
\[
  \lambda_n^{\rm prime}
  =
  \lim_{\varepsilon\downarrow0}
  \left[-n+\int_1^\infty E(y)f'_{n,\varepsilon}(y)\,dy\right]
  \ge -\lambda_n^{\rm arch},
  \qquad n\ge8.
\]

Equivalently,
\[
  \lim_{\varepsilon\downarrow0}
  \int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
  \ge -\lambda_n^{\rm arch}.
\]

## Reduction obtained in this phase

The global inequality is reduced to a compact signed core plus a uniform tail.
For each \(n\ge8\), choose \(T_n\) satisfying the tail theorem of
`104_A0_MELLIN_LAGUERRE_TAIL.md`. Then
\[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T_n}}^\infty E(y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{\rm arch}.
\]
Therefore point 05 follows from the compact core inequality
\[
  -n+\int_1^{e^{T_n}}E(y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{\rm arch},
  \qquad n\ge8.
\]

This is the current minimal target. It is not a numerical finite check,
because the compact interval grows with \(n\). It is also not a local prime
shell statement: all prime powers up to \(e^{T_n}\), the pole term, and the
Laguerre oscillation remain paired.

## Closure status

Point 05 is not closed by this phase. Its tail component is closed after
choosing \(T_n\), but the signed compact core remains open and carries the
full Li obstruction.

The exact open theorem is:
\[
  {\rm Core}(n):=
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}
  \ge0
  \qquad(n\ge8).
\]

Any proof of this theorem, combined with the finite certificate for
\(1\le n\le7\), closes \(\Omega_7\).
