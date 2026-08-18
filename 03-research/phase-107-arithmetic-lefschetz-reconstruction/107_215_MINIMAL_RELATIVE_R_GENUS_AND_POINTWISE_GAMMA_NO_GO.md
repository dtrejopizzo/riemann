# 107.215 -- A minimal relative R-genus exists, but it is not the Gamma channel prime by prime

## 1. Forced cut correction

Retain the notation

\[
 D(z)=\left.\partial_\nu\mathrm{Li}_\nu(z)\right|_{\nu=0}
 \]

from 107_214.  For \(x>1\), with the boundary convention induced by
\(x\pm i0\),

\[
 \mathrm{Disc}\,D(x)={2\pi i\over\log x},
 \qquad
 \mathrm{Disc}\,\log(1-x)=-2\pi i.
 \tag{1.1}
\]

Therefore

\[
 D^{\mathrm{rel}}(x)
 =
 D(x)+{\log(1-x)\over\log x}
 \tag{1.2}
\]

has zero discontinuity across \(x>1\).

Among corrections of the form \(D(x)+c(x)\log(1-x)\), cancellation of
(1.1) forces

\[
 c(x)={1\over\log x}.
 \tag{1.3}
\]

Thus (1.2) is the unique minimal logarithmic cut correction, before
adding an arbitrary function holomorphic across the cut.

## 2. Log-lifted relative anomaly

For \(0<q<1\), define

\[
 R^{\mathrm{rel}}(q)
 =
 D(q)-D^{\mathrm{rel}}(q^{-1}).
 \tag{2.1}
\]

The two lateral values at \(q^{-1}>1\) agree, so (2.1) is real and
single-valued on the positive character ray.  More generally it is
defined on the logarithmic cover once a branch of \(\log q\) is fixed.

### Proposition 2.1

Equation (2.1) constructs the minimal log-lifted scalar boundary
correction of the degree-zero line \(R\)-genus across the nonunitary
prime character.  This assertion is about the two lateral boundary
values on the positive ray; it does not assert a global holomorphic
continuation on the punctured character plane.

This closes the local branch problem left by 107_214.  It does not yet
identify (2.1) with an arithmetic analytic-torsion direct image; that
would require extending the Koehler--Roessler immersion theorem itself,
not only its scalar anomaly.

## 3. Pointwise Gamma comparison fails

Set

\[
 A_p(s)=\log p\,R^{\mathrm{rel}}(p^{-s}).
 \tag{3.1}
\]

The completed archimedean Green channel of 107_186 is

\[
 G_\Gamma(s)
 =-\frac12\psi(s/2)+\frac12\log\pi,
 \tag{3.2}
\]

which depends only on \(s\).  Direct evaluation of (3.1) at fixed
\(s\) gives different values for different primes.

### Theorem 3.1 (pointwise Gamma no-go)

There is no identity

\[
 A_p(s)=G_\Gamma(s)
 \]

valid prime by prime.  The nonunitary arithmetic immersion anomaly does
not equal the Gamma channel locally.

Hence any comparison with (3.2) must include a global operation:
prime summation with a generic/white-light subtraction, a relative
determinant, or Meyer's Poisson-summation quotient.

This comparison is only a scalar-symbol diagnostic.  Meyer's
\(W_\infty\) is a distribution on multiplicative Schwartz tests, whereas
\(A_p(s)\) is an evaluation at a Mellin character; the latter is not an
element of Meyer's test algebra.  No equality of distributions is being
asserted or refuted here.

## 4. Exact status

The local chain is now:

\[
 \text{unitary }R_g
 \longrightarrow
 \text{log-lifted relative }R_g
 \longrightarrow
 \text{real prime anomaly}.
\]

Constructed: the middle arrow and its real boundary value.

Still missing:

1. a theorem identifying it with nonunitary analytic torsion;
2. a convergent/renormalized global sum of \(A_p(s)\);
3. cancellation against the generic point;
4. equality of the resulting global anomaly with Gamma and poles;
5. a primitive Hodge pairing.

## 5. Falsifier

107_215_minimal_relative_r_genus_and_pointwise_gamma_no_go.py tests the
two lateral continuations on five actual primes, verifies reality,
checks the forced correction coefficient, and rejects a primewise
Gamma identity at fixed spectral parameters.
