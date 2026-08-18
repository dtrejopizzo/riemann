# Schur zero-coupling diagonal collapse

## Purpose

`199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` states the valid
Loewner--Schur route for compact A1.  This note isolates the degenerate
case in which the Li test vector \(p_n=1-z^n\) is orthogonal to the chosen
comparison block for the comparative form.

The conclusion is sharp: zero coupling removes the Schur penalty, but then
the Schur condition collapses exactly to the diagonal A1 scalar.  It is not
a new proof mechanism unless the diagonal sign is proved independently.

## Comparative block

Let
\[
  \mathfrak Q^{\mathcal C,T_n}
  =
  \mathfrak Q^{\mathcal L}
  -{1\over4}\mathfrak Q^{\mathcal A}
  -\mathfrak Q^{\mathcal R,T_n}
\]
with the normalizations of `195`.  Fix a finite space
\[
  W_n=U_n\oplus\mathbb C p_n,
  \qquad p_n=1-z^n.
\]

In this decomposition write the matrix of
\(\mathfrak Q^{\mathcal C,T_n}\) as
\[
  M_n^{\mathcal C}
  =
  \begin{pmatrix}
    B_n & b_n\\
    b_n^* & d_n
  \end{pmatrix},
\tag{1}
\]
where
\[
\boxed{
  d_n=\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)=2C_n(T_n).
}
\tag{2}
\]

Assume
\[
  B_n\succeq0.
\tag{3}
\]

## Schur condition

The nonnegative Schur-complement condition is
\[
\boxed{
  d_n-b_n^*B_n^\dagger b_n\ge0,
}
\tag{4}
\]
with the usual range condition \(b_n\in\operatorname{Ran}B_n\) in the
semidefinite case.

Since \(b_n^*B_n^\dagger b_n\ge0\), (4) is generally stronger than the A1
diagonal inequality
\[
  d_n\ge0.
\tag{5}
\]

## Zero-coupling collapse

Suppose the chosen comparison space satisfies the comparative orthogonality
\[
\boxed{
  b_n=0.
}
\tag{6}
\]

Equivalently,
\[
  \mathfrak Q^{\mathcal C,T_n}(u,p_n)=0
  \qquad(u\in U_n).
\tag{7}
\]

Then the Schur complement is
\[
  d_n-b_n^*B_n^\dagger b_n=d_n.
\tag{8}
\]

Therefore the Schur condition (4) becomes exactly
\[
\boxed{
  d_n\ge0
  \quad\Longleftrightarrow\quad
  C_n(T_n)\ge0.
}
\tag{9}
\]

Thus zero coupling does not create an innovation margin.  It merely
orthogonalizes the chosen block away from the A1 scalar.

## Equivalent minimization form

The innovation energy from `199` is
\[
  \iota_n=\inf_{u\in U_n}
  \mathfrak Q^{\mathcal C,T_n}(p_n-u,p_n-u).
\tag{10}
\]

Under (3) and (6),
\[
  \mathfrak Q^{\mathcal C,T_n}(p_n-u,p_n-u)
  =
  d_n+\mathfrak Q^{\mathcal C,T_n}(u,u)
  \ge d_n.
\tag{11}
\]

Taking \(u=0\) gives equality:
\[
\boxed{
  \iota_n=d_n=2C_n(T_n).
}
\tag{12}
\]

Hence a proof of \(\iota_n\ge0\) in the zero-coupling case is exactly a
proof of A1.

## Consequence for non-circular Schur routes

A Schur route can be genuinely stronger than the diagonal only if it proves
structural data before the A1 sign is known:

1. \(B_n\succeq0\);
2. \(b_n\in\operatorname{Ran}B_n\);
3. the positive Schur margin
   \[
     d_n-b_n^*B_n^\dagger b_n\ge0.
   \]

If \(b_n=0\), item 3 is exactly \(d_n\ge0\), i.e. compact A1.  Therefore
the zero-coupling strategy is non-circular only if the diagonal sign is
proved from an independent signed compact theorem, margin-tail comparison,
or global route.  It cannot be advertised as a separate Schur innovation.

## Status

Closed as the zero-coupling Schur-collapse audit.

A1 remains open.  A valid Loewner--Schur continuation must either prove a
strictly positive innovation with nonzero structural coupling, or prove the
diagonal compact inequality \(C_n(T_n)\ge0\) by another non-circular
method.
