# Moving-diagonal recurrence defect

## Purpose

`156_A1_LAGUERRE_N_RECURRENCE_GATE.md` gives an exact three-term recurrence
for the fixed-cutoff compact quantities
\[
  C_n(T)
  =
  -n-\int_0^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  +{3\over4}\lambda_n^{\rm arch}.
\tag{1}
\]

A1, however, is not a fixed-cutoff statement.  It asks for
\[
  C_n(T_n)\ge0\qquad(n\ge8)
\tag{2}
\]
on the A0 diagonal \(T=T_n\).

This note records the exact recurrence on that moving diagonal.  The result
does not close A1, but it removes an ambiguity: the missing induction
theorem is not only positivity of the fixed-cutoff forcing \(F_n(T)\).  It
is positivity of \(F_n(T_n)\) plus two signed cutoff-transfer defects.

## Fixed-cutoff recurrence

For every fixed \(T\) and \(n\ge2\),
\[
  nC_{n+1}(T)
  =
  (2n+1)C_n(T)
  -(n+1)C_{n-1}(T)
  +F_n(T),
\tag{3}
\]
where
\[
  F_n(T)=
  M_n(T)+1+{3\over4}D_n^{\rm arch}
\tag{4}
\]
with \(M_n\) and \(D_n^{\rm arch}\) defined in `156` and `157`.

The cutoff-transfer identity from `153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md`
is
\[
  C_k(U)-C_k(S)
  =
  -\int_S^U E(e^u)e^{-u}L_{k-1}^{(2)}(u)\,du.
\tag{5}
\]

Write
\[
  \Phi_k(S,U)
  :=
  C_k(U)-C_k(S)
  =
  -\int_S^U E(e^u)e^{-u}L_{k-1}^{(2)}(u)\,du.
\tag{6}
\]

## Recurrence on the A0 diagonal

Put
\[
  C_k^\ast:=C_k(T_k).
\tag{7}
\]

Apply (3) at the common cutoff \(T=T_n\):
\[
  nC_{n+1}(T_n)
  =
  (2n+1)C_n(T_n)
  -(n+1)C_{n-1}(T_n)
  +F_n(T_n).
\tag{8}
\]

Now
\[
  C_{n+1}(T_n)
  =
  C_{n+1}^\ast-\Phi_{n+1}(T_n,T_{n+1}),
\tag{9}
\]
and
\[
  C_{n-1}(T_n)
  =
  C_{n-1}^\ast+\Phi_{n-1}(T_{n-1},T_n).
\tag{10}
\]

Substituting (9)--(10) into (8) gives the exact diagonal recurrence
\[
\boxed{
  nC_{n+1}^\ast
  =
  (2n+1)C_n^\ast
  -(n+1)C_{n-1}^\ast
  +F_n^{\rm diag},
}
\tag{11}
\]
where
\[
\boxed{
  F_n^{\rm diag}
  =
  F_n(T_n)
  +
  n\,\Phi_{n+1}(T_n,T_{n+1})
  -
  (n+1)\,\Phi_{n-1}(T_{n-1},T_n).
}
\tag{12}
\]

Equivalently, expanding the transfer terms,
\[
\boxed{
\begin{aligned}
  F_n^{\rm diag}
  &=
  M_n(T_n)+1+{3\over4}D_n^{\rm arch} \\
  &\quad
  -n\int_{T_n}^{T_{n+1}}
      E(e^u)e^{-u}L_n^{(2)}(u)\,du  \\
  &\quad
  +(n+1)\int_{T_{n-1}}^{T_n}
      E(e^u)e^{-u}L_{n-2}^{(2)}(u)\,du .
\end{aligned}
}
\tag{13}
\]

This is the exact forcing that controls induction along the actual A1
cutoff sequence.

## First-difference form

Let
\[
  \Delta_n^\ast=C_n^\ast-C_{n-1}^\ast.
\tag{14}
\]

From (11),
\[
\boxed{
  n\Delta_{n+1}^\ast
  =
  (n+1)\Delta_n^\ast+F_n^{\rm diag}.
}
\tag{15}
\]

Thus
\[
\boxed{
  {\Delta_{n+1}^\ast\over n+1}
  =
  {\Delta_n^\ast\over n}
  +
  {F_n^{\rm diag}\over n(n+1)}.
}
\tag{16}
\]

Consequently, for \(n\ge9\),
\[
\boxed{
  {\Delta_n^\ast\over n}
  =
  {\Delta_8^\ast\over8}
  +
  \sum_{k=8}^{n-1}
  {F_k^{\rm diag}\over k(k+1)}.
}
\tag{17}
\]

Therefore the diagonal induction theorem sufficient for A1 is:

1. \(C_8^\ast\ge0\);
2. for every \(n\ge9\),
   \[
     {\Delta_8^\ast\over8}
     +
     \sum_{k=8}^{n-1}
     {F_k^{\rm diag}\over k(k+1)}
     \ge0.
   \tag{18}
   \]

Then \(\Delta_n^\ast\ge0\) for \(n\ge9\), hence
\[
  C_n(T_n)=C_n^\ast\ge C_8^\ast\ge0
  \qquad(n\ge8).
\tag{19}
\]

## Why this matters

The fixed-cutoff forcing \(F_n(T)\) is already signed and difficult.  The
moving diagonal adds the explicit defect
\[
  n\,\Phi_{n+1}(T_n,T_{n+1})
  -
  (n+1)\,\Phi_{n-1}(T_{n-1},T_n).
\tag{20}
\]

Since
\[
  \Phi_k(S,U)
  =
  -\int_S^U E(e^u)e^{-u}L_{k-1}^{(2)}(u)\,du,
\]
the defect has the same prime-error/Laguerre sign problem as A1 itself.  It
is not controlled by monotonicity of \(T\), because `153` proves there is no
formal monotonicity in the cutoff.

Thus the corrected induction route is:

\[
  \hbox{base}
  +
  \hbox{cumulative lower bound for }F_n^{\rm diag}
  \Longrightarrow
  \hbox{A1}.
\tag{21}
\]

The fixed-cutoff theorem is a useful intermediate only if it is accompanied
by signed transfer bounds that control the two extra integrals in (13).

## Exact status

Closed as a moving-diagonal normal form.  A1 remains open.

The live local induction target is no longer ambiguous: prove the cumulative
lower bound (18) for the explicit diagonal forcing (13), with the chosen A0
cutoff sequence \(T_n\).
