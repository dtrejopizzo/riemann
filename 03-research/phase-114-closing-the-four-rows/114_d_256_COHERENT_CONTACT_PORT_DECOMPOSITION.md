# D.256 — Only the coherent contact port can be exchanged

## Verdict

The degree/contact conservation law of D.247 does not admit a
Potapov--Ginzburg exchange of the whole contact block: the degree port is
one-dimensional, whereas the contact port has one coordinate per active
prime.  The would-be pivot is rectangular.

There is, however, a canonical decomposition.  The degree is exactly the
coherent scalar component of the contact vector.  That one-dimensional
component may be exchanged with the degree port; its orthogonal complement
is a positive contact-defect port of dimension \(|S|-1\).  On the
primitive degree kernel the coherent component vanishes and the entire
contact lies in this defect port.

This is the finite-dimensional port geometry behind the source Hodge
inequality of D.244.  It fixes the only well-typed Potapov/Redheffer
ordering available for the global comparison.

## 1. Torsion-normalized ports

Use D.247(4.1).  For a finite active prime set \(S\), put

\[
 q_p=\sqrt{\log p}\,z_p,
 \qquad q=(q_p)_{p\in S}\in\mathbb C^S.             \tag{1.1}
\]

The contact norm and degree port are

\[
 \|q\|^2=\sum_{p\in S}(\log p)|z_p|^2,
 \qquad d=\sum_{p\in S}\sqrt{\log p}\,z_p
       =\mathbf1^*q.                                \tag{1.2}
\]

Thus the degree is not an independent coordinate of the contact block.  It
is its coherent summation functional.

## 2. Canonical coherent/primitive split

Let \(m=|S|\),

\[
 e_S={1\over\sqrt m}(1,\ldots,1),\qquad
 P_{\rm coh}=e_Se_S^*,\qquad P_{\rm prim}=I-P_{\rm coh}.
\]

Then

\[
 q=q_{\rm coh}+q_{\rm prim},
 \qquad
 q_{\rm coh}={d\over m}\mathbf1,
 \qquad
 \mathbf1^*q_{\rm prim}=0,                         \tag{2.1}
\]

and Pythagoras gives

\[
 \boxed{
 \|q\|^2={|d|^2\over m}+\|q_{\rm prim}\|^2.
 }                                                   \tag{2.2}
\]

The normalized coherent coordinate

\[
 d_{\rm coh}:={d\over\sqrt m}=e_S^*q              \tag{2.3}
\]

is unitarily equivalent to the range of \(P_{\rm coh}\).  Hence it is the
unique scalar contact port that can be exchanged with a scalar degree
port by an ordinary block pivot.

The conservation-law degree coordinate is \(d\), not \(d_{\rm coh}\).
Their norms differ by the exact factor \(m\):

\[
 |d|^2-\|q_{\rm coh}\|^2
 =\left(1-{1\over m}\right)|d|^2.                 \tag{2.4}
\]

Thus the coherent pivot is invertible but not an isometric identification
of the two scalar ports when \(m>1\).  The surplus (2.4) is the single
Lorentzian degree direction.  It vanishes on the primitive degree kernel
and must remain explicit in any Potapov--Ginzburg calculation.

## 3. Rectangular-pivot obstruction

Any block system attempting to exchange the scalar degree input with the
full contact output would require an invertible pivot

\[
 D:\mathbb C_{\rm degree}\longrightarrow\mathbb C^S_{\rm contact}.
                                                               \tag{3.1}
\]

For \(m>1\), every such map has rank at most one and cannot be invertible
or surjective.  Therefore the full Potapov--Ginzburg transform is not
defined on these port spaces.

After the decomposition (2.1), the coherent pivot has type

\[
 D_{\rm coh}:\mathbb C_{\rm degree}longrightarrow
              \mathbb C e_S,                       \tag{3.2}
\]

and may be inverted when its scalar coefficient is nonzero.  The
orthogonal contact space

\[
 \mathcal C_S^0:=\ker\mathbf1^*,\qquad
 \dim\mathcal C_S^0=m-1,                            \tag{3.3}
\]

must remain an external defect output.

The scalar coefficient includes the normalization \(d\mapsto d/\sqrt m\).
Consequently port exchange also produces the degree surplus (2.4); it may
not be discarded as a harmless normalization.

## 4. Primitive conservation law

The D.247 conservation identity is

\[
 \|\widetilde{\mathcal E}_-z\|^2+|d|^2
 =\|\widetilde{\mathcal E}_+z\|^2+\|q\|^2.        \tag{4.1}
\]

If \(d=0\), then \(q=q_{\rm prim}\) and

\[
 \boxed{
 \|\widetilde{\mathcal E}_-z\|^2
 -\|\widetilde{\mathcal E}_+z\|^2
 =\|q_{\rm prim}\|^2.
 }                                                   \tag{4.2}
\]

This is the exact positive defect and strict equality statement on the
finite prime tangent space.  It is not produced by shorting a rectangular
pivot; it is what remains after the only coherent scalar port has been
set to zero.

## 5. Correct feedback order

The prime-side feedback must therefore be organized as follows:

1. form the complete matrix-valued contact vector \(q\);
2. split \(q=q_{\rm coh}\oplus q_{\rm prim}\);
3. exchange only \(q_{\rm coh}\) with the normalized degree scalar;
4. retain \(q_{\rm prim}\) as a positive defect output;
5. couple the exchanged scalar to the dual-central/Gamma channel;
6. only then impose the two global Tate equations and position support;
7. compare the resulting old/born short with D.190.

The order is forced by dimensions and by (4.2).  Closing the degree port
before forming the coherent contact sum loses the \((m-1)\)-dimensional
defect.

## 6. What remains

The decomposition above is in prime coefficient space.  The carrying
theorem must prove that its coherent scalar is the scalar port appearing
in the semilocal dual-central/Gamma realization and that the transported
\(q_{\rm prim}\) Gram equals the contact part of the D.190 Schur residual
after support and old-core shorting.

## 7. Classification

* Degree as coherent contact functional (1.2): **PROVED IDENTITY**.
* Orthogonal split and defect (2.1)--(2.2): **PROVED**.
* Coherent degree surplus (2.4): **PROVED**.
* Full degree/contact pivot for \(|S|>1\): **IMPOSSIBLE BY DIMENSION**.
* Coherent scalar pivot plus primitive contact defect: **CONSTRUCTED**.
* Primitive finite-prime conservation (4.2): **PROVED**.
* Transport to semilocal support/Gamma and D.190: **OPEN**.
* Row D: **OPEN**.
