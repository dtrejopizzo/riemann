# Point 06 - Boundary limit

## Statement

The paired expression
\[
  -n+\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
\]
must pass to the boundary \(\varepsilon\downarrow0\) without separating the
polar divergence from the prime sum.

## Reduction

Fix \(n\ge8\) and choose \(T_n\) from A0. Split
\[
  \int_1^\infty E(y)f'_{n,\varepsilon}(y)\,dy
  =
  \int_1^{e^{T_n}}E(y)f'_{n,\varepsilon}(y)\,dy
  +
  \int_{e^{T_n}}^\infty E(y)f'_{n,\varepsilon}(y)\,dy.
\]

On the compact interval \([1,e^{T_n}]\), the function
\[
  f'_{n,\varepsilon}(y)
\]
converges uniformly to \(f'_{n,0}(y)\), because it is a finite polynomial in
\(\log y\) times \(y^{-2-\varepsilon}\), with coefficients continuous in
\(\varepsilon\). Since \(\psi(y)-y\) is bounded on the compact interval,
\[
  \int_1^{e^{T_n}}E(y)f'_{n,\varepsilon}(y)\,dy
  \longrightarrow
  \int_1^{e^{T_n}}E(y)f'_{n,0}(y)\,dy.
\]

The A0 tail estimate is uniform for \(0\le\varepsilon\le1\), so the same
cutoff controls the boundary passage in the tail.

## Closed conditional statement

For every \(n\ge8\), after A0,
\[
  \liminf_{\varepsilon\downarrow0}
  \left[-n+\int_1^\infty E(y)f'_{n,\varepsilon}(y)\,dy\right]
  \ge
  -n+\int_1^{e^{T_n}}E(y)f'_{n,0}(y)\,dy
  -{1\over4}\lambda_n^{\rm arch}.
\]

Consequently, point 06 is closed relative to the A1 compact core inequality.
No unpaired divergent series is used.
