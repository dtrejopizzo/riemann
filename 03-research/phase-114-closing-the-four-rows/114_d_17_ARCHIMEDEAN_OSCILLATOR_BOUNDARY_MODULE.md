# Row (d): an intrinsic archimedean oscillator boundary module

## Status

This note constructs the Gamma translation energy from a positive boundary
module which does not use the zero divisor or the sign of the Weil form.  It
also proves that the real component currently present in `Perf_DN` cannot by
itself supply this module.  The construction gives a genuine new part of a
mixed section theory; the sharp adelic Poincare estimate remains to be
proved.

## 1. Why the existing realification is insufficient

The Deligne--nuclear pullback uses the augmentation

\[
 \varepsilon:\mathcal C_{\mathbb R}\longrightarrow\mathbb R,
 \qquad \varepsilon(a)=a_1.                              \tag{1}
\]

For every `n>1`, `epsilon(delta_n)=0`.  Hence the realification of left
Dirichlet convolution by `delta_n` is the zero endomorphism.  The real
component records the common scalar fibre needed for the homotopy pullback,
but it contains no nontrivial representation of the prime translations.
In particular, a Gamma--prime coupling cannot be obtained by applying a
determinant functor only to this realification.

This is a type obstruction, not a sign obstruction: a separate
archimedean boundary representation is required.

## 2. The oscillator object

Let

\[
 \mathcal H_\infty=\ell^2(\mathbb Z_{\ge0}),\qquad
 A_\infty e_k=(k+\tfrac14)e_k.                           \tag{2}
\]

It is positive, self-adjoint and has compact resolvent.  Its heat trace is

\[
 \Theta_\infty(x)=\operatorname{Tr}(e^{-xA_\infty})
 =\sum_{k\ge0}e^{-x(k+1/4)}
 =\frac{e^{-x/4}}{1-e^{-x}}.                            \tag{3}
\]

No zeta zero occurs in (2)--(3).  The quarter shift is the real Gamma
parameter on the critical line.

## 3. Boundary derivation

Let `S_r F(t)=F(t-r)`.  On compactly supported smooth functions define

\[
 (\partial_\infty F)(x,k,t)
 =2^{-1/2}e^{-x(k+1/4)/2}
       \bigl(F(t)-F(t-x/2)\bigr),                       \tag{4}
\]

as an element of

\[
 \mathcal K_\infty=
 L^2(\mathbb R_{>0},dx;\mathcal H_\infty\widehat\otimes
 L^2(\mathbb R,dt)).                                    \tag{5}
\]

### Proposition 3.1

The norm of (4) is exactly the positive Gamma translation energy

\[
 \|\partial_\infty F\|^2
 =\int_0^\infty\frac{e^{-r/2}}{1-e^{-2r}}
       \|F-S_rF\|_2^2\,dr
 =:\mathcal D_\infty(F).                               \tag{6}
\]

### Proof

Tonelli applies because every summand is nonnegative.  Summing first over
`k` and using (3) gives

\[
 \|\partial_\infty F\|^2
 =\frac12\int_0^\infty
   \frac{e^{-x/4}}{1-e^{-x}}\|F-S_{x/2}F\|_2^2\,dx.
\]

The substitution `x=2r` is (6).

### Corollary 3.2

If

\[
 m_\infty(\tau)=\log\pi-
 \operatorname{Re}\psi(\tfrac14+i\tfrac\tau2),
 \qquad m_0=m_\infty(0),                               \tag{7}
\]

then

\[
 G_\infty(F,F)=m_0\|F\|_2^2-
                  \|\partial_\infty F\|^2             \tag{8}
\]

with the Fourier normalization of row (c).

### Proof

The standard digamma difference formula is

\[
 \operatorname{Re}\psi(a+ib)-\psi(a)
 =\int_0^\infty\frac{e^{-ax}}{1-e^{-x}}
                  (1-\cos bx)\,dx .                    \tag{9}
\]

Put `a=1/4`, `b=tau/2`, and apply Plancherel.  The Fourier
multiplier of `||F-S_{x/2}F||^2` is
`2(1-cos(tau x/2))`; the factor `1/2` in (4) gives exactly (9).
This yields (8).

## 4. The finite boundary derivation

For a cutoff `X`, put

\[
 \mathcal K_{{\rm fin},X}
 =\bigoplus_{2\le n\le X}L^2(\mathbb R),
 \qquad
 (\partial_{{\rm fin},X}F)_n
 =\left(\frac{\Lambda(n)}{\sqrt n}\right)^{1/2}
       (F-S_{\log n}F).                                 \tag{10}
\]

Then

\[
 \|\partial_{{\rm fin},X}F\|^2
 =\sum_{2\le n\le X}\frac{\Lambda(n)}{\sqrt n}
   \|F-S_{\log n}F\|^2=\mathcal E_X(F).                \tag{11}
\]

Thus finite and archimedean places now live in one positive correspondence
module

\[
 \partial_X=\partial_{{\rm fin},X}\oplus\partial_\infty.
                                                                    \tag{12}
\]

The construction is functorial for translations and complex conjugation,
and is made solely from `Lambda(n)>=0`, the shifts attached to the
correspondences, and the oscillator (2).

## 5. Exact relation to the row-(d) form

Let

\[
 A_X=\sum_{2\le n\le X}\frac{\Lambda(n)}{\sqrt n}.
\]

For a test function whose compact support makes the contact sum stabilize,
the identities of the finite and real places give

\[
 B_{\rm nuc}(F,F)
 =(2A_X+m_0)\|F\|_2^2-\|\partial_XF\|^2.               \tag{13}
\]

Both terms on the right depend on the paired cutoff, while their difference
stabilizes.  Consequently row (d) is equivalent to the sharp estimate

\[
 \|\partial_XF\|^2\ge(2A_X+m_0)\|F\|_2^2              \tag{14}
\]

for all `F` satisfying the two boundary moments and every sufficiently large
cutoff for its support.

## 6. Geometric interpretation and remaining theorem

Equations (4) and (10) provide a zero-free candidate for the conormal
module of the completed mixed correspondence: finite edges are the derived
Frobenius contacts and the real edge is the oscillator heat module.  Its
quadratic norm is positive before any comparison with row (c).  This is
strictly stronger data than appending the already evaluated distribution
`W_infty`.

What has **not** yet been proved is (14).  Calling (12) a conormal module
does not imply the required lower bound: that bound is the Hodge-index
content.  The next obligation is to construct a boundary restriction map

\[
 \operatorname{Tr}_X:\operatorname{Dom}(\partial_X)
       \longrightarrow\mathbb C^2                       \tag{15}
\]

whose kernel is exactly the two-moment primitive space, and prove an
intrinsic closed-range/coercivity theorem for the complex

\[
 0\longrightarrow\ker\operatorname{Tr}_X
 \xrightarrow{\ \partial_X\ }\mathcal K_X.             \tag{16}
\]

The sharp constant in that theorem must be `2A_X+m_0`; a smaller constant
does not close row (d).  Establishing (16) from a section multiplication or
duality theorem, rather than from the spectrum of `B_nuc`, is the current
construction target.

