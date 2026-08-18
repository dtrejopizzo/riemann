# Poisson lower bounds do not imply log-kernel domination

## Purpose

`325_EG_REMAINDER_BAD_SET_CERTIFICATE_SCHEMA.md` uses the decomposition
\[
  d\nu_g=aL\,dm+d\rho,\qquad \rho\ge0,
\]
with
\[
  L(e^{i\theta})=-\log|2\sin(\theta/2)|.
\]
This is a measure-order statement: the positive measure \(\nu_g\) must
dominate the signed absolutely continuous component \(aL\,dm\).

This note records a logical separation.  A logarithmic Abel or Poisson lower
bound at the boundary point \(1\) does not imply this domination.  The
decomposition must be proved as its own theorem or replaced by a direct
defect estimate.

## Model counterexample

Let \(\nu=\delta_1\) be the unit point mass at \(1\in\partial\mathbb D\).
With the usual Poisson kernel
\[
  P_r(e^{i\theta})
  =
  {1-r^2\over |e^{i\theta}-r|^2},
\]
we have
\[
  \int P_{1-1/n}\,d\nu
  =
  P_{1-1/n}(1)
  =
  {1+(1-1/n)\over 1-(1-1/n)}
  =
  2n-1.
\]
Thus, for every \(n\ge1\),
\[
\boxed{
  \int P_{1-1/n}\,d\nu\ge \log n.
}
\tag{1}
\]

So \(\nu\) satisfies a logarithmic Poisson lower bound much stronger than
the lower bound used in the Abel route.

However, \(\nu\) does not dominate \(aL\,dm\) for any \(a>0\).  Choose a
small open arc \(J\) with \(1\notin J\) and \(J\subset\{L>0\}\), for
example an arc centered at angle \(\pi/6\).  Then
\[
  \nu(J)=0,
  \qquad
  \int_J L\,dm>0.
\]
If \(\nu=aL\,dm+\rho\) with \(\rho\ge0\), then
\[
  0=\nu(J)
  =
  a\int_J L\,dm+\rho(J)
  \ge
  a\int_J L\,dm
  >
  0,
\]
a contradiction.

Therefore:
\[
\boxed{
  \int P_{1-1/n}\,d\nu\ge \log n-O(1)
  \quad\not\Longrightarrow\quad
  \nu\ge aL\,dm\ \text{for any }a>0.
}
\tag{2}
\]

## Consequence for the Abel--Fejer route

The inputs in `325` are genuinely separate:

1. a positive increment measure \(\nu_g\);
2. an Abel lower bound for its Poisson averages;
3. a log-kernel domination or decomposition
   \(d\nu_g=aL\,dm+d\rho\) with \(\rho\ge0\);
4. a defect or bad-set estimate for \(\rho\).

Input 2 does not imply input 3.  In particular, a large Poisson value at
the point \(1\) may come from concentration rather than from an
absolutely-continuous logarithmic floor.

Thus the Fejer route can still close A1, but only after a non-circular
domination theorem for the actual increment measure, or after replacing the
decomposition by a direct bound for
\[
  \int (P_{1-1/n}-\alpha F_n)_+\,d\nu_g.
\]

## Status

Closed as a no-go for deriving log-kernel domination from Abel lower bounds
alone.  The remaining Fejer obligation is either a measure-domination
theorem for \(\nu_g\) or a direct defect estimate for the full positive
measure.
