# 107.191 -- The unmetrized spectral line has no ordinary intersection class

## 1. Exact trivialization

Retain the domain

\[
 \mathcal H=\{s\in\mathbb C:\Re(s)>1\}.
\]

For a finite prime set \(S\), the transition of the spectral line of
`107_189` is

\[
 c_{S,T}(s)=\prod_{p\in T\setminus S}z_p(s),
 \qquad z_p(s)=(1-p^{-s})^{-1}.
 \tag{1.1}
\]

With \(g_S=\prod_{p\in S}z_p\), one has

\[
 c_{S,T}=g_Tg_S^{-1}.
 \tag{1.2}
\]

Thus the transition cocycle is the coboundary of the explicit
zero-cochain \((g_S)_S\).  In particular

\[
 \mathscr L\simeq\mathcal O_{\mathcal H}
 \quad\hbox{and}\quad [\mathscr L]=0
 \quad\hbox{in the ordinary Picard group.}
 \tag{1.3}
\]

This is stronger than saying that the restrictions satisfy a cocycle:
the line itself is globally trivial.

## 2. The external product is also trivial

On the product semilocal site, `107_190` has transition

\[
 c_{S,T}^{S',T'}=
 {g_{S'}(s_1)g_{T'}(s_2)\over g_S(s_1)g_T(s_2)}.
 \tag{2.1}
\]

Hence

\[
 \mathscr L^\square
 =\operatorname{pr}_1^*\mathscr L\otimes
  \operatorname{pr}_2^*\mathscr L
 \simeq\mathcal O_{\mathcal H^2}.
 \tag{2.2}
\]

Its diagonal pullback is the trivial tensor square.  Therefore every
ordinary first Chern class satisfies

\[
 c_1(\mathscr L)=c_1(\mathscr L^\square)
 =c_1(\delta^*\mathscr L^\square)=0.
 \tag{2.3}
\]

## 3. The canonical section has no divisor on the coefficient domain

Under the trivialization

\[
 f e_S\longmapsto f/g_S,
\]

the canonical section

\[
 \sigma_S=Z_\infty(s)g_S(s)e_S,
 \qquad
 Z_\infty(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2),
\]

becomes \(Z_\infty(s)\).  This is holomorphic and nowhere zero on
\(\mathcal H\): neither \(s\), \(s-1\), the exponential
\(\pi^{-s/2}\), nor \(\Gamma(s/2)\) vanishes there.  Consequently

\[
 \operatorname{div}_{\mathcal H}(\sigma)=0.
 \tag{3.1}
\]

Likewise the external section becomes
\(Z_\infty(s_1)Z_\infty(s_2)\) and has empty divisor on
\(\mathcal H^2\).

The cofinal expression \(\xi(s)\) uses an infinite Euler
re-trivialization.  It is not a nonzero ordinary Picard class on the
semilocal Zariski site.  In particular the prime factors in (1.1) are
units and are erased by ordinary descent.

## 4. No-go theorem

**Theorem.**  Any proposed square-level intersection constructed from
the objects of `107_189--190` using only:

1. the ordinary Picard class of the unmetrized line;
2. pullback, tensor product, and first Chern class;
3. an ordinary Deligne pairing that is invariant under line-bundle
   isomorphism,

is trivial.  It cannot recover the nonzero prime distribution,
\(-\xi'/\xi\), or the Paper-0 graph--diagonal intersections.

**Proof.**  Equations (1.3) and (2.2) identify every line entering those
operations with the unit object.  Functorial first Chern classes vanish
on the unit object, and a bilinear Deligne pairing with a trivial
unmetrized factor is trivial.  Equation (3.1) also rules out recovering
a cycle from the divisor of the canonical section on \(\mathcal H\).
\(\square\)

## 5. Exact scope

This closes only the **unmetrized ordinary-Picard route**.  It does not
apply to:

1. a trivial line equipped with a nonconstant Arakelov metric;
2. a Green current with logarithmic boundary singularities;
3. a determinant line extended meromorphically across the critical
   strip;
4. a renormalized equivariant or secondary characteristic class.

Those are precisely the places where a trivial algebraic line can carry
nontrivial arithmetic information.  The next construction must therefore
put the orbit kernels of `107_185--186` into a metric/current or
secondary class.  Another unmetrized tensor construction cannot advance
row (c).

## 6. Falsifier

The verifier represents every Euler transition by its exact prime
exponent vector.  It checks that the curve and square cocycles are
coboundaries, that diagonal pullback preserves the trivialization, and
that canonical-section Euler exponents vanish after the gauge change.
It also inserts a corrupted transition and requires the cocycle test to
reject it.  High-precision evaluations certify nonvanishing of the
analytic trivializing section on a fixed real/complex atlas.
