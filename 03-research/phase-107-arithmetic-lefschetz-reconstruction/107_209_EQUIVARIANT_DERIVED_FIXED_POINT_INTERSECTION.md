# 107.209 -- The Euler factor is an equivariant derived self-intersection

## 1. Geometry before the nonproper quotient

Let \(Y=\mathbb A^1_{\mathbb C}\) be the archimedean-local point space
of `107_207`, let \(i:Z=\{0\}\hookrightarrow Y\), and let the scaling
operator act on functions by

\[
 T_qf(z)=f(qz),\qquad q=p^{-s}.
 \tag{1.1}
\]

The conormal line

\[
 L=\mathfrak m/\mathfrak m^2
 \tag{1.2}
\]

has character \(\chi(q)=q\).  This is the intrinsic line isolated in
`107_207`.

## 2. Derived self-intersection

The regular embedding has the equivariant Koszul resolution

\[
 0\longrightarrow \mathcal O_Y\otimes L
 \xrightarrow{\ z\ }\mathcal O_Y
 \longrightarrow i_*\mathcal O_Z\longrightarrow0,
 \tag{2.1}
\]

with the linearization chosen according to (1.1).  Pulling back
derivedly to \(Z\) makes the differential zero and gives

\[
 \operatorname{Tor}^{\mathcal O_Y}_0(\mathcal O_Z,\mathcal O_Z)
 =\mathcal O_Z,
 \qquad
 \operatorname{Tor}^{\mathcal O_Y}_1(\mathcal O_Z,\mathcal O_Z)=L.
 \tag{2.2}
\]

Hence in equivariant \(K\)-theory

\[
 \boxed{
 i^*i_*[\mathcal O_Z]
 =\lambda_{-1}(L)
 =1-[L].}
 \tag{2.3}
\]

Evaluating the character at the prime twist gives

\[
 \operatorname{ch}_{p,s}(i^*i_*1)=1-p^{-s}.
 \tag{2.4}
\]

This is exactly the local inverse Euler factor, the relative Fock
determinant of `107_196`, the balanced Dirac block determinant of
`107_199`, and the fixed-germ normal determinant of `107_207`.

### Theorem 2.1 (local intersection realization)

The Phase 107 local factor \(1-p^{-s}\) is the character of an actual
equivariant derived self-intersection class on the Connes--Consani
archimedean-local point space.  It is defined before taking the
non-\(T_1\) quotient rejected in `107_208`.

## 3. Coordinate invariance and Green trace

The class (2.3) depends only on the regular embedding and its conormal
line.  Under every coordinate change \(w=uz+O(z^2)\), \(u\ne0\), the
line \(\mathfrak m/\mathfrak m^2\) and its character \(q\) are
unchanged.  Thus (2.4) is intrinsic.

Taking the logarithmic derivative of the inverse Euler class gives

\[
 -{d\over ds}\log(1-p^{-s})
 =-\log p\,{p^{-s}\over1-p^{-s}},
 \tag{3.1}
\]

while the determinant convention of `107_196` uses the positive
derivative

\[
 {d\over ds}\log(1-p^{-s})
 =\log p\,{p^{-s}\over1-p^{-s}}.
 \tag{3.2}
\]

Thus the \(\log p\) weight comes from differentiating the scale
character; it is not inserted as an intersection multiplicity.

## 4. Scope and the remaining global obstruction

This is the first genuine intersection class in the new local
CC/Deninger chain: it is a derived, equivariant self-intersection, not a
prescribed scalar table.  It survives the ordinary-quotient no-go
because it is formed before quotienting.

It does not yet provide:

1. a proper pushforward or numerical degree for (2.3);
2. a global sum over all prime fixed germs in one finite-type object;
3. the Gamma/pole class in the same equivariant \(K\)-category;
4. a diagonal/correspondence pairing on an arithmetic square;
5. packet/Galois sensitivity or the component data ruled necessary by
   legacy row (c);
6. a Hodge theorem.

The next exact target is no longer “find a local intersection.”  It is
to construct a legitimate trace/pushforward of the classes (2.3) whose
logarithmic character is Meyer's nuclear finite-place distribution,
without passing through the nonproper coarse quotient.

## 5. Falsifier

`107_209_equivariant_derived_fixed_point_intersection.py` computes the
two Tor characters, their alternating class, nonlinear jet conjugacies,
and the logarithmic derivative on five actual primes.  It rejects an
ordinary underived pullback, which would retain only \(1\) and miss the
Euler factor.

