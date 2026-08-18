# 106.40 — The Möbius--theta primitive and curvature gate

## Purpose

The complementary contraction of 106.39 is equivalent to the full sharp
ordinary-prime inequality: radical shorting subtracts the same square from
both sides.  This note therefore returns to the literal source and combines
two structures which had previously been used separately:

1. the continuous theta atoms of 106.38; and
2. the Möbius connection (Z^{-1}\delta Z=V_\Lambda) of Phase 70.

Their combination gives an exact spatial Möbius inversion: the complete
Riemann theta kernel is the multiplicative zeta transform of its first
theta atom, and Möbius inversion recovers that atom pointwise.  The second
connection jet then yields a sharp scalar curvature inequality.  A minimal
prime-tower computation shows why this scalar inequality cannot be promoted
to an unrestricted Gram inequality without retaining Gamma, the pole and
the spatial embedding.

No zero location is used.

## 1. Zeta transform of the primitive theta atom

Use the theta atoms of 106.38,

\[
 k_m(x)=\pi m^2e^{5x/2}
 (2\pi m^2e^{2x}-3)e^{-\pi m^2e^{2x}},
 \qquad K(x)=\sum_{m\geq1}k_m(x),                    \tag{1}
\]

for (x\geq0).  Direct substitution gives the equivalent form of the
theta scaling law

\[
 \boxed{k_m(x)=m^{-1/2}k_1(x+\log m).}                \tag{2}
\]

Let (S_a f(x)=f(x+a)), and define on the orbit of (k_1)

\[
 Z=\sum_{m\geq1}m^{-1/2}S_{\log m},
 \qquad
 M=\sum_{d\geq1}\mu(d)d^{-1/2}S_{\log d}.             \tag{3}
\]

The double-exponential decay of (k_1(x+\log n)) makes every series below
absolutely convergent, locally uniformly for (x\geq0), even after any
fixed number of logarithmic weights has been inserted.

### Theorem 1 — Spatial Möbius--theta inversion

For (x\geq0),

\[
 \boxed{Zk_1=K,\qquad MK=k_1.}                         \tag{4}
\]

#### Proof

The first equality is (1)--(2).  For the second, absolute convergence
allows divisor regrouping:

\[
 \begin{aligned}
 (MK)(x)
 &=\sum_{d,m\geq1}\frac{\mu(d)}{\sqrt{dm}}
        k_1(x+\log(dm))\\
 &=\sum_{\ell\geq1}\frac{k_1(x+\log\ell)}{\sqrt\ell}
        \sum_{d\mid\ell}\mu(d)=k_1(x).
 \end{aligned}                                         \tag{5}
\]

This is ordinary Möbius inversion, but now as a pointwise identity for
Riemann's actual theta kernel. \(\square\)

## 2. First and second connection jets

Let the scale derivation satisfy

\[
 \delta(m^{-1/2}S_{\log m})
 =\log m\,m^{-1/2}S_{\log m}.                          \tag{6}
\]

Then Dirichlet convolution and (2) give

\[
 \boxed{
 (M\delta Z)k_1
 =\sum_{n\geq2}\Lambda(n)k_n.}                        \tag{7}
\]

Likewise, with

\[
 j_2(n)=(\mu*\log^2)(n)\geq0,
\]

one has

\[
 \boxed{
 (M\delta^2Z)k_1
 =\sum_{n\geq1}j_2(n)k_n.}                            \tag{8}
\]

The operator identity behind (7)--(8) is the Riccati equation

\[
 \delta A+A^2=M\delta^2Z,
 \qquad A=M\delta Z,                                   \tag{9}
\]

already known algebraically in Phase 70.  Equations (4), (7) and (8) are
its new literal realization on the full theta kernel.

## 3. A pointwise curvature inequality

Set

\[
 A_\theta(x)=\sum_{n\geq2}\Lambda(n)k_n(x),
 \qquad
 B_\theta(x)=\sum_{n\geq1}j_2(n)k_n(x).                \tag{10}
\]

### Theorem 2 — Primitive connection bound

For every (x\geq0),

\[
 \boxed{A_\theta(x)^2\leq K(x)B_\theta(x).}            \tag{11}
\]

#### Proof

First note the coefficient inequality

\[
 j_2(n)\geq\Lambda(n)^2.                               \tag{12}
\]

If (n) is not a prime power, the right side is zero and (12) follows
from (j_2(n)\geq0).  If (n=p^a), then

\[
 j_2(p^a)
 =\{a^2-(a-1)^2\}(\log p)^2
 =(2a-1)(\log p)^2\geq(\log p)^2.                     \tag{13}
\]

Since every (k_n(x)>0), weighted Cauchy--Schwarz and (12) give

\[
 \begin{aligned}
 A_\theta(x)^2
 &\leq\left(\sum_nk_n(x)\right)
       \left(\sum_n\Lambda(n)^2k_n(x)\right)\\
 &\leq K(x)B_\theta(x).
 \end{aligned}
\]

This proves (11). \(\square\)

The estimate retains all prime powers and is exactly saturated only when
the logarithmic prime-power mark is constant on the active theta support.
It is a curvature estimate on the primitive cyclic theta vector, not yet
the required inequality for arbitrary spatial increments.

## 4. Why the unrestricted operator lift is false

A direct operator lift of (11) would require positivity of the Hankel-type
kernel

\[
 \mathcal H(m,n)=j_2(mn)-\Lambda(m)\Lambda(n).           \tag{14}
\]

That kernel is already indefinite on one ordinary prime tower.  On the
indices (p,p^2), after division by ((\log p)^2>0), its matrix is

\[
 \begin{pmatrix}
  j_2(p^2)-1&j_2(p^3)-1\\
  j_2(p^3)-1&j_2(p^4)-1
 \end{pmatrix}
 =
 \begin{pmatrix}2&4\\4&6\end{pmatrix}.                \tag{15}
\]

Its determinant is

\[
 \boxed{12-16=-4<0.}                                   \tag{16}
\]

Thus (11) cannot be polarized over arbitrary divisor coefficients.  The
failure is not caused by an abstract Euler model: (15) uses any literal
ordinary prime (p).  A valid lift must exploit the constrained spatial
vectors produced by the four complete channels of 106.38 and must include
Gamma and the polar variance before estimating the sign.

## 5. Exact surviving target

The new identities replace the formal Euler gauge by a concrete theta
gauge:

\[
 K=Zk_1,qquad k_1=MK,qquad
 A_\theta=(M\delta Z)k_1.                               \tag{17}
\]

Accordingly, the remaining construction can be stated without an abstract
semigroup algebra.  One must prove that the four-channel spatial embedding
of the connection satisfies

\[
 \|D_\mu r\|^2
 \leq\|G_\Gamma r\|^2+\|G_{\rm div}r\|^2
      +\|G_{\rm frac}r\|^2+\|G_{\rm ctr}r\|^2,          \tag{18}
\]

using (4), (7)--(11) before any Cauchy--Schwarz in the divisor index.
Theorem 2 supplies the required cyclic curvature, while (16) proves that
the extension must be spatially constrained and jointly completed.

The operator lift (18) is not proved in this note.
