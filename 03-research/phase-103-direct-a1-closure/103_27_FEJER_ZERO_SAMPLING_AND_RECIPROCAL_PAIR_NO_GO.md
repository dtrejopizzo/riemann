# Fejer zero sampling and reciprocal-pair obstruction

## Purpose

Let
\[
 D_n:=2\lambda_n-\lambda_n^{\rm arch}.
\tag{1}
\]
This is the strong-margin quantity whose nonnegativity would imply A1 after
A0.  This note derives its exact zero-side sampling form, identifies the
precise place where Fejer positivity enters, and tests whether functional
pairs can replace it without assuming critical-line support.

The result is negative but sharp: Fejer/Parseval coercivity is available
only after the zero divisor has reached the unit circle.  Functional pairing
away from that circle produces an explicitly sign-indefinite reciprocal
quartet.

## 1. Divisor coordinates and the Li identity

For every nontrivial zero, counted with multiplicity, put
\[
 w_\rho=1-{1\over\rho}={\rho-1\over\rho}.
\tag{2}
\]
The exact Li divisor identity, in symmetric limiting order, is
\[
 \lambda_n=\sum_\rho^*\bigl(1-w_\rho^n\bigr).                    \tag{3}
\]
Moreover,
\[
 |w_\rho|^2={|\rho-1|^2\over|\rho|^2},\qquad
 |\rho|^2-|\rho-1|^2=2\Re\rho-1.                                \tag{4}
\]
Thus
\[
 |w_\rho|=1\quad\Longleftrightarrow\quad\Re\rho={1\over2}.     \tag{5}
\]
The functional and conjugation symmetries act by
\[
 w_{\bar\rho}=\overline{w_\rho},\qquad
 w_{1-\rho}=w_\rho^{-1},\qquad
 w_{1-\bar\rho}=\overline{w_\rho}^{-1}.                          \tag{6}
\]

## 2. Positive Fejer sampling under RH

Write
\[
 \mathscr D_n(w)=1+w+\cdots+w^{n-1},\qquad
 F_n(w)={1\over n}|\mathscr D_n(w)|^2.                            \tag{7}
\]
Assume RH for this paragraph only.  Then \(|w_\rho|=1\) and
\[
 {1\over|\rho|^2}=|1-w_\rho|^2.                                  \tag{8}
\]
Consequently,
\[
 {1\over|\rho|^2}|\mathscr D_n(w_\rho)|^2
 =(1-w_\rho^n)(1-\overline{w_\rho}^n)
 =2-w_\rho^n-\overline{w_\rho}^n.                                \tag{9}
\]
Summing (9) and using (3) plus conjugation symmetry yields the exact
positive sampling formula
\[
 \boxed{\quad
 2\lambda_n=\sum_\rho {1\over|\rho|^2}
 |\mathscr D_n(w_\rho)|^2
 =n\sum_\rho {1\over|\rho|^2}F_n(w_\rho).
 \quad}                                                          \tag{10}
\]
Therefore the strong-margin quantity has the conditional spectral form
\[
 \boxed{\quad
 D_n=\sum_\rho {1\over|\rho|^2}|\mathscr D_n(w_\rho)|^2
 -\lambda_n^{\rm arch}.
 \quad}                                                          \tag{11}
\]
This is the requested Fejer sampling representation.  It does **not** prove
the required lower bound: it is a positive atomic sampling formula only
after RH, and the subtraction of the archimedean scale remains.

The atomic measure in (10) is exactly the Herglotz measure calculated in
`103_24`.  Thus it has no separately available positive density that could
be inserted to dominate \(\lambda_n^{\rm arch}\).

## 3. Unconditional reciprocal sampling identity

Without RH, use the involution \(\rho^*=1-\bar\rho\).  From (6),
\(w_{\rho^*}=\overline{w_\rho}^{-1}\).  Applying this permutation to
(3) gives the exact real symmetric identity
\[
 2\lambda_n
 =\sum_\rho^*\left(2-w_\rho^n-
 \overline{w_\rho}^{-n}\right).                                  \tag{12}
\]
This is the only direct replacement for (10) supplied by the functional
equation.  It is not a positive Fejer kernel when \(|w_\rho|\ne1\).

Indeed, group a genuinely noncritical zero and all four distinct symmetry
partners.  Writing \(w_\rho=re^{i\theta}\), its quartet contribution to
\(2\lambda_n\) is
\[
 \boxed{\quad
 8-4\bigl(r^n+r^{-n}\bigr)\cos(n\theta).
 \quad}                                                          \tag{13}
\]
For \(r=1\), the four labels coalesce into the usual two-element conjugate
pair; one must then divide (13) by two.  The actual contribution of that
pair to \(2\lambda_n\) is
\[
 4-4\cos(n\theta)=2|1-e^{in\theta}|^2\ge0.
\]
Off the circle the quartet is distinct and (13) has both signs.

For a concrete adversarial choice, fix an \(n\) divisible by four, take
\(\theta=\pi/2\), and choose \(0<r<1\).  Then \(\cos(n\theta)=1\), so (13)
equals
\[
 8-4(r^n+r^{-n})<0.                                                \tag{14}
\]
The corresponding \(\rho=1/(1-re^{i\theta})\) satisfies
\(1/2<\Re\rho<1\), and its quartet obeys all functional and conjugation
symmetries.  Its multiplicity could also be repeated formally.  Hence no
coercive lower bound follows from functional pairing, conjugation, and the
strip alone.  In particular, pairing \(\rho\) with \(1-\rho\) does not
turn (12) into a Parseval square.

## 4. Parseval and de Branges circularity

Suppose one constructs a positive measure or de Branges/Parseval space whose
Dirichlet-vector norm equals the right side of (10) without first assuming
\(|w_\rho|=1\).  Its Toeplitz moments would make the increment kernel
positive.  Testing on \(\mathbf1_n\) gives
\[
 2\lambda_n\ge0\qquad(n\ge1),                                   \tag{15}
\]
which is Li positivity and hence RH.  If the claimed norm instead equals
\(D_n\), its nonnegativity gives the still stronger
\(\lambda_n\ge\lambda_n^{\rm arch}/2\).

Thus Parseval is a valid language for a proof, but not an independent source
of positivity.  To make its spectral support lie on \(\partial\mathbb D\)
is exactly to impose (5), i.e. RH.  The reciprocal quartet (13) is the
local algebraic obstruction to extending the square off the boundary.

## Status

The exact surviving scalar target is
\[
 \boxed{\quad
 2\lambda_n-\lambda_n^{\rm arch}\ge0\qquad(n\ge8),
 \quad}                                                          \tag{16}
\]
equivalently the integrated Dirichlet/Fejer lower bound in (11).  The full
Herglotz/Loewner strengthening is eliminated by `103_25`; functional pairing
cannot replace it by (13).  A new inequality controlling the particular
scalar energies in (16), directly from the paired Euler--Gamma expression,
would be RH-strength but is not supplied here.
