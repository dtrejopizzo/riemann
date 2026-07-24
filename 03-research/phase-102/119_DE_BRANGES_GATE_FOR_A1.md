# de Branges gate for A1

## Purpose

This document tests whether a de Branges or Hermite--Biehler construction can
close A1 without assuming the conclusion.

## Desired theorem

Let
\[
  \Xi(t)=\xi\left({1\over2}+it\right).
\]

A de Branges closure would construct an entire function \(E\) in the
Hermite--Biehler class such that
\[
  \Xi(t)=\frac{E(t)+E^*(t)}{2}
\]
on the real axis, with \(E\) built from Euler--Gamma data and not from the
zeros of \(\Xi\).

If \(E\) is Hermite--Biehler, then its real part has only real zeros under the
usual interlacing hypotheses. This would imply that the zeros of \(\Xi\) are
real and hence close Omega7.

## Equivalent positivity

The Hermite--Biehler condition is
\[
  |E(z)|>|E^*(z)|\qquad(\Im z>0).
\]

Equivalently, the phase of \(E\) is increasing on the real line and the
associated de Branges kernel
\[
  K_E(w,z)=
  {E(z)\overline{E(w)}-E^*(z)\overline{E^*(w)}
  \over 2\pi i(\overline w-z)}
\]
is positive.

This is a positive-kernel statement at the boundary. In the Omega7
coordinates it is another form of the missing positive boundary measure.

## Tautological construction eliminated

If one defines \(E\) by first factoring \(\xi\) over its zeros and then
assigning zero factors to the upper or lower half-plane, the
Hermite--Biehler property is equivalent to the zeros being real. That
construction does not prove A1.

The following class is eliminated:
\[
  \hbox{choose }E\hbox{ from the zero divisor, then invoke de Branges
  positivity}.
\]

It assumes the support property that must be proved.

## Non-tautological target

The de Branges route remains viable only in the following form:

Construct \(E\) explicitly from the Euler product, Gamma factor and functional
equation, and prove
\[
  |E(z)|>|E^*(z)|\qquad(\Im z>0)
\]
without using the zero divisor of \(\xi\).

This theorem would imply the positive boundary measure target, hence A1.

## Obstruction

No such canonical \(E\) is currently available in phase 102. The natural
candidate \(E=A-iB\), built from even and odd parts of \(\xi\), has the
Hermite--Biehler property exactly when the relevant real-rootedness and
interlacing properties hold. Those are equivalent to the missing sign
statement.

## Status

The de Branges route is reduced to constructing an Euler--Gamma
Hermite--Biehler function \(E\) independently of the zero divisor. The
tautological divisor-built route is eliminated.
