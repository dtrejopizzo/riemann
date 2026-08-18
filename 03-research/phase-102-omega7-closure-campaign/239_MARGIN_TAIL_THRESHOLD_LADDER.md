# Margin--tail threshold ladder

## Purpose

`238_TAIL_MARGIN_COMPENSATION_FRONTIER.md` writes
\[
  C_n(T_n)=M_n+\delta_n,
  \qquad
  M_n=\lambda_n-\frac12A_n,
  \qquad
  \delta_n=\frac14A_n-R_n(T_n),
\]
where \(A_n=\lambda_n^{\rm arch}\).  This note records the quantitative
ladder between strong margin and one-sided tail improvement.

The result is a simple but useful calibration:

- A0 tail control requires strong margin.
- Li positivity alone would require a much stronger negative tail
  placement.
- Intermediate Li-margin lower bounds require corresponding one-sided tail
  surplus.

## Two-parameter sufficient theorem

Assume that for some constants \(\kappa_n,\rho_n\),
\[
\boxed{
  \lambda_n\ge \kappa_n A_n
}
\tag{1}
\]
and
\[
\boxed{
  R_n(T_n)\le \rho_n A_n.
}
\tag{2}
\]

Then
\[
\begin{aligned}
  C_n(T_n)
  &=
  \lambda_n-\frac14A_n-R_n(T_n)\\
  &\ge
  \left(\kappa_n-\frac14-\rho_n\right)A_n.
\end{aligned}
\tag{3}
\]

Therefore A1 follows from the threshold
\[
\boxed{
  \kappa_n-\rho_n\ge {1\over4}.
}
\tag{4}
\]

This is the margin--tail ladder.

## Known points on the ladder

### A0 tail bound

A0 gives
\[
  \rho_n={1\over4}.
\tag{5}
\]

Then (4) requires
\[
  \kappa_n\ge {1\over2}.
\tag{6}
\]

This is exactly the strong-margin gate
\[
  \lambda_n\ge {1\over2}A_n.
\]

### Li positivity alone

Ordinary Li positivity gives only
\[
  \kappa_n=0.
\tag{7}
\]

Then (4) requires
\[
  \rho_n\le -{1\over4},
\tag{8}
\]
namely
\[
\boxed{
  R_n(T_n)\le -{1\over4}A_n.
}
\tag{9}
\]

Thus Li positivity plus A0 is not enough.  If one insists on using only
Li positivity for the main coefficient, the tail must be placed on the
negative side by at least a quarter archimedean unit.

### Intermediate margin

If one can prove
\[
  \lambda_n\ge \theta A_n
  \qquad(0<\theta<1/2),
\tag{10}
\]
then the required tail theorem is
\[
\boxed{
  R_n(T_n)\le \left(\theta-{1\over4}\right)A_n.
}
\tag{11}
\]

For example:

1. \(\theta=1/4\) requires \(R_n(T_n)\le0\);
2. \(\theta=3/8\) requires \(R_n(T_n)\le A_n/8\);
3. \(\theta=1/2\) requires only the A0 bound \(R_n(T_n)\le A_n/4\).

## Exact nonconstant form

The constants above can be replaced by index-dependent quantities.  Define
\[
  \kappa_n={\lambda_n\over A_n},
  \qquad
  \rho_n={R_n(T_n)\over A_n}.
\tag{12}
\]

Then A1 is exactly
\[
\boxed{
  \kappa_n-\rho_n\ge {1\over4}.
}
\tag{13}
\]

Equivalently,
\[
\boxed{
  \rho_n\le \kappa_n-{1\over4}.
}
\tag{14}
\]

This is the sharp indexwise one-sided tail requirement.

## Consequence for the active routes

Any successful proof can be located on this ladder:

1. strong margin proves \(\kappa_n\ge1/2\) and uses A0;
2. one-sided tail proves a better \(\rho_n\) than A0;
3. a hybrid proof proves both a partial margin and a partial tail surplus;
4. a global/comparative proof proves (13) directly without splitting.

The ladder makes clear why no symmetric estimate closes A1: a symmetric
tail estimate controls \(|\rho_n|\), but A1 needs the signed upper bound
(14).

## Status

Closed as the quantitative margin--tail threshold ladder.

A1 remains open.  The missing theorem is an indexwise proof of
\(\kappa_n-\rho_n\ge1/4\), or one of the sufficient points on the ladder.
