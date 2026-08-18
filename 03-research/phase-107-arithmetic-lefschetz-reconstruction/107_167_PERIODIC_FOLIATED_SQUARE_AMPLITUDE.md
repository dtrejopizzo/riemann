# 107.167 -- Surface amplitude on the periodic foliated square

## 1. Published input

For every rational prime \(p\), Connes--Consani construct the compact
mapping torus \(\Gamma(p)\) in their complex lift of the Scaling Site.
Its leaves are one-dimensional complex manifolds.  Proposition 5.7 of
*The Riemann--Roch strategy* proves that the canonical projection

\[
 \Gamma(p)\longrightarrow
 \mathbb R_+^\times/p^\mathbb Z\cong S^1
 \tag{1.1}
\]

is an isomorphism in de Rham cohomology.  Their proof is explicit: the
zero Fourier orbit gives the circle complex, while every nonzero
\(p^\mathbb Z\)-orbit is contracted by the inverse of the leafwise
operator \(X\).

Consequently

\[
 H^k_{\rm dR}(\Gamma(p))\cong
 \begin{cases}
 \mathbb C,&k=0,1,\\
 0,&k\ge2.
 \end{cases}
 \tag{1.2}
\]

## 2. Product theorem

**Theorem.**  For any primes \(p,q\), the periodic product
\(\Gamma(p)\times\Gamma(q)\) has de Rham cohomology

\[
 \dim H^k_{\rm dR}(\Gamma(p)\times\Gamma(q))
 =(1,2,1)_k,
 \tag{2.1}
\]

and vanishes for \(k>2\).

**Proof.**  The complexes used in Proposition 5.7 split into the circle
subcomplex and contractible nonzero-orbit summands.  Tensoring the two
splittings leaves only the tensor product of the circle complexes;
every summand containing a contractible factor remains contractible.
Equivalently, apply Kunneth over \(\mathbb C\) to (1.2):

\[
 H^\bullet_{\rm dR}(\Gamma(p)\times\Gamma(q))
 \cong H^\bullet(S^1;\mathbb C)\otimes
 H^\bullet(S^1;\mathbb C)
 \cong H^\bullet(T^2;\mathbb C).
\]

This gives (2.1). \(\square\)

The two degree-one generators come from the two rulings.  Their exterior
product generates degree two, exactly matching the local cohomological
shape required of a square.

## 3. Comparison with the raw topos

The result is structurally different from 107_166.  On the same finite
prime atlas, raw monoid-derived cohomology has nonzero classes through
degree \(2r\).  The foliated geometry contracts every nonzero Fourier
orbit and retains only one circle direction per geometric factor.
Therefore the amplitude-two reduction is a theorem of the complex lift,
not an arbitrary truncation.

This identifies the geometric source of a three-term complex:

\[
 0\longrightarrow\Omega^0
 \xrightarrow{d}\Omega^1
 \xrightarrow{d}\Omega^2
 \longrightarrow0
\]

on each periodic product.  A Dolbeault version has the same length
because the product leaves have complex dimension two.

## 4. Scope

This proves local periodic amplitude, not the global row-(a) theorem.
Moreover, the de Rham retraction has no degree-four class, so it cannot
by itself support cup-product intersections of divisors; this is proved
in 107_170.  "Surface amplitude" here refers only to the three-term
sheaf/coefficient complex.
It does not establish:

1. a compact global square containing all periodic products;
2. a line bundle realizing \(D(f)\) on that square;
3. finite-dimensional global leafwise cohomology;
4. regularized intersection of diagonal and correspondences;
5. Hirzebruch--Riemann--Roch or tropical descent.

Those are exactly Steps 2--5 left open in the 2018 strategy.  The next
Phase 107 gate is compatibility of the support enrichment of 107_165
and the correspondence kernels of 107_163 with this foliated
three-term complex.

## 5. Falsifier

The verifier uses cellular circle models with actual prime sizes and
computes the ranks of both coboundary matrices of their product over
\(\mathbb Q\).  It must recover \((1,2,1)\) for every fixed pair.  The
calculation can return `NO`; no Betti number is inserted by hand.
