# 106.137 — Literal prime-ratio cocycle and the passive-path stop gate

## 1. Purpose and verdict

After 106.135 and 106.138, a natural proposal is to use pairs of literal
prime-power delays to transport the negative pre-prime continuum onto
positive arithmetic edges.  The first such edge is

\[
 \log 3-\log 2=\log(3/2),
\]

which lies inside the interval where the residual displacement density is
negative.  More generally, differences of prime-power logarithms are dense.

This note performs the corresponding cocycle calculation without a triangle
inequality.  The conclusions are exact.

1.  A pair of delays has an exact ratio-edge identity.  Summing it gives a
    positive weighted graph variance and an explicit Schur complement.
2.  That Schur complement has the wrong structural role for the physical
    surplus: it is the conditional dispersion which occurs with a negative
    coefficient in the star-current formula of 106.49.
3.  The single edge \(\log(3/2)\), and in fact every finite family of
    prime-ratio paths, fails to observe a continuum interval.  The falsifier
    is an exact two-component character and retains all theta weights.
4.  Passing to all positive prime pairs does not repair this: the raw passive
    ratio bank diverges cofinally by spatial escape.  Centering it by the PNT
    continuum produces a signed, not a Hilbert-positive, block.

Therefore the literal ratio cocycle does not by itself produce an enlarged
positive block whose Schur complement is \(G_J-\delta_J\).  It identifies
precisely what a successful successor must add: the complete mean-periodic
anti-short must enter before the cofinal signed centering, and the resulting
ordinary-prime--Gamma block must prove a genuine alignment estimate.  A
finite passive delay network cannot supply that estimate.

No assertion about the sign of the complete Riemann surplus is made.

## 2. Nonduplication audit

The closest prior calculations are the following.

* 106.22 rewrites the completed Weil form on the cone of translation
  metrics and gives a one-frequency counterexample to generic negative-type
  transport.  It does not derive the exact prime-ratio cocycle below.
* 106.50 separates product and ratio triangles in the complete cluster
  current.  The present note isolates the ratio channel in the exact
  Stieltjes coordinate \(J_u\), computes its Schur complement, and gives a
  cofinal path falsifier.
* 106.128 proves that covariant cyclic triangles retain a signed
  \(h\)-divergence and that a polar connection merely moves the missing sign.
  The present result is compatible with that gate: it shows directly why a
  flat passive path enlargement cannot remove the sign.
* 106.134 proves that a fixed finite delay bank cannot control the physical
  Abel connection.  The character argument below is a different statement:
  it rules out continuum observability by any finite graph of literal
  prime-ratio edges, even when no triangle inequality is used.

Thus the result is not a new positivity mechanism.  It is the exact stop
gate for the proposed literal-ratio passive realization.

## 3. Exact two-delay cocycle

Let \(K>0\) be Riemann's even theta kernel and, for a scalar or
Hilbert-valued multiplier \(q\), put

\[
 d_aq(x)=q(x)-q(x-a),
 \qquad
 J_a(q)=\int_{\mathbb R}K(x)K(x-a)\|d_aq(x)\|^2\,dx.
 \tag{1}
\]

### Theorem 1 — Ratio-edge identity

For every \(a,b\geq0\),

\[
\boxed{
 J_{|a-b|}(q)
 =\int_{\mathbb R}K(x-a)K(x-b)
   \|d_aq(x)-d_bq(x)\|^2\,dx.}
 \tag{2}
\]

#### Proof

Assume \(a\geq b\) and set \(y=x-b\).  Then

\[
 d_aq(x)-d_bq(x)=q(y)-q(y-(a-b))=d_{a-b}q(y),
\]

while

\[
 K(x-a)K(x-b)=K(y-(a-b))K(y).
\]

Substitution gives (2).  Symmetry gives the case \(b>a\). \(\square\)

Formula (2) retains the complete relative phase.  No use of
\(\|v-w\|^2\leq2\|v\|^2+2\|w\|^2\) has been made.

## 4. The exact finite graph and its Schur complement

Let \(a_1,\ldots,a_M\) be a finite family of delays and let
\(\lambda_j>0\).  At a fixed base point define

\[
 \kappa_j(x)=\lambda_jK(x-a_j),\quad
 v_j(x)=d_{a_j}q(x),
\]

and

\[
 W(x)=\sum_j\kappa_j(x),\qquad
 S(x)=\sum_j\kappa_j(x)\|v_j(x)\|^2,
 \qquad
 B(x)=\sum_j\kappa_j(x)v_j(x).
 \tag{3}
\]

### Theorem 2 — Literal ratio variance

One has

\[
\boxed{
 \frac12\sum_{j,k}\lambda_j\lambda_k
 J_{|a_j-a_k|}(q)
 =\int_{\mathbb R}\{W(x)S(x)-\|B(x)\|^2\}\,dx.}
 \tag{4}
\]

Pointwise, when \(W(x)>0\),

\[
\boxed{
 S(x)-\frac{\|B(x)\|^2}{W(x)}
 =\inf_z\sum_j\kappa_j(x)\|v_j(x)-z\|^2.}
 \tag{5}
\]

Thus (4) is exactly \(W\) times the Schur complement obtained by
eliminating one common regression variable.

More explicitly, with

\[
 D_x=\mathrm{diag}(\kappa_1(x),\ldots,\kappa_M(x)),
 \qquad
 \boldsymbol\kappa_x=(\kappa_1(x),\ldots,\kappa_M(x))^{\mathsf T},
\]

the canonical passive delay block is

\[
 \mathbb B_x=
 \begin{pmatrix}
  D_x&-\boldsymbol\kappa_x\\
  -\boldsymbol\kappa_x^*&W(x)
 \end{pmatrix}\succeq0.
 \tag{5a}
\]

Its Schur complement in the common port is

\[
 D_x-\frac{\boldsymbol\kappa_x\boldsymbol\kappa_x^*}{W(x)},
 \tag{5b}
\]

whose quadratic form on \((v_1,\ldots,v_M)\) is the right side of (5).
Thus \(\mathbb B_x\) is the elementary positive enlargement supplied by
the literal path cocycle; it realizes dispersion, not the physical
surplus.

#### Proof

Insert (2), expand the difference square, and interchange the finite sums
and the integral.  The two diagonal terms give \(2WS\), and the two cross
terms give \(2\|B\|^2\).  This proves (4).  Completing the square in
\(z\) proves (5). \(\square\)

For the literal arithmetic bank one takes

\[
 a_j=\log n_j,qquad
 \lambda_j=\frac{\Lambda(n_j)}{\sqrt{n_j}}.
 \tag{6}
\]

Then (4) contains all ratios \(\log(n_j/n_k)\) with their exact ordinary
von Mangoldt weights.

The sign lesson is important.  The finite passive block gives the
nonnegative conditional variance (5).  But the exact star-current surplus
106.49(15) contains

\[
 -\frac14W(x)\mathcal V_x
 \tag{7}
\]

and asks the coherent current to dominate it.  Hence adjoining passive
ratio paths does not prove the needed sign: it realizes the dispersion
which must be dominated.  Shorting further passive path variables can only
produce another nonnegative graph Schur complement; it cannot reverse the
coefficient in (7).  To obtain the physical surplus exactly, an additional
diagonal storage term must dominate (5).  That domination is the projection
alignment theorem, not a consequence of the path realization.

## 5. The first prime ratio does not observe an interval

Let

\[
 H(u)=(K*K)(u)=\int_{\mathbb R}K(x)K(x-u)\,dx>0.
 \tag{8}
\]

Consider the exact two-component real character

\[
 Q_\xi(x)=(\cos\xi x,\sin\xi x).
 \tag{9}
\]

Then

\[
\boxed{
 J_u(Q_\xi)=2(1-\cos\xi u)H(u).}
 \tag{10}
\]

Take \(\delta=\log(3/2)\) and \(\xi_N=2\pi N/\delta\).  Equation (10)
gives

\[
 J_\delta(Q_{\xi_N})=0
 \qquad(N\geq1).
 \tag{11}
\]

On the other hand, if \(I\subset(0,\infty)\) has positive length and
\(g\in L^1(I)\) is positive almost everywhere, the Riemann--Lebesgue lemma
gives

\[
\boxed{
 \lim_{N\to\infty}\int_Ig(u)J_u(Q_{\xi_N})\,du
 =2\int_Ig(u)H(u)\,du>0.}
 \tag{12}
\]

In particular, (12) applies to every compact subinterval of the negative
pre-prime interval in 106.138, with \(g(u)=e^{u/2}\).  Therefore no
inequality of the form

\[
 \int_Ie^{u/2}J_u(q)\,du\leq C J_{\log(3/2)}(q)
 \tag{13}
\]

can hold on the common smooth multiplier core, for any finite \(C\).

This is not caused by taking an absolute value.  The ratio edge vanishes
because the two delayed amplitudes agree exactly.

The same falsifier exists in the real-even scalar sector.  Put

\[
 q_\xi^{\rm e}(x)=\cos\xi x
\]

and change variables \(z=x-u/2\).  Then

\[
\boxed{
 J_u(q_\xi^{\rm e})
 =4\sin^2(\xi u/2)
 \int_{\mathbb R}K(z+u/2)K(z-u/2)\sin^2(\xi z)\,dz.}
 \tag{14}
\]

Thus \(J_\delta(q_{2\pi N/\delta}^{\rm e})=0\) exactly.  Uniform
Riemann--Lebesgue on a compact displacement interval gives

\[
 \lim_{\xi\to\infty}\int_Ig(u)J_u(q_\xi^{\rm e})\,du
 =\int_Ig(u)H(u)\,du>0.
 \tag{15}
\]

Indeed, the family
\(K(z+u/2)K(z-u/2)\), \(u\in I\), is compact in \(L^1(dz)\).
Its Fourier transform therefore tends to zero uniformly in \(u\), and
the remaining factor \(2\sin^2(\xi u/2)\) is handled by the ordinary
Riemann--Lebesgue lemma.  Hence the obstruction is not an artifact of
using a complex or parity-mixed feature.

## 6. Every finite prime-ratio path family has the same defect

### Theorem 3 — Finite path observability fails

Let \(\delta_1,\ldots,\delta_R>0\) be arbitrary, let \(c_r\geq0\), and
let \(I,g\) be as in (12).  There is a sequence \(\xi_k\to\infty\) such
that

\[
 \sum_{r=1}^Rc_rJ_{\delta_r}(q^{\rm e}_{\xi_k})\longrightarrow0,
 \tag{16}
\]

while

\[
 \int_Ig(u)J_u(q^{\rm e}_{\xi_k})\,du
 \longrightarrow\int_Ig(u)H(u)\,du>0.
 \tag{17}
\]

The same result holds if finitely many anchor edges \(J_{a_j}\) are added.

#### Proof

Simultaneous Dirichlet recurrence supplies \(\xi_k\to\infty\) for which

\[
 e^{i\xi_k\delta_r}\longrightarrow1
 \qquad(1\leq r\leq R).
\]

If there is an exact common period, take its integer multiples; otherwise
the usual pigeonhole approximants have an unbounded subsequence.  Equation
(14) proves (16), and (15) proves (17).  Anchor delays are
included in the same simultaneous recurrence. \(\square\)

Adding constants to \(q\) does not change any \(J_u(q)\).  Consequently the
falsifier survives exact orthogonal projection off the constant mode: one
subtracts the weighted mean of \(q^{\rm e}_{\xi_k}\), and
(16)--(17) are unchanged.

Theorem 3 does not survive an arbitrary projection off the complete
Riemann radical, because subtracting nonconstant radical modes changes the
increments.  This is precisely why a successful theorem must use the
complete cofinal anti-short before making the path estimate.

## 7. Why the positive all-prime path bank is not a cofinal storage

One might try to evade Theorem 3 by using every prime pair.  The raw
positive ratio bank, however, has no finite cofinal limit on the character
core.

Fix \(\xi\ne0\).  Restrict the pair sum in (4) to primes
\(X<p,q\leq2X\).  Since

\[
 |\log(p/q)|\leq\log2,
\]

the continuous positive function \(H\) has a positive minimum on that
interval.  The prime number theorem and partial summation give

\[
 \sum_{X<p\leq2X}\frac{\log p}{\sqrt p}
 \sim2(\sqrt2-1)\sqrt X.
 \tag{18}
\]

Moreover the normalized twisted sum converges to the nonconstant Mellin
average

\[
 e^{i\xi\log X}
 \frac{\int_1^2t^{-1/2+i\xi}\,dt}
      {\int_1^2t^{-1/2}\,dt},
 \tag{19}
\]

whose modulus is strictly smaller than one.  Equations (10), (18), and
(19) imply

\[
 \frac12\sum_{X<p,q\leq2X}
 \frac{\log p\log q}{\sqrt{pq}}
 J_{|\log p-\log q|}(Q_\xi)
 \geq c_\xi X
 \tag{20}
\]

for all sufficiently large \(X\), with \(c_\xi>0\).  Thus the raw passive
ratio storage diverges along every nonzero character.

The divergence is spatial: at a fixed base point the theta factors suppress
remote delays, but integration over the whole line follows the bank as its
center moves to \(\log X\).  This is the same cofinal escape which forbids
taking the positive prime and continuous PNT pieces separately.

## 8. Signed PNT centering and the Krein sign

The only literal centering compatible with 106.138 is the signed measure

\[
 d\mu_Y(a)
 =\sum_{\log n\leq Y}\frac{\Lambda(n)}{\sqrt n}
       \delta_{\log n}(da)
  -e^{a/2}\mathbf1_{[0,Y]}(a)\,da,
 \tag{21}
\]

with the common endpoint convention.  Formula (4) extends algebraically
to every finite signed measure.  Namely, define

\[
\begin{aligned}
 W_\mu(x)&=\int K(x-a)\,d\mu(a),\\
 S_\mu(x)&=\int K(x-a)\|d_aq(x)\|^2\,d\mu(a),\\
 B_\mu(x)&=\int K(x-a)d_aq(x)\,d\mu(a).
\end{aligned}
 \tag{22}
\]

Then

\[
\boxed{
 \frac12\iint J_{|a-b|}(q)\,d\mu(a)d\mu(b)
 =\int\{W_\mu S_\mu-\|B_\mu\|^2\}\,dx.}
 \tag{23}
\]

For positive \(\mu\), (23) is the passive Schur complement (5).  For the
PNT-centered measure (21), both \(W_\mu\) and \(S_\mu\) are signed.  The
right side is not a positive block.  In the flat centered limit
\(W_\mu=0\), its surviving term is in fact

\[
 -\int\|B_\mu(x)\|^2\,dx,
 \tag{24}
\]

with the opposite sign from passive storage.

Thus the cofinal operation needed to make the all-prime bank finite changes
the Hilbert block into a signed, or Krein, block.  Gamma absorption from
106.135 remains a genuine positive resource, but it does not change the
algebraic sign in (23).  Proving that the complete Gamma--prime--pole
realization is positive after the exact radical anti-short is therefore a
new theorem; it is not furnished by the ratio cocycle.

## 9. Consequence for the proposed port-Hamiltonian realization

The natural passive realization of literal delays has the following exact
outcome.

* At finite cutoff, its shorted energy is the positive conditional
  dispersion (5).
* The physical cluster surplus contains the negative of that dispersion,
  coupled to the coherent current as in 106.49(15).
* No finite graph of ratio paths observes the negative continuum, by
  Theorem 3.
* The raw all-prime passive graph diverges, by (20).
* The unique PNT centering which removes that divergence produces the
  signed identity (23), not a positive Hilbert block.

Consequently there is no exact identification

\[
 G_J-\delta_J
 =\text{Schur complement of the finite or raw-cofinal passive ratio bank}.
 \tag{25}
\]

Any such identification omits either the coherent-current term, the PNT
continuum, or the sign change caused by cofinal centering.

The surviving possibility is narrower and genuinely cofinal: construct a
single enlarged ordinary-prime--Gamma--pole block **after** the complete
mean-periodic radical anti-short, and prove its positivity with the signed
PNT centering already inside the block.  Equivalently, one must prove the
projection alignment estimate of 106.49(22), now allowed to spend the
explicit Gamma margin of 106.135.  The ratio identities (2), (4), and (23)
are exact bookkeeping for that theorem, but they do not supply its sign.
