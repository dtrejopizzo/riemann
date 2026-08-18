# Tail-sign explicit-formula phase gate

## Purpose

`250_NONPOSITIVE_TAIL_SYMMETRIC_ENVELOPE_NO_GO.md` shows that the
nonpositive-tail condition cannot follow from a two-sided envelope for
\(E(x)=\psi(x)-x\).  This note writes the next admissible target: the
signed tail as an explicit-formula phase inequality over the nontrivial
zeros.

It is a reduction, not a proof of A1.

## Tail functional

For \(T>0\), set
\[
  K_{n,T}(u)=\mathbf 1_{u\ge T}\,e^{-u}L_{n-1}^{(2)}(u)
\]
and
\[
\boxed{
  I_n(T)=
  \int_T^\infty E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du .
}
\tag{1}
\]

The nonpositive-tail gate of `247` is
\[
\boxed{I_n(T_n)\ge0.}
\tag{2}
\]

The full A0-improvement gate of `244` is
\[
\boxed{
  I_n(T_n)\ge \left(d_n-\frac14\right)A_n.
}
\tag{3}
\]

## Incomplete Laguerre transform

For \(\Re a<1\), define
\[
\boxed{
  \Phi_{n,T}(a)
  =
  \int_T^\infty
    e^{-(1-a)u}L_{n-1}^{(2)}(u)\,du .
}
\tag{4}
\]

Since
\[
  L_{n-1}^{(2)}(u)
  =
  \sum_{k=0}^{n-1}
    (-1)^k
    {1\over k!}
    \binom{n+1}{n-1-k}
    u^k,
\]
one has the finite closed form
\[
\boxed{
  \Phi_{n,T}(a)
  =
  \sum_{k=0}^{n-1}
    (-1)^k
    {1\over k!}
    \binom{n+1}{n-1-k}
    { \Gamma(k+1,(1-a)T)\over (1-a)^{k+1}} .
}
\tag{5}
\]

This is the exact transfer coefficient by which a zero \(\rho\) contributes
to the Laguerre tail.

## Explicit-formula expansion

Use the standard symmetric explicit formula for the Chebyshev function
\[
  \psi_0(x)
  =
  x-\sum_\rho {x^\rho\over\rho}
  -\log(2\pi)
  -{1\over2}\log(1-x^{-2}),
\]
where \(\psi_0\) is the midpoint convention at prime-power jumps.  The
choice of midpoint does not affect (1), because changing \(\psi\) on a
discrete set changes no Lebesgue integral.

For \(u>0\),
\[
  E(e^u)
  =
  -\sum_\rho {e^{\rho u}\over\rho}
  -\log(2\pi)
  -{1\over2}\log(1-e^{-2u})
\]
in the usual symmetric limiting sense.  Pairing this distributional
identity against the exponentially decaying polynomial kernel \(K_{n,T}\)
gives
\[
\boxed{
  I_n(T)
  =
  -\sum_\rho {\Phi_{n,T}(\rho)\over\rho}
  -\log(2\pi)\Phi_{n,T}(0)
  -{1\over2}
    \int_T^\infty
      \log(1-e^{-2u})e^{-u}L_{n-1}^{(2)}(u)\,du .
}
\tag{6}
\]

Equivalently, pairing conjugate zeros,
\[
\boxed{
  I_n(T)
  =
  -2\Re\sum_{\Im\rho>0}{\Phi_{n,T}(\rho)\over\rho}
  -\mathcal T_{n,T},
}
\tag{7}
\]
where the real archimedean/trivial tail is
\[
\boxed{
  \mathcal T_{n,T}
  =
  \log(2\pi)\Phi_{n,T}(0)
  +{1\over2}
    \int_T^\infty
      \log(1-e^{-2u})e^{-u}L_{n-1}^{(2)}(u)\,du .
}
\tag{8}
\]

The second integral is absolutely convergent, because
\(\log(1-e^{-2u})=O(e^{-2u})\) on every tail \(T>0\).

## Phase inequality for the nonpositive tail

The condition \(I_n(T_n)\ge0\) is exactly
\[
\boxed{
  2\Re\sum_{\Im\rho>0}{\Phi_{n,T_n}(\rho)\over\rho}
  \le
  -\mathcal T_{n,T_n}.
}
\tag{9}
\]

The full A0-improvement condition (3) is exactly
\[
\boxed{
  2\Re\sum_{\Im\rho>0}{\Phi_{n,T_n}(\rho)\over\rho}
  \le
  -\mathcal T_{n,T_n}
  -\left(d_n-\frac14\right)A_n .
}
\tag{10}
\]

Thus the missing signed tail theorem is a phase theorem for the zero sum
with weights \(\Phi_{n,T_n}(\rho)/\rho\).

## Why this is stronger than a zero-location or modulus estimate

A modulus estimate gives at most
\[
  \left|
    2\Re\sum_{\Im\rho>0}{\Phi_{n,T_n}(\rho)\over\rho}
  \right|
  \le
  2\sum_{\Im\rho>0}
    \left|{\Phi_{n,T_n}(\rho)\over\rho}\right|,
\]
which is symmetric under changing phases.  It cannot imply the one-sided
upper bound (9) unless the right side is already large enough to absorb the
entire absolute sum, which is exactly the failed absolute route.

Even assuming RH only changes the decay profile to
\[
  \Phi_{n,T_n}\!\left({1\over2}+i\gamma\right);
\]
it does not by itself determine the sign of the real part in (9).
Therefore the compact tail theorem requires signed phase information about
the zeros, not merely their location in the critical strip or on the
critical line.

## Consequence for A1

Combining `247` with (9), compact A1 follows from the two RH-strength
statements
\[
  \lambda_n\ge {1\over4}A_n
\]
and
\[
  2\Re\sum_{\Im\rho>0}{\Phi_{n,T_n}(\rho)\over\rho}
  \le
  -\mathcal T_{n,T_n}
\]
for all \(n\ge8\).

Combining `244` with (10), compact A1 follows directly if the stronger
phase inequality (10) holds for all \(n\ge8\).

## Status

Closed as the explicit-formula phase gate for the signed tail.

A1 remains open.  The nonpositive-tail route now has an exact zero-side
target: prove the one-sided phase inequality (9), or the stronger
deficit-compensating inequality (10), from a non-circular arithmetic or
spectral mechanism.
