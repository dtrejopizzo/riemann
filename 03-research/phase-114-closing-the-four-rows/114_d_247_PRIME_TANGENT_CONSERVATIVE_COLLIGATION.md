# D.247 — A conservative prime-tangent colligation with unit defect

## Verdict

The Lorentzian tangent identity of D.244 is equivalent to an exact
source-defined conservation law.  After adjoining one scalar degree
channel to the odd tangent and one reduced-contact channel per prime to the
even tangent, the resulting input and output maps have identical Grams.
They therefore define a canonical partial isometry.

On the primitive degree kernel this colligation gives the D.244 contraction
with an explicit positive contact defect and constant exactly one.  No
pseudoinverse, zero, or assumed Weil sign enters.

This closes the conservative colligation problem for the complete
prime-tangent sector, including all powers through D.244(5.4).  The
remaining port is to identify its support-compressed transfer colligation,
with the Gaussian channel of D.246 adjoined, with the D.190 old/born
colligation.

## 1. Exact balance

Use the notation of D.244:

\[
 \mathcal E_\pm c=\sum_{p\in S}c_pe_{p,\pm},\qquad
 A_S=\prod_{p\in S}(1-p^{-2}),\qquad
 x_p=-{\log p\over p+1}.
\]

D.244(2.7) says

\[
 \|\mathcal E_+c\|^2-\|\mathcal E_-c\|^2
 =A_S\left(|x^*c|^2-\sum_p|x_p|^2|c_p|^2\right).
                                                               \tag{1.1}
\]

Rearranging gives the conservation identity

\[
 \boxed{
 \|\mathcal E_-c\|^2+A_S|x^*c|^2
 =
 \|\mathcal E_+c\|^2
 +A_S\sum_p|x_p|^2|c_p|^2.
 }                                                   \tag{1.2}
\]

Define

\[
 \begin{aligned}
 \mathcal I_Sc
  &=\left(\mathcal E_-c,\sqrt{A_S}\,x^*c\right),\\
 \mathcal O_Sc
  &=\left(\mathcal E_+c,
          \sqrt{A_S}\,(x_pc_p)_{p\in S}\right).
 \end{aligned}                                      \tag{1.3}
\]

Then

\[
 \boxed{\mathcal I_S^*\mathcal I_S
       =\mathcal O_S^*\mathcal O_S.}                \tag{1.4}
\]

Because \(\mathcal E_-\) is injective, \(\mathcal I_S\) is injective.

## 2. Canonical partial isometry

On \(\operatorname{Ran}\mathcal I_S\), define

\[
 \mathcal U_S(\mathcal I_Sc)=\mathcal O_Sc.         \tag{2.1}
\]

Equation (1.4) proves that this is well defined and isometric.  It extends
uniquely by continuity to

\[
 \boxed{
 \mathcal U_S:
 \overline{\operatorname{Ran}\mathcal I_S}
 \xrightarrow{\ \simeq\ }
 \overline{\operatorname{Ran}\mathcal O_S}.
 }                                                   \tag{2.2}
\]

Extending it by zero on the orthogonal complement gives a canonical partial
isometry; adjoining the two defect complements gives a unitary dilation if
one is required.  No choice of a positive spectral subspace is involved:
both initial and final spaces are the ranges of the explicit source maps
(1.3).

## 3. Primitive defect

On the primitive coefficient hyperplane

\[
 \mathcal K_S=\ker x^*,
\]

the scalar input channel vanishes.  Formula (1.2) becomes

\[
 \boxed{
 \|\mathcal E_-c\|^2-\|\mathcal E_+c\|^2
 =A_S\sum_p|x_p|^2|c_p|^2,
 \qquad c\in\mathcal K_S.
 }                                                   \tag{3.1}
\]

Thus the contraction of D.244 has the exact defect operator

\[
 \boxed{
 I-\Theta_S^*\Theta_S
 =A_S\,
 (\mathcal E_-|_{\mathcal K_S})^{-\!*}
 \operatorname{diag}(|x_p|^2)
 (\mathcal E_-|_{\mathcal K_S})^{-1}
 }                                                   \tag{3.2}
\]

as a quadratic form on \(\operatorname{Ran}
\mathcal E_-|_{\mathcal K_S}\).  Formula (3.1), rather than the formal
inverse notation in (3.2), is the definition on the source range.

Equality is possible only at \(c=0\) for finite \(S\).

## 4. Torsion normalization

After the coordinate changes of D.244(4.1) and (4.7), divide the common
scalar \(A_S\) from the auxiliary channels.  The conservation law has the
canonical arithmetic shape

\[
 \boxed{
 \|\widetilde{\mathcal E}_-z\|^2
 +\left|\sum_p\sqrt{\log p}\,z_p\right|^2
 =
 \|\widetilde{\mathcal E}_+z\|^2
 +\sum_p(\log p)|z_p|^2.
 }                                                   \tag{4.1}
\]

The scalar input is the global degree channel.  The diagonal output is
exactly the reduced torsion determinant contact of row B.  For
\(z_p=\sum_kp^{-k/2}a_{p^k}\), it includes all prime powers and gives
\(\Lambda(p^{k+\ell})/\sqrt{p^{k+\ell}}\).

Thus (4.1) is a conservative, source-defined local-to-global completion of
the finite-contact blocks.

## 5. What remains for D.190

The colligation (4.1) lives before:

1. the semilocal quotient;
2. position support compression;
3. the Gaussian/Gamma tangent channel;
4. the two global Tate equations;
5. old-core Green shorting.

D.245--D.246 prove that pairing the even tangent with the dual central
state yields exactly the complete prime--Gamma score before these
operations.  The carrying comparison theorem is now:

> The support-compressed transfer colligation induced by
> \(\mathcal U_S\), after adjoining the archimedean tangent and removing the
> two Tate channels, has old/born transfer block \(X_{OE}\), old defect
> \(A_O\), and born defect \(B_E\) of D.190.

If proved, contractivity of a transfer block of the unitary dilation gives
the sharp Douglas bound with constant one.  The theorem must be checked at
the level of ranges and closed form domains; it cannot be defined by the
D.190 pseudoinverse.

## 6. Classification

* Conservative identity (1.2)--(1.4): **PROVED**.
* Canonical partial isometry (2.1)--(2.2): **PROVED**.
* Primitive unit defect and equality case (3.1): **PROVED**.
* Torsion-normalized contact colligation (4.1): **PROVED**.
* Inclusion of every prime power through the orbit coordinate:
  **PROVED**, using D.244.
* Support/Gamma/Tate transfer comparison with D.190: **OPEN**.
* Row D: **OPEN**.
