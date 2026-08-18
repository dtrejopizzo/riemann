# Tail phase and lobe duality gate

## Purpose

`249_TAIL_SIGN_LAGUERRE_ZERO_PARTITION_GATE.md` writes the nonpositive-tail
condition as a signed lobe inequality in the \(u\)-variable.  `254` writes
the same condition as a one-sided phase inequality over zeros.  This note
records the exact duality between those two descriptions.

It is a reduction, not a proof of A1.  Its role is to prevent treating the
lobe route and the zero-phase route as independent sources of positivity:
they are the same signed functional in two transforms.

## The tail functional

Let
\[
  K_{n,T}(u)=\mathbf 1_{u\ge T}e^{-u}L_{n-1}^{(2)}(u)
\]
and
\[
  I_n(T)=\int_T^\infty E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{1}
\]

The nonpositive-tail condition is
\[
\boxed{I_n(T_n)\ge0.}
\tag{2}
\]

Let the zeros of \(L_{n-1}^{(2)}\) beyond \(T\) partition the tail into
intervals \(J_{n,j}\), as in `249`, and write
\[
  \sigma_{n,j}=\operatorname{sgn}L_{n-1}^{(2)}(u)
  \qquad(u\in J_{n,j}).
\]

Then
\[
\boxed{
  I_n(T)=\sum_j\sigma_{n,j}\mathcal E_{n,j},
  \qquad
  \mathcal E_{n,j}=
  \int_{J_{n,j}}E(e^u)e^{-u}|L_{n-1}^{(2)}(u)|\,du.
}
\tag{3}
\]

Thus the lobe theorem is
\[
\boxed{
  \sum_j\sigma_{n,j}\mathcal E_{n,j}\ge0.
}
\tag{4}
\]

## Zero-side transform of each lobe

For each lobe \(J_{n,j}\), define the incomplete lobe transform
\[
\boxed{
  \Phi_{n,j}(\rho)
  =
  \int_{J_{n,j}}
  e^{(\rho-1)u}\,|L_{n-1}^{(2)}(u)|\,du.
}
\tag{5}
\]

Since
\[
  L_{n-1}^{(2)}(u)=\sigma_{n,j}|L_{n-1}^{(2)}(u)|
  \qquad(u\in J_{n,j}),
\]
the full incomplete Laguerre transform of `254` decomposes as
\[
\boxed{
  \Phi_{n,T}(\rho)
  =
  \sum_j\sigma_{n,j}\Phi_{n,j}(\rho).
}
\tag{6}
\]

Pairing the explicit formula for \(E(e^u)\) against each lobe gives
\[
\mathcal E_{n,j}
=
-2\Re\sum_{\Im\rho>0}{\Phi_{n,j}(\rho)\over\rho}
-\mathcal T_{n,j},
\tag{7}
\]
where \(\mathcal T_{n,j}\) is the corresponding trivial/archimedean lobe
contribution.  Summing with signs and using (6) gives exactly `254`:
\[
\boxed{
  I_n(T)
  =
  -2\Re\sum_{\Im\rho>0}{\Phi_{n,T}(\rho)\over\rho}
  -\mathcal T_{n,T}.
}
\tag{8}
\]

Thus the signed lobe inequality (4) and the zero-phase inequality
\[
\boxed{
  2\Re\sum_{\Im\rho>0}{\Phi_{n,T_n}(\rho)\over\rho}
  \le
  -\mathcal T_{n,T_n}
}
\tag{9}
\]
are identical obligations.

## No independent positivity from lobe absolute values

Suppose one proves only unsigned lobe bounds
\[
  |\mathcal E_{n,j}|\le B_{n,j}.
\tag{10}
\]

Then the signed sum in (4) is not determined.  The model choices
\[
  \mathcal E_{n,j}^{\pm}=\pm B_{n,j}
\]
produce the same absolute data but can change the sign of
\[
  \sum_j\sigma_{n,j}\mathcal E_{n,j}.
\]

Therefore a lobe proof must give oriented correlations between the signs of
the Chebyshev error and the Laguerre lobe signs.  Absolute lobe control is
only the failed absolute route in partitioned form.

## No independent positivity from zero magnitudes

Similarly, suppose on the zero side one proves only
\[
  \left|{\Phi_{n,j}(\rho)\over\rho}\right|
  \quad\hbox{or}\quad
  \left|{\Phi_{n,T}(\rho)\over\rho}\right|
\tag{11}
\]
bounds, possibly together with critical-line support.  These data do not
determine
\[
  \Re\sum_{\Im\rho>0}{\Phi_{n,T}(\rho)\over\rho}.
\]

The missing information is the same oriented phase information that appears
as the signed lobe correlation in (4).  This is the zero-side version of the
sign-flip obstruction in `250` and the support no-go in `258`.

## Exact remaining theorem

The nonpositive-tail route may be stated in either of the two equivalent
forms:
\[
\boxed{
  \sum_j\sigma_{n,j}\mathcal E_{n,j}\ge0
}
\tag{12}
\]
or
\[
\boxed{
  2\Re\sum_{\Im\rho>0}{\Phi_{n,T_n}(\rho)\over\rho}
  \le
  -\mathcal T_{n,T_n}.
}
\tag{13}
\]

For the full A0-improvement route, replace the right side of (13) by
\[
  -\mathcal T_{n,T_n}
  -\left(d_n-\frac14\right)A_n,
\]
or equivalently replace the lower bound \(0\) in (12) by
\[
  \left(d_n-\frac14\right)A_n.
\]

Thus any successful proof must provide a signed lobe-correlation theorem,
a zero-phase theorem, or an equivalent margin-tail bridge.  It cannot
combine an unsigned lobe estimate with an unsigned zero estimate and obtain
the one-sided tail sign.

## Status

Closed as the duality gate between Laguerre lobe balance and zero-phase
balance.  A1 remains open until one of these equivalent signed inequalities
is proved.
