# Comparative innovation margin gate

## Purpose

`195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md` formulated the comparative form
\[
  \mathfrak Q^{\mathcal C,T_n}
  =
  \mathfrak Q^{\mathcal L}
  -{1\over4}\mathfrak Q^{\mathcal A}
  -\mathfrak Q^{\mathcal R,T_n}.
\tag{1}
\]

This note refines that gate into a Schur/innovation condition sufficient
for compact A1, and records the circularity that must be avoided.

The central point is:

\[
  \hbox{a Schur complement proves A1 only if the comparative block
  positivity is proved before the A1 diagonal is inserted.}
\]

Computing a Schur complement after choosing the diagonal so that it equals
the A1 scalar is only a repackaging of A1.

## Comparative finite matrix

Fix \(n\ge8\) and a finite-dimensional polynomial space
\[
  W_n\supset\{1-z^n\}.
\]

Let
\[
  p_n=1-z^n
\]
and set
\[
  M_n^{\mathcal C}
  =
  M_n^{\mathcal L}
  -
  {1\over4}M_n^{\mathcal A}
  -
  M_n^{\mathcal R,T_n},
\tag{2}
\]
the Gram matrix of \(\mathfrak Q^{\mathcal C,T_n}\) on \(W_n\).

Then
\[
  {1\over2}\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)=C_n(T_n).
\tag{3}
\]

Therefore A1 follows from the diagonal inequality
\[
  \mathfrak Q^{\mathcal C,T_n}(p_n,p_n)\ge0.
\tag{4}
\]

A non-diagonal Schur proof should prove something stronger and structural.

## Innovation relative to a comparison space

Choose a subspace
\[
  U_n\subset W_n
\]
and decompose
\[
  W_n=U_n\oplus\mathbb C p_n.
\tag{5}
\]

With respect to this decomposition, write
\[
  M_n^{\mathcal C}
  =
  \begin{pmatrix}
    B_n & b_n\\
    b_n^* & d_n
  \end{pmatrix},
\tag{6}
\]
where
\[
  d_n=\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)=2C_n(T_n).
\tag{7}
\]

The comparative innovation margin is the Schur complement
\[
  \boxed{
  \iota_n
  =
  d_n-b_n^*B_n^\dagger b_n,
  }
\tag{8}
\]
provided
\[
  B_n\succeq0
\tag{9}
\]
and \(b_n\) lies in the range of \(B_n\), with the Moore--Penrose inverse
used in the semidefinite case.

If
\[
  B_n\succeq0
  \qquad\hbox{and}\qquad
  \iota_n\ge0,
\tag{10}
\]
then
\[
  M_n^{\mathcal C}\succeq0
\]
on \(U_n\oplus\mathbb Cp_n\).  In particular,
\[
  d_n\ge b_n^*B_n^\dagger b_n\ge0,
\]
so
\[
  C_n(T_n)\ge0.
\tag{11}
\]

Thus (10) is a sufficient innovation theorem for A1.

## Equivalent minimization form

The same condition can be written without choosing coordinates.  Define the
prediction/innovation energy
\[
  \boxed{
  \iota_n
  =
  \inf_{u\in U_n}
  \mathfrak Q^{\mathcal C,T_n}(p_n-u,p_n-u).
  }
\tag{12}
\]

When \(B_n\succeq0\) and the range condition holds, (12) equals (8).  If
\[
  \iota_n\ge0
\tag{13}
\]
and the form is nonnegative on \(U_n\), then every vector in
\(U_n\oplus\mathbb Cp_n\) has nonnegative comparative energy.

In particular, taking \(u=0\) gives
\[
  \mathfrak Q^{\mathcal C,T_n}(p_n,p_n)\ge\iota_n\ge0,
\]
which implies A1.

This is the clean Schur--Friedrichs interpretation: \(p_n\) must have
nonnegative comparative innovation after projecting away all modes in
\(U_n\).

## What would be non-circular

A valid comparative innovation theorem must prove the following from
Euler--Gamma data before using A1:

1. a canonical choice of \(W_n\) and \(U_n\);
2. explicit construction of the three forms
   \(\mathfrak Q^{\mathcal L}\), \(\mathfrak Q^{\mathcal A}\), and
   \(\mathfrak Q^{\mathcal R,T_n}\);
3. nonnegativity of the comparative block:
   \[
     B_n\succeq0;
   \]
4. the range condition for \(b_n\);
5. the innovation margin:
   \[
     \iota_n\ge0.
   \]

Only after these five points are proved may one conclude
\[
  C_n(T_n)\ge0.
\]

The theorem is stronger than the diagonal A1 scalar unless \(U_n=\{0\}\).
Its value is that it could reveal a structural positivity mechanism rather
than a single coefficient inequality.

## Circular Schur complement to avoid

The following proof pattern is circular:

1. start from the scalar identity
   \[
     d_n=2C_n(T_n);
   \]
2. choose \(B_n\) and \(b_n\) after the fact;
3. define
   \[
     \iota_n=d_n-b_n^*B_n^\dagger b_n;
   \]
4. prove \(\iota_n\ge0\) using \(d_n\ge0\), or by arranging \(B_n,b_n\) so
   that the Schur complement equals a known restatement of \(C_n(T_n)\).

This does not prove A1.  It assumes the sign of the diagonal quantity whose
sign is the target.

The reason is elementary.  Since
\[
  b_n^*B_n^\dagger b_n\ge0
\]
when \(B_n\succeq0\), the Schur inequality
\[
  d_n-b_n^*B_n^\dagger b_n\ge0
\tag{14}
\]
is stronger than
\[
  d_n\ge0.
\]

Therefore one cannot obtain (14) from \(d_n\ge0\), and one cannot claim a
Schur proof by first identifying \(d_n\) with A1 and then treating the
remainder as automatically positive.

The order of proof matters:

\[
  B_n\succeq0\ \hbox{and}\ \iota_n\ge0
  \quad\Longrightarrow\quad
  d_n\ge0,
\]
not conversely.

## Minimal non-circular gate

The exact surviving innovation theorem is:

**Comparative innovation margin theorem.**  For every \(n\ge8\), construct a
finite comparison space \(U_n\subset W_n\) for the comparative form
\[
  \mathfrak Q^{\mathcal C,T_n}
  =
  \mathfrak Q^{\mathcal L}
  -{1\over4}\mathfrak Q^{\mathcal A}
  -\mathfrak Q^{\mathcal R,T_n},
\]
such that
\[
  \mathfrak Q^{\mathcal C,T_n}\big|_{U_n}\succeq0
\]
and
\[
  \inf_{u\in U_n}
  \mathfrak Q^{\mathcal C,T_n}(1-z^n-u,1-z^n-u)
  \ge0.
\tag{15}
\]

Then
\[
  C_n(T_n)\ge0
\]
for every \(n\ge8\), hence A1 follows.

This is the Schur/innovation version of the Loewner comparison gate in
`195`.  It is not supplied by global Toeplitz positivity, because it is a
positivity theorem for the comparative form after subtracting the
archimedean quarter and the moving tail.

## Status

Closed as a gate formulation.  A1 remains open.

The missing theorem is a non-circular comparative innovation margin:
comparative block positivity plus a nonnegative Schur complement must be
proved before the diagonal \(2C_n(T_n)\) is used.
