# 102 A0 uniform tail theorem

## Statement

Let

[
  f_{n,\varepsilon}(y)
  =
  y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
  \qquad
  E(y)=\psi(y)-y.
]

Assume the explicit prime number theorem input

[
  |E(y)|\le A y\exp(-\eta(\log y))
  \qquad(y\ge e^{U_0}),
]

where `A>=1`, `eta` is increasing on `[U_0,\infty)`, and `eta(u)/log(1+u)`
tends to infinity.  Let `B_n` be any explicit lower bound satisfying

[
  0<B_n\le \lambda_n^{arch}\qquad(n\ge8).
]

For each `n>=8`, choose `T(n)>=U_0` so that, for every `u>=T(n)`,

[
  \eta(u)\ge (n+1)\log(1+u)+\log {12A n^2\over B_n}.
]

Then

[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T(n)}}^\infty
  E(y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{arch}.
]

Thus A0 is reduced to one external explicit input and one internal
phase-102 input:

- a zero-free-region prime number theorem in the displayed form;
- the explicit positive lower bound for `lambda_n^{arch}` when `n>=8`,
  supplied by `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`.

Neither input is RH-strength.

## Proof

Write `u=log y`.  The Laguerre polynomial has the finite expansion

[
  L_{n-1}^{(1)}(u)
  =
  \sum_{j=0}^{n-1}(-1)^j {n\choose j+1}{u^j\over j!}.
]

For `u>=0`,

[
  |L_{n-1}^{(1)}(u)|
  \le
  \sum_{j=0}^{n-1}{n\choose j+1}u^j
  \le
  n(1+u)^{n-1}.
]

The derivative in `u` satisfies

[
  \left|{d\over du}L_{n-1}^{(1)}(u)\right|
  \le n^2(1+u)^{n-2}.
]

Since

[
  f'_{n,\varepsilon}(y)
  =
  y^{-2-\varepsilon}
  \left[
    -(1+\varepsilon)L_{n-1}^{(1)}(u)
    +{d\over du}L_{n-1}^{(1)}(u)
  \right],
]

we have, uniformly for `0<=epsilon<=1`,

[
  |f'_{n,\varepsilon}(y)|
  \le
  3n^2 y^{-2}(1+\log y)^{n-1}.
]

Therefore

[
\begin{aligned}
  \left|
  \int_{e^T}^\infty E(y)f'_{n,\varepsilon}(y)\,dy
  \right|
  &\le
  3A n^2
  \int_T^\infty
  (1+u)^{n-1}\exp(-\eta(u))\,du.
\end{aligned}
]

By the defining condition on `T(n)`,

[
  (1+u)^{n-1}\exp(-\eta(u))
  \le
  {B_n\over 12A n^2}(1+u)^{-2},
  \qquad u\ge T(n).
]

Hence

[
  \left|
  \int_{e^{T(n)}}^\infty E(y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le
  {B_n\over4}
  \int_{T(n)}^\infty(1+u)^{-2}\,du
  \le {B_n\over4}
  \le {1\over4}\lambda_n^{arch}.
]

This proves the theorem.

## Status

A0 is structurally closed up to inserting the explicit PNT constants `A`,
`U_0` and `eta` chosen for the final paper.  The lower bound `B_n` is now
available internally from
`151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`.  The remaining PNT
insertion is specified in `152_EXPLICIT_PNT_INPUT_ADAPTER.md`; it is
mechanical and does not contain the sign problem of Omega7.
