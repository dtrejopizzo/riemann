# 102 A0 uniform tail target

## Target

Let

[
  f_{n,\varepsilon}(y)
  =
  y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
  \qquad
  E(y)=\psi(y)-y.
]

Prove an explicit `T(n)>=8n` such that

[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T(n)}}^\infty
  E(y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

## Allowed inputs

- Explicit prime number theorem with a zero-free-region error term.
- Uniform upper bounds for Laguerre polynomials and their derivatives.
- Exact archimedean lower bounds for `lambda_n^{arch}`.

## Status

Closed in `102_A0_UNIFORM_TAIL_THEOREM.md`.

The closure is deliberately crude: the threshold `T(n)` may be enormous, but
it is effective once explicit PNT constants are fixed. This is enough for the
logical decomposition, because all RH-strength content is now concentrated in
the finite signed core A1.
