# 106.88 — Cumulative adaptive block selection

## Purpose and conclusion

Documents 106.85--106.86 identify the exact Stieltjes gain of one finite
prime block and the completed gain of the whole omitted tail.  This note
fills the intermediate step: it partitions the omitted ordinary prime
powers into consecutive finite blocks and accumulates their adaptive
innovations.

The result is stronger than asking one block to pay the entire initial
deficit.  If the initial Schur pivot is \(-\delta\), and the \(j\)-th
block has adaptive Stieltjes moments

\[
 R_j=\int d\nu_j,
 \qquad
 C_j=\int s\,d\nu_j,
\]

then after \(J\) blocks

\[
 \boxed{
 \sigma_J
 \ge -\delta+
 \sum_{j=1}^J\frac{R_j^2}{R_j+C_j}.}             \tag{1}
\]

Therefore a finite prefix crosses whenever

\[
 \boxed{
 \sum_{j\ge1}\frac{R_j^2}{R_j+C_j}>\delta.}       \tag{2}
\]

Because the summands are nonnegative, (2) automatically selects a finite
prefix.  No single block is required to satisfy
\(R_j^2>\delta(R_j+C_j)\) against the original deficit.

The criterion is sharp as a selection principle.  The Stieltjes structure,
literal positive von Mangoldt weights, theta summability, and nonzero
response of every atom do not force the strict surplus in (2).  An exact
threshold countermodel with the literal theta envelope has

\[
 \sum_j\frac{R_j^2}{R_j+C_j}=\delta,
\]

so every finite pivot is negative and the completed pivot is zero.  Thus
the remaining input is a **strict adaptive source--deficit estimate**, not
a further pigeonhole argument.

## 1. Consecutive adaptive blocks

Fix one staircase row and let its signed head be

\[
 H_0=
 \begin{pmatrix}A_0&c_0\\c_0^*&h_0\end{pmatrix},
 \qquad A_0\succ0,
 \qquad
 \sigma_0=h_0-c_0^*A_0^{-1}c_0=-\delta<0.         \tag{3}
\]

Enumerate the omitted prime powers increasingly and partition them into
consecutive finite blocks

\[
 \mathcal B_1,\mathcal B_2,\ldots .              \tag{4}
\]

The blocks can be single atoms, dyadic intervals, PNT relative intervals,
or any other consecutive exhaustion.  Let

\[
 \mathcal D_j=[\,U_j\ \ v_j\,]                    \tag{5}
\]

be the complete literal feature of \(\mathcal B_j\), including its
von Mangoldt weights.  After the first \(j-1\) blocks have been added,
write

\[
 H_{j-1}=
 \begin{pmatrix}A_{j-1}&c_{j-1}\\
 c_{j-1}^*&h_{j-1}
 \end{pmatrix},
 \qquad
 a_{j-1}=A_{j-1}^{-1}c_{j-1}.                    \tag{6}
\]

Since every block increment is positive semidefinite,

\[
 A_{j-1}\succeq A_0\succ0                       \tag{7}
\]

for every \(j\).  Define the adaptive response and regression operator

\[
 r_j=v_j-U_ja_{j-1},
 \qquad
 B_j=U_jA_{j-1}^{-1}U_j^*\succeq0.               \tag{8}
\]

Let \(\nu_j\) be the spectral measure of \(B_j\) at \(r_j\):

\[
 \nu_j(\Omega)=
 \langle r_j,E_{B_j}(\Omega)r_j\rangle.          \tag{9}
\]

Put

\[
 R_j=\|r_j\|^2=\int d\nu_j,
 \qquad
 C_j=\|A_{j-1}^{-1/2}U_j^*r_j\|^2
     =\int s\,d\nu_j.                            \tag{10}
\]

When \(R_j>0\), also put

\[
 \kappa_j=\frac{C_j}{R_j}.                       \tag{11}
\]

## 2. Exact telescoping theorem

### Theorem 1 — Cumulative adaptive innovation

Let \(\sigma_j\) be the last Schur pivot of \(H_j\).  Then

\[
 \boxed{
 \sigma_j-\sigma_{j-1}
 =g_j
 :=\langle r_j,(I+B_j)^{-1}r_j\rangle
 =\int\frac{d\nu_j(s)}{1+s}.}                    \tag{12}
\]

Consequently

\[
 \boxed{
 \sigma_J=-\delta+\sum_{j=1}^Jg_j.}              \tag{13}
\]

The sequence \(\sigma_J\) is nondecreasing.  If the blocks exhaust the
complete omitted tail, then

\[
 \boxed{
 \text{some finite prefix crosses}
 \quad\Longleftrightarrow\quad
 \sum_{j\ge1}g_j>\delta.}                         \tag{14}
\]

#### Proof

At stage \(j-1\), adding \(\mathcal D_j^*\mathcal D_j\) changes the
three matrix blocks by

\[
 A_{j-1}\mapsto A_{j-1}+U_j^*U_j,
 \quad
 c_{j-1}\mapsto c_{j-1}+U_j^*v_j,
 \quad
 h_{j-1}\mapsto h_{j-1}+\|v_j\|^2.              \tag{15}
\]

The block-Kalman identity, or the Woodbury formula applied to (15), gives

\[
 \sigma_j-\sigma_{j-1}
 =\langle r_j,
   (I+U_jA_{j-1}^{-1}U_j^*)^{-1}r_j\rangle,       \tag{16}
\]

which is the first equality in (12).  The spectral theorem gives the
integral form.  Summing (12) and using \(\sigma_0=-\delta\) proves (13).

Each \(g_j\ge0\), so the partial sums in (13) increase to the completed
gain.  If their limit is strictly larger than \(\delta\), a finite partial
sum is already larger than \(\delta\).  Conversely, a finite crossing
forces the limiting sum to be strictly larger than \(\delta\).  This
proves (14). \(\square\)

Equation (14) is the blockwise version of the complete-tail equivalence in
106.86.  Its role here is to preserve the separate adaptive moments of
each consecutive block.

## 3. Optimal cumulative moment bound

### Theorem 2 — Finite selection from two moments

For every \(J\),

\[
 \boxed{
 \sigma_J
 \ge -\delta+
 \sum_{j=1}^J\frac{R_j^2}{R_j+C_j}
 =-\delta+
 \sum_{\substack{1\le j\le J\\R_j>0}}
 \frac{R_j}{1+\kappa_j}.}                         \tag{17}
\]

Here a zero-response block contributes zero.  In particular, either of
the following conditions selects a finite crossing:

\[
 \sum_{j\ge1}\frac{R_j^2}{R_j+C_j}>\delta,        \tag{18}
\]

or, given explicit estimates \(R_j\ge L_j\ge0\) and
\(\kappa_j\le K_j\),

\[
 \boxed{
 \sum_{j\ge1}\frac{L_j}{1+K_j}>\delta.}          \tag{19}
\]

#### Proof

Document 106.85 proves the optimal Stieltjes moment bound

\[
 g_j=\int\frac{d\nu_j(s)}{1+s}
 \ge\frac{R_j^2}{R_j+C_j}.                       \tag{20}
\]

Insert (20) into the exact telescope (13) to obtain (17).  If the positive
series in (18) or (19) is larger than \(\delta\), one of its finite partial
sums is larger than \(\delta\); (17) then gives a finite crossing.
\(\square\)

The estimate is optimal block by block using only \((R_j,C_j)\), because
the equality example of 106.85 can be realized independently at every
stage.  Refining or coarsening the partition may change the numerical
lower bound, since both the adaptive residual and the preceding inverse
change, but every partition gives a valid certificate.

### Corollary 3 — Uniform leakage budget

If

\[
 C_j\le K R_j
 \qquad(j\ge1)                                    \tag{21}
\]

for one \(K\ge0\), then a finite prefix crosses as soon as

\[
 \boxed{
 \sum_{j\ge1}R_j>(1+K)\delta.}                   \tag{22}
\]

This separates the two estimates that a sampling argument must provide:
enough adaptive response mass and a bound for its old-mode leakage.

## 4. Relation with the one-block polynomial

For one block at a head whose remaining deficit is \(\delta_{j-1}\), the
two-moment certificate is

\[
 F_j
 =R_j^2-\delta_{j-1}(R_j+C_j)>0.                \tag{23}
\]

Requiring (23) for the first block is unnecessarily strong.  For example,
with \(U_j=0\), initial deficit \(\delta=1\), and three blocks with
\(R_1=R_2=R_3=0.4\), every block used alone at the initial head has

\[
 R_j^2-\delta R_j=-0.24<0,                       \tag{24}
\]

but the cumulative pivot after three blocks is

\[
 -1+0.4+0.4+0.4=0.2>0.                           \tag{25}
\]

Thus the correct pigeonhole object is the positive innovation series in
(13) or its lower series in (17), not the maximum of the isolated
one-block polynomials measured against the original deficit.

Conversely, if no finite prefix satisfies the cumulative two-moment
certificate, then every \(J\) obeys

\[
 \sum_{j=1}^J\frac{R_j}{1+\kappa_j}\le\delta.     \tag{26}
\]

This is the exact form of the missing budget.  Repartitioning cannot prove
that its left side exceeds \(\delta\) without an estimate linking the
actual source deficit to the omitted adaptive responses.

## 5. Dyadic and relative-window criterion

Take, for example,

\[
 \mathcal B_j
 =\{p^k:2^jX_0<p^k\le2^{j+1}X_0\}.               \tag{27}
\]

The same theorem applies without change.  If a sampling estimate gives

\[
 R_j\ge L_j
\]

and an adaptive regression estimate gives

\[
 C_j\le K_jR_j,                                   \tag{28}
\]

then

\[
 \sum_j\frac{L_j}{1+K_j}>\delta                 \tag{29}
\]

is a valid dyadic finite-selection criterion.

The relative-window PNT theorem of 106.84 supplies a lower bound of the
form \(L_j\) for each fixed spectral block.  It does not compare the sum
in (29) with \(\delta\), and its theta-weighted version loses the factor
\(e^{-2\pi\eta X}\) across a fixed relative width \(\eta\).  The Stieltjes
argument does not restore that lost factor: it only discounts each block
further by \((1+K_j)^{-1}\).

## 6. Sharp theta-envelope counterexample

The need for a strict source surplus can be seen while retaining positive
ordinary-prime weights, an exact theta-type envelope, strict atomwise
observability, and zero adaptive leakage.

Enumerate the ordinary prime powers as \(m_1<m_2<\cdots\), put

\[
 w_j=\frac{\Lambda(m_j)}{\sqrt{m_j}},
 \qquad
 \tau_j=w_je^{-2\pi m_j},
 \qquad
 S=\sum_{j\ge1}\tau_j<\infty,                    \tag{30}
\]

and fix \(\delta>0\).  Let

\[
 H_0=\begin{pmatrix}1&0\\0&-\delta\end{pmatrix},
 \qquad
 \alpha=\frac{\delta}{S}.                        \tag{31}
\]

For each \(j\), use a two-dimensional observation space with orthonormal
vectors \(e_{j,1},e_{j,2}\), and define the unweighted feature by

\[
 D_je_1=\sqrt{\alpha e^{-2\pi m_j}}\,e_{j,1},
 \qquad
 D_je_2=\sqrt{\alpha e^{-2\pi m_j}}\,e_{j,2}.     \tag{32}
\]

The literal weighted increment is

\[
 w_jD_j^*D_j=\alpha\tau_j I_2\succ0.             \tag{33}
\]

Thus every atom observes both coordinates injectively.  Since the old and
new response vectors in (32) are orthogonal,

\[
 C_j=0,
 \qquad
 R_j=g_j=\alpha\tau_j.                            \tag{34}
\]

For every finite \(J\),

\[
 \sigma_J
 =-\delta+\alpha\sum_{j=1}^J\tau_j<0,          \tag{35}
\]

whereas

\[
 \sigma_\infty
 =-\delta+\alpha S=0.                            \tag{36}
\]

Every finite consecutive union \(I\) has

\[
 R_I<\delta,
 \qquad C_I=0,
 \qquad
 F_I=R_I(R_I-\delta)<0                            \tag{37}
\]

when tested at the initial head.  The same statement holds after any
finite prefix, with \(\delta\) replaced by the remaining tail mass.

This model does not reproduce the physical theta displacement maps.  It
proves the exact structural limitation: Stieltjes positivity, the literal
von Mangoldt labels, theta summability, strict finite observability, and
even perfect orthogonality to the old response do not select a finite
crossing.  They are compatible with threshold saturation.

The constant \(\alpha\) displays sharpness.  If

\[
 \alpha S>\delta,                                 \tag{38}
\]

then a finite prefix crosses by monotone convergence.  If
\(\alpha S=\delta\), every finite prefix remains below zero and converges
to zero.  If \(\alpha S<\delta\), the completed pivot remains negative.

## 7. Surviving estimate

The exact remaining statement for the physical ordinary-prime theta
features is the strict surplus

\[
 \boxed{
 \sum_{j\ge1}
 \int_{[0,\infty)}\frac{d\nu_j(s)}{1+s}
 >\delta.}                                         \tag{39}
\]

A sufficient version accessible to finite estimates is

\[
 \boxed{
 \sum_{j\ge1}\frac{R_j^2}{R_j+C_j}>\delta.}       \tag{40}
\]

Once either strict inequality is proved, a finite crossing follows
without any further uniformity or cutoff argument.  Equality is not
enough.  Therefore the next force-bearing input must compare the physical
prime--Gamma source deficit with the cumulative adaptive theta response;
neither PNT sampling nor the Stieltjes representation makes that comparison
by itself.

## 8. Verification

The identities (12)--(17) are finite-dimensional Schur-complement and
spectral-theorem calculations.  The only limiting step is monotone
convergence of a nonnegative scalar series, justified by the established
theta-tail summability on each fixed mode block.

In the counterexample,

\[
 \sum_jw_jD_j^*D_j
 =\alpha S I_2=\delta I_2,
\]

so (35)--(36) follow by direct diagonal addition.  No floating-point
calculation is used.
