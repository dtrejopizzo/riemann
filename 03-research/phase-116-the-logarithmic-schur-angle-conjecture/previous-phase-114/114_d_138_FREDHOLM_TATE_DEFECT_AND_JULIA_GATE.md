# D.138 — Fredholm--Tate defect, determinant line, and the Julia gate

## Verdict

The exact centred factorization of D.134 does produce a canonical mixed
Fredholm object on every support window.  If

\[
 A_T=\mathcal W_T\mathcal R_T^{-1/2},
 \qquad D_T=I-A_T^*A_T,
\]

then (A_T) is compact and (D_T) is a bounded self-adjoint Fredholm
operator.  Its transported quadratic form is exactly the complete
A--B--C pullback,

\[
 \boxed{
 \langle \mathcal R_T^{1/2}F,
 D_T\mathcal R_T^{1/2}G\rangle
 =-B_{\rm nuc}(F,G)}                                   \tag{0.1}
\]

on the two-Tate primitive space.  The definitions of (\mathcal R_T) and
(\mathcal W_T) include every active (p^k), the full (5/4)-Gamma screw,
the continuous Chebyshev resolvent, and the central atom.  Hence (0.1) is
not a finite-place or truncated-Gamma comparison.

The Fredholm determinant **line** of (D_T) exists.  It does not supply the
required sign: it only detects the eigenvalue (0) of (D_T), whereas row
D asks that the whole spectrum lie in ([0,\infty)).  Nor is there an
ordinary numerical relative determinant.  The compact operator
(A_T^*A_T) belongs to no Schatten class, so
(\prod_j(1-\lambda_j(A_T^*A_T))) has no canonical Fredholm
regularization.

Most decisively, a positive Hilbert Julia colligation for (A_T) exists
exactly when (A_T) is a contraction:

\[
 \boxed{
 \text{positive Julia realization of the mixed defect}
 \Longleftrightarrow D_T\ge0
 \Longleftrightarrow -B_{\rm nuc}^{\rm prim}\ge0.}     \tag{0.2}
\]

Thus the Fredholm/Tate enlargement constructs and correctly types the
mixed object, but positivity of its metric is precisely the row-D theorem.
It cannot be inserted as an axiom without circularity.  An indefinite
Krein realization always exists; its negative index is exactly the number
of Birman--Schwinger eigenvalues above one.

No zero of (\xi), RH, or sign of the Weil form is assumed.  The paper is
not modified.

## 1. The energy source and the complete channel map

Fix (T>0), put (I_T=[-T,T]), and let

\[
 \mathcal P_T=left\{F\in L^2(I_T):
  \int_{I_T}e^{t/2}F(t)\,dt=
  \int_{I_T}e^{-t/2}F(t)\,dt=0\right\}.               \tag{1.1}
\]

The two equations in (1.1) are the two Tate moments.  Under the
Paley--Wiener transform they are evaluation at (i/2) and (-i/2), hence
the (s=1) and (s=0) jets.

For (n=p^k), write

\[
 a_n=k\log p,\qquad w_n=(\log p)p^{-k/2},              \tag{1.2}
\]

and, when (a_n\le2T),

\[
 J_{n,\pm}F(t)={F(t+a_n)\pm F(t)\over\sqrt2},
 \qquad -T\le t\le T-a_n.                             \tag{1.3}
\]

Let

\[
 \gamma_{5/4}(r)={e^{-5r/2}\over1-e^{-2r}},           \tag{1.4}
\]

and use zero extension outside (I_T).  The positive reference form is

\[
\begin{aligned}
 \mathcal R_T(F,G)={}&
 {1\over2}\iint_{\mathbb R^2}\gamma_{5/4}(|t-s|)
   (\widetilde F(t)-\widetilde F(s))
   \overline{(\widetilde G(t)-\widetilde G(s))}\,dt\,ds\\
 &+\sum_{p^k\le e^{2T}}w_{p^k}
   \langle J_{p^k,-}F,J_{p^k,-}G\rangle .             \tag{1.5}
\end{aligned}
\]

It is closed, strictly positive, and has compact embedding of its form
domain into (L^2(I_T)).  Denote by (\mathcal E_T) its energy completion.

Put

\[
 \beta=\log\pi-\psi(5/4)>0,
 \qquad (R_{1/2,T}F)(t)=\int_{I_T}e^{-|t-s|/2}F(s)\,ds, \tag{1.6}
\]

and define the channel map

\[
 \mathcal W_TF=left(
  \sqrt\beta F, R_{1/2,T}^{1/2}F,
  (\sqrt{w_{p^k}}J_{p^k,+}F)_{p^k\le e^{2T}}
 \right).                                               \tag{1.7}
\]

The target is the Hilbert direct sum of the displayed channels.  D.133 and
D.134 prove the sesquilinear identity

\[
 -B_{\rm nuc}(F,G)=
 \mathcal R_T(F,G)-\langle\mathcal W_TF,\mathcal W_TG\rangle . \tag{1.8}
\]

The (5/4) in (1.4) is the exact digamma recurrence after the two moments
short the (e^{a/2}) Chebyshev term.  The sum in (1.5)--(1.7) is over all
prime powers whose translation acts on (I_T); no (k=1) replacement is
made.

By the Riesz identification of (\mathcal E_T) with the (L^2) source,

\[
 A_T=\mathcal W_T\mathcal R_T^{-1/2}                  \tag{1.9}
\]

is bounded and compact.  Transporting (1.8) gives (0.1).

## 2. The canonical Fredholm object

Since (A_T) is compact,

\[
 K_T=A_T^*A_T\ge0                                      \tag{2.1}
\]

is compact and

\[
 D_T=I-K_T                                               \tag{2.2}
\]

is self-adjoint Fredholm.  Its essential spectrum is the singleton
({1}), and

\[
\begin{aligned}
 \ker D_T&=E_{K_T}(\{1\}),\\
 \operatorname{ind}_-(D_T)
 &=\dim E_{K_T}((1,\infty))<\infty.                    \tag{2.3}
\end{aligned}
\]

The second integer is the exact dangerous count of D.134.  In particular,
the mixed object is not merely formal: it is an candid Fredholm quadratic
complex with finite Morse defect on every bounded window.

For a Fredholm operator (D:H\to H), its determinant line is

\[
 \operatorname{Det}(D)=
 \Lambda^{\max}\ker D\otimes
 (\Lambda^{\max}\operatorname{coker}D)^*.              \tag{2.4}
\]

Thus (\operatorname{Det}(D_T)) exists.  Self-adjointness identifies
(\operatorname{coker}D_T\simeq\ker D_T), but this finite-dimensional
line only changes when an eigenvalue passes through (0), equivalently
when an eigenvalue of (K_T) passes through (1).  Eigenvalues of (K_T)
strictly larger than one are invisible to the isomorphism class of (2.4).
Consequently a metric or orientation on (2.4) cannot prove that the Morse
index in (2.3) vanishes.

## 3. Why there is no numerical Fredholm determinant

D.134 proves the operator lower bound

\[
 K_T\ge \beta\mathcal R_T^{-1}                         \tag{3.1}
\]

and the eigenvalue estimate

\[
 \lambda_j(K_T)\ge {c_T\over\log(2+j)}.                \tag{3.2}
\]

Hence (K_T\notin\mathcal S_p) for every finite (p).  In particular it
is not trace class, so the usual relative determinant

\[
 \det(I-K_T)=\prod_j(1-\lambda_j(K_T))                 \tag{3.3}
\]

is not defined.  No finite-order regularized determinant (\det_p) applies
either, because those require (K_T\in\mathcal S_p).

A subtraction tailored to the full asymptotic sequence could define a
renormalized scalar, but that subtraction is additional data.  The
Fredholm line (2.4) is canonical without such data; a numerical Quillen
norm is not.  More importantly, any scalar regularization of (3.3) would
still record a product of eigenvalues and not imply each factor
(1-\lambda_j(K_T)) is nonnegative.

## 4. The positive Julia realization is exactly D

Suppose first that (A_T) is a contraction.  The positive defect operators

\[
 D_A=(I-A_T^*A_T)^{1/2},\qquad
 D_{A^*}=(I-A_TA_T^*)^{1/2}                            \tag{4.1}
\]

exist.  The intertwining identity

\[
 A_TD_A=D_{A^*}A_T                                     \tag{4.2}
\]

follows first for polynomials in (A_T^*A_T) and then by continuous
functional calculus.  Therefore the Julia operator

\[
 \mathcal U_T=
 \begin{pmatrix}
  A_T&D_{A^*}\\
  D_A&-A_T^*
 \end{pmatrix}                                         \tag{4.3}
\]

is unitary.  Direct block multiplication, using (4.2), proves
(\mathcal U_T^*\mathcal U_T=mathcal U_T\mathcal U_T^*=I).

Conversely, any Hilbert-space colligation with upper-left corner (A_T)
and an isometric first column gives

\[
 A_T^*A_T+C^*C=I                                       \tag{4.4}
\]

for some (C), hence (I-A_T^*A_T=C^*C\ge0).  Thus

\[
 \text{(A_T) has a positive conservative Julia realization}
 \Longleftrightarrow I-A_T^*A_T\ge0.                   \tag{4.5}
\]

Combining (0.1) and (4.5) proves (0.2).  The square root in (4.1) is not a
new construction of the Hodge metric: its existence already assumes its
positivity.

## 5. The unconditional Krein realization

The polar decomposition and spectral theorem always split

\[
 \mathcal E_T=E_T^{<}\oplus E_T^{=}\oplus E_T^{>},     \tag{5.1}
\]

according to the spectrum of (K_T) below, at, and above one.  On the
nondegenerate quotient of (D_T), the fundamental symmetry

\[
 J_T=\operatorname{sgn}(D_T)                           \tag{5.2}
\]

turns (|D_T|^{1/2}) into an indefinite defect operator.  Standard Krein
completion then gives a (J)-unitary colligation for (A_T).  Its negative
index is

\[
 \operatorname{ind}_-(J_T)=\dim E_T^>
 =\#\{\lambda_j(K_T)>1\}=d_T.                          \tag{5.3}
\]

This realization is unconditional and finite-Pontryagin on each window,
but (5.3) is not the Hodge theorem.  Row D is precisely the assertion
(d_T=0) for every (T).

## 6. Compatibility as the window grows

If (0<S<T), extend (F\in\mathcal P_S) by zero to (I_T).  Its Tate
moments remain zero.  The zero-extension Gamma form, the resolvent form,
and every old prime-power translation agree with their (S)-window
values.  For a new prime-power channel with (2S<a_n\le2T), the two
translates have disjoint support.  Therefore

\[
 \|J_{n,+}F\|^2=\|J_{n,-}F\|^2,                       \tag{6.1}
\]

so its positive reference and positive load contributions cancel in the
difference (1.8).  They do not vanish separately.  Consequently

\[
 B_{{\rm nuc},T}(F,G)=B_{{\rm nuc},S}(F,G).            \tag{6.2}
\]

The primitive Hermitian forms therefore form a compatible inductive
system.  Their negative indices are monotone:

\[
 d_S\le d_T.                                           \tag{6.3}
\]

Equation (6.3) localizes a possible failure, but does not exclude one.
Because the equal terms in (6.1) alter both (\mathcal R_T) and
(\mathcal W_T^*\mathcal W_T), the Riesz operators (D_S,D_T) live in
different energy metrics and are not related by a literal compression.  In
particular, the individual determinant lines (2.4) do not automatically
assemble into a determinant line on the inductive limit: the quotient
between successive energy spaces is infinite-dimensional.

## 7. Consequence for a mixed Riemann--Roch construction

The object (D_T) is the canonical Fredholm candidate whose transported
cross-effect is the exact form (B_{\rm nuc}).  It settles the typing part
of the mixed determinant problem at finite window.  What it does **not**
provide is any of the following independently:

1. a nonnegative section dimension or effective cone;
2. a positive Quillen metric on the full defect spectrum;
3. a contraction (A_T);
4. a compatible determinant orientation on the infinite-window limit.

Giving (D_T) the positive square-root metric is equivalent to row D by
(0.2).  Giving it the Krein metric is unconditional but retains exactly
the dangerous index (d_T).  Therefore the next construction must produce
the Hilbert colligation, or an RR/effectivity theorem forcing it, from a
source independent of (D_T\)'s spectral sign.

The Fredholm/Tate step is nevertheless a strict advance over an untyped
wish for a mixed object: the object exists, its cross-effect is exact, its
finite-window determinant line exists, and the sole remaining datum is a
positive compatible metric/effectivity structure.
