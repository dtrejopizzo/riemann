# 106.79 — A Fermi-staircase countermodel and the block-gain criterion

## Conclusion

There is an exact finite reversible Markov model with all of the abstract
features invoked by the energy-level argument:

* a constant ground state;
* an exact radical at energy \(1/2\);
* a discrete spectrum;
* strictly positive, full-rank prime sensors carrying the literal weights
  \(\Lambda(p^k)/p^{k/2}\);
* monotone finite heads and a norm-convergent omitted tail.

Nevertheless it has a bound state at energy \(1/4\), and no finite head
crosses the \(1/2\) threshold. Therefore discreteness, reversibility,
strict prime observability, and a threshold radical do not force
\(X_*(M)<\infty\). The specifically Riemannian mean-periodic geometry must
enter through a quantitative gain inequality.

The second result below gives the strongest elementary sufficient
condition which preserves complementarity among several primes: a
block-Kalman lower bound. Unlike sums of atomwise minimum eigenvalues, it
uses the minimum eigenvalue of the **joint block Gram**.

## 1. Exact three-level countermodel

Work on \(\mathbb R^3\) with its standard inner product and put

\[
 \mathbf 1=(1,1,1)^T,
 \qquad
 \Pi=I-\frac13\mathbf1\mathbf1^T.                  \tag{1}
\]

Let \(G\) be the graph Laplacian of the path \(1-2-3\), with both edge
weights equal to \(1/8\):

\[
 G=\frac18
 \begin{pmatrix}
  1&-1&0\\
  -1&2&-1\\
  0&-1&1
 \end{pmatrix}.                                   \tag{2}
\]

Its orthogonal eigenvectors

\[
 e_0=(1,1,1)^T,\quad
 e_-=(1,0,-1)^T,\quad
 e_R=(1,-2,1)^T                                   \tag{3}
\]

have eigenvalues \(0,1/8,3/8\), respectively.

Enumerate the prime powers \(n=p^k\). Put

\[
 w_n=\frac{\Lambda(n)}{\sqrt n},\qquad
 b_n=w_ne^{-2\pi n},\qquad
 B=\sum_{n=p^k}b_n<\infty,                         \tag{4}
\]

and define

\[
 a_n=\frac{b_n}{8B}>0,\qquad
 D_n=\sqrt{\frac{a_n}{w_n}}\,\Pi.                 \tag{5}
\]

Then every literal weighted sensor is

\[
 w_nD_n^*D_n=a_n\Pi,                              \tag{6}
\]

which is positive definite on the centered space, and

\[
 \sum_{n=p^k}w_nD_n^*D_n=\frac18\Pi.              \tag{7}
\]

For a finite prime-power head \(X\), set

\[
 L_X=G+s_X\Pi,\qquad
 s_X=\sum_{n\le X}a_n<\frac18.                    \tag{8}
\]

The completed generator is

\[
 L_\infty=G+\frac18\Pi.                           \tag{9}
\]

### Theorem 1 — Discrete levels need not cross

The operators \(L_X\) are reversible nonnegative graph generators,
\(L_X\uparrow L_\infty\) in norm, and every added prime-power channel is
strictly positive on the centered space. Nevertheless

\[
\begin{array}{c|ccc}
 &e_0&e_-&e_R\\ \hline
 L_X&0&1/8+s_X&3/8+s_X\\
 L_\infty&0&1/4&1/2.
\end{array}                                       \tag{10}
\]

Thus \(\mathcal R=\operatorname{span}\{e_R\}\) is an exact completed
threshold radical, while its orthogonal centered complement contains the
bound state \(e_-\) at \(1/4\). For every finite head,

\[
 \langle e_-,(L_X-\tfrac12)e_-\rangle<0.           \tag{11}
\]

Hence the staircase frontier of this complementary mode is infinite.

#### Proof

Equations (2) and (6) are graph Laplacians, so every \(L_X\) is a
reversible nonnegative generator and annihilates constants. Equations
(3), (7), and (8) diagonalize every member of the family and give (10).
Since every \(a_n>0\), all heads increase strictly on the centered space;
since their sum is \(1/8\), they converge in norm. Equation (11) follows
from \(1/8+s_X<1/4<1/2\). \(\square\)

The model does not reproduce the physical theta displacement maps or the
mean-periodic equation. It proves exactly that those special ingredients,
not generic energy-level discretization, must supply the missing sign.

## 2. Joint block-Kalman gain

Return to one \(M\)-mode row. Suppose the preceding-mode block \(A\) is
positive, its cross column is \(c\), and \(a=A^{-1}c\). Combine any finite
set \(\mathcal B\) of literal prime powers into one weighted feature map

\[
 \mathcal D_{\mathcal B}q
 =\bigoplus_{n\in\mathcal B}\sqrt{w_n}\,D_nq.       \tag{12}
\]

Write

\[
 U_{\mathcal B}=\mathcal D_{\mathcal B}|_{V_{M-1}},
 \qquad
 v_{\mathcal B}=\mathcal D_{\mathcal B}\phi_M,
 \qquad
 r_{\mathcal B}=v_{\mathcal B}-U_{\mathcal B}a.    \tag{13}
\]

### Theorem 2 — Exact block update and lower bound

Adding all atoms in \(\mathcal B\) simultaneously changes the adaptive
Schur innovation by

\[
 \boxed{
 \Delta_{\mathcal B}
 =\left\langle r_{\mathcal B},
 (I+U_{\mathcal B}A^{-1}U_{\mathcal B}^*)^{-1}
 r_{\mathcal B}\right\rangle.}                   \tag{14}
\]

In particular,

\[
 \boxed{
 \Delta_{\mathcal B}
 \ge
 \frac{\|r_{\mathcal B}\|^2}
 {1+\|U_{\mathcal B}\|^2/\lambda_{\min}(A)}.}     \tag{15}
\]

If

\[
 m_M(\mathcal B)
 =\lambda_{\min}\!\left(
 N_M^{-1/2}\mathcal D_{\mathcal B}^*
 \mathcal D_{\mathcal B}N_M^{-1/2}\right)         \tag{16}
\]

and \(\nu_M\) is the ambient innovation distance of 106.78(24), then

\[
 \boxed{
 \Delta_{\mathcal B}
 \ge
 \frac{m_M(\mathcal B)\nu_M}
 {1+\|U_{\mathcal B}\|^2/\lambda_{\min}(A)}.}     \tag{17}
\]

#### Proof

The proof of 106.78(12) applies verbatim to the direct-sum feature (12),
giving (14). The positive operator in (14) is bounded below by

\[
 (I+U_{\mathcal B}A^{-1}U_{\mathcal B}^*)^{-1}
 \succeq
 \frac{I}{1+\|U_{\mathcal B}\|^2/\lambda_{\min}(A)},
\]

which proves (15). The residual has coefficient one on the new mode, so
its ambient norm is at least \(\nu_M\); (16) therefore gives
\(\|r_{\mathcal B}\|^2\ge m_M(\mathcal B)\nu_M\), proving (17).
\(\square\)

## 3. A genuinely joint sufficient condition

Partition the remaining prime powers into finite consecutive blocks
\(\mathcal B_1,\mathcal B_2,\ldots\), updating \(A\), \(a\), and the
residual after every block. If the initial innovation is \(\sigma_0<0\),
then the row has a finite frontier whenever, for some finite \(R\),

\[
 \boxed{
 \sum_{j=1}^R
 \frac{m_M(\mathcal B_j)\nu_M}
 {1+\|U_{\mathcal B_j}\|^2/\lambda_{\min}(A_{j-1})}
 >-\sigma_0.}                                     \tag{18}
\]

This follows by summing (17). Unlike the atomwise bound, the block floor
\(m_M(\mathcal B_j)\) is the least eigenvalue of the sum of all Gram
channels in the block. It therefore retains the complementarity by which
different primes repair different nearly invisible directions.

Condition (18) is finite and can be certified by outward interval
arithmetic. It is not automatic: the countermodel in Theorem 1 violates
it in the \(e_-\) direction. For the Riemann system, proving (18) along a
cofinal form-core exhaustion is a concrete quantitative use of the
mean-periodic theta geometry which is stronger than observability and
strictly more informative than summing individual atom floors.

