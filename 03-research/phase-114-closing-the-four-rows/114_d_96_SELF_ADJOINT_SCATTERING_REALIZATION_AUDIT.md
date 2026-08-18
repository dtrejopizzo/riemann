# D.96 — Self-adjoint scattering realization audit

## Status

The completed determinant of D.94 has a canonical transfer function.  For
each positive displacement `a`, it is the quotient of the two determinant
lines exchanged by the functional-equation reflection.  Its boundary
values are unitary.  It admits a positive Hilbert-space colligation, a
Hermite--Biehler de Branges space, and a self-adjoint canonical system
exactly when it is Schur in the upper half-plane.

The Schur/Hermite--Biehler condition is equivalent to absence of zeros with
`Re(rho)>1/2+a`.  The realization is therefore unconditional at the safe
edge `a>=1/2`; continuation of the positive canonical-system chain to
every `a>0` is equivalent to RH.  An off-line zero creates a pole of the
transfer function and a negative de Branges kernel value.  In finite
truncations it contributes exactly the negative direction of the free
Real orbit found in D.95.

The prime and Gamma determinants do define the transfer function without
using the zeros in their half-plane of absolute convergence, but their
individual local ratios are not Schur.  Thus placewise positivity cannot
be tensored to the centre.  The symmetric prime--Gamma convolution
operator is source-defined and self-adjoint on finite windows, but its
spectral determinant is not `Xi`; identifying the two would be the missing
theorem.

Accordingly, no essentially self-adjoint Hilbert--Polya operator is
constructed here.  The canonical object currently obtained from A--B--C
is a Real/Krein scattering system; it becomes a Hilbert self-adjoint system
precisely after the row-D positivity is known.

No RH statement is assumed.  The paper is not modified.

## 1. Transfer function of the functional-equation double

Let `Xi` be the real entire completed function, normalized so that

\[
 \Xi(s)=\Xi(1-s),\qquad
 \overline{\Xi(\overline s)}=\Xi(s).                       \tag{1.1}
\]

For `a>0` put

\[
 E_a(z)=\Xi(1/2+a-iz),
 \qquad E_a^\#(z)=\overline{E_a(\overline z)}.              \tag{1.2}
\]

The functional equation gives

\[
 E_a^\#(z)=\Xi(1/2-a-iz),                                 \tag{1.3}
\]

and hence the canonical scattering/transfer function is

\[
 \Theta_a(z)={E_a^\#(z)\over E_a(z)}
 ={\Xi(1/2-a-iz)\over\Xi(1/2+a-iz)}.                      \tag{1.4}
\]

For real `x`, `E_a^#(x)=overline(E_a(x))`, so

\[
 |\Theta_a(x)|=1                                          \tag{1.5}
\]

away from boundary zeros.  Thus the functional equation supplies
unitarity on the boundary, but not contractivity in the upper half-plane.

## 2. Exact zero transport

Let `rho=beta+i gamma` be a zero of `Xi`.  A zero of `E_a` occurs at

\[
 z_\rho=-\gamma+i(\beta-1/2-a).                            \tag{2.1}
\]

Therefore

\[
 z_\rho\in\mathbb C_+
 \quad\Longleftrightarrow\quad
 \beta>1/2+a.                                             \tag{2.2}
\]

Such a zero is a pole of `Theta_a`, unless a nongeneric cancellation with
its reflected numerator is present; keeping multiplicities, the divisor
statement is exact and the free Real orbit is not cancelled in the
mapping-cone realization.

The de Branges kernel associated with `E_a` is

\[
 K_a(z,w)=
 {E_a(z)\overline{E_a(w)}
  -E_a^\#(z)\overline{E_a^\#(w)}
  \over 2\pi i(\overline w-z)}.                            \tag{2.3}
\]

At an upper-half-plane zero `z_rho` of `E_a` for which
`E_a#(z_rho)` is nonzero,

\[
 K_a(z_\rho,z_\rho)
 =-{ |E_a^\#(z_\rho)|^2\over4\pi\operatorname{Im}z_\rho}<0.
                                                                    \tag{2.4}
\]

Hence an off-line zero produces an explicit negative square for every
generic displacement `a` for which the reflected value does not vanish;
the exceptional displacements form a discrete set of horizontal
coincidences between zeros.  At a simultaneous zero the strict
Hermite--Biehler inequality still fails, and an arbitrarily nearby generic
displacement separates the two values.  No global index theorem is needed
to see the failure of the positive chain.

## 3. Existing realization theorems and their exact hypothesis

The following standard implications are the relevant ones:

* `E_a` is Hermite--Biehler if and only if
  `|E_a#(z)|<|E_a(z)|` on `C_+` (with the standard bounded-type/mean-type
  normalization).
* This is equivalent to `Theta_a` being a Schur inner function.
* A scalar Schur inner function is the characteristic/transfer function of
  a conservative Hilbert-space colligation and determines a positive
  de Branges/canonical system.
* If the kernel has negative squares, the corresponding realization is in
  a Pontryagin/Krein space; it is not a Hilbert self-adjoint realization.

For the finite-order completed function, (2.2) gives

\[
 E_a\text{ Hermite--Biehler}
 \quad\Longleftrightarrow\quad
 \Xi\text{ has no zero with }\operatorname{Re}\rho>1/2+a.
                                                                    \tag{3.1}
\]

The harmless standard exponential factor fixes mean type and does not
move a zero or change (2.4).

All nontrivial zeros lie in `0<Re(rho)<1`.  Consequently the safe system
at

\[
 a\ge1/2                                                   \tag{3.2}
\]

has no upper-half-plane denominator zeros and admits the positive
realization.  On the other hand,

\[
 \boxed{
 E_a\text{ is Hermite--Biehler for every }a>0
 \quad\Longleftrightarrow\quad
 \operatorname{Re}\rho=1/2
 \text{ for every nontrivial zero}.}                      \tag{3.3}
\]

At `a=0`, the quotient in (1.4) degenerates to `1`; the mathematical
content is the existence of the positive chain all the way down to the
endpoint, not the endpoint quotient by itself.

## 4. Loewner-chain form of the remaining estimate

Differentiating (1.4) gives

\[
 \partial_a\log\Theta_a(z)
 =-{\Xi'\over\Xi}(1/2-a-iz)
  -{\Xi'\over\Xi}(1/2+a-iz).                              \tag{4.1}
\]

A positive nested canonical-system realization would require the
corresponding infinitesimal transfer generator to have the Herglotz/Pick
sign throughout `C_+`.  A pole enters (4.1) exactly when `a` crosses

\[
 a_\rho=\operatorname{Re}\rho-1/2                         \tag{4.2}
\]

for a zero to the right of the centre.  Thus preservation of the positive
Loewner chain from the safe edge to all `a>0` is another exact form of
(3.3).

The A--B central torsor specifies the centre and the reflection `a->-a`.
It supplies neither the Pick sign of (4.1) nor a mechanism preventing a
pole crossing (4.2).

## 5. Local prime factors are not Schur factors

In the half-plane where the Euler product converges, the prime part of the
ratio (1.4) contains factors of the form

\[
 R_{p,a}(z)={1-r_+e^{i\theta}\over1-r_-e^{i\theta}},
 \qquad 0<r_+<r_-<1,                                     \tag{5.1}
\]

with radii determined by the two real parts.  On the same circle,

\[
 |R_{p,a}(0)|={1-r_+\over1-r_-}>1,
 \qquad
 |R_{p,a}(\pi)|={1+r_+\over1+r_-}<1.                      \tag{5.2}
\]

Thus a finite-place determinant ratio is neither contractive nor
expansive pointwise.  The Gamma ratio does not turn each individual prime
factor into a Schur factor.  Contractivity, if true, is a completed global
statement after analytic continuation; proving it is not reducible to
tensoring local positive colligations.

This is the transfer-function counterpart of the sign-changing local
symbol in D.93--D.94.

## 6. Audit of source-defined symmetric operators

The arithmetic convolution form of D.32 is real and symmetric.  On each
support window its Friedrichs realization after a lower scalar shift is
self-adjoint, and the Gamma jump part is generated by a positive
Dirichlet form.  These statements use only prime--Gamma data.

However, its spectral parameter is the eigenvalue of the window operator,
whereas the zeros of `Xi` are the spectral parameters of the Meyer
quotient/explicit formula.  No determinant identity

\[
 \det_\zeta(A_{\rm arithmetic}-z)
 =e^{g(z)}\Xi(1/2-iz)                                     \tag{6.1}
\]

has been derived.  Moreover, forcing (6.1) for a Hilbert self-adjoint
operator would force all zeros of its right side to correspond to real
`z`, hence would already imply (3.3).

The Meyer realization is source-defined and has the correct spectral
determinant in a nuclear Frechet quotient, but it is not supplied with a
positive Hilbert norm making its generator self-adjoint.  Constructing
such a norm is equivalent to making the Real divisor form of D.95
positive.

Thus the available source operators split the desired properties:

\[
 \begin{array}{c|c|c}
 &\text{source-defined self-adjointness}&\text{determinant }\Xi\\ \hline
 \text{prime--Gamma window operator}&\checkmark&\text{not proved}\\
 \text{Meyer nuclear quotient}&\text{not Hilbert-positive}&\checkmark
 \end{array}                                               \tag{6.2}
\]

## 7. Consequence

The transfer-function route gives a precise noncircular target:

> Construct from the A--B--C prime--Gamma correspondence, without first
> using `Xi`'s divisor, a conservative Hilbert colligation whose transfer
> function is `Theta_a` for every `a>0`, or equivalently prove the Pick
> sign of (4.1) from a source estimate.

Existing realization theorems cannot be invoked before that estimate:
their Schur/Hermite--Biehler hypothesis is exactly the absence of the free
Real divisor blocks.  A Krein realization is canonical and unconditional,
but its negative index records rather than removes those blocks.

The next admissible test is therefore an **energy estimate for the
source-side Loewner generator** (4.1), expressed through the prime--Gamma
normal connection of D.94, on the two-moment primitive quotient.  If its
Pick kernel can be shown positive without analytic continuation through
the zero divisor, the positive chain and row D follow.  If that kernel is
algebraically the Weil form, the route is only an equivalent
reformulation.
