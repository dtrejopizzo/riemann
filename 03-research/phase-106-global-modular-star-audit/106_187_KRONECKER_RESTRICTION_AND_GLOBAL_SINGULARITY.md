# 106.187 — Kronecker restriction and global spectral singularity

## 1. Purpose

The Euler--Bohr kernel of 106.186 and the Cauchy path kernel of 106.154
agree on every individual prime tower but disagree globally.  This note
identifies the comparison map and proves its exact analytic status.

The map is restriction from the infinite prime torus to the real
Kronecker orbit.  It is algebraically defined and equivariant on
trigonometric polynomials.  Nevertheless it is not closable between the
two natural positive Hilbert spaces, because their spectral measures are
mutually singular.  Thus the missing descent cannot be a bounded or
closable Hilbert comparison of the already positive coefficient modules.
It must be a relative/renormalized trace operation before Hilbert
completion.

## 2. The two spectral measures on the prime torus

Retain

\[
 G=\log\mathbb Q_+^\times,qquad
 \widehat G=\prod_p\mathbb T,                                \tag{1}
\]

and the Euler product measure

\[
 \mu_E=\bigotimes_p\mu_{p^{-1/2}}.                           \tag{2}
\]

Let \(\nu_C\) be the centered Cauchy probability measure on \(\mathbb R\)
with characteristic function

\[
 \int_{\mathbb R}e^{it\xi}\,d\nu_C(\xi)=e^{-|t|/2}.         \tag{3}
\]

Define the Kronecker embedding

\[
 \kappa:\mathbb R\longrightarrow\widehat G,qquad
 \kappa(\xi)_p=p^{i\xi}.                                    \tag{4}
\]

Unique factorization and irrationality of \(\log p/\log r\) for distinct
primes show that \(\kappa\) is injective.  Put

\[
 \mu_C=\kappa_*\nu_C.                                       \tag{5}
\]

For \(g=\log q\in G\), its Fourier coefficient is

\[
 \widehat\mu_C(g)
 =\int q^{i\xi}\,d\nu_C(\xi)
 =e^{-|\log q|/2}.                                          \tag{6}
\]

Thus \(\mu_C\) is exactly the spectral measure of the continuous Cauchy
scale coefficient, viewed on the same compact dual as \(\mu_E\).

## 3. Local agreement

Let \(G_p=\mathbb Z\log p\).  Restriction of both measures to the quotient
dual detected by \(G_p\) has Fourier coefficients

\[
 \widehat\mu_E(k\log p)
 =p^{-|k|/2}
 =\widehat\mu_C(k\log p).                                   \tag{7}
\]

### Proposition 3.1 — Exact primewise equality

For every prime \(p\), the pushforwards of \(\mu_E\) and \(\mu_C\) to
\(\widehat{G_p}\simeq\mathbb T\) coincide with the Poisson measure
\(\mu_{p^{-1/2}}\).

#### Proof

Equation (7) gives equality of every Fourier coefficient of the two
probability measures on \(\mathbb T\).  Fourier uniqueness proves the
claim. \(\square\)

This recovers, in one statement, the exact agreement of all local
prime-power masses established in 106.153--106.154.

## 4. Global mutual singularity

Write

\[
 \mathcal C=\kappa(\mathbb R)\subset\widehat G.              \tag{8}
\]

The set \(\mathcal C\) is Borel: \(\kappa\) is a continuous injection
between Polish spaces, so the Lusin--Souslin theorem applies.

### Theorem 4.1 — Primewise equality, global singularity

\[
 \boxed{\mu_C(\mathcal C)=1,
 \qquad \mu_E(\mathcal C)=0.}                               \tag{9}
\]

Consequently \(\mu_C\perp\mu_E\).

#### Proof

The first equality follows from (5).  For the second, retain only the
coordinates at \(2\) and \(3\).  Conditional on a value
\(z_2=e^{i\theta_2}\), a point on \(\mathcal C\) must have

\[
 \xi=\frac{\theta_2+2\pi k}{\log2},qquad k\in\mathbb Z.     \tag{10}
\]

Its \(3\)-coordinate must therefore belong to the countable set

\[
 \left\{
  \exp\!\left(i\frac{\theta_2+2\pi k}{\log2}\log3\right):
  k\in\mathbb Z
 \right\}.                                                   \tag{11}
\]

Under \(\mu_E\), the coordinates \(z_2,z_3\) are independent and the
Poisson measure \(\mu_{3^{-1/2}}\) is atomless.  Hence the conditional
probability of (11) is zero for every \(z_2\).  Fubini gives
\(\mu_E(\mathcal C)=0\). \(\square\)

The theorem is stronger than the discontinuity found in 106.186.  The
two positive realizations share every one-prime marginal while having no
common global spectral mass.

## 5. The algebraic comparison map

For a trigonometric polynomial \(F\) on \(\widehat G\), define

\[
 \boxed{
 (\mathcal RF)(\xi)=F(\kappa(\xi))
 =F((p^{i\xi})_p).}                                         \tag{12}
\]

Identifying \(L^2(\mathbb R,\nu_C)\) with
\(L^2(\widehat G,\mu_C)\), this is the identity map on the common
algebra of trigonometric polynomials, viewed between two different
\(L^2\) completions:

\[
 \mathcal R:
 \mathrm{Trig}(\widehat G)\subset L^2(\mu_E)
 \longrightarrow L^2(\mu_C).                               \tag{13}
\]

It intertwines the multiplication representation of \(G\) and agrees
with the local identifications of Proposition 3.1.

### Lemma 5.1 — Closability criterion for change of measure

Let \(X\) be compact, let \(\mu,\nu\) be finite Radon measures, and let a
unital self-adjoint algebra \(\mathcal A\subset C(X)\) be uniformly dense.
The identity operator

\[
 I:\mathcal A\subset L^2(\mu)\longrightarrow L^2(\nu)       \tag{14}
\]

is closable if and only if \(\nu\ll\mu\).  When it is closable, its
closure is multiplication by the square root of the Radon--Nikodym
density in the standard common-measure realization.

#### Proof

If \(\nu\ll\mu\), the graph closure is the usual closed inclusion on the
domain \(\{f\in L^2(\mu):f\in L^2(\nu)\}\).

Conversely, suppose \(I\) is closable.  Its adjoint must be densely
defined in \(L^2(\nu)\).  For \(h\in\mathcal D(I^*)\), there is
\(k\in L^2(\mu)\) such that

\[
 \int_X f\overline h\,d\nu
 =\int_X f\overline k\,d\mu\qquad(f\in\mathcal A).         \tag{15}
\]

Density of \(\mathcal A\) in \(C(X)\) makes the measures
\(\overline h\nu\) and \(\overline k\mu\) equal, so
\(h=0\) \(\nu\)-almost everywhere on every \(\mu\)-null set.  Since
\(\mathcal D(I^*)\) is dense, the indicator of any \(\mu\)-null set must
vanish in \(L^2(\nu)\).  Thus \(\nu\ll\mu\). \(\square\)

### Theorem 5.2 — The Kronecker restriction is not closable

The operator (13) is not closable.

#### Proof

Trigonometric polynomials form a unital self-adjoint algebra separating
points of the compact group \(\widehat G\), hence are uniformly dense by
Stone--Weierstrass.  Lemma 5.1 applies.  Theorem 4.1 gives
\(\mu_C\perp\mu_E\), so in particular \(\mu_C\not\ll\mu_E\). \(\square\)

## 6. Interpretation as the missing arithmetic trace theorem

The operator \(\mathcal R\) is the exact global comparison suggested by
the local coefficient modules:

* on each prime coordinate it is isometric after identifying the common
  Poisson marginal;
* it is equivariant on its algebraic core;
* it carries the complete multiplicative phase vector to the real
  scaling orbit.

But it is a restriction to a measure-zero Kronecker curve.  Therefore it
cannot descend by ordinary Hilbert completion.  This gives a concrete
meaning to the phrase ``torsion-sensitive descent'': one needs a trace
operation which is defined on a stronger source domain than
\(L^2(\mu_E)\), admits the Gamma/polar boundary correction, and becomes
closable only after passing to the relative degree-one complex.

A finite-dimensional approximation makes the analytic price visible.
For the first \(m\ge2\) primes, restriction is from an \(m\)-dimensional
torus to a one-dimensional Kronecker curve.  A Sobolev trace requires more
than \((m-1)/2\) transverse derivatives.  Since \(m\to\infty\), no fixed
finite Sobolev order can make the infinite-prime restriction bounded.
Any successful domain must therefore have anisotropic or nuclear
regularity increasing with the prime support.

## 7. Consequence for the polarization programme

The alternative majorant of 106.184 does not require a literal arithmetic
surface, but it cannot be obtained from a bounded comparison of the two
positive coefficient spaces.  The exact remaining analytic construction
is now:

> Build a nuclear, prime-support-sensitive domain \(\mathscr D_E\) in the
> Euler--Bohr space and a Gamma/polar corrected restriction
> \(\mathcal R_{\rm rel}\) whose graph is closed, whose degree-one
> cokernel is the nonreduced CCM object, and whose Green boundary form
> represents \(\Omega\) by a boundedly invertible skew-adjoint operator.

This is an analytic replacement for an intersection product on the
arithmetic square.  It is more specific than asking for a factorization
of the Weil form: the algebraic map, its two endpoint measures, and its
failure of closability are all explicit before any zero input.

## 8. Status

Proved without RH or zero input:

* exact equality of the Euler and Cauchy realizations on every prime
  subgroup;
* global mutual singularity of their spectral measures;
* the explicit Kronecker restriction map relating them algebraically;
* failure of closability of that map in the natural positive Hilbert
  norms;
* divergence of the finite-dimensional Sobolev trace order with the
  number of primes.

Still required:

* a nuclear anisotropic domain and a relative Gamma/polar correction that
  make the restriction closable in derived degree one;
* faithful identification of that degree one with the CCM cokernel and
  strong nondegeneracy of its alternating form.
