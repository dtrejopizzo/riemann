# 106.78 — Literal-atom Kalman updates for the scalar innovation

## Purpose and conclusion

Document 106.77 reduces the completed \(M\)-mode Gram sign to a scalar
Schur innovation.  The next question is whether that scalar can be tracked
prime by prime without destroying the cross-mode alignment.  It can.

Suppose the preceding \((M-1)\)-mode block is positive at a given finite
head.  When the literal prime power \(n=p^k\) is added, with its actual
weight

\[
 w_n={\Lambda(n)\over\sqrt n}={\log p\over p^{k/2}},             \tag{1}
\]

the adaptive finite-head innovation satisfies the exact Kalman formula

\[
\boxed{
\sigma_{M,+}-\sigma_{M,-}
=w_n\left\langle r_{n,-},
\left(I+w_nU_nA_-^{-1}U_n^*\right)^{-1}r_{n,-}
\right\rangle_{\mathcal Y_n}.}                    \tag{2}
\]

Here \(A_-\) is the preceding-mode Gram block before the atom is added,
\(U_n\) is the full displacement feature restricted to the preceding
modes, and \(r_{n,-}\) is the displacement feature of the current signed
regression residual.  No rank-one replacement is made in (2).

Every factor on the right of (2) is positive, and the increment is
strictly positive because one literal displacement observes every
nonzero finite zero-mode vector.  Iteration gives an exact positive series
for the completed innovation.

This is the strongest update statement supplied by prime-by-prime
positivity.  It does not by itself force a crossing: theta localization
makes the cumulative large-prime gain summable.  The row closes exactly
when the positive Kalman series exceeds the finite deficit present when
the preceding row has closed.  A determinant lower-frame bound is
available, but diagnostics show that it is much too small; the exact
directional series (2) must be retained.

## 1. Finite-head blocks and literal feature maps

Let

\[
 V_M=\mathrm{span}\,\{\phi_1,\ldots,\phi_M\},
 \qquad V_{M-1}\subset V_M,                         \tag{3}
\]

be one stage of the elementary zero-mode exhaustion.  For a head \(X\),
write the finite signed Gram matrix as

\[
 H_{M,X}=
 \begin{pmatrix}
 A_X&c_X\\
 c_X^*&h_X
 \end{pmatrix},                                    \tag{4}
\]

where \(A_X=H_{M-1,X}\).  Whenever \(A_X\succ0\), define the adaptive
finite-head innovation

\[
\boxed{
\begin{aligned}
 a_{M,X}&=A_X^{-1}c_X,\\
 q_{M,X}^*&=\phi_M-\sum_{j<M}(a_{M,X})_j\phi_j,\\
 \sigma_{M,X}
 &=h_X-c_X^*A_X^{-1}c_X
 =\mathcal A_X(q_{M,X}^*,q_{M,X}^*).
\end{aligned}}                                     \tag{5}
\]

This \(\sigma_{M,X}\) is the actual Schur pivot of the finite head.  It
must be distinguished from evaluating the *completed* regression vector
\(q_M^*\) in a finite head; the latter does not adapt when the earlier
block changes.

For \(n=p^k\), put \(u_n=\log n\) and define the unweighted displacement
feature

\[
\begin{aligned}
 \mathcal Y_n&=L^2(\mathbb R,dx),\\
 (D_nq)(x)
 &=\sqrt{K(x)K(x-u_n)}\,
       \{q(x)-q(x-u_n)\}.
\end{aligned}                                      \tag{6}
\]

Thus

\[
 \|D_nq\|_{\mathcal Y_n}^2=\mathcal J_{u_n}(q).    \tag{7}
\]

Relative to (3), write

\[
 U_n=D_n|_{V_{M-1}}:\mathbb C^{M-1}\to\mathcal Y_n,
 \qquad v_n=D_n\phi_M\in\mathcal Y_n.              \tag{8}
\]

Adding the atom \(n\) changes (4) by the complete Gram increment

\[
\boxed{
 w_n
 \begin{pmatrix}
 U_n^*U_n&U_n^*v_n\\
 v_n^*U_n&\langle v_n,v_n\rangle
 \end{pmatrix}.}                                   \tag{9}
\]

Equation (9) contains the complete divisor/fractional/central atom of
106.38.  No midpoint rank-one asymptotic has been used.

## 2. Exact Kalman--Schur update

Suppress \(M,X,n\) temporarily and put

\[
 A=A_X,\quad c=c_X,\quad h=h_X,\quad
 a=A^{-1}c,\quad r=v-Ua=D_nq_{M,X}^*.              \tag{10}
\]

After adding \(wD_n^*D_n\), the three blocks become

\[
\begin{aligned}
 A_+&=A+wU^*U,\\
 c_+&=c+wU^*v,\\
 h_+&=h+w\|v\|^2.
\end{aligned}                                      \tag{11}
\]

### Theorem 1 — Full-feature innovation formula

If \(A\succ0\), then

\[
\boxed{
\sigma_+
=\sigma_-
+w\langle r,(I+wUA^{-1}U^*)^{-1}r\rangle.}        \tag{12}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
\sigma_+-\sigma_-
={}&w\|r\|^2\\
&-w^2\left\langle
 U^*r,(A+wU^*U)^{-1}U^*r
\right\rangle.
\end{aligned}}                                     \tag{13}
\]

#### Proof

For \(y\in\mathbb C^{M-1}\), write the coefficient of the new mode as
one and the preceding coefficients as \(-a+y\).  Completion of the
square for the old signed matrix gives

\[
 \mathcal A_X(q_{M,X}^*+\Phi y)
 =\sigma_-+\langle y,Ay\rangle,                    \tag{14}
\]

where \(\Phi y=\sum_{j<M}y_j\phi_j\).  The added atom contributes

\[
 w\|r+Uy\|^2.                                      \tag{15}
\]

Therefore

\[
 \sigma_+
 =\sigma_-+
 \min_y\{\langle y,Ay\rangle+w\|r+Uy\|^2\}.        \tag{16}
\]

The normal equation is

\[
 (A+wU^*U)y=-wU^*r.                                \tag{17}
\]

Substitution in (16) gives (13).  The Woodbury identity

\[
 I-wU(A+wU^*U)^{-1}U^*
 =(I+wUA^{-1}U^*)^{-1}                             \tag{18}
\]

turns (13) into (12).  \(\square\)

Since \(UA^{-1}U^*\succeq0\), (12) immediately gives

\[
 0\le\sigma_+-\sigma_-\le w\|r\|^2.               \tag{19}
\]

The inequalities are strict on the left in the present setting.
Indeed \(q_{M,X}^*\ne0\), and Theorem 1 of 106.76 proves that
\(D_nq_{M,X}^*\ne0\) for every \(u_n>0\).  Hence \(r\ne0\), while the
inverse in (12) is strictly positive.

### Corollary 2 — Rank-one sensor

If a feature component is scalar, let \(u\in\mathbb C^{M-1}\) be its row
on the old modes and \(v\in\mathbb C\) its value on \(\phi_M\).  Then

\[
\boxed{
\sigma_+-\sigma_-
={w\,|v-u^*a|^2\over1+w\,u^*A^{-1}u}.}            \tag{20}
\]

This is the literal scalar Kalman innovation.  In the large-prime
midpoint regime of 106.73, (20) is the leading term, while (12) retains
the full atom and its additive error without division by a possibly
vanishing leading sample.

## 3. Coupling flow and a certified lower bound

There is an equivalent continuous-coupling form which is useful for
lower estimates.  For \(0\le t\le w_n\), set

\[
 H_M(t)=H_{M,X}+tD_n^*D_n                         \tag{21}
\]

and let \(q_M^*(t)\) be its adaptive regression residual, defined as in
(5).  The envelope theorem here is just differentiation of a finite
quadratic minimum.

### Theorem 3 — Innovation flow

\[
\boxed{
 {d\over dt}\sigma_M(t)
 =\mathcal J_{u_n}(q_M^*(t))>0,}                  \tag{22}
\]

and consequently

\[
\boxed{
 \sigma_+-\sigma_-
 =\int_0^{w_n}\mathcal J_{u_n}(q_M^*(t))\,dt.}    \tag{23}
\]

#### Proof

Equation (16), with \(w\) replaced by \(t\), represents
\(\sigma_M(t)\) as the minimum of a differentiable strictly convex
quadratic in \(y\).  Differentiating at its unique minimizer eliminates
the derivative of that minimizer and leaves
\(\|D_nq_M^*(t)\|^2\).  Strict positivity follows from 106.76.  Integration
proves (23).  \(\square\)

Let \(N_M\) be the ambient norm Gram and define the positive ambient
innovation

\[
 \nu_M
 :=\min_{a\in\mathbb C^{M-1}}
 \left\|\phi_M-\sum_{j<M}a_j\phi_j\right\|_{\mu_K}^2
 >0.                                               \tag{24}
\]

With the normalized atom floor \(m_{V_M}(u)\) from 106.76,

\[
 \mathcal J_u(q)\ge m_{V_M}(u)\|q\|_{\mu_K}^2
 \qquad(q\in V_M).                                 \tag{25}
\]

Every regression residual in (23) has coefficient one on \(\phi_M\), so
its ambient norm is at least \(\nu_M\).  Therefore

\[
\boxed{
\sigma_+-\sigma_-
\ge w_n\,m_{V_M}(u_n)\nu_M.}                      \tag{26}
\]

A directional lower estimate, often much sharper than (26), follows
directly from (12):

\[
\boxed{
\sigma_+-\sigma_-
\ge
{w_n\,\mathcal J_{u_n}(q_{M,X}^*)
\over
1+w_n\|U_n\|^2/\lambda_{\min}(A_X)}.}              \tag{27}
\]

## 4. Exact prime-by-prime induction

Enumerate the prime powers increasingly:

\[
 2=n_1<n_2<\cdots,\qquad n_\ell=p_\ell^{k_\ell}.  \tag{28}
\]

Assume row \(M-1\) has already closed.  Enlarge its closing head by one
atom if necessary so that

\[
 A_{\ell_0}=H_{M-1,n_{\ell_0}}\succ0.              \tag{29}
\]

For \(\ell>\ell_0\), let \(\Delta_{M,\ell}\) denote the right side of
(2), evaluated adaptively just before \(n_\ell\) is inserted.

### Theorem 4 — Cumulative literal innovation

For every \(L>\ell_0\),

\[
\boxed{
\sigma_{M,n_L}
=\sigma_{M,n_{\ell_0}}
+\sum_{\ell=\ell_0+1}^{L}\Delta_{M,\ell},
\qquad \Delta_{M,\ell}>0.}                        \tag{30}
\]

If the completed preceding block has a positive gap, the limit exists and

\[
\boxed{
\sigma_M
=\sigma_{M,n_{\ell_0}}
+\sum_{\ell>\ell_0}\Delta_{M,\ell}.}              \tag{31}
\]

The \(M\)-th staircase row closes after finitely many ordinary prime
powers if and only if

\[
\boxed{
\sum_{\ell>\ell_0}\Delta_{M,\ell}
>-\sigma_{M,n_{\ell_0}}.}                         \tag{32}
\]

If equality holds in (32), every finite head remains negative and tends
to zero.

#### Proof

Apply Theorem 1 successively to obtain (30).  The finite-head matrices
converge in norm to their completed matrices.  Positivity of the
completed preceding block makes inversion continuous from some point
onward, so the Schur pivots converge to the completed pivot \(\sigma_M\).
This proves (31).

All partial sums in (30) are strictly increasing.  They cross zero at a
finite index exactly when their limit is positive, which is (32).
When the limit is zero, strict positivity of every omitted tail makes
each proper partial sum strictly smaller than zero.  \(\square\)

Theorem 4 is an exact induction scheme:

\[
\boxed{
\text{close row }M-1
\ \longrightarrow\
\text{accumulate literal Kalman gains}
\ \longrightarrow\
\text{close row }M.}                              \tag{33}
\]

It retains all cross-prime effects because the regression vector is
updated after every atom.

## 5. Does the certified lower bound force a crossing?

Summing (26) gives the rigorous sufficient condition

\[
\boxed{
\sigma_{M,n_{\ell_0}}
+\nu_M
\sum_{\ell>\ell_0}
{\Lambda(n_\ell)\over\sqrt{n_\ell}}\,
m_{V_M}(\log n_\ell)>0.}                          \tag{34}
\]

This is a theorem with the real ordinary weights.  It is not strong enough
to prove the cofinal crossing.  The reason is quantitative rather than
algebraic.

First, for fixed \(M\), theta localization gives

\[
{\Lambda(n)\over\sqrt n}
\|D_n|_{V_M}\|^2
\ll_M(\log n)n^{2+b}e^{-2\pi n},                 \tag{35}
\]

with \(b<1/2\) determined by the finite strip block.  Hence both the exact
Kalman series in (31) and the lower series in (34) are convergent.  The
infinitely many positive prime levels therefore supply a finite total
gain, not a divergent reservoir which must cross every deficit.

Second, the scalar lower-frame estimate discards directional
complementarity.  The diagnostic in 106.76(30) already shows a four-mode
head whose exact combined margin is positive even though the sum of the
individual least atom gains is more than an order of magnitude below the
Gamma deficit.  Thus (34) can fail while the exact Kalman sum (32)
succeeds.

Finally, (31) gives the identity

\[
\boxed{
\sigma_{M,n_{\ell_0}}
+\sum_{\ell>\ell_0}\Delta_{M,\ell}
=\sigma_M.}                                       \tag{36}
\]

Consequently, proving (32) uniformly is exactly proving the completed
innovation \(\sigma_M>0\).  The update algebra does not manufacture that
sign.

## 6. Verdict and next quantitative target

The prime-by-prime calculation has now been completed:

* the full literal atom has the exact positive Kalman update (2);
* the update is strict for every finite zero-mode row;
* its rank-one midpoint limit is (20);
* the adaptive gains telescope exactly to the completed innovation;
* the real-weight lower bound (34) is rigorous.

What remains is not a hidden Schur term.  It is the arithmetic gain
inequality

\[
\boxed{
\sum_{\ell>\ell_0}
{\Lambda(n_\ell)\over\sqrt{n_\ell}}
\left\langle r_{\ell,-},
\left(
I+{\Lambda(n_\ell)\over\sqrt{n_\ell}}\,
U_\ell A_{\ell-}^{-1}U_\ell^*
\right)^{-1}
r_{\ell,-}
\right\rangle
>-\sigma_{M,n_{\ell_0}}.}                         \tag{37}
\]

Unlike the sum of per-atom minimum eigenvalues, (37) preserves the
directional adaptation responsible for the observed crossings.  But by
(36), it is equivalent to the strict completed \(M\)-th pivot.  A proof
must therefore exploit a new quantitative relation between the actual
ordinary-prime phases and the Gamma deficit; positivity, discretization,
and summability alone do not decide it.
