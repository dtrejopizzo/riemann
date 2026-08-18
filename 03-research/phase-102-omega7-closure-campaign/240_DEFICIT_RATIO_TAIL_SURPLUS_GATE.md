# Deficit-ratio tail-surplus gate

## Purpose

`239_MARGIN_TAIL_THRESHOLD_LADDER.md` gives the sharp condition
\[
  \kappa_n-\rho_n\ge {1\over4},
  \qquad
  \kappa_n={\lambda_n\over A_n},
  \qquad
  \rho_n={R_n(T_n)\over A_n}.
\]

This note packages the same condition into a normalized deficit ratio.
The goal is to make every future partial proof auditable by one number:
how much of the strong-margin deficit must the tail surplus cover?

## Deficit ratio

Let
\[
  A_n=\lambda_n^{\rm arch}>0.
\]
Define the strong-margin deficit ratio
\[
\boxed{
  d_n=
  \max\left(0,\ {1\over2}-{\lambda_n\over A_n}\right).
}
\tag{1}
\]

Equivalently,
\[
  d_n={(-M_n)_+\over A_n},
  \qquad
  M_n=\lambda_n-\frac12A_n.
\tag{2}
\]

Thus:

1. \(d_n=0\) is exactly strong margin;
2. \(d_n\le1/2\) follows from Li positivity;
3. \(d_n>1/2\) would violate Li positivity.

## Tail surplus ratio

From `238`, define
\[
  \delta_n={1\over4}A_n-R_n(T_n).
\]

Normalize
\[
\boxed{
  s_n={\delta_n\over A_n}
  =
  {1\over4}-{R_n(T_n)\over A_n}.
}
\tag{3}
\]

A0 gives
\[
\boxed{
  s_n\ge0.
}
\tag{4}
\]

## Exact A1 gate

Since
\[
  C_n(T_n)=M_n+\delta_n,
\]
A1 is equivalent to
\[
  \delta_n\ge -M_n.
\]

After normalization, this is
\[
\boxed{
  s_n\ge d_n.
}
\tag{5}
\]

This is the deficit-ratio tail-surplus gate.

## Calibration

The ladder of `239` becomes:

1. Strong margin:
   \[
     d_n=0,
   \]
   so A0's \(s_n\ge0\) is enough.
2. Li positivity only:
   \[
     d_n\le {1\over2},
   \]
   so one needs
   \[
     s_n\ge d_n
   \]
   and in the worst Li-positive case \(s_n\ge1/2\), i.e.
   \(R_n(T_n)\le-A_n/4\).
3. Partial margin:
   if \(\lambda_n\ge\theta A_n\), then
   \[
     d_n\le {1\over2}-\theta,
   \]
   so the tail surplus must satisfy
   \[
     s_n\ge {1\over2}-\theta.
   \]

## Why this helps audit future attempts

Any proposed proof must deliver at least one of:

1. a bound \(d_n=0\) or \(d_n\le d_n^\ast\);
2. a signed tail surplus \(s_n\ge s_n^\ast\);
3. a direct proof \(s_n-d_n\ge0\).

If the proof only supplies symmetric A0 information, then it supplies only
\[
  s_n\ge0,
\]
which closes A1 only when \(d_n=0\).  If it supplies only Li positivity,
then it supplies only \(d_n\le1/2\), which closes nothing unless a
positive lower bound for \(s_n\) is also proved.

## Status

Closed as a normalized deficit/surplus gate.

A1 remains open.  The missing theorem is \(s_n\ge d_n\) for every
\(n\ge8\), or a sufficient pair of independent margin and tail estimates.
