# 106.118 — Signed Abel quadrature and the variation gate

## 1. Purpose and verdict

The compensated physical source has the exact Stieltjes form

\[
 d\sigma(u)
 =e^{-u/2}d\{\psi(e^u)-e^u\}
  +\frac{e^{-5u/2}}{1-e^{-2u}}\,du.
\]

This note performs Abel summation without separating primes, Gamma and the
pole by an absolute estimate.  The result is a finite, convention-free
quadrature formula

\[
 \int_0^\infty J(u)\,d\sigma(u)
 =-\int_0^\infty D(u)J'(u)\,du
  +\int_0^\infty r_\Gamma(u)J(u)\,du,
\]

where \(D\) is the literal weighted prime discrepancy and
\(r_\Gamma>0\) is the completed Gamma remainder.

For compact oscillatory hybrid rows \(r_N=\chi\cos(Nx)\), the formula
proves the physical surplus at high spatial frequency: the signed
quadrature term is \(O(1)\), whereas the Gamma remainder is

\[
 \frac12\|K\chi\|_2^2\log N+O(1).
\]

This is the Abel-coordinate form of the already proved essential-threshold
coercivity.  It does not close the low-frequency physical surplus.

The same family gives a decisive obstruction to the natural next step.
On every fixed interval below the first prime,

\[
 \int |D(u)|\,|J_N'(u)|\,du\gg N,
\]

while the entire positive Gamma remainder is only \(O(\log N)\).  Thus no
uniform Abel proof may replace the signed integral by total variation, even
with an arbitrary fixed multiplicative constant.  The obstruction survives
the exact projection off any fixed finite radical block.  The signs of the
quadrature must be preserved globally; bounded variation destroys a factor
\(N/\log N\).

No zero location is used below.

## 2. Nonduplication audit

The nearest prior calculations are distinct.

1. 106.66 constructs finite-part first and second primitives of the whole
   compensated measure and proves that \(J'\) and \(J''\) have both signs.
   It does not isolate the locally finite prime discrepancy or quantify the
   loss from total variation.
2. 106.102 inserts heat profiles into the second finite-part primitive.  It
   records that heat does not imply convexity, but gives no oscillatory
   variation witness.
3. 106.109 performs Gaussian Stieltjes summation on individual and
   aggregated theta fibres.  Its obstruction is the negative cumulative
   drift between prime powers, not the \(N/\log N\) variation loss below.
4. 106.47 proves the essential threshold by local Gamma compactness and PNT
   tail quadrature.  The high-frequency theorem below is its exact
   common-displacement/Abel realization, not a second proof of the missing
   low spectrum.

## 3. The finite weighted prime discrepancy

Define

\[
 \boxed{
 D(U)
 :=\sum_{\log n\leq U}\frac{\Lambda(n)}{\sqrt n}
   -2(e^{U/2}-1),\qquad U\geq0,}
 \tag{1}
\]

with the right-continuous convention at prime powers, and put

\[
 \boxed{
 r_\Gamma(u)
 :=\frac{e^{-5u/2}}{1-e^{-2u}}>0.}
 \tag{2}
\]

The Stieltjes differential of (1) is

\[
 dD(u)
 =\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
    \delta_{\log n}(du)-e^{u/2}\,du
 =e^{-u/2}d\{\psi(e^u)-e^u\}.
 \tag{3}
\]

Consequently

\[
 \boxed{d\sigma=dD+r_\Gamma(u)\,du.}
 \tag{4}
\]

Unlike the finite-part primitive of the full Gamma density, \(D(0)=0\)
and \(D\) is locally finite.  Before the first prime one has the exact
formula

\[
 \boxed{
 D(u)=-2(e^{u/2}-1)<0,
 \qquad 0<u<\log2.}
 \tag{5}
\]

### Theorem 1 — Exact signed Abel formula

Let \(J\) be an admissible translation-smooth displacement profile with

\[
 J(0)=0,\qquad D(U)J(U)\longrightarrow0
 \quad(U\to\infty).
 \tag{6}
\]

Then

\[
\boxed{
 \int_0^\infty J(u)\,d\sigma(u)
 =-\int_0^\infty D(u)J'(u)\,du
  +\int_0^\infty r_\Gamma(u)J(u)\,du.}
\tag{7}
\]

The two integrals are understood first with the same finite upper cutoff.
For compact smooth multipliers they converge separately.

#### Proof

Equation (4) gives

\[
 \int_0^U J\,d\sigma
 =\int_0^U J\,dD+\int_0^U r_\Gamma J\,du.
\]

Stieltjes integration by parts, \(D(0)J(0)=0\), and (6) give (7) after
the common limit. \(\square\)

The point is that (7) still retains the actual signs of the prime
quadrature error.  The immediately sufficient absolute estimate

\[
 \boxed{
 \int_0^\infty |D(u)|\,|J'(u)|\,du
 \leq\int_0^\infty r_\Gamma(u)J(u)\,du}
 \tag{8}
\]

would prove the physical surplus, but is much stronger than (7).

## 4. Compact oscillatory hybrid rows

Choose a nonzero real even cutoff

\[
 \chi\in C_c^\infty(\mathbb R)
\]

and put

\[
 r_N(x)=\chi(x)\cos(Nx),\qquad N=1,2,\ldots.
 \tag{9}
\]

Its displacement profile is

\[
 J_N(u)
 =\int_{\mathbb R}K(x)K(x-u)
   |r_N(x)-r_N(x-u)|^2\,dx.
 \tag{10}
\]

Define, for \(u\) in a fixed compact interval,

\[
\begin{aligned}
 A(u)
 &:=\frac12\int K(x)K(x-u)
   \{\chi(x)^2+\chi(x-u)^2\}\,dx,\\
 B(u)
 &:=\int K(x)K(x-u)\chi(x)\chi(x-u)\,dx.
\end{aligned}
\tag{11}
\]

### Lemma 2 — Uniform oscillatory profile

For every compact interval \(I\subset(0,\infty)\) and every \(M\geq1\),

\[
\boxed{
 J_N(u)=A(u)-B(u)\cos(Nu)+O_{I,M}(N^{-M})}
\tag{12}
\]

uniformly for \(u\in I\), and

\[
\boxed{
 J_N'(u)=NB(u)\sin(Nu)+O_I(1).}
\tag{13}
\]

#### Proof

Expand both cosine squares and their cross product.  The nonoscillatory
terms are precisely (11).  Every remaining term is an integral of a
smooth compactly supported amplitude against \(e^{\pm2iNx}\).  Repeated
integration by parts in \(x\) gives (12), uniformly with all fixed
\(u\)-derivatives on \(I\).  Differentiating (12) gives (13).
\(\square\)

Choose a closed interval

\[
 I=[a,b]\subset(0,\log2)
\tag{14}
\]

small enough that the supports of \(\chi(\cdot)\) and
\(\chi(\cdot-u)\) overlap for every \(u\in I\).  Positivity of \(K\)
then gives

\[
 \inf_{u\in I}B(u)=b_I>0,
 \qquad
 \inf_{u\in I}|D(u)|=d_I>0.
 \tag{15}
\]

### Theorem 3 — Linear variation blowup

For the rows (9),

\[
 \boxed{
 \int_I|D(u)|\,|J_N'(u)|\,du\geq c_I N}
 \tag{16}
\]

for all sufficiently large \(N\), with \(c_I>0\).

#### Proof

By (13)--(15),

\[
 \int_I|D||J_N'|
 \geq Nd_Ib_I\int_I|\sin(Nu)|\,du-O_I(1).
\]

The last integral tends to \(2|I|/\pi\).  This proves (16).
\(\square\)

## 5. The positive Gamma remainder has only logarithmic size

At the origin,

\[
 r_\Gamma(u)=\frac1{2u}+O(1).
 \tag{17}
\]

Moreover,

\[
 A(0)=B(0)=C_\chi,
 \qquad
 C_\chi:=\int_{\mathbb R}K(x)^2\chi(x)^2\,dx>0.
 \tag{18}
\]

The mean-value theorem and the boundedness of \(r_N\) give the uniform
estimate

\[
 J_N(u)\leq C\min\{1,N^2u^2\},
 \qquad 0<u\leq1.
 \tag{19}
\]

For \(u\geq1\), compact support of \(\chi\) and the
double-exponential tail of \(K\) give

\[
 J_N(u)\leq C\exp\{-c e^u\}.
 \tag{20}
\]

### Theorem 4 — Exact Gamma asymptotic

\[
\boxed{
 \int_0^\infty r_\Gamma(u)J_N(u)\,du
 =\frac{C_\chi}{2}\log N+O_\chi(1).}
\tag{21}
\]

#### Proof

Fix a small \(u_0>0\).  The expansion used in Lemma 2, now uniformly down
to \(u=0\), gives

\[
 J_N(u)
 =C_\chi\{1-\cos(Nu)\}
  +O(u)+O_M(uN^{-M})
\tag{22}
\]

uniformly in the \(du/u\)-integrable sense.  The extra factor \(u\) in the
last remainder follows because the exact profile and its oscillatory
expansion both vanish at \(u=0\); differentiate once in \(u\) and integrate
by parts sufficiently many times in \(x\).
Equations (17), (19) and the classical identity

\[
 \int_0^{u_0}\frac{1-\cos(Nu)}{u}\,du
 =\log N+O_{u_0}(1)
\tag{23}
\]

give the main term in (21).  Equations (19)--(20) bound the remaining
range uniformly. \(\square\)

For the obstruction alone, the weaker upper bound

\[
 \int_0^\infty r_\Gamma J_N\,du=O(\log N)
\tag{24}
\]

follows immediately by splitting (19) at \(u=N^{-1}\).

Combining (16) and (24) proves

\[
\boxed{
 \frac{\int|D|\,|J_N'|}
      {\int r_\Gamma J_N}
 \longrightarrow\infty.}
\tag{25}
\]

Thus (8), and even the same estimate with any fixed constant on its
right-hand side, is false.

## 6. Signed quadrature cancels the linear variation

The failure of (8) does not signal a negative physical form.  It measures
exactly the cancellation destroyed by total variation.

### Lemma 5 — Uniform signed quadrature bound

\[
 \boxed{\left|\int_0^\infty J_N(u)\,dD(u)\right|=O_\chi(1).}
 \tag{26}
\]

#### Proof

From (3),

\[
 \int J_N\,dD
 =\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}J_N(\log n)
  -\int_0^\infty e^{u/2}J_N(u)\,du.
\tag{27}
\]

The second term is uniformly bounded by (19)--(20).  The part of the
first sum with \(\log n\) in a fixed compact interval contains finitely
many terms and \(J_N\) is uniformly bounded.  On the remaining tail,
(20), with the corresponding translated compact-support estimate, is
summable against the aggregate von Mangoldt mass. \(\square\)

Theorems 1, 4 and Lemma 5 give the actual high-frequency surplus:

\[
\boxed{
 \int_0^\infty J_N\,d\sigma
 =\frac{C_\chi}{2}\log N+O_\chi(1)>0}
\tag{28}
\]

for all sufficiently large \(N\).  Thus Abel summation succeeds only while
the signed quadrature is kept intact.

## 7. Stability under a fixed finite radical anti-short

Let

\[
 \mathcal R_M=\mathrm{span}\,\{r_1,\ldots,r_M\},
 \qquad r_j=K^{(2j)}/K,
\tag{29}
\]

and let \(\Pi_M^{\mathscr E}\) denote orthogonal projection onto
\(\mathcal G\mathcal R_M\) in the complete source-gradient Hilbert space.
Write

\[
 \widetilde r_N
 =r_N-\sum_{j=1}^M c_{j,N}r_j,
\qquad
\mathcal G\widetilde r_N
=(I-\Pi_M^{\mathscr E})\mathcal G r_N.
\tag{30}
\]

### Lemma 6 — Finite anti-short does not remove the witness

For fixed \(M\),

\[
 c_{j,N}=O_{A,M}(N^{-A})\quad\text{for every }A>0,
 \qquad 1\leq j\leq M.
\tag{31}
\]

Consequently

\[
\begin{aligned}
 \int_I|D|\,|J_{\widetilde r_N}'|
   &\geq c_{I,M}N,\\
 \int r_\Gamma J_{\widetilde r_N}
   &=\frac{C_\chi}{2}\log N+O_M(1),\\
 \int J_{\widetilde r_N}\,dD&=O_M(1).
\end{aligned}
\tag{32}
\]

#### Proof

Polarized radical equality gives the exact cross identity

\[
 \langle\mathcal G r_N,\mathcal G r_j\rangle
 =\langle D_\mu r_N,D_\mu r_j\rangle.
\tag{33}
\]

Indeed, the difference is the polarized completed Weil form and
\(Kr_j=K^{(2j)}\) annihilates it at every nontrivial zero.  The right side
of (33) is a polar covariance.  Its densities contain
\(hK r_j=hK^{(2j)}\), whose derivatives decrease double exponentially.
Repeated integration by parts against \(\chi e^{iNx}\) therefore gives

\[
 |\langle\mathcal G r_N,\mathcal G r_j\rangle|
 =O_{A,j}(N^{-A})
\tag{34}
\]

The displayed radical block has already removed the constant \(r_0=1\);
its fixed source Gram matrix is nonsingular modulo constants, so (31)
follows.  On \(I\), differentiating a cross profile containing one
fixed radical costs at most \(O(N)\); multiplication by (31) is
superpolynomially small.  Equations (16), (21) and (26) therefore persist
with the stated errors. \(\square\)

Lemma 6 applies to every fixed finite hybrid enlargement used before the
cofinal radical limit.  It does not assert uniformity when \(M\) grows with
\(N\); that genuinely global anti-short remains load-bearing.

## 8. Consequence for heat and hybrid rows

Compact smooth rows belong to the translation-smooth hybrid form core, and
the heat-core exhaustion of 106.98 approximates them in the complete
source form norm.  The family above proves two complementary facts.

1. The signed Abel coordinate does prove the surplus in the
   high-frequency sector, with logarithmic coercivity.
2. Any attempt to make that proof uniform by controlling
   \(-\int DJ'\) through weighted total variation loses a full factor
   \(N/\log N\), even after any fixed finite radical anti-short.

The heat evolution does not repair the loss: the scalar heat profile is
not an autonomous variation-diminishing flow (106.110), and 106.115 proves
that the folded physical semigroup is not stochastically monotone.

Therefore a successful Abel successor must estimate the **signed**
quadrature

\[
 -\int_0^\infty D(u)J_t'(u)\,du
\]

directly on the globally anti-shorted heat covariance.  It cannot pass
through \(|D|\,|J_t'|\), bounded variation, monotonicity, or a finite
martingale filtration.

## 9. Status

Proved here:

* the finite, convention-free discrepancy decomposition \(d\sigma=dD+
  r_\Gamma du\);
* the exact signed Abel identity (7);
* linear growth of weighted absolute variation on explicit compact hybrid
  rows;
* logarithmic Gamma coercivity and bounded signed prime discrepancy on the
  same rows;
* strict high-frequency physical surplus;
* persistence of the \(N/\log N\) obstruction after every fixed finite
  radical anti-short.

Not proved here:

\[
 \int_0^\infty J_t(u)\,d\sigma(u)\geq-o(\mathrm{Tr}\,\Gamma_t)
\]

along a cofinal globally anti-shorted heat sequence.  The remaining
quadrature theorem must preserve the signs of \(D\) at all prime-power
jumps and continuous intervals simultaneously.
