# 106.148 — Cofinal multi-atom Riccati flatness gate

## 1. Purpose and result

The finite staircase already has an exact one-atom Kalman update, an exact
block Stieltjes flow, and an exact radical-conditioned tail gain.  A remaining
possibility is that the *simultaneous* interaction of different literal
prime-power chords might carry an additional signed holonomy which is absent
from every one-parameter calculation.  Such a term would be genuinely
nonlocal in the chord length and could, in principle, couple the ordinary
von Mangoldt weights to the Gamma and polar source before the final square.

This note computes that interaction without diagonalizing, separating, or
reordering the chord bank.  On every finite seeded heat/hybrid row, after the
exact radical variables have been included, the full multi-atom Riccati
one-form is

\[
 \Omega=\sum_{\alpha}\|r_\alpha(\mathbf t)\|^2\,dt_\alpha,
 \tag{1}
\]

where \(\alpha=p^k\) runs through literal prime powers and
\(r_\alpha\) is the *jointly adapted* response of that chord.  The main
identity is

\[
 \boxed{\Omega=d\sigma.}
 \tag{2}
\]

Consequently the connection is flat.  More explicitly,

\[
 \boxed{
 \partial_\beta\partial_\alpha\sigma
 =-2\operatorname {Re}
 \left\langle
 A^{-1/2}U_\beta^*r_\beta,
 A^{-1/2}U_\alpha^*r_\alpha
 \right\rangle ,}
 \tag{3}
\]

and, for every real finitely supported vector \(s=(s_\alpha)\),

\[
 \boxed{
 D^2\sigma(\mathbf t)[s,s]
 =-2\left\|
 A^{-1/2}\sum_\alpha s_\alpha U_\alpha^*r_\alpha
 \right\|^2\le0.}
 \tag{4}
\]

All cross-prime terms are present in (3)--(4), but they are exactly the
adaptation loss.  Their integral is path independent.  Thus changing the
order of the prime powers, grouping them into blocks, inserting signed loops,
or using a cofinal Riccati schedule cannot create an extra reserve: every such
path has the same endpoint

\[
 \boxed{\sigma_\infty=-\delta_J+G_J.}
 \tag{5}
\]

The result is an exact stop gate for *Riccati path holonomy*.  It does not
exclude a nonlinear arithmetic inequality which uses the actual theta phases
before the Schur minimization, and it does not prove or disprove the physical
surplus.

## 2. Nonduplication audit

The calculation is adjacent to, but not contained in, the following earlier
results.

| Document | Existing result | Additional issue settled here |
|---|---|---|
| 106.78 | One literal atom has a positive Kalman innovation | Does not compute mixed derivatives between distinct atoms |
| 106.85 | A whole fixed block scaled by one scalar has a Stieltjes flow | Restricts the parameter space to one ray |
| 106.88 | Consecutive block gains telescope | Does not identify the multi-parameter curvature or rule out loop holonomy |
| 106.89 | The exact radical-conditioned endpoint is \(-\delta_J+G_J\) | Supplies the endpoint used in (5), but not the full source-parameter connection |
| 106.91 | Finite augmented determinants increase to \(G_J\) | Supplies cofinal compactness, but no signed cross-atom differential formula |
| 106.143 | Finite dynamic IQCs fail and exact multipliers are null IQCs | Does not classify source-parameter Riccati paths |
| 106.144 | Decomposable chord rotations are isometric | Does not address a common regression mixing different chord lengths |
| 106.145--106.146 | The global chord constraint and canonical null-IQC leave \(PJP\) | Identify the force-bearing block; the present note computes every cofinal Riccati path inside that block |

The new statement is the exact multi-parameter Hessian (3), its negative
semidefinite square (4), and the resulting flatness theorem.  It closes the
specific proposal that cross-prime Riccati curvature may supply a positive
holonomy not seen by one-atom or one-ray updates.

## 3. The seeded augmented physical row

Fix one finite heat/hybrid mode row and a finite exact-radical space.  Work
after the old Gamma, retained-prime, polar, and threshold terms have been
assembled and after enough literal omitted atoms have been inserted to make
the preceding augmented block strictly positive.  This is the seeded region
of 106.91.

Let \(E_-\) be the finite coefficient space containing the old-mode and
radical adaptation variables.  Let \(\phi\) denote the affine new mode.
Write the seeded Hermitian matrix as

\[
 H_0=
 \begin{pmatrix}
 A_0&c_0\\ c_0^*&h_0
 \end{pmatrix},
 \qquad A_0\succ0.
 \tag{6}
\]

The matrix \(H_0\) contains jointly:

1. the complete Gamma form on the row;
2. every retained ordinary prime power;
3. the polar subtraction and the threshold term;
4. the finite exact-radical anti-short data; and
5. the finite seed required to make the augmented adaptation block
   invertible.

The radical basis is held fixed along the auxiliary source path.  It is an
adaptation coordinate, not a claim that the interpolated operator has the
same radical for every \(\mathbf t\).  The physical radical identity is used
at the completed endpoint.  Thus the covariant moving-radical derivative
audited in 106.125 is neither assumed to vanish nor omitted here.

For each additional literal prime power \(\alpha=p^k\), put

\[
 u_\alpha=\log\alpha,
 \qquad
 w_\alpha={\Lambda(\alpha)\over\sqrt\alpha}
 ={\log p\over p^{k/2}}.
 \tag{7}
\]

Let \(D_\alpha\) be the complete theta displacement feature

\[
 (D_\alpha q)(x)
 =\sqrt{w_\alpha K(x)K(x-u_\alpha)}
 \{q(x)-q(x-u_\alpha)\}.
 \tag{8}
\]

No midpoint approximation is made in (8).  Its target Hilbert space may
retain the divisor, fractional, and central-crossing components separately;
their orthogonal direct sum gives the same formulas below.  In the affine
basis \(E_-\oplus\mathbb C\phi\), write

\[
 D_\alpha=[\,U_\alpha\ \ v_\alpha\,].
 \tag{9}
\]

For a finite set \(F\) of additional prime powers and parameters
\(\mathbf t=(t_\alpha)_{\alpha\in F}\in[0,\infty)^F\), define

\[
\begin{aligned}
 A(\mathbf t)
 &=A_0+\sum_{\alpha\in F}t_\alpha U_\alpha^*U_\alpha,\\
 c(\mathbf t)
 &=c_0+\sum_{\alpha\in F}t_\alpha U_\alpha^*v_\alpha,\\
 h(\mathbf t)
 &=h_0+\sum_{\alpha\in F}t_\alpha\|v_\alpha\|^2.
\end{aligned}
 \tag{10}
\]

Since \(A_0\succ0\), one has \(A(\mathbf t)\succ0\) throughout the
positive orthant.  Put

\[
 a(\mathbf t)=A(\mathbf t)^{-1}c(\mathbf t),
 \qquad
 r_\alpha(\mathbf t)=v_\alpha-U_\alpha a(\mathbf t),
 \tag{11}
\]

and let

\[
 \sigma(\mathbf t)
 =h(\mathbf t)-c(\mathbf t)^*A(\mathbf t)^{-1}c(\mathbf t).
 \tag{12}
\]

This is the exact Schur pivot after all atoms in \(F\) have been inserted
with strengths \(t_\alpha\), while every old and radical coordinate is
allowed to readapt jointly.

## 4. Exact multi-atom Riccati system

### Theorem 1 — Gradient, mixed curvature, and concavity

For every \(\alpha,\beta\in F\),

\[
 \boxed{
 \partial_\alpha a
 =A^{-1}U_\alpha^*r_\alpha,}
 \tag{13}
\]

\[
 \boxed{
 \partial_\beta r_\alpha
 =-U_\alpha A^{-1}U_\beta^*r_\beta,}
 \tag{14}
\]

and

\[
 \boxed{
 \partial_\alpha\sigma=\|r_\alpha\|^2.}
 \tag{15}
\]

The mixed second derivative is (3), and the Hessian obeys (4).  In
particular, \(\sigma\) is jointly concave on \([0,\infty)^F\).

#### Proof

The normal equation is

\[
 A(\mathbf t)a(\mathbf t)=c(\mathbf t).
 \tag{16}
\]

Differentiate it with respect to \(t_\alpha\):

\[
 U_\alpha^*U_\alpha a+A\,\partial_\alpha a
 =U_\alpha^*v_\alpha.
 \tag{17}
\]

Rearranging (17) gives (13).  Differentiating the definition of
\(r_\alpha\) and inserting (13) with index \(\beta\) proves (14).

Differentiate (12).  The two terms containing
\(\partial_\alpha a\) cancel by (16), leaving

\[
\begin{aligned}
 \partial_\alpha\sigma
 &={\|v_\alpha\|^2}
 -2\operatorname {Re}\langle U_\alpha a,v_\alpha\rangle
 +\|U_\alpha a\|^2\\
 &=\|v_\alpha-U_\alpha a\|^2
 =\|r_\alpha\|^2,
\end{aligned}
 \tag{18}
\]

which is (15).  Now (14) gives

\[
\begin{aligned}
 \partial_\beta\partial_\alpha\sigma
 &=2\operatorname {Re}
   \langle\partial_\beta r_\alpha,r_\alpha\rangle\\
 &=-2\operatorname {Re}
   \langle U_\alpha A^{-1}U_\beta^*r_\beta,r_\alpha\rangle,
\end{aligned}
 \tag{19}
\]

which is (3).  The expression is symmetric in \(\alpha,\beta\), as a
mixed derivative must be.

For a real vector \(s\), sum (19) against \(s_\alpha s_\beta\).  The
result is

\[
\begin{aligned}
 D^2\sigma[s,s]
 &=-2\operatorname {Re}
 \left\langle
 \sum_\beta s_\beta A^{-1/2}U_\beta^*r_\beta,
 \sum_\alpha s_\alpha A^{-1/2}U_\alpha^*r_\alpha
 \right\rangle\\
 &=-2\left\|
 A^{-1/2}\sum_\alpha s_\alpha U_\alpha^*r_\alpha
 \right\|^2.
\end{aligned}
 \tag{20}
\]

This proves (4) and joint concavity. \(\square\)

The off-diagonal entries in (3) need not be negative.  Only the complete
Hessian square (4) has a sign.  Therefore no termwise sign can be assigned
to a pair of distinct prime powers before their common regression is kept.

## 5. Flatness and path independence

### Theorem 2 — Exact Riccati one-form

Let \(\gamma:[0,1]\to[0,\infty)^F\) be piecewise \(C^1\).  Then

\[
 \boxed{
 \sigma(\gamma(1))-\sigma(\gamma(0))
 =\int_0^1\sum_{\alpha\in F}
 \dot\gamma_\alpha(s)\,
 \|r_\alpha(\gamma(s))\|^2\,ds.}
 \tag{21}
\]

In particular, every closed path has zero integral:

\[
 \boxed{\oint_\gamma\Omega=0.}
 \tag{22}
\]

#### Proof

The chain rule and (15) give

\[
 {d\over ds}\sigma(\gamma(s))
 =\sum_\alpha\dot\gamma_\alpha(s)
 \|r_\alpha(\gamma(s))\|^2.
 \tag{23}
\]

Integration proves (21).  If the endpoints agree, its left side is zero,
which proves (22). \(\square\)

Theorem 2 includes paths with decreasing or signed parameter velocities as
long as the path remains in the domain where \(A(\mathbf t)\succ0\).
Consequently a signed Riccati loop cannot leave a residual null correction.
Blocking and reordering correspond to different monotone polygonal paths
with the same endpoints, so they also have identical total gain.

There is a useful concavity inequality.  For \(0\le\mathbf s\le\mathbf t\),

\[
 \sum_\alpha(t_\alpha-s_\alpha)
 \|r_\alpha(\mathbf t)\|^2
 \le \sigma(\mathbf t)-\sigma(\mathbf s)
 \le
 \sum_\alpha(t_\alpha-s_\alpha)
 \|r_\alpha(\mathbf s)\|^2.
 \tag{24}
\]

The upper and lower bounds are the tangent inequalities for a concave
function.  They identify the exact meaning of cross-prime interaction:
readaptation can only reduce the response seen later.  It supplies no
positive surplus beyond the endpoint pivot.

## 6. Exact two-atom sign falsifier

The absence of an atom-pair sign is already visible in the smallest
possible model.  Let the old coefficient and both observation spaces be
one-dimensional, and take

\[
 A_0=1,\qquad c_0=0,\qquad h_0=-\delta,\qquad
 U_1=U_2=1.
 \tag{25}
\]

First choose

\[
 v_1=1,\qquad v_2=-1.
 \tag{26}
\]

At \(\mathbf t=0\), one has \(a=0\), \(r_1=1\), and \(r_2=-1\).
Formula (3) gives

\[
 \boxed{
 D^2\sigma(0)
 =\begin{pmatrix}-2&2\\2&-2\end{pmatrix}\preceq0.}
 \tag{27}
\]

Thus the mixed coefficient is strictly positive.  If instead
\(v_1=v_2=1\), then

\[
 \boxed{
 D^2\sigma(0)
 =\begin{pmatrix}-2&-2\\-2&-2\end{pmatrix}\preceq0,}
 \tag{28}
\]

and the same mixed coefficient is strictly negative.  Positive literal
weights can be prescribed arbitrarily in this example: absorb
\(w_i^{1/2}\) into \(U_i,v_i\), or rescale the displayed unweighted
features by \(w_i^{-1/2}\).  In particular one may label the two atoms by
\(2\) and \(3\) and use the exact positive weights
\(\log2/\sqrt2\) and \(\log3/\sqrt3\).

This is not a counterexample to the Riemann theta displacement system.
It is the minimal algebraic falsifier of any argument which assigns a
fixed favorable sign to a distinct-atom Riccati cross term using only
positive atom weights and a positive old block.  One atom has no mixed
coefficient; two atoms are therefore minimal.

## 7. Cofinal passage

Let \(\alpha_1,\alpha_2,\ldots\) enumerate the omitted ordinary prime
powers.  On a fixed seeded finite heat/hybrid row assume:

1. \(A_0\succeq a_0I\) for some \(a_0>0\);
2. the positive feature series
   \(\sum_jD_{\alpha_j}^*D_{\alpha_j}\) converges in operator norm on the
   finite row; and
3. the completed preceding block remains positive.

Condition 2 is supplied on each fixed row by the established
double-exponential theta overlap.  Let \(F_N\uparrow\{\alpha_j:j\ge1\}\)
be any cofinal sequence of finite sets and put

\[
 H_N=H_0+\sum_{\alpha\in F_N}D_\alpha^*D_\alpha.
 \tag{29}
\]

### Theorem 3 — Cofinal order independence

The corresponding matrices, regression coefficients, and pivots converge
in norm:

\[
 A_N\to A_\infty,\qquad
 a_N\to a_\infty,\qquad
 \sigma_N\to\sigma_\infty.
 \tag{30}
\]

Moreover, for every ordering or finite blocking of the same literal atoms,
the exact adaptive gains telescope to

\[
 \boxed{
 \sum_{j\ge1}g_j
 =\sigma_\infty-\sigma_0,}
 \tag{31}
\]

and the value is independent of that ordering or blocking.  If the row is
the radical-conditioned row of 106.89, then

\[
 \boxed{
 \sigma_\infty-\sigma_0=G_J,
 \qquad
 \sigma_\infty=-\delta_J+G_J.}
 \tag{32}
\]

#### Proof

Norm convergence of the positive feature series gives norm convergence of
all four blocks of \(H_N\).  Since \(A_N\succeq A_0\succeq a_0I\), inversion
is uniformly continuous on this family, and hence

\[
 A_N^{-1}c_N\to A_\infty^{-1}c_\infty.
 \tag{33}
\]

Substitution in the Schur complement proves (30).

For a finite prefix, Theorem 2 says that the sum of the gains along any
polygonal insertion path is exactly \(\sigma_N-\sigma_0\).  Taking
\(N\to\infty\) and using (30) proves (31).  Equations (32) are precisely
the radical-conditioned source balance 106.89(22)--(23). \(\square\)

If the radical dimension also grows, Theorem 3 applies at each finite
radical level \(J\).  Passing \(J\to\infty\) requires the same cofinal
form convergence and uniform invertibility used by the complete anti-short.
No additional Riccati term appears in that passage.  If uniform
invertibility fails, the Riccati coordinate itself degenerates; one cannot
claim a bounded cofinal correction from (13)--(21).

For a simultaneous infinite path \(t\mapsto(t,t,\ldots)\), equations
(21) and (31) pass to the limit whenever the derivative series is locally
uniformly summable.  This follows on a fixed row from the theta bound and
\(A(t)^{-1}\preceq A_0^{-1}\).  Without that summability, the safe
definition is the finite cofinal limit (29)--(31), which is independent of
the exhaustion.

## 8. Null-IQC interpretation

Document 106.146 constructs the exact literal constraint \(\mathcal L\)
for the prime, Gamma, and polar chord ports and proves

\[
 \ker\mathcal L=Z\{q:(hq)*K=0\}.
 \tag{34}
\]

On a finite row its canonical null correction eliminates every
off-physical block and leaves

\[
 J+\mathcal L^*Y+Y^*\mathcal L
 =\operatorname {diag}(PJP,I).
 \tag{35}
\]

The source parameters in this note are inserted in the fixed physical
\(q\)-coordinate *after* the range (34) has been identified.  Equivalently,
one uses the unweighted master-chord ports and places \(t_\alpha w_\alpha\)
in the positive signature operator.  This is congruent to putting
\(\sqrt{t_\alpha w_\alpha}\) in the copy port, but it avoids differentiating
a moving ambient port normalization.  In particular, no derivative of the
physical range projection is silently discarded.

Taking the new-mode Schur complement of the resulting compressed form gives
exactly \(\sigma(\mathbf t)\) above.  Equations (2) and (22) therefore prove:

\[
 \boxed{
 \text{every Riccati null correction generated solely by a source path
 has zero loop contribution on the physical range}.}
 \tag{36}
\]

This statement does not say that all source-specific null corrections are
trivial.  A correction may use a new nonlinear identity among the actual
theta phases before the common Schur minimization.  What (36) excludes is
more precise: no correction formed by reordering, blocking, continuously
rescaling, or looping through the already-known positive literal chord
increments can produce a new endpoint sign.

## 9. Exact stress tests

### 9.1 Radical saturation

Before the complete radical is removed, an exact nonconstant radical vector
has completed physical value zero.  For that row, every proper finite head
is negative and the cofinal positive gain equals the entire finite deficit:

\[
 \sigma_\infty=0,
 \qquad
 \sum_jg_j=\delta.
 \tag{37}
\]

Thus no strict surplus can follow merely from positivity, infinitely many
atoms, strict one-atom observability, or a favorable ordering.  This is the
literal Riemann saturation mechanism of 106.63 and 106.87.  It is removed,
not contradicted, by the complete anti-short.

### 9.2 Off-line conditional falsifier

Counterfactually, if an off-line zero orbit exists, 106.93 gives a literal
mean-periodic vector with negative completed physical value.  Theorem 3
then forces every cofinal Riccati schedule to have the same negative
endpoint:

\[
 \sigma_\infty=-\delta_J+G_J<0.
 \tag{38}
\]

No source ordering or signed loop can change (38).  This is a conditional
stress test, not an assertion that such a vector exists.

## 10. Result and surviving mechanism

The exact strongest Riccati statement is now multi-parameter and cofinal:

\[
 \boxed{
 \Omega=d\sigma,
 \qquad
 D^2\sigma[s,s]
 =-2\left\|A^{-1/2}\sum_\alpha
 s_\alpha U_\alpha^*r_\alpha\right\|^2.}
 \tag{39}
\]

It retains distinct literal prime-power chords, the common old-mode and
radical regression, Gamma, retained primes, the pole, and the threshold.
The calculation proves that cross-prime Riccati interaction is adaptation
loss and that its connection has zero holonomy.

Therefore the following variants are closed as independent sign sources:

1. choosing a different ordering of literal prime powers;
2. changing the finite block partition;
3. continuously rescaling the same positive atom bank;
4. adding a signed loop while the preceding block remains positive; and
5. claiming a favorable pairwise sign for the mixed Riccati terms.

The surviving class is narrower and genuinely different.  One must prove a
nonlinear arithmetic inequality for the actual theta phases *before* the
common regression collapses them to (39), or construct a global signed
factorization of \(PJP\) which is not generated by a source-parameter
Riccati path.  The present theorem neither supplies nor falsifies such an
inequality.
