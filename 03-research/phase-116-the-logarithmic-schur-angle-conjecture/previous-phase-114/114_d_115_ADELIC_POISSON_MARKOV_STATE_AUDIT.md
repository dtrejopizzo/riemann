# D.115 — The adelic Poisson state and the logarithmic-contact obstruction

## Status

The diagonal embedding of \(\mathbb Q\) in the additive adeles produces a
canonical non-product positive functional (a state/weight on the relevant
Schwartz domain).  It is self-dual under adelic Fourier
transform, invariant under rational scaling by the product formula, and its
two boundary functionals are exactly evaluation at zero and Fourier
evaluation at zero.  Thus it supplies the right Poisson coupling and the
right two Tate jets without using \(B_{\rm nuc}\).

This state does not give the required adelic conditional expectation.
Poisson periodization is continuous on Schwartz--Bruhat/nuclear Fréchet
spaces but is not a bounded \(L^2\) map, hence not a norm-one conditional
expectation.  Averaging over \(\mathbb Q^\times\) has no normalized Haar
probability.  The positive covariance of the Poisson comb yields divisor
counts; the von Mangoldt contact appears only after applying the
logarithmic derivative \(Z\partial Z^{-1}\), which is not a positive or
Markov operation.

Meyer's quotient resolves these facts topologically and gives the exact
nuclear supercharacter, including Gamma.  It does not provide a Hilbert
metric on the odd quotient.  Promoting the Poisson quotient to a
reflection-positive closed Hilbert quotient with the required character is
precisely the remaining unitarizability/Hodge problem; its primitive
two-point positivity is D.

No zeta zero or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Adelic convolution algebra and Poisson state

Let \(\mathbb A=\mathbb A_{\mathbb Q}\) be the additive adele ring, equipped
with its self-dual Haar measure and standard self-dual additive character.
Let \(\mathcal S(\mathbb A)\) be the Schwartz--Bruhat convolution algebra,
with

\[
 f^*(x)=\overline{f(-x)}.                               \tag{1.1}
\]

The diagonal copy of \(\mathbb Q\) is discrete and cocompact in
\(\mathbb A\).  Define

\[
 \omega_{\mathbb Q}(f)=\sum_{q\in\mathbb Q}f(q).       \tag{1.2}
\]

Poisson summation and \(\widehat{f*f^*}=|\widehat f|^2\) give

\[
 \boxed{
 \omega_{\mathbb Q}(f*f^*)
 =\sum_{q\in\mathbb Q}|\widehat f(q)|^2\geq0.}         \tag{1.3}
\]

Thus \(\omega_{\mathbb Q}\) is a positive, non-product functional on the
Schwartz convolution algebra (and defines the corresponding GNS weight on
its natural domain).  Its GNS seminorm is

\[
 \|f\|_{\omega}^2=\sum_{q\in\mathbb Q}|\widehat f(q)|^2.             \tag{1.4}
\]

It couples all local components through one rational lattice; it is not the
independent product state of D.114.

## 2. Reflection, product formula and the two jets

The Real reflection is

\[
 (\Theta f)(x)=\overline{f(-x)}.                        \tag{2.1}
\]

Fourier transform exchanges convolution and multiplication and preserves
the comb because \(\mathbb Q\) is its own annihilator.  For
\(a\in\mathbb Q^\times\), multiplication permutes the diagonal rational
lattice.  The adelic product formula

\[
 \prod_v|a|_v=1                                         \tag{2.2}
\]

shows that this action has module one on \(\mathbb A\).  Hence it acts
unitarily in the GNS representation of (1.2).

The two Poisson boundary maps are

\[
 j_0(f)=f(0),\qquad j_1(f)=\widehat f(0)=\int_{\mathbb A}f(x)\,dx.   \tag{2.3}
\]

The intrinsic Poisson core is

\[
 \mathcal S(\mathbb A)_0=ker j_0\cap\ker j_1.          \tag{2.4}
\]

After passing to the radial/scaling realization, these are the two Tate
characters \(\widehat h(0)\) and \(\widehat h(1)\) already identified in
A--B--C.

## 3. Periodization is not a conditional expectation

The additive periodization map is

\[
 (\mathcal Pf)(x)=\sum_{q\in\mathbb Q}f(x+q),qquad
 x\in\mathbb A/\mathbb Q.                              \tag{3.1}
\]

It is continuous on Schwartz--Bruhat spaces.  Fourier series on the compact
quotient give

\[
 \|\mathcal Pf\|_{L^2(\mathbb A/\mathbb Q)}^2
 =\sum_{q\in\mathbb Q}|\widehat f(q)|^2.                \tag{3.2}
\]

The sampling map in (3.2) is not bounded from \(L^2(\mathbb A)\).  The
obstruction is already visible in the archimedean factor.  Let

\[
 \phi(u)=\max(1-|u|,0),\qquad \|\phi\|_2^2={2\over3},   \tag{3.3}
\]

and, for \(0<\varepsilon<1/2\), prescribe

\[
 \widehat f_{N,\varepsilon}(\xi)
 =\sum_{k=1}^N\phi\left({\xi-k\over\varepsilon}\right).              \tag{3.4}
\]

The supports are disjoint, so

\[
 \|f_{N,\varepsilon}\|_2^2
 ={2\over3}N\varepsilon,qquad
 \sum_{k\in\mathbb Z}|\widehat f_{N,\varepsilon}(k)|^2=N.           \tag{3.5}
\]

The squared norm ratio is \(3/(2\varepsilon)\), which is unbounded.  Taking
the standard compact-open finite adelic factor embeds this example in
\(\mathbb A\).

Therefore \(\mathcal P\) is not an \(L^2\)-bounded map and cannot be a
norm-one conditional expectation.  Equivalently, nonzero
\(\mathbb Q\)-periodic functions lifted from \(\mathbb A/\mathbb Q\) have
infinite \(L^2(\mathbb A)\)-norm, so there is no nonzero invariant Hilbert
subspace onto which one could orthogonally project inside \(L^2(\mathbb A)\).

The multiplicative quotient has the analogous problem:
\(\mathbb Q^\times\) is an infinite discrete group and has no normalized
averaging probability.  The norm-one conditional expectation postulated in
D.114 is therefore not supplied by quotienting by \(\mathbb Q^\times\).

## 4. Positive Poisson covariance gives divisor counts, not contact

Let

\[
 Z=\sum_{n\geq1}U_n=prod_p(1-U_p)^{-1}                \tag{4.1}
\]

be the radial Poisson/Zeta operator.  Its positive Gram \(Z^*Z\), or the
convolution square of its coefficient sequence, counts factorizations and
common multiples.  At the formal Dirichlet-series level,

\[
 \left(\sum_{n\geq1}n^{-s}\right)^2
 =\sum_{n\geq1}d(n)n^{-s}.                              \tag{4.2}
\]

For example

\[
 d(6)=4,qquad \Lambda(6)=0.                            \tag{4.3}
\]

Thus the positive comb covariance has the wrong local contact.

The correct contact is obtained from the logarithmic derivative

\[
 Z\partial Z^{-1}
 =\sum_{n\geq2}\Lambda(n)U_n.                           \tag{4.4}
\]

Although all coefficients \(\Lambda(n)\) are nonnegative, the operation
\(Z\mapsto Z\partial Z^{-1}\) is neither completely positive nor a
conditional expectation.  It is a derivation followed by multiplication
by an inverse.  Positivity of the original state (1.2) does not pass through
(4.4).

This is the exact point where prime contact enters and Markov positivity is
lost.

## 5. Poisson quotient and Gamma

In the radial nuclear Fréchet model, let \(\mathcal H_+\) be the even
Schwartz space and

\[
 \mathcal H_\cap={f:f(0)=\mathcal Ff(0)=0\}.           \tag{5.1}
\]

Meyer's Poisson theorem gives a continuous map

\[
 Z:\mathcal H_+\longrightarrow\mathcal H_\cup          \tag{5.2}
\]

with closed range in the declared nuclear Fréchet topology, and

\[
 Zf\in\mathcal H_-\quad\Longleftrightarrow\quad
 f\in\mathcal H_\cap.                                  \tag{5.3}
\]

The quotients

\[
 \mathcal H_+^0\simeq\mathbb C(x^0)\oplus\mathbb C(x^1),
 \qquad
 \mathcal H_-^0=\mathcal H_-/Z\mathcal H_\cap          \tag{5.4}
\]

produce the exact nuclear supercharacter.  The Fourier commutator supplies
the normalized Gamma finite part.

This is a topological exact quotient, not an orthogonal Hilbert quotient.
The positive comb seminorm (1.4) does not vanish on
\(Z\mathcal H_\cap\), so it does not descend to (5.4).  At the critical
Hilbert norm, the corresponding Poisson range is not promoted by the
construction to a closed complemented subspace with a norm-one projection.
Thus no conditional expectation on \(\mathcal H_-^0\) follows from (5.2).

## 6. Covariance of the quotient

Before taking a logarithmic derivative, the GNS covariance is the positive
rational-sampling form (1.4).  After the three commutator traces used in
row C -- finite orientation, opposite orientation and Fourier/Gamma -- the
supercharacter is the explicit-formula distribution

\[
 I_\Delta^{\rm nuc}(h).
\]

Its polarization is \(B_{\rm nuc}\).  Hence the exact prime--Gamma
covariance is obtained as a **supertrace of a quotient**, not as the
covariance of the positive state (1.2).

If one equips the odd quotient in (5.4) with a positive Hilbert metric for
which scaling is unitary and the supertrace remains the same, then on the
two-jet primitive sector

\[
 -B_{\rm nuc}(F,G)
\]

would be its Gram/character form.  Its positivity is exactly row D.  Thus
the missing step is the unitarizability and closed Hilbert realization of
the Poisson cokernel, not the adelic Poisson identity itself.

## 7. Why product-formula conditioning is insufficient

Conditioning an independent Gaussian product state on \(r\) linear product
formula constraints changes its covariance by an operator of rank at most
\(r\):

\[
 K_{\rm cond}=K-KL^*(LKL^*)^{-1}LK.                    \tag{7.1}
\]

For the two Tate conditions, \(r=2\).  On their common kernel the correction
in (7.1) vanishes.  It therefore cannot create the infinite-rank
prime--Gamma cancellation required on the primitive space.

The rational Poisson comb avoids this rank-two defect because it is an
infinite lattice coupling.  But Sections 3--6 show that its periodization
is nuclear/Fréchet rather than a Hilbert conditional expectation, and that
its positive covariance is changed by the nonpositive logarithmic
derivative before becoming the required contact.

## 8. Precise geometric obstruction

The sought construction would require all four properties simultaneously:

1. a positive adelic GNS state coupling the places;
2. a norm-one quotient/conditional expectation by the rational scaling
   relation;
3. compatibility with logarithmic contact \(Z\partial Z^{-1}\) and the
   Fourier/Gamma commutator;
4. descent of the resulting Hilbert metric to the two-jet Poisson cokernel.

The Poisson state proves (1).  Meyer proves the nuclear exact analogue of
(2)--(4) and the required character.  The failures are:

\[
 \boxed{
 \text{periodization is not }L^2\text{-bounded},\qquad
 Z\partial Z^{-1}\text{ is not positive},\qquad
 \text{the comb norm does not descend to the cokernel}.}
\]

A new geometric Hilbert norm making the quotient closed and the
logarithmic contact a contractive Markov covariance would close D.  Defining
that norm by \(-B_{\rm nuc}\) is circular; deriving it from an independent
adelic correspondence or modular state is the remaining target.
