# 106.86 — Complete adaptive-tail equivalence and finite capture

## Purpose and conclusion

Documents 106.77--106.83 derive the finite-head Schur residual, its
literal prime-by-prime Kalman updates, and finite matched-filter lower
bounds. This note performs the corresponding calculation for the
**entire omitted ordinary-prime tail**.

Fix one row of the mode staircase. Suppose the preceding-mode block is
positive at a finite cutoff \(X_0\), while the current Schur pivot is

\[
 \sigma_0=-\delta<0.
\]

Let \(E\) be the omitted-tail energy of the current signed regression
residual. The complete tail does not transfer all of \(E\) into the
Schur pivot. The exact decomposition is

\[
 \boxed{
 E=G_\infty+
 \left\|a_\infty-a\right\|_{A_\infty}^{2},}
 \tag{1}
\]

where \(G_\infty\) is the total adaptive Kalman gain and the second term
is the exact regression-adaptation loss. Consequently,

\[
 \boxed{
 \text{some finite prime head crosses}
 \quad\Longleftrightarrow\quad
 G_\infty>\delta
 \quad\Longleftrightarrow\quad
 \sigma_\infty>0.}
 \tag{2}
\]

Thus theta decay creates no further convergence gap: a strictly positive
completed pivot is captured by a finite head, with an exponential cutoff
bound. Conversely, the adaptive normal equation, strict observability of
every prime atom, the literal positive weights, and summability of the
tail do not force (2). An explicit two-mode countermodel below satisfies
all those abstract properties and retains a negative completed pivot.

The force-bearing comparison is not merely \(E>\delta\). It is

\[
 \boxed{
 E>\delta+b^*(A+P)^{-1}b,}
 \tag{3}
\]

where \(b\) is the old-mode cross response of the omitted tail. Formula
(3) is exactly the strict completed Schur pivot on the selected mode
space.

## 1. Finite-head residual and the complete omitted feature

Let

\[
 V_{M-1}=\operatorname{span}\{\phi_1,\ldots,\phi_{M-1}\}
 \subset V_M
\]

and let the signed finite-head matrix at \(X_0\) be

\[
 H_0=
 \begin{pmatrix}
  A&c\\
  c^*&h
 \end{pmatrix},
 \qquad A\succ0.                                  \tag{4}
\]

Define

\[
 a=A^{-1}c,
 \qquad
 q^*=\phi_M-\sum_{j<M}a_j\phi_j,
 \qquad
 \sigma_0=h-c^*A^{-1}c=-\delta<0.                \tag{5}
\]

For every prime power \(n=p^k>X_0\), put

\[
 w_n=\frac{\Lambda(n)}{\sqrt n}
     =\frac{\log p}{p^{k/2}},                    \tag{6}
\]

and use the literal displacement feature

\[
 (D_nq)(x)
 =\sqrt{K(x)K(x-\log n)}
   \{q(x)-q(x-\log n)\}.                         \tag{7}
\]

The complete omitted feature is the convergent direct sum

\[
 \mathcal D_{>X_0}q
 =\bigoplus_{n>X_0}\sqrt{w_n}\,D_nq.             \tag{8}
\]

On the fixed finite-dimensional space \(V_M\), convergence of (8) follows
from the double-exponential theta-tail estimate of 106.67. Write

\[
 U=\mathcal D_{>X_0}|_{V_{M-1}},
 \qquad
 v=\mathcal D_{>X_0}\phi_M,
 \qquad
 r=v-Ua=\mathcal D_{>X_0}q^*.                    \tag{9}
\]

Finally set

\[
 P=U^*U,
 \qquad
 b=U^*r,
 \qquad
 E=\|r\|^2.                                      \tag{10}
\]

Here \(E\) is the tail evaluated on the **initial** residual \(q^*\):

\[
 E=\sum_{n>X_0}\frac{\Lambda(n)}{\sqrt n}
       \mathcal J_{\log n}(q^*).                 \tag{11}
\]

It is not yet the adaptive gain.

## 2. Exact coefficient update

Adding the complete omitted feature changes the three blocks of (4) to

\[
 \begin{aligned}
  A_\infty&=A+U^*U=A+P,\\
  c_\infty&=c+U^*v,\\
  h_\infty&=h+\|v\|^2.
 \end{aligned}                                   \tag{12}
\]

Since \(v=r+Ua\) and \(c=Aa\),

\[
 c_\infty=(A+P)a+b=A_\infty a+b.                \tag{13}
\]

### Theorem 1 — Complete adaptive coefficient

The completed regression coefficient and residual are

\[
 \boxed{
 a_\infty=a+(A+P)^{-1}b,}                        \tag{14}
\]

\[
 \boxed{
 q_\infty^*
 =q^*-\Phi(A+P)^{-1}b,}                          \tag{15}
\]

where

\[
 \Phi y=\sum_{j<M}y_j\phi_j.
\]

#### Proof

By definition,

\[
 a_\infty=A_\infty^{-1}c_\infty.
\]

Substitution of (13) gives (14), and inserting the result in
\(q_\infty^*=\phi_M-\Phi a_\infty\) gives (15). \(\square\)

The vector

\[
 d:=a_\infty-a=(A+P)^{-1}b                       \tag{16}
\]

is the complete change in the old-mode regression.

## 3. Adaptive gain and the adaptation-loss identity

### Theorem 2 — Exact complete gain

The completed Schur pivot is

\[
 \boxed{
 \sigma_\infty=-\delta+G_\infty,}                \tag{17}
\]

where

\[
 \boxed{
 \begin{aligned}
 G_\infty
 &=E-b^*(A+P)^{-1}b\\
 &=\left\langle r,
  (I+UA^{-1}U^*)^{-1}r\right\rangle.
 \end{aligned}}                                  \tag{18}
\]

Moreover,

\[
 \boxed{
 E=G_\infty+\|d\|_{A+P}^2.}                      \tag{19}
\]

#### Proof

The block-Kalman identity of 106.80, applied to the convergent direct-sum
feature (8), gives the second line of (18). Woodbury gives

\[
 (I+UA^{-1}U^*)^{-1}
 =I-U(A+U^*U)^{-1}U^*,                           \tag{20}
\]

which yields the first line of (18). Therefore the new pivot is the old
pivot plus \(G_\infty\), proving (17).

Finally, (16) gives

\[
 \|d\|_{A+P}^2=b^*(A+P)^{-1}b=E-G_\infty,
\]

which proves (19). \(\square\)

The initial Schur normal equation gives

\[
 \mathcal A_{X_0}(w,q^*)=0
 \qquad(w\in V_{M-1}).                            \tag{21}
\]

After the tail is inserted, its cross functional is precisely \(b\):

\[
 \mathcal A_\infty(\Phi y,q^*)=y^*b.             \tag{22}
\]

Thus

\[
 \mathcal A_\infty(q^*,q^*)=-\delta+E,           \tag{23}
\]

and completed regression subtracts the exact square

\[
 b^*(A+P)^{-1}b.                                 \tag{24}
\]

This proves directly why positivity of (23) on the fixed residual is not
enough to make the completed Schur pivot positive.

## 4. Equivalent forms of finite crossing

Define the positive augmented Gram matrix

\[
 \mathcal K_\infty
 =\begin{pmatrix}
   A+P&b\\
   b^*&E
  \end{pmatrix}.                                 \tag{25}
\]

It is the Gram matrix of the old augmented columns
\((A^{1/2}e_j,Ue_j)\) and the new column \((0,r)\). Its Schur complement
over \(A+P\) is \(G_\infty\), so

\[
 \boxed{
 G_\infty
 =\frac{\det\mathcal K_\infty}{\det(A+P)}.}       \tag{26}
\]

### Theorem 3 — Complete adaptive-tail equivalence

The following statements are equivalent.

1. There exists a finite prime-power cutoff \(Y>X_0\) at which the
   \(M\)-th Schur pivot is positive.
2. \(G_\infty>\delta\).
3. The fixed tail energy satisfies

   \[
    E>\delta+b^*(A+P)^{-1}b.                     \tag{27}
   \]

4. The bordered determinant satisfies

   \[
    \det\mathcal K_\infty
    >\delta\det(A+P).                            \tag{28}
   \]

5. \(\sigma_\infty>0\).
6. The completed \(M\)-mode matrix is positive definite, assuming the
   completed preceding block is positive definite.

#### Proof

Equivalence of 2, 3, and 5 follows from (17)--(18). Formula (26) gives
equivalence with 4. Since the completed preceding principal block is
\(A+P\succ0\), the Schur-complement criterion gives equivalence of 5 and
6.

It remains to compare 1 and 2. Let \(G_Y\) be the exact adaptive gain
from the atoms \(X_0<n\le Y\). Prime-by-prime Kalman monotonicity gives

\[
 0\le G_Y\le G_Z<G_\infty
 \qquad(X_0<Y<Z<\infty),                         \tag{29}
\]

with strict inequalities whenever the newly inserted interval contains
at least one prime power. Strictness follows because every literal
displacement observes every nonzero finite zero-mode residual. Norm
convergence of the tail gives \(G_Y\uparrow G_\infty\). The finite pivot is

\[
 \sigma_Y=-\delta+G_Y.                           \tag{30}
\]

If \(G_\infty>\delta\), monotone convergence gives a finite \(Y\) with
\(G_Y>\delta\). Conversely, a finite crossing implies
\(G_\infty>G_Y>\delta\). This proves
\(1\Longleftrightarrow2\). \(\square\)

The strict alternatives are

\[
\begin{array}{c|c|c}
 \sigma_\infty&\sigma_Y\text{ for large finite }Y&
 \text{finite crossing}\\ \hline
 >0&>0&\text{yes}\\
 =0&<0\text{ and increasing to }0&\text{no}\\
 <0&<0&\text{no}.
\end{array}                                      \tag{31}
\]

## 5. One-row Christoffel and bordered-determinant test

For one scalar projected prime response, let

\[
 s=[\,u\ \ v\,]:\mathbb C^M\longrightarrow\mathbb C               \tag{32}
\]

be the weighted row; the factor
\(\sqrt{\Lambda(n)/\sqrt n}\) is already included. Its adaptive response
is

\[
 \eta=v-ua.                                      \tag{33}
\]

Because \(\sigma_0=-\delta\ne0\), block inversion gives

\[
 H_0^{-1}
 =\begin{pmatrix}
 A^{-1}-aa^*/\delta&a/\delta\\
 a^*/\delta&-1/\delta
 \end{pmatrix}.                                  \tag{34}
\]

Consequently,

\[
 \boxed{
 |\eta|^2
 =\delta\{uA^{-1}u^*-sH_0^{-1}s^*\}.}            \tag{35}
\]

The exact one-row gain is

\[
 \Delta_s
 =\frac{|\eta|^2}{1+uA^{-1}u^*}.                 \tag{36}
\]

### Theorem 4 — One-row crossing criterion

The following statements are equivalent:

\[
 \boxed{
 \begin{aligned}
  \sigma_0+\Delta_s&>0,\\
  -sH_0^{-1}s^*&>1,\\
  1+sH_0^{-1}s^*&<0,\\
  \det(H_0+s^*s)&>0.
 \end{aligned}}                                  \tag{37}
\]

#### Proof

Substitution of (35) in (36) gives

\[
 \frac{\Delta_s}{\delta}
 =\frac{uA^{-1}u^*-sH_0^{-1}s^*}
        {1+uA^{-1}u^*}.                           \tag{38}
\]

Thus \(\Delta_s>\delta\) is equivalent to
\(-sH_0^{-1}s^*>1\). The matrix determinant lemma gives

\[
 \det(H_0+s^*s)
 =\det H_0\{1+sH_0^{-1}s^*\}.                    \tag{39}
\]

Now \(\det H_0=-\delta\det A<0\), while the updated preceding principal
block \(A+u^*u\) is positive. Hence positivity of the updated determinant
is equivalent to positivity of its Schur pivot and to the negative sign
of the brace in (39). This proves (37). \(\square\)

If an unweighted row \(\ell=[\,u_0\ \ v_0\,]\) has weight \(w>0\), then
\(s=\sqrt w\,\ell\), and (37) becomes

\[
 \boxed{-w\,\ell H_0^{-1}\ell^*>1.}              \tag{40}
\]

## 6. Quantitative finite capture

Let \(q_Y^*\) be the adaptive residual after all atoms \(n\le Y\) have
been included, and let \(\mathcal T_Y\) be the remaining literal tail.
Applying the block-gain formula at the head \(Y\) gives

\[
 \begin{aligned}
 0\le G_\infty-G_Y
 &\le \mathcal T_Y(q_Y^*,q_Y^*)\\
 &\le C_Me^{-cY}\|q_Y^*\|_{\mu_K}^2.             \tag{41}
 \end{aligned}
\]

The family \(q_Y^*\) is bounded for fixed \(M\). Indeed, the preceding
blocks increase from \(A\succ0\), their inverses are uniformly bounded,
and their cross columns converge. Equivalently, \(a_Y\to a_\infty\).
Therefore

\[
 Q_M:=\sup_{Y\ge X_0}\|q_Y^*\|_{\mu_K}^2<\infty. \tag{42}
\]

Combining (41)--(42),

\[
 \boxed{
 0\le\sigma_\infty-\sigma_Y
 \le C_MQ_Me^{-cY}.}                             \tag{43}
\]

### Corollary 5 — Explicit capture schedule

If

\[
 m:=\sigma_\infty>0,                             \tag{44}
\]

then every cutoff satisfying

\[
 \boxed{C_MQ_Me^{-cY}<m}                         \tag{45}
\]

has \(\sigma_Y>0\). Thus it is enough that

\[
 Y>\frac1c\log\frac{C_MQ_M}{m}.                 \tag{46}
\]

The estimate assumes the displayed completed margin; it does not
manufacture that margin.

## 7. Countermodel: fixed tail energy need not become adaptive gain

The distinction in (19) is necessary even when every tail atom is
strictly observable and the weights have literal theta decay.

Take

\[
 H_0=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
 \qquad
 A=1,\qquad a=0,\qquad\delta=1.                  \tag{47}
\]

Let \(S=[\,U\ \ v\,]\) map \(\mathbb C^2\) to \(\mathbb C^2\), where

\[
 U=\binom{2}{0},
 \qquad
 v=\binom{\sqrt2}{1/2},
 \qquad
 S=\begin{pmatrix}2&\sqrt2\\0&1/2\end{pmatrix}.  \tag{48}
\]

The matrix \(S\) is injective. The fixed residual is \(r=v\), and

\[
 E=\|v\|^2=\frac94>\delta.                       \tag{49}
\]

Nevertheless,

\[
 P=4,\qquad b=2\sqrt2,
\]

so

\[
 \begin{aligned}
 G_\infty
 &=\frac94-\frac85\\
 &=\frac{13}{20}<1=\delta,
 \end{aligned}                                   \tag{50}
\]

and

\[
 \sigma_\infty=-1+\frac{13}{20}
 =-\frac7{20}<0.                                 \tag{51}
\]

To split this block into positive summable atoms, put

\[
 \widetilde b_n
 =\frac{\Lambda(n)}{\sqrt n}e^{-2\pi n},
 \qquad
 B=\sum_{n=p^k}\widetilde b_n,
 \qquad
 \alpha_n=\frac{\widetilde b_n}{B},              \tag{52}
\]

and define

\[
 D_n=\sqrt{\frac{\alpha_n}{w_n}}\,S.             \tag{53}
\]

Then

\[
 w_nD_n^*D_n=\alpha_nS^*S,                       \tag{54}
\]

every \(D_n\) is injective, every increment is strictly positive, and

\[
 \sum_{n=p^k}w_nD_n^*D_n=S^*S.                  \tag{55}
\]

The heads are monotone and converge with the literal
\(e^{-2\pi n}\) envelope, but every finite and completed pivot remains
negative. This countermodel does not reproduce the physical Riemann
displacement maps or their mean-periodic theta geometry. It proves that
those specific features, rather than Schur adaptivity, positive ordinary
weights, strict observability, or summability alone, must establish (3).

## 8. Final consequence

The complete omitted tail gives no hidden reserve beyond the completed
pivot. Its exact contribution is

\[
 \boxed{
 \sigma_\infty
 =-\delta
 +\mathcal T_{X_0}(q^*,q^*)
 -b^*(A+P)^{-1}b.}                               \tag{56}
\]

Therefore a proposed proof must establish one of the equivalent strict
inequalities (27)--(28) by using the actual theta translations and the
ordinary von Mangoldt phases. Once that strict completed margin is
obtained, finite capture follows automatically from (43)--(46); if the
margin is zero or negative, no finite selection of the same positive tail
can cross it.
