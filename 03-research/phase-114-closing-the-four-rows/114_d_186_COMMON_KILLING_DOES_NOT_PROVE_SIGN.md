# D.186 — Common killing improves the Green operator but cannot prove sign

## Verdict

The \(\sqrt N\)-coercivity of the zero-extension reference in D.185 is a
major resolvent gain, but it cannot by itself imply the row-D inequality.
The reason is an exact congruence invariant.

Let

\[
 Q=R-L                                                    \tag{0.1}
\]

be the signed primitive form, and let \(P\ge0\) be any common positive
energy added to both sides.  If \(R+P>0\), define

\[
 T_P=(R+P)^{-1/2}(L+P)(R+P)^{-1/2}.                    \tag{0.2}
\]

Then

\[
 \boxed{
 I-T_P=(R+P)^{-1/2}Q(R+P)^{-1/2},}                    \tag{0.3}
\]

and hence

\[
 \boxed{T_P\le I\quad\Longleftrightarrow\quad Q\ge0.} \tag{0.4}
\]

In particular the boundary energy added simultaneously to
\(\widehat J_+\) and \(\widehat J_-\) in D.182 can make the Green norm
\(O(N^{-1/2})\), but it cannot turn a negative direction of
\(-B_{\rm nuc}=Q\) into a positive one.  It only makes the corresponding
eigenvalue excess above one small.

This identifies the legitimate use of D.185:

* it gives a strong ambient inverse for an exact Douglas/Schur estimate;
* it removes the Gamma-only prolate low-rank obstruction;
* it does not pay the unit defect budget or establish positivity.

The remaining theorem is still a divisibility statement for the actual
centered cross:

\[
 q=D^{1/2}a,\qquad \|a\|^2\le\hbox{remaining budget}, \tag{0.5}
\]

where \(D=I-T_P\).  The common killing may be used in constructing \(a\),
but (0.3) shows that the factor \(D^{1/2}\) cannot be omitted.

## 1. Congruence proof

From \(Q=R-L\),

\[
\begin{aligned}
 I-T_P
 &=(R+P)^{-1/2}\bigl((R+P)-(L+P)\bigr)(R+P)^{-1/2}\\
 &=(R+P)^{-1/2}Q(R+P)^{-1/2}.
\end{aligned}
\]

Congruence by an invertible positive operator preserves inertia.  This
proves (0.3)--(0.4), including multiplicities of positive, zero and
negative directions.

On a form domain, the same statement follows by the closed-form
representation theorem and approximation with \(R+P+\varepsilon I\).
Restriction to the two-Tate primitive subspace is performed before the
congruence and changes none of the logic.

## 2. Large common energy approaches one from the correct side

Take \(P=\lambda I\).  For a vector \(f\) with
\(\langle f,Qf\rangle<0\), put \(g=(R+\lambda I)^{1/2}f\).  Equation
(0.3) gives

\[
 {\langle g,T_\lambda g\rangle\over\|g\|^2}
 =1-{\langle f,Qf\rangle\over
          \langle f,(R+\lambda I)f\rangle}>1          \tag{2.1}
\]

for every \(\lambda\).  The excess is \(O(\lambda^{-1})\), but its sign
does not change.

Likewise, if \(Q\ge0\), every common \(P\) gives \(T_P\le I\).  Thus common
killing is a conditioning device, not a positivity mechanism.

## 3. Application to the zero-extension factorization

D.182 proves

\[
 -B_{\rm nuc}^{\rm prim}
 =\widehat{\mathcal R}_T-
  \widehat{\mathcal W}_T^*\widehat{\mathcal W}_T,     \tag{3.1}
\]

and D.185 proves

\[
 \widehat{\mathcal R}_T\ge A_NI,\qquad
 A_N\gg\sqrt N.                                      \tag{3.2}
\]

Relative to the regional factorization of D.134, both terms in (3.1)
received the same positive boundary multiplication operator.  Therefore
(0.3) applies exactly with

\[
 R+P=\widehat{\mathcal R}_T,\qquad
 L+P=\widehat{\mathcal W}_T^*\widehat{\mathcal W}_T. \tag{3.3}
\]

The strong estimate

\[
 \|\widehat{\mathcal R}_T^{-1}\|=O(N^{-1/2})          \tag{3.4}
\]

is valid and useful inside every return.  But

\[
 \left\|
 \widehat{\mathcal R}_T^{-1/2}
 \widehat{\mathcal W}_T^*\widehat{\mathcal W}_T
 \widehat{\mathcal R}_T^{-1/2}\right\|\le1           \tag{3.5}
\]

is still equivalent to \(-B_{\rm nuc}^{\rm prim}\ge0\).  It cannot be
deduced by observing that both numerator and denominator have leading
size \(\sqrt N\).

## 4. Correct next estimate

Use the D.170--D.176 notation after the common-killing normalization.
The output Schur condition is

\[
 y^*D_{\rm out}^{\dagger}y\le I.                    \tag{4.1}
\]

The exact first-return cancellation writes the non-telescoping part as

\[
 q^*D^\dagger q,\qquad q=Dh-u.                       \tag{4.2}
\]

D.185 improves every reference inverse occurring in \(q\) and \(h\).
Equation (0.3), however, requires the source-derived factorization

\[
 q\in\operatorname {Ran}D^{1/2}                     \tag{4.3}
\]

with the sharp norm budget.  PNT bounds, finite rank, or common-energy
coercivity do not imply (4.3).  This is the exact residual Douglas
obligation.

