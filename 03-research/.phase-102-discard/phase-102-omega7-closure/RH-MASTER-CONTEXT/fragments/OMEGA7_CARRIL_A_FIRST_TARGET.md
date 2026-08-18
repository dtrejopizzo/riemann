# Omega7 carril A first target

## Direct unit

The only canonical signed unit currently available is global:

[
  \mathcal U_{n,\varepsilon}
  =
  \int_1^\infty f_{n,\varepsilon}(y)\,dy
  -
  \int_{1^-}^\infty f_{n,\varepsilon}(y)\,d\psi(y),
]

where

[
  f_{n,\varepsilon}(y)
  =
  y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y).
]

It keeps the pole and prime powers paired. Equivalently,

[
  \lambda_n^{prime}
  =
  \lim_{\varepsilon\downarrow0}
  \left[
  -n+\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
  \right].
]

No local unit by single prime, finite shell, Laguerre lobe, Fejer--Riesz
factorization, positive Gram form, or smoothing in `n` survives the known
no-go tests. Each of those moves either loses the sign before summation or
assumes the positivity that must be proved.

## A0: uniform tail theorem

Let

[
  E(y)=\psi(y)-y,\qquad
  R_{n,\varepsilon}(X)
  =
  \int_X^\infty E(y)f'_{n,\varepsilon}(y)\,dy.
]

The first noncircular theorem to prove is:

[
  \boxed{
  \sup_{0\le\varepsilon\le1}
  |R_{n,\varepsilon}(e^{T(n)})|
  \le {1\over4}\lambda_n^{arch}
  \qquad(n\ge8)
  }
  \tag{A0}
]

for an explicit function `T(n)>=8n` built only from an explicit
Vinogradov--Korobov prime number theorem and uniform Laguerre bounds.

One sufficient shape is to choose `T(n)` as the least `T` satisfying

[
  cT^{3/5}(\log T)^{-1/5}
  \ge
  4n\log(1+T)+
  \log {C n^2\over \lambda_n^{arch}},
]

with all constants declared. This statement is not force-RH: it uses only an
unconditional tail estimate and does not try to prove the core sign.

## A1: isolated force-RH core

After A0, the remaining signed core becomes the single force-RH target

[
  \boxed{
  -n+
  \int_1^{e^{T(n)}}E(y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{arch}
  \qquad(n\ge8).
  }
  \tag{A1}
]

A0 plus A1 gives

[
  \lambda_n^{prime}\ge-\lambda_n^{arch}\qquad(n\ge8),
]

and therefore closes the infinite range of Omega7. Thus A0 is the immediate
technical target, while A1 is the first precisely isolated place where new
mathematics of force-RH must enter.
