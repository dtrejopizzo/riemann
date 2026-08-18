# D.249 — The complete Gamma channel is a renormalized Blaschke-delay network

## Verdict

The continuous Gamma reference and the resolvent load in D.137 admit an
exact scattering decomposition.  The digamma difference is the convergent
sum, over the archimedean oscillator levels, of a free delay minus the
positive Wigner--Smith delay of a half-plane Blaschke factor.  The
\((\tau^2+1/4)^{-1}\) load is itself the delay of one additional Blaschke
factor.

Thus every component of the balanced prime--Gamma factorization now comes
from a source-defined conservative local scattering system.  The
renormalized free-delay constants must remain paired with their delays;
separating them creates a divergent harmonic sum.

This completes the local conservative network.  The remaining theorem is
global: identify its support-compressed, Tate-shorted transfer defect with
the D.190 Schur residual.

## 1. Half-plane Blaschke delay

For \(a>0\), put

\[
 \mathfrak b_a(\tau)={\tau-ia\over\tau+ia}.         \tag{1.1}
\]

It is the boundary value of a scalar inner function on the upper
half-plane.  Direct differentiation gives

\[
 \boxed{
 -i\,\partial_\tau\log\mathfrak b_a(\tau)
 ={2a\over\tau^2+a^2}=:D_a(\tau)>0.
 }                                                   \tag{1.2}
\]

Its zero-frequency, or free, delay is

\[
 D_a(0)={2\over a}.                                 \tag{1.3}
\]

Hence

\[
 D_a(0)-D_a(\tau)
 ={2\tau^2\over a(\tau^2+a^2)}\ge0.                \tag{1.4}
\]

Each \(\mathfrak b_a\) has the standard two-dimensional unitary
continuous-time colligation; equation (1.2) is its positive
Wigner--Smith kernel.

## 2. Digamma reference

The classical absolutely convergent digamma identity is

\[
 \mathrm{Re}\,\psi(b+iy)-\psi(b)
 =\sum_{n\ge0}{y^2\over
   (n+b)((n+b)^2+y^2)},\qquad b>0.                 \tag{2.1}
\]

Take \(b=5/4\), \(y=\tau/2\), and put

\[
 a_n=2(n+\tfrac54)=2n+\tfrac52.                    \tag{2.2}
\]

Then every summand in (2.1) is

\[
 {\tau^2\over(n+\tfrac54)
      (\tau^2+4(n+\tfrac54)^2)}
 ={2\over a_n}-{2a_n\over\tau^2+a_n^2}.            \tag{2.3}
\]

Therefore

\[
 \boxed{
 R_\Gamma(\tau):=
 \mathrm{Re}\,\psi(\tfrac54+\tfrac{i\tau}{2})
 -\psi(\tfrac54)
 =\sum_{n\ge0}\bigl(D_{a_n}(0)-D_{a_n}(\tau)\bigr).
 }                                                   \tag{2.4}
\]

The series converges locally uniformly because its summands are
\(O(\tau^2a_n^{-3})\).  Formula (2.4) is exactly the Fourier symbol of
\(D_\infty^*D_\infty\) in D.137.

The individual free-delay sum \(\sum_n2/a_n\) diverges.  Only the paired
differences in (2.4) are defined.  This is the archimedean analogue of the
order-\(\vartheta(N)\) identity/Poisson cancellation in D.238.

## 3. The resolvent load

At \(a=1/2\), equation (1.2) gives

\[
 \boxed{
 D_{1/2}(\tau)={1\over\tau^2+1/4}.
 }                                                   \tag{3.1}
\]

This is exactly the Gram symbol of the D.137 load channel \(Q_{1/2}\).
The remaining load scalar is

\[
 \beta=\log\pi-\psi(5/4)>0.                         \tag{3.2}
\]

Using the recurrence

\[
 \psi(5/4+iy)=\psi(1/4+iy)+{1\over1/4+iy}
\]

and taking real parts yields the exact Gamma score decomposition

\[
 \boxed{
 m_\infty(\tau)
 =\beta+D_{1/2}(\tau)-R_\Gamma(\tau).
 }                                                   \tag{3.3}
\]

This is the archimedean part
\(\|Y_TF\|^2-\|X_TF\|^2\) of D.137.

## 4. Conservative network interpretation

Equations (2.4) and (3.3) give a source network with:

* reference ports \(D_{a_n}(0)-D_{a_n}(\tau)\), \(n\ge0\);
* one load delay \(D_{1/2}(\tau)\);
* the finite renormalized scalar port \(\beta\).

Every \(D_a\) is the delay of a unitary Blaschke colligation.  The
renormalized difference in (2.4) is positive and has the screw-feature
realization \(D_\infty\).  Thus no condition on zeta zeros is hidden in the
Gamma factorization.

Together with D.248, the complete balanced network consists of:

1. prime disk-Blaschke colligations, one state per prime and all powers;
2. archimedean half-plane Blaschke colligations, one per oscillator level;
3. the scalar free-delay/contact ports fixed by Tate normalization.

## 5. Remaining transfer theorem

Let \(\mathcal U_S^{\rm loc}\) denote the cascade/direct-sum network just
described, with the prime tangent colligation of D.247.  It is conservative
before position support compression.  The required theorem is:

> The transfer defect of the compression of
> \(\mathcal U_S^{\rm loc}\) to the old/born support cells, after the two
> Tate ports are shorted, equals
> \[
> B_E-X_{OE}^*A_O^\dagger X_{OE}.
> \]

The equality must retain the paired free-delay cancellations and be proved
first with \(A_O+\varepsilon I\), then in the monotone
\(\varepsilon\downarrow0\) limit.  If it holds, conservativity supplies
the sign and the supported-range inclusion simultaneously.

## 6. Classification

* Blaschke delay identity (1.2)--(1.4): **PROVED**.
* Digamma delay network (2.4): **PROVED**.
* Resolvent delay identification (3.1): **PROVED**.
* Complete Gamma balance (3.3): **PROVED**.
* Local prime--Gamma conservative network: **CONSTRUCTED AS AN
  ORTHOGONAL SUM/CASCADE OF THE DISPLAYED LOCAL COLLIGATIONS**.
* Equality of its compressed transfer defect with D.190: **OPEN**.
* Row D: **OPEN**.
