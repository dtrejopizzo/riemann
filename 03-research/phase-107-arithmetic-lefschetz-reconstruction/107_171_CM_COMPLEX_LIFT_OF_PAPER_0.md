# 107.171 -- A CM complex lift preserving the complete Paper-0 chain

## 1. Fixed control and its CM model

The Phase 107 control is

\[
 E/\mathbb F_5:\qquad y^2=x^3+x+1.
\]

It has

\[
 \#E(\mathbb F_5)=9,\qquad a_1=5+1-9=-3,
\]

so its Frobenius polynomial is

\[
 P(T)=T^2+3T+5
\]

with discriminant \(-11\).  The Hilbert class polynomial is

\[
 H_{-11}(X)=X+32768.
\]

Sage produces the rational CM model

\[
 E_{\rm CM}/\mathbb Q:qquad
 y^2+y=x^3-x^2-7x+10,
 \qquad j(E_{\rm CM})=-32768.
 \tag{1.1}
\]

It has good reduction at \(5\), and that reduction is isomorphic over
\(\mathbb F_5\) to the fixed control \(E\).  In particular it has the
same Frobenius trace \(-3\).

Let

\[
 K=\mathbb Q(\sqrt{-11}),
 \qquad
 \alpha=\frac{-3+\sqrt{-11}}2\in\mathcal O_K.
\]

Then

\[
 \operatorname{Tr}_{K/\mathbb Q}(\alpha)=-3,
 \qquad N_{K/\mathbb Q}(\alpha)=5,
\]

and \(P(\alpha)=0\).  Since (1.1) has CM by \(\mathcal O_K\), \(\alpha\)
acts as an endomorphism after base change to the CM field.  This is the
complex lift of the fixed Frobenius endomorphism.

## 2. Graph intersections on the complex surface

Put

\[
 A=E_{\rm CM}\times E_{\rm CM}
\]

over \(\mathbb C\), and let

\[
 F_1=E_{\rm CM}\times\{0\},qquad
 F_2=\{0\}\times E_{\rm CM},qquad
 \Delta=\Gamma_1.
\]

For \(\beta\in\operatorname{End}(E_{\rm CM})\), standard graph
intersection gives

\[
 \Gamma_\beta\cdot F_1=\deg\beta=N(\beta),
 \qquad
 \Gamma_\beta\cdot F_2=1,
 \tag{2.1}
\]

and

\[
 \Gamma_\beta\cdot\Delta
 =\deg(\beta-1)=N(\beta-1).
 \tag{2.2}
\]

Every graph is an elliptic curve in the abelian surface \(A\).  Since
\(K_A=0\), adjunction gives

\[
 \Gamma_\beta^2=0.
 \tag{2.3}
\]

Take \(\beta=\alpha^n\), and write

\[
 s_n=\operatorname{Tr}(\alpha^n).
\]

Then

\[
 N(\alpha^n)=5^n,
\]

and

\[
 N(\alpha^n-1)=5^n+1-s_n.
 \tag{2.4}
\]

The recurrence

\[
 s_0=2,\qquad s_1=-3,\qquad
 s_n=-3s_{n-1}-5s_{n-2}
\]

is the Frobenius recurrence of the fixed curve, so

\[
 N_n=\#E(\mathbb F_{5^n})=5^n+1-s_n.
\]

Combining this with (2.1)--(2.4) gives

\[
 \boxed{\Gamma_{\alpha^n}\cdot\Delta=N_n}
\]

for every \(n\ge1\), now on a characteristic-zero complex surface.

## 3. Centering and Hodge form

Define

\[
 \Delta^0=\Delta-F_1-F_2,
\]

and

\[
 \Gamma_n^0
 =\Gamma_{\alpha^n}-F_1-5^nF_2.
\]

Both are orthogonal to \(F_1,F_2\).  Direct expansion using (2.1)--(2.3)
gives

\[
 (\Delta^0)^2=-2,
 \qquad
 (\Gamma_n^0)^2=-2\cdot5^n,
\]

and

\[
 \Gamma_n^0\cdot\Delta^0
 =N_n-5^n-1=-s_n.
\]

Thus the primitive Gram matrix is exactly the matrix of Paper 0:

\[
 G_n^0=
 \begin{pmatrix}
 -2&-s_n\\
 -s_n&-2\cdot5^n
 \end{pmatrix},
 \qquad
 \det G_n^0=4\cdot5^n-s_n^2\ge0.
\]

The inequality is the complex Hodge index theorem on the abelian
surface.  Equivalently, the two conjugates of \(\alpha\) have absolute
value \(\sqrt5\), giving \(|s_n|\le2\cdot5^{n/2}\).

## 4. Result and scope

This constructs an actual complex lift of the complete geometric chain
of Paper 0:

1. a smooth projective complex surface;
2. graph correspondences lifting every Frobenius iterate;
3. exact point-count intersections;
4. the centered primitive Hodge form and determinant bound.

It is stronger than a numerical recurrence: the rational model (1.1)
reduces to the fixed curve, and the endomorphism \(\alpha\) lives in its
CM endomorphism ring.

This does **not** construct the universal Phase 107 space over
\(\operatorname{Spec}\mathbb Z\).  The correspondence \(\alpha\) is
defined over the CM field after base change, and the construction uses
the special ordinary elliptic control.  It neither realizes Riemann
zeta's prime/Gamma divisor nor resolves the finite-place no-go of row
(c).  It proves that the complex-surface/Hodge architecture itself can
preserve the entire Weil chain when a genuine Frobenius lift exists.

## 5. Falsifier

The Sage verifier constructs both curves, checks the Hilbert class
polynomial and CM element, verifies reduction and isomorphism over
\(\mathbb F_5\), independently counts points through \(n=16\), and
checks every intersection and determinant identity.  Any mismatch
returns `VERDICT: NO`.
