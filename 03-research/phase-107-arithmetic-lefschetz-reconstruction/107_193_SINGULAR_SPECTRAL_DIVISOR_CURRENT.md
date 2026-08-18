# 107.193 -- Singular spectral divisor current and finite-type compactification no-go

## 1. Source-derived entire determinant

The determinant construction of `107_182--187` begins in

\[
 \mathcal H=\{s\in\mathbb C:\Re(s)>1\}
\]

with prime orbit determinants, the archimedean number operator, and the
degree-zero/two factors.  Its completed value is

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
 \tag{1.1}
\]

The classical functional equation and analytic continuation extend
(1.1) to an entire function on \(\mathbb C\).  No zero list is used to
define this extension.

## 2. Singular current

Let

\[
 Z_\xi=\sum_{\xi(\rho)=0}m_\rho[\rho]
 \tag{2.1}
\]

be the locally finite analytic divisor of the derived entire function.
Normalize \(dd^c\) so that the Poincare--Lelong formula reads
\(dd^c\log|f|=[\mathrm{div}(f)]\).  Then

\[
 dd^c\log|\xi|=[Z_\xi].
 \tag{2.2}
\]

Equivalently, the flat connection of `107_192` extends meromorphically:

\[
 A=-d\log\xi,
 \qquad
 \mathrm{res}_{s=\rho}A=-m_\rho.
 \tag{2.3}
\]

Thus the smooth zero curvature on \(\mathcal H\) acquires exactly the
atomic divisor current when the singular extension is admitted.  This
constructs a genuine spectral current from the determinant rather than
installing a prescribed trace.

## 3. Infinite-divisor theorem

Hardy's theorem gives infinitely many zeros of \(\zeta\) on the
critical line.  None is cancelled in (1.1), so \(Z_\xi\) has infinite
support.

**Theorem.**  There is no proper finite-type algebraic curve \(C\), no
finite-degree algebraic line bundle \(L\) on \(C\), and no nonzero
meromorphic section \(\sigma\) of \(L\) whose divisor contains the
full spectral divisor \(Z_\xi\) with the spectral parameter realized
algebraically on a dense open.

**Proof.**  The divisor of a nonzero meromorphic section of a line
bundle on a proper algebraic curve has finite support.  Indeed zeros and
poles are closed zero-dimensional subschemes of a noetherian proper
curve and therefore have finite length.  But Hardy's theorem makes the
support of \(Z_\xi\) infinite.  Hence such \((C,L,\sigma)\) cannot
exist. \(\square\)

In particular, adding one point at infinity to the spectral plane does
not make \(\xi\) a meromorphic function on \(\mathbb P^1\): infinity
is an essential singularity, as also forced by the infinite zero
divisor.

## 4. Consequence for the arithmetic-square program

The singular mechanism left open by `107_192` is real, but it cannot
enter ordinary finite-type Arakelov intersection theory through a
proper algebraic spectral compactification.  A surviving realization
must use at least one of:

1. a noncompact analytic spectral direction with locally finite
   currents;
2. an ind/pro object carrying an infinite divisor;
3. a relative boundary or renormalized current;
4. an analytic-torsion/Bott--Chern class on a different proper
   arithmetic geometry.

Equation (2.2) is not yet row (c): it is a current on the spectral
parameter plane, not on the Connes--Consani absolute square, and no
Deligne pairing or primitive Hodge form has been constructed.  It does,
however, prove that the missing information reappears precisely as a
singular divisor after continuation.

## 5. Mandatory falsifiers

The construction is zero-free at source level: prime/Gamma determinants
define \(\xi\) on \(\mathcal H\), and analytic continuation produces
the divisor.  The Davenport--Heilbronn function also has a zero divisor,
but it has no prime-orbit Euler determinant feeding (1.1); therefore it
fails before the current is admitted.  Merely applying
Poincare--Lelong to an arbitrary completed function is not a Phase 107
source construction.

The verifier uses actual zeta zeros only as target-side falsifiers.  It
checks distinct zeros, small values of \(\xi\) at them, and contour
integrals of \(\xi'/\xi\) giving multiplicity one.  For every fixed
degree cap below the tested count, the observed divisor already rejects
that cap.  The theorem of infinite support rests on Hardy, not on the
finite numerical sample.

## 6. Exact scope

This result closes the proper finite-type **spectral compactification**
route.  It does not rule out a proper arithmetic surface whose
archimedean Green datum is infinite-dimensional, because the spectral
parameter need not be an algebraic coordinate of that surface.  Nor
does it prove negativity of the singular current.
