# Loewner negative-part compensation reduction

## Purpose

`195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md` writes compact A1 as a
comparative quadratic-form inequality:
\[
  \mathfrak Q^{\mathcal L}
  -
  {1\over4}\mathfrak Q^{\mathcal A}
  -
  \mathfrak Q^{\mathcal R,T_n}
  \ge0
\]
on the test vector \(p_n=1-z^n\), or on a stronger finite subspace.

`241_TAIL_SURPLUS_GENERATOR_DIAGONAL_NO_GO.md` rewrites the same scalar
condition as
\[
  \mathcal M+\Delta_{T_n}=\mathcal C_{T_n},
  \qquad
  \mathcal M=\mathcal L-\frac12\mathcal A,
  \qquad
  \Delta_T=\frac14\mathcal A-\mathcal R_T.
\]

This note gives the exact Loewner version of that split.  It isolates the
only way a quadratic-form route can beat the strong-margin gate: the tail
surplus form must dominate the negative part of the strong-margin form.

## Form split

Define
\[
\boxed{
  \mathfrak Q^{\mathcal M}
  =
  \mathfrak Q^{\mathcal L}
  -
  {1\over2}\mathfrak Q^{\mathcal A}
}
\tag{1}
\]
and
\[
\boxed{
  \mathfrak Q^{\Delta,T}
  =
  {1\over4}\mathfrak Q^{\mathcal A}
  -
  \mathfrak Q^{\mathcal R,T}.
}
\tag{2}
\]

Then
\[
\boxed{
  \mathfrak Q^{\mathcal C,T}
  =
  \mathfrak Q^{\mathcal M}
  +
  \mathfrak Q^{\Delta,T}.
}
\tag{3}
\]

On the Li test vector \(p_n=1-z^n\),
\[
\boxed{
  {1\over2}\mathfrak Q^{\mathcal M}(p_n,p_n)
  =
  M_n
  =
  \lambda_n-\frac12A_n,
}
\tag{4}
\]
and
\[
\boxed{
  {1\over2}\mathfrak Q^{\Delta,T_n}(p_n,p_n)
  =
  \delta_n
  =
  \frac14A_n-R_n(T_n).
}
\tag{5}
\]

Thus
\[
\boxed{
  {1\over2}\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)
  =
  M_n+\delta_n
  =
  C_n(T_n).
}
\tag{6}
\]

## Minimal diagonal compensation theorem

Compact A1 is exactly
\[
\boxed{
  \mathfrak Q^{\Delta,T_n}(p_n,p_n)
  \ge
  -\mathfrak Q^{\mathcal M}(p_n,p_n)
  \qquad(n\ge8).
}
\tag{7}
\]

This is the quadratic-form version of
\[
  \delta_n\ge -M_n.
\]

A0 gives only
\[
  \mathfrak Q^{\Delta,T_n}(p_n,p_n)\ge0.
\tag{8}
\]

Therefore A0 closes A1 precisely on those indices for which
\[
  \mathfrak Q^{\mathcal M}(p_n,p_n)\ge0,
\]
which is the strong-margin gate.

## Stronger finite-subspace theorem

Let \(V_n\) be any finite-dimensional subspace containing \(p_n\).  On
\(V_n\), write the Hermitian form \(\mathfrak Q^{\mathcal M}\) as
\[
  \mathfrak Q^{\mathcal M}
  =
  \mathfrak Q^{\mathcal M}_+
  -
  \mathfrak Q^{\mathcal M}_-
\]
by spectral decomposition, where both parts are nonnegative on \(V_n\).

Then a sufficient Loewner theorem for compact A1 is
\[
\boxed{
  \mathfrak Q^{\Delta,T_n}
  -
  \mathfrak Q^{\mathcal M}_-
  \succeq0
  \quad\hbox{on }V_n.
}
\tag{9}
\]

Indeed, (9) implies
\[
  \mathfrak Q^{\mathcal M}+\mathfrak Q^{\Delta,T_n}
  =
  \mathfrak Q^{\mathcal M}_+
  +
  \left(\mathfrak Q^{\Delta,T_n}
        -\mathfrak Q^{\mathcal M}_-\right)
  \succeq0
\]
on \(V_n\), and hence gives (6) on \(p_n\).

Conversely, if the target is positivity on the whole subspace \(V_n\), then
the exact condition is
\[
\boxed{
  \mathfrak Q^{\Delta,T_n}
  \succeq
  -\mathfrak Q^{\mathcal M}
  \quad\hbox{after restriction to every direction where the sum is tested.}
}
\tag{10}
\]

For the single A1 vector \(p_n\), this reduces exactly to (7).

## No-go for separated positivity

The following implication is false as a matter of Loewner algebra:
\[
  \mathfrak Q^{\mathcal L}\succeq0,\qquad
  \mathfrak Q^{\Delta,T_n}\succeq0
  \quad\Longrightarrow\quad
  \mathfrak Q^{\mathcal M}+\mathfrak Q^{\Delta,T_n}\succeq0.
\tag{11}
\]

The reason is that
\[
  \mathfrak Q^{\mathcal M}
  =
  \mathfrak Q^{\mathcal L}
  -
  {1\over2}\mathfrak Q^{\mathcal A}
\]
can have a negative part even when \(\mathfrak Q^{\mathcal L}\) is
nonnegative.  Positivity of the surplus form only says it lies above zero;
compact A1 needs it to lie above the negative part of
\(\mathfrak Q^{\mathcal M}\) in the tested direction.

On \(p_n\), the false implication becomes
\[
  \lambda_n\ge0,\qquad \delta_n\ge0
  \quad\not\Longrightarrow\quad
  M_n+\delta_n\ge0.
\]

This is the same obstruction as `238`--`241`, now in the exact
Loewner-order language.

## Status

Closed as the negative-part compensation reduction.

A1 remains open.  The surviving comparative route must prove either the
diagonal bound (7), the subspace domination (9), or an equivalent direct
positivity statement for \(\mathfrak Q^{\mathcal C,T_n}\).
