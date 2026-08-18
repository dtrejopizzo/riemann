# Absolute diagonal budget scale audit

## Purpose

`188_DIAGONAL_CUMULATIVE_COERCIVITY_AUDIT.md` proves that a two-sided
envelope for
\[
  E(e^u)=\psi(e^u)-e^u
\]
gives only the absolute-value lower bound
\[
  \mathcal S_n
  \ge
  \mathcal B_n
  -
  \int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du.
\tag{1}
\]

This note audits the scale content of that sufficient route.  It derives
the exact conditions an envelope \(R\) must satisfy to let the
base-archimedean budget dominate the absolute diagonal pairing.

The conclusion is not a closure of A1.  The absolute route is viable only
after proving explicit weighted \(L^1\) bounds for the cumulative kernel
\(\mathcal H_n\).  Without those bounds, a PNT envelope is only a size
statement and does not supply the signed A1 mechanism.

## Absolute sufficient theorem

Recall from `188` that
\[
  \mathcal S_n
  =
  \mathcal B_n+
  \int_0^{T_n}E(e^u)e^{-u}\mathcal H_n(u)\,du.
\tag{2}
\]

Let \(R(u)\ge0\) be any envelope satisfying
\[
  |E(e^u)|\le R(u)
  \qquad(0\le u\le T_n).
\tag{3}
\]

Define the weighted absolute diagonal load
\[
\boxed{
  W_n(R)
  =
  \int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du.
}
\tag{4}
\]

Then the absolute route proves A1 by diagonal induction if
\[
\boxed{
  C_8^\ast\ge0
  \qquad\hbox{and}\qquad
  \mathcal B_n\ge W_n(R)
  \quad(n\ge9).
}
\tag{5}
\]

This is exactly sufficient by (1).  Conversely, within the information class
\(|E|\le R\), it is also sharp: `188` shows that the worst allowed sign
pattern gives the lower value \(-W_n(R)\).  Thus no proof using only (3) can
replace (5) by a weaker scale condition.

## Relative PNT envelopes

Most PNT-type estimates on the compact \(u\)-side have the form
\[
  |E(e^u)|\le e^u\varepsilon(u),
\tag{6}
\]
where \(\varepsilon(u)\ge0\) is a relative error profile.  In that case
\[
\boxed{
  W_n(R)=
  \int_0^{T_n}\varepsilon(u)|\mathcal H_n(u)|\,du.
}
\tag{7}
\]

Therefore the exact absolute sufficient condition is
\[
\boxed{
  \mathcal B_n
  \ge
  \|\mathcal H_n\|_{L^1(\varepsilon;[0,T_n])}
  :=
  \int_0^{T_n}\varepsilon(u)|\mathcal H_n(u)|\,du.
}
\tag{8}
\]

This is the scale theorem for every relative PNT envelope.

### Constant relative envelope

If
\[
  |E(e^u)|\le C e^u,
\tag{9}
\]
then
\[
\boxed{
  W_n=C\int_0^{T_n}|\mathcal H_n(u)|\,du.
}
\tag{10}
\]

Thus constant-relative Chebyshev control can close the absolute diagonal
route only if
\[
\boxed{
  C\|\mathcal H_n\|_{L^1(0,T_n)}
  \le \mathcal B_n
  \qquad(n\ge9).
}
\tag{11}
\]

This is a very strong kernel \(L^1\) requirement.  The current phase does
not contain such a bound, and positivity of the cumulative weights
\(w_{n,k}\) does not imply it.

### Log-power relative envelope

If for \(u\ge u_0\)
\[
  |E(e^u)|\le C e^u(1+u)^{-A},
\tag{12}
\]
with an arbitrary finite envelope inserted on \(0\le u<u_0\), then the
large-\(u\) part of the required condition is
\[
\boxed{
  C\int_{u_0}^{T_n}(1+u)^{-A}|\mathcal H_n(u)|\,du
  +
  W_{n,<u_0}
  \le \mathcal B_n.
}
\tag{13}
\]

Here
\[
  W_{n,<u_0}
  =
  \int_0^{u_0}R(u)e^{-u}|\mathcal H_n(u)|\,du
\tag{14}
\]
is a finite low-range load.  It cannot be ignored, because
\(\mathcal H_n\) is supported from \(0\), not only near the final cutoff.

### Vinogradov--Korobov type envelope

If
\[
  |E(e^u)|
  \le
  C e^u\exp(-a u^\theta)
  \qquad(u\ge u_0),
\tag{15}
\]
with \(a>0\), \(\theta>0\), then the absolute sufficient condition is
\[
\boxed{
  C\int_{u_0}^{T_n}e^{-a u^\theta}|\mathcal H_n(u)|\,du
  +
  W_{n,<u_0}
  \le \mathcal B_n.
}
\tag{16}
\]

This is the precise way a decaying PNT input can help the diagonal absolute
route.  It helps only through weighted \(L^1\)-smallness of
\(\mathcal H_n\) in the region where the decay is active.

## Necessary scale obstruction

The previous conditions can be read contrapositively.  For any measurable
set \(A_n\subset[0,T_n]\), define
\[
  r_n(A_n)=\mathop{\mathrm{ess\,inf}}_{u\in A_n}R(u)e^{-u}.
\tag{17}
\]

Then
\[
  W_n(R)
  \ge
  r_n(A_n)\int_{A_n}|\mathcal H_n(u)|\,du.
\tag{18}
\]

Therefore the absolute route fails for index \(n\) whenever
\[
\boxed{
  r_n(A_n)\int_{A_n}|\mathcal H_n(u)|\,du
  >
  \mathcal B_n.
}
\tag{19}
\]

This is a rigorous scale obstruction.  It becomes a theorem against a
particular natural envelope class once one proves a lower bound for
\(\int_{A_n}|\mathcal H_n|\) and an upper bound for \(\mathcal B_n\) that
make (19) hold infinitely often.

The current phase has not yet proved such lower bounds for the cumulative
Laguerre kernel.  Hence no unconditional scale-disproof of the absolute
route is recorded here.  The exact missing estimates are now explicit.

## Finite computable certificate

For a fixed \(n\), the absolute route is decidable from finite data once
\(T_n\), \(R\), and \(\mathcal H_n\) are fixed.  Define
\[
\boxed{
  \Theta_n(R)
  =
  W_n(R)-\mathcal B_n.
}
\tag{20}
\]

Then:

- if \(\Theta_n(R)\le0\), the envelope \(R\) proves the diagonal inequality
  \(\mathcal S_n\ge0\) at that index;
- if \(\Theta_n(R)>0\), the envelope \(R\) is insufficient at that index.

Uniform closure by this route requires
\[
\boxed{
  \sup_{n\ge9}\Theta_n(R)\le0.
}
\tag{21}
\]

This certificate contains no zero-side input and no RH assumption.  It is a
pure finite Laguerre-envelope computation for each \(n\), but a proof of
A1 requires the uniform inequality (21), not isolated checks.

## Relation to signed A1

The absolute route deliberately discards the sign of the pairing
\[
  \int E(e^u)e^{-u}\mathcal H_n(u)\,du.
\]

Thus even if (5) is eventually proved, it would be a strong sufficient
theorem rather than the intrinsic signed compensation theorem.  If (5)
fails for natural envelopes, the diagonal route must return to the signed
finite arithmetic target from `188`:
\[
  \mathcal B_n
  +
  \sum_{m\le e^{T_n}}\Lambda(m)
  \int_{\log m}^{T_n}e^{-u}\mathcal H_n(u)\,du
  -
  \int_0^{T_n}\mathcal H_n(u)\,du
  \ge0.
\tag{22}
\]

That is the one-sided arithmetic theorem that avoids the absolute
\(L^1\)-loss.

## Exact status

Closed as a scale audit for the absolute diagonal budget.  A1 remains open.

The absolute-envelope path now has a precise theorem to prove:
\[
  \mathcal B_n
  \ge
  \int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du
  \qquad(n\ge9),
\]
with \(R\) an explicit PNT envelope.  A scale no-go for any proposed class
of envelopes must prove the obstruction (19) uniformly.
