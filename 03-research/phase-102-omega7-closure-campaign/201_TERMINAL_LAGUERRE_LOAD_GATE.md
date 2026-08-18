# Terminal Laguerre load gate

## Purpose

`197_CUMULATIVE_KERNEL_INTERVAL_FORM.md` proves that on the terminal
interval
\[
  (T_{n-1},T_n)
\]
the cumulative diagonal kernel is exactly
\[
  \mathcal H_n(u)=-L_{n-1}^{(2)}(u).
\tag{1}
\]

This note isolates the resulting necessary condition for every absolute
diagonal proof.  It is a terminal obstruction/gate: if the base budget
\(\mathcal B_n\) cannot dominate this last Laguerre load, then the absolute
route of `191` fails before the earlier mixed intervals are considered.

## Terminal load

For a relative PNT envelope
\[
  |E(e^u)|\le e^u\varepsilon(u),
\]
define
\[
\boxed{
  \mathcal T_n(\varepsilon)
  =
  \int_{T_{n-1}}^{T_n}
  \varepsilon(u)|L_{n-1}^{(2)}(u)|\,du.
}
\tag{2}
\]

Since
\[
  W_n(\varepsilon)
  =
  \int_0^{T_n}\varepsilon(u)|\mathcal H_n(u)|\,du,
\]
(1) gives
\[
\boxed{
  W_n(\varepsilon)\ge \mathcal T_n(\varepsilon).
}
\tag{3}
\]

Therefore the absolute diagonal theorem
\[
  \mathcal B_n\ge W_n(\varepsilon)
\]
implies the necessary terminal condition
\[
\boxed{
  \mathcal B_n\ge \mathcal T_n(\varepsilon)
  \qquad(n\ge9).
}
\tag{4}
\]

## Sign-partition formula

Let the positive zeros of \(L_{n-1}^{(2)}\) be
\[
  0<\alpha_{n,1}<\cdots<\alpha_{n,n-1}.
\]

Refine the interval \([T_{n-1},T_n]\) by the zeros lying inside it:
\[
  T_{n-1}=b_0<b_1<\cdots<b_q=T_n,
\tag{5}
\]
where
\[
  \{b_1,\ldots,b_{q-1}\}
  =
  \{\alpha_{n,r}:T_{n-1}<\alpha_{n,r}<T_n\}.
\]

On each open interval \((b_\ell,b_{\ell+1})\), the sign is constant.  Let
\[
  \sigma_\ell
  =
  \mathrm{sgn}\,L_{n-1}^{(2)}(u)
  \qquad(b_\ell<u<b_{\ell+1}).
\tag{6}
\]

Then
\[
\boxed{
  \mathcal T_n(\varepsilon)
  =
  \sum_{\ell=0}^{q-1}
  \sigma_\ell
  \int_{b_\ell}^{b_{\ell+1}}
  \varepsilon(u)L_{n-1}^{(2)}(u)\,du.
}
\tag{7}
\]

This is the terminal component of the sign-partition certificate in `193`,
now written with the classical Laguerre zeros.

## Constant relative envelope

If
\[
  \varepsilon(u)=C,
\]
then the terminal load is elementary.  Since
\[
  {d\over du}L_n^{(1)}(u)=-L_{n-1}^{(2)}(u),
\tag{8}
\]
one has
\[
\boxed{
  \mathcal T_n(C)
  =
  C\sum_{\ell=0}^{q-1}
  \sigma_\ell
  \left[
    L_n^{(1)}(b_\ell)-L_n^{(1)}(b_{\ell+1})
  \right].
}
\tag{9}
\]

Consequently, constant-relative envelopes can pass the terminal gate only if
\[
\boxed{
  \mathcal B_n
  \ge
  C\sum_{\ell=0}^{q-1}
  \sigma_\ell
  \left[
    L_n^{(1)}(b_\ell)-L_n^{(1)}(b_{\ell+1})
  \right].
}
\tag{10}
\]

This is a finite endpoint certificate for the terminal interval.

## Monotone relative envelopes

Suppose \(\varepsilon\) is nonincreasing on \([T_{n-1},T_n]\).  On every
sign subinterval,
\[
  \varepsilon(b_{\ell+1})
  \int_{b_\ell}^{b_{\ell+1}}|L_{n-1}^{(2)}(u)|\,du
  \le
  \int_{b_\ell}^{b_{\ell+1}}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du
\]
and
\[
  \int_{b_\ell}^{b_{\ell+1}}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du
  \le
  \varepsilon(b_\ell)
  \int_{b_\ell}^{b_{\ell+1}}|L_{n-1}^{(2)}(u)|\,du.
\]

Thus
\[
\boxed{
\begin{aligned}
  \sum_{\ell=0}^{q-1}
  \varepsilon(b_{\ell+1})M_{n,\ell}
  \le
  \mathcal T_n(\varepsilon)
  \le
  \sum_{\ell=0}^{q-1}
  \varepsilon(b_\ell)M_{n,\ell},
\end{aligned}
}
\tag{11}
\]
where
\[
  M_{n,\ell}
  =
  \sigma_\ell
  \left[
    L_n^{(1)}(b_\ell)-L_n^{(1)}(b_{\ell+1})
  \right]
  =
  \int_{b_\ell}^{b_{\ell+1}}|L_{n-1}^{(2)}(u)|\,du.
\tag{12}
\]

For Vinogradov--Korobov or log-power relative envelopes, (11) gives an
explicit terminal lower bound without integrating the weight exactly.

## Local obstruction form

For any measurable subinterval
\[
  J\subset(T_{n-1},T_n),
\]
define
\[
  \varepsilon_J=\mathop{\mathrm{ess\,inf}}_{u\in J}\varepsilon(u).
\]

Then
\[
  \mathcal T_n(\varepsilon)
  \ge
  \varepsilon_J\int_J|L_{n-1}^{(2)}(u)|\,du.
\tag{13}
\]

Therefore the absolute route fails at index \(n\) if there exists
\[
  J\subset(T_{n-1},T_n)
\]
such that
\[
\boxed{
  \varepsilon_J\int_J|L_{n-1}^{(2)}(u)|\,du
  >
  \mathcal B_n.
}
\tag{14}
\]

This is the terminal version of the scale obstruction in `191`.

## What remains beyond the terminal gate

Passing (4) is necessary, not sufficient.  The full weighted \(L^1\) load is
\[
  W_n(\varepsilon)
  =
  \mathcal T_n(\varepsilon)
  +
  \hbox{earlier mixed-interval loads}.
\]

The earlier loads involve cumulative mixtures of Laguerre polynomials, as
shown in `197`.  They must still be controlled after the terminal gate is
passed.

Thus the absolute route now has a two-stage necessary checklist:

1. prove the terminal inequalities (4), or the sharper endpoint forms
   (10)--(11);
2. prove the remaining mixed-interval \(L^1\) domination.

## Status

Closed as a terminal necessary gate for the absolute diagonal route.

A1 remains open.  Any proposed absolute proof must first pass the terminal
Laguerre load condition (4), with the exact sign-partition formula (7).
