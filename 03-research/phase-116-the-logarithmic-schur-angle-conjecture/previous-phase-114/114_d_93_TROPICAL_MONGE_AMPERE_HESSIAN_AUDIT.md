# D.93 — Tropical Monge--Ampere/Ronkin Hessian audit

## Status

This note tests a genuinely coefficient-dependent geometric energy on the
periodic section moduli of row A.  Unlike the framed determinant metric,
the Ronkin (log-sum-exp) energy has a nonzero intrinsic Hessian.  Its
Hessian is, however, a positive covariance/graph-Laplacian form; after the
concave sign convention it is a negative local Dirichlet form and kills
the common coefficient direction.

The row-C prime-power block is not of this type.  Its Bloch symbol changes
sign and has a nonzero value at the trivial character.  Even if the edge
weights are chosen to be the already constructed central orbit weights
`p^(-k/2)`, the natural Monge--Ampere Laplacian differs from the required
prime symbol by an explicit positive constant.  The Gamma oscillator has
the correct Dirichlet part but also contains a finite-part mass which no
translation-invariant coefficient Hessian can produce.  On separable
Kunneth coefficients the mixed Hessian vanishes identically.

Thus periodic Ronkin/Aubin--Mabuchi concavity supplies genuine geometry,
but not the completed prime--Gamma form.  The mismatch is structural and
term-by-term; no weights are tuned from `B_nuc`.  This rules out this
particular proposed source of row D, not row D itself.

No RH statement or desired sign is used.  The paper is not modified.

## 1. The intrinsic Ronkin energy of a regular section cell

Fix a periodic component `C_p x C_q`, effective one-dimensional extremals
`phi_i`, `psi_j`, and write `alpha=(i,j)`.  On a regular mixed cell the
section is

\[
 F_c(z)=\max_{\alpha}\{B_\alpha(z)+c_\alpha\},\qquad
 B_{ij}(x,y)=\phi_i(x)+\psi_j(y).                         \tag{1.1}
\]

Let `mu` be normalized Haar measure on the periodic product.  For
`beta>0` define the smooth Ronkin approximation

\[
 \mathcal R_\beta(c)=\int {1\over\beta}
 \log\!\left(\sum_\alpha
 e^{\beta(B_\alpha(z)+c_\alpha)}\right)d\mu(z).          \tag{1.2}
\]

Put

\[
 w_\alpha(z;c)=
 {e^{\beta(B_\alpha(z)+c_\alpha)}\over
  \sum_\gamma e^{\beta(B_\gamma(z)+c_\gamma)}}.         \tag{1.3}
\]

Differentiation under the finite sum and compact integral gives

\[
 \partial_\alpha\mathcal R_\beta=\int w_\alpha d\mu,
 \qquad
 \partial_\alpha\partial_\gamma\mathcal R_\beta
 =\beta\int(\delta_{\alpha\gamma}w_\alpha
             -w_\alpha w_\gamma)d\mu.                    \tag{1.4}
\]

Consequently, for every coefficient tangent `v`,

\[
 v^*D^2\mathcal R_\beta v
 =\beta\int\left(\sum_\alpha w_\alpha|v_\alpha|^2
       -\left|\sum_\alpha w_\alpha v_\alpha\right|^2
          \right)d\mu\ge0.                               \tag{1.5}
\]

The rows sum to zero, the off-diagonal entries are nonpositive, and the
common coefficient vector is in the radical.  Thus `D^2 R_beta` is a
weighted graph Laplacian.  With the concave convention `-R_beta`, it is a
negative Dirichlet form.  As `beta` tends to infinity the measure
concentrates on dominance walls and gives the corresponding tropical
Monge--Ampere wall Laplacian; the sign and the radical persist.

This is an intrinsic coefficient Hessian of actual effective sections.
It therefore repairs the zero-Hessian defect of the framed determinant,
but its very construction sharply restricts its possible kernel.

## 2. Bloch comparison with every prime power

Any translation-invariant concave graph energy on a cyclic/bilateral
coefficient orbit, with nonnegative edge conductances `a_k`, has symbol

\[
 h_{\rm MA}(\theta)
 =-2\sum_{k\ge1}a_k(1-\cos k\theta)\le0,
 \qquad h_{\rm MA}(0)=0.                                  \tag{2.1}
\]

For one prime put `L=log p` and `r=p^(-1/2)`.  The exact row-C block from
D.32 has all nonzero prime powers and Bloch symbol

\[
 h_p(\theta)
 =L\bigl(P_r(e^{i\theta})-1\bigr)
 =2L\sum_{k\ge1}r^k\cos(k\theta),                         \tag{2.2}
\]

where

\[
 P_r(e^{i\theta})={1-r^2\over1-2r\cos\theta+r^2}.          \tag{2.3}
\]

It is not a graph-Laplacian symbol:

\[
 h_p(0)={2Lr\over1-r}>0,
 \qquad
 h_p(\pi)=-{2Lr\over1+r}<0.                               \tag{2.4}
\]

The mismatch remains even if one imports only the already geometrically
constructed central orbit conductances `a_k=L r^k`.  Their natural
concave Laplacian is

\[
 \begin{aligned}
 h_{\rm lap,p}(\theta)
 &=-2L\sum_{k\ge1}r^k(1-\cos k\theta)\\
 &=L\bigl(P_r(e^{i\theta})-P_r(1)\bigr)\le0.               \tag{2.5}
 \end{aligned}
\]

Hence, exactly,

\[
 \boxed{h_p(\theta)-h_{\rm lap,p}(\theta)
       =L\bigl(P_r(1)-1\bigr)={2Lr\over1-r}.}              \tag{2.6}
\]

This constant is the local mass subtraction/finite part which a
coefficient-difference Hessian cannot see.  Formula (2.6) includes every
power `p^k`; it is not an asymptotic comparison.

## 3. Gamma comparison

The exact archimedean block of D.32 is

\[
 G_\infty(f,g)=m_0\langle f,g\rangle
 -\langle\partial_\infty f,\partial_\infty g\rangle,       \tag{3.1}
\]

with

\[
 \langle\partial_\infty f,\partial_\infty g\rangle
 =\int_0^\infty {e^{-s/2}\over1-e^{-2s}}
 \langle f-S_sf,g-S_sg\rangle ds.                         \tag{3.2}
\]

The second term is exactly of Dirichlet/Monge--Ampere type: its multiplier
is nonnegative and vanishes at the trivial character.  The first term is
the nonzero Gamma finite-part mass

\[
 m_0=\log\pi-\psi(1/4).                                   \tag{3.3}
\]

Because every Hessian in (1.4) kills the common coefficient direction, it
cannot generate (3.3).  Adding `m_0 I` by hand would import the completed
Gamma character rather than derive it from periodic section concavity.

Thus the same obstruction occurs at infinity as at a finite prime:
section competition constructs the difference energy, while the required
completed block also has a finite-part mass.

## 4. Kunneth audit

For separable coefficient tangents

\[
 c_{ij}=u_i+v_j,                                         \tag{4.1}
\]

the partition sum factors pointwise:

\[
 \sum_{i,j}e^{\beta(\phi_i+\psi_j+u_i+v_j)}
 =\left(\sum_i e^{\beta(\phi_i+u_i)}\right)
  \left(\sum_j e^{\beta(\psi_j+v_j)}\right).            \tag{4.2}
\]

With product Haar measure this yields

\[
 \mathcal R_{p,q}(u\boxplus v)
 =\mathcal R_p(u)+\mathcal R_q(v),
 \qquad D_uD_v\mathcal R_{p,q}=0.                         \tag{4.3}
\]

Therefore the natural Ronkin energy has no mixed Hessian on the two
primitive Kunneth jets.  Allowing arbitrary matrix coefficients creates
competition between extremals and the local graph Laplacian (1.4), but it
does not turn (4.3) into the completed convolution character of row C.

The periodic site is a disjoint sum over `(p,q)` components.  Summing
their intrinsic energies remains componentwise; it does not create the
global signed coupling between the finite contact tower and the Gamma
boundary which D requires.

## 5. Aubin--Mabuchi and Mahler variants

The same conclusion applies to the standard local
Aubin--Mabuchi/Monge--Ampere Hessian.  On a fixed positive
Monge--Ampere background its second variation, modulo affine constants,
is a local Dirichlet pairing.  It is sign-definite and annihilates the
constant potential.  These two structural properties already contradict
(2.4) and the mass term (3.3).

A direct Mahler/Ronkin functional for `1-rz` is harmonic away from its
amoeba boundary and piecewise affine after circle averaging (Jensen's
formula).  Its Monge--Ampere measure lives on the dominance boundary.  It
does not produce the Poisson kernel (2.3) as a coefficient Hessian unless
one additionally supplies the Hardy/Szego metric and the central radius
`r=p^(-1/2)` from row C.  Supplying them recovers the feature factorization
of D.32, not a new positive geometric Hessian.

## 6. Consequence and next admissible pivot

The calculation distinguishes three objects which must not be conflated:

1. the intrinsic Ronkin/Monge--Ampere Hessian, a local graph Laplacian;
2. the exact row-C contact, a signed correlation plus finite-part mass;
3. the primitive restriction, where the two global Tate moments vanish.

The first does not pull back to the second.  In particular, periodic
section concavity alone cannot prove row D.

The remaining viable geometric pivot must produce the missing mass by a
**global boundary curvature or Schur complement before restriction to the
two-jet kernel**, not by a local coefficient Hessian.  The exact target
remains the D.32 factorization

\[
 B_{\rm nuc}(f,g)
 =\langle\mathbf Sf,\mathbf Sg\rangle
  -\langle\mathbf Bf,\mathbf Bg\rangle,                  \tag{6.1}
\]

with the primitive condition

\[
 M_-(f)=M_+(f)=0.                                       \tag{6.2}
\]

Thus the next test is a global Deligne-pairing/Quillen-curvature or
Dirichlet-to-Neumann construction whose Schur complement has (6.1) as its
exact boundary pullback.  Such a construction would derive the mass terms
and could potentially force the missing contraction; merely declaring its
curvature to be `-B_nuc` would be circular.

