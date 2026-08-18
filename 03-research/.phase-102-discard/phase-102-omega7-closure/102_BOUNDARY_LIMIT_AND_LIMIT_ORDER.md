# 102 boundary limit and order of limits

## Objects

For `epsilon>0`,

[
  f_{n,\varepsilon}(y)
  =
  y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y).
]

The paired arithmetic identity is

[
  \lambda_n^{prime}
  =
  \lim_{\varepsilon\downarrow0}
  \left[
    -n+\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
  \right].
]

The equivalent boundary form is

[
  \lambda_n^{prime}
  =
  \lim_{\varepsilon\downarrow0}
  \int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
]

## Limit order

The admissible order for the direct route is:

[
  X=e^{T(n)}\quad\hbox{fixed after }n,
  \qquad
  \varepsilon\downarrow0,
  \qquad
  \hbox{then use the uniform tail theorem for }[X,\infty).
]

Equivalently, for each fixed `n>=8`,

[
\begin{aligned}
  \lambda_n^{prime}
  &=
  \lim_{\varepsilon\downarrow0}
  \left[
    -n+\int_1^{e^{T(n)}}E(y)f'_{n,\varepsilon}(y)\,dy
  \right]
  +R_n,\\
  |R_n|
  &\le {1\over4}\lambda_n^{arch},
\end{aligned}
]

provided A0 is instantiated with explicit constants.

## Fixed-core passage

On the compact interval `[1,e^{T(n)}]`, the function

[
  E(y)f'_{n,\varepsilon}(y)
]

converges pointwise to `E(y)f'_{n,0}(y)` away from the jump points of `psi`.
The jumps are harmless because `psi` is of bounded variation on compact
intervals and the integration-by-parts identity may be written as a
Stieltjes identity before passing to the Lebesgue form.  Since
`f'_{n,\varepsilon}` is uniformly bounded on each compact interval
`[1,e^{T(n)}]`, dominated convergence gives

[
  \lim_{\varepsilon\downarrow0}
  \int_1^{e^{T(n)}}E(y)f'_{n,\varepsilon}(y)\,dy
  =
  \int_1^{e^{T(n)}}E(y)f'_{n,0}(y)\,dy.
]

No divergent series is separated in this passage.  The pole contribution
remains the explicit term `-n`.

## Consequence

A0 plus the fixed-core passage reduce the infinite range to A1:

[
  -n+\int_1^{e^{T(n)}}E(y)f'_{n,0}(y)\,dy
  \ge -{3\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

If A1 is proved, then

[
  \lambda_n^{prime}
  \ge -\lambda_n^{arch}
  \qquad(n\ge8).
]

## Status

The boundary limit is closed conditionally on A0 and A1.  Its remaining
dependence is not an independent obstruction: the only sign-bearing input is
A1.
