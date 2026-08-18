# 107.185 -- The inverse Euler class is a Green kernel on each prime orbit

## 1. Existing geometric orbit

For every prime \(p\), both Deninger's system and the Connes--Consani
scaling space contain a periodic orbit

\[
 C_p=\mathbb R/(\log p)\mathbb Z.
\]

Write \(\ell_p=\log p\).  For a spectral parameter \(s\), consider the
first-order operator on periodic functions

\[
 D_{p,s}={d\over dx}+s.
 \tag{1.1}
\]

Its homogeneous transport around the orbit has monodromy

\[
 t_p(s)=e^{-s\ell_p}=p^{-s}.
 \tag{1.2}
\]

The cellular cochain complex of the circle with this rank-one local
system has differential

\[
 1-t_p(s).
 \tag{1.3}
\]

Thus the Euler class inverted in `107_178` is the actual determinant of
the twisted orbit complex.

## 2. Explicit Green kernel

Assume \(t_p(s)\neq1\).  The periodic Green kernel based at the origin,
for \(0<x<\ell_p\), is

\[
 G_{p,s}(x)={e^{-sx}\over1-e^{-s\ell_p}}.
 \tag{2.1}
\]

Away from the origin, \(D_{p,s}G_{p,s}=0\).  Across the origin,

\[
 G_{p,s}(0^+)-G_{p,s}(\ell_p^-)=1,
\]

so distributionally

\[
 D_{p,s}G_{p,s}=\delta_0.
 \tag{2.2}
\]

The two one-sided return values are

\[
 G_{p,s}(0^+)={1\over1-p^{-s}},
 \qquad
 G_{p,s}(\ell_p^-)={p^{-s}\over1-p^{-s}}.
 \tag{2.3}
\]

The first is the full localized boundary class; the second is the
reduced class of `107_182`.

## 3. Recovery of the finite Euler channel

Multiplying the return value by the geometric orbit length gives

\[
 \ell_pG_{p,s}(\ell_p^-)
 =\log p\,{p^{-s}\over1-p^{-s}}.
\]

Therefore

\[
 \sum_p\ell_pG_{p,s}(\ell_p^-)
 =-{\zeta'(s)\over\zeta(s)}
 \qquad(\Re s>1).
 \tag{3.1}
\]

This realizes the finite-prime scalar Green channel on the **actual
periodic orbits supplied by row (b)**.  The passage

\[
 \text{Deninger orbit}
 \longrightarrow
 \text{twisted orbit determinant}
 \longrightarrow
 \text{return Green value}
\]

is now explicit.

When \(t_p(s)=1\), the twisted cohomology of the circle is nonzero and
the Green inverse does not exist.  Its pole is therefore cohomological,
not inserted by normalization.

## 4. Exact scope

The kernel (2.1) is a Green kernel for the first-order twisted orbit
operator.  It is not yet an Arakelov Green function for a divisor on a
proper arithmetic surface.  The missing global comparison must turn the
family \(G_{p,s}\), after Mellin pairing, into the archimedean/current
component of one primitive arithmetic class and add the Gamma orbit.

Nevertheless this closes a genuine part of the row-(b)/(c) bridge: the
finite local inverse Euler class and its global logarithmic derivative
now live on Deninger's constructed correspondences rather than on a
formal normal line.

## 5. Falsifier

The verifier fixes five real prime orbits and real/complex spectral
parameters.  It checks monodromy, the cellular determinant, the Green
equation away from the source, the unit jump, both return values, and
the geometric-series expansion.  Any failed orbit identity returns
`VERDICT: NO`.
