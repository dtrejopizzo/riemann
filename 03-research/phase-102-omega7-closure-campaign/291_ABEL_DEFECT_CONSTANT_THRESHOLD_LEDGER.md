# Abel-defect constant threshold ledger

## Purpose

`266_ABEL_TO_FEJER_DEFECT_GATE.md` isolates the exact positive defect
\[
  D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+
\]
that prevents an Abel/Poisson lower bound from becoming a Fejer lower
bound.  This note records the constant-level threshold that is sufficient
to close the strong-margin route, with the effective large-\(n\) threshold
made explicit.

It is a conditional closure ledger, not a proof of A1.  The missing input
is still a non-circular positive increment measure \(\nu_g\) and an
anti-concentration theorem for \(D_{n,\alpha}\).

## General constant theorem

Let \(\nu\) be a positive finite measure on \(\partial\mathbb D\).  Put
\[
  P_n=P_{1-1/n},
  \qquad
  D_{n,\alpha}=(P_n-\alpha F_n)_+,
  \qquad \alpha>0.
\]

Assume that for all \(n\ge N_0\)
\[
\boxed{
  \int P_n\,d\nu\ge c_P\log n-B_P
}
\tag{1}
\]
and
\[
\boxed{
  \int D_{n,\alpha}\,d\nu\le d_\alpha\log n+B_D.
}
\tag{2}
\]

Since
\[
  P_n\le\alpha F_n+D_{n,\alpha},
\]
we get
\[
  \alpha\int F_n\,d\nu
  \ge
  \int P_n\,d\nu-\int D_{n,\alpha}\,d\nu.
\]
Thus
\[
\boxed{
  \int F_n\,d\nu
  \ge
  q_\alpha\log n-B_\alpha,
  \qquad
  q_\alpha={c_P-d_\alpha\over\alpha},
  \quad
  B_\alpha={B_P+B_D\over\alpha}.
}
\tag{3}
\]

Therefore the Fejer lower theorem of `259` follows whenever
\[
\boxed{
  q_\alpha>{1\over2}
}
\tag{4}
\]
or equivalently
\[
\boxed{
  d_\alpha<c_P-{\alpha\over2}.
}
\tag{5}
\]

## Euler--Gamma normalization

For the Euler--Gamma increment generator, once the positive increment
measure exists, the radial Carathéodory identity gives
\[
  \int P_n\,d\nu_g
  =
  \mathrm{Re}\,H_g(1-1/n)
  =
  \log n+O(1).
\]

Thus the natural leading Abel constant is
\[
\boxed{c_P=1.}
\tag{6}
\]

In that normalization, the exact defect condition is
\[
\boxed{
  d_\alpha<1-{\alpha\over2}.
}
\tag{7}
\]

Consequently:

- \(\alpha\ge2\) cannot give a strict Fejer margin from \(c_P=1\), because
  the right side of (7) is nonpositive and \(d_\alpha\ge0\);
- \(\alpha=1\) gives the simple condition \(d_1<1/2\), already noted in
  `266`;
- the full Abel-transfer problem is the tradeoff
  \[
    \hbox{make }\alpha F_n\hbox{ large enough to dominate }P_n
    \hbox{ except on a set whose defect coefficient is }<1-\alpha/2.
  \]

This is the constant form of anti-concentration against the moving Fejer
zeros.

## Effective threshold after the defect theorem

Assume now that \(\nu=\nu_g\) is the Euler--Gamma increment measure and
that (1)--(2) hold with \(q_\alpha>1/2\).  By `262`,
\[
  {A_n\over n}
  =
  {\lambda_n^{arch}\over n}
  \le
  {1\over2}\log n+3
  \qquad(n\ge2).
\tag{8}
\]

The strong margin follows from
\[
  \int F_n\,d\nu_g\ge {A_n\over n}.
\]

Using (3) and (8), this is guaranteed whenever
\[
  q_\alpha\log n-B_\alpha
  \ge
  {1\over2}\log n+3,
\]
that is whenever
\[
\boxed{
  \log n\ge {3+B_\alpha\over q_\alpha-1/2}.
}
\tag{9}
\]

Thus an explicit large-\(n\) threshold is
\[
\boxed{
  N_\infty(\alpha)
  =
  \max\left(
    N_0,\,
    2,\,
    \left\lceil
      \exp\left({3+B_\alpha\over q_\alpha-1/2}\right)
    \right\rceil
  \right).
}
\tag{10}
\]

For every \(n\ge N_\infty(\alpha)\), the strong margin
\[
  \lambda_n\ge {1\over2}A_n
\]
holds.  Then A0 implies compact A1 at those indices.  The remaining range
\[
  8\le n<N_\infty(\alpha)
\]
is exactly the finite interval certificate of `261`.

## Relation to the log-density route

The local log-density route of `263`--`264` gives a direct Fejer lower
bound
\[
  \int F_n\,d\nu_g
  \ge
  (1/2+\eta)\log n-B_F
\]
without passing through Abel.  The present route is an alternative:

1. prove the Abel lower bound (1), which is natural from the radial
   Euler--Gamma generator;
2. prove the defect upper bound (2), which excludes concentration of
   logarithmic Abel mass near the moving zeros of \(F_n\);
3. apply the threshold (10);
4. verify the finite remainder as in `261`.

The two routes meet at the same Fejer lower theorem.  Local density is one
way to prove the lower layers directly; Abel defect control is a way to
prove that radial mass is not hidden in Fejer-null layers.

## Sharp obstruction recorded by the model

The model in `281` shows why condition (7) is not automatic.  There exists
a positive finite measure with logarithmic Poisson spikes along a sequence
\(N_j\) but bounded matching Fejer integrals:
\[
  \int P_{N_j}\,d\nu\gg\log N_j,
  \qquad
  \int F_{N_j}\,d\nu=O(1).
\]

For such a model, the defect integral necessarily carries almost all of
the Abel logarithmic mass along that sequence.  In the constant notation
above, \(d_\alpha\) cannot satisfy (5) along those indices.  Hence the
defect theorem must use specific Euler--Gamma structure, not positivity or
radial size alone.

## Exact remaining input

The Abel-transfer route closes compact A1 if one proves, non-circularly,
all of the following:

1. a positive increment measure \(\nu_g\) with the Euler--Gamma increment
   moments;
2. effective constants \(N_0,B_P\) in
   \[
     \int P_{1-1/n}\,d\nu_g\ge\log n-B_P;
   \]
3. some \(0<\alpha<2\) and effective constants \(B_D,d_\alpha\) such that
   \[
     \int (P_{1-1/n}-\alpha F_n)_+\,d\nu_g
     \le d_\alpha\log n+B_D,
     \qquad
     d_\alpha<1-{\alpha\over2};
   \]
4. the finite certificate for \(8\le n<N_\infty(\alpha)\).

These four items are sufficient, and item 3 is the genuine new
anti-concentration theorem.

## Status

Closed as the constant-threshold ledger for the Abel-defect route.  A1
remains open until the positive increment measure and the defect
anti-concentration estimate are proved with constants satisfying
\(d_\alpha<1-\alpha/2\).
