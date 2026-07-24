# Strip Poisson boundary no-go

## Purpose

`177_UNCONDITIONAL_SIGMA_GT_1_POSITIVITY.md` reduces the log-derivative
positivity route to the strip
\[
  {1\over2}<\Re s\le1.
\]

This note records the natural Poisson/Dirichlet attempt in that strip and
the exact obstruction:

the boundary data have the right signs, but the Poisson argument requires
holomorphy in the strip, which is precisely the missing zero-free theorem.

## The strip and the target

Let
\[
  q(s)={\xi'\over\xi}(s),
  \qquad
  u(s)=\Re q(s).
\]

The target is
\[
  u(s)\ge0
  \qquad
  {1\over2}<\Re s\le1.
\tag{1}
\]

If \(q\) is holomorphic in the open strip, then \(u\) is harmonic there and
one can try to recover it from boundary values by the Poisson kernel of the
strip.  The problem is that holomorphy of \(q\) in the strip is equivalent to
absence of zeros of \(\xi\) there.

## Left boundary

The functional equation is
\[
  \xi(s)=\xi(1-s).
\]

Differentiating gives
\[
  q(s)=-q(1-s).
\tag{2}
\]

On the critical line \(s=1/2+it\), away from zeros,
\[
  1-s=\overline{s}.
\]

Since \(\xi(\overline{s})=\overline{\xi(s)}\), one has
\[
  q(\overline{s})=\overline{q(s)}.
\tag{3}
\]

Combining (2) and (3),
\[
  q(s)=-\overline{q(s)}
  \qquad(\Re s=1/2,\ \xi(s)\ne0).
\]

Therefore
\[
  \boxed{
  \Re q(1/2+it)=0
  }
\tag{4}
\]
away from zeros on the critical line.

Thus the left boundary has the correct nonnegative sign, but only in the
principal sense and with singularities at critical-line zeros.

## Right boundary

On the line \(\Re s=1\), the paired Hadamard product gives
\[
  q(1+it)=\sum_\rho {1\over 1+it-\rho}.
\tag{5}
\]

Since every nontrivial zero satisfies \(0<\Re\rho<1\),
\[
  \Re {1\over 1+it-\rho}
  =
  {1-\Re\rho\over(1-\Re\rho)^2+(t-\Im\rho)^2}
  >0.
\tag{6}
\]

The paired limit preserves nonnegative real part, hence
\[
  \boxed{
  \Re q(1+it)\ge0.
  }
\tag{7}
\]

This is the boundary form of the unconditional region
\[
  \Re q(s)>0\qquad(\Re s>1).
\]

## What Poisson would prove if the strip were zero-free

Assume, for this paragraph only, that \(q\) is holomorphic in
\[
  1/2<\Re s<1.
\]

Then \(u=\Re q\) is harmonic in the strip.  With suitable symmetric
truncation in \(t\), the strip Poisson formula and the boundary signs
(4), (7) give
\[
  u(s)\ge0
  \qquad(1/2<\Re s<1).
\tag{8}
\]

Together with `177`, this proves
\[
  \Re q(s)\ge0\qquad(\Re s>1/2).
\]

By `175`, RH and Omega7 follow.

## The obstruction

The assumption that \(q\) is holomorphic in the strip is equivalent to:
\[
  \xi(s)\ne0
  \qquad(1/2<\Re s<1).
\tag{9}
\]

But (9) is already the right-half part of RH.  If a zero
\[
  \rho,\qquad 1/2<\Re\rho<1,
\]
exists, then
\[
  q(s)={m\over s-\rho}+h(s)
\tag{10}
\]
near \(\rho\).  The real part of the principal part takes both signs on
small circles around \(\rho\).  Thus no Poisson argument using only the two
vertical boundary signs can bypass the pole.

Equivalently, applying the Poisson formula on a punctured strip introduces
additional small-circle boundary terms around the poles.  Those terms have
no fixed sign and are exactly the missing zero-support content.

## Exact no-go statement

The following inference is circular:
\[
  \Re q=0\hbox{ on }\Re s=1/2
  \quad+\quad
  \Re q\ge0\hbox{ on }\Re s=1
  \quad\Longrightarrow\quad
  \Re q\ge0\hbox{ in the strip}.
\]

It becomes valid only after adding:
\[
  q\hbox{ is holomorphic in }1/2<\Re s<1,
\]
which is equivalent to the absence of off-line zeros in the right half of
the critical strip.

Therefore the strip-boundary method is not a proof of A1/Omega7 by itself.
It identifies the precise missing input: control or exclusion of interior
poles.

## Status

Closed as a boundary-method no-go.  A1 remains open.

The remaining half-plane route must prove either holomorphy in the strip
from Euler--Gamma data, or a positive principle that absorbs the pole
contributions without assuming their absence.
