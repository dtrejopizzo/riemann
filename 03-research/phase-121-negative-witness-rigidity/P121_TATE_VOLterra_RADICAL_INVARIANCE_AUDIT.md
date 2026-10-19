# Phase 121 -- Tate--Volterra radical-invariance audit

## Status

This note tests a bounded replacement for the failed translation-jet
argument.  The canonical triangular Tate Green operator of v94 (739) is a
bounded Volterra regularization of differentiation and has an exact
clamped identity.  If it preserved a first-contact radical, it would
annihilate that radical without any positivity comparison or residue
selector.  The exclusion theorem below is genuine.  The invariance itself,
however, is not supplied by the first-contact equation: it contains both
the moving Tate jet and the exterior compression defect.  Thus the route
does not close the global square.

## 1. Canonical operator

Let

\[
 (C_TF)(u)=\int_u^T2\cosh((t-u)/2)F(t)\,dt          \tag{1.1}
\]

and let `B` be the two Tate moments, `P` the orthogonal projection onto
`P_T=ker B`.  V94 (740)--(743) proves

\[
 C_T+C_T^*=B^*J_2B,                                \tag{1.2}
\]

and, on the primitive smooth core,

\[
 (\partial_u^2-\tfrac14)C_TF=-2F',\qquad
 C_TF\in H_0^2(-T,T).                              \tag{1.3}
\]

The integral formula itself extends `C_T` boundedly from `L2` to `H1`.
Moreover v94 (741), with the notation there, gives the exact normal
component

\[
 BC_TP=BQP=2DB_1'.                                  \tag{1.4}
\]

## 2. A bounded radical-invariance theorem

Let `Delta_T` be the nonnegative primitive compression at a hypothetical
first contact and put

\[
 \mathcal N_T=\ker\Delta_T.                         \tag{2.1}
\]

The kernel is finite-dimensional by compact resolvent.

### Theorem 2.1

If

\[
                         C_T\mathcal N_T
                         \subseteq\mathcal N_T,     \tag{2.2}
\]

then `N_T={0}`.

#### Proof

Because `N_T` is contained in `ker B`, equation (1.2) shows that the
restriction of `C_T` to `N_T` is skew-adjoint.  It is an endomorphism of a
finite-dimensional complex space by (2.2), so it has an eigenvector
`0 != F in N_T` with

\[
                         C_TF=i\lambda F,
                         \qquad\lambda\in\mathbb R. \tag{2.3}
\]

If `lambda=0`, injectivity of the Volterra operator (differentiate (1.1)
from the right endpoint) gives `F=0`, a contradiction.

If `lambda != 0`, (1.1) first gives `F in H1`; substitution back into the
integral equation bootstraps `F` to every Sobolev order.  Equation (1.3)
and (2.3) therefore give the constant-coefficient ODE

\[
 i\lambda(F''-\tfrac14F)=-2F'.                     \tag{2.4}
\]

At the right endpoint, (1.1) gives `(C_TF)(T)=0`, hence `F(T)=0`.
Differentiating (1.1) gives `(C_TF)'(T)=-2F(T)=0`, hence (2.3) also gives
`F'(T)=0`.  Uniqueness for (2.4) yields `F=0`, again a contradiction.
Therefore the assumed nonzero eigenvector cannot exist and `N_T={0}`.
QED.

This is a bounded analogue of v94 (335): no translation-generator
regularity of the hypothetical radical is assumed.

## 3. Exact obstruction to invariance

Condition (2.2) has two independent components.  For `F in N_T`, it
requires

\[
 BC_TF=0,\qquad P\mathscr A_TC_TF=0.                \tag{3.1}
\]

The first is not formal.  By (1.4),

\[
 BC_TF=2DB_1'F,                                    \tag{3.2}
\]

so invariance already forces the complete moving Tate jet to vanish on
the radical.  First contact does not imply this: the endpoint/Rellich audit
in v94 (501)--(507) shows that first loss need not be stationary and that
primitive clamping does not annihilate `B_1'`.

The second component is also not obtained by commuting Fourier
multipliers.  The zero extension of `C_TF` is a global multiplier only
because the Tate moments of `F` cancel its endpoint distributions.  The
global Gamma--Euler operator applied before and after `C_T` differs, after
restriction, by precisely the exterior localization history of v94
(451)--(455).  Replacing that compressed commutator by the formal global
multiplier commutator deletes the same incoming tail whose vanishing is
annular transport.

There is an exact block formula for this failure.  On a common core let
`A` denote the global translation-invariant Gamma--Euler operator and
retain the same letters for its window compression.  Put

\[
 H=PAP,\qquad S=PC_TP,\qquad
 X=P^\perp AP,\qquad Y=P^\perp C_TP.                \tag{3.3}
\]

Before restriction, `A` commutes with the Fourier multiplier represented
by `C_T`, and that multiplier is skew.  Inserting `I=P+P^perp` at the two
compression cuts therefore gives

\[
 \boxed{HS+S^*H=-(X^*Y+Y^*X).}                     \tag{3.4}
\]

Here `Y` is completely explicit from (1.4),

\[
 Y=B^*K^{-1}(2DB_1'),                               \tag{3.5}
\]

while `X` is the two-Tate exterior boundary of the compressed
Gamma--Euler operator.  Both have range in the two-dimensional normal
space, so the right side of (3.4) has rank at most four.

For `F in N_T`, equation (3.4) reduces to

\[
 HS F=-(X^*Y+Y^*X)F.                               \tag{3.6}
\]

Thus `S` preserves the radical exactly when this boundary vector vanishes
on the radical.  Its diagonal pairing with `F` is automatically zero,
because `HF=0`; scalar conservation cannot promote that fact to the vector
identity (3.6).  Formula (3.4) is therefore the precise kill test for the
candidate, not a new unnamed commutator gate.

There is a sharper reason why Real symmetry cannot supply that promotion.
Let `R F(u)=F(-u)`.  The global Weil operator commutes with `R`, whereas
reflection exchanges the right and left triangular Green operators.  Thus

\[
 RH=HR,\qquad RSR=S^*=-S,                          \tag{3.7}
\]

and consequently the defect

\[
 D_T:=HS+S^*H=-(X^*Y+Y^*X)                        \tag{3.8}
\]

**reverses parity**.  If a first-contact vector has parity `epsilon`, then
`D_TF` has parity `-epsilon`; hence

\[
                         \langle D_TF,F\rangle=0   \tag{3.9}
\]

holds before using the zero-mode equation.  In the generic situation where
the first radical occurs in only one parity sector, every scalar identity
obtained by pairing (3.6) back with that radical is therefore vacuous.  If
both parity sectors have radical vectors, polarization yields only the
cross-sector boundary relation; it still does not make `D_TF` vanish.

This disposes of the remaining symmetry shortcut: the rank-four defect is
not an error term that Real symmetry kills.  It is precisely an
off-diagonal port from the null parity sector into the opposite sector.
Eliminating it requires a vector-valued annular law, not another conserved
scalar.

Hence

\[
 C_T\mathcal N_T\subseteq\mathcal N_T              \tag{3.10}
\]

is a valid sufficient source theorem but not a consequence presently
available from (445).  Its normal part asks for zero moving Tate flux; its
tangential part asks for zero exterior innovation.

## 4. Why compression does not repair the route

The compressed operator `S_T=PC_TP` is bounded, compact and skew-adjoint on
the primitive space.  It does preserve primitivity, but it is no longer
Volterra: the rank-two Tate projection feeds the right endpoint back into
the interval.  A nonzero compact skew-adjoint operator has ordinary
imaginary eigenvalues, and the associated eigenvectors solve (2.4) with
nonzero Tate boundary data rather than clamped Cauchy data.  Thus replacing
`C_T` by `S_T` destroys the step in Theorem 2.1.

This is the exact bounded-regularizer version of the recurring
local/global trap:

* uncompressed `C_T` is causal and clamped but does not preserve the
  primitive radical;
* compressed `PC_TP` preserves the primitive space but loses the causal
  boundary condition that makes the ODE unique.

## 5. Corpus verdict

The ingredients occur separately in v94: translation-jet exclusion
(335)--(341), the moving Tate correction (528)--(531), the exterior
localization defect (451)--(455), and the triangular Green operator
(739)--(743).  No prior phase-1--120 note was found combining them into
Theorem 2.1.  The theorem is a real equality-state exclusion criterion,
but the audit proves that its invariance hypothesis is the conjunction of
the two already identified boundary leakages.  It therefore does not close
F2 or the global square.
