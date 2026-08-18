# Critical-line support tail-phase no-go

## Purpose

The file `254_TAIL_SIGN_EXPLICIT_FORMULA_PHASE_GATE.md` rewrites the
nonpositive-tail route as a one-sided phase inequality over the zero side of
the explicit formula.  This note records the corresponding no-go:

\[
\boxed{
  \hbox{support of the zeros on the critical line is not, by itself, a
  compact A1 tail-phase theorem.}
}
\]

This is not a counterexample to zeta and it is not a replacement for RH.
It is a separation of proof data.  Critical-line support controls the
location of the spectral points.  Compact A1 needs an oriented weighted sum
with the incomplete Laguerre phase.

## Phase functional on critical-line data

Fix \(n\ge8\) and \(T\ge T_n\).  Write
\[
  W_{n,T}(\gamma)
  =
  {\Phi_{n,T}(1/2+i\gamma)\over 1/2+i\gamma},
\]
where
\[
  \Phi_{n,T}(\rho)
  =
  \int_T^\infty e^{(\rho-1)u}L_{n-1}^{(2)}(u)\,du
\]
is the incomplete Laguerre transform appearing in `254`.

For a positive symmetric model measure on the critical line,
\[
  \mu=\sum_j a_j(\delta_{\gamma_j}+\delta_{-\gamma_j}),
  \qquad a_j>0,\quad \gamma_j>0,
\]
define the phase functional
\[
  \mathcal P_{n,T}(\mu)
  =
  2\Re\int_{\gamma>0} W_{n,T}(\gamma)\,d\mu(\gamma).
\]

The actual zeta divisor would give one special arithmetic measure.  The
point here is weaker and logical: the assertion
\[
  \operatorname{supp}\mu\subset\mathbb R,\qquad \mu\ge0
\]
does not imply a numerical upper bound for \(\mathcal P_{n,T}(\mu)\).

## Exact obstruction

Let
\[
  q_{n,T}(\gamma)=\Re W_{n,T}(\gamma).
\]

If there is a point \(\gamma_0>0\) with
\[
  q_{n,T}(\gamma_0)>0,
\]
then the positive critical-line measures
\[
  \mu_A=A(\delta_{\gamma_0}+\delta_{-\gamma_0}),\qquad A>0,
\]
satisfy
\[
  \mathcal P_{n,T}(\mu_A)=2Aq_{n,T}(\gamma_0)\to+\infty.
\]
Therefore no upper bound of the form
\[
  \mathcal P_{n,T}(\mu)\le B
\]
can follow from critical-line support and positivity alone.

Consequently, a proof that uses only the fact that the divisor is supported
on \(\Re\rho=1/2\) cannot prove the compact tail phase inequality unless it
also proves one of the following additional facts:

1. a pointwise kernel sign theorem
   \[
     q_{n,T}(\gamma)\le0
     \qquad(\gamma>0),
   \]
   together with the required finite upper margin;
2. a one-sided weighted moment inequality for the actual arithmetic zero
   measure;
3. an independent structure theorem identifying the actual measure as lying
   in a smaller cone on which \(q_{n,T}\) has the needed oriented bound.

The first alternative is itself a new Laguerre phase theorem.  The second
and third alternatives are exactly the missing arithmetic input, not a
consequence of support.

## Relation with the compact tail theorem

By `254`, the nonpositive-tail condition is equivalent to
\[
  2\Re\sum_{\Im\rho>0}
  {\Phi_{n,T_n}(\rho)\over\rho}
  \le
  -\mathcal T_{n,T_n}.
\]

Under RH this becomes
\[
  \mathcal P_{n,T_n}(\mu_\zeta)
  \le
  -\mathcal T_{n,T_n},
\]
where \(\mu_\zeta\) is the positive counting measure of ordinates on the
critical line.  The statement is still an oriented inequality against the
specific oscillatory weight \(q_{n,T_n}\).  The support condition
\(\operatorname{supp}\mu_\zeta\subset\mathbb R\) supplies the domain of
integration, but not the sign or size of that integral.

Thus the compact A1 route
\[
  R_n(T_n)\le0
\]
is not obtained from RH-location alone inside the compact budget.  It
requires a tail-phase theorem for the actual zero measure or an equivalent
margin-tail bridge.

## Relation with the global half-plane route

The global route in `246` and `253` is different.  If one constructs a
positive Herglotz boundary measure for
\[
  H_\xi(z)=2{\xi'\over\xi}\!\left({1\over1-z}\right)
\]
before using zero support, then the resulting half-plane theorem closes
Omega7 externally through RH and Li.

That does not provide an internal proof of compact A1 unless it is coupled
to the pointwise margin-tail gate
\[
  s_n\ge d_n.
\]
The present no-go explains why: line support is a location theorem, while
compact A1 is a coefficientwise oriented phase theorem.

## Consequence

Any future proof that tries to pass from critical-line support to the
nonpositive-tail condition must explicitly add a theorem of the form
\[
\boxed{
  \int_{\gamma>0}
  \Re\!\left(
    {\Phi_{n,T_n}(1/2+i\gamma)\over1/2+i\gamma}
  \right)
  d\mu_\zeta(\gamma)
  \le
  -{1\over2}\mathcal T_{n,T_n}
  \qquad(n\ge8).
}
\]

Equivalently, it must prove the normalized margin-tail inequality
\[
  s_n\ge d_n.
\]

Without this oriented moment theorem, critical-line support, modulus
control, and symmetric zero counting remain insufficient for compact A1.
