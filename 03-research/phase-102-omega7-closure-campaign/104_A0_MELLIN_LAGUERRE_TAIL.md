# A0 - Mellin-Laguerre uniform tail

## Goal

Remove the tail of the Li integral without using RH and without losing the
pole-prime pairing.

For \(n\ge8\), prove a cutoff \(T_n\) such that
\[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T_n}}^\infty
  (\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{\rm arch}.
\]

## Effective theorem

Assume an explicit prime number theorem of the form
\[
  |\psi(e^t)-e^t|
  \le C_0 e^t\exp(-\eta(t)),
  \qquad t\ge t_0,
\]
where \(\eta(t)\to\infty\) and
\[
  \int_A^\infty (1+t)^m\exp(-\eta(t))\,dt<\infty
  \qquad(A>t_0,\ m\ge0).
\]
The Vinogradov--Korobov error has this property.

For \(t=\log y\),
\[
  f'_{n,\varepsilon}(e^t)e^t
  =
  e^{-(1+\varepsilon)t}
  \left[
    {d\over dt}L_{n-1}^{(1)}(t)
    -(1+\varepsilon)L_{n-1}^{(1)}(t)
  \right].
\]
Using
\[
  L_{n-1}^{(1)}(t)
  =
  \sum_{j=0}^{n-1}
  (-1)^j {n\choose j+1}{t^j\over j!},
\]
one has, for \(t\ge0\) and \(0\le\varepsilon\le1\),
\[
  \left|
    {d\over dt}L_{n-1}^{(1)}(t)
    -(1+\varepsilon)L_{n-1}^{(1)}(t)
  \right|
  \le
  B_n(1+t)^{n-1},
\]
with the explicit admissible constant
\[
  B_n
  =
  2\sum_{j=0}^{n-1}{n\choose j+1}{1\over j!}
  +
  \sum_{j=1}^{n-1}{n\choose j+1}{j\over j!}.
\]
Hence, for \(T\ge t_0\),
\[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^T}^\infty E(y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le
  C_0B_n
  \int_T^\infty(1+t)^{n-1}\exp(-\eta(t))\,dt.
\]

Since \(\lambda_n^{\rm arch}>0\) for \(n\ge8\), choose any \(T_n\ge t_0\)
for which
\[
  C_0B_n
  \int_{T_n}^\infty(1+t)^{n-1}\exp(-\eta(t))\,dt
  \le {1\over4}\lambda_n^{\rm arch}.
\]
Then A0 holds.

## What is closed

A0 is closed in the following precise form:

\[
  \forall n\ge8\ \exists T_n<\infty:
  \quad
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T_n}}^\infty E(y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{\rm arch}.
\]

This uses only unconditional PNT input and elementary Laguerre bounds.

## What is not closed

This theorem does not close \(\Omega_7\), because it says nothing about the
sign of the compact core
\[
  -n+\int_1^{e^{T_n}}E(y)f'_{n,0}(y)\,dy .
\]
It only proves that the infinite tail can be made harmless without invoking
zeros. The whole RH-strength load is now concentrated in A1.
