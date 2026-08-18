# D.239 — Prime towers as the score of the semilocal cyclic measure

## Verdict

The rational state of D.236--D.237 is exactly the normalized local density
which appears in the semilocal Hardy--Titchmarsh cyclic measure.  Moreover
the full prime-power contact tower is its transverse logarithmic derivative.
This gives a precise bridge from the D.190 boundary operator to the
Connes--Consani--Moscovici semilocal prolate framework.

For

\[
 L_p(s)=(1-p^{-s})^{-1},\qquad s=\sigma+i\tau,
\]

put (r=p^{-1/2}) and (U_p(\tau)=e^{-i\tau\log p}).  Then

\[
 \boxed{
 (1-p^{-1})|L_p(\tfrac12+i\tau)|^2
 ={1-r^2\over|1-rU_p(\tau)|^2}
 =P_r(U_p(\tau)).
 }                                                     \tag{0.1}
\]

The same Poisson function is the symbol of (V_p^*V_p) in D.236.  Also

\[
 \boxed{
 -\left.\partial_\sigma
   \log|L_p(\sigma+i\tau)|^2\right|_{\sigma=1/2}
 =(\log p)(P_r(U_p(\tau))-1)
 =\sum_{k\ge1}{\log p\over p^{k/2}}
  (U_p(\tau)^k+U_p(\tau)^{-k}).
 }                                                     \tag{0.2}
\]

Thus the finite-place part of row D is the score of the product of the
local cyclic densities, while D.237 gives a state-space spectral factor of
each density.  This is derived before using any zero of zeta.

The bridge does not yet prove the sign.  A derivative of a positive measure
need not be positive, and the semilocal prolate literature explicitly
presents global Weil positivity as the remaining strategy rather than a
theorem.  The new exact target is a monotonicity/defect theorem for the
semilocal cyclic pair after support cutoff and removal of the two Tate
characters.  Proving that theorem would supply the source-defined
contraction required by D.190; assuming it would be circular.

## 1. Proof of the local score identity

Let

\[
 q=p^{-\sigma-i\tau}.
\]

Since

\[
 \partial_\sigma\log L_p(\sigma+i\tau)
 =-{(\log p)q\over1-q},                              \tag{1.1}
\]

we obtain

\[
 -\partial_\sigma\log|L_p(\sigma+i\tau)|^2
 =2(\log p)\mathrm{Re}{q\over1-q}.           \tag{1.2}
\]

At (sigma=1/2), the scalar Poisson identity is

\[
 {1-r^2\over|1-rU|^2}-1
 =2\mathrm{Re}{rU\over1-rU}.                 \tag{1.3}
\]

Equations (1.2)--(1.3) prove the first equality in (0.2).  Expanding the
resolvent in its absolutely convergent geometric series proves the second.
Equation (0.1) is immediate from the Euler factor.

## 2. Finite semilocal product

For a finite set of primes (S), define

\[
 \mathcal L_S(\sigma,\tau)=\prod_{p\in S}L_p(\sigma+i\tau),
 \qquad
 d\mu_{S,\sigma}(\tau)=
 |\mathcal L_S(\sigma,\tau)|^2d\tau.               \tag{2.1}
\]

Logarithmic differentiation and (0.2) give the exact additive contact
identity

\[
 -\left.\partial_\sigma\log d\mu_{S,\sigma}(\tau)
 \right|_{\sigma=1/2}
 =\sum_{p\in S}(\log p)(P_{p^{-1/2}}(U_p(\tau))-1). \tag{2.2}
\]

After inverse Fourier transformation, (2.2) is exactly the sum over all
(p^k) of the central coefficients
((\log p)p^{-k/2}) and translations by (k\log p).  Support compression
retains precisely the finite powers active in the window.

The normalized density

\[
 \prod_{p\in S}(1-p^{-1})|\mathcal L_S(1/2,\tau)|^2
\]

is the product of the D.236 Poisson states.  Notice that row D uses the
**logarithmic derivative** of this product, hence an additive direct sum of
local scores; it does not use the product itself as a positive replacement
for the Weil form.

## 3. Archimedean completion and the exact research target

The Gamma screw in D.137 is likewise a logarithmic derivative of the
archimedean local factor, after the Tate--Chebyshev shift from (1/4) to
(5/4).  The scalar (eta) and (Q_{1/2}) channels record that shift and
the two polar modes.  Therefore the complete D.190 multiplier is the
centered score of the completed semilocal cyclic measure, compressed to a
support window.

Let ((\mathbb S_S,\xi_S)) denote the semilocal cyclic pair and let
(K_{S,n}) be the degree-(n) Christoffel--Darboux kernel of its orthogonal
polynomial filtration.  A sufficient source theorem would have the
following form:

\[
 \boxed{
 -\left.\partial_\sigma
   \langle F,K_{S,n}(\sigma)F\rangle_{\mu_{S,\sigma}}
   \right|_{\sigma=1/2}\ge0
 }
                                                               \tag{3.1}
\]

for the support-localized vectors satisfying the two Tate equations, with
a limit theorem as (n\to\infty) and (S\uparrow\{p<e^{2T}\}) identifying
the limiting derivative with (Q_T=-B_{\rm nuc,T}).  To close D, (3.1)
must be strengthened or translated into the sharp old/shell defect identity
of D.190, including range and equality.

The point of (3.1) is not that it is already known.  It identifies what the
semilocal prolate approach must prove in order to pay the D.190 capacity:
monotonicity of the **score of the cyclic filtration**, not positivity of
the cyclic measure itself.

## 4. Literature audit

The primary semilocal paper states that for every cutoff (n) there is a
finite-place property whose validity for all (n) is equivalent to RH, and
describes the prolate construction as a strategy for semilocal Weil
positivity.  It proves the cyclic-pair/prolate infrastructure and stability
of the semilocal Sonin spaces, but does not prove the global positivity
required in (3.1):

* A. Connes, C. Consani, H. Moscovici,
  [Zeta zeros and prolate wave operators](https://arxiv.org/abs/2310.18423).

The single-archimedean-place predecessor proves a positive Sonin trace and
controls its discrepancy using pairs of projections and Toeplitz matrices,
while explicitly presenting the general semilocal case as the intended
extension:

* A. Connes, C. Consani,
  [Weil positivity and Trace formula, the archimedean place](https://arxiv.org/abs/2006.13771).

Therefore neither result may be cited as a proof of (3.1).  D.236--D.239
instead identify the exact local score and the precise extra monotonicity
statement that would port their framework to row D.

## 5. Equality and falsification requirements

If (3.1) is proved by a projection/Christoffel--Darboux identity, equality
must be traced through that identity.  The only permissible limiting kernel
on the primitive space is the known radical; the two polar modes are removed
before the limit.

The proposed monotonicity must also be tested on the off-line Beurling
surrogate.  A proof using only positivity of each local Poisson density and
PNT-type moment bounds will survive there and cannot be sufficient.  The
step which fails for the surrogate must use the adelic Fourier/Poisson
self-duality or an equivalent arithmetic feature specific to
\(\mathbb Q\).

## 6. Classification

* Local density identity (0.1): **PROVED**.
* Logarithmic score/contact identity (0.2), including all (p^k):
  **PROVED**.
* Finite semilocal product identity (2.2): **PROVED**.
* Identification with the local cyclic densities of the semilocal
  framework: **PROVED BY FORMULA / PRIMARY-SOURCE COMPATIBLE**.
* Monotonicity theorem (3.1) and its sharp Douglas realization: **OPEN**.
* Global row D: **OPEN**.
