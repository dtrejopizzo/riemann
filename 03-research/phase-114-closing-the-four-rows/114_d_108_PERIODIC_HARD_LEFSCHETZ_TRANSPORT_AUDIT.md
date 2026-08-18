# D.108 — Periodic hard-Lefschetz transport audit

## Status

Row A contains a genuine numerical Hodge-index form on the completed
external ruling degrees.  Choosing the ample ruling class `H=e_1+e_2`, its
primitive line is negative definite.  This proves the expected
two-dimensional ruling Hodge theorem.

That theorem does not transport to the row-D primitive test space.  The
degree realization has rank two and vanishes on the two-moment primitive
kernel, while `-B_nuc` is an infinite-rank prime--Gamma form there.  The
nuclear correspondence direction `e_Gamma` retains `Lambda(mn)`, but its
half-density-normalized same-prime kernel has rank one.  The required
Poisson/translation kernel depends on the difference of prime-power
depths and has full rank.  Diagonal torsor normalization preserves rank and
cannot repair the mismatch.  The Gamma oscillator is absent from the
numerical ruling adjoint and from the finite `ell` contact.

Thus A supplies the correct finite ruling Hodge index, Kunneth
multiplication and determinant metric, but not a hard-Lefschetz
polarization of Meyer's odd quotient.  Defining the missing adjoint from
`B_nuc` would make the construction circular.

No RH statement or desired infinite-dimensional sign is assumed.  The
paper is not modified.

## 1. Numerical Lefschetz operator in row A

The completed external numerical degree space is

\[
 N^1_{\rm deg}=\mathbb R e_1\oplus\mathbb R e_2,          \tag{1.1}
\]

with intrinsic determinant/intersection form

\[
 B_{\rm int}(x,y)
 =d_1(x)d_2(y)+d_2(x)d_1(y).                              \tag{1.2}
\]

Choose

\[
 H=e_1+e_2.                                               \tag{1.3}
\]

The numerical Lefschetz functional and primitive line are

\[
 L_H(x)=B_{\rm int}(x,H)=d_1(x)+d_2(x),
 \qquad P_H=\ker L_H.                                     \tag{1.4}
\]

If `x` is primitive, `d_2(x)=-d_1(x)`, and therefore

\[
 \boxed{B_{\rm int}(x,x)=-2d_1(x)^2\le0,}                \tag{1.5}
\]

with equality only at zero in `N^1_deg`.  This is the complete numerical
Hodge-index theorem on the ruling quotient.  It follows directly from the
intrinsic periodic determinant metric and does not use row C.

## 2. What the periodic determinant defines

For effective periodic divisors of degrees `(a,b)`, the intrinsic
cohomology has continuous dimension `ab` and determinant metric with
polarization (1.2).  Kunneth multiplication is constructed on the
representable periodic section objects.

These data define:

1. multiplication of effective section objects;
2. cotangent Kunneth frames;
3. a determinant line and its degree Hessian;
4. the numerical functional (1.4).

They do not define a cohomological grading with operators

\[
 L:H^0\to H^2,
 \qquad \Lambda=L^*,                                     \tag{2.1}
\]

on the Meyer quotient `V`.  In particular, no adjoint functor transports
the periodic determinant metric through the Frechet Poisson cokernel.

The only constructed common map from A to C is the nuclear scalar action
and the determinant contact character.  It preserves labels and traces,
not a positive Hilbert adjoint.

## 3. Rank-two degree pullback

Under the central logarithmic realization, the two degree/Tate functionals
are

\[
 M_-(f),\qquad M_+(f).                                    \tag{3.1}
\]

Any form obtained solely by pulling back (1.2) factors through

\[
 f\longmapsto(M_-(f),M_+(f)).                             \tag{3.2}
\]

Consequently it has rank at most two and vanishes identically on

\[
 \mathcal P=\ker M_-\cap\ker M_+.                         \tag{3.3}
\]

By D.32, the form on this same space is

\[
\begin{aligned}
 -B_{\rm nuc}(f,g)={}&
 -\sum_p\log p\sum_{k\ne0}p^{-|k|/2}
       \langle f,S_{k\log p}g\rangle\\
 &-m_0\langle f,g\rangle
 +\langle\partial_\infty f,\partial_\infty g\rangle.    \tag{3.4}
\end{aligned}
\]

It has infinite translation rank and is not identically zero.  Therefore
the numerical Lefschetz form of A cannot pull back to (3.4).

This is not a defect of (1.5): it proves a different, finite numerical
statement which the row-A construction explicitly separates from mixed
correspondences.

## 4. Nuclear correspondence direction

Row A adjoins the free nuclear direction

\[
 \mathcal O_{\mathcal C}e_\Gamma                           \tag{4.1}
\]

with scalar action `rho_n(a e_Gamma)=(delta_n*a)e_Gamma` and contact

\[
 \ell(\delta_m*\delta_n)=\Lambda(mn).                     \tag{4.2}
\]

This is exact for composition.  Central half-density normalization gives
the same-prime-power kernel

\[
 K_{\rm sum}(r,s)
 ={\Lambda(p^{r+s})\over p^{(r+s)/2}}
 =\log p\,p^{-(r+s)/2},
 \qquad r,s\ge1.                                         \tag{4.3}
\]

It is a rank-one outer product.

The row-C Poisson orbit Gram needed for all bilateral correlations is

\[
 K_{\rm diff}(r,s)
 =\log p\,p^{-|r-s|/2}.                                   \tag{4.4}
\]

Already on depths `1,2`, after dividing by `log p`,

\[
 K_{\rm sum}=
 \begin{pmatrix}p^{-1}&p^{-3/2}\\p^{-3/2}&p^{-2}\end{pmatrix},
 \qquad\det K_{\rm sum}=0,                               \tag{4.5}
\]

while

\[
 K_{\rm diff}=
 \begin{pmatrix}1&p^{-1/2}\\p^{-1/2}&1\end{pmatrix},
 \qquad\det K_{\rm diff}=1-p^{-1}>0.                    \tag{4.6}
\]

Thus the composition contact and the correlation/Hodge kernel are
differently typed, exactly as row C emphasizes.

## 5. Torsor normalization cannot correct the rank

Any further normalization supplied by a one-dimensional multiplicative
torsor rescales the depth basis diagonally:

\[
 K\longmapsto D^*KD.                                     \tag{5.1}
\]

For invertible diagonal `D`, rank and inertia are unchanged.  Therefore a
rank-one matrix such as (4.5) cannot become the full-rank Toeplitz matrix
(4.6).

The canonical B torsor has already fixed the scale `p^{-r/2}`; changing it
would also destroy the central coefficient
`Lambda(p^r)/sqrt(p^r)`.  No alternative multiplicative scalar can change
sum dependence `(r+s)` into difference dependence `|r-s|`.

The latter emerges only after the opposite orientation and involutive
correlation are assembled in C.  That assembly also supplies the Gamma
term.  A finite determinant contact line in A has no archimedean oscillator
adjoint whose energy is `partial_infinity^* partial_infinity`.

## 6. Formal hard Lefschetz versus row D

One can freely form the exterior algebra on `N^1_deg`, use `H` as a raising
operator and (1.2) to define its formal adjoint.  The resulting finite
Lefschetz module satisfies hard Lefschetz and (1.5).  Its realization still
factors through the two degrees and hence vanishes on (3.3).

To obtain (3.4), one would have to enlarge the adjoint so that on the
`e_Gamma`/Poisson direction it has Gram `K_diff` and the Gamma oscillator.
No such adjoint is determined by the determinant metric.  Defining it by

\[
 \langle f,g\rangle_{\rm prim}:=-B_{\rm nuc}(f,g)         \tag{6.1}
\]

is exactly the GNS construction after row-D positivity and is circular as
a proof.

## 7. Outcome and next intrinsic test

The available Hodge theorem and the desired one must remain distinct:

\[
 \begin{array}{c|c|c}
 &\text{primitive space}&\text{form}\\ \hline
 \text{A ruling index}&\ker(d_1+d_2)\subset\mathbb R^2
   &B_{\rm int}\le0\\
 \text{D Weil positivity}&\ker(M_-,M_+)\subset\mathcal S
   &B_{\rm nuc}\le0
 \end{array}                                               \tag{7.1}
\]

The A Kunneth metric, B torsor and C trace determine every coefficient in
the second row but do not transport the first-row adjoint to it.

The next source-side possibility is to build a Lefschetz operator directly
on the **periodic section moduli**, not on degrees: use addition of one
extremal section as raising map and residuation as a candidate lowering
map.  Its finite-depth incidence matrices are canonical and positive.
The decisive audit is whether their primitive Schur complements converge
to the Toeplitz kernels (4.4) and the Gamma oscillator, rather than to the
local graph/Monge--Ampere kernels already ruled out in D.93.

