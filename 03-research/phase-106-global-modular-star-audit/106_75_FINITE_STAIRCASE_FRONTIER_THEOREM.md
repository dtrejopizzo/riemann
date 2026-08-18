# 106.75 — The finite staircase frontier theorem

## Purpose and conclusion

The mode--prime staircase of 106.72 is a monotone family of finite
Hermitian matrices.  It is tempting to infer that, because every row has
only finitely many energy levels and the omitted Euler bank tends to zero,
every row must cross the threshold after finitely many prime powers.  The
finite-dimensional spectral calculation can in fact be completed exactly.

For every fixed mode dimension $M$ and radical dimension $J$, let

\[
 \mathbf S_{M,J,X}
 =\mathbf H_M-\mathbf T_{X,/\mathcal R_J}              \tag{1}
\]

be the maximal radical anti-short of the finite head, as in 106.72.  Then
the tail short is **strictly positive definite** at every proper finite
head and tends to zero in norm.  Consequently

\[
 \boxed{
 X_*(M,J)<\infty
 \quad\Longleftrightarrow\quad
 \mathbf H_M\succ0 .}                               \tag{2}
\]

More precisely, the excess negative index eventually stabilizes at

\[
 \boxed{
 \kappa(M,J,X)
 =n_-(\mathbf H_M)+n_0(\mathbf H_M)
 \qquad(X\ge X_0(M,J)).}                            \tag{3}
\]

Thus a discrete staircase does stabilize, exactly as the energy-level
picture predicts.  What discreteness does not determine is the side of the
fixed threshold on which the limiting levels lie.  A completed zero level
approaches the threshold monotonically from below without crossing at any
finite head.  A completed negative level remains negative.  A finite
frontier occurs exactly when every completed level is strictly positive.

This theorem eliminates a possible ambiguity in the moving-filter
interpretation: the issue is not convergence of the literal prime bank.
That convergence is already proved.  The force-bearing statement is the
strict sign of the completed quotient Gram matrix.

## 1. Setup

Use the notation of 106.72.  The complete defect on $V_M$ is represented
by the Hermitian matrix $\mathbf H_M$.  For the omitted literal
prime-power bank, write

\[
 \mathbf T_{M,J,X}
 =
 \begin{pmatrix}
  \mathbf T^{VV}&\mathbf T^{VR}\\
  \mathbf T^{RV}&\mathbf T^{RR}
 \end{pmatrix}                                     \tag{4}
\]

on $V_M\oplus\mathcal R_J$.  Its short to $V_M$ is

\[
 \mathbf T_{X,/\mathcal R_J}
 =\mathbf T^{VV}
 -\mathbf T^{VR}(\mathbf T^{RR})^{-1}\mathbf T^{RV}. \tag{5}
\]

Let $\mathbf N_M\succ0$ be the norm Gram matrix on $V_M$, and put

\[
 \delta_M
 =\lambda_{\min}
 \left(\mathbf N_M^{-1/2}\mathbf H_M
                    \mathbf N_M^{-1/2}\right).     \tag{6}
\]

The finite inertia identity is

\[
 \kappa(M,J,X)
 =n_-(\mathbf S_{M,J,X}),                           \tag{7}
\]

and $X_*(M,J)$ is the first head for which this number vanishes.

## 2. The literal omitted bank has only the constant common kernel

### Lemma 1 — Strict tail positivity on every finite centered space

For every finite $X,M,J$,

\[
 \boxed{\mathbf T_{M,J,X}\succ0.}                  \tag{8}
\]

#### Proof

Let $q\in V_M\oplus\mathcal R_J$ and suppose that its omitted-tail
energy is zero.  Every summand has the literal nonnegative form

\[
 {\Lambda(n)\over\sqrt n}
 \int_{\mathbb R}K(x)K(x-\log n)
 |q(x)-q(x-\log n)|^2\,dx .                        \tag{9}
\]

Choose two distinct omitted primes $p,r>X$.  Since $K>0$, equation
(9) gives

\[
 q(x)=q(x-\log p)=q(x-\log r)                     \tag{10}
\]

almost everywhere and hence everywhere by continuity.  The quotient
$\log p/\log r$ is irrational: a rational relation would give
$p^a=r^b$ for nonzero integers $a,b$.  A continuous function with two
incommensurable periods is constant.  Every vector of
$V_M\oplus\mathcal R_J$ is centered, so that constant is zero.  Hence
the quadratic form in (8) has trivial kernel.  It is represented on a
finite-dimensional space, and is therefore positive definite.  \(\square\)

### Corollary 2 — Strict positivity of the tail short

For every finite $X,M,J$,

\[
 \boxed{\mathbf T_{X,/\mathcal R_J}\succ0.}        \tag{11}
\]

#### Proof

The lower-right block of the positive-definite matrix (4) is positive
definite.  Congruence by block Gaussian elimination gives

\[
 \mathbf T_{M,J,X}
 \sim
 \mathbf T_{X,/\mathcal R_J}\oplus\mathbf T^{RR}.
\]

Sylvester's law of inertia proves (11).  Equivalently,

\[
 v^*\mathbf T_{X,/\mathcal R_J}v
 =\inf_{r\in\mathcal R_J}\mathcal T_X(v+r,v+r),
\]

and a zero infimum is attained in finite dimension and would contradict
Lemma 1.  \(\square\)

Define the strictly positive normalized tail level

\[
 \eta_{M,J,X}
 :=\lambda_{\min}\!\left(
 \mathbf N_M^{-1/2}\mathbf T_{X,/\mathcal R_J}
 \mathbf N_M^{-1/2}\right)>0.                     \tag{12}
\]

The superexponential tail estimate and the order property of a short give

\[
 0<\eta_{M,J,X}\le
 \left\|\mathbf N_M^{-1/2}
 \mathbf T_{X,/\mathcal R_J}\mathbf N_M^{-1/2}
 \right\|
 \le C_Me^{-cX}.                                   \tag{13}
\]

In particular the finite tail is nonzero at every step, but it tends to
zero.

## 3. Exact stabilization of the discrete energy levels

Let

\[
 \widetilde H
 =\mathbf N_M^{-1/2}\mathbf H_M\mathbf N_M^{-1/2},
 \qquad
 \widetilde T_X
 =\mathbf N_M^{-1/2}\mathbf T_{X,/\mathcal R_J}
                      \mathbf N_M^{-1/2}.          \tag{14}
\]

Then

\[
 \widetilde S_X=\widetilde H-\widetilde T_X,
 \qquad
 \widetilde T_X\succ0,
 \qquad
 \|\widetilde T_X\|\longrightarrow0.             \tag{15}
\]

### Theorem 3 — Eventual inertia formula

There is a finite $X_0(M,J)$ such that

\[
 \boxed{
 n_-(\widetilde S_X)
 =n_-(\widetilde H)+n_0(\widetilde H)
 \quad(X\ge X_0(M,J)).}                            \tag{16}
\]

#### Proof

Let $E_-$, $E_0$, and $E_+$ be the negative, null, and positive
spectral subspaces of $\widetilde H$.  On $E_-\oplus E_0$,

\[
 \langle v,\widetilde S_Xv\rangle
 =\langle v,\widetilde Hv\rangle
  -\langle v,\widetilde T_Xv\rangle<0              \tag{17}
\]

for every nonzero $v$, because the first term is nonpositive and the
second is strictly positive.  Therefore

\[
 n_-(\widetilde S_X)
 \ge n_-(\widetilde H)+n_0(\widetilde H).          \tag{18}
\]

Let

\[
 g_+=\min\bigl(\sigma(\widetilde H)\cap(0,\infty)\bigr)
\]

when $E_+\ne0$.  For sufficiently large $X$, (15) gives
$\|\widetilde T_X\|<g_+$.  Weyl's eigenvalue perturbation inequality
then prevents any positive eigenvalue of $\widetilde H$ from crossing
zero.  Hence the right side of (18) is also an upper bound.  If
$E_+=0$, (18) already equals the full dimension.  This proves (16).
\(\square\)

Combining (7) and (16) proves the announced stabilization law (3).

### Theorem 4 — Exact finite-frontier criterion

For every fixed $M,J$, the following are equivalent:

1. $X_*(M,J)<\infty$;
2. $\mathbf S_{M,J,X}\succeq0$ for some finite $X$;
3. $\mathbf H_M\succ0$.

If these conditions hold, every cutoff satisfying

\[
 C_Me^{-cX}<\delta_M                              \tag{19}
\]

lies beyond the frontier.

#### Proof

Condition 3 and (13) imply

\[
 \widetilde S_X
 \succeq(\delta_M-C_Me^{-cX})I,
\]

which proves $3\Rightarrow2\Rightarrow1$.  Conversely, if
$\widetilde S_X\succeq0$, then

\[
 \widetilde H=\widetilde S_X+\widetilde T_X\succ0
\]

by (11).  Thus $2\Rightarrow3$.  Equivalence of 1 and 2 is the finite
inertia identity (7).  \(\square\)

## 4. The threshold level does not cross at a finite head

The two-sided estimate

\[
 \boxed{
 \delta_M-C_Me^{-cX}
 \le\lambda_{\min}(\widetilde S_X)
 \le\delta_M-\eta_{M,J,X}}                        \tag{20}
\]

follows from (13), the min--max principle, and
$\widetilde T_X\succeq\eta_{M,J,X}I$.

If $\delta_M=0$ and $\widetilde H\succeq0$, formula (20) becomes

\[
 -C_Me^{-cX}
 \le\lambda_{\min}(\widetilde S_X)
 \le-\eta_{M,J,X}<0.                              \tag{21}
\]

Therefore the least level increases to zero but is negative at every
finite prime head.  This is not a numerical artifact and is not excluded
by discretization.  The scalar model

\[
 s_X=-\sum_{p>X}(\log p)p^2e^{-2\pi p}             \tag{22}
\]

has precisely the same literal step structure: every increment is
positive, the total omitted strength tends to zero, and no finite step
reaches zero.

If $\delta_M<0$, then

\[
 \lambda_{\min}(\widetilde S_X)\le\delta_M<0      \tag{23}
\]

for every finite $X$.  Thus a completed negative bound state cannot be
repaired by adding more of a positive bank whose complete sum already
defines that state.

## 5. Spectral interpretation and the remaining sign

For a discrete Fermi-type spectrum, finite-dimensionality guarantees that
each isolated limiting level has a stable eventual inertia.  Theorem 3 is
that statement for the literal prime staircase.  It separates three
cases:

\[
\begin{array}{c|c|c}
\text{completed level}&\text{finite heads}&\text{frontier}\\ \hline
\delta>0&\text{eventually positive}&X_*<\infty\\
\delta=0&\text{negative and increasing to }0&X_*=\infty\\
\delta<0&\text{eventually negative}&X_*=\infty.
\end{array}                                       \tag{24}
\]

The exact radical removes the known threshold eigenspace, but that fact
alone does not exclude negative bound states on its complement.  In the
Krein factorization of 106.64, those states are exactly the accessible
off-line evaluation channel.  Hence the statement

\[
 \mathbf H_M\succ0\quad\text{for every member of a form-core exhaustion}
                                                               \tag{25}
\]

is the force-bearing sign assertion.  Together with the weighted
form-core synthesis theorem, (25) excludes every negative quotient state
and yields the Riemann closure.  The finite staircase then supplies an
explicit finite certificate for every row through (19).

What has been proved here is that there is no additional convergence or
level-discretization gap between (25) and finite frontier attainment: once
the completed level is strictly positive, the frontier is automatically
finite, and if it is nonpositive no finite prime head can make it cross.

## 6. Reusable criterion

Any proposed proof that $X_*(M,J)$ is finite should now be checked at the
completed head.  It is enough, and necessary, to prove one of the
equivalent estimates

\[
\boxed{
\begin{aligned}
 &\mathbf H_M\succ0,\\
 &s_{\min}(A_M)>\|C_M^-\|,\\
 &\mathbf T_{X,/\mathcal R_J}\prec\mathbf H_M
   \quad\text{for one finite }X.
\end{aligned}}                                    \tag{26}
\]

The first line is the completed quotient sign, the second is its exact
positive-versus-negative Krein contraction, and the third is its finite
literal-prime certificate.  Prime-tail convergence proves that the third
line follows from the first; it does not prove the first line.
