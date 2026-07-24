# Tail-lobe one-sided envelope criterion

## Purpose

`280_TAIL_PHASE_LOBE_BALANCE_GATE.md` gives the exact signed lobe balance
needed for compact A1.  `250_NONPOSITIVE_TAIL_SYMMETRIC_ENVELOPE_NO_GO.md`
shows that symmetric bounds for \(\psi(x)-x\) cannot decide that balance.

This note records the corresponding positive criterion: a tail proof may
use local envelopes, but the envelopes must be one-sided with the correct
orientation on each Laguerre lobe.

## Tail notation

Put
\[
  E(e^u)=\psi(e^u)-e^u,
  \qquad
  K_{n}(u)=e^{-u}L_{n-1}^{(2)}(u),
\]
and
\[
  I_n(T_n)=\int_{T_n}^{\infty}E(e^u)K_n(u)\,du .
\]

The compact tail-margin target is
\[
\boxed{
  I_n(T_n)\ge \left(d_n-\frac14\right)A_n,
}
\tag{1}
\]
where \(A_n=\lambda_n^{\rm arch}\) and
\[
  d_n=\max\left(0,\frac12-\frac{\lambda_n}{A_n}\right).
\]
By `255`, (1) is exactly the pointwise compact A1 condition in
tail-margin coordinates.

Let the zeros of \(L_{n-1}^{(2)}\) split \([T_n,\infty)\) into lobes
\[
  J_{n,j}\qquad(0\le j\le N_n),
\]
and write
\[
  \sigma_{n,j}=\operatorname{sgn}K_n(u)\quad(u\in J_{n,j}).
\]
Then
\[
  I_n(T_n)=
  \sum_{j=0}^{N_n}
  \sigma_{n,j}
  \int_{J_{n,j}}E(e^u)|K_n(u)|\,du .
\tag{2}
\]

## One-sided lobe envelopes

Assume that on every positive lobe \(\sigma_{n,j}=+1\) one has a lower
envelope
\[
\boxed{
  E(e^u)\ge \ell_{n,j}(u)
  \qquad(u\in J_{n,j}),
}
\tag{3}
\]
and on every negative lobe \(\sigma_{n,j}=-1\) one has an upper envelope
\[
\boxed{
  E(e^u)\le u_{n,j}(u)
  \qquad(u\in J_{n,j}).
}
\tag{4}
\]

Define the certified oriented lobe lower bound
\[
\boxed{
  \mathcal L_n
  =
  \sum_{\sigma_{n,j}=+1}
    \int_{J_{n,j}}\ell_{n,j}(u)|K_n(u)|\,du
  -
  \sum_{\sigma_{n,j}=-1}
    \int_{J_{n,j}}u_{n,j}(u)|K_n(u)|\,du .
}
\tag{5}
\]

Then
\[
\boxed{
  I_n(T_n)\ge \mathcal L_n.
}
\tag{6}
\]

Indeed, (3) bounds the positive-lobe terms in (2) from below, while
(4) bounds the negative-lobe terms from below after multiplication by
\(-1\).

Consequently compact A1 follows at the index \(n\) if
\[
\boxed{
  \mathcal L_n\ge \left(d_n-\frac14\right)A_n.
}
\tag{7}
\]

Thus the full compact theorem follows if (3)--(4) and (7) hold for every
\(n\ge8\), or for every \(n\ge N_\infty\) together with the finite
certificate required by `261`.

## Constant-envelope corollary

If the lobe bounds are constant on each lobe,
\[
  E(e^u)\ge a_{n,j}\quad(\sigma_{n,j}=+1),
  \qquad
  E(e^u)\le b_{n,j}\quad(\sigma_{n,j}=-1),
\]
then (5) becomes
\[
\boxed{
  \mathcal L_n
  =
  \sum_{\sigma_{n,j}=+1}a_{n,j}W_{n,j}
  -
  \sum_{\sigma_{n,j}=-1}b_{n,j}W_{n,j},
  \qquad
  W_{n,j}=\int_{J_{n,j}}|K_n(u)|\,du .
}
\tag{8}
\]

This is the clean finite lobe budget associated with the signed tail
route.

## Why symmetric envelopes collapse to the failed absolute route

Suppose the only input is a symmetric bound
\[
  |E(e^u)|\le W(u).
\]
Then the one-sided data forced by that bound are
\[
  \ell_{n,j}(u)=-W(u),
  \qquad
  u_{n,j}(u)=W(u).
\]
Therefore (5) gives only
\[
\boxed{
  \mathcal L_n
  =
  -\int_{T_n}^{\infty}W(u)|K_n(u)|\,du .
}
\tag{9}
\]

This is exactly the absolute worst-case bound from `250`.  Hence a
symmetric PNT/VK envelope can certify A1 through this criterion only if the
old absolute route is already strong enough:
\[
  -\int_{T_n}^{\infty}W(u)|K_n(u)|\,du
  \ge
  \left(d_n-\frac14\right)A_n.
\]

The live obstruction is therefore not the use of envelopes as such.  It is
the absence of oriented one-sided envelopes matched to the signs of the
Laguerre lobes.

## Zero-side equivalent

Through the explicit formula and the duality of `274`, the same criterion
can be stated on the zero side.  The lower envelopes (3) and upper
envelopes (4) are equivalent to proving that the zero-phase contribution
on the positive Laguerre lobes is not too negative and on the negative
Laguerre lobes is not too positive.  In the notation of `280`, this is
precisely a method for proving
\[
  P_{n,T_n}^{-}-P_{n,T_n}^{+}
  \ge
  {1\over2}
  \left(
    \mathcal T_{n,T_n}
    +
    \left(d_n-\frac14\right)A_n
  \right).
\]

Thus the lobe-envelope criterion is not a separate route; it is an
actionable sufficient form of the signed lobe-balance theorem.

## Status

Closed as a sufficient pointwise tail criterion.  A1 remains open until
the required oriented one-sided lobe envelopes are proved for the actual
Chebyshev error, or until an equivalent Fejer/Herglotz/RDI theorem closes
the compact core.
