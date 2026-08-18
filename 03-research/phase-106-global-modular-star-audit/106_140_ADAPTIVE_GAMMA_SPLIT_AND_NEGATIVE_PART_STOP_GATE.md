# 106.140 — Adaptive Gamma splitting and the negative-part stop gate

## 1. Purpose and result

Document 106.135 proves the exact positive decomposition

\[
 \mathfrak b_{\Gamma,*}=2\mathfrak b_K+\mathfrak b_{w_\Gamma},
 \qquad
 w_\Gamma=r_\Gamma-2K>0.
 \tag{1}
\]

Document 106.139 shows that spending one fixed fraction of Gamma gives a
strictly stronger gate which is numerically false even on a four-zero
subspace of the complete radical complement.  The remaining natural
proposal is to choose the amount of the positive remainder adaptively on
each heat or hybrid row.

This note proves that the adaptive coefficient contains no additional
slack.  Its sharp value is at most one if and only if the original physical
form is nonnegative on that row.  Replacing the sharp generalized
eigenvalue by domination of the negative spectral part is not equivalent;
it is a strictly stronger condition, already falsified by a rational
two-dimensional example.

## 2. Exact finite-row decomposition

Let \(E\) be a finite-dimensional heat or hybrid row after the complete
radical anti-short.  Compress the two self-adjoint forms

\[
 B_E=\left(\mathfrak P_{\rm PNT}+2\mathfrak b_K\right)\big|_E,
 \qquad
 W_E=\mathfrak b_{w_\Gamma}\big|_E.
 \tag{2}
\]

The strict positivity of \(w_\Gamma\) and the displacement form imply that
\(W_E>0\) after constants have been removed.  By (1), the original physical
form on \(E\) is exactly

\[
 \boxed{
 \mathfrak Q_{\rm phys}\big|_E=B_E+W_E.}
 \tag{3}
\]

For \(\kappa\ge0\), the adaptive Gamma gate is

\[
 B_E+\kappa W_E\succeq0.
 \tag{4}
\]

## 3. The optimal coefficient is the physical sign

Define

\[
 \boxed{
 \kappa_E=
 \max\left\{0,
 -\lambda_{\min}\!\left(
 W_E^{-1/2}B_EW_E^{-1/2}
 \right)\right\}.}
 \tag{5}
\]

### Theorem 1 — Exact adaptive coefficient

For every \(\kappa\ge0\),

\[
 B_E+\kappa W_E\succeq0
 \quad\Longleftrightarrow\quad
 \kappa\ge\kappa_E.
 \tag{6}
\]

In particular,

\[
 \boxed{
 \kappa_E\le1
 \quad\Longleftrightarrow\quad
 B_E+W_E\succeq0
 \quad\Longleftrightarrow\quad
 \mathfrak Q_{\rm phys}\big|_E\succeq0.}
 \tag{7}
\]

#### Proof

Congruence by \(W_E^{-1/2}\) transforms (4) into

\[
 W_E^{-1/2}B_EW_E^{-1/2}+\kappa I\succeq0.
\]

The least admissible nonnegative \(\kappa\) is therefore (5), proving
(6).  Setting \(\kappa=1\) and using (3) proves (7).  \(\square\)

Let \((E_m)\) be any nested exhaustion of the complete form core by the
heat rows of 106.98, or by the corresponding hybrid rows.  Closed-form
convergence gives

\[
 \boxed{
 \sup_m\kappa_{E_m}\le1
 \quad\Longleftrightarrow\quad
 \mathfrak Q_{\rm phys}\ge0
 \text{ on the complete anti-short}.}
 \tag{8}
\]

Thus an adaptive split does not weaken the force-bearing theorem.  A
subthreshold vector has negative physical energy; its form-core heat
approximants eventually satisfy \(\kappa_{E_m}>1\).

## 4. Operator-valued and state-dependent allocation also collapse

The scalar coefficient in (4) could appear unnecessarily restrictive.  Let
\(X_E=X_E^*\) be an operator on \(E\) satisfying

\[
 0\preceq X_E\preceq I,
 \tag{9}
\]

and allocate the available Gamma remainder direction by direction through

\[
 B_E+W_E^{1/2}X_EW_E^{1/2}\succeq0.
 \tag{10}
\]

### Theorem 2 — Maximal-reserve rigidity

There exists an operator \(X_E\) satisfying (9)--(10) if and only if the
original physical form is nonnegative on \(E\):

\[
 \boxed{
 \exists X_E\in[0,I]:
 B_E+W_E^{1/2}X_EW_E^{1/2}\succeq0
 \quad\Longleftrightarrow\quad
 B_E+W_E\succeq0.}
 \tag{11}
\]

#### Proof

If the right side holds, choose \(X_E=I\).  Conversely, if (10) holds,
then

\[
 B_E+W_E
 =B_E+W_E^{1/2}X_EW_E^{1/2}
  +W_E^{1/2}(I-X_E)W_E^{1/2}\succeq0.
\]

This proves (11).  \(\square\)

The same argument closes a state-dependent scalar rule.  For each nonzero
\(q\in E\), allowing an arbitrary \(\kappa(q)\in[0,1]\) gives

\[
 \langle q,B_Eq\rangle+
 \kappa(q)\langle q,W_Eq\rangle\ge0
\]

for every \(q\) if and only if
\(\langle q,(B_E+W_E)q\rangle\ge0\) for every \(q\).  The maximal available
reserve is already \(W_E\); no nonlinear choice of how much of it to spend
can produce an intermediate theorem.

## 5. Why the negative-part shortcut is invalid

A tempting sufficient condition is

\[
 (B_E)_-\preceq W_E,
 \tag{12}
\]

where \((B_E)_-\) is the negative spectral part of \(B_E\).  Condition
(12) implies \(B_E+W_E\succeq0\), but the converse is false because the
positive and negative spectral subspaces of \(B_E\) need not reduce
\(W_E\).

Take the exact rational matrices

\[
 B=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
 \qquad
 W=\begin{pmatrix}2&2/5\\2/5&1/10\end{pmatrix}.
 \tag{13}
\]

Here

\[
 \det W=\frac1{25}>0,
 \qquad
 W_{11}>0,
\]

so \(W>0\).  Also

\[
 B+W=\begin{pmatrix}1&2/5\\2/5&11/10\end{pmatrix}>0
\]

because its determinant is \(47/50>0\).  But

\[
 W-B_-=
 \begin{pmatrix}1&2/5\\2/5&1/10\end{pmatrix},
 \qquad
 \boxed{\det(W-B_-)=-\frac3{50}<0.}
 \tag{14}
\]

Therefore (12) is strictly stronger than the physical sign and cannot be
substituted for (7).

## 6. Result

The positive Gamma remainder can be spent adaptively, but its optimal
coefficient is the bottom generalized eigenvalue (5).  Requiring that
coefficient to remain at most one on a cofinal heat/hybrid exhaustion is
exactly the original physical surplus.  Dominating the negative part of
\(B_E\) introduces a false stronger condition.

Consequently neither fixed, scalar-adaptive, state-dependent, nor
operator-valued Gamma splitting supplies an intermediate theorem.  The
remaining input is still the jointly signed, complete
ordinary-prime--Gamma--pole alignment after the exact radical anti-short.
