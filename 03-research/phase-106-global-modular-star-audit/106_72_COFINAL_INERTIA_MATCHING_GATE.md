# 106.72 — Cofinal inertia matching and the mode--prime staircase

## Purpose and verdict

The observed effect has an exact finite-dimensional interpretation. A prime
head may repair the defect on a fixed mode space, while admitting a new mode
can expose a new negative direction and force the prime head to move again.
This is not a scalar moving average. It is an inertia matching problem.

Let \(V_M\) be a nested Galerkin mode space in the complement of the complete
Riemann radical, let \(\mathcal R_J\) be the span of the first \(J\)
centered radical modes, and let \(\mathcal A_X\) be the
Gamma-plus-\(p^k\le X\) defect at the fixed threshold \(1/2\).

Every proper finite head is strictly negative on \(\mathcal R_J\). The
finite certificate is

\[
 \boxed{
 n_-\!\left(\mathcal A_X|_{V_M\oplus\mathcal R_J}\right)=J.}
                                                               \tag{1}
\]

Haynsworth additivity proves that (1) is equivalent to nonnegativity of the
maximal radical anti-short on \(V_M\). It is therefore a valid sufficient
certificate for nonnegativity of the completed form on \(V_M\).

The excess negative index is nonincreasing when the prime cutoff \(X\)
grows, nondecreasing when the mode space \(V_M\) grows, and nonincreasing
when the radical space \(\mathcal R_J\) grows. This is the rigorous
mode--prime staircase. A head ending at \(7\) may close one row and fail
after more modes are admitted.

If the completed normalized gap on \(V_M\) is \(\delta_M>0\), the theta
tail gives the sufficient schedule

\[
 X(M)>{1\over c}\log {C_M\over\delta_M}.            \tag{2}
\]

A vanishing threshold compensation gives an exact cofinal criterion even
when strict finite gaps are not assumed.

Loewner monotonicity and interlacing prove the staircase; they do not force
the excess index to reach zero. CCM finite self-adjointness does not prove
(1): CCM shifts by a moving least Ritz value and removes the resulting
moving radical, whereas (1) retains the fixed threshold \(1/2\) and the
exact Riemann radical. The remaining finite matrix inequality is (21).

## 1. Complete and finite-head defects

Work in the real even centered space

\[
 \mathcal H_0
 =\left\{q\in L^2(\mu_K):\int q\,d\mu_K=0\right\}.  \tag{3}
\]

The complete defect is

\[
 \mathcal A_\infty(q,s)
 =\mathscr E_K(q,s)-{1\over2}\langle q,s\rangle_{\mu_K}. \tag{4}
\]

For \(X\ge2\), retain Gamma and the literal ordinary-prime-power atoms
\(p^k\le X\):

\[
\begin{aligned}
 \mathcal A_X(q,s)
 &:=\mathscr E_\Gamma(q,s)
 +\sum_{p^k\le X}{\Lambda(p^k)\over p^{k/2}}
       \mathcal J_{k\log p}(q,s)
 -{1\over2}\langle q,s\rangle_{\mu_K},\\
 \mathcal T_X(q,s)
 &:=\sum_{p^k>X}{\Lambda(p^k)\over p^{k/2}}
       \mathcal J_{k\log p}(q,s).
                                                               \tag{5}
\end{aligned}
\]

Then

\[
 \boxed{\mathcal A_X=\mathcal A_\infty-\mathcal T_X,
 \qquad \mathcal T_X\succeq0,}                    \tag{6}
\]

and \(X\le Y\) implies

\[
 \mathcal A_X\preceq\mathcal A_Y\preceq\mathcal A_\infty. \tag{7}
\]

Let

\[
 r_j={K^{(2j)}\over K}-4^{-j},\qquad
 \mathcal R_J=\operatorname {span}\{r_1,\ldots,r_J\},
 \qquad
 \mathcal R=\overline{\bigcup_J\mathcal R_J}.       \tag{8}
\]

The complete radical identity and its polarization give

\[
 \boxed{\mathcal A_\infty(r,f)=0
 \quad(r\in\mathcal R).}                           \tag{9}
\]

Choose nested finite-dimensional Galerkin spaces

\[
 V_1\subset V_2\subset\cdots
 \subset\mathcal R^\perp\cap\mathcal H_0.          \tag{10}
\]

They may be elementary zero-mode spaces, finite CCM model spaces after
projection away from the radical, or any explicit form-core exhaustion.
Only (10) is used in the finite algebra.

## 2. Strict negativity on the finite radical

Fix bases of \(V_M\) and \(\mathcal R_J\). Let

\[
 \mathbf T^{VV},\qquad
 \mathbf T^{VR},\qquad
 \mathbf T^{RR}                                    \tag{11}
\]

be the corresponding blocks of the omitted-tail Gram matrix
\(\mathcal T_X\), and let \(\mathbf H_M\) be the Gram matrix of
\(\mathcal A_\infty|_{V_M}\).

### Lemma 1 — The radical tail block is positive definite

For every finite \(X\) and \(J\),

\[
 \boxed{\mathbf T^{RR}\succ0.}                     \tag{12}
\]

#### Proof

Take a nonzero \(r=\sum_{j=1}^Jc_jr_j\). If
\(\mathcal T_X(r,r)=0\), every omitted nonnegative atom vanishes. For an
omitted prime \(p>X\), positivity of \(K(x)K(x-\log p)\) gives

\[
 r(x)=r(x-\log p)                                  \tag{13}
\]

almost everywhere and hence everywhere by analyticity.

This is impossible. If \(j_0\) is the largest index with
\(c_{j_0}\ne0\), the leading \(m=1\) theta term shows that

\[
 \sum_{j=1}^Jc_j{K^{(2j)}(x)\over K(x)}
\]

is, to leading order as \(x\to+\infty\), a nonconstant polynomial in
\(e^{2x}\) whose highest term comes from \(j_0\). It is unbounded and
cannot be periodic. Hence every nonzero vector in \(\mathcal R_J\) has
strictly positive tail energy. Finite dimensionality proves (12).
\(\square\)

By (6), (9), and (12), the finite-head Gram matrix on
\(V_M\oplus\mathcal R_J\) is

\[
 \boxed{
 \mathbf A_{M,J,X}=
 \begin{pmatrix}
  \mathbf H_M-\mathbf T^{VV} &-\mathbf T^{VR}\\
  -\mathbf T^{RV}&-\mathbf T^{RR}
 \end{pmatrix}.}                                  \tag{14}
\]

Its radical block has exactly \(J\) negative eigenvalues.

## 3. Exact finite inertia matching

Define the positive tail short

\[
 \mathbf T_{X,/\mathcal R_J}
 :=\mathbf T^{VV}
  -\mathbf T^{VR}(\mathbf T^{RR})^{-1}\mathbf T^{RV}
 \succeq0,                                        \tag{15}
\]

and the maximal radical anti-short

\[
 \boxed{
 \mathbf S_{M,J,X}
 :=\mathbf H_M-\mathbf T_{X,/\mathcal R_J}.}       \tag{16}
\]

Equivalently, for \(v\in V_M\),

\[
 v^*\mathbf S_{M,J,X}v
 =\sup_{r\in\mathcal R_J}\mathcal A_X(v+r,v+r).    \tag{17}
\]

### Theorem 2 — Finite inertia criterion

\[
\boxed{
\begin{aligned}
 n_-(\mathbf A_{M,J,X})
   &=J+n_-(\mathbf S_{M,J,X}),\\
 n_0(\mathbf A_{M,J,X})
   &=n_0(\mathbf S_{M,J,X}),\\
 n_+(\mathbf A_{M,J,X})
   &=n_+(\mathbf S_{M,J,X}).
                                                               \tag{18}
\end{aligned}}
\]

Consequently,

\[
 \boxed{
 n_-(\mathbf A_{M,J,X})=J
 \quad\Longleftrightarrow\quad
 \mathbf S_{M,J,X}\succeq0.}                       \tag{19}
\]

#### Proof

The lower-right block in (14) is invertible by Lemma 1. Block Gaussian
congruence diagonalizes (14) into

\[
 \mathbf S_{M,J,X}\oplus(-\mathbf T^{RR}).         \tag{20}
\]

Sylvester's law of inertia and (12) prove (18)--(19). Formula (17) is the
same completion of the square. \(\square\)

The force-bearing finite matrix inequality is exactly

\[
 \boxed{
 \mathbf T^{VV}
 -\mathbf T^{VR}(\mathbf T^{RR})^{-1}\mathbf T^{RV}
 \preceq\mathbf H_M.}                              \tag{21}
\]

It retains the literal \(\Lambda(p^k)\), Gamma, the threshold, every
selected mode, and every selected radical correction.

### Corollary 3 — A finite match certifies the completed sign

If (19) holds, then

\[
 \boxed{\mathbf H_M\succeq0.}                     \tag{22}
\]

Indeed, the tail short is nonnegative and

\[
 \mathbf H_M
 =\mathbf S_{M,J,X}+\mathbf T_{X,/\mathcal R_J}.
\]

Thus one successful finite inertia match proves the completed sign on that
mode space. No \(X\to\infty\) passage is needed after (19) has been
certified.

## 4. The mode--prime--radical staircase

Define the excess negative index

\[
 \kappa(M,J,X)
 :=n_-(\mathbf A_{M,J,X})-J
 =n_-(\mathbf S_{M,J,X})\ge0.                     \tag{23}
\]

### Theorem 4 — Three monotonicities

\[
\boxed{
\begin{array}{lll}
 X\uparrow&\Longrightarrow&\kappa(M,J,X)\downarrow,\\
 M\uparrow&\Longrightarrow&\kappa(M,J,X)\uparrow,\\
 J\uparrow&\Longrightarrow&\kappa(M,J,X)\downarrow.
\end{array}}                                      \tag{24}
\]

Once \(\kappa(M,J,X)=0\), it remains zero at every larger prime cutoff.

#### Proof

Increasing \(X\) increases \(\mathbf A_{M,J,X}\) in Loewner order, so its
negative index cannot increase. The radical block stays negative
definite, so that index cannot fall below \(J\).

Increasing \(M\) enlarges the trial space; the old Gram matrix is a
principal compression of the new one. Its negative index cannot decrease.

Finally,

\[
 \mathcal T_{X,/\mathcal R_J}(v)
 =\inf_{r\in\mathcal R_J}\mathcal T_X(v+r)         \tag{25}
\]

decreases when \(\mathcal R_J\) grows. Therefore
\(\mathbf S_{M,J,X}\) increases in Loewner order and its negative index
cannot increase. \(\square\)

Put

\[
 X_*(M,J)
 =\inf\{X:\kappa(M,J,X)=0\}\in[2,\infty].          \tag{26}
\]

Then

\[
 \boxed{
 X_*(M+1,J)\ge X_*(M,J),\qquad
 X_*(M,J+1)\le X_*(M,J).}                          \tag{27}
\]

This is the exact form of the moving-head observation. The atom \(7\)
can finish one row while a new mode opens the next.

## 5. Quantitative cofinal schedules

Let \(\mathbf N_M\) be the norm Gram matrix on \(V_M\), and define

\[
 \delta_M
 =\lambda_{\min}\!\left(
 \mathbf N_M^{-1/2}\mathbf H_M\mathbf N_M^{-1/2}
 \right).                                         \tag{28}
\]

Document 106.67 proves, for each fixed \(M\),

\[
 0\preceq\mathbf T^{VV}
 \preceq C_Me^{-cX}\mathbf N_M.                   \tag{29}
\]

The constant is independent of \(J\). Since a short never exceeds its
unshorted form,

\[
 0\preceq\mathbf T_{X,/\mathcal R_J}
 \preceq\mathbf T^{VV}.                            \tag{30}
\]

### Theorem 5 — Effective strict-gap schedule

If \(\delta_M>0\) and

\[
 C_Me^{-cX}<\delta_M,                              \tag{31}
\]

then, for every finite \(J\),

\[
 \boxed{
 \mathbf S_{M,J,X}\succ0,\qquad
 n_-(\mathbf A_{M,J,X})=J.}                       \tag{32}
\]

#### Proof

Equations (16), (28)--(30) give

\[
 \mathbf S_{M,J,X}
 \succeq(\delta_M-C_Me^{-cX})\mathbf N_M\succ0.
\]

Apply Theorem 2. \(\square\)

Solving (31) gives (2). The growth of \(X(M)\) is governed by the mode
conditioning hidden in \(C_M\) and the completed finite gap \(\delta_M\).
No fixed cutoff follows unless both are controlled uniformly.

## 6. Vanishing compensated inertia

For \(\varepsilon>0\), shift only the mode block:

\[
 \mathbf A_{M,J,X}^{(\varepsilon)}
 =\mathbf A_{M,J,X}
 +\varepsilon
 \begin{pmatrix}\mathbf N_M&0\\0&0\end{pmatrix}.   \tag{33}
\]

The radical block remains negative definite, and Theorem 2 gives

\[
\boxed{
 n_-(\mathbf A_{M,J,X}^{(\varepsilon)})=J
 \quad\Longleftrightarrow\quad
 \mathbf S_{M,J,X}\succeq-\varepsilon\mathbf N_M.} \tag{34}
\]

### Theorem 6 — Cofinal compensated criterion

Assume that \(\bigcup_MV_M\) is a form core of the radically shorted
complement. The following are equivalent.

1. \(\mathcal A_\infty\succeq0\) on that complement.
2. For every sequence \(\varepsilon_M\downarrow0\), there are cofinal
   schedules \(J(M)\uparrow\infty\) and \(X(M)\uparrow\infty\) such that

   \[
    n_-\!\left(
    \mathbf A_{M,J(M),X(M)}^{(\varepsilon_M)}
    \right)=J(M)
    \qquad(M\ge1).                                 \tag{35}
   \]

When 1 holds, it is enough to choose

\[
 C_Me^{-cX(M)}<\varepsilon_M.                     \tag{36}
\]

#### Proof

Assume 1. Then \(\mathbf H_M\succeq0\). Equations (29)--(30) and (36)
give

\[
 \mathbf S_{M,J,X(M)}+\varepsilon_M\mathbf N_M\succ0.
\]

Equation (34) gives (35). The cutoffs may be enlarged to make both
schedules increasing, because matching persists under increasing \(X\),
and any prescribed cofinal \(J(M)\) is allowed.

Conversely, (34) and (16) imply

\[
 \mathbf H_M\succeq-\varepsilon_M\mathbf N_M.      \tag{37}
\]

Fix \(v\in V_{M_0}\). Apply (37) at every \(M\ge M_0\) and let
\(M\to\infty\). Then \(\mathcal A_\infty(v,v)\ge0\). Form-core density and
closedness extend the inequality to the complete complement. \(\square\)

With the moving/model identification, this complete floor is the RH
closure. Without it, Theorem 6 proves the sign on the selected Galerkin
closure.

## 7. Positive moving averages cannot improve the largest head

Let \(X_i\le X_*\), \(\alpha_i\ge0\), and
\(\sum_i\alpha_i=1\). Then

\[
 \overline{\mathbf A}
 :=\sum_i\alpha_i\mathbf A_{M,J,X_i}
 \preceq\mathbf A_{M,J,X_*}.                      \tag{38}
\]

Hence

\[
 \boxed{
 n_-(\overline{\mathbf A})
 \ge n_-(\mathbf A_{M,J,X_*}).}                   \tag{39}
\]

A Cesaro, exponential, trimmed, or other positive moving average can
stabilize numerical evaluation, but it cannot reach inertia matching
before the largest head does. The correct signal-processing analogue is a
nested filter bank, not an average of independent estimators.

## 8. Loewner/interlacing do not force matching

Let \(t_X,s_X>0\) decrease to zero and compare

\[
 \mathbf A_X^+
 =\begin{pmatrix}\delta-t_X&0\\0&-s_X\end{pmatrix},
 \qquad
 \mathbf A_X^-
 =\begin{pmatrix}-\delta-t_X&0\\0&-s_X\end{pmatrix},
 \qquad\delta>0.                                  \tag{40}
\]

Both families have Loewner-positive increments, one strictly negative
radical direction at every finite \(X\), and a vanishing tail. But
\(\mathbf A_X^+\) eventually has negative index \(1\), while
\(\mathbf A_X^-\) has negative index \(2\) for every \(X\). The difference
is exactly the sign of the completed quotient entry \(\pm\delta\).

Thus Loewner order proves monotonicity of the excess index but cannot prove
that it reaches zero. In the Riemann problem the missing input is (21), or
equivalently (35) cofinally.

## 9. Audit against CCM and the existing phase

The finite inertia match is not already supplied by self-adjointness.

1. **CCM finite quotient.** CCM subtracts the moving least Ritz value at
   each semilocal level and quotients by the resulting one-dimensional
   moving radical. Positivity of that shifted quotient is built into the
   construction. Matrix (14) is instead evaluated at the fixed threshold
   \(1/2\) and uses the exact Riemann radical. Self-adjointness gives real
   eigenvalues, not (1).
2. **Paper 39.** Equation (19.14) assumes
   \[
   \lambda_1(\mathcal D_N)<\kappa_N<\lambda_2(\mathcal D_N)
   \]
   before applying its rank-one determinant criterion. This is the
   \(J=1\) ancestor of inertia matching, not a proof of it.
3. **106.25.** The asymptotic-inertia lemma shows that a qualitative
   complementary floor plus a vanishing residual excludes a macroscopic
   negative branch. It does not derive that floor from a finite head.
4. **106.63 and 106.68.** The former proves that the ordinary lower short
   is unbounded at every proper head; the latter introduces the maximal
   anti-short and gives Haynsworth at one fixed head. The new content here
   is the three-parameter staircase, its schedule, and the compensated
   criterion.
5. **106.71.** The filter-bank theorem controls the omitted tail and
   isolates the negative-channel contraction. Theorem 2 is its
   radical-adapted inertia coordinate; it does not remove that contraction.

A semantic search over the project for inertia, negative index,
Haynsworth, radical, cofinal head, and finite quotient found no earlier
theorem combining (18), (24), and (35). This is a repository audit, not a
novelty claim for the finite-dimensional Haynsworth algebra.

## 10. Exact next theorem

Choose an explicit nested Galerkin exhaustion and prove, using the literal
ordinary values \(\Lambda(p^k)=\log p\), that there are schedules

\[
 M\longmapsto(J(M),X(M),\varepsilon_M),\qquad
 J(M),X(M)\uparrow\infty,\quad
 \varepsilon_M\downarrow0                         \tag{41}
\]

for which

\[
 \boxed{
 n_-\!\left(
 \mathbf A_{M,J(M),X(M)}
 +\varepsilon_M
 \begin{pmatrix}\mathbf N_M&0\\0&0\end{pmatrix}
 \right)=J(M).}                                   \tag{42}
\]

Equivalently, prove

\[
 \boxed{
 \mathbf T^{VV}
 -\mathbf T^{VR}(\mathbf T^{RR})^{-1}\mathbf T^{RV}
 \preceq\mathbf H_M+\varepsilon_M\mathbf N_M.}     \tag{43}
\]

The cutoff error in (43) is already bounded by
\(C_Me^{-cX(M)}\mathbf N_M\). The remaining term is the completed signed
floor, the same compact central channel isolated in 106.71. An off-line
orbit keeps an excess negative direction for every \(J\) and \(X\); a
proof of (42) on a form-core exhaustion excludes that orbit and closes the
quotient floor.
