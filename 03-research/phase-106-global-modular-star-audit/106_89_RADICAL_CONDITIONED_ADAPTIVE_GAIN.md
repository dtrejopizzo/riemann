# 106.89 — Radical-conditioned adaptive gain

## Purpose and conclusion

Documents 106.68 and 106.72 remove a finite exact-radical space by a
maximal anti-short, while 106.77--106.86 compute the adaptive Schur gain
of an ordinary-prime tail without that radical coordinate. This note
combines the two calculations.

The combination is exact. If \(V\) is the omitted-tail feature and
\(\mathcal R_J\) is a finite radical space, put

\[
 \Pi_J=I-P_{V\mathcal R_J}.
\]

After the radical has been maximized out, the correct tail feature is not
\(V\), but \(\Pi_JV\). If \(q_J^*\) is the Schur residual formed **after**
this radical anti-short, then the force-bearing tail vector is

\[
 \boxed{z_J=\Pi_JVq_J^*.}                         \tag{1}
\]

Its exact adaptive gain is

\[
 \boxed{
 G_J=\left\langle z_J,
 (I+\bar U\widehat A^{-1}\bar U^*)^{-1}z_J
 \right\rangle,}
 \qquad
 \bar U=\Pi_JV|_{V_{M-1}},                        \tag{2}
\]

where \(\widehat A\) is the preceding-mode block of the finite maximal
anti-short. Consequently, if its current pivot is
\(\widehat\sigma_X=-\delta_J<0\), the exact strict-surplus condition is

\[
 \boxed{G_J>\delta_J.}                            \tag{3}
\]

Equivalently, there must be one tail combiner \(\omega\) for which

\[
 \boxed{
 |\langle\omega,\Pi_JVq_J^*\rangle|^2
 >\delta_J\left(
 \|\omega\|^2+
 \|\widehat A^{-1/2}\bar U^*\omega\|^2
 \right).}                                       \tag{4}
\]

Finite-support combiners are enough in (4). Hence a strict directional
surplus has a finite prime-power witness and, by the cofinal frontier
theorem, produces a finite anti-short crossing.

The radical projection removes tail energy that can be synthesized by
radical corrections. It does **not** automatically improve the
adaptation-loss term, and it does not force (3). Explicit finite
counterexamples below show both facts. Thus (4), specialized to the
literal theta translations and the ordinary values
\(\Lambda(p^k)=\log p\), is a sharper statement of the remaining
arithmetic target, not a proof of its strict sign.

## 1. The exact three-block matrix

Fix one mode row

\[
 V_M=V_{M-1}\oplus\operatorname {span}\{\phi_M\},
\]

and a finite radical space

\[
 \mathcal R_J=\operatorname {span}\{r_1,\ldots,r_J\}.
\]

Choose coordinate maps

\[
 \Phi:\mathbb C^{M-1}\to V_{M-1},
 \qquad
 \Psi:\mathbb C^J\to\mathcal R_J.
\]

Let the completed defect on \(V_M\) have matrix

\[
 H_\infty=
 \begin{pmatrix}
  A_\infty&c_\infty\\
  c_\infty^*&h_\infty
 \end{pmatrix}.                                  \tag{5}
\]

The complete radical identity says that all completed matrix entries
involving \(\mathcal R_J\) vanish. For a finite prime head \(X\), let
\(V=V_X\) be the complete omitted-tail feature and write

\[
 U=V\Phi,
 \qquad
 v=V\phi_M,
 \qquad
 W=V\Psi.                                        \tag{6}
\]

The finite-head matrix on
\(V_{M-1}\oplus\operatorname {span}\{\phi_M\}\oplus\mathcal R_J\)
is therefore exactly

\[
 \boxed{
 \mathbb H_X=
 \begin{pmatrix}
 A_\infty-U^*U&c_\infty-U^*v&-U^*W\\
 c_\infty^*-v^*U&h_\infty-v^*v&-v^*W\\
 -W^*U&-W^*v&-W^*W
 \end{pmatrix}.}                                 \tag{7}
\]

By strict tail positivity on every finite radical space,

\[
 C:=W^*W\succ0.                                   \tag{8}
\]

Define

\[
 P_W=W(W^*W)^{-1}W^*,
 \qquad
 \Pi_J=I-P_W.                                     \tag{9}
\]

Thus \(P_W\) is the orthogonal projection onto
\(V\mathcal R_J=\operatorname {ran}W\).

### Theorem 1 — Exact radical anti-short

Maximizing the quadratic form (7) in the radical coordinate gives the
two-block mode matrix

\[
 \boxed{
 \widehat H_X
 =H_\infty-
 \begin{pmatrix}U^*\\v^*\end{pmatrix}
 \Pi_J
 \begin{pmatrix}U&v\end{pmatrix}.}               \tag{10}
\]

In particular,

\[
 \begin{aligned}
  \widehat A&=A_\infty-U^*\Pi_JU,\\
  \widehat c&=c_\infty-U^*\Pi_Jv,\\
  \widehat h&=h_\infty-v^*\Pi_Jv.
 \end{aligned}                                    \tag{11}
\]

#### Proof

The radical block in (7) is \(-C\). Its Schur complement is

\[
 H_\infty-
 \begin{pmatrix}U^*\\v^*\end{pmatrix}
 \begin{pmatrix}U&v\end{pmatrix}
 +
 \begin{pmatrix}U^*W\\v^*W\end{pmatrix}
 C^{-1}
 \begin{pmatrix}W^*U&W^*v\end{pmatrix}.
\]

Using (9) gives (10), hence (11). This is precisely the finite
tail-short formula of 106.72. \(\square\)

## 2. The correct residual after quotienting the radical

Assume

\[
 \widehat A\succ0.                                \tag{12}
\]

Define the anti-shorted regression coefficient, mode residual, and pivot

\[
 \widehat a=\widehat A^{-1}\widehat c,
 \qquad
 q_J^*=\phi_M-\Phi\widehat a,
 \qquad
 \widehat\sigma_X
 =\widehat h-\widehat c^*\widehat A^{-1}\widehat c.
                                                            \tag{13}
\]

The optimal radical coefficient attached to this mode residual is

\[
 \zeta_J^*=-(W^*W)^{-1}W^*Vq_J^*,                \tag{14}
\]

and the joint saddle residual is

\[
 \boxed{
 \widetilde q_J^*=q_J^*+\Psi\zeta_J^*.}           \tag{15}
\]

### Theorem 2 — Projected residual and source equation

The omitted-tail response of the joint residual is

\[
 \boxed{
 V\widetilde q_J^*
 =\Pi_JVq_J^*=z_J.}                               \tag{16}
\]

Moreover,

\[
 \boxed{
 \mathbb H_X
 \begin{pmatrix}-\widehat a\\1\\\zeta_J^*\end{pmatrix}
 =\widehat\sigma_X
 \begin{pmatrix}0\\1\\0\end{pmatrix}.}            \tag{17}
\]

Thus \(\widetilde q_J^*\), not the uncorrected mode residual, is the
stationary residual of the full old-mode/new-mode/radical saddle problem.

#### Proof

Equation (14) is the normal equation for minimizing

\[
 \|Vq_J^*+W\zeta\|^2
\]

in \(\zeta\). Substitution gives (16). The last block row of (17)
vanishes by (14). The first two block rows reduce, by the same
substitution, to

\[
 \widehat H_X
 \begin{pmatrix}-\widehat a\\1\end{pmatrix}
 =\begin{pmatrix}0\\\widehat\sigma_X\end{pmatrix},
\]

which is the Schur normal equation following from (13). \(\square\)

## 3. Exact radical-conditioned adaptive gain

Put

\[
 \bar U=\Pi_JU,
 \qquad
 \bar v=\Pi_Jv.                                   \tag{18}
\]

Since \(\Pi_J\) is an orthogonal projection, (10) becomes

\[
 H_\infty
 =\widehat H_X+
 \begin{pmatrix}\bar U^*\\\bar v^*\end{pmatrix}
 \begin{pmatrix}\bar U&\bar v\end{pmatrix}.       \tag{19}
\]

In particular,

\[
 A_\infty=\widehat A+\bar U^*\bar U.              \tag{20}
\]

The projected adaptive response is

\[
 \bar r=\bar v-\bar U\widehat a
 =\Pi_JVq_J^*=z_J.                                \tag{21}
\]

### Theorem 3 — Gain, loss, and strict surplus

Let \(\sigma_\infty\) be the Schur pivot of the completed matrix
\(H_\infty\). Then

\[
 \boxed{
 \sigma_\infty=\widehat\sigma_X+G_J,}             \tag{22}
\]

where

\[
 \boxed{
 \begin{aligned}
 G_J
 &=\langle\bar r,
 (I+\bar U\widehat A^{-1}\bar U^*)^{-1}\bar r\rangle\\
 &=\|\bar r\|^2-
 (\bar U^*\bar r)^*A_\infty^{-1}(\bar U^*\bar r).
 \end{aligned}}                                   \tag{23}
\]

The completed coefficient is

\[
 a_\infty
 =\widehat a+A_\infty^{-1}\bar U^*\bar r,         \tag{24}
\]

and the exact adaptation-loss decomposition is

\[
 \boxed{
 \|\bar r\|^2
 =G_J+\|a_\infty-\widehat a\|_{A_\infty}^2.}      \tag{25}
\]

If \(\widehat\sigma_X=-\delta_J<0\), the following are equivalent:

\[
 \boxed{
 \begin{aligned}
 \sigma_\infty&>0,\\
 G_J&>\delta_J,\\
 \|\Pi_JVq_J^*\|^2
 &>\delta_J+
 (\bar U^*\bar r)^*A_\infty^{-1}(\bar U^*\bar r).
 \end{aligned}}                                   \tag{26}
\]

#### Proof

Apply the complete adaptive-tail identity of 106.86 to the positive
update (19), with initial old block \(\widehat A\), old feature
\(\bar U\), new feature \(\bar v\), and response \(\bar r\). This gives
(22)--(25). Substituting
\(\widehat\sigma_X=-\delta_J\) in (22) proves (26). \(\square\)

By the cofinal frontier theorem, the strict conditions (26) are also
equivalent to positivity of this mode pivot at some later finite
maximal-radical anti-short. Equality gives monotone convergence to zero
from below and no finite crossing.

## 4. Exact directional criterion

The positive operator

\[
 M_J=I+\bar U\widehat A^{-1}\bar U^*              \tag{27}
\]

is bounded below by the identity. Hilbert-space duality gives

\[
 \boxed{
 G_J
 =\sup_{\omega\ne0}
 \frac{|\langle\omega,\Pi_JVq_J^*\rangle|^2}
 {\|\omega\|^2+
  \|\widehat A^{-1/2}\bar U^*\omega\|^2}.}        \tag{28}
\]

Indeed, this is the Rayleigh dual formula for
\(\langle\bar r,M_J^{-1}\bar r\rangle\); equality is attained at any
nonzero scalar multiple of \(M_J^{-1}\bar r\).

### Corollary 4 — Finite directional crossing certificate

If \(\widehat\sigma_X=-\delta_J<0\), the completed pivot is positive if
and only if there is a tail combiner \(\omega\) such that

\[
 \boxed{
 |\langle\omega,
 (I-P_{V\mathcal R_J})Vq_J^*\rangle|^2
 >\delta_J\left(
 \|\omega\|^2+
 \|\widehat A^{-1/2}
  (\Pi_JU)^*\omega\|^2
 \right).}                                       \tag{29}
\]

Finite-support tail combiners are dense. Because (29) is strict, it is
enough to find one supported on finitely many ordinary prime powers.
Such a witness proves \(\sigma_\infty>0\); monotonicity and cofinal
convergence then give a (possibly larger) finite anti-short cutoff.

Equation (29) is the exact radical-conditioned version of the matched
filter in 106.83. It asks for directional energy of the part of the
negative residual that cannot be reproduced by a radical correction,
while charging the complete old-mode regression leakage in the same
direction.

## 5. What the radical projection does and does not improve

For fixed \(A\succ0\), \(U\), and \(r\), define

\[
 \begin{aligned}
 E_\Pi&=\|\Pi r\|^2,\\
 L_\Pi&=(U^*\Pi r)^*(A+U^*\Pi U)^{-1}(U^*\Pi r),\\
 G_\Pi&=E_\Pi-L_\Pi.
 \end{aligned}                                    \tag{30}
\]

Then

\[
 G_\Pi
 =\min_d\left\{d^*Ad+\|\Pi(r-Ud)\|^2\right\}.     \tag{31}
\]

Consequently

\[
 0\le G_\Pi\le G_I,                               \tag{32}
\]

because an orthogonal projection decreases the objective in (31) for
every \(d\). Thus radical conditioning removes an irrelevant portion of
the positive update; it does not create extra gain.

The adaptation loss \(L_\Pi\) itself has no monotonicity. For example,
take \(A=1\),

\[
 U=\binom11,
 \qquad r=\binom1{-1},
 \qquad \Pi=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Then \(L_I=0\), while \(L_\Pi=1/2\). In the opposite direction, with
\(U=r=(1,0)^T\) and
\(\Pi=\operatorname {diag}(0,1)\), one has \(L_I=1/2\) and
\(L_\Pi=0\).

In the anti-short problem the current matrix also changes when the
projection is inserted:

\[
 H_\infty-S^*\Pi_JS\succeq H_\infty-S^*S.         \tag{33}
\]

Therefore radical conditioning reduces both the omitted defect and the
current deficit. Neither change alone decides (26); their exact balance
is the same completed pivot.

## 6. Counterexample: arbitrarily large raw energy with no surplus

The projected strict surplus does not follow from positive tail weights,
strict finite-dimensional observability, or large unprojected tail
energy.

Take no old mode, one new mode, one radical mode, and tail space
\(\mathbb R^2\). Let

\[
 h_\infty=-1,
 \qquad
 W=\binom10,
 \qquad
 v=\binom K\varepsilon,
 \qquad K>0,\quad\varepsilon>0.                   \tag{34}
\]

The full new-mode/radical feature \([v\ W]\) is injective. Here

\[
 \Pi_J=\begin{pmatrix}0&0\\0&1\end{pmatrix},
 \qquad
 \|v\|^2=K^2+\varepsilon^2,
 \qquad
 \|\Pi_Jv\|^2=\varepsilon^2.                      \tag{35}
\]

The finite new-mode/radical matrix is

\[
 \begin{pmatrix}
  -1-K^2-\varepsilon^2&-K\\
  -K&-1
 \end{pmatrix}.                                   \tag{36}
\]

Its maximal radical anti-short is

\[
 \widehat\sigma_X=-1-\varepsilon^2,               \tag{37}
\]

so \(\delta_J=1+\varepsilon^2\), while the entire projected adaptive
gain is only

\[
 G_J=\varepsilon^2<\delta_J.                      \tag{38}
\]

The completed pivot remains \(-1\). Meanwhile the raw tail energy
\(K^2+\varepsilon^2\) is arbitrarily large. The radical has synthesized
the entire \(K\)-component, leaving only the small transverse response.

As in 106.86, the positive feature Gram in this example can be split into
a summable sequence of injective positive atoms carrying the literal
coefficients \(\Lambda(p^k)/\sqrt{p^k}\) and an arbitrarily fast theta
envelope. The example is not the Riemann displacement system. It proves
that the missing strict inequality must use its specific theta and
mean-periodic geometry.

## 7. Exact surviving target

The maximal-radical extension changes the target from raw tail energy to
transverse directional energy. For every negative anti-short pivot, one
must prove from the literal ordinary-prime translations that there is a
finite-support \(\omega\) satisfying (29). Equivalently, one must prove

\[
 \boxed{
 \left\langle
 (I-P_{V\mathcal R_J})Vq_J^*,
 (I+\bar U\widehat A^{-1}\bar U^*)^{-1}
 (I-P_{V\mathcal R_J})Vq_J^*
 \right\rangle
 >\delta_J.}                                      \tag{39}
\]

This is genuinely sharper than the unconditioned fixed-energy test: it
retains old-mode adaptation and removes exactly the radical-synthesizable
tail. It is not logically stronger than the completed quotient sign.
By (22), it is exactly that sign written in the joint
old/new/radical tail coordinate.
