# 107.194 -- A prime orbit alone cannot carry the published secondary current

## 1. Actual prime orbit geometry

For every rational prime \(p\), Deninger's closed orbit is

\[
 C_p=\mathbb R/(\log p)\mathbb Z
\]

with translation flow

\[
 \phi^t(x)=x+t.
 \tag{1.1}
\]

This is the real geometry used in `107_185`; it is not a toy model.
Its twisted rank-one operator \(d/dx+s\) has determinant
\(1-p^{-s}\).

## 2. Fixed loci of the translation

Equation (1.1) gives

\[
 \mathrm{Fix}(\phi^t)=
 \begin{cases}
  \varnothing,&t\notin(\log p)\mathbb Z,\\
  C_p,&t\in(\log p)\mathbb Z.
 \end{cases}
 \tag{2.1}
\]

At a return time \(t=k\log p\), the derivative is the identity:

\[
 D\phi^t=1,\qquad 1-D\phi^t=0.
 \tag{2.2}
\]

Thus the orbit itself supplies neither an isolated nondegenerate fixed
point nor a nontrivial normal character.  The factor \(1-p^{-s}\) in
the twisted determinant comes from coefficient holonomy, not from the
tangent Euler class of a fixed-point embedding.

## 3. Complex-geometry obstruction

The Bismut--Goette current used in the arithmetic residue formula of
Koehler--Roessler is defined on a compact complex/Kahler manifold with a
holomorphic isometric torus action.  It uses the complex tangent bundle,
the normal bundle of the fixed manifold, equivariant characteristic
forms, and integration of differential forms of complex bidegree.

The circle \(C_p\) has real dimension one.  It admits no almost-complex
structure: an endomorphism \(J\) of a one-dimensional real tangent
space cannot satisfy \(J^2=-1\).  Hence it cannot be a complex or
Kahler manifold and cannot supply the bundles and forms entering that
secondary current.

**Theorem.**  The published Koehler--Roessler/Bismut--Goette secondary
current cannot be instantiated directly on an isolated Deninger prime
orbit \(C_p\).  Replacing its twisted determinant by that current is
therefore invalid without an ambient complex transverse geometry.

**Proof.**  The parity argument excludes the required complex/Kahler
structure.  Independently, (2.1)--(2.2) show that the translation has
either no fixed locus or the entire orbit with trivial tangent action,
so the missing inverse Euler class cannot arise from an orbit-normal
fixed-point denominator. \(\square\)

## 4. What survives

This does not invalidate `107_185`.  The one-dimensional twisted
determinant and Green kernel are well defined and recover the finite
Euler channel.  It says only that this odd-dimensional spectral
determinant is not already the even-dimensional equivariant
analytic-torsion current required by arithmetic Lefschetz theory.

Nor does the theorem exclude an ambient foliated or noncommutative
phase space whose closed orbit has a complex transverse normal bundle.
Such an ambient object would need to provide, and verify:

1. an even-dimensional complex/Kahler transverse complex;
2. a torus action extending the return dynamics;
3. a fixed or clean-intersection normal bundle with the correct
   character;
4. a comparison of its secondary current with the orbit determinant.

None of these data is produced by the product semilocal sheaf of
`107_190`.

## 5. Falsifier

The verifier consumes the real prime atlas \(2,3,5,7,11\).  For every
orbit it tests nonreturn and return times, derivative degeneracy,
positive-dimensional return fixed loci, and the simultaneous
nonvanishing of the actual twisted holonomy determinant for
\(\Re(s)>1\).  A mutation replacing translation derivative \(1\) by a
contracting normal derivative must be detected as different geometry.
