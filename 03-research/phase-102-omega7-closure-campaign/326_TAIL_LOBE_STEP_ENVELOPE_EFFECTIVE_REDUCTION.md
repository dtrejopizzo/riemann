# Tail-lobe step-envelope effective reduction

## Purpose

`320_TAIL_LOBE_ONE_SIDED_ENVELOPE_CRITERION.md` states the oriented
tail-lobe theorem, and `322_TAIL_LOBE_INTERVAL_CERTIFICATE_SCHEMA.md`
states the interval data needed to certify it.

This note strengthens the effective part of that route.  On every bounded
tail lobe, the required constant one-sided envelope for
\[
  E(e^u)=\psi(e^u)-e^u
\]
is exactly reducible to finitely many prime-power endpoints.  Therefore the
bounded-lobe part of a `322` certificate is a finite arithmetic
computation.  The only genuinely infinite lobe for a fixed \(n\) is the
final ray after the largest remaining zero of \(L_{n-1}^{(2)}\), and that
ray still needs a separate analytic one-sided weighted theorem.

## Step structure of the Chebyshev error

Write
\[
  \mathcal E(u)=E(e^u)=\psi(e^u)-e^u.
\]
Between two consecutive prime-power logarithms, \(\psi(e^u)\) is constant,
so
\[
  {d\over du}\mathcal E(u)=-e^u<0.
\]
At a prime-power point \(u=\log m\), \(m=p^k\), the function has the upward
jump
\[
  \mathcal E(\log m)-\mathcal E(\log m-)=\Lambda(m)>0.
\]
Thus \(\mathcal E\) is strictly decreasing between jumps and jumps upward
by a positive amount at each prime power.

## Exact finite extrema on bounded intervals

Let \(J=[a,b]\) with \(a<b<\infty\).  Let
\[
  \mathcal P(J)=\{m=p^k:\ a<\log m\le b\}.
\]
Then the lower and upper one-sided constants on \(J\) are determined by the
finite sets
\[
\boxed{
  \inf_{u\in J}\mathcal E(u)
  =
  \min\left(
    \mathcal E(b),
    \{\mathcal E(\log m-):m\in\mathcal P(J)\}
  \right),
}
\tag{1}
\]
and
\[
\boxed{
  \sup_{u\in J}\mathcal E(u)
  =
  \max\left(
    \mathcal E(a),
    \{\mathcal E(\log m):m\in\mathcal P(J)\}
  \right).
}
\tag{2}
\]

Here \(\mathcal E(\log m-)\) denotes the left limit before the jump.  Formula
(1) is sufficient for a rigorous lower envelope because
\(\mathcal E(u)\ge\inf_J\mathcal E\) for all \(u\in J\), even when the
infimum is attained only as a left limit.  Formula (2) uses the value after
the jump, matching the usual convention
\(\psi(x)=\sum_{r\le x}\Lambda(r)\).

The proof is immediate from monotonicity on every open gap between
successive prime-power logarithms: a minimum on a gap occurs at its right
end, just before the next jump or at \(b\), while a maximum occurs at its
left end, just after the previous jump or at \(a\).

## Insertion into the tail-lobe certificate

For a bounded lobe \(J_{n,j}=[\xi_{n,j},\xi_{n,j+1}]\), define
\[
  m_{n,j}^{-}=\inf_{u\in J_{n,j}}\mathcal E(u),
  \qquad
  m_{n,j}^{+}=\sup_{u\in J_{n,j}}\mathcal E(u),
\]
using (1)--(2), with outward-rounded endpoint and prime-power arithmetic.

Then the constant-envelope part of `322` may be filled by the exact choices
\[
  L_{n,j}^-=m_{n,j}^{-}
  \qquad(\sigma_{n,j}=+1),
\]
and
\[
  U_{n,j}^+=m_{n,j}^{+}
  \qquad(\sigma_{n,j}=-1).
\]
Consequently every bounded tail lobe contributes a finite, checkable
quantity to the certified lower bound
\[
  \mathcal L_n^-.
\]

This does not use a symmetric PNT envelope.  It uses the actual arithmetic
step structure of \(\psi\) and preserves the one-sided orientation demanded
by `320`.

## Remaining final-ray gate

For a fixed \(n\), the tail partition has only finitely many bounded lobes
and one final ray
\[
  J_{n,\infty}=[\xi_{n,J_n},\infty).
\]
The finite reduction above gives no finite enumeration for that ray.  The
tail-lobe route must therefore provide one of the following additional
inputs:

1. a direct weighted one-sided ray bound,
   \[
     \sigma_{n,\infty}
     \int_{J_{n,\infty}}\mathcal E(u)|K_n(u)|\,du
     \ge B_{n,\infty};
   \]
2. a function envelope on the ray with the correct orientation and enough
   weighted margin;
3. an effective threshold theorem proving the required final-ray and
   bounded-lobe inequalities uniformly for every \(n\ge N_\infty\), plus
   complete finite certificates for \(8\le n<N_\infty\).

Finite prime-power enumeration on bounded lobes cannot replace this
final-ray theorem.  It only converts the finite part of `322` into an
explicit arithmetic computation.

## Consequence for A1

The strengthened effective tail route is now:

1. isolate the zeros of \(L_{n-1}^{(2)}\) beyond \(T_n\);
2. compute every bounded-lobe envelope by the step-extrema formulas
   (1)--(2);
3. certify the final ray by a genuinely one-sided weighted theorem;
4. compare the resulting \(\mathcal L_n^-\) with
   \[
     \left(d_n-\frac14\right)A_n.
   \]

If these four steps hold for every \(n\ge8\), or above an effective
threshold with the finite remainder checked, then `320` proves compact A1.
Without the final-ray theorem and the all-index coverage rule, this remains
an effective schema rather than a proof of A1.

## Status

Closed as the bounded-lobe finite reduction and final-ray gate for the
oriented tail route.  A1 remains open until the final-ray theorem and the
all-index comparison are supplied.
