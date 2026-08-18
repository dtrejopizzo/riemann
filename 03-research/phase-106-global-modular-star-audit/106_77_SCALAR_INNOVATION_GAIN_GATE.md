# 106.77 — Scalar innovation gain for the cofinal staircase

## Purpose and conclusion

Documents 106.75--106.76 reduce finiteness of a staircase row to the
strict completed matrix inequality

\[
 \mathbf H_M\succ0.                                 \tag{1}
\]

The remaining matrix statement can be reduced further, without losing
any directional information.  After ordering the elementary zero modes,
each new row contributes exactly one scalar innovation.  If all preceding
rows are positive, then

\[
 \boxed{
 \mathbf H_M\succ0
 \quad\Longleftrightarrow\quad
 \sigma_M>0,}                                      \tag{2}
\]

where

\[
 \boxed{
 \sigma_M
 =h_M-c_M^*\mathbf H_{M-1}^{-1}c_M
 ={\det\mathbf H_M\over\det\mathbf H_{M-1}}
 =\mathcal A_\infty(q_M^*,q_M^*).}                 \tag{3}
\]

Here $q_M^*$ is the new zero mode after exact orthogonal regression against
the preceding modes in the **completed signed form**, not in the ambient
norm.  Formula (3) is the smallest scalar inequality left by the
mode--prime staircase.  It retains jointly Gamma, every literal
von Mangoldt atom, the pole/threshold subtraction, and the cross-mode
alignment which is lost by summing individual atom frame floors.

The scalar has the exact physical expression

\[
 \boxed{
 \sigma_M
 =\mathscr E_\Gamma(q_M^*)
  +\sum_{p^k}{\log p\over p^{k/2}}
       \mathcal J_{k\log p}(q_M^*)
  -{1\over2}\|q_M^*\|_{\mu_K}^2.}                 \tag{4}
\]

Thus the remaining global theorem is the sequence of strict scalar gains
$\sigma_M>0$.  A first nonpositive innovation is an explicit one-vector
certificate for failure of the corresponding staircase row.  Under a
form-core exhaustion, excluding such an innovation for every $M$ is
equivalent to the completed quotient sign; the scalarization does not
weaken that content.

## 1. Nested completed Gram matrices

Let

\[
 V_1\subset V_2\subset\cdots,
 \qquad \dim V_M=M,                                \tag{5}
\]

be a nested elementary mean-periodic exhaustion after projection away
from the constant and the complete radical.  Choose any ordered basis
$\phi_1,\phi_2,\ldots$ adapted to (5), and let

\[
 \mathcal A_\infty(q,s)
 =\mathscr E_K(q,s)-{1\over2}\langle q,s\rangle_{\mu_K}. \tag{6}
\]

Its Gram matrix on $V_M$ has the block form

\[
 \mathbf H_M
 =\begin{pmatrix}
   \mathbf H_{M-1}&c_M\\
   c_M^*&h_M
  \end{pmatrix},                                  \tag{7}
\]

where

\[
 (c_M)_j=\mathcal A_\infty(\phi_j,\phi_M),
 \qquad
 h_M=\mathcal A_\infty(\phi_M,\phi_M).           \tag{8}
\]

All entries in (7) are given by the absolutely convergent literal
prime--Gamma formula.  No zero-location hypothesis enters the block
algebra.

## 2. Exact one-scalar Schur recursion

Assume $\mathbf H_{M-1}\succ0$ and define

\[
 a_M=\mathbf H_{M-1}^{-1}c_M,
 \qquad
 q_M^*=\phi_M-\sum_{j=1}^{M-1}(a_M)_j\phi_j.      \tag{9}
\]

### Theorem 1 — Signed innovation identity

The vector $q_M^*$ satisfies

\[
 \mathcal A_\infty(v,q_M^*)=0
 \qquad(v\in V_{M-1}),                            \tag{10}
\]

and

\[
 \boxed{
 \mathcal A_\infty(q_M^*,q_M^*)
 =h_M-c_M^*\mathbf H_{M-1}^{-1}c_M
 =:\sigma_M.}                                    \tag{11}
\]

Moreover,

\[
 \boxed{
 \mathbf H_M\succ0
 \quad\Longleftrightarrow\quad
 \mathbf H_{M-1}\succ0\ \text{and}\ \sigma_M>0.} \tag{12}
\]

#### Proof

For $v=\sum_{j<M}v_j\phi_j$, equations (7)--(9) give

\[
 \mathcal A_\infty(v,q_M^*)
 =v^*(c_M-\mathbf H_{M-1}a_M)=0,
\]

which proves (10).  A second block expansion gives (11).  Finally,
congruence by

\[
 \begin{pmatrix}I&-a_M\\0&1\end{pmatrix}
\]

reduces $\mathbf H_M$ to

\[
 \mathbf H_{M-1}\oplus[\sigma_M].                \tag{13}
\]

Sylvester's law of inertia proves (12).  \(\square\)

### Corollary 2 — Determinant ratio

Whenever $\mathbf H_{M-1}\succ0$,

\[
 \boxed{
 \sigma_M={\det\mathbf H_M\over\det\mathbf H_{M-1}}.} \tag{14}
\]

This follows either from (13) or the block determinant formula.

Consequently, if the first row is positive, then

\[
 \boxed{
 \mathbf H_M\succ0\ \text{for every }M
 \quad\Longleftrightarrow\quad
 \sigma_M>0\ \text{for every }M.}                \tag{15}
\]

## 3. The literal physical scalar

The completed form is

\[
\begin{aligned}
 \mathcal A_\infty(q,q)
 ={}&\mathscr E_\Gamma(q)
 +\sum_{p^k}{\log p\over p^{k/2}}
      \int_{\mathbb R}K(x)K(x-k\log p)\\
 &\hspace{23mm}\times
      |q(x)-q(x-k\log p)|^2\,dx
 -{1\over2}\|q\|_{\mu_K}^2.                     \tag{16}
\end{aligned}
\]

Substitution of $q=q_M^*$ proves (4).  Every prime-power term in (4) is
nonnegative, but $q_M^*$ was selected using the complete signed matrix.
Thus its prime contributions remain directionally coupled through the
coefficients in (9).  Replacing them by the sum of their individual
minimum eigenvalues destroys precisely this coupling.

The finite-head value of the completed innovation vector is

\[
 \sigma_{M,X}
 :=\sup_{r\in\mathcal R_J}
 \mathcal A_X(q_M^*+r,q_M^*+r),                   \tag{17}
\]

when the radical anti-short coordinate is used.  Documents 106.72 and
106.75 imply

\[
 \sigma_{M,X}<\sigma_M,
 \qquad
 0\le\sigma_M-\sigma_{M,X}\le C_Me^{-cX}\|q_M^*\|^2. \tag{18}
\]

Hence $\sigma_M>0$ gives the explicit condition

\[
C_Me^{-cX}\|q_M^*\|^2<\sigma_M.                 \tag{19}
\]

for this particular innovation vector to become positive.  The full
frontier additionally requires the analogous bounds on all preceding
innovations and their tail-induced cross terms; equivalently one uses the
completed minimum $\delta_M$ in 106.75(19).  If $\sigma_M=0$, strict
omitted-tail positivity keeps $\sigma_{M,X}<0$ for every finite head.  If
$\sigma_M<0$, no head can repair the row.

## 4. Circularity audit

The scalarization (3) is algebraically exact, but it is not an independent
positivity source.  In the complete Krein coordinate,

\[
 \sigma_M
 =\|Aq_M^*\|^2-\|C^-q_M^*\|^2,               \tag{20}
\]

where $C^-$ is the off-line evaluation channel.  If an off-line quotient
state is accessible in the form-core closure, some finite innovation is
nonpositive.  Conversely, positivity of every innovation makes every
finite completed Gram positive and, after form-core synthesis, excludes
the negative channel.

Accordingly, none of the following proves $\sigma_M>0$:

* finite-dimensionality of $V_M$;
* nonvanishing of each prime atom on $V_M$;
* a positive sum of per-atom minimum eigenvalues;
* norm convergence of the prime bank;
* discreteness of the finite-head energy levels.

They prove that (4) is finite and observable, not that its signed value is
positive.  A proof of (4) must use the coupled alignment of the real
$\Lambda(p^k)$ channels with Gamma and the threshold subtraction.

## 5. Smallest remaining statement

After all convergence, radical, rank, and matrix bookkeeping have been
removed, the staircase closure is the following scalar theorem:

> **Literal innovation-gain theorem.**  For the nested ordinary-Riemann
> zero-mode exhaustion and every $M\ge1$, the signed regression residual
> $q_M^*$ defined by (9) satisfies
> \[
>  \mathscr E_\Gamma(q_M^*)
>  +\sum_{p^k}{\log p\over p^{k/2}}
>       \mathcal J_{k\log p}(q_M^*)
>  >{1\over2}\|q_M^*\|_{\mu_K}^2.                 \tag{21}
> \]

Equation (21) is sufficient and necessary, one scalar at a time.  It is
also directly certifiable at any fixed $M$ by outward interval evaluation
of (9) and (16).  A uniform proof of its sign along a form-core exhaustion
is the remaining global arithmetic input.
